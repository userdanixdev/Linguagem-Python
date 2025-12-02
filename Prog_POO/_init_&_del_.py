# Desafio:
#	Crie um programa onde o usuário informa: nome, raça, idade do cachorro.
	# Um cachorro pode: latir, correr e sentar
#   Adicione esses comportamentos.

# O Objetivo desse estudo é além de mostrar o comportamento do objeto. Como também mostrar os métodos especiais '__init__'
# mostrando uma mensagem inicializando. E o método '__del__' que deleta os comportamentos do objeto, no final do programa.

class cachorro:
    def __init__(self,nome,raca,idade, acordado=True):		# <- Método construtor com os atributos 'self' e os argumentos e '__init__'
     print('Inicializando dados do cachorro...') #<- Mensagem de inicialização    
     self.nome = nome           #<- Atributos da classe
     self.raca = raca     		#<- Atributos da classe
     self.idade = idade			#<- Atributos da classe
     self.acordado = acordado   #<- Atributos da classe
     
    def __del__(self):				#<- Método destrutor, executado no final do programa
     print(f'O cachorro {self.nome} foi deletado da memória.')
# Agora preciso colocar 3 comportamentos para a bicicleta. Os métodos são bem parecidos com funções que estão dentro de uma classe.
    def latir (self):
        print('AU AU AU!!')
    def sentar(self):
	    print('Cachorro sentado.')
    def correr (self):
        print('Vapt Vupt!!')

    def __str__(self): #<- Método especial para representar o objeto como strings
        return f"{self.__class__.__name__}: {[f'{chave}={valor}'for chave, valor in self.__dict__.items()]}"

def dog_novo():        # Método para criar um novo cachorro. Inicializa o programa de novo, sem cadastro. E no final deleta.
    d = cachorro("Rex","Pastor Alemão",5,True)
    print(d)

# Os comportamentos da classe do cachorro são definidos por métodos. Para definir o método usamos em Python a palavra reservada 'def'
# e pelo menos dentro do comportamento, entre parênteses, um argumento, obrigatoriamente, chamado 'self'
# Usuário informa os dados do cachorro:
nome = input("Digite o nome do dog: ")
raca = input("Digite a raça do dog: ")
idade = int(input("Digite a idade do dog: "))

c = cachorro(nome, raca, idade, acordado=False) #<- Instância da classe + argumentos

print("\n--- Cachorro cadastrado ---")
print(f"Nome: {c.nome}")
print(f"Raça: {c.raca}")
print(f"Idade: {c.idade} anos")

print("\n--- Testando comportamentos ---")
c.latir()
c.sentar()
c.correr()
print(c)
dog_novo()

Resultadados mostrados na tela:

Digite o nome do dog: Star
Digite a raça do dog: Pitbull
Digite a idade do dog: 5
Inicializando dados do cachorro...

--- Cachorro cadastrado ---
Nome: Star
Raça: Pitbull
Idade: 5 anos

--- Testando comportamentos ---
AU AU AU!!
Cachorro sentado.
Vapt Vupt!!
cachorro: ['nome=Star', 'raca=Pitbull', 'idade=5', 'acordado=False']
Inicializando dados do cachorro...  # Aqui ele inicializa novamente, porque foi criado um novo método. Sem cadastro. E mostra os dados.
cachorro: ['nome=Rex', 'raca=Pastor Alemão', 'idade=5', 'acordado=True']
O cachorro Rex foi deletado da memória.
O cachorro Star foi deletado da memória.
