# Somando valores:

n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
s = n1+n2
print(f' A soma entre {n1} e {n2} é igual a: {s}')
# Obs: Sem converter o tipo do dado, a variável será 'str', padrão do Python, assim o resultado será concatenado.

# Somando valores da forma correta:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
print(f' A soma entre {n1} e {n2} é igual a: {s}')
