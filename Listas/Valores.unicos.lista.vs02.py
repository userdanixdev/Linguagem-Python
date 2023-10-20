#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Versão 02:

lista=[]
while True:
    n1=int(input('Digite um número: '))
    if n1 in lista:
        print('Digite um valor único!')
    else:
        lista.append(n1)
    n2=input('Deseja continuar? [S/N]')
    if n2.lower()=='n':
        break
    lis=sorted(lista)
    print(f'Você digitou os valores{lis}.')
print(f'Você digitou os valores{lis}.')
    





