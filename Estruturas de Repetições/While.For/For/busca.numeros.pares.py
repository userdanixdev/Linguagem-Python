# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:07:00 2024

@author: US
"""

## Busca de número pares dentro de listas:
  
lista1 = [10,16,24,39,47]
lista2 = [32,89,47,76,12]

soma = 0   ## Contador inicial

for lista in [lista1,lista2]:
    for num in lista:
        if num % 2 == 0:
            soma = soma + num
print('A soma dos números pares das duas listas são:', soma)

    