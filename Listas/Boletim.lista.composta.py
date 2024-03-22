#Crie um programa que leia nome e duas notas de vários alunos e
#guarde tudo em uma lista composta. No final, mostre um boletim contendo a
#média de cada um e permita que o usuário possa mostrar as notas de cada
#aluno individualmente.
ficha=[]
while True:
    nome=input('Nome: ')
    nota1=float(input('Nota 01: '))
    nota2=float(input('Nota 02: '))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2], media])                  
    resp=(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
print('='*30)   
#print(ficha)
print(f'{"No.":<4}{"Nome":<10}{"MÉDIA":>8}')
print('+'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('+'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc ==999:
        print('Finalizou.')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')

----------------//--------------------------------//--------------------------------------//--------------------------------//
    
