# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:27:31 2017

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
        H1 = cv2.add(H,255)
        S1 = cv2.add(S,255)
        V1 = cv2.add(V,255)
        
        H2 = cv2.add(H,-255)
        H2 = cv2.add(H2,150)
        S2 = cv2.add(S,-255)
        V2 = cv2.add(V,-255)
        
        
        S3 = cv2.multiply(S,2)
        V3 = cv2.multiply(V,2)
        
        triada = (180-H,S,V) #Tonalidad invertida
        triada = (H2,S,V) #Tonalidad en azul
#        
        triada = (H,S1,V1) # Misma tonalidad máximo saturación y brillo
        triada = (H,S,V1) # Misma tonalidad y saturaición, máximo brillo
        triada = (H,S1,V) # Misma tonalidad y brillo, máxima saturación
#        
        triada = (H,S2,V) # Misma tonalidad mínimo saturación
        triada = (H,S,V2) # Misma tonalidad y saturaición, mínimo brillo
        triada = (H,S2,V) # Misma tonalidad y brillo, mínimo saturación
#        
        triada = (H,S3,V3) # Misma tonalidad doble saturación y brillo
        triada = (H,S,V3) # Misma tonalidad y saturaición, doble brillo
        triada = (H,S3,V) # Misma tonalidad y brillo, doble saturación
        
        salida = cv2.cvtColor(cv2.merge(triada), cv2.COLOR_HSV2BGR)

        cv2.imshow('Salida',salida)
        


    else:
        captura = cv2.VideoCapture("Sofa - 11294.mp4")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando finaliza libera la cámara y destruye las ventanas
captura.release()
cv2.destroyAllWindows()