# Estatisticas em produtos:

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Versão 02:
# POO: Versão 02

class Produtos:
    def __init__(self):
        
        self.total = 0
        self.produtos_1000 = 0
        self.produtos_comprados = 0
        self.preco_produto_mais_barato = 0
        self.preco_produto = 0
        self.nome_produto = ''
        # Init para o segundo programa:
        self.total = 0
        self.totmil = 0
        self.menor = 0
        self.cont = 0
        barato = ' '
        self.preco = 0.0
        self.produto = ' '

    def prog_1_obter_dados(self):
        
        self.nome_produto = input('Nome do produto: ').strip().lower()
        self.preco_produto=float(input('Preço do produto: ').strip())

    def prog_1_condicionais(self):
        
        self.produtos_comprados += 1
        self.total += self.preco_produto
        if self.preco_produto > 1000:
            self.produtos_1000 += 1
        if self.produtos_comprados == 1:
            self.nome_produto_mais_barato = self.nome_produto
            self.preco_produto_mais_barato = self.preco_produto
        else:
            if self.preco_produto_mais_barato > self.preco_produto:
                self.preco_produto_mais_barato = self.preco_produto
                self.nome_produto_mais_barato = self.nome_produto
                    
    def prog_1_exibir_dados(self):

        print(f'Total:{self.total}\nProdutos mais de R$1.000,00:{self.produtos_1000}\nProduto mais barato:{self.nome_produto_mais_barato}.')
        print(f'O produto mais barato custou:{self.preco_produto_mais_barato}.')

    def init(self):
        while True:
            while True:
                self.prog_1_obter_dados()
                self.prog_1_condicionais()
                continuar = input('Deseja continuar no Programa 1 [1-SIM/2-NÃO]: ')
                if continuar == '2':
                    break
                elif continuar != '1':
                    print('Somente 1 para sim e 2 para não.')
            
               
            self.prog_1_exibir_dados()

            while True:
                print()
                print('Programa 02')
                self.prog_2_variaveis_contadoras()
                self.prog_2_obter_dados()
                self.prog_2_condicionais()
                continuar = input('Deseja continuar no Programa 02? [1-SIM / 2-NÃO] ')
                if continuar == '2':
                    break
                elif continuar != '1':
                    print('Somente 1 para SIM e 2 para NÃO.')
            
                                    
            self.prog_2_exibir_dados()
          
            continuar = input('Deseja executar os programas novamente? [1-Sim/Não-2]: ')
            if continuar == '2':
                break
            elif continuar != '1':
                print('Somente 1 para SIM e 2 para NÃO.')
                       

    def prog_2_variaveis_contadoras(self):

        self.total = 0
        self.totmil = 0
        self.menor = 0
        self.cont = 0
        barato = ' '
        self.preco = 0.0
        self.produto = ' '

    def prog_2_obter_dados(self):

        self.produto = input('Nome do produto: ')
        self.preco = float(input('Preço do produto: R$ '))

    def prog_2_condicionais(self):

        self.cont += 1
        self.total += self.preco
        if self.preco > 1000:
            self.totmil += 1
        if self.cont == 1:
            self.menor = self.preco
            self.barato = self.produto
        else:
            if self.preco < self.menor:
                self.menor = self.preco
                
    def prog_2_exibir_dados(self):

        print(f'O total da compra foi {self.total}.')    
        print(f'Temos {self.totmil} que custa mais de mil reais.')
        print(f'O produto mais barato custa R${self.menor:.2f}. e foi {self.barato}')        
        
       

        
if __name__=='__main__':
    analise_prod = Produtos()
    analise_prod.init()

        
        
