# Lista composta: Versão 03

while True:
    pessoas_temp.append(str(input('Nome: ')))
    pessoas_temp.append(float(input('Peso: ')))
    pessoas.append(pessoas_temp.copy())
    if pessoas_temp[1] >= 100:
        pesados.append(pessoas[0])
    elif pessoas_temp[1] <= 70:
        leves.append(pessoas[0])
    pessoas_temp.clear()
    resposta=str(input('Quer continuar?[S/N]')).upper()
    if resposta in 'N':
        break
print(f'Quantidade de pessoas cadastradas: [{len(pessoas_temp)}]')
print(f'Pessoas acima de 100Kg:{pesados}.')
print(f'Pessoas abaixo de 70 Kg: {leves}.')
