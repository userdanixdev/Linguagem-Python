# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Versão 01:

ficha = list()
while True:
    nome=input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resposta = input('Quer continuar? [S/N] ')
    if resposta in 'Nn':
        break
print('+'*36)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i,a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno?'))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Valew')        
