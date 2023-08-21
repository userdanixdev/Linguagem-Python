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

mirim = range(0, 10)
infantil = range(10, 15)
junior = range(15, 20)
senior = 20

#CONDIÇÕES
if idade in mirim:
    print(f'MIRIM. O aluno tem {idade} anos, então se encaixa nessa categoria.')
elif idade in infantil:
    print(f'INFANTIL. O aluno tem {idade} anos, então se encaixa nessa categoria.')
elif idade in junior:
    print(f'JUNIOR. O aluno tem {idade} anos, então se encaixa nessa categoria.')
elif idade == senior:
    print(f'SENIOR. O aluno tem {idade} anos, então se encaixa nessa categoria.')
else:
    print(f'MASTER. O aluno tem {idade} anos, então se encaixa nessa categoria.')

