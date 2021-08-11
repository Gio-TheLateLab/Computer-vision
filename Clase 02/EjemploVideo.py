

import numpy as np
import cv2

#Se crea un objeto tipo captura y se especifica el dispositivo
captura = cv2.VideoCapture(0)
entrada = cv2.imread("Background.jpg")

alto, ancho, canales = entrada.shape
zeros = np.zeros((alto,ancho), np.uint8)

#Se crea un ciclo infinito
while(True):
    #Se captura el fotograma actual
    disponible, fotograma = captura.read()
    if (disponible == True):
        cv2.imshow('Captura',fotograma)
        
        b,g,r = cv2.split(fotograma)
        #cv2.imshow("entrada",entrada)  
        
        b0 = cv2.merge((b,zeros,zeros))
        g0 = cv2.merge((zeros,g,zeros))
        r0 = cv2.merge((zeros,zeros,r))
        
        cv2.imshow("b",b0)  
        cv2.imshow("g",g0)  
        cv2.imshow("r",r0) 
        
        salida = cv2.addWeighted(entrada,0.65,fotograma,0.35,0)
        cv2.imshow('Resultado',salida)

    else:
        print("Cámara no disponible")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando finaliza libera la cámara y destruye las ventanas
captura.release()
cv2.destroyAllWindows()