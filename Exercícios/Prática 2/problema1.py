# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:17:44 2021

@author: aline
"""

primeiro = int(input('Digite o primeiro inteiro:'))
segundo = int(input('Digite o segundo inteiro:'))
terceiro = int(input('Digite o terceiro inteiro:'))
quarto = int(input('Digite o quarto inteiro:'))
quinto = int(input('Digite o quinto inteiro:'))

maior = primeiro
menor = primeiro
contador = 0

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro
if quarto > maior:
    maior = quarto
if quinto > maior:
    maior = quinto
    
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro
if quarto < menor:
    menor = quarto
if quinto < menor:
    menor = quinto
    
if primeiro % 3 == 0:
    contador+=1
if segundo % 3 == 0:
    contador+=1
if terceiro % 3 == 0:
    contador+=1
if quarto % 3 == 0:
    contador+=1
if quinto % 3 == 0:
    contador+=1

print('Maior: ', maior)
print('Menor: ', menor)
print('Quantidade de divisíveis por 3: ', contador)