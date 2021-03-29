# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 23:52:15 2021

@author: aline
"""
import math 

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a==0:
    print('Não é uma equação quadrática')
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print('Não existe raiz real')
    elif delta == 0:
        print('Raiz única')
        print('Raiz = %.2f' % float(-b/(2*a)))
    else:
        print('Raiz 1 = %.2f' % float((-b + math.sqrt(delta))/(2*a)))
        print('Raiz 2 = %.2f' % float((-b - math.sqrt(delta))/(2*a)))




    