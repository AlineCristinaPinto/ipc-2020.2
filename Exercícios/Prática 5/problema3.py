# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:11:34 2021

@author: aline
"""

def arredondar_para_cima(numero):
    if numero % 1 != 0:
        return int(numero+1)
    
    return int(numero)

def palindromo(palavra):
    palavra_par = len(palavra) % 2 == 0
    indice_meio = arredondar_para_cima(len(palavra)/2)
    
    primeira_parte = palavra[:indice_meio]
    
    if palavra_par:            
        segunda_parte = palavra[indice_meio:]
    else: 
        segunda_parte = palavra[indice_meio-1:]
  
    return primeira_parte == segunda_parte[::-1]
    

palavra = input('')

if palindromo(palavra):
    print('É palíndromo')
else:
    print('Não é palíndromo')