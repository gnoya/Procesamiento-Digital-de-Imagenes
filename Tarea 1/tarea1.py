import cv2
import numpy as np 
from matplotlib import pyplot as plt
    
Nletras=0
img1=cv2.imread('test1.png')
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

#Eliminar ruido
kernel=np.ones((1,1),np.uint8)
img=cv2.dilate(img,kernel,iterations=1)
img=cv2.erode(img,kernel,iterations=1)

#Creacion imagen binaria
img= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,31,2)

#Barrido con elemento estructurante
kernel=np.ones((5,1),np.uint8)
img=cv2.dilate(img,kernel,iterations=1)
img=cv2.erode(img,kernel,iterations=1)

#buscar contornos
(_,contorno,_)=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contorno:
    (x,y,w,h)=cv2.boundingRect(c)
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),1,cv2.LINE_AA)
    Nletras+=1

plt.imshow(img1)
print(Nletras)
plt.show()
