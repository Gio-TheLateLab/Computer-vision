# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 23:58:02 2017

@author: Gio
"""
import numpy as np
import cv2

#Se crea un objeto tipo captura y se especifica el dispositivo (o nombre del archivo)
captura = cv2.VideoCapture("Sofa - 11294.mp4")
estado = 0
frames = 0

#Se crea un ciclo infinito
while(True):
    #Se captura el fotograma actual
    disponible, fotograma = captura.read()
    if (disponible == True):
        cv2.imshow('Captura',fotograma)
        b,g,r = cv2.split(fotograma)
        
        if(estado == 0):
            
            bMin, bMax, ret, ret = cv2.minMaxLoc(b)
            gMin, gMax, ret, ret = cv2.minMaxLoc(g)
            rMin, rMax, ret, ret = cv2.minMaxLoc(r)
    
            bMin -= 15
            gMin -= 15
            rMin -= 15
    
            deltaB = 270/(bMax-bMin)
            deltaG = 270/(gMax-gMin)
            deltaR = 270/(rMax-rMin)
            estado = 1
            
        elif(estado == 1):
            b = cv2.subtract(b,bMin)
            g = cv2.subtract(g,gMin)
            r = cv2.subtract(r,rMin)
            
            b = cv2.multiply(b,deltaB)
            g = cv2.multiply(g,deltaG)
            r = cv2.multiply(r,deltaR)

            salida = cv2.merge( (b,g,r) )
            cv2.imshow("Salida",salida)

    else:
        captura = cv2.VideoCapture("Sofa - 11294.mp4")

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# Cuando finaliza libera la cámara y destruye las ventanas
captura.release()
cv2.destroyAllWindows()

