# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:14:44 2021

@author: aline
"""

def soma_divisores(numero):
    soma = 0
    
    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma += divisor
    
    return soma


def main():
    numero = int(input('Número: '))
    print(soma_divisores(numero))
    
main()