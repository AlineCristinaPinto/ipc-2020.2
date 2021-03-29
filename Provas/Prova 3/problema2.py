# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:03:49 2021

@author: aline
"""

def consumo(distancia_percorrida, litros_consumidos_gasolina):
    km_l = distancia_percorrida/litros_consumidos_gasolina
    
    if km_l < 8:
        return 'Venda o carro!'
    elif km_l < 12:
        return 'Econômico!'
    else:
        return 'Super econômico!'