#esafio
#	Crie um programa onde joão informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr.
#   Adicione esses comportamentos.

class cachorro:
    def __init__(self,nome,raca,idade, acordado=True):		
     self.nome = nome           #<- Atributos da classe
     self.raca = raca     		#<- Atributos da classe
     self.idade = idade			#<- Atributos da classe
     self.acordado = acordado   #<- Atributos da classe
     

# Agora preciso colocar 3 comportamentos para a bicicleta. Os métodos são bem parecidos com funções que estão dentro de uma classe.
    def latir (self):
        print('AU AU AU!!')
    def sentar(self):
	    print('Cachorro sentado.')
    def correr (self):
        print('Vapt Vupt!!')

def __str__(self): #<- Método especial para representar o objeto como strings
	return f"{self.__class__.__name__}: {[f'{chave}={valor}'for chave, valor in self.__dict__.items()]}"

def dog_novo():        
    d = cachorro("Rex","Pastor Alemão",5,True)
    print(d)

# Os comportamentos da classe do cachorro são definidos por métodos. Para definir o método usamos em Python a palavra reservada 'def'
# e pelo menos dentro do comportamento, entre parênteses, um argumento, obrigatoriamente, chamado 'self'
# Usuário informa os dados do cachorro:
nome = input("Digite a cor da bicicleta: ")
raca = input("Digite o modelo da bicicleta: ")
idade = int(input("Digite o ano da bicicleta: "))

c = cachorro(nome, raca, idade, acordado) #<- Instância da classe + argumentos

print("\n--- Cachorro cadastrado ---")
print(f"Nome: {c.cor}")
print(f"Raça: {c.modelo}")
print(f"Idade: {c.ano}")

print("\n--- Testando comportamentos ---")
c.latir()
c.sentar()
c.correr()
