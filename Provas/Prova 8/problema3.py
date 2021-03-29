# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 21:16:08 2021

@author: aline
"""

def ler_arquivo(arquivo):
    texto = [linha.rstrip() for linha in arquivo]
    competidores = {}
    
    for competidor in texto:
        competidor_tempos = competidor.split()
        competidores[competidor_tempos[0]] = competidor_tempos[1:] 
    
    return competidores
    
def calcular_media_tempo(tempos):
    return sum(int(tempo) for tempo in tempos)/len(tempos)

def buscar_media_competidores(competidores):
    resultado_competidores = {}
    for nome, tempos in competidores.items():
        resultado_competidores[nome] = calcular_media_tempo(tempos) 
    
    return resultado_competidores

def ordenar_crescente(resultado):
    return sorted([(valor, competidor) for competidor, valor in resultado.items()])

def buscar_melhor_volta(tempos):
    return min(int(tempo) for tempo in tempos)

def buscar_competidor_melhor_volta(competidores):
    resultado_competidores = {}
    for nome, tempos in competidores.items():
        resultado_competidores[nome] = buscar_melhor_volta(tempos) 
        
    return ordenar_crescente(resultado_competidores)[0]

def exibir_melhor_volta(competidores):
    competidor = buscar_competidor_melhor_volta(competidores)    
    print('Melhor volta: %s - %d segundos' % (competidor[1], competidor[0]))
    
def exibir_classificacao(resultado):
    posicao = 1    
    print('Classificação final:')
    for competidor in resultado:
        print('%d - %s - %.2f' % (posicao, competidor[1], competidor[0]))
        posicao += 1
 

arquivo = open('tempos.txt', 'r', encoding='utf8') 

competidores = ler_arquivo(arquivo)
arquivo.close() 
competidores_tempo_medio = buscar_media_competidores(competidores)

exibir_melhor_volta(competidores)
exibir_classificacao(ordenar_crescente(competidores_tempo_medio))   