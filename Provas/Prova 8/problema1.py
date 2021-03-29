# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:50:02 2021

@author: aline
"""

TRINCA_AMINOACIDO = {'UUU': 'Phe', 'CUU': 'Leu', 'UUA': 'Leu',
                     'AAG': 'Lisina', 'UCU': 'Ser', 'UAU': 'Tyr',
                     'CAA': 'Gln'}

def buscar_trincas(rna):
    return [(rna[i:i+3]) for i in range(0, len(rna), 3)] 

def buscar_cadeia_aminoacidos(trincas):
    cadeia_aminoacidos=TRINCA_AMINOACIDO[trincas[0]]

    for i in range(1, len(trincas)):
        cadeia_aminoacidos += '-' + TRINCA_AMINOACIDO[trincas[i]]
        
    return cadeia_aminoacidos


rna = input('Digite o RNA: ')
print('Cadeia de Aminoácidos: ', buscar_cadeia_aminoacidos(buscar_trincas(rna)))