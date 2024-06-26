# Lista composta:
# Versão 2.1:  Validações de entrada de dados

pessoas = []

def input_nome():
    while True:
        nome = input('Nome: ')
        if nome.isalpha():
            return nome
        else:
            print('Somente letras são permitidas.')

def input_peso():
    while True:
        try:
            peso = float(input('Peso: '))
            return peso
        except ValueError:
            print('Somente valores numéricos são permitidos.')

def Lista_Composta():            

    while True:
        nome = input_nome()
        peso = input_peso()
        pessoas.append([nome,peso])
        while True:
            continuar = input('Quer continuar? [S/N]').strip().lower()[0]
            if continuar in ('s','n'):
                break
            else:
                print('Somente S para Sim e N para não.')
        if continuar == 'n':
            break
           
    print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
    print()
    maior_peso=max([p for n,p in pessoas])
    print(f'O maior peso foi de {maior_peso:.1f}KG.',end='')
    print(f'Peso de{[n for n,p in pessoas if p == maior_peso]}')
    print()
    menor_peso=min([p for n,p in pessoas])
    print(f'O menor peso foi de {menor_peso:.1f}KG.',end='')
    print(f'Peso de {[n for n,p in pessoas if p == menor_peso]}')             
                 

Lista_Composta()    
