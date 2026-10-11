#!/usr/bin/env python3
"""Three focused rest-residue/curvature checks in J=1 lattice units.

The continuum reference integrates the defining real-line normalization and
curvature numerator directly, with reciprocal tails and algebraic endpoint
weights.  It does not evaluate a beta/gamma function or call a routine for
the new coefficients.  Lattice energies and the separate velocity diagnostic
explicitly reuse the preserved scalar solver.  Floating-point quadrature
error estimates and refinement checks are not certified numerical intervals.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import unittest
import warnings

sys.dont_write_bytecode = True

from scipy.integrate import IntegrationWarning, quad

from detuning import ROOT, coupling, dimer, pole

warnings.simplefilter("error", IntegrationWarning)
REPORT: dict = {}


def closed_coefficients(z: float) -> dict[str, float]:
    """The three independently checked analytical coefficients, not a solver."""
    beta = (1 - z) / z
    A = 2 ** (-1 / z) / (z * math.sin(math.pi * beta))
    a = A ** (-1 / beta)
    D = beta / a
    C = z * 2 ** (2 / z - 3) * a ** (1 - 2 / z)
    return {"beta": beta, "A": A, "a_star": a, "D0": D,
            "curvature_coefficient": C, "curvature_numerator": D * C}


def continuum_integrals(z: float, a: float, tolerance: float) -> dict:
    """Integrate D and N on x>0; x=1/t handles their infinite tails.

    D=(1/pi) integral (2*x**z+a)**(-2) dx and
    N=(z**2/pi) integral x**(2*z-2)/(2*x**z+a)**3 dx.
    The reciprocal-tail powers are 2*z-2 and z, respectively.  No compact
    beta-function formula is used in this independent numerical reference.
    """
    options = dict(epsabs=tolerance, epsrel=tolerance, limit=300)
    d_low = quad(lambda x: (2 * x ** z + a) ** -2, 0, 1, **options)
    d_tail = quad(lambda t: (2 + a * t ** z) ** -2, 0, 1,
                  weight="alg", wvar=(2 * z - 2, 0), **options)
    n_low = quad(lambda x: (2 * x ** z + a) ** -3, 0, 1,
                 weight="alg", wvar=(2 * z - 2, 0), **options)
    n_tail = quad(lambda t: (2 + a * t ** z) ** -3, 0, 1,
                  weight="alg", wvar=(z, 0), **options)
    D = (d_low[0] + d_tail[0]) / math.pi
    N = z * z * (n_low[0] + n_tail[0]) / math.pi
    return {"D": D, "N": N, "C": N / D,
            "D_error_estimate": (d_low[1] + d_tail[1]) / math.pi,
            "N_error_estimate": z * z * (n_low[1] + n_tail[1]) / math.pi,
            "requested_tolerance": tolerance}


def lattice_rest_integrals(rho: float, z: float, tolerance: float) -> dict:
    """Cusp-safe lattice D and N using q=length*x, not epsilon''.

    The integrable numerator singularity x**(2*z-2) is supplied as an
    algebraic weight on the first cell; subsequent positive cells double in
    width.  Scaling resolves the narrow rest feature before integration.
    """
    delta, U = coupling(rho, z)
    E0 = dimer.rest_bound_energy(z, U)
    gap = -E0
    length = (gap / 2) ** (1 / z)
    xmax = math.pi / length
    cuts = [0.0, min(1.0, xmax)]
    while cuts[-1] < xmax:
        cuts.append(min(2 * cuts[-1], xmax))
    options = dict(epsabs=tolerance, epsrel=tolerance, limit=300)

    def sinc_half(q: float) -> float:
        return math.sin(q / 2) / (q / 2) if q else 1.0

    def denominator(x: float) -> float:
        return 1 + (x * sinc_half(length * x)) ** z

    d_cells = [quad(lambda x: denominator(x) ** -2, a, b, **options)
               for a, b in zip(cuts[:-1], cuts[1:])]

    def numerator_regular(x: float) -> float:
        q = length * x
        return (math.cos(q / 2) ** 2 * sinc_half(q) ** (2 * z - 2)
                / denominator(x) ** 3)

    n_cells = [quad(numerator_regular, 0, cuts[1], weight="alg",
                    wvar=(2 * z - 2, 0), **options)]
    n_cells.extend(quad(lambda x: x ** (2 * z - 2) * numerator_regular(x),
                        a, b, **options)
                   for a, b in zip(cuts[1:-1], cuts[2:]))
    d_prefactor = length / (math.pi * gap ** 2)
    n_prefactor = z * z * length ** (2 * z - 1) / (math.pi * gap ** 3)
    D = d_prefactor * sum(item[0] for item in d_cells)
    N = n_prefactor * sum(item[0] for item in n_cells)
    d_error = d_prefactor * sum(item[1] for item in d_cells)
    n_error = n_prefactor * sum(item[1] for item in n_cells)
    C = N / D
    Z = 1 / (U * U * D)
    return {"rho": rho, "delta": delta, "U_over_J": U, "E0_over_J": E0,
            "rest_gap_length": length, "quadrature_cells": len(d_cells),
            "D": D, "N": N, "C_over_J": C, "Z0": Z,
            "D_error_estimate": d_error, "N_error_estimate": n_error,
            "C_error_estimate": abs(C) * (d_error / D + n_error / N),
            "scaled_energy": E0 / rho ** z,
            "scaled_residue": U * U * Z / rho ** (2 * z - 1),
            "scaled_curvature": C * rho ** (2 - z),
            "effective_mass_in_J_units": 1 / (2 * C),
            "requested_tolerance": tolerance}


def floating_budget(value: float, error_estimate: float) -> float:
    """Allow QUADPACK's indicator plus floating arithmetic, not an enclosure."""
    return 16 * error_estimate + 64 * sys.float_info.epsilon * abs(value)


