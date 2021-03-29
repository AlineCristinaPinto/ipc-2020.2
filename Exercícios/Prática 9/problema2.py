# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:36:39 2021

@author: aline
"""

palavra = input()
letras = dict()
vogais = ('a', 'e', 'i', 'o', 'u')

for letra in palavra:
    if letra in vogais:
        letras[letra] = letras.get(letra, 0) + 1

vogaisPorQuantidade = list()

for letra, quantidade in letras.items():
    vogaisPorQuantidade.append((quantidade, letra))
    
vogaisPorQuantidade.sort(reverse=True)

print(vogaisPorQuantidade[0][1])