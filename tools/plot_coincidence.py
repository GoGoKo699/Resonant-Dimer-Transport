#!/usr/bin/env python3
"""Plot the infinite-lattice, long-time unconditional coincidence tail.

All plotted probabilities are lattice pole quadratures of Z(P)^2 dP/pi,
with both local-source and local-detector overlaps. The preserved scalar
solver is imported read-only through detuning.py. Crossing scans and located
maxima are finite numerical diagnostics, not interval/global certificates.
No finite-time propagation is simulated. The analytical support statements
are proved separately in research/DETUNING_CROSSOVER.md.

Default outputs: figures/coincidence_tail.svg and coincidence_tail.json.
An optional --preview PNG can be placed outside the repository for review.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import sys
import warnings

sys.dont_write_bytecode = True
import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import brentq, minimize_scalar

from detuning import ROOT, coupling, dimer, pole, state_pole

Z_EXPONENT = .75
DETUNINGS = (.06, .09, .135)
OBSERVABLE = 'Q_U(v)=integral_{|E_d_prime(P)|>v} Z(P)^2 dP/(2*pi)'
SOURCE_PATHS = ('tools/plot_coincidence.py', 'tools/detuning.py',
                'tools/transport.py',
                'tools/dimer.py')
VMIN, VMAX = .3, 3.
warnings.simplefilter('error', IntegrationWarning)


@lru_cache(maxsize=20000)
def velocity(P: float, U: float) -> float:
    """Use the exact endpoint symmetry; elsewhere use the lattice solver."""
    if P == math.pi:
        return 0.
    if P == 0.:
        return math.inf if U == dimer.rest_threshold(Z_EXPONENT) else 0.
    return float(pole(float(P), Z_EXPONENT, U)[2])


def make_scan(U: float, delta: float, cells: int) -> np.ndarray:
    # The resonant low-momentum velocity already exceeds the displayed range.
    # The interval [0,pmin] remains in the probability integral, not truncated.
    pmin = 1e-4 if delta == 0 else .2*delta**4
    return np.r_[0., np.geomspace(pmin, math.pi, cells+1)]


def locate_cutoff(U: float, scan: np.ndarray) -> tuple[float, float]:
    values = np.array([abs(velocity(float(p), U)) for p in scan])
    i = int(np.argmax(values))
    if not 0 < i < len(scan)-1:
        raise ArithmeticError('Maximum was not bracketed inside the scan.')
    result = minimize_scalar(lambda logp: -abs(velocity(math.exp(logp), U)),
                             bounds=(math.log(scan[i-1]), math.log(scan[i+1])),
                             method='bounded', options={'xatol': 2e-9})
    if not result.success or -result.fun < max(values)-2e-9:
        raise ArithmeticError('Located maximum disagrees with the scan.')
    return math.exp(float(result.x)), float(-result.fun)


def intervals(U: float, level: float, grid: np.ndarray) -> list[tuple[float, float]]:
    """All superlevel components detected by the supplied full-zone scan."""
    values = [abs(velocity(float(p), U))-level for p in grid]
    roots = []
    for a, b, fa, fb in zip(grid[:-1], grid[1:], values[:-1], values[1:]):
        if fa == 0 or fb == 0:
            raise ArithmeticError('Shift a scan point off a crossing.')
        if np.sign(fa) != np.sign(fb):
            roots.append(float(brentq(lambda p: abs(velocity(float(p), U))-level,
                                      float(a), float(b), xtol=2e-13, rtol=2e-11)))
    edges = ([0.] if values[0] > 0 else []) + roots
    if values[-1] > 0:
        edges.append(math.pi)
    if len(edges) % 2:
        raise ArithmeticError('Unpaired velocity crossings.')
    return list(zip(edges[::2], edges[1::2]))


def weight(U: float, pieces: list[tuple[float, float]], *, refined: bool = False) -> tuple[float, float]:
    """Adaptive integration on every detected interval, with no probability floor."""
    total = error = 0.
    for a, b in pieces:
        # Rescale each interval to [0,1] so a tiny tail is not an absolute-error
        # afterthought. epsabs=0 enforces relative quadrature control.
        def density(x: float) -> float:
            p = a+(b-a)*x
            return state_pole(float(p), Z_EXPONENT, U)[1]**2*(b-a)/math.pi
        if refined:
            cuts = (0., .25, .5, .75, 1.)
            epsrel = 2e-8
        else:
            cuts = (0., 1.)
            epsrel = 3e-7
        for x0, x1 in zip(cuts[:-1], cuts[1:]):
            value, err = quad(density, x0, x1, epsabs=0., epsrel=epsrel, limit=160)
            total += value
            error += err
    return float(total), float(error)


def independent_normalization(U: float, P: float) -> dict:
    """Cusp-split direct quadrature, independent of dimer's power substitution."""
    E, Z, norm = state_pole(float(P), Z_EXPONENT, U)
    I = D = 0.
    for sign, length in ((-1., P/2), (1., math.pi-P/2)):
        # q=P/2 +/- u. The below-band denominator is nonsingular at u=0;
        # geometric subdivision resolves its physical P scale directly.
        cuts = [0., min(P/2, length)]
        while cuts[-1] < length:
            cuts.append(min(2*cuts[-1], length))
        def denominator(u: float) -> float:
            return float(dimer.epsilon(P+sign*u, Z_EXPONENT)
                         + dimer.epsilon(u, Z_EXPONENT)-E)
        for a, b in zip(cuts[:-1], cuts[1:]):
            I += quad(lambda u: 1/denominator(u), a, b,
                      epsabs=2e-12, epsrel=2e-11, limit=160)[0]/math.pi
            D += quad(lambda u: 1/denominator(u)**2, a, b,
                      epsabs=2e-12, epsrel=2e-11, limit=160)[0]/math.pi
    normalized_mass = D/norm
    contact_probability = I*I/norm
    if abs(U*I-1) > 2e-8 or abs(normalized_mass-1) > 2e-8 or abs(contact_probability/Z-1) > 3e-8:
        raise ArithmeticError('Independent source/residue normalization failed.')
    return {'P': P, 'U_over_J': U, 'pole_equation_U_times_I': U*I,
            'wavefunction_norm_squared': normalized_mass,
            'source_contact_probability': contact_probability, 'residue_Z': Z,
            'coincidence_density_Z_squared_over_pi': Z*Z/math.pi}


