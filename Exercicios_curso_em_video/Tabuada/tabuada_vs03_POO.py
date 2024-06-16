# Tabuada : Versão 03
# POO: 

class Tabuada:
    def __init__(self):
        self.continuar = True

    def exibir_tabuada(self,n):
        i = 1
        while i < 10:
            print(f'{n} X {i} = {n*i}')
            i += 1
        print(f'{n} x {i+0} = {n*(i+0)}')

    def pergunta_loop(self):
        saida = input('Deseja continuar?     [Digite N para não] ')
        if saida.capitalize() == 'n':
            self.continuar = False

    def iniciar_prog(self):
        while self.continuar:
            try:
                n = int(input("Digite um número para iniciar a tabuada: "))
                self.exibir_tabuada(n)
                self.pergunta_loop()
            except ValueError:
                print("Por favor, digite um número inteiro.")
        print('Fim')

if __name__=="__main__":
    tabuada = Tabuada()
    tabuada.iniciar_prog()
            
        
