# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:25:59 2021

@author: aline
"""

salario_carlos = float(input('Digite o salário do Carlos: '))
rendimento_poupanca = float(input('Digite o rendimento da poupança(%): '))
rendimento_renda_fixa = float(input('Digite o rendimento do fundo de renda fixa(%): '))

salario_joao = salario_carlos/3
rendimento_poupanca = rendimento_poupanca/100
rendimento_renda_fixa = rendimento_renda_fixa/100

meses = 0

while (salario_joao < salario_carlos):
    meses += 1
    salario_carlos = salario_carlos + salario_carlos * rendimento_poupanca
    salario_joao = salario_joao + salario_joao * rendimento_renda_fixa
        
print('Meses: ', meses)