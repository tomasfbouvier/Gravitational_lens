# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 09:04:22 2020

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

def variables(nl, ntheta, nphi, r, theta):

    pl=nl
    ptheta=r*ntheta
    pphi=r*np.sin(theta)*nphi
    
    b=pphi
    B2=ptheta**2+pphi**2/np.sin(theta)**2

    return pl, ptheta, pphi, b, B2

rho=1
lc= 10
thetac = np.pi/2
phic = 0


thetacs=np.linspace(0,np.pi, 100)
phics=np.linspace(0, 2*np.pi, 100)


m=np.zeros([len(thetacs),len(phics)])
datos=[]

plt.figure()

for i in range(50,51):
    for j in range(50,53):

        
        Nx = np.sin(thetacs[i])*np.cos(phics[j])
        Ny = np.sin(thetacs[i])*np.sin(phics[j])
        Nz = np.cos(thetacs[i])
        
        nl=-Nx
        nphi=-Ny
        ntheta=Nz
        
        l, theta, phi = lc, thetac, phic
        t=0
        deltat= -0.01
        
        
        
        while (t>-20):
           t += deltat
           
           r= np.sqrt(l**2+rho**2)
           pl, ptheta, pphi, b, B2 = variables(nl, ntheta, nphi, r, theta) 
           
           k1l = deltat*pl
           k1theta = deltat*ptheta/r**2
           k1phi = deltat*b/(r**2*np.sin(theta)**2)
           k1pl = deltat*B2/r**3*(l/r)
           k1ptheta = deltat*(b**2/r**2)*np.cos(theta)/(np.sin(theta))**3
           l, theta, phi, pl, ptheta = l+k1l, theta+k1theta, phi+k1phi, pl+k1pl, ptheta+k1ptheta
           plt.plot(l, phi, 'b.', markersize=0.5)
        """   
           r= np.sqrt((l+k1l/2)**2+rho**2)
           pl, ptheta, pphi, b, B2 = variables(nl, ntheta, nphi, r, theta+k1theta/2)   
           
           k2l = deltat*(pl+k1l/2)
           k2theta = deltat*(ptheta+k1ptheta/2)/r**2
           k2phi = deltat*b/(r**2*np.sin(theta+k1theta/2)**2)
           k2pl = deltat*B2/r**3*((l+k1l)/r)
           k2ptheta = deltat*b**2/r**2*np.cos(theta+k1theta/2)/(np.sin(theta+k1theta/2))**3
        """

          
#           l, theta, phi, pl, ptheta = l+k2l, theta+k2theta, phi+k2phi, pl+k2pl, theta+k2ptheta
        aux=[thetacs[i], phics[j], theta, phi]
        datos.append(aux)

plt.plot(lc, phic, 'r.', markersize=20, label="posición de la cámara")
datos=np.array(datos)
np.savetxt("intento.txt",datos)        
plt.xlabel("l")
plt.ylabel("$ \phi $")
plt.legend(shadow=True, fontsize=9)
plt.savefig("ejemplo rayos")
plt.show()