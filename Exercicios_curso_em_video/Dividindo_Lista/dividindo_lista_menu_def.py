def extraindo_dados():

    valores = []
    while True:
               try:
                   valores.append(int(input('Digite um valor: ')))
                   while True:
                         resposta = input('Quer continuar? [S/N] ')
                         if resposta in 'Nn':
                             break
                         elif resposta in 'Ss':
                             break
                         else:
                             print('Somente S para Sim e N para não.')
                   if resposta in 'Nn':
                       break
               except ValueError:
                    print('Somente valores inteiros.')
            
    print(f'\nVocê digitou {len(valores)} elementos.')
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
            try:
                numero.append(int(input('Digite um número: ')))
                while True:
                    resp = input('Quer continuar? [S/N] ')
                    if resp in 'Nn':
                        break
                    elif resp in 'Ss':
                        break
                    else:
                        print('Somente S para SIM e N para NÃO.')
                if resp in 'Nn':
                    break
            except ValueError:
                print('Somente valores inteiros.')
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
    
    while True:
        try:
            x = int(input('Digite um número: '))
            lista_1.append(x)
            if x % 2 == 0 and x!=0:
                lista_pares.append(x)
            elif x % 2 != 0:
                lista_impares.append(x)
        except ValueError:
            print('Somente números inteiros.')
            continue
            while True:
                r = input ('Quer continuar? [S/N]').strip()
                if r in 'Nn':
                    break
                elif r in 'Ss':
                    break
                else:
                    print('Somente S para SIM e N para não.')
            if r in 'Nn':
                break
    print(f'A lista com todos os valores é: {lista_1}\n'
          f'\nA lista com os valores pares:{lista_pares}\n'
          f'\nA lista com os valores impares:{lista_impares}')

def extraindo_dados_4():
    while True:
        try:            
            q = int(input('Quantidade de números a inserir: '))
            break  # sair do loop se a entrada for válida
        except ValueError:
            print('Somente números inteiros.')
    def input_numero (i):
        while True:
            try:
                return int(input(f'Digite um número {i}: '))
            except ValueError:
                print('Somente números inteiros.')

    lista = sorted([input_umero(i) for i in range(1,q+1)])
    #lista = sorted([int(input(f'Digite o número {i}:'))for i in range(1,q+1)])
    print(f'\nLista:{lista}'
          f'\nNúmeros impares:{[x for x in lista if x % 2 != 0]}'
          f'\nNúmeros pares:{[y for y in lista if y % 2 == 0]}')

def menu():

    while True:
            try:
                menu= '''\n
        +++++ MENU +++++

        [1] -\tExtraindo Dados
        [2] -\tExtraindo Dados - Dividindo Lista
        [3] -\tExtraindo Dados - Dividindo Lista
        [4] -\tExtraindo Dados - Dividindo (List Compreenhension)
        [5] -\tExecutar Todos
        [6] -\tSair

        ===> '''
                opcao = int(input(menu))
                return opcao
            except ValueError:
                print('Opção inválida. Insira somente números.')

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
    

    
                      
