#Crie um programa que tenha uma função chamada voto() que vai receber 
#como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
#indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

#Versão 03:

import datetime
        
def voto(vt):
    if vt >= 65:
        print('O voto é opcional')
    if vt >= 18 and vt <= 65:
        print('O voto é obrigatório')
    if vt >= 16 and vt <= 18:
        print('O voto é opcional')
    if vt < 16:
        print('Não vota')
nasc = int(input('Ano de Nascimento:'))        
ano = datetime.date.today().year
idade = ano - nasc
print(f'Com {idade} anos:', end='')
voto(idade)

    