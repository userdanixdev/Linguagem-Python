# Alistamento Militar:
# Versão 2.1 : Com validação na data de nascimento.

from datetime import datetime
import calendar

print('Alistamento Militar')
while True:
    try:
        nascimento = input('Informe sua data de nascimento(dd/mm/aaaa):')
        dia,mes,ano = map(int,nascimento.split('/'))
        if len(nascimento) == 10 and nascimento[2] == '/' and nascimento[5] == '/':
          break
        else:
            print('Formato incorreto. Insira o formato correto: dd/mm/aaa.')
    except ValueError:
        print('Entrada válida. Insira a ordem correta.')
#dia=int(nascimento[0:2])
#mes=int(nascimento[3:5])
#ano=int(nascimento[6:10])

if (datetime.now().year-ano)>18:
    print(f'Já passou da hora de se alistar!\nProcure uma unidade imediatamente.\nPassaram-se {(datetime.now().year-ano)-18} anos.')
    
elif (datetime.now().year-ano)<18:
    print(f'Ficamos contente com sua disposição. Mas você não precisa se alistar este ano.')
    
elif (mes-datetime.now().month)>1 and dia > datetime.now().day:
    print(f'Seu alistamento será este ano. Faltam {(mes-datetime.now().month)-1} meses e {dia-datetime.now().day} dias.'if (dia-datetime.now().day!=0)else '')
    
elif (mes-datetime.now().month) == 1 and dia >= datetime.now().day:
    print(f'Seu alistamento será este ano.\nFalta 1 mês e {dia-datetime.now().day}dias'if(dia-datetime.now().day !=0)else'')
    
elif (mes-datetime.now().month) == 1 and dia <= datetime.now().day:
    print(f'Seu alistamento será no próximo mês. Faltam {(calendar.monthrange(ano,(datetime.now().month)))[1]-datetime.now().day+dia} dias')
    
elif(datetime.now().day==dia):
    print(f'Seu alistamento vence hoje.\nCorra para uma agência.')
    
elif (dia-datetime.now().day)== 1 and datetime.now().month ==mes:
    print(f'Seu alistamento será amanhã.\nPor favor, procure uma agência.')
    
elif (dia -datetime.now().day) > 1 and datetime.now().month == mes:
    print(f'Seu alistamento será este mês. Faltam {dia-datetime.now().day} dias.')
    
elif datetime.now().month == mes:
    print(f'Já passou da hora de alistar. Procure uma unidade imediatamente.\nPassaram {datetime.now().day-dia} dias.')
    
elif datetime.now().year-ano == 18:
    print(f'Já passou da hora de alistar.\nProcure uma unidade imediatamente.\nPassaram {datetime.now().month-mes}meses.')

    
    

