#Faça um programa que leia um número qualquer e mostre o seu fatorial:
#Com a estrutura de repetição for


numero=int(input('Digite um número para saber o fatorial: '))
fatorial=1
for i in range(1,numero+1):
    fatorial = fatorial *i
    print(f'O resultado de {numero} é {fatorial}.')

