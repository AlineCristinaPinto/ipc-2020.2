# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:41:28 2021

@author: aline
"""

def calcularMedia(nota1, nota2):
    return (nota1 + nota2) / 2

nome = input()
mediasAlunos = []

while nome != '':
	nota1 = float(input())
	nota2 = float(input())
	mediasAlunos.append((calcularMedia(nota1, nota2), nome))
	nome = input()
    
mediasAlunos.sort(reverse=True)
for infoAluno in mediasAlunos:
	print('%s - %.2f' % (infoAluno[1], infoAluno[0]))