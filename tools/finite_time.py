"""Finite-time bound arithmetic and static derivative diagnostics.

All spectral inputs to a certificate must be supplied as valid bounds.
This module performs no interval enclosure of the continuum variation norm.
Dimer scalar routines are explicitly reused from the preserved project.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from detuning import dimer, state_pole, validate_z
import numpy as np
from scipy.integrate import quad
from scipy.special import beta as beta_function


def nonnegative(**values: float) -> None:
    for name, value in values.items():
        if not math.isfinite(value) or value < 0:
            raise ValueError(f'{name} must be finite and nonnegative.')


def error_bound(q: float, band_error: float, continuum_norm: float) -> float:
    """F4, uncapped; validity is conditional on the supplied error budgets."""
    nonnegative(q=q, band_error=band_error, continuum_norm=continuum_norm)
    if q > 1:
        raise ValueError('An unconditional event probability cannot exceed one.')
    return (band_error + 2*math.sqrt(q+band_error)*continuum_norm
            + continuum_norm**2)


def band_budget(a: float, h: float, mass: float,
                zprime_norm: float, curvature_weight_norm: float) -> float:
    """A(h) in F3, with normalized momentum L2 norms."""
    nonnegative(a=a, h=h, mass=mass, zprime_norm=zprime_norm,
                curvature_weight_norm=curvature_weight_norm)
    if a == 0 or h == 0 or mass > 1:
        raise ValueError('Require a,h>0 and 0<=mass<=1.')
    return math.sqrt(mass)/math.pi * (
        9*a*zprime_norm/h + 27*a*a*curvature_weight_norm/(2*h*h))


@dataclass(frozen=True)
class TimeBudget:
    """Algebraic sufficient time, conditional on valid static inputs."""
    q: float
    relative_accuracy: float
    shell_mass_bound: float
    excluded_mass_bound: float
    band_coefficient_bound: float
    continuum_variation_norm_bound: float

    def sufficient_time(self) -> float:
        nonnegative(q=self.q, relative_accuracy=self.relative_accuracy,
                    shell_mass_bound=self.shell_mass_bound,
                    excluded_mass_bound=self.excluded_mass_bound,
                    band_coefficient_bound=self.band_coefficient_bound,
                    continuum_variation_norm_bound=self.continuum_variation_norm_bound)
        if not 0 < self.q <= 1 or not 0 < self.relative_accuracy <= 1:
            raise ValueError('Require 0<q<=1 and 0<relative accuracy<=1.')
        q, eps = self.q, self.relative_accuracy
        if self.shell_mass_bound > eps*q/6:
            raise ValueError('Shell bound exceeds its relative-error allocation.')
        if self.excluded_mass_bound > eps*eps*q/144:
            raise ValueError('Excluded-momentum bound exceeds its allocation.')
        return max(6*self.band_coefficient_bound/(eps*q),
                   12*self.continuum_variation_norm_bound/(eps*math.sqrt(q)))

    def bound_at(self, t: float) -> float:
        self.sufficient_time()  # Validate every allocation before arithmetic.
        if not math.isfinite(t) or t <= 0:
            raise ValueError('Use a finite positive time.')
        eta = math.sqrt(self.excluded_mass_bound
                        + (self.continuum_variation_norm_bound/t)**2)
        return error_bound(self.q, self.shell_mass_bound+self.band_coefficient_bound/t, eta)


def uniform_sum_cdf(x):
    """Exact CDF of the sum of three independent Uniform[-1/3,1/3]."""
    x = np.asarray(x, dtype=float)
    y = (3*x+3)/2
    ans = sum((-1)**k*math.comb(3,k)*np.maximum(y-k,0)**3 for k in range(4))/6
    # Outside support avoid cancellation in the truncated-power representation.
    return np.where(x <= -1, 0., np.where(x >= 1, 1., np.clip(ans,0,1)))


def smoothed_inside(x, radius: float, h: float):
    if radius < 0 or h <= 0:
        raise ValueError('Require radius>=0 and h>0.')
    x = np.asarray(x)
    return uniform_sum_cdf((x+radius)/h)-uniform_sum_cdf((x-radius)/h)


def epsilon_prime(k: float, z: float) -> float:
    s = 2*math.sin(k/2)
    if s == 0:
        raise ValueError('The derivative has a cusp at this momentum.')
    return z*math.cos(k/2)*math.copysign(abs(s)**(z-1),s)


def static_derivatives(P: float, z: float, U: float) -> dict:
    """Independent uncentered first-derivative integrals for E'', Z', J=1.

    The energy and contact normalization reuse the preserved scalar solver.
    Quadrature of F12 avoids epsilon'' entirely. Values are diagnostics, not
    outward-rounded bounds. Use momenta strictly inside (0,pi).
    """
    validate_z(z)
    if not math.isfinite(P) or not 0 < P < math.pi or U <= dimer.rest_threshold(z):
        raise ValueError('Use 0<P<pi and U>Uc in this diagnostic.')
    E, Z, IE = state_pole(P,z,U)
    def integrate(fn):
        return sum(quad(fn,lo,hi,epsabs=3e-10,epsrel=3e-10,limit=220)[0]
                   for lo,hi in ((0.,P),(P,2*math.pi)))/(2*math.pi)
    def den(k):
        return float(dimer.epsilon(k,z)+dimer.epsilon(P-k,z)-E)
    IP = -integrate(lambda k: epsilon_prime(P-k,z)/den(k)**2)
    IPE = -2*integrate(lambda k: epsilon_prime(P-k,z)/den(k)**3)
    IEE = 2*integrate(lambda k: den(k)**(-3))
    IPP = 2*integrate(lambda k: epsilon_prime(k,z)*epsilon_prime(P-k,z)/den(k)**3)
    velocity = -IP/IE
    curvature = -(IPP+2*IPE*velocity+IEE*velocity**2)/IE
    residue_derivative = -(IPE+IEE*velocity)/(U*U*IE*IE)
    return dict(P=P,z=z,U=U,E=E,Z=Z,IE=IE,IP=IP,IPE=IPE,IEE=IEE,
                IPP=IPP,velocity=velocity,curvature=curvature,
                residue_derivative=residue_derivative)


def conservative_norm_envelope(z: float, U: float) -> dict:
    """F11--F12 envelope using g=-E(0), J=1; numerical g is not certified."""
    validate_z(z)
    if U <= dimer.rest_threshold(z):
        raise ValueError('Require U>Uc.')
    g = -dimer.rest_bound_energy(z,U)
    L = 2**(z+1)+U
    l1 = 2**z/math.pi
    l2 = z*z*2**(2*z-2)*beta_function(z-.5,1.5)/math.pi
    vs = L*L*l1/g**2
    curvature = 2*L*L/g**3*(l2+2*l1*vs+vs*vs)
    zp = 2*L**4/(U*U*g**3)*(l1+vs)
    return dict(gap_lower_bound=g,velocity_upper_bound=vs,
                curvature_upper_bound=curvature,residue_derivative_upper_bound=zp,
                epsilon_derivative_L1=l1,epsilon_derivative_L2_squared=float(l2))


def continuum_density(E: float, P: float, z: float, U: float) -> float:
    """Contact continuous density from a principal-value quadrature, J=1.

    This is a diagnostic for energies separated from the three critical values.
    It does not enclose the variation integral in F2. Cauchy quadrature removes
    simple on-shell poles; a local Taylor quotient limits cancellation near a
    root. Critical energies themselves are deliberately excluded.
    """
    from scipy.optimize import brentq
    validate_z(z)
    if not 0 < P < math.pi or not math.isfinite(U) or U <= dimer.rest_threshold(z):
        raise ValueError('Require 0<P<pi and finite U>Uc.')
    def energy(q):
        return float(dimer.epsilon(q+P/2,z)+dimer.epsilon(q-P/2,z))
    threshold=float(dimer.epsilon(P,z));middle=energy(0.);top=energy(math.pi)
    if not threshold < E < top or E == middle:
        raise ValueError('Use an interior noncritical continuum energy.')
    def derivative(q):
        return epsilon_prime(q+P/2,z)+epsilon_prime(q-P/2,z)
    def second(k):
        return z*abs(2*np.sin(k/2))**(z-2)*((z-1)*np.cos(k/2)**2-np.sin(k/2)**2)
    free_density=0.;real_resolvent=0.
    for lo,hi in ((0.,P/2),(P/2,math.pi)):
        if (energy(lo)-E)*(energy(hi)-E) < 0:
            root=brentq(lambda q:energy(q)-E,lo,hi,xtol=5e-15)
            slope=derivative(root)
            curvature=second(root+P/2)+second(root-P/2)
            root_energy=energy(root)
            def quotient(q):
                dx=q-root
                if abs(dx)<min(1e-6,abs(root-P/2)*1e-4):
                    return 1/(slope+.5*curvature*dx)
                return dx/(energy(q)-root_energy)
            integral=quad(quotient,lo,hi,weight='cauchy',wvar=root,
                          epsabs=3e-8,epsrel=3e-8,limit=240)[0]
            free_density += 1/(math.pi*abs(slope))
        else:
            integral=quad(lambda q:1/(energy(q)-E),lo,hi,
                          epsabs=3e-8,epsrel=3e-8,limit=240)[0]
        real_resolvent += integral/math.pi
    return float(free_density/((1-U*real_resolvent)**2+(U*math.pi*free_density)**2))
