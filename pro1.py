import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500)
F=250;
fs=10000;
s1=0.5*np.cos(2*np.pi*F/fs*n+np.pi/2)
s2=1*np.cos(2*np.pi*F/fs*n+np.pi/2)
s=s1+s2
plt.subplot(2,2,1);
plt.stem(n,s);
u1=0.5*np.cos(2*np.pi*F/fs*n+np.pi/2)
F1=100;
fs1=10000;
u2=0.5*np.cos(2*np.pi*F1/fs1*n+np.pi/2)
u=u1+u2
plt.subplot(2,2,2);
plt.stem(n,u);
p1=0.5*np.cos(2*np.pi*F/fs*n+np.pi)
p2=0.5*np.cos(2*np.pi*F/fs*n+np.pi/2)
p=p1+p2
plt.subplot(2,2,3);
plt.stem(n,p);
plt.show()
