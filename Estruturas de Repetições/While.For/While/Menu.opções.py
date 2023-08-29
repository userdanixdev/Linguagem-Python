'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
======================================'''

from time import sleep
num01=int(input('Primeiro valor: '))
num02=int(input('Segundo valor: '))
opcao=0
while opcao !=5:
        print('''
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior número
        [ 4 ] Novos números
        [ 5 ] Sair do programa''')
        opcao=int(input('Qual a sua opção? '))
        if opcao ==1:
            soma = num01 + num02
            print(f'A soma de {num01} + {num02} é : {soma}.')
        elif opcao==2:
            produto = num01*num02
            print(f'O resultado de {num01} X {num02} é: {produto}.')
        elif opcao==3:
                if num01>num02:
                    maior = num01
                else:
                    maior = num02
                    print(f'Entre {num01} e {num02} o maior número é:{maior}.')
        elif opcao==4:
             print('Informe os números novamente: ')
             num01=int(input('Informe então o primeiro valor: '))
             num02=int(input('Informe o segundo valor: '))
        elif opcao==5:
             sleep(2)
             print('Finalizando...')
             sleep(2)
        else:
             print('Opção inválida. Tente de novo')
             sleep(2)
print('Fim do programa. Até mais!')             




