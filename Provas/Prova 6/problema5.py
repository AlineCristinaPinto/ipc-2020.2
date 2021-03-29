# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:31:04 2021

@author: aline
"""

def tamanho_maior_string(lista):
    return max(len(item) for item in lista) if len(lista) > 0 else 0

