# Aumento Salarial : POO

class Salario:
    def __init__(self):
        self.nome = ''
        self.salario = 0.0
        self.aumento = 0.0
        self.novo_salario = 0.0        
        self.continuar = True

    def obter_dados(self):
        while True:
            self.nome=input('Qual o nome do empregado: ')
            if self.nome.replace(" ", "").isalpha(): # A função replace troca espaços por vazios.
                break
            else:
                print('Nome inválido. Digite apenas letras.')
        self.salario=float(input('Qual o salário atual? '))
        self.aumento = float(input('Quantos por cento? '))

    def calculo_novo_salario(self):
        self.novo_salario=self.salario*((100+self.aumento)/100)

    def mostrar_dados(self):
        print(f'O funcionário {self.nome} que ganhava R$ {self.salario:.2f} com {self.aumento:.0f}%',end=''
              f' de aumento, passa a receber R${self.novo_salario:.2f}.\n')

    def loop(self):
        while True:
            self.obter_dados()
            self.calculo_novo_salario()
            self.mostrar_dados()
            self.continuar = input('Deseja continuar? [1-SIM & 2-NÃO]')
            if self.continuar == '1':
                continue
            if self.continuar == '2':
                break


if __name__=='__main__':
    salario = Salario()
    salario.loop()
        
