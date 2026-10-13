#!/usr/bin/env python3
"""Fresh two-body pilot checks. No source, code or test from prior projects used.

The mathematical claims rest on research/SPECTRAL_PROOF.md. Tests validate representations and
finite calculations, not literature priority, infinite-volume limits or devices.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import unittest
import warnings
import numpy as np
import mpmath as mp
import sympy as sp
from scipy.integrate import quad, IntegrationWarning
from scipy.linalg import eigh
from scipy.optimize import brentq
import dimer as d

REPORT={}
warnings.simplefilter('error',IntegrationWarning)


class Checks(unittest.TestCase):
    def test_01_lattice_kernel_and_resonance(self):
        records=[]
        for z in (.6,.75,.9):
            errors=[]
            for r in (1,2,5):
                numerical=-quad(lambda k: d.epsilon(k,z)*np.cos(r*k),0,np.pi,
                                epsabs=2e-12,epsrel=2e-12)[0]/np.pi
                errors.append(abs(numerical-d.hopping(r,z)))
            self.assertLess(max(errors),2e-11)
            # Independent zero-energy resolvent Fourier integral.
            pref=np.pi**(1-z)/(2*np.pi*(1-z))
            for r in (0,1,2):
                def fun(v):
                    k=np.pi*v**(1/(1-z))
                    return np.cos(r*k)*np.sinc(k/(2*np.pi))**(-z)
                val=pref*quad(fun,0,1,epsabs=2e-12,epsrel=2e-12)[0]
                self.assertAlmostEqual(val,d.free_rest(r,z),places=10)
            rng=np.random.default_rng(1702)
            p=rng.uniform(-np.pi,np.pi,3000);q=rng.uniform(-np.pi,np.pi,3000)
            slack=d.epsilon(p,z)+d.epsilon(q,z)-d.epsilon(p+q,z)
            self.assertGreaterEqual(float(min(slack)),-1e-14)
            prefhop=mp.gamma(1+z)*mp.sin(mp.pi*z/2)/mp.pi
            asym=d.hopping(1000,z)*1000**(1+z)/float(prefhop)
            self.assertLess(abs(asym-1),2e-6)
            records.append({'z':z,'Uc':d.rest_threshold(z),'Fourier_max_error':max(errors),
                            'large_distance_kernel_ratio':asym,'minimum_subadditivity_slack':float(min(slack))})
        # The chosen window is necessary for the claimed resonance, not a numerical regulator.
        for z in (.5,1.):
            with self.assertRaises(ValueError):d.rest_threshold(z)
        REPORT['microscopic_model']={'cases':records,'note':'The resonance vector is not square integrable for z>1/2; that assertion is proved by the local power law, not finite-size diagonalization.'}

    def test_02_independent_two_particle_hamiltonian(self):
        L=12;m=2;P=2*np.pi*m/L;z=.75;U=d.rest_threshold(z)
        x=np.arange(L);k=2*np.pi*np.arange(L)/L
        W=np.exp(1j*np.outer(x,k))/np.sqrt(L)
        h=(W*d.epsilon(k,z))@W.conj().T
        H=np.kron(h,np.eye(L))+np.kron(np.eye(L),h)
        for j in range(L):H[j*L+j,j*L+j]-=U
        Q=np.column_stack([np.kron(W[:,n],W[:,(m-n)%L]) for n in range(L)])
        A=d.epsilon(k,z)+d.epsilon(P-k,z)
        reduced=np.diag(A)-U/L*np.ones((L,L))
        err=float(np.linalg.norm(H@Q-Q@reduced))
        self.assertLess(err,3e-13)
        eigen,vectors=eigh(reduced)
        self.assertEqual(int(np.sum(eigen<min(A)-1e-10)),1)
        E=float(eigen[0]);phi=vectors[:,0]
        self.assertAlmostEqual(float(np.mean(1/(A-E))),1/U,places=12)
        contact=abs(sum(phi)/np.sqrt(L))**2
        formula=1/(U**2*np.mean(1/(A-E)**2))
        self.assertAlmostEqual(contact,formula,places=12)
        # Exact hard-core projection, even relative-coordinate sector.
        q=k-P/2;R=np.exp(1j*np.outer(q,np.arange(L)))/np.sqrt(L)
        Hrel=R.conj().T@np.diag(A)@R
        V=d.hardcore_threshold(z)
        Hrel[1,1]-=V;Hrel[-1,-1]-=V
        S=np.zeros((L,L//2),complex)
        for r in range(1,L//2):S[r,r-1]=S[L-r,r-1]=1/np.sqrt(2)
        S[L//2,-1]=1
        Eh=float(np.linalg.eigvalsh(S.conj().T@Hrel@S)[0])
        g=np.array([np.mean(np.cos(r*q)/(A-Eh)) for r in (0,1,2)])
        self.assertAlmostEqual(float(g[0]+g[2]-2*g[1]**2/g[0]),1/V,places=12)
        REPORT['finite_space_dictionary']={'ring_cells':L,'full_Hilbert_dimension':L*L,
            'total_momentum':P,'fiber_intertwining_error':err,'contact_energy':E,'contact_weight':float(contact),
            'hardcore_even_energy':Eh,'warning':'A finite ring is a normalization check. Its discrete rest spectrum does not prove infinite-line unbinding.'}

    def test_03_independent_continuum_integral(self):
        mp.mp.dps=48;rows=[]
        for z0 in (.6,.75,.9):
            c=d.universal_root(z0);z=mp.mpf(str(z0));e=mp.mpf(str(c))
            def A(q):return abs(q+mp.mpf('.5'))**z+abs(q-mp.mpf('.5'))**z
            low=mp.quad(lambda q:1/(A(q)-e),[0,mp.mpf('.5'),1])-1/(2*(1-z))
            def log_tail(x):
                q=mp.exp(x)
                return q*(1/(A(q)-e)-1/(2*q**z))
            high=mp.quad(log_tail,[0,1,5,10,20,40,60])
            # At q=e^60, omitted shift corrections contribute less than 1e-40
            # in these checked z values. This comparison is not interval arithmetic.
            tail=sum(e**n/mp.mpf(2)**(n+1)*mp.exp((1-(n+1)*z)*60)/((n+1)*z-1) for n in range(1,10))
            independent=float((low+high+tail)/mp.pi)
            self.assertLess(abs(independent),8e-10)
            deriv=d.universal(c,z0,True)
            h=1e-5
            fd=(d.universal(c+h,z0)-d.universal(c-h,z0))/(2*h)
            self.assertLess(abs(fd-deriv),3e-7*(1+deriv))
            self.assertLess(d.universal(0,z0),0);self.assertGreater(d.universal(1,z0),0)
            rows.append({'z':z0,'c':c,'binding_fraction':1-c,'F0':d.universal(0,z0),
                         'F1':d.universal(1,z0),'Fprime':deriv,'independent_root_residual':independent})
        REPORT['universal_integral']={'cases':rows,'independent_precision_digits':48,'coefficients_are_interval_certified':False}

    def test_04_lattice_scaling_weight_and_dispersion(self):
        rows=[]
        for z in (.6,.75,.9):
            c=d.universal_root(z);pref=1/(d.rest_threshold(z)**2*d.universal(c,z,True))
            cases=[]
            for P in (.1,.01,.001):
                E=d.contact_energy(P,z);edge=float(d.epsilon(P,z))
                self.assertTrue(0<E<edge)
                weight=1/(d.rest_threshold(z)**2*d.lattice_resolvent(E,P,z,derivative=True))
                cases.append({'P':P,'E':E,'edge':edge,'E_over_Pz':E/P**z,
                              'contact_weight':weight,'scaled_contact_weight':weight/P**(2*z-1)})
            # These are finite convergence diagnostics, not fitted exponent proofs.
            self.assertLess(abs(cases[-1]['E_over_Pz']-c),abs(cases[0]['E_over_Pz']-c))
            self.assertLess(abs(cases[-1]['scaled_contact_weight']-pref),abs(cases[0]['scaled_contact_weight']-pref))
            rows.append({'z':z,'limiting_contact_weight_coefficient':pref,'cases':cases})
        z=.75;c=d.universal_root(z);vel=[]
        for P in (.01,.001):
            h=1e-4*P
            velocity=(d.contact_energy(P+h,z)-d.contact_energy(P-h,z))/(2*h)
            vel.append({'P':P,'velocity':velocity,'velocity_over_P_zminus1':velocity/P**(z-1)})
        self.assertLess(abs(vel[-1]['velocity_over_P_zminus1']-z*c),.002)
        U=2*d.rest_threshold(z);E0,C=d.quadratic_coefficient(z,U);mass_cases=[]
        for P in (.04,.01,.001,.0002):
            value=(d.contact_energy(P,z,U)-E0)/P**2
            mass_cases.append({'P':P,'energy_difference_over_P2':value})
        errors=[abs(x['energy_difference_over_P2']-C) for x in mass_cases]
        self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))
        REPORT['observable_scaling']={'contact_models':rows,'resonant_velocity':vel,
            'limiting_velocity_coefficient':z*c,'fixed_stronger_attraction':{'z':z,'U':U,'E0':E0,'quadratic_coefficient':C,'cases':mass_cases},
            'scope':'Dispersion and spectral weight, not a simulated signal front or a prepared wavepacket propagation claim.'}

    def test_05_hardcore_and_detuning_controls(self):
        z=.75;c=d.universal_root(z);Vc=d.hardcore_threshold(z)
        a=d.free_rest(1,z)/d.free_rest(0,z)
        rows=[]
        for P in (.1,.01,.001):
            E=d.hardcore_energy(P,z)
            self.assertTrue(0<E<d.epsilon(P,z))
            rows.append({'P':P,'E':E,'E_over_Pz':E/P**z})
        self.assertLess(abs(rows[-1]['E_over_Pz']-c),.005)
        # Independent symbolic derivative of the Schur complement.
        g0,g1,g2,t=sp.symbols('g0 g1 g2 t',positive=True)
        f=(g0+t)+(g2+t)-2*(g1+t)**2/(g0+t)
        self.assertEqual(sp.factor(sp.diff(f,t).subs(t,0)-2*(1-g1/g0)**2),0)
        weaker=.7*d.rest_threshold(z)
        with self.assertRaises(ValueError):d.contact_energy(.0001,z,weaker)
        E=d.contact_energy(.1,z,weaker)
        self.assertTrue(0<E<d.epsilon(.1,z))
        # Threshold shift is compared with the universal expression, not
        # promoted to a globally monotone critical-momentum curve.
        threshold=[]
        for P in (.01,.001):
            Ucp=1/d.lattice_resolvent(float(d.epsilon(P,z)),P,z)
            shifted=(1/Ucp-1/d.rest_threshold(z))/P**(1-z)
            threshold.append({'P':P,'UcP':Ucp,'scaled_inverse_threshold_shift':shifted})
        self.assertLess(abs(threshold[-1]['scaled_inverse_threshold_shift']-d.universal(1,z)),.01)
        REPORT['physical_controls']={'z':z,'hardcore_Vc':Vc,'singular_shift_coefficient':2*(1-a)**2,
            'hardcore_cases':rows,'weaker_attraction':weaker,'weaker_attraction_bound_energy_at_P_point1':E,
            'threshold_cases':threshold,'universal_threshold_coefficient':d.universal(1,z),
            'no_go_scope':'No normalizable rest threshold vector for the declared z range; no automatic preparation by applying a force; no group-velocity claim about an information front.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():p.error('Refusing to overwrite an evidence report.')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
                  old_project_modules_imported=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(REPORT,f,sort_keys=True,indent=2,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
