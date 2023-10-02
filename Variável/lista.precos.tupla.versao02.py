#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Versão 02:
# Sem a verificação de par/impar. Colocando o terceiro parâmetro no range
#para pular de 2 em 2. Veja abaixo:

tabela=('Lápis',1.75,'Borracha',2,'Carderno',15.9,'Estojo',25,'Transferidor',4.2,
        'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('+'*40)
print(f'{"Listagem de preços":^40}')
print('+'*40)
for c in range(0,len(tabela),2):
    print(f'{tabela[c]:.<30}R${tabela[c+1]:>10.2f}')
print('+'*40)    
        
