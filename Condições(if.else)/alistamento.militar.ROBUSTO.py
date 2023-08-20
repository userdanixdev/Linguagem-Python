#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from time import sleep
from datetime import date
while True:
    sexo=int(input('''
               ----| ALISTAMENTO MILITAR |----
                    [ 1 ] para FEMININO
                    [ 2 ] para MASCULINO
                    Escolha uma opção:
                    '''))
    if sexo in [1,2]:
        break
    print('''Opção inválida.
         Por favor, escolha 1 para FEMININO
         ou 2 para MASCULINO''')
ano_atual = date.today().year
nasc= int(input('Ano de nascimento: '))
print('Analisando dados...')
sleep(2)
idade = ano_atual - nasc
if sexo == 1:
    print(f'Quem nasceu {nasc} tem {idade} anos em {ano_atual}. ')
    if idade==18:
        print('Você está na idade de se alistar, mas não é obrigatório.')
                  
    elif idade>18:
        saldo = idade - 18
        ano=ano_atual - saldo
        print(f'''
Você já deveria ter se alistado há {saldo} anos.
Seu alistamento foi no ano de {ano}...''')
    elif idade<18:
        saldo = 18 - idade
        ano = ano_atual + saldo
        print(f'''
                Você não tem idade para se alistar...
                Ainda faltam {saldo} anos.
                Mas lembre-se que você não é obrigada a se alistar''')
        
#print(f' Quem nasceu {nasc} tem {idade}anos em {ano_atual}. ')
if sexo ==2:
    print(f' Quem nasceu {nasc} tem {idade}anos em {ano_atual}. ')
    if idade == 18:
        print('Voçe deve se alistar.')
    elif idade<18:
        saldo = 18 - idade
        ano = ano_atual + saldo
        print(f'''
            Você ainda não tem idade para se alistar...
            Ainda faltam {saldo} anos.
                ''')
    elif idade>18:
        saldo = idade - 18
        ano=ano_atual - saldo
        print(f'''
                Você já deveria ter se alistado há {saldo} anos.
                Seu alistamento foi no ano de {ano}. ''')
