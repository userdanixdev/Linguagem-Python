'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.'''

#versão 02:

extensos= ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
            'dez','onze','doze','treze','quatorze','quinze','dezesseis',
           'dezessete','dezoito','dezenove','vinte')
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if numero >= 21:
        print('Tente novamente.')
    else:
        print(f'Você digitou o número {extensos[numero]}.')
        continuar = ''
        while continuar not in 'NnSs':
            continuar = input('Quer continuar [S/N]?').strip().upper()
        if continuar == 'N':
            break
