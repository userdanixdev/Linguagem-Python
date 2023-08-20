#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year
nasc= int(input('Ano de nascimento: '))
idade = ano_atual - nasc
print(f' Quem nasceu {nasc} tem {idade}anos em {ano_atual}. ')
if idade == 18:
    print('Voçe deve se alistar.')
elif idade<18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print(f'''
            Você ainda não tem idade para se alistar...
            Ainda faltam {saldo} anos.
            Seu alistamento foi {saldo} anos    ''')
elif idade>18:
    saldo = idade - 18
    ano=ano_atual - saldo
    print(f'''
Você já deveria ter se alistado há {saldo} anos.
    Seu alistamento foi no ano de {ano}. ''')
