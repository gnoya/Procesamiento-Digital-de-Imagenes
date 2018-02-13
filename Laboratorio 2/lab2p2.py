import cv2
import numpy as np
from scipy import ndimage 
from matplotlib import pyplot as plt

fileName = 'NoyaCabrera.jpg'

#suavizado a y b

image = cv2.imread(fileName)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
dimension = 5

kernel = np.ones((dimension, dimension), np.float32) / (dimension * dimension)
dst = cv2.filter2D(image, -1, kernel)
plt.figure()
plt.imshow(image), plt.title('Original')
plt.figure()
plt.imshow(dst), plt.title('Promedio')

# Perfilado c
#imagen=cv2.imread('Pirata.tif')

kernelp = np.ones((3, 3), np.float32) * (-1)
kernelp[1,1] = 8
imagenp = cv2.filter2D(image, -1, kernelp)
plt.figure()
plt.imshow(image), plt.title('Original')
plt.figure()
plt.imshow(imagenp), plt.title('Perfilado')
plt.figure()
plt.imshow(imagenp + image), plt.title('Imagen + perfilado')


#Filtro gaussiano d

gaussian = cv2.GaussianBlur(image, (dimension, dimension), 0)
plt.figure()
plt.imshow(image), plt.title('Original')
plt.figure()
plt.imshow(gaussian), plt.title('Filtro gaussiano')

#Parte e

gaussian = cv2.GaussianBlur(image, (dimension, dimension), 0)
laplacian = cv2.Laplacian(image, cv2.CV_8U)
laplacianGaussian = cv2.Laplacian(gaussian, cv2.CV_8U)

sobelx = cv2.Sobel(image,cv2.CV_8U, 1, 0, ksize = 3)
sobely = cv2.Sobel(image,cv2.CV_8U, 0, 1, ksize = 3)
plt.figure()
plt.imshow(image, cmap = 'gray'), plt.title('Original')
plt.figure()
plt.imshow(laplacian, cmap = 'gray'), plt.title('Laplaciano')
plt.figure()
plt.imshow(sobelx, cmap = 'gray'), plt.title('Sobel X')
plt.figure()
plt.imshow(sobely, cmap = 'gray'), plt.title('Sobel Y')
plt.figure()
plt.imshow(laplacianGaussian, cmap = 'gray'), plt.title('Laplaciano del gaussiano')

plt.show()