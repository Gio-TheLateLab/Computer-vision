# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:21:05 2017

@author: Gio
"""

import numpy as np
import cv2

entrada0 = cv2.imread("Background.jpg")
entrada1 = cv2.imread("Background2.jpg")

alto, ancho, canales = entrada0.shape
salida = np.zeros((alto,ancho,3), np.uint8)

while(True):   
    for i in range(0, alto):
        for j in range(0, ancho): 
            
            b0 = entrada0.item(i,j,0)
            g0 = entrada0.item(i,j,1)
            r0 = entrada0.item(i,j,2)
            
            b1 = entrada1.item(i,j,0)
            g1 = entrada1.item(i,j,1)
            r1 = entrada1.item(i,j,2)
           
            salida.itemset((i,j,0),0.5*b0+0.5*b1)
            salida.itemset((i,j,1),0.5*g0+0.5*g1)
            salida.itemset((i,j,2),0.5*r0+0.5*r1)   
  
    cv2.imshow("Background",entrada0) 
    cv2.imshow("Background2",entrada1) 
    cv2.imshow("Resultado",salida)  
    
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        
        cv2.imwrite("Resultado.jpg",salida)
        break

cv2.destroyAllWindows()