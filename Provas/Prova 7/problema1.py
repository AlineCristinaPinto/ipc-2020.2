# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:43:34 2021

@author: aline
"""

def calcular_media_aluno(notas):
    return sum(int(nota) for nota in notas)/len(notas)
        
arquivo = open('notas.txt', 'r', encoding='utf8') 
media_notas = []

texto = arquivo.read()
alunos = texto.split('\n')
arquivo.close() 

for aluno in alunos:
    aluno_notas = aluno.split(' ')
    media_notas.append(calcular_media_aluno(aluno_notas[1:]))
    
print('%.2f' % max(media_notas)) 
print('%.2f' % min(media_notas)) 