# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:26:58 2020

@author: aline
"""

PI =  3.1415

raio = input("Digite o valor do raio da circunferência:")
raio = float(raio)

print("Perímetro: %.2f" % (2 * PI * raio))
print("Área: %.2f" % (PI * raio ** 2))
print("Volume: %.2f" % (4 * PI * raio ** 3/3))