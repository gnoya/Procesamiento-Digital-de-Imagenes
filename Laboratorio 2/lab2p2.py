import cv2
import numpy as np
from scipy import ndimage 
from matplotlib import pyplot as plt

#suavisado a y b

image = cv2.imread('NoyaCabrera.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
dimension=5
kernel = np.ones((dimension,dimension),np.float32)/(dimension*dimension)
dst = cv2.filter2D(image,-1,kernel)
plt.figure()
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Promedio')
plt.xticks([]), plt.yticks([])

#perfilado c
imagen=cv2.imread('Pirata.tif')
kernelp=np.ones((3,3),np.float32)*(-1)
kernelp[1,1]=8
imagenp=cv2.filter2D(imagen,-1,kernelp)
plt.figure()
plt.subplot(131),plt.imshow(imagen),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(imagenp),plt.title('Perfilado')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(imagenp+imagen),plt.title('Imagen + perfilado')
plt.xticks([]), plt.yticks([])


#Filtro gaussiano d
dim=5
gaussian=cv2.GaussianBlur (image, (dim,dim), 0)
plt.figure()
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gaussian),plt.title('Filtro gaussiano')
plt.xticks([]), plt.yticks([])
plt.show()
