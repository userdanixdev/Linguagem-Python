# Simulador Caixa eletrônico: Saques
# Versão : POO : Versão 3 : Com 3 programas com scripts diferentes + versão 06 estruturada

class Simulador_Saque:
    def __init__(self):
        
        self.valor = 0
        self.total = self.valor
        self.cedula = 50
        self.total_cedulas = 0
        #3ºPrograma:
        self.ced_200 = 0
        self.ced_100 = 0
        self.ced_50 = 0
        self.ced_20 = 0
        self.ced_10 = 0
        self.ced_5 = 0
        self.ced_1 = 0
        self.saque = 0
        self.pedido = 0

    def simulador_saque_1_input_usuario(self):

        self.valor = int(input('Que valor você quer sacar? R$ '))
        self.total = self.valor
        
    def simulador_saque_1_condicionais(self):

        while self.total > 0:
            if self.total >= self.cedula:
                self.total -= self.cedula
                self.total_cedulas += 1
            else:
                if self.total_cedulas > 0:
                    print(f'Total de {self.total_cedulas} cédulas de R${self.cedula}.')
                if self.cedula == 50:
                    self.cedula = 20
                elif self.cedula == 20:
                    self.cedula = 10
                elif self.cedula == 10:
                    self.cedula = 5
                elif self.cedula == 5:
                    self.cedula = 1
                self.total_cedulas = 0
        if self.total_cedulas > 0:
            print(f'Total de {self.total_cedulas} cedula(s) de R$ {self.cedula},00')

    def iniciar(self):
                print('Simulado: Saque - Versão 01')
                self.simulador_saque_1_input_usuario()
                self.simulador_saque_1_condicionais()
                print('\nSimulador - Versão 002')
                self.simulador_saque_2_input()
                self.simulador_saque_2_condicionais()
                print('\nSimulador: Saque - Versão 003')
                self.simulador_saque_3_input()
                self.simulador_saque_3_condicionais()
                self.simulador_saque_3_exibir_dados()
                print('\nSimulador: Saque - Versão 006')
                self.simulador_saque_6()

    def simulador_saque_2_input(self):

        self.total=int(input('Digite um valor: '))
        
        
    def simulador_saque_2_condicionais(self):

        for i in (50,20,10,5,1):
            self.total_cedulas = 0
            while self.total >= i:
                    self.total -= i
                    self.total_cedulas += 1
            if self.total_cedulas != 0:
                print(f'Total de cédulas de R${i}:{self.total_cedulas}.')

    def simulador_saque_3_input(self):

        self.pedido=int(input('Que valor você quer sacar? R$ '))

    def simulador_saque_3_condicionais(self):
        
        while self.pedido != self.saque:
            if (self.pedido - self.saque)>= 50:
                self.ced_50 += 1
                self.saque +=50
            elif 50 > (self.pedido-self.saque) >= 20:
                self.ced_20 += 1
                saque += 20
            elif 20 > (self.pedido - self.saque)>=10:
                self.ced_10 += 1
                self.saque += 10
            elif 10 > (self.pedido - self.saque) >= 5:
                self.ced_5 += 1
                self.saque += 5
            else:
                self.ced_1 +=1
                self.saque +=1

    def simulador_saque_3_exibir_dados(self):

        print(f'''
    Seu saque foi de R$ {self.saque},00 contendo {(self.ced_50+self.ced_20+self.ced_10+self.ced_5+self.ced_1)} notas, sendo:

                R$ 50,00 X {self.ced_50}
                R$ 20,00 X {self.ced_20}
                R$ 10,00 X {self.ced_10}
                R$ 5,00  X {self.ced_5}
                R$ 1,00  X {self.ced_1}
                ''')

    def simulador_saque_6(self):

        valor = int(input('Insira o valor que deseja sacar: R$ '))
        notas = [100,50,20,10,5,1]
        for i in range(len(notas)):
            n = int(valor/notas[i])
            if n >= 1:
                print(f'Você receberá {n} notas de R$ {notas[i]:.2f}')
                valor  = valor - (n*notas[i])
                    

if __name__ == '__main__':
    
    simulador_banc = Simulador_Saque()
    simulador_banc.iniciar()
