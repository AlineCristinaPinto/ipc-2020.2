# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:11:17 2021

@author: aline
"""

def pagamento(valor_hora, horas_trabalhadas):
    desconto = 0.0
    salario_bruto = horas_trabalhadas * valor_hora
    
    if salario_bruto <= 900:
        return salario_bruto
    elif salario_bruto <= 1500:
        desconto = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        desconto = salario_bruto * 0.1
    else:
        desconto = salario_bruto * 0.2
    
    return salario_bruto - desconto
    
    