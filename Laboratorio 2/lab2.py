import cv2
import numpy as np
from matplotlib import pyplot as plt

fileName = 'NoyaCabrera.jpg'

def maxMin(hist, totalPixels):
    pxHist = 0
    i = 0
    mina = 0
    maxa = 0
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

def plotHistogram(hist, color, text, subplot):
    plt.subplot(subplot)
    plt.xlim([0, 256])
    plt.plot(hist, color)
    plt.title(text)

def plotBGRImage(image, text, subplot):
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.subplot(subplot)
    plt.title(text)
    plt.imshow(image, cmap = 'gray')

image = cv2.imread(fileName, 0)
totalPixels = image.size / 3

histogram = cv2.calcHist([image], [0], None, [256], [0,256])

# Stretch
minValue, maxValue = maxMin(histogram, totalPixels)
stretchImage = stretchFormula(image, minValue, maxValue)

# Equalization
eqImage = cv2.equalizeHist(image)

# New histograms
stretchHistogram = cv2.calcHist([stretchImage], [0], None, [256], [0,256])
equalizedHistogram = cv2.calcHist([eqImage], [0], None, [256], [0,256])

# Histogram plotting
plt.figure()
plotHistogram(histogram, 'b', 'Histograma original', 131)
plotHistogram(stretchHistogram, 'b', 'Histograma estirado', 132)
plotHistogram(equalizedHistogram, 'b', 'Histograma equalizado', 133)

# Image plotting
plt.figure()
plotBGRImage(image, 'Imagen original', 131)
plotBGRImage(stretchImage, 'Imagen estirada', 132)
plotBGRImage(eqImage, 'Imagen equalizada', 133)

plt.show()
