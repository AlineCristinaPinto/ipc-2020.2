# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 23:22:09 2021

@author: aline
"""

valor_hora = float(input('Digite o valor da hora de trabalho: '))
qtd_horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = float(valor_hora * qtd_horas_trabalhadas)
inss = float(salario_bruto * 0.1)
fgts = float(salario_bruto * 0.11)
ir = 0.0

if salario_bruto <= 900:
    ir = 0.0
elif salario_bruto <= 1500 :
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2
    
descontos = float(inss + ir)
salario_liquido = float(salario_bruto - descontos)

print('Salário Bruto: R$ %.2f' % salario_bruto)
print('IR: R$ %.2f' % ir)
print('INSS: R$ %.2f' % inss)
print('FGTS: R$ %.2f' % fgts)
print('Total de descontos: R$ %.2f' % descontos)
print('Salário líquido: R$ %.2f' % salario_liquido)
    
