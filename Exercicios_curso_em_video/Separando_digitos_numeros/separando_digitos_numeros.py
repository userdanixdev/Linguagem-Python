# Separando digitos de um número:

n = input('Informe um número de 0 a 9999: ')
print('unidade:',n[-1:])
print('dezena:',n[-2:-1])
print('centena',n[-3:-2])
print('milhar',n[-4:-3])
print()
print('Segunda forma:')
num = input('Digite um número entre 0 e 9999: ')
num = num[::-1]+'000'
print(f'Unidades:{num[0]}\nDezenas:{num[1]}\nCentenas:{num[2]}\nMilhar:{num[3]}.')
print()
print('Terceira forma:')
numero=int(input('Informe um numero: '))
print(f'Unidade {numero // 1 % 10}.')
print(f'Dezena {numero // 10 % 10}.')
print(f'Centena {numero // 100 % 10}.')
print(f'Milhar {numero // 1000 % 10}.')
print()
print('Quarta forma:')
number=input('Digite um número: ')
number_2=number.replace(number,'000'+number)
print(f'unidade:{number_2[-1]}')
print(f'dezena:{number_2[-2]}')
print(f'centena:{number_2[-3]}')
print(f'milhar:{number_2[-4]}')



