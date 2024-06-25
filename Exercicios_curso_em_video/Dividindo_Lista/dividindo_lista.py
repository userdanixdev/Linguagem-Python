# Dividindo listas:

def extraindo_dados():

    valores = []
    while True:
        valores.append(int(input('Digite um valor: ')))
        resposta = input('Quer continuar? [S/N] ')
        if resposta in 'Nn':
            break
    print(f'Você digitou {len(valores)} elementos.')
    valores.sort(reverse=True)
    print(f'Os valores em ordem descrescente {valores}.')
    if 5 in valores:
        print('O valor 5 não faz parte da lista.')
    else:
        print('O valor 5 não foi encontrado.')

    
def extraindo_dados_2():

    numero = list()
    pares = list()
    impares = list()
    while True:
        numero.append(int(input('Digite um número: ')))
        resp = input('Quer continuar? [S/N] ')
        if resp in 'Nn':
            break
    for indice,valor in enumerate(numero):
        if valor % 2  == 0:
            pares.append(valor)
        if valor % 2 == 1:
            impares.append(valor)
    print(f'A lista completa é {numero}.')
    print(f'A lista de pares: {pares}.')
    print(f'A lista de pares: {impares}.')

def extraindo_dados_3():

    lista_1 = []
    lista_pares = []
    lista_impares = []
    r = 's'
    while r == 's':
        x = int(input('Digite um número: '))
        if x % 2 == 0 and x!=0:
            lista_pares.append(x)
        elif x % 2 == 0 and x!= 0:
            lista_impares.append(x)
        lista_1.append(x)
        r = input('Quer continuar? [S/N]').strip()
        while r not in 'SsNn':
            r=input('Digite S ou N: ')
    print(f'A lista com todos os valores é: {lista_1}'
          f'A lista com os valores pares:{lista_pares}'
          f'A lista com os valores impares:{lista_impares}')

def extraindo_dados_4():

    q = int(input('Quantidade de números a inserir: '))
    lista = sorted([int(input(f'Digite o número {i}:'))for i in range(1,q+1)])
    print(f'\nLista:{lista}'
          f'\nNúmeros impares:{[x for x in lista if x % 2 != 0]}'
          f'\nNúmeros pares:{[y for y in lista if y % 2 == 0]}')
    

    

    
                      
