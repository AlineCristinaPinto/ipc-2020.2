# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:39:16 2020

@author: aline
"""

velocidade = input("Digite o valor da velocidade:")
aceleracao = input("Digite o valor da aceleração:")
tempo = input("Digite o valor do tempo:")

velocidade = float(velocidade)
aceleracao = float(aceleracao)
tempo = float(tempo)

print("Velocidade final: %.2f" % (velocidade + aceleracao * tempo))
print("Distância percorrida: %.2f" % (velocidade * tempo + (aceleracao * tempo ** 2)/2 ))