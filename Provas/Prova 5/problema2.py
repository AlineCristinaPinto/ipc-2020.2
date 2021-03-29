# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:50:13 2021

@author: aline
"""

def palavras_alternadas(primeira_palavra, segunda_palavra):
    palavras_combinadas = ''
    
    if len(primeira_palavra) < len(segunda_palavra):
        tamanho_menor_palavra = len(primeira_palavra)
        maior_palavra = segunda_palavra
    else:
        tamanho_menor_palavra = len(segunda_palavra)
        maior_palavra = primeira_palavra
        
    for i in range(tamanho_menor_palavra):
        palavras_combinadas += primeira_palavra[i] + segunda_palavra[i]
        
    return palavras_combinadas + maior_palavra[tamanho_menor_palavra:]

primeira_palavra = input('Digite a primeira palavra: ')
segunda_palavra = input('Digite a segunda palavra: ')

print('Combinação: ', palavras_alternadas(primeira_palavra, segunda_palavra))
