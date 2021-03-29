# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:39:12 2021

@author: aline
"""

idade = int(input('Digite a idade:'))
tempo = int(input('Digite o tempo de contribuição:'))
sexo = str(input('Digite o sexo (M/F):'))

if (sexo == 'M' and ((idade >= 60 and tempo >= 35) or idade >= 65)) or ( sexo == 'F' and ((idade >= 55 and tempo >= 30) or idade >= 60)):
    print('Pode aposentar')
else:
    print('Não pode aposentar')
