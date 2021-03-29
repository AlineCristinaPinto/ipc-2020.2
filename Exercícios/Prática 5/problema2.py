# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:54:28 2021

@author: aline
"""

palavra = input('')

palavra_aux = palavra

for letra in palavra:
    palavra_aux = palavra_aux.replace((letra+letra), letra.upper())
    
print(palavra_aux)