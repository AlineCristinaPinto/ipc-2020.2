# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:24:22 2021

@author: aline
"""

maxima = int(input('Digite o valor da velocidade máxima:'))
registrada = int(input('Digite o valor da velocidade registrada:'))

if registrada <= maxima:
    print('Sem Infração')
elif registrada <= (maxima + maxima*0.2) :
    print('Infração Média')    
elif registrada <= (maxima + maxima*0.5) :
    print('Infração Grave')
else:
    print('Infração Gravíssima')
