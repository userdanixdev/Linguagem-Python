#Conhecer o paradigma de programação orientada a objeto (POO)

#	É a forma como você soluciona os problemas através do código.

#Alguns paradigmas em Python

#	Imperativo ou procedural
##	Orientado a eventos
#	Orienta a objetos

#O paradigma de programação orientado a objetos estrutura o código abstraindo problemas em objetos do mundo real,
#facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender são: classes e objetos

#Exemplo: Produtos que foram vendidos em um supermercado
#Com a orientação a objetos eu consigo criar classes e objetos que vão mapear os produtos dentro do sistema que irão se parecer muito com
#os objetos da vida real.

#Criando uma classe eu posso descrever as caracaterísticas desses produtos de supermercado.
#O produto tem um preço, um nome, fabricante, data de validade. Tudo isso vai na especificação de uma classe.
#Mas são diversos produtos como uma farinha, bolacha, sal, açucar. Podemos trazer esses produtos para a programação orientada a objeto.

#CLASSES E OBJETOS:
#	Uma classe define as características e comportamentos de um objeto. Os objetos podemos usá-los e eles possuem características
#e comportamentos que foram definidos nas classes. A 'instância' deles (objetos) eu consigo utilizar.
#Imagine uma classe 'casa' onde podemos colocar 'números de quartos', 'caragem', 'cor das paredes'. Assim podemos instânciar várias 'casas'
#com diversas características. A ideia da programação orientada a objetos, a partir da planta de uma casa, construir outras casas.

#Desafio
#	Crie um programa onde joão informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr.
#Adicione esses comportamentos.

#Desafio
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


