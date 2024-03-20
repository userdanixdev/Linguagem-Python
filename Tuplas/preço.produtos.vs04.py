#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.


# Versão 04:
# Essa versão o programa irá perguntar quantos e quais produtos entrar na lista.(tupla)
# Best Version

tuple=()
while True:
    item=input('Digite o nome do item: ')
    preco=float(input('Digite o preço do item: '))
    tuple = tuple + (item,preco)
    while True:
        novo_item=input('Adicionar novo item?[S/N]').strip().upper()[0]
        if novo_item not in 'SN':
            print('Somente S para SIM ou N para NÃO')
        else:
            break
    if novo_item == 'N':
        break
        print('Programa finalizado.')
print('+'*40)
print(f'{"Preços":^40}')
print('+'*40)
for x in range(0,len(tuple),2):
    print(f'{tuple[x]:.<28}R${tuple[x+1]:>10.2f}')
print('+'*40)    
    
    
    


