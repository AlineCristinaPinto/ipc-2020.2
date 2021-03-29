# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:51:52 2021

@author: aline
"""

def numeroPrimo(numero):    
    if numero < 2:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
    return True

numero = int(input('Digite um inteiro n:'))

if(numeroPrimo(numero)):
    print('É primo')
else:
    print('Não é primo')

