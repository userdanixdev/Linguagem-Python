#Escreva um programa que leia um número N inteiro qualquer e
#mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.


from time import sleep
print('Sequência de Fibonacci.')
sleep(1)
n=int(input('Quantos termos você quer mostrar? '))
t1=0
t2=1
print(f'{t1} -> {t2}.')
cont=3 # Já temos os primeiros termos. Portanto o contador comecará no 3.
while cont <=n:
    t3=t1+t2
    print(f'-> {t3}.')
    t1=t2
    t2=t3
    cont = cont + 1
print('FIM')

Results:
Sequência de Fibonacci.
Quantos termos você quer mostrar? 10
0 -> 1.
-> 1.
-> 2.
-> 3.
-> 5.
-> 8.
-> 13.
-> 21.
-> 34.
FIM
=========================================================




