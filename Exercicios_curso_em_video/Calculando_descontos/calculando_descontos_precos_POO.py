class Descontos:
    def __init__(self):
        self.preco = 0.0
        self.novo_preco = 0
        self.price = 0
        self.desconto_x = 0
        self.desconto = 0
        self.valor_final = 0.0

    def desconto_fixo_cinco(self):
        print('Desconto de 5%')
        preco = float(input('Qual é o preço do produto? R$ '))
        novo_preco = preco - (preco * 5/100)
        print(f'O produto que custava R${preco:.2f}, na promoção de 5% vai custar R${novo_preco:.2f}.')
        print()

    def calcular_desconto_variavel(self):
        self.preco = float(input('Qual o preço do produto? R$ '))
        self.desconto_x = int(input('De quanto será o desconto? '))
        self.desconto = (self.preco/100)*self.desconto_x
        self.valor_final = self.preco - self.desconto
        print(f'O produto que custava R${self.preco:.2f} com {self.desconto_x:.0f}% de desconto vai custar R${self.valor_final:.2f}.')
        
    def perguntar_continuar(self):
        while True:
            saida = input('Fazer outra operação? 1-Sim / 2-Não: ')
            if saida == '1':
                return True
            elif saida == '2':
                return False
            else:
                print("Opção inválida. Digite 1 para Sim ou 2 para Não.")

    def iniciar(self):
        self.desconto_fixo_cinco()
        print('Calculando Descontos: ')
        while True:
            self.calcular_desconto_variavel()
            if not self.perguntar_continuar():
                break
        print('Fim')

if __name__ == "__main__":
    desc_desc = Descontos()
    desc_desc.iniciar()


