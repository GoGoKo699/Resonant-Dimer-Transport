"""Detuning diagnostics in J=1 units; preserved scalar routines are read-only.

The global theorems are proved in research/DETUNING_CROSSOVER.md. Numerical
maxima and crossing scans here are diagnostics, not exhaustive certificates.
"""
from __future__ import annotations
from functools import lru_cache
import math
from pathlib import Path
import sys
from typing import Callable

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
from transport import dimer, pole, state_pole  # Declared same-project reuse.
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar


def validate_z(z: float) -> None:
    if not math.isfinite(z) or not .5 < z < 1:
        raise ValueError('Require a finite exponent 1/2<z<1.')


def rest_constants(z: float) -> tuple[float, float]:
    """Return A_z and a_z^* in G(0,-a)=-A_z*a^((1-z)/z)."""
    validate_z(z)
    beta = (1-z)/z
    A = 2**(-1/z)/(z*math.sin(math.pi*beta))
    return A, A**(-1/beta)


@lru_cache(maxsize=8192)
def continuum_pole(k: float, z: float = .75) -> tuple[float, float, float]:
    """Return scaled energy, velocity, and D(k); k is nonnegative.

    Small-k velocity uses a difference of terms in an exact identity and can
    lose relative precision. No claim of reliable arbitrary-precision or
    uniform numerical accuracy over the entire parameter window is made.
    """
    validate_z(z)
    if not math.isfinite(k) or k < 0:
        raise ValueError('Use finite k>=0.')
    A, a = rest_constants(z)
    if k == 0:
        beta = (1-z)/z
        return -a, 0., A*beta*a**(beta-1)
    target = k**(z-1)
    low = -1.
    for _ in range(64):
        if dimer.universal(low, z) < -target:
            break
        low *= 2
    else:
        raise ArithmeticError('Could not bracket the continuum pole.')
    c = dimer.universal_root(z)
    y = brentq(lambda y: dimer.universal(y, z)+target, low, c,
               xtol=1e-12, rtol=1e-13)
    fp = dimer.universal(y, z, True)
    velocity = target*(z*y+(1-z)*target/fp)
    return float(k**z*y), float(velocity), float(k**(1-2*z)*fp)


def ratio_profile(y: float, z: float = .75) -> tuple[float, float]:
    """Return k and V(k), parametrized by y=e_z(k)/k^z<c_z."""
    validate_z(z)
    F = dimer.universal(y, z)
    if not F < 0:
        raise ValueError('Require F_z(y)<0.')
    h = -F
    fp = dimer.universal(y, z, True)
    return float(h**(-1/(1-z))), float(h*(z*y+(1-z)*h/fp))


def located_maximum(z: float = .75) -> dict:
    """Locate a maximum and compare a wider scan; this is not certification."""
    c = dimer.universal_root(z)
    result = minimize_scalar(lambda y: -abs(ratio_profile(float(y), z)[1]),
                             bounds=(-8., c-1e-7), method='bounded',
                             options={'xatol':2e-10})
    if not result.success:
        raise ArithmeticError('Profile optimization failed.')
    k, value = ratio_profile(float(result.x), z)
    ys = np.concatenate((-np.geomspace(64, 1, 24), np.linspace(-1, c-1e-5, 60)))
    scan = [abs(ratio_profile(float(y), z)[1]) for y in ys]
    return {'z':z, 'energy_ratio_at_located_maximum':float(result.x),
            'k_at_located_maximum':k, 'K_estimate':abs(value),
            'wider_scan_maximum':max(scan), 'scan_points':len(scan),
            'scope':'Quadrature and optimization, not a uniqueness or global numerical certificate.'}


def coupling(rho: float, z: float = .75) -> tuple[float, float]:
    validate_z(z)
    if not math.isfinite(rho) or rho <= 0:
        raise ValueError('Use finite rho>0.')
    delta = rho**(1-z)
    inverse = 1/dimer.rest_threshold(z)-delta
    if inverse <= 0:
        raise ValueError('Detuning does not define a positive coupling.')
    return float(delta), float(1/inverse)


