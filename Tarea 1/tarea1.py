import cv2
import numpy as np 
import sys
from matplotlib import pyplot as plt

# Configuracion predeterminada
fileName = 'CabreraNoya.png'
kernelRows = 5
mode = True

# Chequeo de los argumentos de entrada
x = 1
while(x < len(sys.argv)):
    if sys.argv[x] == "-k":
        x += 1
        kernelRows = int(sys.argv[x])

    if sys.argv[x] == "-n":
        x += 1
        fileName = sys.argv[x]
    
    if sys.argv[x] == "-ocr":
        mode = False
    x += 1

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
    kernel = createKernel(2, 2)
    image = noiseFilter(image, kernel)
    image = imageToBinary(image)

    if mode:
        imageCanny = cv2.Canny(image, 100, 200)
        plt.figure(1)
        plt.title('Contornos extraidos con el filtro Canny')
        plt.imshow(imageCanny, cmap='gray')
        kernel = createKernel(kernelRows, 1)
        image = applyStructuralElement(image, kernel)
        (_,contour,_) = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        charNumber = len(contour)
        print("Cantidad de caracteres:", charNumber)

        markCharacters(origImage, contour)
        plt.figure(2)
        plt.title('Imagen con caracteres identificados')
        plt.imshow(origImage)
        plt.show()

    else:
        import pytesseract 
        chars = 0
        text = pytesseract.image_to_string(image)
        lineas = text.split('\n')
        for x in range (0, len(lineas)):
            words = lineas[x].split(' ')
            for i in range (0, len(words)):
                chars += len(words[i])
        print("El texto es el siguiente:")
        print(text + "\n")
        print("Cantidad de caracteres:")
        print(chars)