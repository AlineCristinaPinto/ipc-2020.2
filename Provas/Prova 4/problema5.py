# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:48:56 2021

@author: aline
"""

n = int(input('Digite um número: '))
maior = n
menor = n

while True:    
    if n < 0:
        break
    
    if n > maior:
        maior = n
    
    if n < menor:
        menor = n
        
    n = int(input('Digite um número: '))

print('Maior: ', maior)
print('Menor: ', menor )
    
    