@lru_cache(maxsize=8192)
def lattice_profile(rho: float, k: float, z: float = .75) -> tuple[float, float, float]:
    """Return scaled lattice energy, velocity, and U^2*Z/rho^(2z-1)."""
    delta, U = coupling(rho, z)
    if not math.isfinite(k) or not 0 <= rho*k <= math.pi:
        raise ValueError('Use 0<=rho*k<=pi.')
    if k == 0:
        E = dimer.rest_bound_energy(z, U)
        # The rest normalization develops a narrow feature at q~|E|^(1/z).
        # Scale that feature out and split the positive integral geometrically;
        # no preserved tolerance, assertion, or scalar source is modified.
        length = (-E/2)**(1/z)
        xmax = math.pi/length
        cuts = [0., min(1., xmax)]
        while cuts[-1] < xmax:
            cuts.append(min(2*cuts[-1], xmax))
        integral = sum(quad(lambda x: (1+(x*np.sinc(length*x/(2*math.pi)))**z)**(-2),
                            a, b, epsabs=3e-11, epsrel=3e-11, limit=250)[0]
                       for a, b in zip(cuts[:-1], cuts[1:]))
        norm = length*integral/(math.pi*E**2)
        return float(E/rho**z), 0., float(1/(norm*rho**(2*z-1)))
    E, Z, v = pole(float(rho*k), z, U)
    return E/rho**z, delta*v, U*U*Z/rho**(2*z-1)


def crossing_intervals(fn: Callable[[float], float], level: float,
                       grid: np.ndarray) -> list[tuple[float, float]]:
    """Bracket all scan-detected superlevel intervals; unobserved roots possible."""
    values = np.array([abs(fn(float(k)))-level for k in grid])
    if not (values[0] < 0 and values[-1] < 0):
        raise ValueError('Both scan boundaries must lie below the level.')
    roots = []
    for a, b, fa, fb in zip(grid[:-1], grid[1:], values[:-1], values[1:]):
        if fa*fb < 0:
            roots.append(float(brentq(lambda k: abs(fn(float(k)))-level,
                                     a, b, xtol=1e-8, rtol=1e-10)))
        elif fa == 0 or fb == 0:
            raise ArithmeticError('Move a scan grid point off the crossing.')
    if len(roots) % 2:
        raise ArithmeticError('Unpaired scan crossings.')
    return list(zip(roots[::2], roots[1::2]))


def continuum_weight(level: float, z: float = .75, points: int = 96) -> dict:
    """Crossover weight on scan-detected intervals for the checked velocity range."""
    if not math.isfinite(level) or level <= 0:
        raise ValueError('Use a finite positive scaled velocity.')
    grid = np.geomspace(.2, 10000., points)
    intervals = crossing_intervals(lambda k: continuum_pole(k, z)[1], level, grid)
    weight = sum(quad(lambda k: continuum_pole(float(k), z)[2]**(-2)/math.pi,
                      a, b, epsabs=1e-6, epsrel=2e-8, limit=160)[0]
                 for a, b in intervals)
    return {'level':level, 'intervals':intervals, 'H_estimate':weight,
            'grid_points':points,
            'scope':'Scan-detected intervals only; analytical support and limits are proved separately.'}


def lattice_weight(rho: float, level: float, z: float = .75, points: int = 96) -> dict:
    """Compute U^4*Q(J*s/delta)/rho^(4z-1) on scan-detected intervals, J=1."""
    delta, U = coupling(rho, z)
    grid = np.geomspace(.2, math.pi/rho, points)
    # Avoid multiplication rounding the last physical momentum above pi.
    grid[-1] = np.nextafter(math.pi/rho, 0.)
    intervals = crossing_intervals(lambda k: lattice_profile(rho, k, z)[1], level, grid)
    def density(k: float) -> float:
        _, Z, _ = state_pole(float(rho*k), z, U)
        return (U*U*Z/rho**(2*z-1))**2/math.pi
    weight = sum(quad(density, a, b, epsabs=1e-6, epsrel=2e-8, limit=160)[0]
                 for a, b in intervals)
    return {'rho':rho, 'delta':delta, 'U_over_J':U, 'level':level,
            'intervals':intervals, 'scaled_weight':weight,
            'unconditional_Q':rho**(4*z-1)*weight/U**4,
            'grid_points':points, 'scope':'Finite quadrature on scan-detected intervals, not a finite-time measurement.'}
