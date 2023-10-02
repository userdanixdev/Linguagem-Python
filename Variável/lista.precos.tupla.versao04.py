#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Versão 04:
# Essa versão o programa irá perguntar quantos e quais produtos para entrar na lista.
final=int(input('Quantos produtos você quer listar?'))
produtos=()
for c in range(0,final):
    nome=input('Nome do produto:'),float(input('Preço do produto: '))
    produtos = produtos + (nome[0],nome[1])
print('-'*50)
for c in range(0,len(produtos)):
    if c%2==0:
        nome=produtos[c]
        preco=produtos[c+1]
        pontos='.'*(50-len(produtos[c]))
        print(f'{nome.capitalize()}{pontos}R${preco:.2f}')
print('+'*50)        
