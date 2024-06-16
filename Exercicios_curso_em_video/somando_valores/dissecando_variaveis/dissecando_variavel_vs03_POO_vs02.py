# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# Versão 03:     
# POO: Versão 2
# Essa versão recebe o loop como método estático para não modificar ou criar instância.

class DissecandoVariavel:
    def __init__(self,texto):
        self.texto = texto
        

    def exibir_analise(self):
        print(
            f'''
            O tipo primitivo é {type(self.texto)}
            É número:       {self.texto.isnumeric()}
            É alfabético:   {self.texto.isalpha()}
            É alfanumérico: {self.texto.isalnum()}
            É maiúscula:    {self.texto.isupper()}
            É minúscula:    {self.texto.islower()}
            É capitalizada: {self.texto.istitle()}
            ''')

    @staticmethod
    def ativador_loop():
        while True:
            texto  = input('Escreva algo:   \nDigite (-S-) para sair.')
            analise= DissecandoVariavel(texto)
            analise.exibir_analise()
            if 'S' == texto.capitalize():
                break
    
if __name__ == "__main__":
     DissecandoVariavel.ativador_loop()
    
  
