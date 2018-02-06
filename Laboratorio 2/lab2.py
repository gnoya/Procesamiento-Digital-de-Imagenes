import cv2
import numpy as np
from matplotlib import pyplot as plt

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

image = cv2.imread('tornado.jpg')
totalPixels = image.size / 3

## Histogramas RGB (BGR)

blueHistogram = cv2.calcHist([image], [0], None, [256], [0, 256])
greenHistogram = cv2.calcHist([image], [1], None, [256], [0, 256])
redHistogram = cv2.calcHist([image], [2], None, [256], [0, 256])


## BLUE
minValue, maxValue = maxMin(blueHistogram, totalPixels)

b = np.array(image[:,:,0], int)
b = (int)(255 / (maxValue - minValue)) * (b - minValue)
b[b < 0] = 0
b = np.array(b, np.uint8)

## GREEN 
minValue, maxValue = maxMin(greenHistogram, totalPixels)

g = np.array(image[:,:,1], int)
g = (int)(255 / (maxValue - minValue)) * (g - minValue)
g[g < 0] = 0
g = np.array(g, np.uint8)

## RED
minValue, maxValue = maxMin(redHistogram, totalPixels)

r = np.array(image[:,:,2], int)
r =  (int)(255 / (maxValue - minValue)) * (r - minValue)
r[r < 0] = 0
r = np.array(r, np.uint8)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img = cv2.merge((b,g,r))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.title('Imagen Original')
plt.imshow(image)
plt.figure()
plt.title('Imagen con stretch')
plt.imshow(img)

plt.figure()
plt.xlim([0, 256])
plt.title('Histograma Original')
plt.plot(blueHistogram, 'b')
plt.plot(greenHistogram, 'g')
plt.plot(redHistogram, 'r')


blueHistogram = cv2.calcHist([img], [0], None, [256], [0, 256])
greenHistogram = cv2.calcHist([img], [1], None, [256], [0, 256])
redHistogram = cv2.calcHist([img], [2], None, [256], [0, 256])

plt.figure()
plt.xlim([0, 256])
plt.title('Histograma con stretch')
plt.plot(blueHistogram, 'b')
plt.plot(greenHistogram, 'g')
plt.plot(redHistogram, 'r')

plt.show()

