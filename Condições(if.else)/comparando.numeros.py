Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais


num1=float(input('Digite um número : '))
num2=float(input('Digite outro número: '))
if num1>num2:
           print('O número 1 é maior que o número 2. ')
elif num2>num1:
    print('O número 2 é maior que o número 1. ')
elif num2==num1 or num1==num2:
    print('Os números são iguais. ')
    
