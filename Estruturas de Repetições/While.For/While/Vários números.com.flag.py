#Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados
#e qual foi a soma entre elas (desconsiderando o flag).

soma = 0
cont = 0
while True:
    num=int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont=cont+1
    soma= soma + num
print(f'A soma dos {cont} valores foi {soma}.')    

Results:
Digite um valor (999 para parar): 1
Digite um valor (999 para parar): 2
Digite um valor (999 para parar): 5
Digite um valor (999 para parar): 45
Digite um valor (999 para parar): 78
Digite um valor (999 para parar): 564
Digite um valor (999 para parar): 999
A soma dos 6 valores foi 695.
==============================================================
