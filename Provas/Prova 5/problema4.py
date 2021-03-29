# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:32:38 2021

@author: aline
"""

def rotacionar_caracter(letra, chave):
    soma_caracteres = ord(letra) + chave
  
    while soma_caracteres > ord('z'):
        aux = soma_caracteres - ord('z')
        soma_caracteres = ord('a') + aux - 1
       
    return chr(soma_caracteres)

def criptografar_por_cifra_de_cesar(palavra, chave):
    palavra_criptografada = ''
    
    for letra in palavra:
        palavra_criptografada += rotacionar_caracter(letra, chave)
    
    return palavra_criptografada

palavra = input('Digite uma palavra: ')
chave = int(input('Digite o valor da chave: '))

print('Resultado: ', criptografar_por_cifra_de_cesar(palavra, chave))