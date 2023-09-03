#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*30)
print('Seja bem vindo ao BANCO!')
print('='*30)
valor = int(input('Que valor quer sacar? R$ '))
total = valor # montante
cedula_atual=50  # comecar com uma cedula
total_cedulas= 0
while True:
    if total >=cedula_atual:
        total = total - cedula_atual
        total_cedulas = total_cedulas + 1
    else:
        if total_cedulas>0:
            print(f'Total de cédulas {total_cedulas} cédulas de R${cedula_atual} reais.')
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual ==10:
            cedula_atual = 1
        total_cedulas=0
        if total == 0:
           break
print('+'*30)
print('Volte sempre ao BANCO!')

