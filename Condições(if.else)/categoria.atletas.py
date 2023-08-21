

#A Confederação Nacional de Natação precisa de um programa que leia
#o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
ano_atual = date.today().year
ano_nasc=int(input('Qual o ano de nascimento do atleta: '))
idade = ano_atual - ano_nasc
print(f'A idade do atleta é {idade} anos e...')
if idade <= 9:
    print('A categoria é MIRIM.')
elif idade <= 14: 
    print('A categoria é INFANTIL.')
elif idade <=19: 
    print('A categoria é JÚNIOR.')
elif idade > 19 and idade<= 25:
    print('A categoria é SÊNIOR. ')
elif idade>25:
    print('A categoria é MASTER. ')
    
