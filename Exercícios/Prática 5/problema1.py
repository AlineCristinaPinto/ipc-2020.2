# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:50:41 2021

@author: aline
"""

nome_completo = input('')

inicial_sobrenome = nome_completo.rfind(' ')
nome_formatado = nome_completo[inicial_sobrenome+1:] + ', ' + nome_completo[:inicial_sobrenome]

print('Nome formatado:', nome_formatado)