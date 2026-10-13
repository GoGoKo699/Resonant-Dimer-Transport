#!/usr/bin/env python3
"""Regressions for the exact-threshold lemma; original scalar code is read-only."""
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
import dimer
import numpy as np
from scipy.integrate import IntegrationWarning, quad
warnings.simplefilter('error', IntegrationWarning)
REPORT: dict = {}


def edge_integral(P: float, z: float, J: float = 1.0) -> float:
    """Independent algebraically weighted quadrature at the exact edge.

    A trigonometric increment and expm1 avoid cancellation in epsilon(P+t)
    minus epsilon(P). Naive subtraction is ill-conditioned near either cusp.
    Values are diagnostic floating-point quadratures, not interval bounds.
    """
    if not (math.isfinite(P) and 0 < P <= math.pi and .5 < z < 1
            and math.isfinite(J) and J > 0):
        raise ValueError('Require 0<P<=pi, 1/2<z<1, and finite J>0.')
    edge = float(abs(2 * np.sin(P / 2)) ** z)
    result = 0.0
    for sign, length in ((-1, P / 2), (1, np.pi - P / 2)):
        def regular(t: float) -> float:
            if t == 0:
                return 1.0
            change = (sign * 2 * np.sin(t / 4)
                      * np.cos(P / 2 + sign * t / 4) / np.sin(P / 2))
            increment = edge * np.expm1(z * np.log1p(change))
            denominator = abs(2 * np.sin(t / 2)) ** z + increment
            if not denominator > 0:
                raise ArithmeticError('Nonpositive below-edge denominator.')
            return float(t ** z / denominator)
        result += quad(regular, 0, length, weight='alg', wvar=(-z, 0),
                       epsabs=2e-10, epsrel=2e-10, limit=300)[0]
    return float(result / (J * np.pi))


class Checks(unittest.TestCase):
    def test_01_exact_edge_and_excluded_substitution(self):
        rows = []
        for z in (.6, .75, .9):
            for P in (.08, .02, .005):
                edge = float(dimer.epsilon(P, z))
                continuum_approximation = P ** z
                upper_local_extremum = float(2 * dimer.epsilon(P / 2, z))
                self.assertTrue(edge < continuum_approximation < upper_local_extremum)
                with self.assertRaises(ValueError):
                    dimer.lattice_resolvent(continuum_approximation, P, z)
                value = dimer.lattice_resolvent(edge, P, z)
                self.assertTrue(math.isfinite(value) and value > 0)
                gap_coefficient = (continuum_approximation - edge) / P ** (z + 2)
                self.assertAlmostEqual(gap_coefficient, z / 24, delta=1e-5)
                rows.append({'z': z, 'P': P, 'edge': edge,
                             'invalid_energy': continuum_approximation,
                             'gap_over_P_zplus2': gap_coefficient})
        REPORT['domain'] = rows

    def test_02_two_threshold_representations(self):
        rows = []
        for z in (.6, .75, .9):
            for P in (.08, .02, .005):
                independent = edge_integral(P, z)
                preserved = dimer.lattice_resolvent(float(dimer.epsilon(P, z)), P, z)
                difference = abs(independent - preserved)
                # An absolute cross-quadrature diagnostic, not an error certificate.
                self.assertLess(difference, 3e-9)
                rows.append({'z': z, 'P': P, 'weighted': independent,
                             'preserved': preserved, 'absolute_difference': difference})
        REPORT['representations'] = rows

    def test_03_endpoint_coefficient_and_energy_units(self):
        rows = []
        for z in (.6, .75, .9):
            target = dimer.universal(1, z)
            values = [(edge_integral(P, z) - 1 / dimer.rest_threshold(z))
                      / P ** (1-z) for P in (.08, .02, .005)]
            errors = [abs(value - target) for value in values]
            self.assertGreater(target, 0)
            self.assertTrue(all(a > b for a, b in zip(errors, errors[1:])))
            self.assertLess(errors[-1], .11)
            # Scaling J is exact for the entire resolvent, not just asymptotically.
            reference = edge_integral(.02, z)
            for J in (.4, 2.5):
                self.assertAlmostEqual(J * edge_integral(.02, z, J), reference, places=12)
            rows.append({'z': z, 'momenta': [.08, .02, .005],
                         'scaled_edge_shift': values, 'F_at_one': target})
        REPORT['coefficient'] = rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or output == ROOT or ROOT in output.parents:
        parser.error('Use a new report outside the repository.')
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',
                  test_groups=result.testsRun, preserved_scalar_solver_reused=True,
                  scope='Finite regressions, not interval certification or a proof of the limit.')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x') as stream:
        json.dump(REPORT, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    main()
