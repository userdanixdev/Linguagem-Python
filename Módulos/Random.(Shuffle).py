# Um professor precisa sortear uma ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

from random import shuffle
print('''Bem vindo ao sorteio de alunos do professor em Python!
            Agora, nesse sorteio, será ORDENADO POR UMA LISTA!
''')
n1=input('Digite o nome do primeiro aluno: ')
n2=input('Digite o nome do segundo aluno: ')
n3=input('Digite o nome do terceiro aluno: ')
n4=input('Digite o nome do quarto aluno: ')
n5=input('Digite o nome do quinto aluno: ')
n6=input('Digite o nome do sexto aluno: ')
lista =[n1,n2,n3,n4,n5,n6]
#obrigatório_excluir_random
#escolhido = random.shuffle(lista)
shuffle(lista)
print(f'A ordem dos alunos sorteados será: {lista}.')
print('Fim do programa meus queridos')

Result:
Digite o nome do primeiro aluno: Daniel
Digite o nome do segundo aluno: Daniela
Digite o nome do terceiro aluno: Marisa
Digite o nome do quarto aluno: Junior
Digite o nome do quinto aluno: Adelino
Digite o nome do sexto aluno: Thiago
A ordem dos alunos sorteados será: ['Thiago', 'Junior', 'Marisa', 'Adelino', 'Daniel', 'Daniela'].
Fim do programa meus queridos





