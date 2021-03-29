# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:08:01 2021

@author: aline
"""

def arredondar_para_cima(numero):
    if numero % 1 != 0:
        return int(numero+1)
    
    return numero

def obter_horas_estacionamento(hora_chegada, min_chegada, hora_saida, min_saida):
    minutos_estacionados = 0

    if hora_chegada > hora_saida:
        minutos_estacionados = (24 - hora_chegada + hora_saida -1)*60 + (60 - min_chegada + min_saida)
    else:
        minutos_estacionados = (hora_saida - hora_chegada - 1)*60 + (60 - min_chegada + min_saida)
    
    return arredondar_para_cima(minutos_estacionados/60)

def estacionamento(hora_chegada, min_chegada, hora_saida, min_saida):
    horas_estacionados = obter_horas_estacionamento(hora_chegada, min_chegada, hora_saida, min_saida)
            
    if horas_estacionados <= 2:
        return (horas_estacionados*1)
    elif horas_estacionados <= 4:
        return (horas_estacionados*1.40)
    else:
        return (horas_estacionados*2)
        
def main():
    hora_chegada = int(input("Hora chegada:"))
    min_chegada = int(input("Min chegada:"))
    hora_saida = int(input("Hora partida:"))
    min_saida = int(input("Min partida:"))
    
    print('Preço: R$ %.2f' % estacionamento(hora_chegada, min_chegada, hora_saida, min_saida))
    
main()