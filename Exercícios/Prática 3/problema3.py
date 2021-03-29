# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:23:12 2021

@author: aline
"""

def verifica_triangulo(x, y, z):
    return ((z < (x+y)) and (y < (x+z)) and (x < (y+z)))

def tipo_triangulo(x, y, z):
    if not verifica_triangulo(x, y, z):
        return 'Não é um triângulo'
    elif (x == y == z):
        return 'Equilátero'
    elif (x != y != z ):
        return 'Escaleno'
    else:
        return 'Isósceles'