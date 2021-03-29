# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:50:17 2021

@author: aline
"""

DIA = 0
MES = 1
ANO = 2

def data_referencia_ultrapassou_aniversario(nascimento, referencia):
    return (referencia[MES] > nascimento[MES] 
            or (referencia[MES] == nascimento[MES] 
                and referencia[DIA] > nascimento[DIA]))

def calcular_idade(aniversario, referencia):
    data_nascimento = aniversario.split('/')
    data_referencia = referencia.split('/')
    
    if data_referencia_ultrapassou_aniversario(data_nascimento, data_referencia):
        return int(data_referencia[ANO]) - int(data_nascimento[ANO]) 
    
    return int(data_referencia[ANO]) - int(data_nascimento[ANO]) - 1

arquivo = open('datas.txt', 'r', encoding='utf8') 
data_referencia = '05/10/2020'

texto = arquivo.read()
datas = texto.split('\n')
arquivo.close() 

for data in datas:
    dados_pessoa = data.split(' ')
    print('Nome: ', dados_pessoa[0])
    print('Idade: %d anos' % calcular_idade(dados_pessoa[1], data_referencia))
    