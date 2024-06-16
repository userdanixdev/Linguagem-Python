# Pintando Paredes:
## Versão 01
### POO 

class PintandoParede:
    def __init__(self):
        self.largura = 0
        self.altura = 0
        self.area = 0
        self.tinta = 0

    def calculo_area(self):
        self.area = self.largura*self.altura

    def calculo_tinta(self):
        self.tinta = self.area/2
        #return self.tinta
    
    def exibir_tela(self):
        print(f'Sua parede tem a dimensão de {self.largura:.2f}x{self.altura:.2f} e sua área é de {self.area:.2f}m².')
        tinta_necessaria = self.calculo_tinta()
        print(f'Para pintar essa parede você vai precisar de {self.tinta} Litros de tinta.')

    def info_usuarios(self):
        self.largura=float(input('Largura da parede: '))
        self.altura=float(input('Altura da parede: '))

    def iniciar(self):
        self.info_usuarios()  # Os métodos devem usar 'self' para referenciar outros métodos
        self.calculo_area()
        self.exibir_tela()


if __name__=="__main__":
    paredes=PintandoParede()
    paredes.iniciar()
        
