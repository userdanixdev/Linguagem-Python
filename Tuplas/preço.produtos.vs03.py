#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.


# Versão 03:
# Essa versão o programa irá perguntar quantos e quais produtos entrar na lista.(tupla)

qtd=int(input('Quantos produtos voce quer listar? '))
produtos=()
for c in range(0,qtd):
    nome=input('Nome do produto: '),float(input('Preço do produto: '))
    produtos = produtos + (nome[0],nome[1])
print('='*50)
for p in range(0,len(produtos),2):
    nome = produtos[p]
    preco=produtos[p+1]
    pontos='.'*(50-len(produtos[p]))
    print(f'{nome.capitalize()}{pontos}R${preco:.2f}')
    
    


