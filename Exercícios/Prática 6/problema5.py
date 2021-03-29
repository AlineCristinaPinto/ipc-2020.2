# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:09:31 2021

@author: aline
"""

def formatar_para_data_americana(data_brasileira):
    unidades_data = data_brasileira.split('/')
    return unidades_data[1] + '/' + unidades_data[0] + '/' + unidades_data[2]
    
    
data = input()
print(formatar_para_data_americana(data))