# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:36:13 2017

@author: Gio
"""


# Mejora el contraste y el brillo en imagen a color

import numpy as np
import cv2

entrada = cv2.imread("LCCity.jpg")
alto, ancho, canales = entrada.shape
salida = np.zeros((alto,ancho,3), np.uint8)

while(True):   
    
    minimos = [300,300,300]
    maximos = [0,0,0]
    for i in range(0, alto):
        for j in range(0, ancho):
            for h in range(0, canales):
                pixel = entrada.item(i,j,h)
                if( pixel < minimos[h]):
                    minimos[h] = pixel
                if( pixel > maximos[h]):
                    maximos[h] = pixel
                    
    print(maximos)
    print(minimos)
    
    for i in range(0, alto):
        for j in range(0, ancho):
            for h in range(0, canales):
                pixel = entrada.item(i,j,h)
                g = int((pixel-minimos[h])*(255.0/(maximos[h]-minimos[h])))
                salida.itemset((i,j,h),g)
    
    cv2.imshow("Original",entrada)        
    cv2.imshow("Resultado",salida)  
    
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        
        cv2.imwrite("Clase2Desafio3.jpg",salida)
        break
    
cv2.destroyAllWindows()




