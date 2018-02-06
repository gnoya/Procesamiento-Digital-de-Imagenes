import cv2
from matplotlib import pyplot as plt

image = cv2.imread('./NoyaCabrera.png')

## Histogramas RGB (BGR)

plt.xlim([0, 256])

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.title('Blue histogram')
plt.plot(histogram, 'b')

plt.figure()
histogram = cv2.calcHist([image], [1], None, [256], [0, 256])
plt.title('Green histogram')
plt.plot(histogram, 'g')

plt.figure()
histogram = cv2.calcHist([image], [2], None, [256], [0, 256])
plt.title('Red histogram')
plt.plot(histogram, 'r')

## HSV

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

plt.figure()
plt.imshow(hsv)

## Histograma HSV

plt.figure()
histogram = cv2.calcHist([hsv], [0], None, [256], [0, 256])
plt.title('Hue histogram')
plt.plot(histogram, 'c')

plt.figure()
histogram = cv2.calcHist([hsv], [1], None, [256], [0, 256])
plt.title('Saturation histogram')
plt.plot(histogram, 'm')

plt.figure()
histogram = cv2.calcHist([hsv], [2], None, [256], [0, 256])
plt.title('Value histogram')
plt.plot(histogram, 'y')

plt.show()