# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# Versão 02:

a = input('escreva algo:')

print(
    f'''
    O tipo primitivo é {type(a)}
    É número:       {a.isnumeric()}
    É alfabético:   {a.isalpha()}
    É alfanumérico: {a.isalnum()}
    É maiúscula:    {a.isupper()}
    É minúscula:    {a.islower()}
    É capitalizada: {a.istitle()}
    ''')