def compute() -> dict:
    records = []
    checks = []
    normalizations = []
    for delta in (0.,)+DETUNINGS:
        U = dimer.rest_threshold(Z_EXPONENT) if delta == 0 else coupling(delta**4, Z_EXPONENT)[1]
        coarse = make_scan(U, delta, 72)
        fine = make_scan(U, delta, 144)
        pmax = vmax = None
        if delta:
            pmax, vmax = locate_cutoff(U, fine)
            fine = np.sort(np.r_[fine, pmax])
            coarse = np.sort(np.r_[coarse, pmax])
            levels = np.unique(np.r_[np.geomspace(VMIN, .98*vmax, 34),
                                      vmax*np.array([.99, .995, .998, .999, .9995]), .9*vmax])
            validation_levels = (.5*vmax, .9*vmax, .995*vmax)
            normalizations.append(independent_normalization(U, pmax))
        else:
            levels = np.geomspace(VMIN, VMAX, 45)
            validation_levels = (.4, 1.2, 3.)
            normalizations.append(independent_normalization(U, .002))
        rows = []
        for level in levels:
            pieces = intervals(U, float(level), fine)
            q, err = weight(U, pieces)
            if q <= 0 or not math.isfinite(q):
                raise ArithmeticError('Displayed below-cutoff probability must be positive.')
            rows.append({'v_over_J': float(level), 'Q': q,
                         'quadrature_error_estimate': err, 'momentum_intervals': pieces})
        for level in validation_levels:
            a = intervals(U, float(level), coarse)
            b = intervals(U, float(level), fine)
            if len(a) != len(b):
                raise ArithmeticError('Grid refinement changed the detected crossing count.')
            crossing_error = max((abs(x-y) for aa, bb in zip(a,b) for x,y in zip(aa,bb)), default=0.)
            q0, _ = weight(U, a)
            q1, err1 = weight(U, b, refined=True)
            relative = abs(q0/q1-1)
            if crossing_error > 2e-9 or relative > 3e-6:
                raise ArithmeticError('Crossing/quadrature refinement check failed.')
            checks.append({'delta': delta, 'v_over_J': float(level),
                           'coarse_cells': 72, 'refined_cells': 144,
                           'detected_components': len(a),
                           'crossing_absolute_difference': crossing_error,
                           'Q_coarse': q0, 'Q_refined': q1,
                           'Q_relative_difference': relative,
                           'refined_quadrature_error_estimate': err1})
        entry = {'delta': delta, 'rho': delta**4, 'U_over_J': U,
                 'located_cutoff_v_over_J': vmax, 'located_maximum_P': pmax,
                 'curve': rows}
        if delta:
            # No finite floor or clipped small value is substituted for zero:
            # this follows from an empty numerical superlevel-set scan.
            above = intervals(U, vmax*(1+1e-6), fine)
            if above:
                raise ArithmeticError('A scan-detected component exceeds the located cutoff.')
            entry['above_located_cutoff_diagnostic'] = {
                'v_over_J': vmax*(1+1e-6), 'Q_from_detected_intervals': 0.,
                'detected_intervals': above}
            q90, qerr = weight(U, intervals(U, .9*vmax, fine), refined=True)
            entry['Q_at_90_percent_cutoff'] = q90
            entry['Q_at_90_percent_cutoff_quadrature_error_estimate'] = qerr
        records.append(entry)
        print(f'delta={delta:.3f}: {len(rows)} probabilities; located cutoff={vmax}', flush=True)
    return {'z': Z_EXPONENT, 'J': 1.,
            'observable': OBSERVABLE,
            'normalization': 'Unconditional local-source and same-site-detector probability; two overlaps.',
            'limit_order': 'Infinite lattice; t to infinity at fixed U and v. No finite-time curve.',
            'scope': 'Finite lattice-dispersion quadrature and crossing scans, not interval enclosures or a global maximum certificate.',
            'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCE_PATHS},
            'series': records, 'crossing_and_quadrature_refinement': checks,
            'independent_source_residue_checks': normalizations}


