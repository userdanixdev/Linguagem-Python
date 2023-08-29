#Lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

from time import sleep
print('Bem vindo a Progressão Aritmética em Python!')
sleep(2)
print('Digite o primeiro termo para iniciar a progressão aritmética.')
sleep(1)
num=int(input('Digite o termo: '))
print('Para proseguir com a progressão é necessário informar o razão.')
sleep(0.5)
razao=int(input('Digite a razão da progressão: '))
sleep(0.5)
print('Processando as informações...')
sleep(1)
termos=10
acumulador=0
contador=1
while termos !=0:
    acumulador = acumulador + termos
    while contador <=acumulador:
        print(f"{num} ->",end='')
        num = num + razao
        contador = contador + 1
        sleep(1)
    print('PAUSA')
    sleep(1)
    termos= int(input('Quantos termos vc quer mostrar a mais? '))
print(f'Progressão finalizada com {acumulador} termos exibidos.')


        

