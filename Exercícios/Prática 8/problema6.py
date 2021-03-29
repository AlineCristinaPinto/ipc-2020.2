# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:37:13 2021

@author: aline
"""

def imprime_naturais_pares(n):
    if n < 0:
        return 0
    
    imprime_naturais_pares(n - 1)
    
    if n % 2 == 0:
        print(n)

n = int(input('Digite N: '))

imprime_naturais_pares(n)