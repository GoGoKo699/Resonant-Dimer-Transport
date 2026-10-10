#!/usr/bin/env python3
"""Local-source dimer transport checks.

The analytical statements are in FOLLOWUP.md. Tests compare independent
representations and finite diagnostics; they do not certify infinite-volume
limits, literature priority, or a hardware operating window. The new support
module reuses this candidate's preserved scalar solver, never another project.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import unittest
import warnings
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad,IntegrationWarning
from scipy.linalg import eigh,expm
from scipy.special import roots_legendre
from scipy.sparse.linalg import LinearOperator,expm_multiply
from transport import dimer,pole,weight_integral,velocity_tail,relative_size,size_constant
warnings.simplefilter('error',IntegrationWarning)
REPORT={}


def continuum_grid(P,z,nq,times):
    """Independent Fourier-grid evolution; includes scattering and the pole."""
    q=2*np.pi*(np.arange(nq)+.5)/nq-np.pi
    A=np.abs(2*np.sin((q+P/2)/2))**z+np.abs(2*np.sin((q-P/2)/2))**z
    U=dimer.rest_threshold(z)
    def mv(x):
        x=np.asarray(x)
        return A*x-U*np.mean(x) if x.ndim==1 else A[:,None]*x-U*np.mean(x,axis=0)
    H=LinearOperator((nq,nq),matvec=mv,rmatvec=mv,matmat=mv,dtype=np.complex128)
    one=np.ones(nq)/np.sqrt(nq)
    vals=[]
    for t in times:
        state=expm_multiply((-1j*t)*H,one,traceA=-1j*t*(A.sum()-U))
        vals.append(np.vdot(one,state))
    return np.asarray(vals)


def band_characteristic(time,s,nodes=90):
    z=.75;h=s/(2*time)
    def EZ(p):
        p=(p+np.pi)%(2*np.pi)-np.pi
        if abs(p)<1e-14:return 0.,0.
        E,Z,_=pole(float(abs(p)),z)
        return E,Z
    points=sorted(set([0.,abs(h),np.pi-abs(h),np.pi]))
    x,w=roots_legendre(nodes);total=0.
    for lo,hi in zip(points[:-1],points[1:]):
        if hi<=lo:continue
        ps=(x+1)*(hi-lo)/2+lo
        val=[]
        for p in ps:
            Ep,Zp=EZ(p+h);Em,Zm=EZ(p-h)
            val.append(Zp*Zm*np.cos(time*(Ep-Em)))
        total+=(hi-lo)/2*np.dot(w,val)/np.pi
    return float(total)


class Checks(unittest.TestCase):
    def test_01_complete_real_space_vs_fiber(self):
        L=14;z=.75;U=dimer.rest_threshold(z)
        p=2*np.pi*np.arange(L)/L;x=np.arange(L)
        F=np.exp(1j*np.outer(x,p))/np.sqrt(L)
        eps=np.abs(2*np.sin(p/2))**z
        K=(F*eps)@F.conj().T
        V=np.diag((np.repeat(x,L)==np.tile(x,L)).astype(float))
        H=np.kron(K,np.eye(L))+np.kron(np.eye(L),K)-U*V
        lam,vec=eigh(H);init=np.zeros(L*L);init[0]=1
        weights=vec.conj().T@init
        rows=[]
        for time in (.37,2.,7.):
            exact=(vec@(np.exp(-1j*time*lam)*weights)).reshape(L,L)
            C=[];Cb=[];mass=[]
            for P in p:
                A=eps+np.abs(2*np.sin((P-p)/2))**z
                h=np.diag(A)-U/L*np.ones((L,L))
                e,w=eigh(h);overlap=np.sum(w,axis=0)/np.sqrt(L)
                spectral=abs(overlap)**2
                C.append(np.sum(spectral*np.exp(-1j*time*e)))
                Cb.append(spectral[0]*np.exp(-1j*time*e[0]));mass.append(spectral[0])
                resolvent=1/np.mean(1/(A-e[0]))
                residue=1/(U**2*np.mean(1/(A-e[0])**2))
                self.assertLess(abs(resolvent-U),3e-13)
                self.assertLess(abs(residue-spectral[0]),2e-13)
            site=np.fft.ifft(C);bound=np.fft.ifft(Cb)
            error=np.linalg.norm(site-np.diag(exact))
            self.assertLess(error,3e-13)
            self.assertAlmostEqual(np.sum(abs(bound)**2),np.mean(np.array(mass)**2),places=12)
            ac=site-bound
            lhs=np.sum(abs(abs(site)**2-abs(bound)**2))
            rhs=2*np.linalg.norm(bound)*np.linalg.norm(ac)+np.linalg.norm(ac)**2
            self.assertLessEqual(lhs,rhs+1e-13)
            rows.append({'time':time,'contact_amplitude_vector_error':float(error),'coincidence_probability':float(np.sum(abs(site)**2)),
                         'finite_ring_bound_coincidence_mass':float(np.sum(abs(bound)**2))})
        REPORT['independent_real_space']={'dimension':L*L,'cells':L,'z':z,'cases':rows,
            'scope':'Finite ring verifies normalization and exact decompositions, not late-time continuum loss; its P=0 eigenstate is not the infinite-line resonance.'}

    def test_02_relative_size_and_local_source_bound(self):
        z=.75;c=dimer.universal_root(z);B=1/(dimer.rest_threshold(z)**2*dimer.universal(c,z,True));size=size_constant(z)
        rows=[]
        for P in (.01,.001):
            E,Z,v=pole(P,z);sigma=relative_size(P,z)
            local=[]
            for R in (0,1,3):
                U=dimer.rest_threshold(z)
                amplitudes=np.array([U*np.sqrt(Z)*dimer.lattice_resolvent(E,P,z,r) for r in range(-R,R+1)])
                mass=np.vdot(amplitudes,amplitudes).real
                SR=sum((U*dimer.free_rest(r,z))**2 for r in range(-R,R+1))
                optimum=amplitudes/np.linalg.norm(amplitudes)
                self.assertAlmostEqual(abs(np.vdot(amplitudes,optimum))**2,mass,places=13)
                rng=np.random.default_rng(106+R)
                test=rng.normal(size=2*R+1)+1j*rng.normal(size=2*R+1);test/=np.linalg.norm(test)
                self.assertLessEqual(abs(np.vdot(amplitudes,test))**2,mass+1e-13)
                local.append({'R':R,'localmass':float(mass),'localmass_over_Z':float(mass/Z),'limiting_ratio':float(SR)})
            rows.append({'P':P,'residue':Z,'residue_over_power':Z/P**(2*z-1),'P_times_rms_size':P*sigma,'velocity':v,'local':local})
        self.assertLess(abs(rows[-1]['P_times_rms_size']-size),.02)
        self.assertLess(abs(rows[-1]['residue_over_power']-B),.002)
        self.assertLess(abs(rows[-1]['local'][-1]['localmass_over_Z']-rows[-1]['local'][-1]['limiting_ratio']),.006)
        REPORT['source_size']={'z':z,'universal_relative_size':size,'residue_coefficient':B,'cases':rows,
            'scope':'The finite-relative-support preparation bound and its attaining projection are exact; asymptotic conclusions use the proof, not these points.'}

    def test_03_velocity_tail_and_mass(self):
        z=.75;c=dimer.universal_root(z);B=1/(dimer.rest_threshold(z)**2*dimer.universal(c,z,True));exponent=(4*z-1)/(1-z)
        coefficient=B*B/(np.pi*(4*z-1))*(z*c)**exponent
        Wc=weight_integral(np.pi,z,True);Wb=weight_integral(np.pi,z,False)
        self.assertTrue(0<Wc<Wb<1)
        rows=[]
        for v in (1.,2.,3.):
            P,prob=velocity_tail(v,z)
            self.assertLess(abs(pole(P,z)[2]-v),2e-8)
            rows.append({'velocity_in_J_units':v,'near_zero_momentum_cutoff':P,'limiting_unconditioned_contact_tail':prob,
                         'large_velocity_leading_term':coefficient/v**exponent,'tail_over_leading_term':prob/(coefficient/v**exponent)})
        self.assertLess(abs(rows[-1]['tail_over_leading_term']-1),.03)
        # Numeric global monotonicity is a diagnostic only; high-velocity theorem does not need it.
        grid=np.linspace(.025,np.pi,65)
        vs=np.array([pole(float(p),z)[2] for p in grid])
        self.assertLess(float(np.max(np.diff(vs))),0.)
        self.assertLess(abs(vs[-1]),2e-13)
        REPORT['tail']={'z':z,'exponent':exponent,'asymptotic_coefficient':coefficient,'eventual_contact_mass':Wc,'bound_sector_mass':Wb,
            'cases':rows,'maximum_adjacent_velocity_increment_on_sampled_grid':float(np.max(np.diff(vs))),
            'numerical_caution':'Tail quadratures are not outward intervals. The asymptotic support/tail theorem does not assume global velocity monotonicity.'}

    def test_04_complete_fiber_evolution_continuum_control(self):
        times=[8.,32.,128.];rows=[]
        for P in (.3,1.):
            E,Z,_=pole(P)
            low=continuum_grid(P,.75,2048,times);high=continuum_grid(P,.75,4096,times)
            error=float(np.max(abs(low-high)))
            residual=abs(high-Z*np.exp(-1j*E*np.array(times)))
            self.assertLess(error,.003)
            self.assertLess(float(residual[-1]),.04)
            rows.append({'P':P,'times':times,'exact_grid_contact_amplitudes_real':high.real.tolist(),'exact_grid_contact_amplitudes_imag':high.imag.tolist(),
                         'amplitude_after_subtracting_infinite_line_pole':residual.tolist(),'grid_refinement_max_change':error})
        REPORT['scattering_diagnostic']={'max_fiber_grid_dimension':4096,'cases':rows,
            'scope':'Complete fiber dynamics, not a projected-band propagation. Finite sampling supports, but does not prove, the continuum Riemann-Lebesgue limit.'}

    def test_05_ballistic_characteristic_and_gapped_control(self):
        s=.4;z=.75
        # The small-P tail is integrable despite oscillating cos(s*v). Bound
        # its omitted contribution by its total coincidence weight.
        pmin=.003
        limit=quad(lambda p:pole(float(p),z)[1]**2*np.cos(s*pole(float(p),z)[2])/np.pi,pmin,np.pi,
                   epsabs=2e-9,epsrel=2e-9,limit=160)[0]
        omitted=weight_integral(pmin,z,True)
        self.assertLess(omitted,1e-6)
        rows=[]
        for time in (8.,32.,128.):
            value=band_characteristic(time,s,nodes=52)
            rows.append({'time':time,'coincidence_characteristic':value,'difference_from_cutoff_limit':abs(value-limit)})
        self.assertLess(rows[-1]['difference_from_cutoff_limit'],3e-5)
        self.assertLess(rows[-1]['difference_from_cutoff_limit'],rows[0]['difference_from_cutoff_limit'])
        # Fixed binding: quadratic low-P band and finite group velocity.
        U=1.3*dimer.rest_threshold(z);gapped=[]
        for P in (.001,.01,.1,1.,2.,np.pi):
            E,Z,v=pole(P,z,U);gapped.append({'P':P,'E':E,'Z':Z,'velocity':v})
        self.assertLess(gapped[0]['velocity'],gapped[1]['velocity'])
        self.assertLess(abs(gapped[-1]['velocity']),1e-13)
        REPORT['propagation']={'characteristic_frequency':s,'ray_measure_integral_excluding_tiny_region':float(limit),
           'omitted_region_mass_upper_bound':omitted,'cases':rows,'stronger_attraction':{'U':U,'cases':gapped},
           'scope':'Characteristic convergence checks an integrated velocity law, not a fitted front or an assertion of finite-time zero tails.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    if a.output.exists():p.error('Refusing to overwrite evidence')
    r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if r.wasSuccessful() else 'FAIL',test_groups=r.testsRun,prior_candidate_module_used='prior/dimer.py; bytes preserved',unrelated_project_modules_used=False)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if r.wasSuccessful() else 1)
if __name__=='__main__':main()
