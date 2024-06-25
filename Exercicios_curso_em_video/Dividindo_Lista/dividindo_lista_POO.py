class ExtratorDados:
    def __init__(self):
        pass
    
    def extraindo_dados(self):
        valores = []
            while True:
                try:
                    valores.append(int(input('Digite um valor: ')))
                    while True:
                         resposta = input('Quer continuar? [S/N] ')
                         if resposta in 'Nn':
                             break
                         elif resposta in 'Ss':
                             break
                         else:
                             print('Somente S para Sim e N para não.')
                    if resposta in 'Nn':
                        break
                except ValueError:
                    print('Somente valores inteiros.')
            
            print(f'\nVocê digitou {len(valores)} elementos.')
            valores.sort(reverse=True)
            print(f'Os valores em ordem descrescente {valores}.')
            if 5 in valores:
                print('O valor 5 não faz parte da lista.')
            else:
                print('O valor 5 não foi encontrado.')

        
    def extraindo_dados_2(self):

        numero = list()
        pares = list()
        impares = list()
        while True:
            try:
                numero.append(int(input('Digite um número: ')))
                while True:
                    resp = input('Quer continuar? [S/N] ')
                    if resp in 'Nn':
                        break
                    elif resp in 'Ss':
                        break
                    else:
                        print('Apenas S para Sim e N para não.')
                if resp in 'Nn':
                    break
            except ValueError:
                print('Somente valores inteiros.')
                    
        for indice,valor in enumerate(numero):
            if valor % 2  == 0:
                pares.append(valor)
            if valor % 2 == 1:
                impares.append(valor)
        print(f'A lista completa é {numero}.')
        print(f'A lista de pares: {pares}.')
        print(f'A lista de pares: {impares}.')

    def extraindo_dados_3(self):

        lista_1 = []
        lista_pares = []
        lista_impares = []
        while True:
            try:
                x = int(input('Digite um número: '))
                lista_1.append(x)
                if x % 2 == 0 and x!=0:
                    lista_pares.append(x)
                elif x % 2 = 0:
                    lista_impares.append(x)
            except ValueError:
                print('Somente números inteiros.')
                continue
            while True:
                r=input('Digite S ou N: ').strip().upper()[0]
                if r in 'N':
                    break
                elif r in 'S':
                    break
                else:
                    print('Somente S para Sim e N para não.')
            if r in 'N':
                break
        print(f'A lista com todos os valores é: {lista_1}\n'
              f'\nA lista com os valores pares:{lista_pares}\n'
              f'\nA lista com os valores impares:{lista_impares}')

    def extraindo_dados_4(self):
        while True:
                try:
                    q = int(input('Quantidade de números a inserir: '))
                    break
                except ValueError:
                    print('Somente valores inteiros.')
                    def input_numero(self,i):
                        while True:
                            try:
                                return int(input(f'Digite o número {i}; '))
                            except ValueError:
                                print('Somente números inteiros.')

        lista = sorted([self.input_numero(i) for i in range(1,q+1)])
        #lista = sorted([int(input(f'Digite o número {i}:'))for i in range(1,q+1)])
        print(f'\nLista:{lista}'
              f'\nNúmeros impares:{[x for x in lista if x % 2 != 0]}'
              f'\nNúmeros pares:{[y for y in lista if y % 2 == 0]}')

    def menu(self):
        while True:
            try:
                menu= '''\n
            +++++ MENU +++++

            [1] -\tExtraindo Dados
            [2] -\tExtraindo Dados - Dividindo Lista
            [3] -\tExtraindo Dados - Dividindo Lista
            [4] -\tExtraindo Dados - Dividindo (List Compreenhension)
            [5] -\tExecutar Todos
            [6] -\tSair

            ===> '''
                opcao = int(input(menu))
                return opcao 
            except ValueError:
                print('Opção Inválida. Insira o número inteiro.')

        

    def main(self):

        while True:
            opcao = self.menu()
            if opcao == 1:
                self.extraindo_dados()
            if opcao == 2:
                self.extraindo_dados_2()
            if opcao == 3:
                self.extraindo_dados_3()
            if opcao == 4:
                self.extraindo_dados_4()
            if opcao == 5:
              self.extraindo_dados()
              self.extraindo_dados_2()
              self.extraindo_dados_3()
              self.xtraindo_dados_4()
            if opcao == 6:
              self.sair()

    @staticmethod
    def sair():
        import sys
        sys.exit()
        
# Criando uma instância da classe e executando método principal:

if __name__ == '__main__':
    app = ExtratorDados()
    app.main()

    
                      
