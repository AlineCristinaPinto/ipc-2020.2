# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:23:00 2021

@author: aline
"""

arquivo = open('texto.txt', 'r', encoding='utf8') 
linhas_texto = []

for linha in arquivo:
    linhas_texto.append(linha)

arquivo.close()     
maior_linha = max(linhas_texto, key=len)

print(maior_linha)
print(len(maior_linha))