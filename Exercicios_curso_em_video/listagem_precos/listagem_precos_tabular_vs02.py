# Listagem de preços:

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Versão 2: Dentro do range colocando como parâmetro 2 em 2:

listagem = ('Lápis',1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',120.32,
            'Canetas',22.30,
            'Livro',34.90)

for c in range(0,len(listagem),2):
    print(f'{listagem[c]:.<34}',end='')
    print(f'R$ {listagem[c+1]:>7.2f}')
print('-'*45)    
# Fazendo em uma linha:
for c in range(0,len(listagem),2):
    print(f'{listagem[c]:.<34}'f'R$ {listagem[c+1]:>7.2f}')
print('-'*45)    