class Checks(unittest.TestCase):
    def test_01_independent_continuum_coefficients(self):
        rows = []
        for z in (.6, .75, .9):
            reference = closed_coefficients(z)
            coarse = continuum_integrals(z, reference["a_star"], 2e-9)
            refined = continuum_integrals(z, reference["a_star"], 2e-12)
            for name, target in (("D", reference["D0"]),
                                 ("N", reference["curvature_numerator"])):
                error_name = name + "_error_estimate"
                self.assertGreater(refined[name], 0)
                self.assertLess(abs(refined[name] - target),
                                floating_budget(target, refined[error_name]))
                self.assertLess(abs(refined[name] - coarse[name]),
                                floating_budget(refined[name],
                                                refined[error_name] + coarse[error_name]))
                self.assertLess(refined[error_name], coarse[error_name])
            rows.append({"z": z, "closed": reference, "coarse": coarse,
                         "refined": refined,
                         "curvature_relative_difference":
                         refined["C"] / reference["curvature_coefficient"] - 1})
        REPORT["independent_continuum_coefficients"] = rows

    def test_02_lattice_rest_scaling(self):
        rows = []
        for z in (.6, .75, .9):
            reference = closed_coefficients(z)
            cases = []
            for rho in (.01, .0025, .000625):
                coarse = lattice_rest_integrals(rho, z, 2e-9)
                refined = lattice_rest_integrals(rho, z, 2e-12)
                for name in ("D", "N"):
                    error_name = name + "_error_estimate"
                    self.assertLess(abs(refined[name] - coarse[name]),
                                    floating_budget(refined[name],
                                                    refined[error_name] + coarse[error_name]))
                self.assertLess(refined["E0_over_J"], 0)
                self.assertTrue(0 < refined["Z0"] < 1)
                self.assertGreater(refined["C_over_J"], 0)
                refined["relative_residue_error_from_limit"] = (
                    refined["scaled_residue"] * reference["beta"]
                    / reference["a_star"] - 1)
                refined["relative_curvature_error_from_limit"] = (
                    refined["scaled_curvature"] / reference["curvature_coefficient"] - 1)
                refined["coarse_D"] = coarse["D"]
                refined["coarse_N"] = coarse["N"]
                cases.append(refined)
            # The selected finite couplings have genuine lattice corrections.
            # Require decreasing error under refinement of rho, rather than
            # imposing an unjustified small tolerance on nonasymptotic data.
            for name in ("relative_residue_error_from_limit",
                         "relative_curvature_error_from_limit"):
                self.assertTrue(all(abs(a[name]) > abs(b[name])
                                    for a, b in zip(cases, cases[1:])))
            rows.append({"z": z, "closed": reference, "lattice": cases})
        REPORT["lattice_rest_scaling"] = rows

    def test_03_separate_velocity_rest_derivative(self):
        rows = []
        z = .75
        for rho in (.01, .0025, .000625):
            rest = lattice_rest_integrals(rho, z, 2e-12)
            C = rest["C_over_J"]
            cases = []
            for fraction in (.001, .0001, .00001):
                P = rest["rest_gap_length"] * fraction
                E, Z, velocity = pole(P, z, rest["U_over_J"])
                estimate = velocity / (2 * P)
                self.assertGreater(estimate, 0)
                cases.append({"momentum_over_gap_length": fraction,
                              "P": P, "E_over_J": E, "Z": Z,
                              "velocity_over_J": velocity,
                              "curvature_from_velocity": estimate,
                              "relative_difference": estimate / C - 1})
            errors = [abs(item["curvature_from_velocity"] - C) for item in cases]
            self.assertTrue(all(b < a / 2 for a, b in zip(errors, errors[1:])))
            last_change = abs(cases[-1]["curvature_from_velocity"]
                              - cases[-2]["curvature_from_velocity"])
            # A posteriori refinement consistency for this checked grid.  This
            # is not a rigorous remainder estimate for arbitrary momentum.
            self.assertLess(errors[-1], 2 * last_change
                            + floating_budget(C, rest["C_error_estimate"]))
            rows.append({"rho": rho, "exact_integral_curvature": C,
                         "velocity_refinements": cases,
                         "last_absolute_change": last_change,
                         "scope": "Separate preserved cusp-split velocity quadrature; finite momentum refinement, not an interval certificate."})
        REPORT["separate_velocity_rest_derivative"] = rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists() or output == ROOT or ROOT in output.parents:
        parser.error("Use a new report outside the repository.")
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    sources = [Path(__file__), ROOT / "tools/detuning.py",
               ROOT / "archive/review-2026-10-10/prior/transport.py",
               ROOT / "archive/review-2026-10-10/prior/prior/dimer.py"]
    REPORT.update(
        status="PASS" if result.wasSuccessful() else "FAIL",
        test_groups=result.testsRun, preserved_scalar_modules_reused=True,
        interval_certification=False,
        source_sha256={str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                       for path in sources},
        scope="Author-side finite rest-residue and curvature checks; analytical limits are proved separately. All units have J=1.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x") as stream:
        json.dump(REPORT, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
