# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:18:41 2021

@author: aline
"""

def calcular_media_aluno(notas):
    return sum(int(nota) for nota in notas)/len(notas)
        
arquivo = open('notas.txt', 'r', encoding='utf8') 

texto = arquivo.read()
alunos = texto.split('\n')
arquivo.close() 

for aluno in alunos:
    aluno_notas = aluno.split(' ')
    media_aluno = calcular_media_aluno(aluno_notas[1:])
    
    if media_aluno >= 60:
        print('Nome: %s - Média:  %.2f' % (aluno_notas[0], media_aluno))