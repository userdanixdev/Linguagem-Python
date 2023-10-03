#Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Versão 05:
# Essa versão o programa irá perguntar quantos e quais produtos para entrar na lista.
# Com  estruturas de repetições 'while' e 'for x in range'.
tuple=()
while True:
    item=(input('Digite o nome do item:'))
    preco=float(input('Digite o preço do item: '))
    tuple = tuple + (item,preco)
    while True:
        novo=input('Adicionar novo item?[Y/N]').strip().upper()[0]
        if novo not in 'YN':
            print('Somente Y ou N.')
        else:
            break
    if novo == 'N':
        break
        print('Programa parou.')
print('+'*40)
print(f'{"Preços":^40}')
print('+'*40)
for x in range(0,len(tuple)):
    if x %2==0:
        print(f'{tuple[x]:.<30}',end='')
    else:
        print(f'R${tuple[x]:>10.2f}')
print('+'*40)        
