'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('zero','um','dois','três','quatro','cinco',
        'seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze',
        'dezesseis','dezessete','dezoito','dezenove',
        'vinte')
while True:  # pra ficar em loop infinito
    num=int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.')
# Verificação dos números dentro do limite imposto pelo enunciado acima.
print(f'Você digitou o número {cont[num]}.')

