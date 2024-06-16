# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# Versão 02:

class DissecandoVariavel:
    def __init__(self,texto):
        self.texto = texto
        

    def exibir_analise(self):
        if self.texto.isspace():
            print('Apenas espaços, dado incorreto')
        if self.texto.isnumeric():
            print('é número')
        if self.texto.isalpha():
            print('é letra')
        if self.texto.isalnum():
            print('é Alfanumérico')
        if self.texto.islower():
            print('letras minusculas')
        if self.texto.istitle():
            print('capitalizada')
        if self.texto.isupper():
            print('maiusculas')
            
    @staticmethod
    def ativador_loop():
        while True:
            texto  = input('Escreva algo:   \nDigite (- S -) para sair.')
            analise= DissecandoVariavel(texto)
            analise.exibir_analise()
            if 'S' == texto.capitalize():
                break
    
if __name__ == "__main__":
     DissecandoVariavel.ativador_loop()
     import time
     time.sleep(1)
     print('Fim')
    
  

