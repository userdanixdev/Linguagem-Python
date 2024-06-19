# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Alistamento Militar:
# Versão POO : As 2 versões estruturais estão aqui.

class AlistamentoMilitar:
    def __init__(self):
        self.nascimento = 0

    def alistamento_1(self):
        from datetime import date
        atual = date.today().year
        self.nascimento = int(input('Ano de nascimento: '))
        idade = atual - self.nascimento
        print(f'Quem nasceu em {self.nascimento} tem {idade} anos em {atual}.')
        if idade == 18:
            saldo = 18 - idade
            print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento.')
            ano = atual + saldo
            print('Seu alistamento será em {ano}.')
        elif idade > 18:
            saldo = idade - 18
            print(f'Você já deveria ter se alistado há {saldo} anos.')
            ano = atual - saldo
            print(f'Seu alistamento foi em {ano}.')

    def alistamento_2(self):
        from datetime import datetime
        import calendar
                  
        while True:
                try:
                    nascimento=input('Informe sua data de nascimento(dd/mm/aaaa): ')
                    dia,mes,ano = map(int,nascimento.split('/'))
                    if len(nascimento)==10 and nascimento[2] == '/' and nascimento[5] == '/':
                        break
                    else:
                        print('Formato incorreto. Insira o formato correto: dd/mm/aaaa.')
                except ValueError:
                    print('Entrada válida. Insira a ordem correta.')
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
                
        elif (dia-datetime.now().day)== 1 and datetime.now().month == mes:
                print(f'Seu alistamento será amanhã.\nPor favor, procure uma agência.')
                
        elif (dia -datetime.now().day) > 1 and datetime.now().month == mes:
                print(f'Seu alistamento será este mês. Faltam {dia-datetime.now().day} dias.')
                
        elif datetime.now().month == mes:
                print(f'Já passou da hora de alistar. Procure uma unidade imediatamente.\nPassaram {datetime.now().day-dia} dias.')
                
        elif datetime.now().year-ano == 18:
                print(f'Já passou da hora de alistar.\nProcure uma unidade imediatamente.\nPassaram {datetime.now().month-mes}meses.')

     

    def iniciar(self):
        while True:
            print('\nAlistamento militar\n')
            self.alistamento_1()
            print('\nAlistamento militar: Versão Data Completa\n')
            self.alistamento_2()
            while True:
                continuar = input('Deseja continuar? [1-SIM / 2-NÃO]: ')
                if continuar in ['1','2']:
                    break
                else:
                    print('Entrada inválida.')
            if continuar == '2':
                break
        print(f'Fim.')            
            
        
if __name__ =='__main__':
    alistamento=AlistamentoMilitar()
    alistamento.iniciar()
        
