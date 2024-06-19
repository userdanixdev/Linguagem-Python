# Estatisticas em produtos:

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Versão 02:

total = 0
produtos_1000 = 0
produtos_comprados = 0
preco_produto_mais_barato = 0

print()
print('Loja')
while True:
    nome_produto = input('Nome do produto: ').strip().lower()
    preco_produto = float(input('Preço do produto: ').strip())
    produtos_comprados += 1
    total += preco_produto
    if preco_produto > 1000:
        produtos_1000 += 1
    if produtos_comprados == 1:
        nome_produto_mais_barato = nome_produto
        preco_produto_mais_barato = preco_produto
    else:
        if preco_produto_mais_barato > preco_produto:
            preco_produto_mais_barato = preco_produto
            nome_produto_mais_barato = nome_produto
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if continuar != 'S' and continuar != 'N':
            print('Opção inválida.')
        else:
            break
    if continuar == 'N':
        print('Finalizando as compras...')
        break
print(f'Total:{total}\nProdutos mais de R$1.000,00:{produtos_1000}\nProduto mais barato:{nome_produto_mais_barato}.')
print(f'O produto mais barato custou:{preco_produto_mais_barato}.')
        
    
