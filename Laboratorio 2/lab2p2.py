import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('Test3.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

dimension=5
kernel = np.ones((dimension,dimension),np.float32)/(dimension*dimension)
dst = cv2.filter2D(image,-1,kernel)
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Promedio')
plt.xticks([]), plt.yticks([])
plt.show()