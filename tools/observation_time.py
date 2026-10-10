"""Static diagnostics for the joint observation-time theorem.

No numerical output here is an interval enclosure. The boundary loop evaluates
an actual lattice continuum, not a finite ring or broadened discrete spectrum.
The already preserved scalar dispersion and first derivative are reused.
"""
from __future__ import annotations
import math
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from finite_time import dimer, epsilon_prime


def check_z(z: float) -> None:
    if not math.isfinite(z) or not .5 < z < 1:
        raise ValueError('Require 1/2<z<1.')


def sufficient_exponent(z: float) -> float:
    """O1: a sufficient, not an optimal or necessary, waiting-time exponent."""
    check_z(z)
    return (3*z-.5)/(1-z) if z <= .75 else (5*z-2)/(1-z)


def time_scale(delta: float, z: float) -> float:
    """Detuning factor in O2 only; its unknown theorem constant is NOT one."""
    check_z(z)
    if not math.isfinite(delta) or not 0 < delta < 1:
        raise ValueError('Require 0<delta<1.')
    log_factor = math.sqrt(math.log(2/delta)) if z == .75 else 1.
    return delta**(-sufficient_exponent(z))*log_factor


def power_integral(exponent: float, rho: float, upper: float = math.pi) -> float:
    """Exact integral of (P+rho)^exponent from 0 to upper, up to roundoff."""
    if not all(math.isfinite(x) for x in (exponent,rho,upper)) or rho <= 0 or upper <= 0:
        raise ValueError('Use finite exponent and positive finite cutoffs.')
    a = exponent+1
    log_ratio = math.log1p(upper/rho)
    if a == 0:
        return log_ratio
    return rho**a*math.expm1(a*log_ratio)/a


def norm_power_budget(z: float, delta: float) -> dict:
    """O14 integral factors with unit envelope constants; not physical norms."""
    check_z(z)
    if not math.isfinite(delta) or not 0 < delta < 1:
        raise ValueError('Require 0<delta<1.')
    rho = delta**(1/(1-z))
    n1 = math.sqrt(power_integral(4*z-4,rho)/math.pi)
    n2 = math.sqrt(power_integral(6*z-6,rho)/math.pi)
    return dict(rho=rho,residue_norm_factor=n1,curvature_norm_factor=n2,
                scaled_band_factor=delta*n1+delta**2*n2,
                mass_power=rho**(4*z-1))


def kinetic_second(k: float, z: float) -> float:
    s = abs(2*np.sin(k/2))
    if s == 0:
        raise ValueError('Do not evaluate the second derivative at a cusp.')
    return float(z*s**(z-2)*((z-1)*np.cos(k/2)**2-np.sin(k/2)**2))


def peak_constants(z: float) -> dict:
    check_z(z)
    a = z*(1-z)*2**(2-z)
    x = brentq(lambda x:(x+.5)**z+(x-.5)**z-2**(1-z),.5,2,xtol=1e-14)
    d = z*((x+.5)**(z-1)+(x-.5)**(z-1))
    return dict(a=a,outer_root=float(x),outer_slope=float(d))


