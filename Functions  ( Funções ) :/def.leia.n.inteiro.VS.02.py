# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:47:19 2024

@author: US
"""

#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
#semelhante ‘a função input() do Python, só que fazendo a validação para
#aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# VERSÃO 02:
    
def leiaInt(a:str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('ERRO!Digite um número válido.')
n = leiaInt('Digite um valor:')            
print(f'Você acabou de digitar o número {n}')
print('FIM')
