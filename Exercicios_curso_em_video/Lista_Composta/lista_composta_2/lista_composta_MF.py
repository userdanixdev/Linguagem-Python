# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Lista: Pares e Ímpares
# Modelo Funcional:

def input_valor(c):
    while True:
            try:
                valor = int(input(f'Digite o {c}º valor: '))
                return valor
            except ValueError:
                print('Somente valores numéricos são permitidos.')

def lista_pares_impares():

    lista = [[],[]]
    valor = 0
    for c in range(1,8):
        valor = input_valor(c)
        if valor % 2 == 0:
            lista[0].append(valor)
        else:
            lista[1].append(valor)
    return lista
                

def lista_pares_impares_exibicao(lista):

    print(f'Os valores pares são: {sorted(lista[0])}')
    print(f'Os valores impares são: {sorted(lista[1])}')

def lista_pares_impares_2():

    lista = []
    lista_par = []
    lista_impar = []

    for c in range(1,8):
        n = input_valor(c)
        if n % 2 == 0:
            lista_par.append(n)
        elif n % 2 == 1:
            lista_impar.append(n)

    lista.append(lista_par)
    lista.append(lista_impar)

    return lista

def lista_pares_impares_exibicao_2(lista):

    print(f'Os valores pares digitados foram: {sorted(lista[0])}\nOs ímpares :{sorted(lista[1])}')

def lista_pares_impares_3():

    lista_composta = [[],[]]
    for c in range(7):
        n = input_valor(c+1)
        lista_composta[0].append(n) if n % 2 == 0 else lista_composta[1].append(n)

    return lista_composta

def lista_pares_impares_3_exibicao(lista_composta):

    print('-'*22,f'\nNúmeros pares:{sorted(lista_composta[0])}\nNúmeros ímpares:{sorted(lista_composta[1])}')
    
def menu():
    while True:
            try:
                menu='''
            ++++++++++++ MENU ++++++++++++++
            [1]-\tLista Composta - Impar/Par
            [2]-\tLista Composta - Impar/Par
            [3]-\tLista Composta - Impar/Par
            [4]-\tSair

            \nEscolha:  '''
                opcao = int(input(menu))
                if opcao in [1,2,3]:
                    return opcao
                else:
                    print('Opção Inválida. Escolha um número entre 1 a 5.')
            except ValueError:
                print('Opção inválida. Insira somente números inteiros.')

def sair():
    import sys
    exit()

def main():
    while True:
        try:
            opcoes = menu()
            if opcoes == 1:
                print('Programa 1 ')
                lista = lista_pares_impares()
                lista_pares_impares_exibicao(lista)
            elif opcoes == 2:
                print('Programa 2')
                lista = lista_pares_impares()
                lista_pares_impares_exibicao_2(lista)
            elif opcoes == 3:
                print('Programa 3')
                lista_composta= lista_pares_impares_3()
                lista_pares_impares_3_exibicao(lista_composta)
            elif opcoes == 4:                
                sair()
        except ValueError:
            print('Somente números inteiros permitidos.')

main()            
    

    
