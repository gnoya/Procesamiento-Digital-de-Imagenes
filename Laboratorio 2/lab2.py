import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('tornado.jpg')
totalPixels = image.size
lowPercentage = 0
highPercentage = 0


print(image)

## Histogramas RGB (BGR)

plt.xlim([0, 256])

blueHistogram = cv2.calcHist([image], [0], None, [256], [0, 256])
greenHistogram = cv2.calcHist([image], [1], None, [256], [0, 256])
redHistogram = cv2.calcHist([image], [2], None, [256], [0, 256])

while()

#plt.plot(blueHistogram, 'b')
# plt.plot(greenHistogram, 'g')
# plt.plot(redHistogram, 'r')

plt.show()