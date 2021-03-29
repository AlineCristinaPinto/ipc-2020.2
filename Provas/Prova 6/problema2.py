# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:42:25 2021

@author: aline
"""

def desvio_padrao(v):
    m = sum(v) / len(v)
    return (1 / (len(v) - 1) * sum((numero - m)**2 for numero in v))**0.5

numeros = []

for i in range(10):
    numeros.append(int(input()))
    
v = numeros
print('Desvio Padrão:  %.2f' % desvio_padrao(v))