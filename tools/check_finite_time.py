#!/usr/bin/env python3
"""Five finite-time analytical regression groups; not a rare-event simulation.

The exact continuous-density and smooth-band examples are mathematical controls,
not substitutes for evaluating the fractional dimer's spectral variation budget.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import unittest
import warnings
sys.dont_write_bytecode = True
import numpy as np
from scipy.integrate import IntegrationWarning, quad
from finite_time import (TimeBudget, band_budget, conservative_norm_envelope, continuum_density,
                        dimer, error_bound, smoothed_inside, state_pole,
                        static_derivatives)
warnings.simplefilter('error', IntegrationWarning)
REPORT = {}


class Checks(unittest.TestCase):
    def test_01_event_local_error_and_relative_budget(self):
        rng = np.random.default_rng(5091)
        errors = []
        for _ in range(30):
            d = rng.normal(size=24)+1j*rng.normal(size=24)
            d /= 2*np.linalg.norm(d)
            residual = rng.normal(size=24)+1j*rng.normal(size=24)
            residual *= .015/np.linalg.norm(residual)
            selected = np.arange(24)%3 == 0
            pd = float(np.sum(abs(d[selected])**2))
            actual = float(np.sum(abs((d+residual)[selected])**2))
            eta = float(np.linalg.norm(residual))
            self.assertLessEqual(abs(actual-pd),error_bound(pd,0,eta)+1e-14)
            self.assertLessEqual(abs(np.sqrt(actual)-np.sqrt(pd)),eta+1e-14)
            errors.append(abs(actual-pd))
        budgets=[]
        for q in (1e-8,.001,.5):
            for eps in (.01,.2,1.):
                b=TimeBudget(q,eps,eps*q/7,eps*eps*q/150,.7,1.3)
                t=b.sufficient_time()
                self.assertLess(b.bound_at(t)/q,eps)
                self.assertLessEqual(b.bound_at(2*t),b.bound_at(t))
                budgets.append(dict(q=q,eps=eps,arithmetic_time=t,relative_bound=b.bound_at(t)/q))
        with self.assertRaises(ValueError):TimeBudget(.1,.2,.1,0,1,1).sufficient_time()
        with self.assertRaises(ValueError):error_bound(.2,-.1,.1)
        REPORT['event_geometry']={'largest_checked_difference':max(errors),'budgets':budgets,
            'scope':'Synthetic amplitude inequality and conditional budget arithmetic, not physical observation times.'}

    def test_02_compact_smoothing_and_constants(self):
        h=.2;s=.7;x=np.linspace(-2,2,2001)
        lower=smoothed_inside(x,s-h,h);upper=smoothed_inside(x,s+h,h)
        exact=(abs(x)<=s).astype(float)
        self.assertLessEqual(float(np.max(lower-exact)),3e-14)
        self.assertLessEqual(float(np.max(exact-upper)),3e-14)
        # After xi=3u/h the envelope moments reduce to elementary integrals.
        I0=2*(3/h)*(1+quad(lambda u:u**(-3),1,np.inf)[0])
        I1=2*(3/h)**2*(.5+quad(lambda u:u**(-2),1,np.inf)[0])
        self.assertAlmostEqual(I0,9/h,places=11)
        self.assertAlmostEqual(I1,27/h**2,places=10)
        for freq in (.2,2.,10.):
            real=quad(lambda x:smoothed_inside(x,s,h)*np.cos(freq*x),-s-h,s+h,
                      points=[-s+h,s-h],epsabs=1e-10,epsrel=1e-10)[0]
            theory=2*np.sin(s*freq)/freq*np.sinc(h*freq/(3*np.pi))**3
            self.assertAlmostEqual(real,theory,places=8)
        REPORT['smoothing']={'h':h,'envelope_integral':I0,'first_moment':I1,
                             'sharp_detector_sandwich_checked':True}

    def test_03_exact_smooth_band_characteristic_and_event(self):
        # A separately specified smooth band; this does not replace the dimer.
        N=32768;P=2*np.pi*np.arange(N)/N-np.pi
        Z=.4+.1*np.cos(P);Zp=-.1*np.sin(P)
        E=1-np.cos(P)+.08*np.cos(2*P)
        V=np.sin(P)-.16*np.sin(2*P);Epp=np.cos(P)-.32*np.cos(2*P)
        mass=float(np.mean(Z**2));a=.6;s=.35;h=.09
        zn=float(np.sqrt(np.mean(Zp**2)));en=float(np.sqrt(np.mean((Epp*Z)**2)))
        coef=band_budget(a,h,mass,zn,en)
        q=float(np.mean(Z**2*(abs(a*V)>s)))
        shell=float(np.mean(Z**2*(abs(abs(a*V)-s)<=2*h)))
        rows=[];j=np.fft.fftshift(np.fft.fftfreq(N,d=1/N))
        for t in (6.,24.,96.):
            amps=np.fft.fftshift(np.fft.ifft(Z*np.exp(-1j*t*E)))
            probs=abs(amps)**2
            self.assertAlmostEqual(float(probs.sum()),mass,places=12)
            event=float(probs[abs(a*j/t)>s].sum())
            self.assertLessEqual(abs(event-q),shell+coef/t+2e-7)
            for freq in (.3,1.,3.):
                # FFT convention sign is immaterial here: E and Z are even.
                measured=np.sum(probs*np.exp(1j*freq*a*j/t))
                target=np.mean(Z**2*np.exp(1j*freq*a*V))
                bound=np.sqrt(mass)/t*(a*abs(freq)*zn+a*a*freq**2*en/2)
                self.assertLessEqual(abs(measured-target),bound+2e-12)
            rows.append(dict(t=t,event=event,limiting_event=q,
                             actual_error=abs(event-q),bound=shell+coef/t))
        REPORT['smooth_band']={'grid':N,'records':rows,'mass':mass,
            'scope':'Exactly specified cosine-band control; no dimer continuum or rare-tail approximation.'}

    def test_04_actual_dimer_curvature_and_gap(self):
        z=.75;U=1.8*dimer.rest_threshold(z)
        env=conservative_norm_envelope(z,U);rows=[]
        for P in (.25,1.1,2.6):
            data=static_derivatives(P,z,U);step=4e-4
            Em,Zm,_=state_pole(P-step,z,U);Ep,Zp,_=state_pole(P+step,z,U)
            e2fd=(Ep-2*data['E']+Em)/step**2
            zpfd=(Zp-Zm)/(2*step)
            self.assertLess(abs(data['curvature']-e2fd),3e-6)
            self.assertLess(abs(data['residue_derivative']-zpfd),3e-7)
            self.assertGreaterEqual(float(dimer.epsilon(P,z))-data['E'],env['gap_lower_bound']-1e-12)
            self.assertLess(abs(data['curvature']),env['curvature_upper_bound'])
            self.assertLess(abs(data['residue_derivative']),env['residue_derivative_upper_bound'])
            data.update(curvature_finite_difference=e2fd,residue_finite_difference=zpfd)
            rows.append(data)
        # Independent integration of the finite first-derivative kinetic norm.
        integral=quad(lambda k:z*z*np.cos(k/2)**2*np.sinc(k/(2*np.pi))**(2*z-2),
                      0,np.pi,weight='alg',wvar=(2*z-2,0),epsabs=1e-11,epsrel=1e-11)[0]/np.pi
        self.assertAlmostEqual(integral,env['epsilon_derivative_L2_squared'],places=10)
        REPORT['dimer_static_derivatives']={'records':rows,'conservative_envelope':env,
            'scope':'Dimer-specific nonoscillatory identities; envelope uses numerical rest energy, not an interval enclosure.'}

    def test_05_continuum_variation_and_cusp_controls(self):
        # Triangular density on [0,2] has mass 1, TV=2 and exact Fourier transform.
        rows=[]
        for t in (.2,1.,4.,16.,64.):
            exact=np.exp(-1j*t)*np.sinc(t/(2*np.pi))**2
            real=quad(lambda E:(1-abs(E-1))*np.cos(t*E),0,2,points=[1],epsabs=1e-11)[0]
            imag=-quad(lambda E:(1-abs(E-1))*np.sin(t*E),0,2,points=[1],epsabs=1e-11)[0]
            self.assertLess(abs(exact-complex(real,imag)),3e-11)
            self.assertLessEqual(abs(exact),min(1,2/t)+1e-13)
            rows.append(dict(t=t,amplitude_abs=float(abs(exact)),BV_bound=min(1,2/t)))
        # Exact beta-density models exhibit the two integrable derivative exponents
        # entering F13--F14. This verifies the exponents, not dimer TV constants.
        for z in (.6,.75,.9):
            beta=(1-z)/z
            self.assertTrue(0<beta<1)
            # f(E)=E^beta(1-E) on [0,1]; TV is twice its unique maximum.
            peak=beta/(beta+1);tv=2*peak**beta*(1-peak)
            actual=sum(quad(lambda E:abs(beta-(beta+1)*E),lo,hi,
                            weight='alg',wvar=(beta-1,0),epsabs=1e-10)[0]
                       for lo,hi in [(0.,peak)])
            # In the second piece the integrable weight is E^(beta-1), not (E-peak)^(beta-1).
            actual+=quad(lambda E:abs(beta-(beta+1)*E)*E**(beta-1),peak,1,epsabs=1e-10)[0]
            self.assertAlmostEqual(actual,tv,places=9)
        z=.75;P=1.2;U=1.8*dimer.rest_threshold(z)
        threshold=float(dimer.epsilon(P,z));middle=2*float(dimer.epsilon(P/2,z))
        top=2*float(dimer.epsilon(np.pi-P/2,z));offsets=[.005,.00125,.0003125]
        powers=[(1-z)/z,.5,1.,.5];samples=[]
        for y in offsets:
            values=[continuum_density(E,P,z,U) for E in
                    (threshold+y,middle-y,middle+y,top-y)]
            self.assertTrue(all(value>0 for value in values))
            samples.append({'offset':y,'density':values,
                            'scaled_density':[value/y**p for value,p in zip(values,powers)]})
        final_slopes=np.log(np.array(samples[-1]['density'])/samples[-2]['density'])/np.log(.25)
        self.assertLess(float(np.max(abs(final_slopes-np.array(powers)))),.08)
        REPORT['continuum_controls']={'triangle':rows,'dimer_corner_samples':samples,
            'last_local_exponent_diagnostic':final_slopes.tolist(),'limiting_local_exponents':powers,
            'scope':'Continuous benchmarks plus actual dimer boundary-density samples; not an enclosure of its variation budget. No finite matrix is treated as a decaying continuum.'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();output=args.output.resolve();root=Path(__file__).resolve().parents[1]
    if output.exists() or output==root or root in output.parents:
        ap.error('Use a new output report outside the repository.')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
                  physical_observation_time_certified=False,continuum_variation_budget_evaluated=False,
                  preserved_scalar_code_reused=True)
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as stream:json.dump(REPORT,stream,indent=2,sort_keys=True,allow_nan=False);stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
