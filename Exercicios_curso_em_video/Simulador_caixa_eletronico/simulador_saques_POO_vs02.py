# Simulador Caixa eletrônico: Saques
# Versão : POO : Versão 2 : Com 2 programas

class Simulador_Saque:
    def __init__(self):
        
        self.valor = 0
        self.total = self.valor
        self.cedula = 50
        self.total_cedulas = 0

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
        
                self.simulador_saque_1_input_usuario()
                self.simulador_saque_1_condicionais()
                print('Simulador - Versão 002')
                self.simulador_saque_2_input()
                self.simulador_saque_2_condicionais()
                

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

                    

if __name__ == '__main__':
    
    simulador_banc = Simulador_Saque()
    simulador_banc.iniciar()
