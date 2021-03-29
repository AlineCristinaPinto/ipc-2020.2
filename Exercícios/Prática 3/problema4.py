# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:29:30 2021

@author: aline
"""

def calcula_valor(preco_litro, quantidade_litros, tipo_combustivel):
    if(tipo_combustivel == 'a'):
        if(quantidade_litros <= 20):
            desconto = preco_litro - preco_litro * 0.03
        else:
            desconto = preco_litro - preco_litro * 0.05
            
        return quantidade_litros * desconto  	
    else:
        if(quantidade_litros <= 20):
            desconto = preco_litro - preco_litro * 0.04
        else:
            desconto = preco_litro - preco_litro * 0.06
        
        return quantidade_litros * desconto  
    