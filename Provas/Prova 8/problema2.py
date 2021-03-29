# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:19:54 2021

@author: aline
"""

UNIDADES = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV',
            5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}

DEZENAS = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL',
           5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}

CENTENAS = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD',
            5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

def numero_para_romano(numero):     
    if numero > 99:
        return CENTENAS[int(numero/100)] + DEZENAS[int((numero%100)/10)] + UNIDADES[numero%10]
    elif numero > 9:
        return  DEZENAS[int((numero%100)/10)] + UNIDADES[numero%10]
    else:
        return UNIDADES[numero]


numero = int(input('Digite um número: '))
print('Número Romano: ', numero_para_romano(numero))