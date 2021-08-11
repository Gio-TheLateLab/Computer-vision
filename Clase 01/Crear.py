import numpy as np
import cv2

#Se definen propiedades basicas de la imagen
ancho = 150
alto = 300

#Se crea la imagen vacía
imagen = np.zeros( (alto,ancho), np.uint8)

#Se crea un ciclo infinito para que el programa no se cierre
while(True): # UPDATE - LOOP

    #Recorremos la imagen
    for i in range(0, alto): #i es analogo a Y
        for j in range(0, ancho): #j es analogo a X

            #Se pintan de blanco los pixeles entre (25,50) y (50,75)
            if (j>25 and i>50) and (j<50 and i<75): imagen.itemset( (i, j), 255 )
            
            #Se pintan de blanco los pixeles entre (100,50) y (125,75)
            if (j>100 and i>50) and (j<125 and i<75): imagen.itemset( (i, j), 255 )
            
            #Se pintan de blanco los pixeles entre (10,185) y (25,200)
            if (j>10 and i>185) and (j<25 and i<200): imagen.itemset( (i, j), 255 )

            #Se pintan de blanco los pixeles entre (125,185) y (140,200)
            if (j>125 and i>185) and (j<140 and i<200): imagen.itemset( (i, j), 255 )
                
            #Se pintan de blanco los pixeles entre (50,30) y (220,120)
            if (j>25 and i>200) and (j<125 and i<215): imagen.itemset( (i, j), 255 )
                

    #Al finalizar el proceso mostramos el resultado
    cv2.imshow("Nombre ventana",imagen)

    #Dejamos el programa esperando una entrada de teclado
    # 11111111 & 00001000 = 00001000
    ch = 0xFF & cv2.waitKey()

    #Se revisa si la persona presiona Q (Quit)
    if ch == ord('x'):

        #Almacenamos en disco la salida
        cv2.imwrite("Resultado.jpg",imagen)
        #salimos del ciclo while
        break

#Eliminamos las ventanas que creamos
cv2.destroyAllWindows()




