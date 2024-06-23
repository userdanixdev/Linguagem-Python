# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Adicionando valores em uma lista:
# Versão 01:


numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado.')
    r=input('Quer continuar? [S/N] ')
    if r in 'Nn':
        break
print(f'Vc digitou os valores...{numeros}.')
numeros.sort()
print(f'Os números em ordem crescente {numeros}.')
