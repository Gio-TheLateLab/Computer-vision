# -*- coding: utf-8 -*-
"""
@author: Gio
"""

import cv2
import numpy as np

entrada = cv2.imread("Background.jpg")

alto, ancho, canales = entrada.shape
zeros = np.zeros((alto,ancho), np.uint8)

while(True):   

    b,g,r = cv2.split(entrada)
    cv2.imshow("entrada",entrada)  
    
    b0 = cv2.merge((b,zeros,zeros))
    g0 = cv2.merge((zeros,g,zeros))
    r0 = cv2.merge((zeros,zeros,r))
    
    #g = cv2.subtract(g,10)
    #g = cv2.multiply(g,1.25)
    
    cv2.imshow("b",b0)  
    cv2.imshow("g",g0)  
    cv2.imshow("r",r0)  
    
    salida = cv2.merge((255-b,g,r))
    cv2.imshow("salida",salida)  
    
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        
        
        break

cv2.destroyAllWindows()