# Lista Composta: Versão 03

pessoas_temp = []
pessoas = []
pesados = []
leves = []


while True:
    nome = input('Nome: ')
    while not nome.isalpha():
        print('Nome deve conter apenas letras.')
        nome = input('Nome: ')
    while True:
            try:
                peso = float(input('Peso: '))
                break
            except ValueError:
                print('Peso deve ser um número válido.')

    pessoas_temp.append(nome)
    pessoas_temp.append(peso)
    pessoas.append(pessoas_temp.copy())

    if peso <= 100:
        pesados.append(nome)
    elif peso <= 70:
        leves.append(nome)

    pessoas_temp.clear()

    resposta = input('Quer continuar? [S/N]').strip().upper()
    while resposta not in 'SN':
        print('Resposta inválida. Digite S para SIM ou N para NÂO.')
        resposta = input('Quer continuar? [S/N] ').strip().upper()
    if resposta == 'N':
        break
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'Pessoas acima de 100Kg: {pesados}')
print(f'Pessoas abaixo de 70Kg: {leves}')    

    
