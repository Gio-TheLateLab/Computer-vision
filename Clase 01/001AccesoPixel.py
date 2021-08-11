import numpy as np
import cv2

# Lectura de imagen. El parámetro 0 indica que es en escala de grises
entrada = cv2.imread("Lena.png",0)
# De la imagen leida se extrae el alto y el ancho
alto, ancho = entrada.shape
# Se crea una imagen vacia para almacenar el resultado
salida = np.zeros((alto,ancho), np.uint8)
# Permite crear un ciclo infinito. Similar a LOOP de Arduino
while(True):   
    
    for i in range(0, alto): #Se recorre la imagen de 0 al alto
        for j in range(0, ancho): #Se recorre la imagen de 0 al ancho
            #Se lee la información del píxel en la posición i,j
            f = entrada.item(i,j)    
            # Se resta 30 al valor original
            g = (f-30)
            #Se asigna el valor calculado, g, a la imagen nueva
            salida.itemset((i,j),g)
    
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