def plot(data: dict, output: Path, preview: Path | None) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import LogLocator, NullFormatter
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'svg.hashsalt': 'resonant-dimer-coincidence-v1',
                         'svg.fonttype': 'none'})
    colors = ['#242B38', '#137F87', '#AD591D', '#78509F']
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.6, 4.5),
                                gridspec_kw={'width_ratios': [1.75, 1.]})
    fig.subplots_adjust(left=.09, right=.975, bottom=.24, top=.78, wspace=.36)
    for i, record in enumerate(data['series']):
        rows = record['curve']
        label = r'Resonance $U=U_c$' if i == 0 else rf'$\delta={record["delta"]:g}$'
        ax.plot([r['v_over_J'] for r in rows], [r['Q'] for r in rows],
                color=colors[i], lw=2.1, label=label)
        if i:
            vmax = record['located_cutoff_v_over_J']
            ax.axvline(vmax, color=colors[i], lw=.9, ls=(0, (3, 3)), alpha=.65)
    ax.set_yscale('log')
    ax.set_xlim(VMIN, VMAX)
    ax.set_ylim(1e-10, .35)
    ax.set_xlabel(r'Velocity threshold $v/J$')
    ax.set_ylabel(r'Unconditional probability $Q_U(v)$')
    ax.set_title('a   The local coincidence tail', loc='left', fontsize=12, pad=12)
    ax.legend(loc='upper right', frameon=False, fontsize=9.5)
    ax.text(.04, .035, 'Dashed verticals: located velocity cutoffs',
            transform=ax.transAxes, color='#50545C', fontsize=8.6)
    ax.grid(axis='y', which='major', color='#E4E6E9', lw=.65)
    points = data['series'][1:]
    xs = [r['located_cutoff_v_over_J'] for r in points]
    ys = [r['Q_at_90_percent_cutoff'] for r in points]
    bx.plot(xs, ys, color='#A2A6AE', lw=1.2, zorder=1)
    for i, (record, x, y) in enumerate(zip(points, xs, ys), 1):
        bx.scatter(x, y, s=54, color=colors[i], zorder=2)
        bx.annotate(rf'$\delta={record["delta"]:g}$', (x,y),
                    xytext=(0, 10), textcoords='offset points', ha='center',
                    color=colors[i], fontsize=9.5)
    bx.set_yscale('log')
    bx.set_xlim(.65, 1.92)
    bx.set_ylim(min(ys)/2.7, max(ys)*3.5)
    bx.set_xlabel(r'Located cutoff $v_{\max}/J$')
    bx.set_ylabel(r'$Q_U(0.9\,v_{\max})$')
    bx.set_title('b   Faster cutoff, rarer events', loc='left', fontsize=12, pad=12)
    bx.grid(axis='y', which='major', color='#E4E6E9', lw=.65)
    for axis in (ax, bx):
        axis.yaxis.set_major_locator(LogLocator(base=10, numticks=7))
        axis.yaxis.set_minor_formatter(NullFormatter())
    fig.suptitle('Resonant dimer transport: the absolute detection probability',
                 fontsize=15, x=.09, ha='left', y=.97, fontweight='bold')
    fig.text(.09, .866, r'Actual lattice dispersion · $z=3/4$ · local creation and same-site detection',
             fontsize=10.5, color='#50545C')
    fig.text(.09, .087, r'$Q_U(v)=\int_{|E_d^\prime(P)|>v}Z(P)^2\,dP/(2\pi)$'
             '     Infinite lattice, then long time at fixed detuning and threshold.', fontsize=10)
    fig.text(.09, .035, 'Lattice pole quadratures; finite crossing scans and located maxima are numerical diagnostics. '
             'These curves do not give finite-time probabilities.', fontsize=8.7, color='#50545C')
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, metadata={'Date': None, 'Creator': 'tools/plot_coincidence.py'})
    if preview:
        preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(preview, dpi=170)
    plt.close(fig)


