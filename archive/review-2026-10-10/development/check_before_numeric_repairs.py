#!/usr/bin/env python3
"""Independent checks for the scoped moving-dimer review.

No prior Python module is imported. The tests verify finite identities and
convergence diagnostics, not infinite-volume asymptotics or literature priority.
Reports are append-only by name. Units J=hbar=lattice spacing=1.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sys,unittest,warnings
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad,IntegrationWarning
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.special import gamma,gammaln,roots_legendre
import sympy as sp
warnings.simplefilter('error',IntegrationWarning)
REPORT={}


def eps(k,z):return np.abs(2*np.sin(np.asarray(k)/2))**z

def uc(z):return float(2**(1+z)*np.sqrt(np.pi)*gamma(1-z/2)/gamma((1-z)/2))

def bfun(x,z):return abs(x+.5)**z+abs(x-.5)**z

def continuum(e,z,derivative=False):
    """Independent finite-interval split and reciprocal-variable tail."""
    if not .5<z<1 or e>=1:raise ValueError('Use .5<z<1 and e<1')
    p=2 if derivative else 1
    low=sum(quad(lambda x:1/(bfun(x,z)-e)**p,a,b,epsabs=2e-11,epsrel=2e-11,limit=180)[0]
            for a,b in ((0,.5),(.5,2)))
    if not derivative:low-=2**(1-z)/(2*(1-z))
    kappa=2*z-1;umax=.5**kappa
    def tail(u):
        if u==0:return .25 if derivative else e/4
        t=u**(1/kappa);tz=t**z
        A=z/2*np.log1p(-t*t/4);B=z*np.arctanh(t/2)
        correction=2*np.expm1(A)+4*np.exp(A)*np.sinh(B/2)**2
        den=2+correction-e*tz
        return 1/den**2 if derivative else (e-correction/tz)/(2*den)
    high=quad(tail,0,umax,epsabs=2e-11,epsrel=2e-11,limit=180)[0]/kappa
    return (low+high)/np.pi


def root(z):return brentq(lambda e:continuum(e,z),0,.99999999,xtol=2e-13,rtol=1e-13)

def lattice_data(P,z):
    """Direct split quadrature, no preserved scalar routines."""
    def I(E,power=1):
        def integrand(q):return 1/(eps(q+P/2,z)+eps(q-P/2,z)-E)**power
        return (quad(integrand,0,P/2,epsabs=2e-11,epsrel=2e-11,limit=180)[0]
                +quad(integrand,P/2,np.pi,epsabs=2e-11,epsrel=2e-11,limit=180)[0])/np.pi
    energy=brentq(lambda E:I(E)-1/uc(z),0,.9999*float(eps(P,z)),xtol=2e-13,rtol=1e-13)
    norm=I(energy,2)
    return float(energy),float(norm)


def ring(L,z,U):
    k=2*np.pi*np.arange(L)/L;x=np.arange(L)
    F=np.exp(1j*np.outer(x,k))/np.sqrt(L)
    K=(F*eps(k,z))@F.conj().T
    V=np.diag((np.repeat(x,L)==np.tile(x,L)).astype(float))
    return np.kron(K,np.eye(L))+np.kron(np.eye(L),K)-U*V


class Checks(unittest.TestCase):
    def test_01_resolvent_geometry_and_source_readout(self):
        z=.75;L=12;k=2*np.pi*np.arange(L)/L;U=uc(z)
        one=np.ones(L)/np.sqrt(L);records=[]
        for P in (2*np.pi/L,4*np.pi/L,np.pi):
            A=eps(k,z)+eps(P-k,z);h=np.diag(A)-U*np.outer(one,one)
            lam,vec=eigh(h);weights=abs(vec.conj().T@one)**2
            self.assertEqual(int(np.sum(lam<A.min())),1)
            self.assertAlmostEqual(float(weights.sum()),1,places=13)
            pole=lam[0];Z=1/(U*U*np.mean(1/(A-pole)**2))
            self.assertAlmostEqual(Z,float(weights[0]),places=13)
            diffs=[]
            for w in (.1+.4j,1.+.23j,3.+.7j):
                I=np.mean(1/(A-w))
                direct=np.vdot(one,np.linalg.solve(h-w*np.eye(L),one))
                diffs.append(float(abs(direct-I/(1-U*I))))
            self.assertLess(max(diffs),2e-13)
            records.append({'P':float(P),'pole':float(pole),'Z':float(Z),'resolvent_error':max(diffs)})
        # The monotonic pieces of A_P are verified independently of the solver.
        geom=[]
        for P in (.2,.9,2.4):
            tiny=1e-6
            q1=np.linspace(tiny,P/2-tiny,150)
            q2=np.linspace(P/2+tiny,np.pi-tiny,300)
            v1=eps(q1+P/2,z)+eps(q1-P/2,z)
            v2=eps(q2+P/2,z)+eps(q2-P/2,z)
            self.assertLess(float(np.max(np.diff(v1))),0)
            self.assertGreater(float(np.min(np.diff(v2))),0)
            geom.append({'P':P,'decreasing_max_increment':float(np.max(np.diff(v1))),
                         'increasing_min_increment':float(np.min(np.diff(v2)))})
        REPORT['spectral_audit']={'finite_fiber_dimension':L,'records':records,'geometry':geom,
            'scope':'Finite resolvent and residue checks. Continuum absence of singular continuous contact measure follows from the explicit analytic arcs and finite exceptional set in the proof, not from matrix diagonalization.'}

    def test_02_strong_scaled_wavefunction(self):
        z=.75;c=root(z);F=continuum(c,z,True)
        self.assertAlmostEqual(c,.634077402040558,places=10)
        self.assertAlmostEqual(F,1.1383958554094546,places=9)
        records=[]
        for P in (.2,.05,.0125):
            E,I2=lattice_data(P,z)
            xmax=np.pi/P
            def integrand(x):
                den=eps(P*(x+.5),z)+eps(P*(x-.5),z)-E
                return np.sqrt(P)/(np.sqrt(I2)*den*np.sqrt(F)*(bfun(x,z)-c))
            points=sorted(set([0,.5,1,2,4,8,16,32,xmax]))
            points=[x for x in points if x<=xmax]
            overlap=sum(quad(integrand,a,b,epsabs=2e-10,epsrel=2e-10,limit=180)[0]
                        for a,b in zip(points[:-1],points[1:]))/np.pi
            distance=np.sqrt(max(0,2-2*overlap))
            self.assertTrue(0<overlap<1)
            records.append({'P':P,'E_over_Pz':float(E/P**z),'scaled_L2_overlap':float(overlap),
                            'scaled_L2_distance':float(distance)})
        self.assertLess(records[-1]['scaled_L2_distance'],.11)
        self.assertTrue(all(records[i+1]['scaled_L2_distance']<records[i]['scaled_L2_distance'] for i in range(2)))
        REPORT['scaled_state']={'z':z,'c':c,'Fprime':F,'records':records,
             'scope':'Numerical overlap is a diagnostic. The strong limit uses an integrable (1+|x|)^(-2z) dominating envelope and Fourier isometries.'}

    def test_03_growing_support_and_best_overlap(self):
        z=.75;records=[]
        for P in (.2,.05):
            E,I2=lattice_data(P,z);versions=[]
            for nq in (8192,16384):
                q=2*np.pi*np.arange(nq)/nq-np.pi
                vm=1/(eps(q+P/2,z)+eps(q-P/2,z)-E);vm=vm/np.linalg.norm(vm)
                vr=np.fft.fftshift(np.fft.fft(np.fft.ifftshift(vm),norm='ortho'))
                r=np.arange(nq)-nq//2;masses=[]
                for a in (.25,1.,4.):
                    R=int(a/P);part=vr[abs(r)<=R];mass=float(np.vdot(part,part).real)
                    best=part/np.sqrt(mass)
                    self.assertAlmostEqual(abs(np.vdot(best,part))**2,mass,places=13)
                    rng=np.random.default_rng(10+R)
                    other=rng.normal(size=len(part))+1j*rng.normal(size=len(part));other/=np.linalg.norm(other)
                    self.assertLessEqual(abs(np.vdot(other,part))**2,mass+1e-13)
                    masses.append(mass)
                self.assertTrue(0<masses[0]<masses[1]<masses[2]<1)
                versions.append({'fourier_grid':nq,'window_mass':masses})
            difference=max(abs(np.array(versions[0]['window_mass'])-np.array(versions[1]['window_mass'])))
            self.assertLess(difference,.001)
            records.append({'P':P,'versions':versions,'max_grid_refinement':float(difference)})
        REPORT['support']={'records':records,'scaled_halfwidths':[.25,1.,4.],
            'largest_fourier_vector':16384,'scope':'FFT of a sampled normalized eigenfunction, not a 16384-dimensional many-body time propagation or a certified interval. Best-support overlap is elementary projection geometry, not an implemented state-loading protocol.'}

    def test_04_complete_dynamics_and_detuning_continuity(self):
        z=.75;L=10;U=uc(z);H=ring(L,z,U);e,v=eigh(H)
        source=np.zeros(L*L);source[0]=1
        odd=np.zeros(L*L);odd[L]=1/np.sqrt(2);odd[1]=-1/np.sqrt(2)
        co=v.conj().T@source;ao=v.conj().T@odd;records=[]
        for t in (.3,1.,3.):
            state=v@(np.exp(-1j*t*e)*co)
            antisym=v@(np.exp(-1j*t*e)*ao)
            self.assertLess(float(np.linalg.norm(np.diag(antisym.reshape(L,L)))),3e-14)
            for detune in (.01,-.04):
                ep,vp=eigh(ring(L,z,U+detune));new=vp@(np.exp(-1j*t*ep)*(vp.conj().T@source))
                n=float(np.linalg.norm(new-state))
                self.assertLessEqual(n,abs(detune)*t+2e-13)
                c0=abs(np.diag(state.reshape(L,L)))**2;cd=abs(np.diag(new.reshape(L,L)))**2
                event_error=float(abs(np.sum(cd[2:5])-np.sum(c0[2:5])))
                self.assertLessEqual(event_error,abs(detune)*t+2e-13)
                records.append({'t':t,'deltaU':detune,'state_norm_difference':n,'event_probability_difference':event_error,
                                'duhamel_upper_bound':abs(detune)*t})
        REPORT['dynamics_controls']={'hilbert_dimension':L*L,'records':records,
            'odd_source_contact_vanishes':True,'scope':'Exact finite identity checks; infinite-lattice detuning bound uses the norm-one contact projection. This is a sufficient continuity bound, not an optimal tuning requirement.'}

    def test_05_tail_rule_and_small_support_coefficient(self):
        eta,kappa,z=sp.symbols('eta kappa z',positive=True)
        self.assertEqual(sp.simplify(((2*eta+1)/kappa).subs({eta:2*z-1,kappa:1-z})-(4*z-1)/(1-z)),0)
        self.assertEqual(sp.simplify(((4*z-1)/(1-z)).subs(z,sp.Rational(3,4))),8)
        zn=.75;c=root(zn);F=continuum(c,zn,True)
        D=gamma(1-zn)*np.sin(np.pi*zn/2)/(2*np.pi*np.sqrt(F))
        small=2*D*D/(2*zn-1)
        B=1/(uc(zn)**2*F);values=[]
        for R in (100,10000):
            n=np.arange(R+1,dtype=float)
            a=np.exp(gammaln(n+zn/2)-gammaln(zn/2)+gammaln(1-zn/2)-gammaln(n+1-zn/2))
            SR=2*np.sum(a*a)-1
            value=B*SR/R**(2*zn-1)
            values.append({'R':R,'coefficient_from_exact_lattice_gamma_ratios':float(value),'limiting_coefficient':float(small)})
        self.assertLess(abs(values[-1]['coefficient_from_exact_lattice_gamma_ratios']/small-1),.02)
        REPORT['asymptotic_dictionary']={'generic_tail_exponent':'(2 eta+1)/kappa','dimer_tail_exponent':8,
            'small_scaled_support_mass_coefficient':float(small),'lattice_matches':values,
            'scope':'The exponent follows from pushing forward two local overlap weights; it is not an independent universality mechanism.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():ap.error('Refusing to overwrite an existing report')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
        prior_python_modules_imported=False,unrelated_project_files_used=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as stream:json.dump(REPORT,stream,indent=2,sort_keys=True,allow_nan=False);stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
