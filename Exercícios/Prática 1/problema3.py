# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:45:00 2020

@author: aline
"""

HORA_EM_SEGUNDOS = 3600
MINUTO_EM_SEGUNDOS = 60

tempo_segundos = input("Digite o valor do tempo em segundos:")
tempo_segundos = int(tempo_segundos)

horas = int(tempo_segundos / HORA_EM_SEGUNDOS)
minutos = int((tempo_segundos % HORA_EM_SEGUNDOS) / MINUTO_EM_SEGUNDOS)
segundos = int(tempo_segundos % MINUTO_EM_SEGUNDOS)

print("Valor convertido: %d h %d min %d s" % (horas, minutos, segundos))