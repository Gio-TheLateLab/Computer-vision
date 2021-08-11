# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 00:21:39 2017

@author: Gio
"""

import cv2

entrada0 = cv2.imread("Background.jpg")
entrada1 = cv2.imread("Background2.jpg")

while(True):   

    salida = cv2.addWeighted(entrada0,0.5,entrada1,0.5,0)    
    cv2.imshow("Resultado",salida)  
    
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        
        cv2.imwrite("Resultado.jpg",salida)
        break

cv2.destroyAllWindows()