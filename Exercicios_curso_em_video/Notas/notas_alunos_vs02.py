# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

#Versão 02:

ficha = list()
while True:
    ficha.append([input('Nome: '),[float(input('Nota 1: ')),float(input('Nota 2: '))]])
    c = input('Deseja continuar? ').lower()
    if c == 'n':
        break
for c,v in enumerate(ficha):
    print('\n',c+1,'nome',v[0].title(),',a primeira nota é',v[1][0],'e a segunda nota é',v[1][1])
    print('a média entre as notas deste aluno é',(v[1][0]+v[1][1])/2)
