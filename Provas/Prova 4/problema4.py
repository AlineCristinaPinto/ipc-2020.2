# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:34:07 2021

@author: aline
"""

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

for numero in range(x, y+1):
    if numero**(1/2) % 1 == 0:
        print(numero)