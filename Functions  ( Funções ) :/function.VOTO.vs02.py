#Crie um programa que tenha uma função chamada voto() que vai receber 
#como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
#indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto(x=0):
    from datetime import date
    data_atual = date.today()
    resp = 'none'
    if x == 0:
        resp = 'Idade Inválida'
    elif data_atual.year-x < 16:
        resp = f'Com {data_atual.year-x} anos: NÃO VOTA'
    elif data_atual.year-x >= 18:
        resp = f'Com {data_atual.year-x} anos: VOTO OBRIGATÓRIO'
    elif data_atual.year-x > 65 or 16 <= data_atual.year-x < 18:
        resp = f'Com {data_atual.year-x} anos: VOTO OPCIONAL'
    return resp
print('+'*49)
ano_nasc=int(input('Em que ano você nasceu?'))         
print(voto(ano_nasc))
