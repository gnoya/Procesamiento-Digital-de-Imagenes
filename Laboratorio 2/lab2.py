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
    
def hist(image):
    return (cv2.calcHist([image], [0], None, [256], [0, 256]), 
        cv2.calcHist([image], [1], None, [256], [0, 256]), cv2.calcHist([image], [2], None, [256], [0, 256]))

# def plotHistogram(b, g, r, text):
#     plt.figure()
#     plt.xlim([0, 256])
#     plt.plot(b, 'b')
#     plt.plot(g, 'g')
#     plt.plot(r, 'r')
#     plt.title(text)

def plotHistogram(hist, color, text, subplot):
    
    plt.xlim([0, 256])
    plt.plot(hist, color)
    plt.title(text)

def plotBGRImage(image, text, subplot):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.subplot(subplot)
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

b = cv2.equalizeHist(image[:,:,0])
g = cv2.equalizeHist(image[:,:,1])
r = cv2.equalizeHist(image[:,:,2])

eqImage = cv2.merge((b,g,r))

stBlueHistogram, stGreenHistogram, stRedHistogram = hist(stretchImage)
eqBlueHistogram, eqGreenHistogram, eqRedHistogram = hist(eqImage)

plt.figure()

plotHistogram(blueHistogram, 'b', 'Histograma azul original', 331)
plotHistogram(greenHistogram, 'g', 'Histograma verde original', 332)
plotHistogram(redHistogram, 'r', 'Histograma rojo original', 333)

plotHistogram(stBlueHistogram, 'b', 'Histograma azul estirado', 334)
plotHistogram(stGreenHistogram, 'g', 'Histograma verde estirado', 335)
plotHistogram(stRedHistogram, 'r', 'Histograma rojo estirado', 336)

plotHistogram(eqBlueHistogram, 'b', 'Histograma azul equalizado', 337)
plotHistogram(eqGreenHistogram, 'g', 'Histograma verde equalizado', 338)
plotHistogram(eqRedHistogram, 'r', 'Histograma rojo equalizado', 339)

# plotHistogram(blueHistogram, greenHistogram, redHistogram, 'Histograma original')
# plotHistogram(stBlueHistogram, stGreenHistogram, stRedHistogram, 'Histograma estirado')
# plotHistogram(eqBlueHistogram, eqGreenHistogram, eqRedHistogram, 'Histograma equalizado')

plt.figure()

plotBGRImage(image, 'Imagen original', 221)
plotBGRImage(stretchImage, 'Imagen estirada', 222)
plotBGRImage(eqImage, 'Imagen equalizada', 223)

plt.show()
