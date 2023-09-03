#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#---------------------------------------
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

#Versão 02:

from time import sleep
total = 0
produtos_mais_1000 =0
produtos_comprados = 0
preco_produto_mais_barato = 0

print('Processando...')
sleep(1)
print('+'*50)
print(':'*20,'Bem vindo a Loja de produtos',':'*20)
print('+'*50)
sleep(2)
print('Processando')
sleep(1)

while True:
    nome_produto = input('Digite o nome do produto: ').strip().lower().upper()
    preco_produto = float(input('Preço do produto: ').strip())
    produtos_comprados = produtos_comprados + 1
    total = total + preco_produto
    if preco_produto>1000:
        produtos_mais_1000 = produtos_mais_1000 + 1
    if produtos_comprados == 1:
        nome_produto_mais_barato = nome_produto
        preco_produto_mais_barato = preco_produto
    else:
        if preco_produto_mais_barato>preco_produto:
            preco_produto_mais_barato = preco_produto
            nome_produto_mais_barato = nome_produto
    continuar=' '        
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('Finalizando compras...')
        break
print('-'*50)
print(f'O total das compras foi E$: {total} reais.')
print(f'O produto mais de mil reais foi o {produtos_mais_1000}')
print(f'''
O produto mais barato foi: {nome_produto_mais_barato}
e seu custo foi R$ {preco_produto_mais_barato} reais.''')


-------------------------------------------------------------------------------
