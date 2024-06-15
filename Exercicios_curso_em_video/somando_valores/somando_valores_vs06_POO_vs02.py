# Somando valores: Versão 6 : POO : Versão 02

class SomaValores:
    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.soma = None
    def obter_valores(self):
        while True:
            n1=input('Insira um valor: ')
            n2=input('Insira um valor: ')
            if not (n1.isnumeric() and n2.isnumeric()):
                print('Somente números inteiros.')
                continue                  
            self.n1=int(n1)
            self.n2=int(n2)
            break
    def calcular_soma_resultado(self):
        self.soma = self.n1  + self.n2
        print(f'A soma entre o número {self.n1} + {self.n2} = {self.soma}.')
        
    def executar(self):
        self.obter_valores()
        self.calcular_soma_resultado()
        

if __name__ == '__main__':
    soma_valores=SomaValores()
    soma_valores.executar()
