# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:39:11 2021

@author: aline
"""

numero = int(input('Digite um inteiro:'))
arquivo = open('texto.txt', 'r', encoding='utf8') 

texto = arquivo.read() 
palavras = texto.split()
arquivo.close() 

for palavra in palavras:
    if len(palavra) >= numero:
        print(palavra)
