#!/usr/bin/env python3
"""Six regressions for the finite-time proof; no asymptotic time evolution is fitted."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import sys
import unittest
import warnings
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
sys.path.insert(0,str(ROOT/'archive/review-2026-10-10/prior/prior'))
import dimer  # Explicit reuse for gapped energies only; preserved and read-only.
import finite_time as ft
import numpy as np
import sympy as sp
from scipy.integrate import quad, IntegrationWarning
from scipy.linalg import eigh
warnings.simplefilter('error',IntegrationWarning)
REPORT: dict = {}


def complex_integral(e: float, eta: float, P: float, z: float) -> complex:
    roots = ft.free_preimages(e,P,z)
    pts = sorted(set([0.,P/2,np.pi,*roots]))
    a = P/2
    def fun(q):
        return 1/(ft.epsilon(q+a,z)+ft.epsilon(q-a,z)-e-1j*eta)
    parts = []
    for component in (np.real,np.imag):
        parts.append(sum(quad(lambda q: component(fun(q)),lo,hi,
                              epsabs=2e-9,epsrel=2e-9,limit=200)[0]
                         for lo,hi in zip(pts[:-1],pts[1:])))
    return complex(*parts)/np.pi


def uncentered_integral(P: float, e: float, z: float, pp: bool = False) -> float:
    P = P % (2*np.pi)
    def fun(q):
        den = ft.epsilon(q,z)+ft.epsilon(P-q,z)-e
        if pp:
            return float(2*ft.derivative(q,z)*ft.derivative(P-q,z)/den**3)
        return float(1/den)
    pts = sorted(set([0.,P,2*np.pi]))
    return sum(quad(fun,lo,hi,epsabs=3e-9,epsrel=3e-9,limit=200)[0]
               for lo,hi in zip(pts[:-1],pts[1:]))/(2*np.pi)


class Checks(unittest.TestCase):
    def test_01_geometry_density_and_derivatives(self):
        rows = []
        for z in (.6,.75,.9):
            const = ft.spectral_constants(z)
            worst_lower = math.inf
            worst_derivative_ratio = 0.
            for P in (.01,.2,1.2,2.7,np.pi):
                a,T,M,B = ft.half_arcs(P,z)
                # Energy intervals may shrink or merge; every sample is regular.
                intervals = [(T,M)] if M > T else []
                if B > M+1e-12:
                    intervals.append((M,B))
                for lo,hi in intervals:
                    for fraction in (.23,.61):
                        e = lo+fraction*(hi-lo)
                        density,d1,d2 = ft.free_density(e,P,z)
                        lower = const['free_density_lower_coefficient']*(e-T)**const['r']
                        self.assertGreaterEqual(density,lower*(1-1e-10))
                        worst_lower = min(worst_lower,density/lower)
                        h = min(1.,abs(e-T),abs(e-M),abs(e-B))
                        b1 = const['free_density_derivative_R1']*h**(-(2/z+.5))
                        b2 = const['free_density_second_derivative_R2']*h**(-(4/z+.5))
                        self.assertLessEqual(abs(d1),b1)
                        self.assertLessEqual(abs(d2),b2)
                        worst_derivative_ratio = max(worst_derivative_ratio,abs(d1)/b1,abs(d2)/b2)
                        for q in ft.free_preimages(e,P,z):
                            app = ft.derivative(q+a,z,2)+ft.derivative(q-a,z,2)
                            self.assertLessEqual(app,-const['concavity']*(1-1e-13))
            # Check the energy derivatives without differentiating the coarea code.
            P=1.2; _,T,M,B=ft.half_arcs(P,z);e=(M+B)/2;h=2e-4
            r0,r1,r2=ft.free_density(e,P,z)
            rm=ft.free_density(e-h,P,z)[0];rp=ft.free_density(e+h,P,z)[0]
            self.assertAlmostEqual((rp-rm)/(2*h),r1,delta=1e-6)
            self.assertAlmostEqual((rp-2*r0+rm)/h**2,r2,delta=3e-6)
            rows.append({'z':z,'minimum_density_to_lower_bound_ratio':worst_lower,
                         'maximum_derivative_to_bound_ratio':worst_derivative_ratio})
        REPORT['geometry'] = rows

    def test_02_boundary_resolvent_and_contact_envelope(self):
        rows=[];z=.75;uc=ft.critical_coupling(z);const=ft.spectral_constants(z)
        for P in (.3,1.1,2.7):
            _,T,M,B=ft.half_arcs(P,z)
            for e in ((T+M)/2,(M+B)/2):
                boundary=ft.boundary_resolvent(e,P,z)
                errors=[abs(complex_integral(e,eta,P,z)-boundary) for eta in (.004,.001)]
                self.assertLess(errors[-1],errors[0])
                self.assertLess(errors[-1],.16)
                for u in (uc,1.3*uc,2*uc):
                    w=ft.contact_density(e,P,z,u)
                    envelope=const['density_envelope_W0']*(e-T)**(-const['r'])
                    self.assertGreater(w,0)
                    self.assertLessEqual(w,envelope)
                    self.assertAlmostEqual(w,(boundary/(1-u*boundary)).imag/np.pi,places=12)
                rows.append({'P':P,'energy':e,'boundary_real':boundary.real,
                             'boundary_imag':boundary.imag,'complex_height_errors':errors})
        REPORT['spectral_density']={'records':rows,'scope':'Finite boundary-value convergence diagnostics; no continuum time-decay fit.'}

    def test_03_global_gap_and_gapped_second_derivative(self):
        z=.75;u=1.4*dimer.rest_threshold(z);E0=dimer.rest_bound_energy(z,u)
        rows=[]
        for P in (.02,.2,.8,1.7,np.pi):
            E=dimer.contact_energy(P,z,u);gap=float(dimer.epsilon(P,z)-E)
            self.assertGreaterEqual(gap,-E0-2e-12)
            rows.append({'P':P,'gap':gap,'rest_binding':-E0})
        derivatives=[]
        for P in (.3,1.2,2.4):
            e=-.4;h=.001
            direct=uncentered_integral(P,e,z,pp=True)
            center=uncentered_integral(P,e,z)
            fd=(uncentered_integral(P+h,e,z)-2*center+uncentered_integral(P-h,e,z))/h**2
            self.assertAlmostEqual(direct,fd,delta=3e-5)
            derivatives.append({'P':P,'energy':e,'integrated_by_parts_Ipp':direct,'finite_difference_Ipp':fd})
        for zn in (.6,.75,.9):
            # Weighted integration removes the square-derivative cusp explicitly.
            def regular(q):
                if q == 0:return zn*zn
                return float(ft.derivative(q,zn)**2/q**(2*zn-2))
            numerical=quad(regular,0,np.pi,weight='alg',wvar=(2*zn-2,0),epsabs=1e-10,epsrel=1e-10)[0]/np.pi
            bounds=ft.band_bounds(zn,1.4*ft.critical_coupling(zn),.01)
            self.assertAlmostEqual(numerical,bounds['F2_squared'],places=10)
        REPORT['band_regularity']={'gap_records':rows,'derivative_records':derivatives,
                                  'scope':'Rest-gap variational identity and gapped derivative regressions; no derivative of an asymptotic remainder.'}

    def test_04_smoothing_sandwich_and_fourier_constants(self):
        s=.7;a=.13;y=np.linspace(-1.2,1.2,10001)
        low=ft.smoothed_interval(y,s-a,a);high=ft.smoothed_interval(y,s+a,a)
        indicator=(abs(y)<=s).astype(float)
        self.assertLessEqual(float(np.max(low-indicator)),2e-13)
        self.assertLessEqual(float(np.max(indicator-high)),2e-13)
        outside=abs(abs(y)-s)>2*a
        self.assertLess(float(np.max(abs(high[outside]-low[outside]))),2e-13)
        # Direct integrals with analytical bounds on the omitted positive tails.
        R=100*np.pi
        cuts=np.linspace(0,R,101)
        fourth=sum(quad(lambda x:np.sinc(x/np.pi)**4,l,r,epsabs=1e-12,epsrel=1e-12)[0]
                   for l,r in zip(cuts[:-1],cuts[1:]))
        weighted=sum(quad(lambda x:x*np.sinc(x/np.pi)**4,l,r,epsabs=1e-12,epsrel=1e-12)[0]
                     for l,r in zip(cuts[:-1],cuts[1:]))
        self.assertLessEqual(fourth,np.pi/3+1e-12)
        self.assertGreaterEqual(fourth+1/(3*R**3),np.pi/3-1e-12)
        self.assertLessEqual(weighted,np.log(2)+1e-12)
        self.assertGreaterEqual(weighted+1/(2*R**2),np.log(2)-1e-12)
        REPORT['smoothing']={'first_fourier_moment_bound_constant':8/3,
                            'second_fourier_moment_bound_constant':32*np.log(2)/np.pi,
                            'positive_integrals_to_R':[fourth,weighted],'R':R,
                            'scope':'Smoothing bounds the original sharp event; it is not substituted as a physical detector.'}

    def test_05_characteristics_and_event_specific_interference(self):
        # An exactly specified smooth periodic fixture tests the general Fourier
        # inequality. It is not another proposed physical dimer dispersion.
        N=8192;P=2*np.pi*np.arange(N)/N
        Z=lambda p:.5+.2*np.cos(p)
        E=lambda p:-.3+.7*(1-np.cos(p))
        Ep=lambda p:.7*np.sin(p)
        Wc=.27;zp=.2/np.sqrt(2);epp=.7;delta=.2;records=[]
        for tau in (8.,32.,128.):
            for xi in (.3,1.,3.):
                h=xi*delta/tau
                exact=np.mean(Z(P)*Z(P+h)*np.exp(1j*tau*(E(P+h)-E(P))))
                limit=np.mean(Z(P)**2*np.exp(1j*xi*delta*Ep(P)))
                upper=abs(xi)*delta/tau*np.sqrt(Wc)*zp+xi*xi*delta*delta/(2*tau)*Wc*epp
                err=abs(exact-limit)
                self.assertLessEqual(err,upper+2e-13)
                records.append({'tau':tau,'xi':xi,'error':float(err),'upper_bound':float(upper)})
        # Complete finite real-space evolution, retaining continuum/pole
        # interference. Finite-ring recurrences are not decay diagnostics.
        L=10;z=.75;u=1.3*ft.critical_coupling(z)
        k=2*np.pi*np.arange(L)/L;x=np.arange(L)
        F=np.exp(1j*np.outer(x,k))/np.sqrt(L);eps=ft.epsilon(k,z)
        K=(F*eps)@F.conj().T
        H=np.kron(K,np.eye(L))+np.kron(np.eye(L),K)
        H-=u*np.diag((np.repeat(x,L)==np.tile(x,L)).astype(float))
        ev,U=eigh(H);source=np.zeros(L*L);source[0]=1;co=U.conj().T@source
        one=np.ones(L)/np.sqrt(L);fibers=[]
        for p in k:
            A=eps+ft.epsilon(p-k,z)
            e,v=eigh(np.diag(A)-u*np.outer(one,one))
            weight=abs(v.conj().T@one)**2
            fibers.append((e,weight))
        event=np.zeros(L,bool);event[2:5]=True;ring=[]
        for t in (.4,2.,8.):
            full=U@(np.exp(-1j*t*ev)*co);contact=np.diag(full.reshape(L,L))
            cf=np.array([np.sum(w*np.exp(-1j*t*e)) for e,w in fibers])
            pole=np.fft.ifft([w[0]*np.exp(-1j*t*e[0]) for e,w in fibers])
            self.assertLess(float(np.linalg.norm(contact-np.fft.ifft(cf))),4e-13)
            eta=float(np.linalg.norm(contact-pole))
            pd=float(np.sum(abs(pole[event])**2));pa=float(np.sum(abs(contact[event])**2))
            upper=ft.event_error_bound(pd,0.,0.,eta)
            self.assertLessEqual(abs(pa-pd),upper+2e-13)
            ring.append({'time':t,'actual_event':pa,'pole_event':pd,'continuum_norm':eta,
                         'event_specific_error_bound':upper})
        REPORT['finite_identities']={'smooth_fixture_characteristics':records,'ring_dimension':L*L,
                                    'ring_records':ring,'scope':'Finite identities, not evidence that a finite ring reproduces the joint limit.'}

    def test_06_exponent_algebra_and_domain_checks(self):
        z=sp.symbols('z',positive=True)
        beta=2-1/z;m=6/z-sp.Rational(5,2)
        gam=(4*z-2)/(10-z);alpha=(4*z-1)/(1-z);M=alpha/(2*gam)
        self.assertEqual(sp.simplify(beta/(m+beta)-gam),0)
        self.assertEqual(sp.simplify(M-(5*z+1)/(1-z)-(-44*z*z+53*z-6)/(4*(1-z)*(2*z-1))),0)
        self.assertEqual(gam.subs(z,sp.Rational(3,4)),sp.Rational(4,37))
        self.assertEqual(M.subs(z,sp.Rational(3,4)),37)
        rows=[]
        for zn in (.55,.6,.75,.9,.95):
            data=ft.spectral_constants(zn)
            self.assertGreater(data['time_exponent'],data['band_time_exponent'])
            self.assertTrue(all(math.isfinite(x) and x>0 for x in data.values()))
            self.assertEqual(ft.continuum_bound(1.,zn),1.)
            rows.append({'z':zn,**data})
        for bad in (.5,1.,float('nan')):
            with self.assertRaises(ValueError):ft.spectral_constants(bad)
        with self.assertRaises(ValueError):ft.continuum_bound(.5,.75)
        with self.assertRaises(ValueError):ft.event_error_bound(-1.,0.,0.,0.)
        with self.assertRaises(ValueError):ft.band_bounds(.75,2.,0.)
        REPORT['exponents']={'records':rows,'time_exponent_is_optimal':False,
                            'scope':'Sufficient exponents of the stated proof; not necessary times or measured relaxation exponents.'}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    output=args.output.resolve()
    if output.exists() or output==ROOT or ROOT in output.parents:
        parser.error('Use a new report outside the repository.')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
                  preserved_scalar_solver_reused=True,unrelated_project_modules_used=False,
                  infinite_lattice_large_time_simulation=False,interval_certification=False)
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as stream:
        json.dump(REPORT,stream,indent=2,sort_keys=True,allow_nan=False);stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__=='__main__':main()
