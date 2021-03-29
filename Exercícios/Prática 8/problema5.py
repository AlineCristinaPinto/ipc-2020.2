# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:26:38 2021

@author: aline
"""

def imprime_naturais(n):
    if n < 0:
        return 0
    
    imprime_naturais(n-1) 
    print(n)

n = int(input('Digite N: '))

imprime_naturais(n)