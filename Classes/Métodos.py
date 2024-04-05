Os métodos de classes são como funções dentro de uma classe. Que realizam operações específicas em objetos criados a partir dessa classe.
O método 'init' é um método especial que é chamado para inicializar os atributos de um objeto.

  class Circulo():
    pi = 3.14   #<-Constante
    def __init__(self,raio=5):
      self.raio = raio
    def area(self):   #<- Método calcula área   
      return (self.raio * self.raio)*Circulo.pi
    def setRaio(self,novo_raio):  #<- Método para gerar novo raio
      self.raio = novo_raio
    def getRaio(self):
        return self.raio






      
