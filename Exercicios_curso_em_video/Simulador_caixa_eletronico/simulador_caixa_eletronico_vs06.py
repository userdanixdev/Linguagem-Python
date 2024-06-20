# Simulador Caixa eletrônico:
# Versão 06:

print('Simulador Caixa Eletrônico: Versão 06')
valor = int(input('Insira o valor que deseja sacar: R$ '))
notas = [100,50,20,10,1]
for i in range(len(notas)):
    n = int(valor/notas[i])
    if n >= 1:
        print(f'Você receberá {n} notas de R$ {notas[i]:.2f}')
        valor = valor-(n*notas[i])
