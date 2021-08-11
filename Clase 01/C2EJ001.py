# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:23:29 2017

@author: Gio
"""

# Mejora el contraste y el brillo en imagen en escala de grises
import numpy as np
import cv2

entrada = cv2.imread("LCCity.jpg",0)
alto, ancho = entrada.shape
salida = np.zeros((alto,ancho), np.uint8)

while(True):   
    
    minimo = 300
    maximo = 0
    for i in range(0, alto):
        for j in range(0, ancho):
            
            f = entrada.item(i,j)
            if( f< minimo):
                minimo = f
            if(f > maximo):
                maximo = f
    
    print(maximo)
    print(minimo)
    
    for i in range(0, alto):
        for j in range(0, ancho):
            
            f = entrada.item(i,j)
            g = int((f-minimo)*(255.0/(maximo-minimo)))
            salida.itemset((i,j),g)
    
    cv2.imshow("Original",entrada)        
    cv2.imshow("Resultado",salida)  
    
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        
        cv2.imwrite("Clase2Desafio1.jpg",salida)
        break
    
cv2.destroyAllWindows()