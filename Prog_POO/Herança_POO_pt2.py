# Herança Simples: Programação Orientada a Objetos em Python
# Aqui na parte II , exibe os métodos '__str__' e o 'super().__init__()' para herdar atributos da classe pai
#### Com o método '__str__' podemos verificar os dados que estão na classe sem a necessidade de imprimi-los. #####
##### Além disso, o método '__str__' só é possível executá-lo quando chamar o método especial 'super().__init__()' ####
### Outro ponto importante: Na herança, as classes 'motocicleta' e 'carro' herdaram os atributos da classe pai. ###
class veiculo:
    def __init__(self, cor, placa, rodas):
     self.cor = cor      # Definições de atributos da classe veiculo
     self.placa = placa  # Definições de atributos da classe veiculo
     self.rodas = rodas  # Definições de atributos da classe veiculo
    
    def ligar_motor(self):
        print( "Ligando o motor..." )  # Método para ligar o motor do veículo ( Definições de comportamentos da classe veiculo )
    def __str__(self):  # Esse método especial retorna uma representação em string do objeto herdado, 
      #sem a necessidade de imprimir cada atributo individualmente
        return f"Veículo(cor={self.cor}, placa={self.placa}, rodas={self.rodas})"        
class motocicleta(veiculo):
    pass
class carro(veiculo):
    pass
class caminhonete(veiculo):
    def __init__(self, cor, placa, rodas, carregado=True):
        super().__init__(cor, placa, rodas) # Chama o construtor da classe pai (veiculo), necessário para herdar e iniciar 
        self.carregado = carregado
    def sim_carregado(self):
        if self.carregado:
            print("A caminhonete está carregada.")
        else:
            print("A caminhonete não está carregada.")        

moto = motocicleta("Vermelha", "XYZ-1234", 2)
print(f"Motocicleta - Cor: {moto.cor}, Placa: {moto.placa}, Rodas: {moto.rodas}") # Não necessário caso o método __str__ esteja implementado
print(moto) # Exibe a representação do objeto moto com os valores que estão alocados na memória
moto.ligar_motor()  # Chama o método ligar_motor da classe veiculo

carro = carro("Azul", "ABC-5678", 4)
print(f"Carro - Cor: {carro.cor}, Placa: {carro.placa}, Rodas: {carro.rodas}") # Não necessário caso o método __str__ esteja implementado
print(carro) # Exibe a representação do objeto carro com os valores que estão alocados na memória
carro.ligar_motor()  # Chama o método ligar_motor da classe veiculo

caminhonete = caminhonete("Preta", "DEF-9012", 8)
print(f"Caminhonete - Cor: {caminhonete.cor}, Placa: {caminhonete.placa}, Rodas: {caminhonete.rodas}")
print(caminhonete) # Exibe a representação do objeto caminhonete com os valores que estão alocados na memória, 'sem o método __str__'
caminhonete.ligar_motor()  # Chama o método ligar_motor da classe veiculo
caminhonete.sim_carregado()  # Chama o método sim_carregado da classe caminhonete


