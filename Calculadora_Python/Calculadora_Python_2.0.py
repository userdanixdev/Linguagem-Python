# Calculadora:
from time import sleep
print(f'{"+"*50}\n{"Calculadora em Python":^49}\n{"+"*50}')
sleep(1)

def add(x,y):
    return x+y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

while True:
    print(f"\n{"Selecione o número da operação desejada":^49} \n")
    print('''
                 +++++++++++++++++++++++
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão
                 +++++++++++++++++++++++                

                '''      )

    sleep(1)
    escolha=input('Digite sua opção (1/2/3/4):')
    sleep(0.5)
    number_1 = int(input('Digite o primeiro número: '))
    sleep(0.3)
    number_2 = int(input('Digite o segundo número: '))
    sleep(1)
    print('Aguarde instantes enquanto estamos realizando o processamento...')
    sleep(1.5)
    if escolha == '1':
        print(number_1,'+',number_2,'=', add(number_1,number_2))
    elif escolha == '2':
        print(number_1,'-',number_2,'=', subtract(number_1,number_2))
    elif escolha == '3':
        print(number_1,'X',number_2,'=', multiply(number_1,number_2))
    elif escolha == '4':
        print(number_1,'/',number_2,'=', divide(number_1,number_2))
    else:
        print('Opção Inválida.')
    sleep(1)        
    resposta = input('Deseja continuar? [S/N]. ')
    while resposta not in 'SsNn':
        resposta=input('Resposta inválida. Somente [S/N].')
    if resposta in 'Nn':
        break
print('Até mais')    
            
        
         


