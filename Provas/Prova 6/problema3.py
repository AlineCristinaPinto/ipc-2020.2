# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:59:45 2021

@author: aline
"""

def calcular_produto_escalar(vetor_1, vetor_2):
    return sum((vetor_1[i] * vetor_2[i]) for i in range(len(vetor_1)))

vetor_1 = []
vetor_2 = []

dimensao = int(input('Digite a dimensão:'))

for i in range(dimensao):
    vetor_1.append(int(input()))

for i in range(dimensao):
    vetor_2.append(int(input()))
    
print('Produto Escalar: ', calcular_produto_escalar(vetor_1, vetor_2))