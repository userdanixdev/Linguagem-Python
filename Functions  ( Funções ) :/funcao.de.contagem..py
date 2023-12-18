#Faça um programa que tenha uma função chamada contador(),
#que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep
def contador(i,f,p):
    if p < 0:   # Se menor que 0 teremos que transformar para positivo.
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
# Contagem abaixo se o início for MENOR que o fim: Acrescentar condição para ser MAIOR QUE O FIM.
    if i < f:
        cont=i
        while cosnt <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont += p
        print('\nFim')
    else:    # Maior que o fim ##
         cont = i
         while cont >= f:
                print(f'{cont}', end=' ', flush=True)
                sleep(0.2)
                cont -= p
         print('\nFIM')            
        


contador(1,10,1)
contador(0,100,10)
contador(10,0,2)
print('+'*30)
print( 'Agora é sua vez de personalizar a contagem: ')
ini=int(input('Início: '))
fim=int(input('FIM: '))
passo=int(input('Passo: '))
contador(ini,fim,passo)

