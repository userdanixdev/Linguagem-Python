#esafio
#	Crie um programa onde joão informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr.
#   Adicione esses comportamentos.

class bicicleta:
    def __init__(self,cor, modelo, ano, valor):		
     self.cor = cor          #<- Atributos da classe
     self.modelo = modelo      #<- Atributos da classe
     self.ano =  ano         #<- Atributos da classe
     self.valor = valor      #<- Atributos da classe

# Agora preciso colocar 3 comportamentos para a bicicleta. Os métodos são bem parecidos com funções que estão dentro de uma classe.
    def buzinar (self):
        print('Plim plim...')
    def parar(self):
	    print('Parando bicicleta...')
	    print('Bicicleta: PARADA.')
    def correr (self):
        print('VRUMMMMM!!')

# Os comportamentos da classe bicicleta são definidos por métodos. Para definir o método usamos em Python a palavra reservada 'def'
# e pelo menos dentro do comportamento, entre parênteses, um argumento, obrigatoriamente, chamado 'self'
# João informa os dados da bicicleta
cor = input("Digite a cor da bicicleta: ")
modelo = input("Digite o modelo da bicicleta: ")
ano = int(input("Digite o ano da bicicleta: "))
valor = float(input("Digite o valor da bicicleta: "))

b1 = bicicleta(cor, modelo, ano, valor) #<- Instância da objeto + argumentos

print("\n--- Bicicleta cadastrada ---")
print(f"Cor: {b1.cor}")
print(f"Modelo: {b1.modelo}")
print(f"Ano: {b1.ano}")
print(f"Valor: R$ {b1.valor:.2f}")

print("\n--- Testando comportamentos ---")
b1.buzinar()
b1.correr()
b1.parar()
