#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem=('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,
          'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print(listagem)
# resultado bagunçado
'''for item in listagem:
    print(item)'''
# Outro resultado de cima para baixo.
print('+'*50)
print(f'{"Lista de preços":^50}')
print('+'*50)
for item in range(0,len(listagem)):  # Com o 'len' marca quantos itens tem na tupla de cima para baixo pelo laço for in range
    if item % 2 ==0:
        print(f'{listagem[item]:.<30}',end='')
    else:
        print(f'R${listagem[item]:>10.2f}')
print('-'*40)        
    
