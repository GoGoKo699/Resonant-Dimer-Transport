#!/usr/bin/env python3
"""Five observation-time regressions, not interval certification or dynamics."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import sys,unittest,warnings
sys.dont_write_bytecode=True
import numpy as np
from scipy.integrate import quad,IntegrationWarning
from observation_time import (boundary_loop,contact_density,continuum_peak,dimer,
    norm_power_budget,peak_constants,power_integral,sufficient_exponent,time_scale)
from finite_time import continuum_density,error_bound
warnings.simplefilter('error',IntegrationWarning)
REPORT={}


class Checks(unittest.TestCase):
    def test_01_uniform_quotient_variation(self):
        rows=[]
        # Upper side of a Morse maximum: u=lambda-1/sqrt(y), v=1+.2*y.
        # Integrate along u, including u=0 explicitly to resolve arbitrarily
        # narrow peaks; a uniform y mesh would miss the large-lambda resonance.
        for lam in (0.,2.,20.,200.):
            top=lam-1
            def f(u):
                y=1/(lam-u)**2;v=1+.2*y;dv=.4/(lam-u)**3
                return abs(-2*v*u/(u*u+v*v)**2+(u*u-v*v)/(u*u+v*v)**2*dv)
            cuts=sorted(set([-1e5,-20.,-2.,0.,2.,20.,top]))
            cuts=[x for x in cuts if x<=top]
            variation=sum(quad(f,l,r,epsabs=1e-9,epsrel=1e-9,limit=180)[0]
                          for l,r in zip(cuts[:-1],cuts[1:]))
            self.assertLess(variation,3.)
            rows.append(dict(lambda_value=lam,variation=float(variation)))
        # Coalescing upper-maxima profile: derivative integrable at both ends.
        peaks=[]
        for c1,c2 in ((.5,2.),(1.,1.),(2.,.5)):
            def value(y):return y*np.sqrt(1-y)/(c1*c1*(1-y)+c2*c2*y)
            y=np.linspace(0,1,10001);v=value(y)
            variation=float(np.sum(abs(np.diff(v))))
            self.assertLess(variation,8.)
            peaks.append(dict(c1=c1,c2=c2,variation=variation))
        REPORT['quotient_controls']={'Morse_crossings':rows,'coalescing_profiles':peaks,
            'scope':'Normal-form benchmarks for the analytical quotient argument, not global lattice variation enclosures.'}

    def test_02_actual_lattice_continuum_peak(self):
        z=.75;U=2*dimer.rest_threshold(z)
        records=[continuum_peak(P,z,U) for P in (1e-4,1e-6,1e-8)]
        for row in records:
            self.assertGreater(row['center'],row['middle'])
            self.assertLess(row['derivative_refinement_relative'],2e-5)
        for field in ('shift_ratio','width_ratio','height_ratio'):
            errors=[abs(r[field]-1) for r in records]
            self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))
        self.assertLess(abs(records[-1]['shift_ratio']-1),.1)
        self.assertLess(abs(records[-1]['width_ratio']-1),.12)
        self.assertLess(abs(records[-1]['height_ratio']-1),.001)
        self.assertLess(float(np.max(abs(np.array(records[-1]['scaled_profile'])-[.5,1,.5]))),.02)
        # A different principal-value implementation at a moderate momentum.
        P=.04;E=2*dimer.epsilon(P/2,z)+.015
        first=contact_density(float(E),P,z,U)
        other=continuum_density(float(E),P,z,U)
        self.assertLess(abs(first-other),3e-7)
        J=2.5
        val=boundary_loop(float(E),P,z)
        self.assertLess(abs(J*boundary_loop(J*float(E),P,z,J)-val),3e-12)
        REPORT['lattice_continuum']={'records':records,'constants':peak_constants(z),
            'cross_representation_absolute_error':float(abs(first-other)),
            'scope':'Unbroadened infinite-lattice boundary integrals. Widths are spectral diagnostics, not fitted decay times or extra bound eigenstates.'}

    def test_03_norm_integrals_and_exponent_accounting(self):
        rows=[]
        for z in (.6,.75,5/6,.9):
            for power in (4*z-4,6*z-6):
                rho=.007
                exact=power_integral(power,rho)
                direct=quad(lambda P:(P+rho)**power,0,np.pi,epsabs=1e-10,epsrel=1e-10)[0]
                self.assertLess(abs(exact-direct),2e-9*(1+exact))
            nu=sufficient_exponent(z)
            alpha=(4*z-1)/(1-z)
            self.assertGreater(nu,alpha/2)
            vals=[]
            for delta in (.08,.02,.005):
                d=norm_power_budget(z,delta)
                band_time=d['scaled_band_factor']/d['mass_power']
                vals.append(float(band_time/time_scale(delta,z)))
            self.assertTrue(all(0<x<20 for x in vals))
            rows.append(dict(z=z,exponent=nu,continuum_exponent=alpha/2,
                             normalized_band_time_factors=vals))
        self.assertAlmostEqual(sufficient_exponent(.75),7.)
        self.assertAlmostEqual(sufficient_exponent(.6),3.25)
        self.assertAlmostEqual(sufficient_exponent(.9),25.)
        for bad in (.5,1.):
            with self.assertRaises(ValueError):sufficient_exponent(bad)
        REPORT['norm_powers']={'records':rows,'scope':'Exact envelope integrals and power accounting, not an equality for actual band norms or the optimal time.'}

    def test_04_integrable_momentum_bound_and_relative_accuracy(self):
        rows=[]
        for z in (.6,.75,.9):
            exponent=2*z-2
            # Substitution P=pi*x^(1/(2z-1)) removes the only singular weight.
            p=1/(2*z-1)
            transformed=quad(lambda x:np.pi**(2*z-1)*p,0,1)[0]/np.pi
            exact=np.pi**(2*z-2)/(2*z-1)
            self.assertAlmostEqual(transformed,exact,places=12)
            rows.append(dict(z=z,squared_singular_envelope_integral=exact))
        budgets=[]
        for q in (1e-12,1e-7,.1):
            for eps in (.01,.2,1.):
                A=.7;C=1.3
                t=max(6*A/(eps*q),12*C/(eps*math.sqrt(q)))
                d=eps*q/6+A/t;eta=C/t
                relative=error_bound(q,d,eta)/q
                self.assertLess(relative,eps)
                budgets.append(dict(q=q,accuracy=eps,relative_bound=relative))
        REPORT['relative_accuracy']={'integrability':rows,'arithmetic':budgets,
            'scope':'Conditional error arithmetic with dimensionless synthetic constants. No physical observation time is numerically certified.'}

    def test_05_scope_and_control_characters(self):
        root=Path(__file__).resolve().parents[1]
        proof=(root/'research/OBSERVATION_TIME.md').read_text()
        for term in ('not**','P^{z-1}','all','principal','exact'):
            self.assertIn(term,proof)
        for path in root.rglob('*.md'):
            if 'archive' in path.parts or '.git' in path.parts:continue
            controls=[ord(c) for c in path.read_text() if ord(c)<32 and c not in '\n\r\t']
            self.assertEqual(controls,[],str(path))
        REPORT['source_controls']={'active_markdown_control_characters':0,
            'archive_scanned_or_changed_by_this_group':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    root=Path(__file__).resolve().parents[1];out=a.output.resolve()
    if out.exists() or out==root or root in out.parents:p.error('Use a new report outside the repository.')
    r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if r.wasSuccessful() else 'FAIL',test_groups=r.testsRun,
                  previous_checkers_modified=False,observation_time_prefactor_certified=False)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if r.wasSuccessful() else 1)

if __name__=='__main__':main()
