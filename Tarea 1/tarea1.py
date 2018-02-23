import cv2
import numpy as np 
import sys
from matplotlib import pyplot as plt

#Variables
nombre="test1.png"
kAlto=5
nLetras=0

def eliminarRuido():
    #Eliminar ruido
    kernel=np.ones((1,1),np.uint8)
    img=cv2.dilate(img,kernel,iterations=1)
    img=cv2.erode(img,kernel,iterations=1)

def imagenBinaria():     
    #Creacion imagen binaria
    return cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,31,2)

def elementoEstrural():
    #Barrido con elemento estructurante
    kernel=np.ones((kAlto,1),np.uint8)
    img=cv2.dilate(img,kernel,iterations=1)
    img=cv2.erode(img,kernel,iterations=1)
    return img 
    
def buscarLetras():
    #Buscar contornos
    (_,contorno,_)=cv2.findContours(imgGray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contorno:
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(imgOriginal,(x,y),(x+w,y+h),(0,255,0),1,cv2.LINE_AA)
        nLetras+=1
    

if __name__ == "__main__":

    global imgOriginal=cv2.imread(nombre)
    global img=cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2GRAY)
    eliminarRuido()
    imagenBinaria()
    elementoEstrural()
    nLetras=buscarLetras()
    plt.imshow()
    plt.show()
    print(nLetras)
