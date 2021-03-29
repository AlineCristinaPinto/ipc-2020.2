# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 23:02:28 2021

@author: aline
"""

x = int(input('Digite o comprimento do primeiro lado: '))
y = int(input('Digite o segundo do primeiro lado: '))
z = int(input('Digite o terceiro do primeiro lado: '))

if not ((z < (x+y)) and (y < (x+z)) and (x < (y+z))):
    print('Não é um triângulo')
elif (x == y == z):
    print('Triângulo Equilátero')
elif (x != y != z ):
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')
