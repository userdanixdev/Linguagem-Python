# Gerenciador de pagamento: Loja

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

# Versão: POO : Todas as versões da pasta estão aqui.

class Gerenciador_Pagamento:
    
    def __init__(self):

        self.preco = 0.0

    def programa_1(self):

        print('Loja de roupas')
        self.preco = float(input('Preço das compras: R$ '))
        print(''' FORMAS DE PAGAMENTO
        [1] - a vista - Dinheiro/cheque
        [2] - a vista cartão
        [3] - 2x no cartão
        [4] - 3x ou mais no cartão
        ''')

        opcao = int(input('Qual a opção? '))
        if opcao == 1:
            total = self.preco - (self.preco*10/100)
        elif opcao == 2:
            total = self.preco - (self.preco*5/100)
            print(f'Sua compra de R$ {self.preco} vai custar R$ {total}.')
        elif opcao == 3:
            total = self.preco
            parcela = total/2
            print(f'Sua compra parcelada em 2x de {parcela}.')
        elif opcao == 4:
            total = self.preco + (self.preco*20/100)
            total_parc=int(input('Quantas parcelas? '))
            parcela = total / total_parc
            print(f' Sua compra será parcelada em {total_parc} de R$ {parcela} com juros.')
        print(f'Sua compra de R$ {self.preco} vai custar {total} no final.')

    def menu(self):
        
        opcoes=int(input('''

            Gerenciador de Pagamento:

            [1] - Programa 1 - Basic
            [2] - Programa 2 - c/ loop para opção principal
            [3] - Programa 3 - Com validação de entrada, pergunta para realizar mais compras e loop para parcelamento.
            [4] - Executar tudo
            [5] - Sair

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
            self.iniciar()
        if opcoes == 5:
            self.sair()

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

    def iniciar(self):

        while True:
            try:
                print('Programa 1 - Basic ')
                self.programa_1()
                print()
                print('Programa 2 - c/ loop para opção principal')
                self.programa_2()
                print()
                print('Programa 3 - Com validação na entrada do preço e pergunta se quer realizar mais compras...\nLoop para menu principal') 
                self.programa_3()

                continuar = int(input('''

                    Repetir a operação ou voltar para o menu principal?

                    [1] - Repetir operação
                    [2] - Menu Principal

                    '''))

                if continuar == 1:
                    continue
                elif continuar == 2:
                    self.menu()
                else:
                    print('Opção inválida. Somente 1 para repetir ou 2 para sair.')
            except ValueError:
                print('Entrada inválida. Por favor, somente os números.')

                              

    def programa_2(self):

        print('Loja de Roupas')
        self.preco = float(input('Preço das compras: R$ '))
        while True:
            print('''FORMAS DE PAGAMENTO
            [1] - à vista / Dinheiro
            [2] - à vista cartão
            [3] - 2x no cartão
            [4] - 3x ou mais no cartão
            ''')

            opcao = int(input('Qual a opção? '))
            if opcao == 1:
                total = self.preco-(self.preco*10/100)
                print(f'Sua compra de R$ {self.preco:.2f} vai custar R$ {total:.2f} com 10% de desconto.')
                break
            elif opcao == 2:
                total = self.preco - (self.preco*5/100)
                print(f'Sua compra de R$ {self.preco:.2f} vai custar R$ {total:.2f} com 5% de desconto.')
                break
            elif opcao == 3:
                total = self.preco
                parcela = total/2
                print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
                break
            elif opcao == 4:
                total_parc = int(input('Quantas parcelas? '))
                if total_parc <= 2:
                    print('\nSelecione a opção 3 do menu princiapl para parcelamento em 2x sem juros.')
                else:
                    total=self.preco + (self.preco*20/100)
                    parcela = total/total_parc
                    print(f'Sua compra será parcelada em {total_parc}x de R$ {parcela:.2f} com juros.')
                    break
            else:
                print('Opção inválida. Tente novamente.')
        print(f'Sua compra de R${self.preco:.2f} vai custar R$ {total:.2f} no final.')

    def programa_3(self):

        while True:
            print('Loja de Roupas')
            while True:
                try:
                    self.preco = float(input('Preço das compras: R$ '))
                    if self.preco > 0 and self.preco < 10000:
                        break
                    else:
                        print('Entrada inválida. Por favor insira dentro do limite.')
                except ValueError:
                    print('Entrada inválida. Insira valores corretos.')
            while True:
                print('''  FORMAS DE PAGAMENTO
                [1] - à vista / Dinheiro
                [2] - à vista cartão
                [3] - 2x no cartão
                [4] - 3x ou mais no cartão
                ''')

                opcao = int(input('Qual a opção? '))
                if opcao == 1:
                    total = self.preco-(self.preco*10/100)
                    print(f'Sua compra de R${self.preco:.2f} vai custar R$ {total:.2f} com 10% de desconto.')
                    break
                elif opcao == 2:
                    total = self.preco-(self.preco*5/100)
                    print(f'Sua compra de R$ {self.preco:.2f} vai custar R$ {total:.2f} com 5% de desconto.')
                    break
                elif opcao == 3:
                    total = self.preco
                    parcela = total/2
                    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros.')
                    break
                elif opcao == 4:
                    total_parc = int(input('Quantas parcelas? '))
                    if total_parc <= 2:
                        print('\nSelecione a opção 3 do menu principal para 2x sem juros.')
                    else:
                        total = self.preco + (self.preco*20/100)
                        parcela = total/total_parc
                        print(f'Sua compra será parcelada em {total_parc}x de R${parcela:.2f} com juros.')
                        break
                else:
                    print('Opção inválida. Tente novamente.')
            print(f'Sua compra de R${self.preco:.2f} vai custar R${total:.2f} no final.')
            while True:
                continuar = input('\nGostaria de realizar mais compras? [1-SIM / 2 - NÃO] ')
                if continuar in ['1','2']:
                    break
                else:
                    print('Digite somente 1 para SIM e 2 para NÃO.')
            if continuar == '2':
                break
        print('Fim')

            
        

    @staticmethod
    def sair():

        import os
        exit()


if __name__=='__main__':
    
    pagamento=Gerenciador_Pagamento()
    pagamento.menu()
            
        




                

        
