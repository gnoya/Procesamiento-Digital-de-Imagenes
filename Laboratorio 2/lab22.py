import cv2
import numpy as np
from matplotlib import pyplot as plt

fileName = 'tornado.jpg'

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

b = cv2.equalizeHist(image[:,:,0])
g = cv2.equalizeHist(image[:,:,1])
r = cv2.equalizeHist(image[:,:,2])

eqImage = cv2.merge((b,g,r))

blueHistogram, greenHistogram, redHistogram  = hist(image)
eqBlueHistogram, eqGreenHistogram, eqRedHistogram = hist(eqImage)

plotHistogram(blueHistogram, greenHistogram, redHistogram, 'Histograma original')
plotHistogram(eqBlueHistogram, eqGreenHistogram, eqRedHistogram, 'Histograma equalizado')

plotBGRImage(image, 'Imagen original')
plotBGRImage(eqImage, 'Imagen equalizada')

plt.show()