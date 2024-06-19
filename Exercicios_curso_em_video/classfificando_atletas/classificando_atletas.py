# Classificando futuros atletas:

from datetime import date
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
idade = date.today().year - ano
if mes > 12 or dia > 31:
        print('Data incorreta.')
else:
        if date.today().month <= mes:
            if date.today().day < dia:
                idade = idade - 1
        if idade < 9:
            print('Atleta Mirim')
        if idade < 14:
            print('Atleta Infantil')
        if idade < 19:
            print('Atleta Junior')
        elif idade < 20:
            print('Atleta Sênior')
        else:
            print('Atleta Master')
