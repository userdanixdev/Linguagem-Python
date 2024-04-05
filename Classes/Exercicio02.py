# Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone(object):
  def __init__(self,tamanho,interface):
    self.tamanho = tamanho
    self.interface = interface

class MP3Player(Smartphone):
  def __init__(self,capacidade,tamanho='Pequeno',interface='Led'):
    self.capacidade = capacidade
    Smartphone.__init__(self,tamanho,interface)
  def print_mp3player(self):
    print('Valores para o objeto: %s %s %s %(self.tamanho,self.interface,self.capacidade))

device1 = MP3Player('64 GB')
device1.print_mp3player()
