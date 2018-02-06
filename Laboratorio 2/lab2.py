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

b = image[:,:,0]
b =  (int)(255 / (maxValue - minValue)) * (b - minValue)

ret,thresh4 = cv2.threshold(b,maxValue,maxValue,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(b,minValue,minValue,cv2.THRESH_TOZERO_INV)


## GREEN 
minValue, maxValue = maxMin(greenHistogram, totalPixels)

g = image[:,:,1]
g =  (int)(255 / (maxValue - minValue)) * (g - minValue)

## RED
minValue, maxValue = maxMin(redHistogram, totalPixels)

r = image[:,:,2]
r =  (int)(255 / (maxValue - minValue)) * (r - minValue)


img = cv2.merge((b,g,r))


plt.figure()
plt.imshow(image)
plt.figure()
plt.imshow(img)

# plt.xlim([0, 256])
# plt.plot(blueHistogram, 'b')
# plt.plot(greenHistogram, 'g')
# plt.plot(redHistogram, 'r')

plt.show()

