# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Versão : POO

class Maior_Menor_Valores:
    def __init__(self):

        self.numeros = 0

    def programa_1(self):

        from random import randint
        self.numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
        print('Os valores sorteados foram: ')
        for n in self.numeros:
            print(f'{n}',end='')
        print(f'\nO maior valor sorteado foi {max(self.numeros)}.')
        print(f'O menor valor sorteado foi {min(self.numeros)}.')

    def programa_2(self):

        from random import randint

        a=tuple(randint(1,10) for i in range(5))
        print()
        print(a)
        print(f'O maior valor da tupla: {max(a)}\ne o menor: {min(a)}.')
        print('Com alcance maior..')
        a = tuple(randint(1,10)for i in range(1,101))
        print(a)
        print('Escolhendo números aleatórios de 1 a 100 com alcance de 1 a 10...')
        a = tuple(randint(1,100) for i in range(1,10))
        print(a)
        print(f'O valor máximo adquirido: {max(a)}\ne o valor mínimo: {min(a)}.')
        print()

    def programa_3(self):

        import random
        from random import randint

        n = tuple(randint(1,10) for i in range(5))
        print(f'Os números sorteados foram: {n}.')
        contador = 0
        maior = 0
        menor = 5
        while True:
            for r in range(0,5):
                if maior <= n[r]:
                    maior = n[r]
                if menor >= n[r]:
                    menor = n[r]
            contador += 1
            if contador == 5:
                break
        print(f'O maior é {maior} e menor é {menor}.')

    def programa_4(self):

        from random import sample

        a=tuple(sample(range(10),5))
        print(f'Os números sorteados foram: {a}\nO maior valor é {max(a)} e o menor é: {min(a)}.')


    def iniciar(self):
            while True:
                try:
                    print('Programa 1')
                    self.programa_1()
                    print('Programa 2')
                    self.programa_2()
                    print('Programa 3')
                    self.programa_3()
                    print('Programa 4')
                    self.programa_4()

                    continuar = int(input('''

                Repetir as operações ou voltar ao menu principal?

                        [1] - Repetir
                        [2] - Menu Principal
                        '''))
                    if continuar == 1:
                        continue
                    elif continuar == 2:
                        self.menu()
                    else:
                        print('Entrada inválida. Somente números 1 ou 2.')
                
                except ValueError:
                    print('Entrada inválida. Somente números de 1 a 2.')
                    
    
    def menu(self):

        opcoes = int(input('''
            Maior e Menor valor de uma tupla de números aleatórios:

            [1] - Programa 1
            [2] - Programa 2
            [3] - Programa 3
            [4] - Programa 4
            [5] - Executar todos
            [6] - Sair

            '''))

        if opcoes == 1:
            self.programa_1()
            self.repetir_operacoes(self.programa_1)
        if opcoes == 2:
            self.programa_2()
            self.repetir_operacoes(self.programa_2)
        if opcoes == 3:
            self.programa_3()
            self.repetir_operacoes(self.programa_3)
        if opcoes == 4:
            self.programa_4()
            self.repetir_operacoes(self.programa_4)
        if opcoes == 5:
            self.iniciar()
        if opcoes == 6:
            self.sair()

    @staticmethod
    def sair():
        import os
        exit()

    
    def repetir_operacoes_1(self):

        while True:
                try:
                    continuar = int(input('''

                            Repetir a operação ou sair?
                    [1] - Repetir                    
                    [2] - Sair
                    '''))
                    
                    if continuar == 1:
                        self.programa_1()
                    elif continuar == 2:
                        self.menu()
                        break
                    else:
                        print('Opção inválida. Somente 1 para repetir ou 2 para sair.')
                except ValueError:
                    print('Entrada inválida. Por favor, somente os números (1 e 2).')

    def repetir_operacoes_2(self):

        while True:
                try:
                    continuar = int(input('''

                            Repetir a operação ou sair?
                    [1] - Repetir                    
                    [2] - Sair
                    '''))
                    
                    if continuar == 1:
                        self.programa_2()
                    elif continuar == 2:
                        self.menu()
                        break
                    else:
                        print('Opção inválida. Somente 1 para repetir ou 2 para sair.')
                except ValueError:
                    print('Entrada inválida. Por favor, somente os números (1 e 2).')

    def repetir_operacoes_3(self):

        while True:
                try:
                    continuar = int(input('''

                            Repetir a operação ou sair?
                    [1] - Repetir                    
                    [2] - Sair
                    '''))
                    
                    if continuar == 1:
                        self.programa_3()
                    elif continuar == 2:
                        self.menu()
                        break
                    else:
                        print('Opção inválida. Somente 1 para repetir ou 2 para sair.')
                except ValueError:
                    print('Entrada inválida. Por favor, somente os números (1 e 2).')

    def repetir_operacoes_4(self):

        while True:
                try:
                    continuar = int(input('''

                            Repetir a operação ou sair?
                    [1] - Repetir                    
                    [2] - Sair
                    '''))
                    
                    if continuar == 1:
                        self.programa_4()
                    elif continuar == 2:
                        self.menu()
                        break
                    else:
                        print('Opção inválida. Somente 1 para repetir ou 2 para sair.')
                except ValueError:
                    print('Entrada inválida. Por favor, somente os números (1 e 2).')                    
            

    def repetir_operacoes(self,programa):

        while True:
                try:
                    continuar = int(input('''

                            Repetir a operação ou sair?
                    [1] - Repetir                    
                    [2] - Sair
                    '''))
                    
                    if continuar == 1:
                         programa()
                    elif continuar == 2:
                        self.menu()
                        break
                    else:
                        print('Opção inválida. Somente 1 para repetir ou 2 para sair.')
                except ValueError:
                    print('Entrada inválida. Por favor, somente os números (1 e 2).')                    
            
        
            
                    
            

if __name__ == '__main__':
    tuplas=Maior_Menor_Valores()
    tuplas.menu()
        
