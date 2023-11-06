#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Versão 02:

lista=[]
while True:
    n1=int(input('Digite um número: '))
    if n1 in lista:
        print('Digite um valor que não está na lista!')
    else:
        lista.append(n1)
    n2=input('Deseja continuar? [S/N]')
    if n2.lower()=='n':
        break
    lis=sorted(lista)
    print(f'Você digitou os valores{lis}.')
print(f'Você digitou os valores{lis}.')
print('Fim do programa')

Resultado:

Digite um número: 5
Deseja continuar? [S/N]s
Você digitou os valores[5].
Digite um número: 10
Deseja continuar? [S/N]s
Você digitou os valores[5, 10].
Digite um número: 15
Deseja continuar? [S/N]s
Você digitou os valores[5, 10, 15].
Digite um número: 15
Digite um valor único!
Deseja continuar? [S/N]s
Você digitou os valores[5, 10, 15].
Digite um número: 1
Deseja continuar? [S/N]n
Você digitou os valores[5, 10, 15].
===================================================





