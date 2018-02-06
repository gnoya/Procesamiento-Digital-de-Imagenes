import cv2
import numpy as np
from matplotlib import pyplot as plt

fileName = 'tornado.jpg'

def maxMin(hist, totalPixels):
    pxHist = 0
    i = 0
    pxMin = totalPixels * 0.05
    pxMax = totalPixels * 0.95
    while (pxHist < totalPixels):
        pxHist += hist[i]
        if (pxHist <= pxMin):
            mina = i
        elif (pxHist <= pxMax):
            maxa = i
        i += 1
    return (mina,maxa)

def stretchFormula(channel, minValue, maxValue):
    channel = np.array(channel, int)
    channel = (int)(255 / (maxValue - minValue)) * (channel - minValue)
    channel[channel < 0] = 0
    return np.array(channel, np.uint8)
    
def hist(image):
    return (cv2.calcHist([image], [0], None, [256], [0, 256]), 
        cv2.calcHist([image], [1], None, [256], [0, 256]), cv2.calcHist([image], [2], None, [256], [0, 256]))

def plotHistogram(b, g, r, text):
    plt.figure()
    plt.xlim([0, 256])
    plt.plot(b, 'b')
    plt.plot(g, 'g')
    plt.plot(r, 'r')
    plt.title(text)

def plotBGRImage(image, text):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure()
    plt.title(text)
    plt.imshow(image)
    

image = cv2.imread(fileName)
totalPixels = image.size / 3

blueHistogram, greenHistogram, redHistogram  = hist(image)

# Stretch del canal azul
minValue, maxValue = maxMin(blueHistogram, totalPixels)
b = stretchFormula(image[:,:,0], minValue, maxValue)

# Stretch del canal verde
minValue, maxValue = maxMin(greenHistogram, totalPixels)
g = stretchFormula(image[:,:,1], minValue, maxValue)

# Stretch del canal rojo
minValue, maxValue = maxMin(redHistogram, totalPixels)
r = stretchFormula(image[:,:,2], minValue, maxValue)

stretchImage = cv2.merge((b,g,r))

stBlueHistogram, stGreenHistogram, stRedHistogram = hist(stretchImage)

plotHistogram(blueHistogram, greenHistogram, redHistogram, 'Histograma original')
plotHistogram(stBlueHistogram, stGreenHistogram, stRedHistogram, 'Histograma equalizado')

plotBGRImage(image, 'Imagen original')
plotBGRImage(stretchImage, 'Imagen estirada')

plt.show()
