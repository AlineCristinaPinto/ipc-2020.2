# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:01:56 2021

@author: aline
"""

def arredondar_para_cima(numero):
    return int(numero+1) if numero % 1 != 0 else int(numero)

def palindromo(frase):
    frase_par = len(frase) % 2 == 0
    indice_meio = arredondar_para_cima(len(frase)/2)
    
    primeira_parte = frase[:indice_meio]
    segunda_parte = frase[indice_meio:] if frase_par else frase[indice_meio-1:]
    
    return primeira_parte == segunda_parte[::-1]

arquivo = open('frases.txt', 'r', encoding='utf8') 
quantidade_palindromos = 0

texto = arquivo.read()
frases = texto.split('\n')
arquivo.close() 

for frase in frases:
    if(palindromo(frase.replace(' ', '').lower())):
        quantidade_palindromos += 1
        
print('Quantidade de palíndromos: ', quantidade_palindromos)

