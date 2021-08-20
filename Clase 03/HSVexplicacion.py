# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:24:31 2017

@author: Gio
"""
import numpy as np
import cv2

#Se crea un objeto tipo captura y se especifica el dispositivo
captura = cv2.VideoCapture("Sofa - 11294.mp4")



#Se crea un ciclo infinito
while(True):
    #Se captura el fotograma actual
    disponible, fotograma = captura.read()
    if (disponible == True):
        cv2.imshow('Captura',fotograma)
        
        hsv = cv2.cvtColor(fotograma, cv2.COLOR_BGR2HSV)
        H,S,V = cv2.split(hsv)

        cv2.imshow('H',H)
        cv2.imshow('S',S)
        cv2.imshow('V',V)
        cv2.imshow('HSV',hsv)
        
        B,G,R = cv2.split(fotograma)

        cv2.imshow('B',B)
        cv2.imshow('G',G)
        cv2.imshow('R',R)
        


    else:
        captura = cv2.VideoCapture("Sofa - 11294.mp4")

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# Cuando finaliza libera la cámara y destruye las ventanas
captura.release()
cv2.destroyAllWindows()