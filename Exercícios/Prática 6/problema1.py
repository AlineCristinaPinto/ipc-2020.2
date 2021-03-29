# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:42:22 2021

@author: aline
"""

def ipValido(octedos):
    for octeto in octedos:
        if int(octeto) < 0 or int(octeto) > 255:
            return False
            break
    
    return True
    

ip = input()
octetos = ip.split('.')

if(ipValido(octetos)):
    print('Válido')
else:
    print('Inválido')
    