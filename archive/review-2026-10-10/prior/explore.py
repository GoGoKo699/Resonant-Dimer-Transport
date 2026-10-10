from pathlib import Path
import sys,json,time
sys.dont_write_bytecode=True
from transport import *
start=time.time();z=.75
c=dimer.universal_root(z);B=1/(dimer.rest_threshold(z)**2*dimer.universal(c,z,True))
print('c,B,Uc',c,B,dimer.rest_threshold(z),flush=True)
for P in (.001,.01,.05,.1,.3,1.,2.,3.):
 print('P,E,Z,v,size',P,*pole(P,z),relative_size(P,z),flush=True)
print('Wc',weight_integral(np.pi,z,True),'Wb',weight_integral(np.pi,z,False),flush=True)
for v in (.75,1.,2.,3.):
 print('tail',v,velocity_tail(v,z),flush=True)
print('elapsed',time.time()-start,flush=True)
