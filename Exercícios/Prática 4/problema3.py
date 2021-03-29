# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:55:09 2021

@author: aline
"""

print('Loja Quase Dois - Tabela de preços')
preco = 1.99

for quantidade in range(1,51):
    print('%d - R$ %.2f' % (quantidade, (quantidade * preco)))