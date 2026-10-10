"""Finite-time estimates and diagnostics, in dimensionless energy and time.

The proof is research/FINITE_TIME.md. Numerical quadratures are diagnostics,
not interval certificates. No prior module is imported by this helper.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import beta, gamma


def validate_z(z: float) -> None:
    if not math.isfinite(z) or not .5 < z < 1:
        raise ValueError('Require finite 1/2 < z < 1.')


def critical_coupling(z: float) -> float:
    validate_z(z)
    return float(2**(1+z)*np.sqrt(np.pi)*gamma(1-z/2)/gamma((1-z)/2))


def epsilon(q, z: float):
    return np.abs(2*np.sin(np.asarray(q)/2))**z


def derivative(q, z: float, order: int = 1):
    """Classical derivative away from the cusp, for orders one through three."""
    k = np.remainder(np.asarray(q), 2*np.pi)
    s, c = np.sin(k/2), np.cos(k/2)
    if np.any(s == 0):
        raise ValueError('No classical derivative at a momentum cusp.')
    if order == 1:
        return z*2**(z-1)*s**(z-1)*c
    if order == 2:
        return -z*2**(z-2)*s**(z-2)*(1-z*c*c)
    if order == 3:
        return z*2**(z-3)*s**(z-3)*c*((z-1)*(z-2)*c*c-(3*z-2)*s*s)
    raise ValueError('Use derivative order 1, 2, or 3.')


def half_arcs(P: float, z: float) -> tuple[float, float, float, float]:
    validate_z(z)
    if not math.isfinite(P) or not 0 <= P <= math.pi:
        raise ValueError('Use 0 <= P <= pi.')
    return P/2, float(epsilon(P,z)), float(2*epsilon(P/2,z)), float(2*epsilon(np.pi-P/2,z))


def free_preimages(e: float, P: float, z: float) -> list[float]:
    a, low, middle, high = half_arcs(P,z)
    if not low < e < high or e == middle:
        raise ValueError('Use a regular interior energy, excluding critical values.')
    f = lambda q: float(epsilon(q+a,z)+epsilon(q-a,z)-e)
    roots = []
    if P > 0 and e < middle:
        roots.append(float(brentq(f,0,a,xtol=2e-14,rtol=1e-14)))
    roots.append(float(brentq(f,a,np.pi,xtol=2e-14,rtol=1e-14)))
    return roots


def free_density(e: float, P: float, z: float) -> tuple[float, float, float]:
    """Density and its first two energy derivatives from inverse branches."""
    a = P/2
    r0 = r1 = r2 = 0.0
    for q in free_preimages(e,P,z):
        d1 = float(derivative(q+a,z)+derivative(q-a,z))
        d2 = float(derivative(q+a,z,2)+derivative(q-a,z,2))
        d3 = float(derivative(q+a,z,3)+derivative(q-a,z,3))
        r0 += 1/abs(d1)
        r1 += -d2/abs(d1)**3
        r2 += -d3/(d1*abs(d1)**3)+3*d2*d2/abs(d1)**5
    return r0/np.pi, r1/np.pi, r2/np.pi


def _increment(k: float, h: float, z: float) -> float:
    """Stable epsilon(k+h)-epsilon(k) for small h with no cusp crossing."""
    ratio_change = 2*np.sin(h/4)*np.cos(k/2+h/4)/np.sin(k/2)
    if ratio_change <= -1:
        return float(epsilon(k+h,z)-epsilon(k,z))
    return float(epsilon(k,z)*np.expm1(z*np.log1p(ratio_change)))


def boundary_resolvent(e: float, P: float, z: float) -> complex:
    """Upper boundary value using Cauchy-weight quadrature on each half-arc.

    The removable root value is evaluated analytically. A stable trigonometric
    energy increment avoids subtracting nearly equal numbers near that root.
    """
    a, low, middle, high = half_arcs(P,z)
    roots = free_preimages(e,P,z)
    result = 0.0
    for lo, hi in ((0.,a),(a,np.pi)):
        if hi == lo:
            continue
        inside = [q for q in roots if lo < q < hi]
        energy = lambda q: float(epsilon(q+a,z)+epsilon(q-a,z))
        if not inside:
            result += quad(lambda q: 1/(energy(q)-e), lo, hi,
                           epsabs=2e-9,epsrel=2e-9,limit=200)[0]
            continue
        root = inside[0]
        slope = float(derivative(root+a,z)+derivative(root-a,z))
        local_radius = 1e-3*min(root-lo,hi-root)
        def regular(q: float) -> float:
            h = q-root
            if h == 0:
                return 1/slope
            if abs(h) < local_radius:
                den = _increment(root+a,h,z)+_increment(root-a,h,z)
            else:
                den = energy(q)-e
            return h/den
        result += quad(regular,lo,hi,weight='cauchy',wvar=root,
                       epsabs=2e-9,epsrel=2e-9,limit=200)[0]
    return complex(result/np.pi, np.pi*free_density(e,P,z)[0])


def contact_density(e: float, P: float, z: float, u: float) -> float:
    if not math.isfinite(u) or u <= 0:
        raise ValueError('Require finite u > 0.')
    m = boundary_resolvent(e,P,z)
    return float(m.imag/(np.pi*abs(1-u*m)**2))


def spectral_constants(z: float) -> dict[str, float]:
    """Explicit nonoptimized constants from (F6)--(F10), with u_min=u_c."""
    validate_z(z)
    r = (1-z)/z
    beta_exp = 1-r
    uc = critical_coupling(z)
    L1 = z*(2/np.pi)**(z-1)
    L2 = z*(2/np.pi)**(z-2)
    L3 = z*(2/np.pi)**(z-3)*((1-z)*(2-z)+abs(3*z-2))
    concavity = z*(1-z)*2**(z-1)
    slope = math.sqrt(2*concavity)
    c = 1/(np.pi*2**(1+r)*L1)
    A2 = 2*L2*2**((2-z)/z)
    A3 = 2*L3*2**((3-z)/z)
    R1 = 2*A2/(np.pi*slope**3)
    R2 = 2/np.pi*(A3/slope**4+3*A2**2/slope**5)
    Cm = 2**(4/z+.5)*R2+32+np.pi*R1
    W0 = 1/(np.pi**2*uc**2*c)
    W1 = Cm/(np.pi**3*uc**2*c*c)
    coefficient = 3*2**beta_exp*W0/beta_exp+8*W0+4*W1
    gamma_exp = (4*z-2)/(10-z)
    alpha_exp = (4*z-1)/(1-z)
    return {'r':r,'beta':beta_exp,'m':6/z-2.5,'gamma':gamma_exp,
            'alpha':alpha_exp,'time_exponent':alpha_exp/(2*gamma_exp),
            'band_time_exponent':(5*z+1)/(1-z),'concavity':concavity,
            'free_density_lower_coefficient':c,'free_density_derivative_R1':R1,
            'free_density_second_derivative_R2':R2,'density_envelope_W0':W0,
            'density_derivative_W1':W1,'continuum_coefficient':coefficient}


def continuum_bound(tau: float, z: float) -> float:
    if not math.isfinite(tau) or tau < 1:
        raise ValueError('Require finite dimensionless time tau >= 1.')
    d = spectral_constants(z)
    return min(1.0, d['continuum_coefficient']*tau**(-d['gamma']))


def band_bounds(z: float, u: float, binding_lower: float,
                velocity_upper: float | None = None) -> dict[str,float]:
    """Derivative bounds given valid static bounds, not a numerical optimizer.

    binding_lower must be a valid positive lower bound on -E_d(0)/J.
    If velocity_upper is omitted, the elementary bound is used. Supplying an
    unvalidated optimized value does not turn this calculation into a certificate.
    """
    validate_z(z)
    if not math.isfinite(u) or u <= critical_coupling(z):
        raise ValueError('Require u > u_c.')
    if not math.isfinite(binding_lower) or binding_lower <= 0:
        raise ValueError('Require a valid positive rest-binding lower bound.')
    L = 2**(1+z)+u
    F1 = 2**z/np.pi
    F2sq = z*z*2**(2*z-2)*beta(z-.5,1.5)/np.pi
    if velocity_upper is None:
        velocity_upper = F1*L*L/binding_lower**2
    if not math.isfinite(velocity_upper) or velocity_upper < 0:
        raise ValueError('Require a valid nonnegative velocity upper bound.')
    H = 2*L*L/binding_lower**3*(F2sq+2*F1*velocity_upper+velocity_upper**2)
    Z1 = 2*L**4/binding_lower**3*(F1+velocity_upper)/u**2
    return {'velocity_upper':float(velocity_upper),'energy_second_derivative':float(H),
            'residue_first_derivative':float(Z1),'F1':float(F1),'F2_squared':float(F2sq)}


def event_error_bound(q: float, boundary_mass: float, band_error: float,
                      continuum_norm: float) -> float:
    """Absolute error (F15), given validated nonnegative input bounds."""
    values = (q,boundary_mass,band_error,continuum_norm)
    if any(not math.isfinite(x) or x < 0 for x in values):
        raise ValueError('All arguments must be finite and nonnegative.')
    D = boundary_mass+band_error
    return D+2*math.sqrt(q+D)*continuum_norm+continuum_norm**2


def smoothing_cdf(x):
    """CDF of the four-uniform mollifier supported on [-1,1]."""
    x = np.asarray(x,dtype=float)
    y = 2*x+2
    ans = sum((-1)**k*math.comb(4,k)*np.maximum(y-k,0)**4 for k in range(5))/math.factorial(4)
    return np.where(x <= -1,0.,np.where(x >= 1,1.,ans))


def smoothed_interval(y, radius: float, width: float):
    if radius <= 0 or width <= 0:
        raise ValueError('Require positive radius and smoothing width.')
    y = np.asarray(y)
    return smoothing_cdf((y+radius)/width)-smoothing_cdf((y-radius)/width)
