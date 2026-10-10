from pathlib import Path
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent/'prior'/'prior'))
import dimer
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
z=.75;c=dimer.universal_root(z);F=dimer.universal(c,z,True)
C=gamma(1-z)*np.sin(np.pi*z/2)/(2*np.pi*np.sqrt(F))
print('c,F,smallwindow',c,F,2*C*C/(2*z-1))
for P in (.2,.05,.0125):
 E=dimer.contact_energy(P,z);I2=dimer.lattice_resolvent(E,P,z,derivative=True)
 def f(x):
  b=abs(x+.5)**z+abs(x-.5)**z
  den=dimer.epsilon(P*(x+.5),z)+dimer.epsilon(P*(x-.5),z)-E
  return np.sqrt(P)/(np.sqrt(I2)*den*np.sqrt(F)*(b-c))
 cuts=sorted(set([0.,.5,1.,2.,4.,8.,16.,32.,np.pi/P]))
 cuts=[x for x in cuts if x<=np.pi/P]
 overlap=sum(quad(f,a,b,epsabs=1e-10,epsrel=1e-10,limit=150)[0] for a,b in zip(cuts[:-1],cuts[1:]))/np.pi
 print('scaling',P,'overlap',overlap,'L2 distance',np.sqrt(max(0,2-2*overlap)))
 for nq in (8192,16384):
  q=2*np.pi*np.arange(nq)/nq-np.pi
  a=dimer.epsilon(q+P/2,z)+dimer.epsilon(q-P/2,z)
  vm=1/(a-E);vm/=np.linalg.norm(vm)
  vr=np.fft.fftshift(np.fft.fft(np.fft.ifftshift(vm),norm='ortho'))
  r=np.arange(nq)-nq//2
  masses=[]
  for window in (.25,1.,4.):
   R=int(window/P)
   masses.append(float(np.sum(abs(vr[abs(r)<=R])**2)))
  print('profile',nq,masses)
