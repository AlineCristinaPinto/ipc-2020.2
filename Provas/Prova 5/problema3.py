# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:18:16 2021

@author: aline
"""

def decifrar_frase(frase_embaralhada):
    indice_meio = int(len(frase_embaralhada)/2)
    
    primeira_parte = frase_embaralhada[:indice_meio]
    segunda_parte = frase_embaralhada[indice_meio:]
    
    return primeira_parte[::-1] + segunda_parte[::-1]

frase_embaralhada = input('Frase embaralhada: ')
print('Frase correta: ', decifrar_frase(frase_embaralhada))

