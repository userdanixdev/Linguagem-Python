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
    print(f'A lista com todos os valores é: {lista_1}\n'
          f'\nA lista com os valores pares:{lista_pares}\n'
          f'\nA lista com os valores impares:{lista_impares}')

def extraindo_dados_4():

    q = int(input('Quantidade de números a inserir: '))
    lista = sorted([int(input(f'Digite o número {i}:'))for i in range(1,q+1)])
    print(f'\nLista:{lista}'
          f'\nNúmeros impares:{[x for x in lista if x % 2 != 0]}'
          f'\nNúmeros pares:{[y for y in lista if y % 2 == 0]}')

def menu():

    menu= '''\n
        +++++ MENU +++++

        [1] -\tExtraindo Dados
        [2] -\tExtraindo Dados - Dividindo Lista
        [3] -\tExtraindo Dados - Dividindo Lista
        [4] -\tExtraindo Dados - Dividindo (List Compreenhension)
        [5] -\tExecutar Todos
        [6] -\tSair

        ===> '''

    return int(input(menu))

def main():

    while True:
        opcao = menu()
        if opcao == 1:
            extraindo_dados()
        if opcao == 2:
            extraindo_dados_2()
        if opcao == 3:
            extraindo_dados_3()
        if opcao == 4:
            extraindo_dados_4()
        if opcao == 5:
          extraindo_dados()
          extraindo_dados_2()
          extraindo_dados_3()
          extraindo_dados_4()
        if opcao == 6:
          sair()

def sair():
    import sys
    sys.exit()
        
    
main()
    

    
                      
