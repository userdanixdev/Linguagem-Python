# Sorteando um item na lista:

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo
# o nome do escolhido.

import random

n1=input('Primeiro aluno: ')
n2=input('Segundo aluno: ')
n3=input('Terceiro aluno: ')
n4=input('Quarto aluno: ')
lista=[n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}.')
print()

print('outra forma')
nome=[input('Digite um nome: ')for i in range(4)]
escolha=random.choice(nome)
print('O nome sorteado foi : ',escolha)
print()

print('Terceira forma')
alunos=input('Escreva o nome dos alunos separados por vírgula: ').split(',')
print(f'O nome dos alunos foi: {random.choice(alunos)}')
