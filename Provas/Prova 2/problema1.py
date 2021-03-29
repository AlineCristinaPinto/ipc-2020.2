# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:31:09 2021

@author: aline
"""

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

mediana = numero_1

if (numero_1 <= numero_2 <= numero_3) or (numero_3 <= numero_2 <= numero_1):
    mediana = numero_2
elif (numero_1 <= numero_3 <= numero_2) or (numero_2 <= numero_3 <= numero_1):
    mediana = numero_3
else:
    mediana = numero_1

print('Mediana:', mediana)