import cv2
import numpy as np
from scipy import ndimage 
from matplotlib import pyplot as plt

#suavizado a y b

# image = cv2.imread('NoyaCabrera.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# dimension=5
# kernel = np.ones((dimension,dimension),np.float32)/(dimension*dimension)
# dst = cv2.filter2D(image,-1,kernel)
# plt.figure()
# plt.subplot(121),plt.imshow(image),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Promedio')
# plt.xticks([]), plt.yticks([])

# #perfilado c
# imagen=cv2.imread('Pirata.tif')
# kernelp=np.ones((3,3),np.float32)*(-1)
# kernelp[1,1]=8
# imagenp=cv2.filter2D(imagen,-1,kernelp)
# plt.figure()
# plt.subplot(131),plt.imshow(imagen),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(132),plt.imshow(imagenp),plt.title('Perfilado')
# plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(imagenp+imagen),plt.title('Imagen + perfilado')
# plt.xticks([]), plt.yticks([])


# #Filtro gaussiano d
# dim=5
# gaussian=cv2.GaussianBlur (image, (dim,dim), 0)
# plt.figure()
# plt.subplot(121),plt.imshow(image),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(gaussian),plt.title('Filtro gaussiano')
# plt.xticks([]), plt.yticks([])
# plt.show()

#Parte e

img = cv2.imread('Pirata.tif')
dim = 5
gaussian=cv2.GaussianBlur (img, (dim,dim), 0)
laplacian = cv2.Laplacian(img,cv2.CV_8U)
laplacianGaus = cv2.Laplacian(gaussian,cv2.CV_8U)

sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplaciano'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(laplacianGaus,cmap = 'gray')
plt.title('Laplaciano del gaussiano'), plt.xticks([]), plt.yticks([])


plt.show()