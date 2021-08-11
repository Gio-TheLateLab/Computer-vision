# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:43:09 2017

@author: Gio
"""



# Mejora el contraste y el brillo en imagen a color
import numpy as np
import cv2

entrada = cv2.imread("LCCity.jpg")
grises = cv2.imread("LCCity.jpg",0)
alto, ancho, canales = entrada.shape
salida = np.zeros((alto,ancho,3), np.uint8)

while(True):   
    
    minimo = 300
    maximo = 0
    for i in range(0, alto):
        for j in range(0, ancho):
            
            f = grises.item(i,j)
            if( f< minimo):
                minimo = f
            if(f > maximo):
                maximo = f
                    
    print(maximo)
    print(minimo)
    
    for i in range(0, alto):
        for j in range(0, ancho):
            for h in range(0, canales):
                pixel = entrada.item(i,j,h)
                g = int((pixel-minimo)*(255.0/(maximo-minimo)))
                salida.itemset((i,j,h),g)
    
    cv2.imshow("Original",entrada)        
    cv2.imshow("Resultado",salida)  
    
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        
        cv2.imwrite("Clase2Desafio4.jpg",salida)
        break
    
cv2.destroyAllWindows()