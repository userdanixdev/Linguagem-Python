# Simulador Caixa eletrônico:
# Versão 03:

print('Simulador Caixa Eletrônico')
ced_50 = 0
ced_20 = 0
ced_10 = 0
ced_1  = 0
saque  = 0
pedido=int(input('Que valor você quer sacar? R$ '))
while pedido != saque:
    if (pedido - saque)>= 50:
        ced_50 += 1
        saque += 50
    elif 50 > (pedido-saque) >= 20:
        ced_20 += 1
        saque += 20
    elif 20 >(pedido-saque)>=10:
        ced_10 += 1
        saque += 10
    else:
        ced_1 += 1
        saque += 1
print(f'''
        Seu saque foi de R$ {saque},00 contendo {(ced_50+ced_20+ced_10+ced_1)} notas sendo:

        R$ 50,00 x {ced_50}
        R$ 20,00 x {ced_20}
        R$ 10,00 x {ced_10}
        R$ 1,00  x  {ced_1}
        ''')
print('Volte sempre')
    

        
