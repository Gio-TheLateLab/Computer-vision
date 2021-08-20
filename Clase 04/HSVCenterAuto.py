# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:09:47 2017
Test it on: https://poki.com/en/g/subway-surfers#
@author: Gio
"""


import numpy as np
import cv2

import keyboard

def nothing(x):
    pass


# Create a black image, a window
cv2.namedWindow('Sliders')

img = np.zeros((100,500), np.uint8)
# create trackbars for color change
cv2.createTrackbar('Vmin','Sliders',140,255,nothing)
cv2.createTrackbar('Smin','Sliders',180,255,nothing)
cv2.createTrackbar('Hmin','Sliders',105,255,nothing)

cv2.createTrackbar('Vmax','Sliders',170,255,nothing)
cv2.createTrackbar('Smax','Sliders',255,255,nothing)
cv2.createTrackbar('Hmax','Sliders',115,255,nothing)


#Se crea un objeto tipo captura y se especifica el dispositivo
captura = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

leftAvailable = True
rightAvailable = True

#Se crea un ciclo infinito
while(True):
    #Se captura el fotograma actual
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
        
        salida = cv2.inRange(hsv,(hMin,sMin,vMin),(hMax,sMax,vMax))
        salida = cv2.morphologyEx(salida, cv2.MORPH_OPEN, kernel) # Eliminación de ruido
        M = cv2.moments(salida)
        
        if(M['m00'] > 100):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            fotograma = cv2.circle(fotograma,(cx,cy),3,(0,255,0))
            #print(cx,cy)
            
            
            if(0 < cx < 200 and leftAvailable):
                #print("Left")
                keyboard.press_and_release("left")
                leftAvailable = False
                
            elif(440 < cx < 640 and rightAvailable):
                #print("Right")
                keyboard.press_and_release("right")
                rightAvailable = False
            elif(200 <= cx <= 440):
                leftAvailable = True
                rightAvailable = True
                
        
        cv2.imshow('Captura',fotograma)
        cv2.imshow('Resultado',salida)
        cv2.imshow('Sliders',img)

    else:
        print("Cámara no disponible")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando finaliza libera la cámara y destruye las ventanas
captura.release()
cv2.destroyAllWindows()