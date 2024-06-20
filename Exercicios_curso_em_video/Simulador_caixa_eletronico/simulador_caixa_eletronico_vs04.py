# Simulador Caixa eletrônico:
# Versão 04:

print('Simulador Caixa Eletrônico')
resto = 0
saldo = int(input('Informe o valor da retirada: R$ '))
print(f'\nPara o valor de R$ {saldo}, será entregue as seguintes cédulas: ')
while True:
    if saldo >= 50:
        resto = saldo % 50
        saldo //=50
        print(f'{saldo}x R$ 50,00')
    saldo =  resto
    if saldo >= 20:
        resto = saldo % 20
        saldo //= 20
        print(f'{saldo}x R$ 20,00')
    saldo = resto
    if saldo >= 10:
        resto = saldo % 10
        saldo //= 10
        print(f'{saldo}x R$ 10,00')
    saldo = resto
    if saldo >= 1:
        resto = saldo % 1
        saldo *= 1
        print(f'{saldo}x R$ 1,00')
    break
print('Obrigado por ser nosso cliente.')

        
