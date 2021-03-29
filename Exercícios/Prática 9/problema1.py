# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:23:50 2021

@author: aline
"""

palavra = input()
letras = dict()

for letra in palavra:
	letras[letra] = letras.get(letra, 0) + 1

letrasPorQuantidade = list()

for letra, quantidade in letras.items():
    letrasPorQuantidade.append((quantidade, letra))
    
letrasPorQuantidade.sort(reverse=True)

print(letrasPorQuantidade[0])