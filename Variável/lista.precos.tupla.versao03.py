#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Versão 03:
comidas=('Lápis', 2.50, 'Borracha', 4.00, 'Borracha Hello Kitty', 6.50, 'Caderno', 15.00, 'Mochila', 70.00,
             'Lapiseira 0.7', 19.00, 'Grafite 0.7', 5.90, 'Cola', 4.90, 'Corretivo', 3.50, 'Caneta', 2.50)
c=0
while c< len(comidas):
        print(f'{comidas[c]:.<20}',end="")
        c=c+1
        print(f'R${comidas[c]:>10.2f}')
        c=c+1
