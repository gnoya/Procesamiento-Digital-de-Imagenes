import cv2
import numpy as np 
from matplotlib import pyplot as plt

x=False
if x:
    import pytesseract #https://github.com/nikhilkumarsingh/tesseract-python
    from PIL import Image 
else:
    print("noya pato")

img=cv2.imread('test4.tif')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

#Creacion imagen binaria
img= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,31,2)

print(pytesseract.image_to_string(img))


