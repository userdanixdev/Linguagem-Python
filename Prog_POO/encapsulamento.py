#Encapsulamento:

#O encapsulamento é um dos conceitos fundamentais em programação orientada a objetos. Ele descreve a ideia de agrupar dados e os métodos
#que manipulam esses dados em uma unidade. Isso impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental
#de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.

#Valores públicos e privados.:

#Para resolver 'bugs' de saída como por exemplo. Ao pagar 20 reais o valor de saída mostra 10 reais.
#Ao encapsular dados, podemos restringir o acesso da variável de valor de saída. Por métodos podemos fazer com que leia o valor da variável
#e escreva o valor da variável, ficando mais simples de verificar o valor de entrada e saída. 
#Em um diagrama UML, o atributo '-saldo:float'  da classe 'conta' é um atributo privado.
#Os atributos '+depositar:float' e '+sacar:float' são atributos públicos da classe 'conta'.
#O cliente tem acesso ao 'saque' e 'depósito' mas ele não pode acessar o saldo sem passar pelos outros atributos 'saque' e 'depósito'.
#Porque ele não pode fazer isso? Se liberar o acesso diretamente ao saldo, um usuário poderá alterar o valor do atributo 'saldo' sem
#pré-validações. As validações serão feitas nos atributos 'sacar' e 'depósito'. O encapsulamento deixa o código mais dinâmico e seguro
#por que não expõe diretamente dos atributos 'saldo'. Mas os atributos '-saldo:float' deverão ser privados.

# O que são recursos públicos e privados?

#Em Python usamos convenções no nome do recurso, para definir se a variável é pública ou privada.
#Já nas linguagens como Java e C++, existem palavras reservadas para definir níveis de acesso aos atributos e métodos da classe.
#Elas são linguagens tipadas e Python não é, ela é dinâmica. Assim por convenção, dentro da equipe, podemos fazer convenções como por exemplo: 
#'_' <- Underline para dizer que o atributo é privado. Um recurso público pode ser acessado de fora da classe.
#Já um recurso privado só pode ser acessado pela classe.

#Por exemplo: Eu tenho uma classe 'pessoa' que possui os atributos 'nome' e 'data_nasc', poderá acessar colocando o ponto '.'
#Quando eu tenho uma variável privada eu teria a classe 'pessoa' '_nome' ou '_data_nasc'. Sendo acessado pela classe.
#Até o 'método' pode ser privado, podendo ser chamado por '_método'

#Sendo assim, todos os recursos são públicos, a menos que o nome inicie com 'underline'. O interpretador não irá garantir a proteção do recurso.
#Por convenção, ao encontrar uma variável e/ou método com nome iniciado por 'underline', sabemos que não deveríamos manipulçar o seu valor
#diretamente ou invocar o método fora do escopo da classe.

	class Conta:
           def __init__(self,saldo=0):
		self._saldo = saldo         # '_saldo' é um atributo privado
	   def depositar(self,valor): # 'depositar' é um atributo público
		pass
	   def sacar (self,valor):    # 'sacar' é um atributo público
		pass




