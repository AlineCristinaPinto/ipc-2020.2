# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:17:43 2021

@author: aline
"""

def has_duplicates(lista):
    for item in lista:
        if lista.count(item) > 1:
            return True
        
    return False 
