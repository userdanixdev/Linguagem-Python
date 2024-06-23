# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Adicionando valores em uma lista:
# Versão POO:

class AdicionandoValoresLista:
    def __init__(self):

        self.numeros = []
        self.lista = []
        self.lista_2 = []
        self.valores = []

    def programa_1(self):

        while True:
            try:
                n = int(input('Digite um valor: '))
                if n not in self.numeros:
                    self.numeros.append(n)
                    print('Valor adicionado com sucesso.')
                else:
                    print('Valor duplicado. Somente números.')
                while True:                    
                    r=str(input('Quer continuar? [S/N] ')).upper().strip()
                    if r in 'SN':
                        break
                    else:
                        print('Entrada inválida. Somente S ou N são permitidos.')
                if r == 'N':
                    break
            except ValueError:
                print('Somente o solicitado.')
        print(f'Você digitou os valores...{self.numeros}.')
        self.numeros.sort()
        print(f'Os números em ordem crescente {self.numeros}.')


    def programa_2(self):

        while True:
                try:
                    numero = int(input('Digite um valor: '))
                    if numero not in self.lista:
                            self.lista.append(numero)
                            print('Valor adicionado.')
                    else:
                            print('Esse número já existe.')
                    while True:
                               resposta = input('Deseja continuar? [S/N]').upper()
                               if resposta in ('S', 'N'):
                                    break
                               else:
                                    print('Somente S ou N')
                    if resposta == 'N':
                        break
                except ValueError:
                    print('Somente números inteiros.')
                                    
                    
        print(f'A lista: {self.lista}',f'\nA lista em ordem: {sorted(self.lista)}')

    def programa_3(self):

        while True:
            try:
                self.lista_2.append(int(input('Escolha um valor: ')))
                print('Valor adicionado a lista.')
            except ValueError:
                print('Erro ao preencher o requisito, apenas números...')
            while True:
                sair = input('Deseja continuar? [S/N]').strip().upper()[0]
                if sair in 'SN':
                    break
                else:
                    print('Entrada inválida. Somente S para continuar ou N para sair.')
            if sair == 'N':
                break
                
        self.lista_2.sort()
        print(f'Os números listados foram:{self.lista_2}')

    def programa_4(self):

        while True:
            try:
                n = int(input('Digite um valor: '))
                if n not in self.valores:
                    self.valores.append(n)
                    self.valores.sort()  # Já deixa a lista em ordem
                    print('Valor adicionado com sucesso..')
                else:
                    print('Valor duplicado, não será incluso na lista.')
            except ValueError:
                print('Somente números inteiros.')
            resp=input('Deseja continuar? [S/N]').upper().strip()
            while resp not in 'SN':
                print('Valor digitado inválido.')
                resp = input('Deseja continuar? [S/N]').upper().strip()[0]
            if resp == 'N':
                break
        print(f'Você digitou os valores {self.valores}.')            

        

    def loop(self):

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

        
              
       
        
            
    def iniciar(self):

        self.programa_1()
        print()
        self.programa_2()
        print()
        self.programa_3()
        print()
        self.programa_4()
        

    @staticmethod
    def sair():
        import os
        exit()

    def menu(self):

        opcoes = int(input('''

                Adicionando valores em uma Lista:

                [1] - Programa 1
                [2] - Programa 2
                [3] - Programa 3
                [4] - Programa 4
                [5] - Executar tudo
                [6] - Sair

                '''))
        
        if opcoes == 1:
            self.programa_1()
            self.loop()
        if opcoes == 2:
            self.programa_2()
            self.loop()
        if opcoes == 3:
            self.programa_3()
            self.loop()
        if opcoes == 4:
            self.programa_4()
            self.loop()
        if opcoes == 5:
            self.iniciar()
            self.loop()
        if opcoes == 6:
            self.sair()
            
if __name__=='__main__':
    lista=AdicionandoValoresLista()
    lista.menu()


