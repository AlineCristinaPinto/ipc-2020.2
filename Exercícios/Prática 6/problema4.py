# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:05:29 2021

@author: aline
"""

temperatura_media_mensal = []

for i in range(12):
    temperatura_media_mensal.append(int(input()))

media_anual = sum(temperatura_media_mensal)/12
print('Média: %.2f' % media_anual)

for temperatura in temperatura_media_mensal:
    if temperatura > media_anual:
        print(temperatura)