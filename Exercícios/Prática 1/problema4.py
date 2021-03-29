# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:57:59 2020

@author: aline
"""

numero = input("Digite um inteiro de 4 algarismos:")
numero = int(numero)

milhares = int(numero / 1000)
centenas = int((numero % 1000) / 100)
dezenas = int((numero % 100) / 10)
unidades = int(numero % 10)

numero_invertido = (unidades * 1000) + (dezenas * 100) + (centenas * 10) + milhares

print("Valor invertido:", numero_invertido)