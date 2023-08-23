#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

 for n in range(0,51):
    print('.',end='')
     if n % 2==0:
       print(n, end='')

# redução (modo reduzido)
for n in range(0,51,2):
    print(n,end='')
print('Acabou')

    
    




