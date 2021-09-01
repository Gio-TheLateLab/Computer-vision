# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 03:12:21 2020

@author: Usuario
"""

import numpy as np
import cv2
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5065
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

state = 0
rect = ['0','0','0','0'] # Datos a enviar

while(True):
    
    available, frame = cap.read()   
    if(available and state == 0):
        state = 1  
    
    elif(state == 1): # Start - Setup
        print("Setup")
        
        h, w, c = frame.shape
        state = 2
        
    elif(state == 2): # Update

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if(len(faces) > 0):
            x0,y0,w0,h0 = faces[0] # Para el ejemplo se usará una sola cara
            frame = cv2.rectangle(gray,(x0,y0),(x0+w0,y0+h0),(255,0,0),2)
            
            x0 += w0/2
            y0 += h0/2
            
            rect[0] = str(  int((x0/w)*100) )
            rect[1] = str(  int((1-(y0/h))*100) )
            rect[2] = str(  int((w0/w)*100) )
            rect[3] = str(  int((h0/h)*100) )
            
            
            #mensaje = str(rect[0]) + "," + str(rect[1]) ...
            mensaje = ','.join(rect)
                
            print((mensaje).encode())
            sock.sendto( mensaje.encode(), (UDP_IP, UDP_PORT) )
        else:
            rect = ['-1','-1','-1','-1'] # Si no deecta un rostro
            mensaje = ','.join(rect)
            sock.sendto( mensaje.encode(), (UDP_IP, UDP_PORT) )
         
        gray = cv2.multiply(gray,0.25)
        cv2.imshow('gray',gray)
        

        
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
    
    else:
        print("Camera not available")
        cap = cv2.VideoCapture(2) 

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
