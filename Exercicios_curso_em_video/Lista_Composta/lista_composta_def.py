# Lista composta: Versão funcional
# Tratamento de erros, funções adicionais para a função principal

def input_numero():

    while True:
                nome = input('Digite o nome: ')
                if nome.isalpha():
                    return nome
                else:
                    print('Somente strings.')

def input_numero_2():

    while True:
            try:
                return float(input('Digite o peso: '))
            except ValueError:
                print('Somente números float.')

def lista_composta():

    lista_temporaria = []
    lista_principal = []
    maior_peso = 0
    menor_peso = 0

    while True:
        lista_temporaria.append(input_numero())
        lista_temporaria.append(input_numero_2())
        if len(lista_principal) == 0:
            maior_peso = menor_peso = lista_temporaria[1]
        else:
            if lista_temporaria[1] > maior_peso:
                maior_peso = lista_temporaria[1]
            if lista_temporaria[1] < menor_peso:
                menor_peso = lista_temporaria[1]
        # Gera uma cópia da lista temporaria na lista principal
        lista_principal.append(lista_temporaria[:])
        lista_temporaria.clear()  # A lista temporaria está salva dentro da principal
        while True:
                    resposta = input('Quer continuar? [S/N] ')
                    if resposta in 'Nn':
                        break
                    elif resposta in 'Ss':
                        break
                    else:
                         print('Somente S para Continuar ou N de não para encerrar.')
        if resposta in 'Nn':
            break
    print(f'\nOs dados foram:{lista_principal}.')
    print(f'Ao todo você cadastrou {len(lista_principal)} pessoas.')
    print(f'O maior peso foi de {maior_peso}KG.')
    print(f'O menor peso foi de {menor_peso}KG.')
    print('O maior peso foi de: ',end='')
    for p in lista_principal:
        if p[1] == maior_peso:
            print(f'[{p[0]}] ',end='')
    print()
    print(f'O menor peso foi de {menor_peso}KG. Peso de ',end='')
    for p in lista_principal:
        if p[1] == menor_peso:
            print(f'[{p[0]}].',end='')
    print()        


lista_composta()
