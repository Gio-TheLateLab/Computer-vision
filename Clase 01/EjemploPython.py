# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:16:48 2021

@author: Usuario
"""

if(5 > 2):
    print('Cumple')
    
x = ["Nicolas", "Sebastian", "Jacobo", "Juan", "Felipe", "Daniel", "Luisa"]


x.append("Daniel")
x.append("Luis")


for i,nombre in enumerate(x):
    print('El nombre en la pos ' , i, ' es ' , nombre)

for i in range(0,len(x)):
    print(x[i])
 

for i in x:
    print(i)