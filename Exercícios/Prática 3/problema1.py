# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 19:53:55 2021

@author: aline
"""

def pagamento(salario_atual):
    ajuste = 0.0
    
    if salario_atual <= 280:
        ajuste = salario_atual * 0.2
    elif salario_atual <= 700:
        ajuste = salario_atual * 0.15
    elif salario_atual <= 1500:
        ajuste = salario_atual * 0.1
    else:
        ajuste = salario_atual * 0.05
    
    return salario_atual + ajuste