def boundary_loop(energy: float, P: float, z: float, J: float = 1.) -> complex:
    """Actual lattice I_P(E+i0) just above the inner maximum.

    Scale q=P*x around the two cusps and the simple outer root. Evaluate its
    real part by a Cauchy quadrature, and its imaginary part from the on-shell
    inverse slope. Geometric outer intervals avoid losing the low-momentum
    contribution. This deliberately supports only an interior low-energy
    region with 0<P<pi/4 and m(P)<E<A_P(4P), not all band energies.
    """
    check_z(z)
    if not all(math.isfinite(x) for x in (energy,P,J)) or J <= 0 or not 0<P<math.pi/4:
        raise ValueError('Require finite J>0 and 0<P<pi/4.')
    e = energy/(J*P**z)
    def b(x):
        return float(dimer.epsilon(P*(x+.5),z)+dimer.epsilon(P*(x-.5),z))/P**z
    if not b(0)<e<b(4):
        raise ValueError('Use an energy above the inner maximum and below A_P(4P).')
    def bp(x):
        return P**(1-z)*(epsilon_prime(P*(x+.5),z)+epsilon_prime(P*(x-.5),z))
    root = brentq(lambda x:b(x)-e,.5,4,xtol=1e-14)
    slope = bp(root)
    curvature = P**(2-z)*(kinetic_second(P*(root+.5),z)+kinetic_second(P*(root-.5),z))
    root_energy = b(root)
    def quotient(x):
        dx=x-root
        if abs(dx)<1e-5:
            return 1/(slope+.5*curvature*dx)
        return dx/(b(x)-root_energy)
    inner = quad(lambda x:1/(b(x)-e),0,.5,epsabs=1e-9,epsrel=1e-9,limit=200)[0]
    near = quad(quotient,.5,4,weight='cauchy',wvar=root,
                epsabs=1e-9,epsrel=1e-9,limit=200)[0]
    points=[4*P]
    while points[-1]*4<math.pi:
        points.append(points[-1]*4)
    points.append(math.pi)
    def integrand(q):
        return 1/(dimer.epsilon(q+P/2,z)+dimer.epsilon(q-P/2,z)-energy/J)
    far=sum(quad(integrand,lo,hi,epsabs=1e-10,epsrel=1e-10,limit=150)[0]
            for lo,hi in zip(points[:-1],points[1:]))
    return complex(((inner+near)*P**(1-z)+far)/(math.pi*J),
                   P**(1-z)/(J*slope))


def contact_density(energy: float, P: float, z: float, U: float, J: float = 1.) -> float:
    if not math.isfinite(U) or U <= J*dimer.rest_threshold(z):
        raise ValueError('Use finite U>Uc for this diagnostic.')
    val = boundary_loop(energy,P,z,J)
    return float(val.imag/(math.pi*U**2*abs(val-1/U)**2))


def continuum_peak(P: float, z: float, U: float, J: float = 1.) -> dict:
    """Numerical real-denominator zero, linewidth and Lorentz-profile check.

    The derivative uses a small centered energy difference. No pole on a
    nonphysical sheet or exponential law for the full time evolution is inferred.
    The root bracket is local to the small-P asymptotic regime.
    """
    check_z(z)
    uc=J*dimer.rest_threshold(z)
    if not math.isfinite(U) or U <= uc or not math.isfinite(J) or J <= 0:
        raise ValueError('Require finite J>0 and U>Uc.')
    c=peak_constants(z);delta=J*(1/uc-1/U)
    middle=2*J*float(dimer.epsilon(P/2,z))
    shift0=J*P**(2-z)/(4*c['a']*delta**2)
    fun=lambda x:boundary_loop(middle+x*shift0,P,z,J).real-1/U
    r=brentq(fun,.03,10,xtol=1e-10)
    center=middle+r*shift0
    imag=boundary_loop(center,P,z,J).imag
    def slope(h):
        return (boundary_loop(center+h,P,z,J).real-boundary_loop(center-h,P,z,J).real)/(2*h)
    derivative=slope(shift0*1e-4)
    refined=slope(shift0*5e-5)
    if derivative <= 0:
        raise ArithmeticError('The local real-part slope was not positive.')
    width=imag/derivative; height=1/(math.pi*U**2*imag)
    profile=[contact_density(center+x*width,P,z,U,J)/height for x in (-1.,0.,1.)]
    width0=J*P**(3-2*z)/(2*c['a']*c['outer_slope']*delta**3)
    height0=J*c['outer_slope']/(math.pi*U**2)*P**(z-1)
    return dict(P=P,z=z,U=U,J=J,delta=delta,middle=middle,center=float(center),
                shift_ratio=float(r),width=float(width),width_ratio=float(width/width0),
                height=float(height),height_ratio=float(height/height0),
                derivative_refinement_relative=float(abs(refined/derivative-1)),
                scaled_profile=[float(x) for x in profile])
