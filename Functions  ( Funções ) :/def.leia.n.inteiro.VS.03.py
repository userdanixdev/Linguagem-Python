# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:47:19 2024

@author: US
"""

#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
#semelhante ‘a função input() do Python, só que fazendo a validação para
#aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# VERSÃO 03:
    
def leiaInt(frase):
    num = input(frase)
    while num.isnumeric()==False:
        print('ERRO. Digite somente números inteiros!')
        num = input(frase)
        print(f'Você acabou de digitar o número {num}.')
num=leiaInt('Digite um número:')

