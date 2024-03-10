#Crie um programa que tenha uma função chamada voto() que vai receber 
#como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
#indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

#Versão 04:       # GOOD VERSION!!

from datetime import date
     
def voto(vt):
    if vt >= 65 or 16 <= vt < 18:
        print(f'Com {vt} anos o voto é opcional')
    elif vt <= 15:
        print('Não pode votar')
    if vt >= 16 and vt <= 18:
        print('O voto é opcional')
    else:
        print(f'Com {vt} anos o voto é obrigatório.')

voto(date.today().year - int(input('Digite ano de nascimento:')))

    