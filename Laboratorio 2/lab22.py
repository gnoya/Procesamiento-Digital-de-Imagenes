import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('tornado.jpg')

b = cv2.equalizeHist(image[:,:,0])
g = cv2.equalizeHist(image[:,:,1])
r = cv2.equalizeHist(image[:,:,2])

img = cv2.merge((b,g,r))

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure()
plt.title('Imagen Original')
plt.imshow(image)
plt.figure()
plt.title('Imagen con stretch')
plt.imshow(img)

plt.show()