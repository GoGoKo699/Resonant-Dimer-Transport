"""Preparation-resolved dimer quantities. Units J=hbar=lattice spacing=1.

The preserved pilot supplies the tested scalar pole/resolvent routines.
This module adds derivative, coincidence, and wavefunction-size quadratures.
Numerical values are diagnostics, not certified intervals.
"""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import sys
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent/'prior'))
import dimer


def epsprime(k,z):
    k=np.asarray(k);s=2*np.sin(k/2)
    if np.any(s==0):
        raise ValueError('Derivative undefined at a zero momentum.')
    return z*np.cos(k/2)*np.sign(s)*np.abs(s)**(z-1)


@lru_cache(maxsize=12000)
def pole(P:float,z:float=.75,U:float|None=None):
    if not 0<P<=np.pi:raise ValueError('Use 0<P<=pi')
    if U is None:U=dimer.rest_threshold(z)
    E=dimer.contact_energy(P,z,U)
    norm=dimer.lattice_resolvent(E,P,z,derivative=True)
    Z=1/(U*U*norm)
    # Divide the interval at both moving cusps. A t^(1/z) substitution
    # cancels their integrable derivative singularity without sampling it.
    total=0.;power=1/z
    for sign,length in ((-1,P/2),(1,np.pi-P/2)):
        def f(v):
            if v==0:
                gap=dimer.epsilon(P,z)-E
                return -sign*length**z/(2*gap**2)
            u=length*v**power;q=P/2+sign*u
            Ap=(epsprime(P+sign*u,z)-epsprime(sign*u,z))/2
            den=dimer.epsilon(P+sign*u,z)+dimer.epsilon(u,z)-E
            return float(Ap/den**2*length*power*v**(power-1))
        total+=quad(f,0,1,epsabs=3e-10,epsrel=3e-10,limit=200)[0]
    velocity=total/(np.pi*norm)
    return float(E),float(Z),float(velocity)


def weight_integral(pmax:float,z:float=.75,squared:bool=True):
    """Integral over both signs |P|<pmax, measure dP/(2pi)."""
    if pmax<=0:return 0.
    power=1/(4*z-1 if squared else 2*z)
    def f(s):
        if s==0:return 0.
        P=pmax*s**power
        Z=pole(float(P),z)[1]
        return Z**(2 if squared else 1)*pmax*power*s**(power-1)/np.pi
    return quad(f,0,1,epsabs=2e-10,epsrel=2e-8,limit=80)[0]


def velocity_tail(v:float,z:float=.75):
    """Small-P tail cutoff; monotonicity must be checked on the used branch.

    The theorem's high-v asymptotic needs no global monotonicity. This numerical
    function uses a sign bracket for the single near-zero root only.
    """
    if v<=0:raise ValueError('Positive velocity required')
    c=dimer.universal_root(z)
    estimate=(z*c/v)**(1/(1-z))
    lo=max(estimate/3,1e-8);hi=min(estimate*3,np.pi)
    if pole(lo,z)[2]<=v or pole(hi,z)[2]>=v:
        raise ValueError('No certified numerical root bracket supplied')
    cut=brentq(lambda P:pole(float(P),z)[2]-v,lo,hi,xtol=1e-11,rtol=1e-10)
    return float(cut),float(weight_integral(cut,z,True))


def relative_size(P:float,z:float=.75):
    E,Z,_=pole(P,z)
    norm=dimer.lattice_resolvent(E,P,z,derivative=True)
    power=1/(2*z-1);out=0.
    for sign,length in ((-1,P/2),(1,np.pi-P/2)):
        def f(v):
            if v==0:
                return z*z*length**(2*z-1)*power/(dimer.epsilon(P,z)-E)**4
            u=length*v**power
            # Avoid the artificial infinite numerator at subnormal u by
            # factoring out the singular power analytically.
            reg=epsprime(P+sign*u,z)*u**(1-z)+sign*z*np.cos(u/2)*np.sinc(u/(2*np.pi))**(z-1)
            den=dimer.epsilon(P+sign*u,z)+dimer.epsilon(u,z)-E
            return float(reg**2*length**(2*z-1)*power/den**4)
        out+=quad(f,0,1,epsabs=2e-8,epsrel=2e-8,limit=200)[0]
    return float(np.sqrt(out/(np.pi*norm)))


def size_constant(z:float=.75):
    c=dimer.universal_root(z);power=1/(2*z-1);length=.5
    low=0.
    for sign in (-1,1):
        def f(v):
            u=length*v**power
            reg=z*((1+sign*u)**(z-1)*u**(1-z)+sign)
            den=(1+sign*u)**z+u**z-c
            return reg**2*length**(2*z-1)*power/den**4
        low+=quad(f,0,1,epsabs=2e-10,epsrel=2e-10,limit=160)[0]
    def f(t):
        if t==0:return 0.
        B=(1+t/2)**z+(1-t/2)**z
        Bp=z*((1+t/2)**(z-1)+(1-t/2)**(z-1))
        return t**(2*z)*Bp**2/(B-c*t**z)**4
    high=quad(f,0,1,epsabs=2e-10,epsrel=2e-10,limit=160)[0]
    return float(np.sqrt((low+high)/(np.pi*dimer.universal(c,z,True))))
