#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = total_mil = 0
menor = cont = 0
while True:   #<- Looping infinito
    produto = input('Nome do produto: ')
    preco=float(input('Preço: R$ '))
    total = total + preco
    cont =  cont + 1
    if cont == 1:
        menor = preco
    else:
        if preco<menor:
         menor = preco
    if preco>1000:
        total_mil = total_mil + 1
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('QUer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^41}'.format('Fim do programa'))
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {total_mil} produtos custando mais de mil reais.')
print(f'O produto mais barato custa R${menor:.2f}.')
      

