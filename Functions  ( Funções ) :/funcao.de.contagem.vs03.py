#Faça um programa que tenha uma função chamada contador(),
#que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

#Versão 03:

from time import sleep

def contador(inicio,fim,passo):
    from time import sleep
    print('+'*30)
    if passo < 0:  # Eliminar parâmetros negativos
       passo = passo *-1   # Inverte para positivo
    if passo == 0:   # Se digitar passo 0 o passo recebe 1 para não dar erro
        passo = 1  # Passo recebe 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.2)
    # Se decrescente:
    if inicio > fim:
        for x in range(inicio, fim-1,passo):
            print(x,end=' ')
            sleep(0.2)
        print('Fim')
    # Se crescente:
    else:
        for x in range(inicio,fim+1,passo):
            sleep(0.2)
            print(x,end=' ')
        print('FIM')

contador(1,10,1)
contador(10,0,2)
print('+'*30)
print('Agora é sua vez de personalizar a contagem: ')
contador(inicio=int(input('Inicio: ')),fim=int(input('Fim: ')),passo=int(input('Passo: ')))
    
      
