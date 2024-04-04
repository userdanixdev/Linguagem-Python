# Colocando os parâmetros dentro da função, podemos criar diferentes livros,
# deixando a classe melhor
class Livro():
  def __init__(self,titulo,isbn):   #<- Parâmetros
    self.titulo = titulo
    self.isbn = isbn
    print('Construtor chamado para criar um objeto desta classe.')
  def imprime(self,titulo,isbn):
    print('Este é o livro %s e ISBN %d' %(titulo,isbn))

-------------//--------------------//-------------------------------
# Com isso podemos colocar o livro dentro do objeto assim:
Livro2 = Livro('O poder do Hábito',7788611)
Resultado:
Construtor chamado para criar um objeto desta classe.
-----------//----------------//----------------//------------
Livro2 = Livro('O poder do Hábito', 7788611)
Resultado:
Construtor chamado para criar um objeto desta classe
-----------//-----------------//-------------
Livro2.titulo
Resultado:
'O poder do Hábito'
-----------------------------------------------------------------------------------
# OUTRO EXEMPLO:
class Algoritmo():
  def __init__(self,tipo_algo):
    self.tipo = tipo_algo
    print('Construtor chamado para criar um objeto desta classe.')
# Criando o objeto a partir da classe:
algo1 = Algoritmo(tipo_algo = "Random Florest")
#Resultado:
# Construtor chamado para criar um objeto desta classe
# Criando outro objeto:
algo2 = Algoritmo(tipo_algo= "Deep Learning")
# Resultado:
# Construtor chamado para criar um objeto desta classe.
-----------//-------------------//--------------------//-------------------//------------
