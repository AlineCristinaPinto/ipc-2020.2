# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:59:50 2021

@author: aline
"""

def fizz_buzz(numero):
    
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero