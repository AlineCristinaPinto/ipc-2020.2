# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:46:08 2021

@author: aline
"""

numero = int(input('Digite um inteiro:'))
arquivo = open('texto.txt', 'r', encoding='utf8') 

texto = arquivo.read() 
palavras = texto.split()
arquivo.close() 

for palavra in palavras:
    if len(palavra) <= numero:
        print(palavra)