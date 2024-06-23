# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Adicionando valores em uma lista:
# Versão 02:

lista = []
resposta = '' 
while resposta in 'S':
    num=int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Esse número já existe.')
    resposta = input('Deseja continuar? [S/N]').upper()
    if resposta == 'N':
        break
print(f'A lista: {lista}.')    
print(f'A lista em ordem:{sorted(lista)}')    

