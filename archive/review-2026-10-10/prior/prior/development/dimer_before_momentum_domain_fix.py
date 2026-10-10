"""Two-body fractional-lattice pilot. Units: lattice spacing = hbar = J = 1.

Endpoint substitutions explicitly remove integrable cusp singularities. Returned
numbers are floating-point quadratures, not certified numerical intervals.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma, gammaln

TOL = 3e-11


def _z(z: float) -> None:
    if not .5 < z < 1:
        raise ValueError('This pilot uses 1/2 < z < 1.')


def epsilon(k, z: float):
    return np.abs(2 * np.sin(np.asarray(k) / 2))**z


def rest_threshold(z: float) -> float:
    _z(z)
    return float(2**(1+z)*np.sqrt(np.pi)*gamma(1-z/2)/gamma((1-z)/2))


def free_rest(r: int, z: float) -> float:
    """Zero-energy rest resolvent: integral cos(r q)/(2 epsilon(q))."""
    _z(z)
    n = abs(int(r))
    value = 1 / rest_threshold(z)
    for j in range(n):
        value *= (j + z/2)/(j + 1-z/2)
    return float(value)


def hopping(r: int, z: float) -> float:
    """Off-diagonal hopping, positive in H=constant - sum t_r translations."""
    n = abs(int(r))
    if n == 0:
        raise ValueError('Use nonzero separation for a hopping coefficient.')
    return float(gamma(1+z)*np.sin(np.pi*z/2)/np.pi * np.exp(gammaln(n-z/2)-gammaln(n+1+z/2)))


def bminus(t: float, z: float) -> float:
    a = z/2*np.log1p(-t*t/4)
    b = z*np.arctanh(t/2)
    return float(np.expm1(a)+2*np.exp(a)*np.sinh(b/2)**2)


def universal(e: float, z: float, derivative: bool = False) -> float:
    """F_z(e), or its first derivative. e<=1; derivative requires e<1."""
    _z(z)
    if e > 1 or (derivative and e >= 1):
        raise ValueError('Energy must be below threshold for this integral.')
    power = 1/(1-z)
    pref = .5**(1-z)/(1-z)
    delta = 1-e
    low = 0.
    for sign in (-1,1):
        def local(v):
            if v == 0:
                return 1. if delta == 0 else 0.
            t = .5*v**power
            tz = t**z
            D = 1 + np.expm1(z*np.log1p(sign*t))/tz
            den = delta+tz*D
            if derivative:
                return tz/den**2
            return 1/D if delta == 0 else tz/den
        low += pref*quad(local,0,1,epsabs=TOL,epsrel=TOL,limit=200)[0]
    tailpower = 1/(2*z-1)
    def tail(v):
        if v == 0:
            return .25 if derivative else e/4
        t = v**tailpower
        tz = t**z
        bm = bminus(t,z)
        den = 2*(1+bm)-e*tz
        if derivative:
            return 1/den**2
        return (e-2*bm/tz)/(2*den)
    high = tailpower*quad(tail,0,1,epsabs=TOL,epsrel=TOL,limit=200)[0]
    return float((low+high-(0 if derivative else 1/(2*(1-z))))/np.pi)


def universal_root(z: float) -> float:
    return float(brentq(lambda e:universal(e,z),0,1,xtol=2e-13,rtol=1e-13))


def lattice_resolvent(E: float, P: float, z: float, r: int=0,
                      derivative: bool=False) -> float:
    """g_r(E,P)=integral cos(rq)/(epsilon(q+P/2)+epsilon(q-P/2)-E)."""
    _z(z)
    P = float(abs((P+np.pi)%(2*np.pi)-np.pi))
    if P == 0:
        if E == 0 and not derivative:
            return free_rest(r,z)
        raise ValueError('Rest energy zero is handled analytically; use P>0 otherwise.')
    edge = float(epsilon(P,z)); gap = edge-E
    if gap < 0 or (gap == 0 and derivative):
        raise ValueError('Requested resolvent is outside its finite below-band domain.')
    sP = np.sin(P/2)
    answer = 0.
    for sign,length in ((-1,P/2),(1,np.pi-P/2)):
        power = 1/(1-z)
        pref = length**(1-z)/(1-z)
        def integrand(v):
            if v == 0:
                return np.cos(r*P/2) if gap == 0 else 0.
            t = length*v**power
            tz = t**z
            change = sign*2*np.sin(t/4)*np.cos(P/2+sign*t/4)/sP
            deltaeps = edge*np.expm1(z*np.log1p(change))
            D = np.sinc(t/(2*np.pi))**z+deltaeps/tz
            den = gap+tz*D
            weight = np.cos(r*(P/2+sign*t))
            if derivative:
                return weight*tz/den**2
            return weight/D if gap == 0 else weight*tz/den
        answer += pref*quad(integrand,0,1,epsabs=TOL,epsrel=TOL,limit=250)[0]
    return float(answer/np.pi)


def contact_energy(P: float,z:float,U:float|None=None) -> float:
    if U is None:U=rest_threshold(z)
    edge=float(epsilon(P,z));target=1/U
    f=lambda E:lattice_resolvent(E,P,z)-target
    if f(edge)<=0:raise ValueError('No strictly below-band contact bound state.')
    bottom=-2*U-2
    return float(brentq(f,bottom,edge,xtol=2e-13,rtol=1e-13))


def hardcore_resolvent(E:float,P:float,z:float,derivative:bool=False)->float:
    g=np.array([lattice_resolvent(E,P,z,r) for r in (0,1,2)])
    if not derivative:
        return float(g[0]+g[2]-2*g[1]**2/g[0])
    d=np.array([lattice_resolvent(E,P,z,r,True) for r in (0,1,2)])
    return float(d[0]+d[2]-4*g[1]*d[1]/g[0]+2*g[1]**2*d[0]/g[0]**2)


def hardcore_threshold(z:float)->float:
    g=np.array([free_rest(r,z) for r in (0,1,2)])
    return float(1/(g[0]+g[2]-2*g[1]**2/g[0]))


def hardcore_energy(P:float,z:float,V:float|None=None)->float:
    if V is None:V=hardcore_threshold(z)
    edge=float(epsilon(P,z));target=1/V
    f=lambda E:hardcore_resolvent(E,P,z)-target
    if f(edge)<=0:raise ValueError('No strictly below-band even hard-core bound state.')
    return float(brentq(f,-2*V-2,edge,xtol=2e-13,rtol=1e-13))
