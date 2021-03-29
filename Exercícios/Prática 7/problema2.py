# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:36:09 2021

@author: aline
"""

arquivo = open('texto.txt', 'r', encoding='utf8') 

texto = arquivo.read() 
palavras = texto.split()
arquivo.close() 

maior_palavra = max(palavras, key=len)

print(maior_palavra)
print(len(maior_palavra))