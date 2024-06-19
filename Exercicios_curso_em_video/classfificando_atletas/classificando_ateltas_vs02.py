# Classificando atletas:
# Versão 02:

while True:
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

    mirim = range(0,10)
    infantil = range(11,15)
    junior = range(16,20)
    senior = range(21,25)

    # Calculo da idade:
    hoje = date.today()
    idade = hoje.year - ano - ((hoje.month,hoje.day)<(mes,dia))


    if idade in mirim:
       print('Atleta Mirim')
    elif idade in infantil:
       print('Atleta Infantil')
    elif idade in junior:
       print('Atleta Junior')
    elif idade in senior:
       print('Atleta Sênior')
    else:
       print('Atleta Master')
    while True:
        continuar = input('Deseja continuar? [1-SIM / 2-NÃO].')
        if continuar in ['1','2']:
           break
        else:
            print('Entrada inválida. Digite 1 para continuar ou 2 para sair.;')
    if continuar == '2':
        break
print('Fim')

