# somando valores versão 02:

while True:
    num_1 = input('Digite um valor: ')
    num_2 = input('Digite outro valor: ')
    if not (num_1.isnumeric() and num_2.isnumeric()):
        print('Somente números inteiros.')
        continue
    num_1=int(num_1)
    num_2=int(num_2)
    soma = num_1 + num_2
    print(f'A soma entre o número:{num_1} + o número:{num_2} é:{soma}.')
    break
