# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:07:13 2021

@author: aline
"""

def potencia(k, n):
    if n > 1:
        return k * potencia(k, n-1)
    
    return k

k = int(input('Digite k: '))
n = int(input('Digite n: '))

print(potencia(k, n))