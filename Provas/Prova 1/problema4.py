# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:14:57 2020

@author: aline
"""

numero = int(input("Digite um inteiro de 4 algarismos:"))

milhares = int(numero / 1000)
centenas = int((numero % 1000) / 100)
dezenas = int((numero % 100) / 10)
unidades = int(numero % 10)

print("Resultado: ", (milhares + centenas + dezenas + unidades))