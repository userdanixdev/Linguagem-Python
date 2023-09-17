'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.'''

#versão 02:

extensos= ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
            'dez','onze','doze','treze','quatorze','quinze','dezesseis',
           'dezessete','dezoito','dezenove','vinte')
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    while numero < 0 or numero > 20:
        numero = int(input('Número inválido. Digite um número entre 0 e 20, somente: '))
    print(f'Você digitou o número {extensos[numero]}!')
    pergunta = input('Vc quer continuar? [S/N]: ').strip().upper()[0]
    if pergunta == 'S' or pergunta =='SIM':
            continue
    else:
            break
print('Obrigada por usar nossa programa.')    
   
