# Estatisticas em produtos:

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Versão 01:

# Variáveis contadoras, numeros inteiros:
total = 0
totmil = 0
menor_preco = 0
cont = 0

barato = ' '  # Recebe string vazia

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi {total}.')    
print(f'Temos {totmil} que custa mais de mil reais.')
print(f'O produto mais barato custa R${menor:.2f}. e foi {barato}')
