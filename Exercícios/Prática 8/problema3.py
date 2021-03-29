# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:11:24 2021

@author: aline
"""

def mdc(x, y):
    if y == 0:
        return x
    
    return mdc(y, x%y)
    

x = int(input('Digite x: '))
y = int(input('Digite y: '))

print(mdc(x, y))