def validate_cached_data(data: dict) -> None:
    if (data.get('z') != Z_EXPONENT or data.get('J') != 1.
            or data.get('observable') != OBSERVABLE
            or [r['delta'] for r in data['series']] != [0., *DETUNINGS]):
        raise ValueError('Cached data does not match the declared physical problem.')
    expected = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCE_PATHS}
    if data.get('source_sha256') != expected:
        raise ValueError('Cached data source hashes differ; recompute with the current script.')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'figures/coincidence_tail.svg')
    parser.add_argument('--data', type=Path, default=ROOT/'figures/coincidence_tail.json')
    parser.add_argument('--preview', type=Path)
    parser.add_argument('--from-data', type=Path, help='Render previously computed values without rerunning diagnostics.')
    args = parser.parse_args()
    data = json.loads(args.from_data.read_text()) if args.from_data else compute()
    if args.from_data:
        validate_cached_data(data)
    if not args.from_data:
        args.data.parent.mkdir(parents=True, exist_ok=True)
        args.data.write_text(json.dumps(data, indent=2, sort_keys=True, allow_nan=False)+'\n')
    plot(data, args.output, args.preview)
    summary = {
        'maximum_crossing_difference': max(r['crossing_absolute_difference'] for r in data['crossing_and_quadrature_refinement']),
        'maximum_probability_refinement_relative_difference': max(r['Q_relative_difference'] for r in data['crossing_and_quadrature_refinement']),
        'maximum_normalization_residual': max(abs(r['wavefunction_norm_squared']-1) for r in data['independent_source_residue_checks']),
        'maximum_source_residue_relative_residual': max(abs(r['source_contact_probability']/r['residue_Z']-1) for r in data['independent_source_residue_checks']),
        'near_cutoff': [{k: r[k] for k in ('delta', 'located_cutoff_v_over_J', 'Q_at_90_percent_cutoff')} for r in data['series'][1:]],
        'source_sha256': data['source_sha256'],
    }
    print(json.dumps(summary, sort_keys=True, allow_nan=False))
    print(f'Wrote {args.output}')


if __name__ == '__main__':
    main()
