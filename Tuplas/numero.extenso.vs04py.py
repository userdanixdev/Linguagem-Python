extensos= ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
            'dez','onze','doze','treze','quatorze','quinze','dezesseis',
           'dezessete','dezoito','dezenove','vinte')

while True:
    numero=int(input('Digite um número de 0 a 20: '))
    while numero < 0 or numero > 20:
        numero=int(input('Numero invalido. Digite o número correto:'))
    print(f'Voce digitou {extensos[numero]}.')
    pergunta=str(input('''
        Quer continuar? Sim para continuar ou digite qualquer letra:
                    ''')).strip().upper()
    if pergunta == 'S' or pergunta == 'SIM':
        continue
    else:
     break
print('Até mais. FIM.')
                   
