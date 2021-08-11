# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 23:58:02 2017

@author: Gio
"""
import numpy as np
import cv2

#Se crea un objeto tipo captura y se especifica el dispositivo
captura = cv2.VideoCapture(0)

#Se crea un ciclo infinito
while(True):
    #Se captura el fotograma actual
    disponible, fotograma = captura.read()
    if (disponible == True):
        cv2.imshow('Captura',fotograma)
        
        b,g,r = cv2.split(fotograma)
        
        bMin, bMax, ret, ret = cv2.minMaxLoc(b)
        gMin, gMax, ret, ret = cv2.minMaxLoc(g)
        rMin, rMax, ret, ret = cv2.minMaxLoc(r)

        deltaB = 255/(bMax-bMin)
        deltaG = 255/(gMax-gMin)
        deltaR = 255/(rMax-rMin)
        
        b = cv2.subtract(b,bMin)
        g = cv2.subtract(g,gMin)
        r = cv2.subtract(r,rMin)
        
        b = cv2.multiply(b,deltaB)
        g = cv2.multiply(g,deltaG)
        r = cv2.multiply(r,deltaR)

        salida = cv2.merge( (b,g,r) )
        cv2.imshow("Salida",salida)

    else:
        print("Cámara no disponible")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando finaliza libera la cámara y destruye las ventanas
captura.release()
cv2.destroyAllWindows()

