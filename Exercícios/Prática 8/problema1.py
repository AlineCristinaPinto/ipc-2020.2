# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:01:08 2021

@author: aline
"""

def soma(m, n):
    if n > m:
        return m + soma(m + 1, n)
    
    return m 

m = int(input('Digite m: '))
n = int(input('Digite n: '))

print(soma(m, n))