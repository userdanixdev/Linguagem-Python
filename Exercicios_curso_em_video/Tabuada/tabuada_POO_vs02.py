# Tabuada Versão 02:
# POO:

class Tabuada:
  def __init__(self):
    self.continuar = True

  def exibir_tabuada(self,numero):
    for c in range(1,11):
      print(f'{numero :2} x {c :2} = {numero * c :2}')

  def perguntar_continuar(self):
    saida = input('Quer continuar? [S/N] ')
    if saida.capitalize() == 'N':
      self.continuar = False

  def iniciar(self):
    while self.continuar:
      try:
          numero = int(input('Digite um número: '))
          self.exibir_tabuada(numero)
          self.perguntar_continuar()
      except ValueError:
          print("Por favor, digite um número válido.")
    print('Fim')

if __name__=="__main__":
  tabuada=Tabuada()
  tabuada.iniciar()




