class LocacaoCarros:
    def __init__(self):
        self.nome = ''
        self.dia = 0
        self.mes = ''
        self.dias = 0
        self.km = 0
        self.pagamento = 0.0
        self.total_alugueis = 0

    def obter_dados(self):
        self.nome = input('Insira o nome do locador: ').capitalize()
        self.dia = int(input(f'{self.nome}, qual dia em o carro foi alugado? '))
        self.mes = input('Qual o mês em que foi alugado? ').capitalize()
        self.dias = int(input('Quantos dias o carro foi alugado? '))
        self.km = int(input('Quantos KM ele foi rodado? '))

    def calcular_pagamento(self):
        self.pagamento = (self.dias*60) + (self.km*0.15)

    def mostrar_dados(self):
        print(f'O total a pagar é de R${self.pagamento:.2f} reais.')
        print(f'O carro foi alugado no dia {self.dia} e no mês {self.mes}.')
        print(f'Ficou {self.dias} dias alugado.')
        print(f'O nome do locador é: {self.nome}.')

    def iniciar(self):
        while True:
            self.obter_dados()
            self.calcular_pagamento()
            self.mostrar_dados()
            self.total_alugueis += 1
            while True:
                continuar = input('Deseja continuar? [1-SIM / 2-NÃO]')
                if continuar in ['1','2']:
                    break
                else:
                    print('Entrada inválida.')
            if continuar == '2':
                break
        print(f'Fim. Total de alugueis: {self.total_alugueis}')

if __name__=='__main__':
    locacao = LocacaoCarros()
    locacao.iniciar()
   
