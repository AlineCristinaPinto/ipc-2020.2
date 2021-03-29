# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:12:37 2021

@author: aline
"""

def populacao(num_habitantes_a, taxa_crescimento_a, num_habitantes_b, taxa_crescimento_b):
    anos = 0
    taxa_crescimento_a = taxa_crescimento_a/100
    taxa_crescimento_b =  taxa_crescimento_b/100
    
    while (num_habitantes_a < num_habitantes_b):
        anos += 1
        num_habitantes_a = num_habitantes_a + num_habitantes_a * taxa_crescimento_a
        num_habitantes_b = num_habitantes_b + num_habitantes_b * taxa_crescimento_b
    
    return anos
        
def main():
    pop_a = int(input("Digite a população da cidade A:"))
    taxa_a = float(input("Digite a taxa de crescimento da população da cidade A:"))
    pop_b = int(input("Digite a população da cidade B:"))
    taxa_b = float(input("Digite a taxa de crescimento da população da cidade B:"))
    
    print(populacao(pop_a, taxa_a, pop_b, taxa_b))
    
main()
    