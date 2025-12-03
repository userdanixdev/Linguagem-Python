#Classes abstratas e métodos estáticos

#As interfaces definem o que uma classe deve fazer. Algo que queremos implementar de forma padrão.
#O conceito de interface é definir um contrato, onde são declarados os métodos( o que deve ser feito) e suas respectivas assinaturas.
#Em python utilizamos classes abstratas para criar contratos. Essas classes abstratas não podem ser instanciadas.
#Em Java po exemplo, não permite herança múltipla. Mas tem o conceito de classes abstrata. Em Python, permite herança múltipla, extendendo
#as classes mas não utiliza palavra reservada 'interface'.

#Criando classes abstratas utilizando o módulo 'abc'.

#	Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo, instalável, que fornece a base para definir
#as classes abstratas e o nome do módulo é ABC. O módulo funciona decorando métodos da classe base como abstratos e em seguida registra
#como se fosse classe concreta. Um método se torna abstrato quando decorado com '@abstractmethod.'

#Exemplo de controle remoto:

from abc import ABC  
from abc import abstractmethod


# O controle remoto terá dois métodos padrões:
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):    # 1º método seria ligar
        pass
    @abstractmethod
    def desligar(self): # 2º método seria desligar
       	pass
    @property
    #@abstractproperty     # 3º método comum para todas as classes filhas, método abstrato de propriedade obrigatório;
    def marca(self):      
        print("Marca: Generic")
class ControleTV(ControleRemoto):
    def ligar(self):
        print("A TV está ligada.")
    def desligar(self):
        print("A TV está desligada.")
    @property
    def marca(self):
        print("Marca: Samsung")        

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("O ar condicionado está ligado.")
    def desligar(self):
        print("O ar condicionado está desligado.")       
    @property
    def marca(self):
        print("Marca: LG")         
        
        

	
controle = ControleTV()   # Foi instânciado a classe 'ControleTV' mas o sistema não deixará, porque foi criado uma 'abstractmethod',       
controle.ligar()            # Eles são agora métodos abstratos. Sendo obrigado a implementar os dois métodos na classe filha.
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
# Sendo assim, por padronização, todas as classes que herdam de 'ControleRemoto' serão obrigadas a implementar os métodos 'ligar' e 'desligar'.
# No qual são métodos abstratos. Fornecendo segurança maior para o polimorfismo. Garantindo que todas as classes filhas terão esses métodos.
# Sendo forçado as classes filhas a implementar esses métodos.

https://docs.python.org/pt-br/3/library/abc.html

