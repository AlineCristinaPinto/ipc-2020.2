# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:01:46 2021

@author: aline
"""

def n_termo_fibonacci(n_termo):
    termo = 1
    antecessor = 1    
    antecessor_antecessor = 1
    
    if n_termo == 1 or n_termo == 2:
        return termo
    
    for i in range(2, n_termo):
        termo = antecessor + antecessor_antecessor
        antecessor_antecessor = antecessor
        antecessor = termo
        
    return termo
        

n_termo = int(input('Digite um inteiro n:'))
print(n_termo_fibonacci(n_termo))