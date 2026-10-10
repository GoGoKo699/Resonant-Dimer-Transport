import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma

def eps(k,z):return abs(2*np.sin(np.asarray(k)/2))**z

def Uc(z):return 2**(1+z)*np.sqrt(np.pi)*gamma(1-z/2)/gamma((1-z)/2)

def Bminus(t,z):
    a=z/2*np.log1p(-t*t/4)
    b=z*np.arctanh(t/2)
    return np.expm1(a)+2*np.exp(a)*np.sinh(b/2)**2

def F(e,z):
    if e==1:
        def inner(t,sgn):
            if t==0:return 1.
            return 1/(1+np.expm1(z*np.log1p(sgn*t))/t**z)
        lo=sum(quad(lambda t:inner(t,s),0,.5,weight='alg',wvar=(-z,0),epsabs=2e-11,epsrel=2e-11)[0] for s in [-1,1])
    else:
        lo=quad(lambda q:1/((q+.5)**z+abs(q-.5)**z-e),0,1,points=[.5],epsabs=2e-11,epsrel=2e-11)[0]
    def tail(t):
        if t==0:return e/4
        bm=Bminus(t,z)
        return (e-2*bm/t**z)/(2*(2*(1+bm)-e*t**z))
    tailint=quad(tail,0,1,weight='alg',wvar=(2*z-2,0),epsabs=2e-11,epsrel=2e-11,limit=200)[0]
    return (lo-1/(2*(1-z))+tailint)/np.pi

def I(e,K,z):
    br=sorted(set([0,K/2,K, min(2*K,np.pi),np.pi]))
    br=[b for b in br if 0<=b<=np.pi]
    def fun(q):return 1/(eps(q+K/2,z)+eps(q-K/2,z)-e)
    return sum(quad(fun,l,r,epsabs=1e-10,epsrel=1e-10,limit=250)[0] for l,r in zip(br[:-1],br[1:]))/np.pi

def Elattice(K,z,V=None):
    if V is None:V=Uc(z)
    top=float(eps(K,z))
    return brentq(lambda e:I(e,K,z)-1/V,0,top*(1-1e-7),xtol=1e-13)

if __name__=='__main__':
    for z in [.55,.6,.65,.75,.85,.9,.95]:
        c=brentq(lambda e:F(e,z),0,1,xtol=1e-13)
        print('z',z,'Uc',Uc(z),'F0',F(0,z),'F1',F(1,z),'c',c,flush=True)
        if z in [.6,.75,.9]:
            for K in [.2,.05,.01,.001]:
                E=Elattice(K,z)
                print(K,E,E/K**z,E/float(eps(K,z)),flush=True)
