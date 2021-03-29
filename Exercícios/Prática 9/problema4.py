# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:49:06 2021

@author: aline
"""

numero = int(input())
numeros = []

while numero != -1:
	numeros.append(numero)
	numero = int(input())
    
numerosDict = dict()
numerosPorQuantidade = list()

for numero in numeros:
	numerosDict[numero] = numerosDict.get(numero, 0) + 1
    
for numero, quantidade in numerosDict.items():
    numerosPorQuantidade.append((quantidade, numero))
    
numerosPorQuantidade.sort(reverse=True)

print(numerosPorQuantidade[0][1])