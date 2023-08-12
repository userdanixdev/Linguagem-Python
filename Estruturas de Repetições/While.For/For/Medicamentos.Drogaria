# Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria
# O programa deve informar o nome e o preço do medicamento mais barato.
# Bem como a média aritmética dos preços informados.


soma_preco = 0
medicamento=input('Nome do Medicamento: ')
preco=float(input('R$:  '))
mais_barato=medicamento
menor_preco=preco
soma_preco = soma_preco + preco #Acumulador de preços
# São 5 medicamentos, sendo assim, a estrutura for in range é mais indicada.
for x in range(4):
    medicamento=input('Medicamento: ')
    preco = float(input('R$:  '))
    if preco<menor_preco:
       menor_preco=preco
       mais_barato=medicamento
       soma_preco += preco
       
media= soma_preco/5
print(f'{mais_barato} é o medicamento mais barato e custa R$ {menor_preco}.')
print(f'Média dos preços: R$ {media}.')

Result:
Nome do Medicamento: Dorflez
R$:  50
Medicamento: Dorpanina
R$:  25
Medicamento: Preferentina
R$:  30
Medicamento: Doralgina
R$:  36
Medicamento: SInucite
R$:  25
Dorpanina é o medicamento mais barato e custa R$ 25.0.
Média dos preços: R$ 15.0.

=============================


