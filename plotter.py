# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:55:09 2020

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

a,b,c,d=np.loadtxt("intento_largo.txt", unpack=True)

a1 = np.linspace(0,np.pi, int(np.sqrt(len(a))))
b1 = np.linspace(0,2*np.pi, int(np.sqrt(len(a))))
a1,b1=np.meshgrid(a1,b1)
m=np.zeros([int(np.sqrt(len(a))),int(np.sqrt(len(a)))])
j=0
k=0
for i in range (0,len(c)):
    m[k,j]=np.sqrt((d[i]-b[i])**2)
    if(m[k,j]>20):
        m[k,j]=m[k-1,j]
    k+=1
    if((k)==int(np.sqrt(len(a)))):
        j+=1
        k=0
        
surf = ax.plot_surface(a1, b1, m , cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_xlabel('$ \Theta_{sc} $ ')
ax.set_ylabel('$\phi_{sc} $')
ax.set_zlabel('Deviation')

# Customize the z axis.
ax.set_zlim(0, 10)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()



plt.savefig("buraco")