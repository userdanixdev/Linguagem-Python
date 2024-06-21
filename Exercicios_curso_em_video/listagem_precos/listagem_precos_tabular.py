# Listagem de preços:

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Versão 1:

listagem = ('Lápis',1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Estojo',25,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',120.32,
            'Canetas',22.30,
            'Livro',34.90)

for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:  # daí só mostra os pares da tupla que são os nomes.
        print(f'{listagem[posicao]:30}')
for posicao in range(0,len(listagem)):
    if posicao % 2 == 1:  # dai percorre o segundo elemento da tupla
        print(f'{listagem[posicao]:30}.')
print()
print('listagem de precos:\n')
for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:  
        print(f'{listagem[posicao]:.<30}',end='')  # a listagem formata para a esquerda e 30 pontos pra direita
    else:
        print(f'R$ {listagem[posicao]:>7.2f}') 

        
