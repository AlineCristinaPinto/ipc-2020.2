# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:01:04 2020

@author: aline
"""

aposta_pedro = float(input("Digite o valor que o Pedro apostou:"))
aposta_joao = float(input("Digite o valor que o João apostou:"))
aposta_marcela = float(input("Digite o valor que a Marcela apostou:"))
premio = float(input("Digite o valor do prêmio:"))

k = premio / (aposta_pedro + aposta_joao + aposta_marcela)

print("Prêmio do Pedro: %.2f" % (aposta_pedro * k))
print("Prêmio do João: %.2f" % (aposta_joao * k))
print("Prêmio da Marcela: %.2f" % (aposta_marcela * k))
