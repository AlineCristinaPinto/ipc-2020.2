# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:15:56 2021

@author: aline
"""

def buscar_datas_com_ano_mais_recente(datas):    
    ano_recente = max(data.split('/')[2] for data in datas)
    return [data for data in datas if data.find(ano_recente) > 1]

def buscar_datas_com_mes_mais_recente(datas):    
    mes_recente = max(data.split('/')[1] for data in datas)
    return [data for data in datas if data.split('/')[1] == mes_recente]

def buscar_data_com_dia_mais_recente(datas):    
    dia_recente = max(data.split('/')[0] for data in datas)
    return [data for data in datas if data.split('/')[0] == dia_recente]

def buscar_data_recente(datas):
    data_anos_recente = buscar_datas_com_ano_mais_recente(datas)
   
    if len(data_anos_recente) == 1:
        return data_anos_recente[0]
    
    data_mes_recente = buscar_datas_com_mes_mais_recente(data_anos_recente)
    
    if len(data_mes_recente) == 1:
        return data_mes_recente[0]
    
    return buscar_data_com_dia_mais_recente(data_mes_recente)[0]
    
arquivo = open('datas.txt', 'r', encoding='utf8') 

texto = arquivo.read()
datas = texto.split('\n')
arquivo.close() 
    
print(buscar_data_recente(datas))