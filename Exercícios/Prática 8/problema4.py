# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:27:53 2021

@author: aline
"""

def soma(n):
    if n > 1:
        return n + soma(n-1)
    
    return n 

n = int(input('Digite N: '))

print(soma(n))