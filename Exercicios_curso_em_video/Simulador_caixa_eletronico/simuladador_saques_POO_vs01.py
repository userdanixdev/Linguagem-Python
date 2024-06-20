# Simulador Caixa eletrônico: Saques
# Versão : POO : Versão 1 : Somente com 1 programa.

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
                    self.cedula = 1
                self.total_cedulas = 0
        if self.total_cedulas > 0:
            print(f'Total de {self.total_cedulas} cedula(s) de R$ {self.cedula},00')

    def iniciar(self):
        while True:
                self.simulador_saque_1_input_usuario()
                self.simulador_saque_1_condicionais()
                while True:
                    continuar = input('Deseja continar? [1-SIM / 2-NÃO]')
                    if continuar in ['1','2']:
                        break
                    else:
                        print('Entrada inválida.')
                if continuar == '2':
                    break
        print(f'Fim.')

if __name__ == '__main__':
    
    simulador_banc = Simulador_Saque()
    simulador_banc.iniciar()
