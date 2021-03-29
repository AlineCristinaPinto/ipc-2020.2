# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:46:24 2021

@author: aline
"""

numero = int(input("Digite um inteiro:"))

print('Tabuada de %d:' % numero)

for multiplicador in range(1,11):
    print('%d X %d = %d' % (numero, multiplicador, (numero * multiplicador)))

