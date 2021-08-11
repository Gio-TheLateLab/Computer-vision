# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:40:08 2017

@author: Gio
"""


import cv2


def nothing(x):
    pass


cv2.namedWindow('slider')
entrada = cv2.imread("Tennis.jpg")
cv2.createTrackbar('RMax','slider',0,255,nothing)
cv2.createTrackbar('RMin','slider',0,255,nothing)

scale_percent = 100
width = int(entrada.shape[1] * scale_percent / 100)
height = int(entrada.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(entrada, dim, interpolation = cv2.INTER_AREA)


while(True):   

    
    
    rMax = cv2.getTrackbarPos('RMax','slider')
    rMin = cv2.getTrackbarPos('RMin','slider')
    print(r)
    rngMin = (50,200,rMin)
    rngMax = (100,255,rMax)
    
    salida = cv2.inRange(resized,rngMin,rngMax)
    cv2.imshow("Entrada",resized) 
    cv2.imshow("image",salida)  
    
    ch = 0xFF & cv2.waitKey(33)
    if ch == ord('q'):
        
        cv2.imwrite("Resultado.jpg",resized)
        break

cv2.destroyAllWindows()