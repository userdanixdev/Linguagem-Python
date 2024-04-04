A maioria dos algoritmos de machine learning é programada por orientação a objeto.

Em programação Orientada a objeto(POO), uma classe é um estrutura que descreve o objeto.
Especificando os comportamentos e atributos deve ter.
  Uma classe define características e ações que um objeto deve possuir.

class Livro():
  def __init__(self):   #<- Método construtor '__init__' <- 'self' é uma referência'
      self.titulo = "Sapiens - Uma breve História da Humanidade."
      self.isbn = 998888
      print('Construtor chamado para criar um objeto desta classe.')
  def imprime(self):
      print('Foi criado o livro %s com ISBN %d' %(self.titulo,self.isbn))

# Criando uma instância da classe Livro
Livro1 = Livro()
Resultado:
Construtor chamado para criar um objeto desta classe.
--------------//----------------------/---------------------//
# O objeto Livro1 é do tipo Livro
type(Livro1)
Resultado:
__main__.Livro
--------------//---------------------//-------------------/----------//
# Atributo do objeto Livro1
Livro1.titulo
Resultado:
'Sapiens - Uma Breve História da Humanidade'
------------;--------------//----------------//-----------------
Livro1.isbn
Resultado:
9988888
===========//===================//======================//=============
# Método do objeto Livro1
Livro1.imprime()
  Resultado:
Foi criado o livro Sapiens - Uma Breve História da Humanidade com ISBN 9988888
  =============//======================//========================//===============
  






