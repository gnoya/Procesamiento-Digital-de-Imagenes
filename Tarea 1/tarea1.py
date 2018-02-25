import cv2
import numpy as np 
import sys
from matplotlib import pyplot as plt

showImage = True
fileName = 'test1.png'
kernelRows = 5
mode=False
#Chequeo de los argumentos de entrada
x=1
while(x<len(sys.argv)):
    if sys.argv[x]=="-k":
        x+=1
        kernelRows=int(sys.argv[x])

    if sys.argv[x]=="-n":
        x+=1
        fileName=sys.argv[x]
    
    if sys.argv[x]=="-ocr":
        x+=1
        mode=True
    x+=1

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

    kernel = createKernel(1, 1)
    image = noiseFilter(image, kernel)
    image = imageToBinary(image)

    kernel = createKernel(kernelRows, 1)
    image = applyStructuralElement(image, kernel)

    (_,contour,_) = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    charNumber = len(contour)
    print("Cantidad de caracteres:", charNumber)

    if showImage:
        markCharacters(origImage, contour)
        plt.imshow(origImage)
        plt.show()