# Maior e menor valor de uma lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Versão : POO

class Maior_Menor_Valor_Lista:
    
    def __init__(self):

        self.lista = []
        self.lista_2 = []

    def programa_1(self):

        maior = 0
        menor = 0
        for c in range(0,5):   # Irá percorrer até o 5
            self.lista.append(int(input(f'Digite um valor para a posição: {c+1}.')))  # Adiciona os valores do usuário a lista
            if c == 0:
                maior = menor = self.lista[c]
            else:
                if self.lista[c] > maior:
                    maior = self.lista[c]
                if self.lista[c] < menor:
                    menor = self.lista[c]
        print(f'\nVocê digitou os valores {self.lista}.\n')
        print(f'O maior valor foi: {maior} nas posições ',end='')
        for i,v in enumerate(self.lista):
            if v == maior:
                print(f' {i}..')
        print()
        print(f'O menor valor foi: {menor} nas posições ',end='')
        for i,v in enumerate(self.lista):
            if v ==  menor:
                print(f' {i}..' )
        print()                

    def iniciar(self):
        
        print('Programa 1')
        self.programa_1()
        print('Programa 2')
        self.programa_2()
        print('Programa 3 - Versão simplicada do programa 2')
        self.programa_3()
        print('Programa 4')
        self.programa_4()

    def programa_2(self):

        for c in range(0,5):
            numero = int(input(f'Digite um número para a posição {c+1}: '))
            self.lista_2.append(numero)
        numero_max = max(self.lista_2)
        numero_min = min(self.lista_2)
        print(f'Os valores digitados foram: {self.lista_2}.')
        print(f'O maior valor digitado foi: {max(self.lista_2)} e a sua posição é: {self.lista_2.index(numero_max)+1}')
        print(f'O menor valor digitado foi: {min(self.lista_2)} e a sua posição é: {self.lista_2.index(numero_min)+1}')

    def programa_3(self):

        valores = []  # Variável valores recebe uma lista vazia
        for c in range(0,5):
            numero = int(input(f'Digite um número para a posição {c}: '))
            valores.append(numero)
        print(f'Os valores digitados foram: {valores}.')
        print(f'O maior valor digitado foi: {max(valores)} e a sua posição é: {valores.index(max(valores))+1}')
        print(f'O menor valor digitado foi: {min(valores)} e a sua posição é: {valores.index(min(valores))+1}')

    def programa_4(self):

        a = [input(f'Digite um valor para a posição {i+1}: ')for i in range(0,5)]
        posmax = []
        posmin = []
        for pos,valor in enumerate(a):
            if valor == max(a):
                posmax.append(pos)
            elif valor == min(a):
                posmin.append(pos)
        print(f'O maior valor foi {max(a)} e está na posição {posmax}.')
        print(f'O menor valor foi {min(a)} e está na posição {posmin}.')

    def menu(self):

        opcoes = int(input('''

                Maior e menores valores dentro de uma lista

                [1] - Programa 1 
                [2] - Programa 2
                [3] - Programa 3
                [4] - Programa 4
                [5] - Executar tudo
                [6] - Sair
                
                '''))

        if opcoes == 1:
            self.programa_1()
            self.loop_repeticoes(self.programa_1)
        if opcoes == 2:
            self.programa_2()
            self.loop_repeticoes(self.programa_2)
        if opcoes == 3:
            self.programa_3()
            self.loop_repeticoes(self.programa_3)
        if opcoes == 4:
            self.programa_4()
            self.loop_repeticoes(self.programa_4)
        if opcoes == 5:
            self.iniciar()
        if opcoes == 6:
            self.sair()

    @staticmethod
    def sair():
        import os
        exit()

    def loop_repeticoes(self,programa):

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

    
        

        

        

if __name__=='__main__':
    
    lista=Maior_Menor_Valor_Lista()
    lista.menu()

        

