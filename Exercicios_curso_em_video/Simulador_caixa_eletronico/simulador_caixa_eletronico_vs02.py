# Simulador Caixa eletrônico:
# Versão 02:

print('Simulador Caixa Eletrônico')
total=int(input('Digite um valor: '))
for i in (50,20,10,1):
    total_cedulas = 0
    while total >= i:
        total -= i
        total_cedulas += 1
    if total_cedulas !=0:
        print(f'Total de cédulas de R${i}:{total_cedulas}.')
