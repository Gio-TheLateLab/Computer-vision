# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:19:52 2017

@author: Gio
"""

# Convierte una imagen a color en una imagen en escala de grises
import numpy as np
import cv2

entrada = cv2.imread("Lena.png")

alto, ancho, canales = entrada.shape

salida = np.zeros((alto,ancho), np.uint8)

while(True):   
    for i in range(0, alto):
        for j in range(0, ancho):
            
            b0 = entrada.item(i,j,0)
            g0 = entrada.item(i,j,1)
            r0 = entrada.item(i,j,2)
            
            promedio = (b0+g0+r0)/3
            salida.itemset((i,j),promedio)
    
    cv2.imshow("Original",entrada)        
    cv2.imshow("Resultado",salida)  
    
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        
        cv2.imwrite("Resultado.jpg",salida)
        break
    
cv2.destroyAllWindows()