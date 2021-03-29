# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:02:11 2021

@author: aline
"""

numeros = []
numeros_pares = []
numeros_impares = []

for i in range(5):
    numeros.append(int(input()))
    
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(numeros)
print(numeros_pares)
print(numeros_impares)