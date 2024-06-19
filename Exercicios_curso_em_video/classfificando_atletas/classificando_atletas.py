# Classificando Atletas: 
# Versão  1

from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
idade = atual - nasc
print(f'Sua idade é de {idade} anos(s).')
if idade <= 9:
    print('Categoria: MIRIM.')
elif idade > 9 and idade <=14:
    print('Categoria: Infantil.')
elif idade > 14 and idade <=19:
    print('Catgoria: Junior')
elif idade > 19 and idade <= 25:
    print('Categoria: Sênior.')
else:
    print('Categoria: Master.')
