# Tabuada
# POO

class Tabuada:
    def __init__(self):
        self.continuar = True  # Resultado booleano para controlar o loop, se verdadeiro, continua
        
    def exibir_tabuada(self,numero):
        for n2 in range(1,11):
            resultado = numero * n2
            print(f'{numero} X {n2} = {resultado}')

    def perguntar_continuar(self):
        resposta=input('Quer continuar? [S/N] ')
        if resposta.capitalize() == 'N':
            self.continuar = False   # Ao colocar 'n' o loop é encerrado pelo construtor 'init'

# Loop principál que solicita o número para o usuário
# Contém o método para exibir a tabuada e controle de resposta para o usuário continuar ou nao
    def iniciar(self):  # O método iniciar recebe o atributo da classe como TRUE
        while self.continuar:
            try:
                numero = int(input('Digite um número da tabuada: '))
                self.exibir_tabuada(numero)
                self.perguntar_continuar()
            except ValueError:
                print('Por favor, digite um número válido.')
        print('Fim')

if __name__=="__main__":
    tabuada = Tabuada()
    tabuada.iniciar()
