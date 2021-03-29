# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:48:04 2021

@author: aline
"""

preco = float(input('Digite o preço do pão:'))

for quantidade in range(1,51):
    print('%d - R$ %.2f' % (quantidade, (quantidade * preco)))