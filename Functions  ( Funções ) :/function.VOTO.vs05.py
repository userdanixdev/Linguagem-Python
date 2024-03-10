#Crie um programa que tenha uma função chamada voto() que vai receber 
#como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
#indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

#Versão 05:      
    
#from datetime import date    
def voto(ano):    
    #atual = date.today().year
    idade = 2024 - ano
    if 16 <= idade < 18 or idade >70:
        return f'Com {idade} anos o voto é opcional'
    elif idade < 16:
        return f'Com {idade} anos. O voto é negado'
    else:
        return f'Com {idade} anos. O voto é obrigatório'
    
anoNasc = int(input('Em que ano você nasceu?'))    
print(voto(anoNasc))
    

