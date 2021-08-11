# -*- coding: utf-8 -*-
import numpy as np
import cv2
# Lectura de imagen.
entrada = cv2.imread("Lena.png")
# De la imagen leida se extrae el alto, el ancho y los canales
alto, ancho, canales = entrada.shape
# Se crea una imagen vacia para almacenar el resultado
salida = np.zeros((alto,ancho,canales), np.uint8)
# Permite crear un ciclo infinito. Similar a LOOP de Arduino
while(True):   
    for i in range(0, alto): #Se recorre la imagen de 0 al alto
        for j in range(0, ancho): #Se recorre la imagen de 0 al ancho
            #Se lee la información del píxel en la posición i,j de cada canal
            b0 = entrada.item(i,j,0)
            g0 = entrada.item(i,j,1)
            r0 = entrada.item(i,j,2)
            
            if(b0 >= 100 and g0 <= 150 and r0 <= 150):
                b1 = 255
                g1 = 0
                r1 = 0
            else:
                b1 = b0
                g1 = g0
                r1 = r0
            #Se asigna cada valor calculado a la imagen nueva
            salida.itemset((i,j,0),b1)
            salida.itemset((i,j,1),g1)
            salida.itemset((i,j,2),r1)   
    #Se muestra la imagen de entrada en una ventana llamada original
    cv2.imshow("Original",entrada)        
    cv2.imshow("Resultado",salida)  
    #Se espera a que se presione la tecla Q para finalizar
    ch = 0xFF & cv2.waitKey()
    if ch == ord('q'):
        #Se almacena la imagen y se rompe el ciclo
        cv2.imwrite("Resultado.jpg",salida)
        break
#Se destruyden las ventanas creadas
cv2.destroyAllWindows()