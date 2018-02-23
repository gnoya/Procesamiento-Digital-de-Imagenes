import cv2
import numpy as np 
import sys
from matplotlib import pyplot as plt

# if __name__ == "__main__":
#     print("Cantidad de caracteres:", len(cv2.findContours(cv2.erode(cv2.dilate(cv2.adaptiveThreshold(cv2.erode(cv2.dilate(cv2.cvtColor(cv2.imread("test1.png"), cv2.COLOR_BGR2GRAY), np.ones((1, 1), np.uint8), iterations=1), np.ones((1, 1), np.uint8), iterations=1), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 2), np.ones((5, 1), np.uint8), iterations=1), np.ones((5, 1), np.uint8), iterations=1), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]))
    

fileName = 'test1.png'
kernelRows = 5

def noiseFilter(image, kernel):
    # Eliminar ruido
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    return image

def imageToBinary(image):
    # Creacion imagen binaria
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 2)

def createKernel(rows, columns):
    # Creacion del kernel
    return np.ones((rows, columns), np.uint8)

def applyStructuralElement(image, kernel):
    # Barrido con elemento estructural
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    return image
    
def markCharacters(image, contour):
    # Buscar contornos
    for c in contour:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)

if __name__ == "__main__":
    origImage = cv2.imread(fileName)
    image = cv2.cvtColor(origImage, cv2.COLOR_BGR2GRAY)
    figure(1)
    plt.title('Imagen original en blanco y negro')
    plt.imshow(image)

    kernel = createKernel(1, 1)
    image = noiseFilter(image, kernel)
    figure(2)
    plt.title('Imagen luego del filtro de ruido')
    plt.imshow(image)

    image = imageToBinary(image)
    figure(3)
    plt.title('Imagen binaria')
    plt.imshow(image)
    

    kernel = createKernel(kernelRows, 1)
    image = applyStructuralElement(image, kernel)

    figure(4)
    plt.title('Imagen luego de aplicar elemento estructural')
    plt.imshow(image)

    (_,contour,_) = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    charNumber = len(contour)
    print("Cantidad de caracteres:", charNumber)

    if showImage:
        markCharacters(origImage, contour)
        plt.title('Imagen con contornos remarcados')
        plt.imshow(origImage)
        plt.show()