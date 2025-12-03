#Variáveis de Classe e variáveis de Instância:

#O que são as variáveis e como nós podemos utilizar?

#Todos os objetos nascem com o mesmo número de atributos de classe e de instância.
#Os atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia)
#Os atributos de classe são compartilhados entre os objetos.

#Vejamos um exemplo:

class Estudante:
	escola = 'DIO'   # Temos 'escola' como atributo
	# Toda variável de classe está declarada logo após a definição da classe	
	def __init__(self,nome,matricula):   # Construtor inicial da classe
		self.nome = nome  	# Temos 'nome' como atributo
		self.matricula = matricula    # Temos 'numero' como atributo

	def __str__(self):   # Método '__str__' para fazer a representação da classe
		return f"{self.nome} ({self.matricula}) - {self.escola}"

aluno_1 = Estudante("Guilherme",56451) # Instanciando o objeto 'gui'
aluno_2 = Estudante("Giovana",17323)  # Instanciando o objeto 'gi'

print(aluno_1)  # Imprimindo o objeto 'gui'
print(aluno_2)  # Imprimindo o objeto 'gi'

# Atributo de instância é único para cada objeto
aluno_1.nome = "Gui"
print(aluno_1)  # Imprimindo o objeto 'gui' após alterar o nome

Estudante.escola = "DIO - Digital Innovation One"  # Alterando o atributo de classe
print(aluno_1)  # Imprimindo o objeto 'gui' após alterar a escola
print(aluno_2)  # Imprimindo o objeto 'gi' após alterar a escola
# Perceba que agora os alunos possuem o mesmo valor para o atributo 'escola', pois é um atributo de classe.
aluno_3 = Estudante("Ana",99876)  # Instanciando o objeto 'ana'
print(aluno_3)  # Imprimindo o objeto 'ana' que também possui

aluno_1.escola = "Outra Escola"  # Alterando o atributo de instância apenas para o objeto 'gui'
print(aluno_1)  # Imprimindo o objeto 'gui' após alterar a
aluno_1.matricula = 11111  # Alterando o atributo de instância apenas para o objeto 'gui'
print(aluno_1)  # Imprimindo o objeto 'gui' 
aluno_4 = Estudante("Carlos",22222)  # Instanciando o objeto de classe 'carlos'
print(aluno_4)  # Imprimindo o objeto 'carlos' 
aluno_1.escola = "Python Brasil"  # Alterando o atributo de instância apenas para o objeto 'gui'
print(aluno_1)  # Imprimindo o objeto 'gui' após alterar a escola

# Sendo assim podemos concluir que:
# Variáveis de instância são únicas para cada objeto. E estão declaradas dentro do método construtor '__init__'.
# Variáveis de classe são compartilhadas entre todos os objetos. E estão declaradas logo após a definição da classe.

# Resultados da tela:
Guilherme (56451) - DIO
Giovana (17323) - DIO
Gui (56451) - DIO
Gui (56451) - DIO - Digital Innovation One
Giovana (17323) - DIO - Digital Innovation One
Ana (99876) - DIO - Digital Innovation One
Gui (56451) - Outra Escola
Gui (11111) - Outra Escola
Carlos (22222) - DIO - Digital Innovation One
Gui (11111) - Python Brasil

