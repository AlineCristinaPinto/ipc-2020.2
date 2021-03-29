# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:49:49 2021

@author: aline
"""

saltos = []

for i in range(5):
    saltos.append(float(input()))

saltos.remove(min(saltos))
saltos.remove(max(saltos))

print('Média:  %.2f' % (sum(saltos)/3))