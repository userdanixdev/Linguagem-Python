A maioria dos algoritmos de machine learning é programada por orientação a objeto.

Em programação Orientada a objeto(POO), uma classe é um estrutura que descreve o objeto.
Especificando os comportamentos e atributos deve ter.
  Uma classe define características e ações que um objeto deve possuir.

class Livro():
  def __init__(self):
      self.titulo = "Sapiens - Uma breve História da Humanidade."
      self.isbn = 998888
      print('Construtor chamado para criar um objeto desta classe.')
  def imprime(self):
      print('Foi criado o livro %s com ISBN %d' %(self.titulo,self.isbn))
    




