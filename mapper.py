# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:14:49 2020

@author: Usuario
"""

import cv2
import numpy as np
import scipy.interpolate as interp

a,b,c,d=np.loadtxt("intento_largo.txt", unpack=True)

a1 = np.linspace(0,np.pi, 100)
b1 = np.linspace(0,2*np.pi, 100)
c1=np.zeros([100,100])
d1=np.zeros([100,100])
j=0
k=0
for i in range (0,len(c)):
    c1[k,j]=c[i]
    d1[k,j]=d[i]
    k+=1
    if((k)==100):
        j+=1
        k=0
        

x, y= 2,4
z=c1

mapx= interp.RectBivariateSpline(a1, b1, c1/(2*np.pi)*260)
mapy= interp.RectBivariateSpline(a1, b1, d1/(2*np.pi)*529)


#IMAGE TRANSFORMATION


img = cv2.imread("messi5.png")

img2= np.zeros([1000,1000,3])
img3= np.zeros([1000,1000,3])

for i in range(np.shape(img)[0]):
    for j in range(np.shape(img)[1]):
        img2[i+250,j+250, :]=(img[i,j,:])*64/255.0
        iprima = int(mapx(i,j))
        jprima = int(mapx(i,j))
        if(iprima>147 && iprima<148):
            print("hey")
        img3[iprima+250,jprima+250, :] = (img[i,j,:])*64/255.0
        
cv2.imwrite('color_img.jpg', img2)
cv2.imshow("image", img2)
cv2.waitKey()

cv2.imwrite('color_img.jpg', img3)
cv2.imshow("image", img3)
cv2.waitKey()





