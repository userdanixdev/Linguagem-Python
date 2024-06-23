# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Lista ordenada: Sem uso do sort
# Versão POO: Todas as versões juntas, Versão 05 incrementada dentro da versão POO. não encontra ela separada.

class Adicionando_Valores_Lista:

    def __init__(self):

      self.lista = []
      self.lista_2 = list()
      self.lista_3= []
      self.list = []
      self.list_1 = []
      self.list_2 = []
      self.list_3 = []
      
    def programa_1(self):

      for c in range(0,5):
            n = int(input('Digite um valor: '))
            if c == 0:  # Primeiro valor
                self.lista.append(n)  # adicionado o primeiro
                print('Adicionado o primeiro valor.')
            elif n > self.lista[len(self.lista)-1]: # Se 'n' for maior que o últio valor,
                self.lista.append(n) # Se 'n' for maior que o último valor, adicionado no final da lista
                print('Adicionado ao final da lista.')
            else:
                posicao = 0
                while posicao < len(self.lista):     # Enquanto posicao for menor que o comprimento da lista
                    if n <= self.lista[posicao]:     # Se 'n' for menor ou igual a posição da lista
                        self.lista.insert(posicao,n) #
                        print(f'Adicionado na posição {posicao} da lista...')
                        break
                    posicao += 1
      print(f'{self.lista}.')


    def iniciar(self):

      print('- Programa 1 - Sem uso do sort')
      self.programa_1()
      print('- Programa 2 - Range e enumerate')
      self.programa_2()
      print('- Programa 3 - While')             
      self.programa_3()
      print('- Programa 4 - Intuitivo -             ')
      self.programa_4()
      print('- Programa 5 -   ')          
      self.programa_5()
      print('-Programa 06 - Enumerate')
      self.programa_6()
      print('-Programa 07 - Dois laços for ')
      self.programa_7()

    def programa_2(self):

        for c in range(0,5):  # Pra fazer um loop 5 vezes
            n = int(input('Digite um número: '))    # Digite o valor por 5 vezes
            if c == 0 or n > self.lista_2[-1]: # Primeiro valor, se for igual a 0 ou maior que o último
                self.lista_2.append(n)
            else:
                for posicao,x in enumerate(self.lista_2):
                    if n <= x:  # X equivale ao valor e não a posicao, se o o valor for menor ou igual 'x'
                        self.lista_2.insert(posicao,n)
                        break
        print(self.lista_2)

    def programa_3(self):

        for numero in range(5):
            numero = int(input('Digite um número: '))
            c = 0
            # enquanto contador 'c' menor que o comprimento da lista e o numero digitado menor que a lista do contador
            while c < len(self.lista_3) and numero > self.lista_3[c]:  
                c += 1 # c recebe mais sempre que for
            self.lista_3.insert(c,numero)   # sendo assim, insert
            print(f'Item adicionado',f'na posição {c+1}'if c<len(self.lista_3)-1 else 'no final','da lista')
        print(f'\nLista ordenada:{self.lista_3}')

    def programa_4(self):

        for c in range(1,6):
            n = int(input(f'Digite o {c}º número: '))
            if c == 1 or n >= self.list[-1]:   # se n for maior ou igual ao maior número, adiciona a lista em 'n'
                self.list.append(n)
            elif n <= self.list[0]:  # Se 'n' for menor ou igual ao primeiro da lista, adiciona na lista com insert.
                self.list.insert[0,n]
            elif self.list[0] <= n <= self.list[1]: # Se o primeiro da lista for menor que 'n' e o 'n' for menor que o segundo da lista
                self.list.insert[1,n]
            elif self.list[1] <= n <= self.list[2]:  # Se o segundo da lista for menor ou igual que 'n' e 'n' for menor/igual que o segundo da lista:
                self.list.insert[2,n]
            elif self.list[2] <= n <= self.list[3]: # Se o terceiro da lista for menor/igual a 'n' e 'n' for menor/igual ao quarto da lista:
                self.list.insert[3,n]
        print(self.list)                

    def programa_5(self):

        
        for c in range(1,6):
            n = int(input(f'Digite o {c}º número: '))
            if c == 1 or n >= self.list_1[-1]:
                self.list_1.append(n)
            elif n <= self.list_1[0]:  # Se for menor ou igual ao primeiro
                self.list_1.insert(0,n)
            else:
                posicao = 0
                while posicao < len(self.list_1):
                    if n <= self.list_1[posicao]:
                        self.list_1.insert(posicao,n)
                        break
                    posicao += 1
                if posicao == len(self.list_1): # Se não encontrou posição menor ou igual
                    self.list_1.append(n)  # Adiciona ao final da lista
        print(self.list_1)

    def programa_6(self):

        for c in range(5):
            n = int(input('Digite um número: '))
            if c == 0 or n > max(self.list_2):
                self.list_2.append(n)
            else:
                for indice,valor in enumerate(self.list_2):
                    if n < valor:
                        self.list_2.insert(indice,n)
                        break
            print(f'{n} inserido na posição {self.list_2.index(n)}')
        print(f'\nValores digitados em ordem: {self.list_2}')            

    def programa_7(self):

        for c in range(5):
            n = int(input('Número: '))
            if c == 0 or n > self.list_3[-1]:
                self.list_3.append(n)
                print(f'O número {n} foi adicionado no final da lista.')
            else:
                for i in range(5):
                    if n <= self.list_3[i]:
                        self.list_3.insert(i,n)
                        print(f'O número {n} foi adicionado na posição {i+1}.')
                        break
        print(self.list_3)
        # Bonus:
        for i,v in enumerate(self.list_3):
            print(f'\nPosição {i+1}: {v}.')

    def menu(self):

        opcoes = int(input('''

                Inserindo valores em um lista ordenada - Sem uso do SORT

                [1] - Programa 1 
                [2] - Programa 2
                [3] - Programa 3
                [4] - Programa 4
                [5] - Programa 5
                [6] - Programa 6
                [7] - Programa 7
                [8] - Rodar tudo
                [9] - Sair

                '''))

        if opcoes == 1:
            self.programa_1()
            self.looping()
        if opcoes == 2:
            self.programa_2()
            self.looping()
        if opcoes == 3:
            self.programa_3()
            self.looping()
        if opcoes == 4:
            self.programa_4()
            self.looping()
        if opcoes == 5:
            self.programa_5()
            self.looping()
        if opcoes == 6:
            self.programa_6()
            self.looping()
        if opcoes == 7:
            self.programa_7()
            self.looping()
        if opcoes == 8:
            self.iniciar()
            self.looping()
        if opcoes == 9:
            self.sair()

    def looping(self):

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

                  

        

    @staticmethod
    def sair():
        import os
        exit()



if __name__== '__main__':
    
    adicionando_lista = Adicionando_Valores_Lista()
    adicionando_lista.menu()
