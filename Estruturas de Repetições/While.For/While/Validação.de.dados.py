'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo=input('Digite o sexo - M ou F: ').strip().upper()[0] #STRIP para formatar a string com somente a primeira letra. e upper para caso for 'f' virar 'F' e 'm' cirar 'M'.
while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
