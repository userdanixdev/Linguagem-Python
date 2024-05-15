# Herança Simples:
class Veiculo:
    def __init__(self,cor,placa,num_rodas):
        self.cor = cor
        self.placa =  placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print('Ligando o motor')
        
class Motocicleta(Veiculo):
    pass
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    pass

moto=Motocicleta('preta','abc-1234',2)
print(moto)
moto.ligar_motor()

carro = Carro('branco','cde-0098',4)
carro.ligar_motor()

caminhao = Caminhao('roxo','gfd-8712',8)
caminhao.ligar_motor()
