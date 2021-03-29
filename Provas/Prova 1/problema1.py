# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:53:41 2020

@author: aline
"""

investimento = float(input("Digite o valor do investimento inicial:"))
taxa_juros = float(input("Digite a taxa de juros anual:"))
anos = int(input("Digite o período do investimento em anos:"))

print("Valor futuro: %.2f" % (investimento * (1 + (taxa_juros * 0.01)) ** anos))
