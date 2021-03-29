# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:25:25 2021

@author: aline
"""

def intersecao(lista_1, lista_2):
    return [item_lista_1 for item_lista_1 in lista_1 if item_lista_1 in lista_2] 


numeros = []

for i in range(10):
    numeros.append(int(input()))
    
lista_1 = numeros[:5]
lista_2 = numeros[5:10]

print('Interseção:', intersecao(lista_1, lista_2))
