# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 08:11:37 2021

@author: Usuario
"""

import cv2
import numpy as np
import keyboard


def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('Sliders')

img = np.zeros((100,500), np.uint8)
# create trackbars for color change
cv2.createTrackbar('Vmin','Sliders',90,255,nothing)
cv2.createTrackbar('Smin','Sliders',85,255,nothing)
cv2.createTrackbar('Hmin','Sliders',100,255,nothing)

cv2.createTrackbar('Vmax','Sliders',165,255,nothing)
cv2.createTrackbar('Smax','Sliders',255,255,nothing)
cv2.createTrackbar('Hmax','Sliders',120,255,nothing)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

izqDisponible = True
derDisponible = True

captura = cv2.VideoCapture(0)
while(True):
    disponible, fotograma = captura.read()
    if (disponible == True):
        fotograma = cv2.flip(fotograma, 1)
        fotograma = cv2.blur(fotograma,(5,5))
        
        hsv = cv2.cvtColor(fotograma, cv2.COLOR_BGR2HSV)
        hMin = cv2.getTrackbarPos('Hmin','Sliders')
        sMin = cv2.getTrackbarPos('Smin','Sliders')
        vMin = cv2.getTrackbarPos('Vmin','Sliders')
        
        hMax = cv2.getTrackbarPos('Hmax','Sliders')
        sMax = cv2.getTrackbarPos('Smax','Sliders')
        vMax = cv2.getTrackbarPos('Vmax','Sliders')
        
        imgSegmentada = cv2.inRange(hsv,(hMin,sMin,vMin),(hMax,sMax,vMax))
        imgSegmentada = cv2.morphologyEx(imgSegmentada, cv2.MORPH_OPEN, kernel)
        
        
        gray = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)
        gray = cv2.multiply(gray,0.5)
        grayRGB = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        
        
        fondo = cv2.bitwise_and(grayRGB,grayRGB, mask = 255-imgSegmentada)
        frente = cv2.bitwise_and(fotograma,fotograma, mask = imgSegmentada)
        salida = cv2.add(fondo,frente)
        
        M = cv2.moments(imgSegmentada)
        if(M['m00'] > 1000):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            salida = cv2.circle(salida,(cx,cy),5,(0,255,0))
            
            if( (0 < cx < 200) and izqDisponible):
                keyboard.press_and_release("left")
                izqDisponible = False
            elif( (440 < cx < 640) and derDisponible):
                keyboard.press_and_release("right")
                derDisponible = False
            elif(200 <= cx <= 440):
                izqDisponible = True
                derDisponible = True
                
        
        cv2.imshow('Captura',fotograma)
        cv2.imshow('salida',salida)
        
    
    else:
        print("Cámara no disponible")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
captura.release()
cv2.destroyAllWindows()