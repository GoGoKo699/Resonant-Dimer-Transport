#!/usr/bin/env python3
"""Five detuning regression groups; finite checks do not prove the limits."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import sys
import unittest
import warnings
sys.dont_write_bytecode = True
import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import minimize_scalar
from detuning import (ROOT, continuum_pole, continuum_weight, coupling, dimer,
                      lattice_profile, lattice_weight, located_maximum, rest_constants)
warnings.simplefilter('error', IntegrationWarning)
REPORT: dict = {}


def independent_normalization_velocity(k: float, E: float, z: float) -> tuple[float, float]:
    """Integrate D and the derivative numerator directly on the real line.

    This does not evaluate F, its root equation, or the differentiated scaling
    identity. Weighted quadrature treats the two derivative cusps explicitly.
    """
    def band(x: float) -> float:
        return abs(x+k/2)**z + abs(x-k/2)**z
    D = sum(quad(lambda x: (band(x)-E)**(-2), a, b,
                 epsabs=2e-9, epsrel=2e-9, limit=200)[0]
            for a, b in ((0., k/2), (k/2, k), (k, np.inf)))/math.pi
    N = 0.
    for sign in (-1, 1):
        def regular(t: float) -> float:
            factor = 0. if t == 0 else (t/(k+sign*t))**(1-z)
            return z/2*(factor-sign)/((k+sign*t)**z+t**z-E)**2
        N += quad(regular, 0, k/2, weight='alg', wvar=(z-1, 0),
                  epsabs=2e-9, epsrel=2e-9, limit=200)[0]
    def tail(x: float) -> float:
        u = x-k/2
        derivative = z/2*u**(z-1)*np.expm1((z-1)*np.log1p(k/u))
        return derivative/(band(x)-E)**2
    N += quad(tail, k, np.inf, epsabs=2e-9, epsrel=2e-9, limit=200)[0]
    return D, N/(math.pi*D)


class Checks(unittest.TestCase):
    def test_01_rest_scale_and_beta_coefficient(self):
        rows = []
        for z in (.6, .75, .9):
            A, a = rest_constants(z); beta = (1-z)/z
            integral = (quad(lambda t:1/(1+t), 0, 1, weight='alg', wvar=(beta-1,0))[0]
                        +quad(lambda t:1/(1+t), 0, 1, weight='alg', wvar=(-beta,0))[0])
            independent = 2**(-1/z)*integral/(math.pi*z)
            self.assertAlmostEqual(A, independent, places=11)
            self.assertAlmostEqual(A*a**beta, 1., places=13)
            E, V, D = continuum_pole(0.,z)
            self.assertAlmostEqual(E, -a, places=13)
            self.assertEqual(V, 0.)
            self.assertGreater(D,0)
            values = [lattice_profile(rho, 0., z)[0] for rho in (.01,.0025,.000625)]
            errors = [abs(value+a) for value in values]
            self.assertTrue(all(x>y for x,y in zip(errors,errors[1:])))
            rows.append({'z':z,'A':A,'a_star':a,'scaled_lattice_rest_energies':values,
                         'rho_values':[.01,.0025,.000625]})
        REPORT['rest'] = rows

    def test_02_independent_continuum_derivative(self):
        rows = []
        for z in (.6,.75,.9):
            for k in (.2,2.,30.):
                E,V,D = continuum_pole(k,z)
                ID,IV = independent_normalization_velocity(k,E,z)
                step=1e-4*k
                finite_difference=(continuum_pole(k+step,z)[0]-continuum_pole(k-step,z)[0])/(2*step)
                self.assertLess(abs(ID/D-1),3e-7)
                self.assertLess(abs(IV-V),3e-7)
                self.assertLess(abs(finite_difference-V),2e-7)
                self.assertLess(E,k**z)
                rows.append({'z':z,'k':k,'E':E,'V':V,'D':D,
                             'direct_velocity':IV,'direct_normalization':ID,
                             'energy_finite_difference':finite_difference})
        REPORT['continuum_derivative'] = rows

    def test_03_lattice_profile_and_residue(self):
        z=.75;rows=[]
        for k in (.2,2.,10.,30.):
            E,V,D=continuum_pole(k,z)
            cases=[]
            for rho in (.0025,.000625,.00015625):
                LE,LV,LZ=lattice_profile(rho,k,z)
                cases.append({'rho':rho,'scaled_energy':LE,'scaled_velocity':LV,
                              'scaled_residue':LZ,'energy_error':abs(LE-E),
                              'velocity_error':abs(LV-V),'residue_error':abs(LZ-1/D)})
            for name in ('energy_error','velocity_error','residue_error'):
                self.assertTrue(all(a[name]>b[name] for a,b in zip(cases,cases[1:])))
            self.assertLess(cases[-1]['energy_error'],.06)
            self.assertLess(cases[-1]['velocity_error'],.0015)
            self.assertLess(cases[-1]['residue_error']*D,.02)
            rows.append({'k':k,'E_limit':E,'V_limit':V,'residue_limit':1/D,'cases':cases})
        REPORT['lattice_profile']={'z':z,'cases':rows}

    def test_04_cutoff_and_competing_momentum_scales(self):
        maxima=[located_maximum(z) for z in (.6,.75,.9)]
        for item in maxima:
            self.assertGreater(item['K_estimate'],0.)
            self.assertLessEqual(item['wider_scan_maximum'],item['K_estimate']+1e-8)
        target=maxima[1]['K_estimate']
        self.assertAlmostEqual(target,.1051707153433,places=9)
        rows=[]
        for rho in (.000625,.00015625,.0000390625):
            result=minimize_scalar(lambda k:-abs(lattice_profile(rho,float(k),.75)[1]),
                                   bounds=(2.,100.),method='bounded',options={'xatol':2e-5})
            self.assertTrue(result.success)
            # A complete Brillouin-zone sampling check is a diagnostic, not proof.
            grid=np.geomspace(.2,np.nextafter(math.pi/rho,0.),80)
            sampled=max(abs(lattice_profile(rho,float(k),.75)[1]) for k in grid)
            self.assertLessEqual(sampled,-result.fun+1e-8)
            self.assertTrue(20<result.x<45)
            rows.append({'rho':rho,'delta':rho**.25,'located_k':float(result.x),
                         'scaled_maximum':float(-result.fun),'sampled_maximum':sampled,
                         'error_from_continuum':abs(-result.fun-target)})
        self.assertTrue(all(a['error_from_continuum']>b['error_from_continuum'] for a,b in zip(rows,rows[1:])))
        self.assertLess(rows[-1]['error_from_continuum'],.001)
        REPORT['maximum']={'continuum':maxima,'lattice':rows,
                           'scope':'Numerical scans do not establish global maximality or uniqueness; D12-D14 do the global analytic work.'}

    def test_05_source_weighted_crossover(self):
        z=.75;level=.10
        first=continuum_weight(level,z,96);refined=continuum_weight(level,z,160)
        self.assertEqual(len(first['intervals']),1)
        self.assertEqual(len(refined['intervals']),1)
        self.assertLess(abs(first['H_estimate']/refined['H_estimate']-1),2e-8)
        rows=[lattice_weight(rho,level,z,96) for rho in (.00015625,.0000390625,.000009765625)]
        errors=[abs(item['scaled_weight']/refined['H_estimate']-1) for item in rows]
        self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))
        self.assertLess(errors[-1],.1)
        # Two local probability overlaps produce alpha=8, not the one-overlap exponent.
        self.assertEqual((4*z-1)/(1-z),8.)
        for item in rows:
            rho=item['rho'];U=item['U_over_J']
            self.assertAlmostEqual(item['unconditional_Q']*U**4/rho**(4*z-1),
                                   item['scaled_weight'],delta=1e-8)
        REPORT['coincidence_crossover']={'continuum':refined,'grid_refinement':first,
                                       'lattice':rows,'relative_errors':errors,
                                       'scope':'Each Q is a limiting velocity-law quadrature, not a finite-time detection probability.'}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve()
    if out.exists() or out==ROOT or ROOT in out.parents:
        parser.error('Use a new report outside the repository.')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
                  preserved_scalar_modules_reused=True,interval_certification=False,
                  scope='Author-side finite checks; analytical limits and global maximum follow from the proof.')
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as stream:
        json.dump(REPORT,stream,indent=2,sort_keys=True,allow_nan=False);stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
