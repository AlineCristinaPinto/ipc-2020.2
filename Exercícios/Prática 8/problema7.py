# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:41:55 2021

@author: aline
"""

def imprime_naturais_impares(n):
    if n < 1:
        return 1
    
    if n % 2 != 0:
        print(n)
        
    imprime_naturais_impares(n - 1)
    

n = int(input('Digite N: '))

imprime_naturais_impares(n)