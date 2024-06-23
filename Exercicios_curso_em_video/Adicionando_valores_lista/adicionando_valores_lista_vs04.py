# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Adicionando valores em uma lista:
# Versão 04:

lista = []
while True:
    try:
        lista.append(int(input('Escolha um valor: ')))
        print('Valor adicionando com sucesso..')
    except ValueError:
        print('Erro ao preencher o requisito,apenas números...')
    sair = ''
    sair=input('Deseja continuar? [S/N]').strip().upper()[0]
    while sair not in 'SN':
        sair=input('Deseja continuar? [S/N]').strip().upper()[0]
    if sair == 'N':
        break
lista.sort()
print(f'Os números listados foram: {lista}.')
