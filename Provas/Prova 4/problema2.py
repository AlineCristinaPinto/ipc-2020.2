# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:20:41 2021

@author: aline
"""

def serie_harmonica(n):
    hn = 0
    
    for denominador in range(1, n+1):
        hn += 1/denominador
        
    return hn

n = int(input('Digite n:'))
print('Resultado %.2f' % serie_harmonica(n))