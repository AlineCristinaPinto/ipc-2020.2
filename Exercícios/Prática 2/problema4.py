# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:51:27 2021

@author: aline
"""

salario_atual = float(input('Digite o valor do salário:'))
aumento = 0

if salario_atual <= 280:
    aumento = salario_atual * 0.2
elif salario_atual <= 700:
    aumento = salario_atual * 0.15
elif salario_atual <= 1500:
    aumento = salario_atual * 0.1
else:
    aumento = salario_atual * 0.05
    
print('Valor do aumento: %.2f' % aumento)
print('Novo salário: %.2f' % (salario_atual + aumento))