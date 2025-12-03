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

from abc import ABC  #

# O controle remoto terá dois métodos padrões:
	class ControleRemoto(ABC):
	        @abstractmethod
		      def ligar(self):    # 1º método seria ligar
			        pass
	        @abstractmethod
		      def desligar(self): # 2º método seria desligar
		        	pass
	class ControleTV(ControleRemoto):
			pass

	
controle =  ControleTV()   # Foi instânciado a classe 'ControleTV' mas o sistema não deixará, porque foi criado uma 'abstractmethod'
controle.ligar()
controle.desligar()
