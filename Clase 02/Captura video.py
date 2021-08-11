# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 23:28:45 2017

@author: Gio
"""
import numpy as np
import cv2

#Se crea un objeto tipo captura y se especifica el dispositivo
captura = cv2.VideoCapture(0)
entrada = cv2.imread("Background.jpg") # Necesita medir lo mismo que la captura de la cámara
# Por defecto es 640x480

#Se crea un ciclo infinito
while(True):
    #Se captura el fotograma actual
    disponible, fotograma = captura.read()
    if (disponible == True):
        cv2.imshow('Captura',fotograma)
        
        salida = cv2.addWeighted(entrada,0.65,fotograma,0.35,0)
        cv2.imshow('Resultado',salida)

    else:
        print("Cámara no disponible")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando finaliza libera la cámara y destruye las ventanas
captura.release()
cv2.destroyAllWindows()
