# Simulador Caixa eletrônico:
# Versão 05:

print('Simulador Caixa Eletrônico: Versão 05')
valor = int(input('Insira o valor que deseja sacar: R$ '))
while True:
    if valor >= 50:
        print(f'R$50,00: {valor//50} notas(s)')
        valor = valor - 50*(valor//50)
    elif valor >= 20:
        print(f'R$20,00: {valor//20} notas(s)')
        valor = valor - 20*(valor//20)
    elif valor >= 10:
        print(f'R$10,00: {valor//10} notas(s)')
        valor = valor - 10*(valor//10)
    elif valor >= 5:
        print(f'R$5,00: {valor//5} nota(s)')
        valor = valor - 5*(valor//5)
    elif valor >= 1:
        print(f'R$1,00: {valor} notas(s)')
        valor = valor - valor
        break
