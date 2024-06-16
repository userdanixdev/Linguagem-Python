

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
        
if __name__ == "__main__":
    while True:
        texto  = input('Escreva algo:   \nDigite (-S-) para sair.')
        analise= DissecandoVariavel(texto)
        analise.exibir_analise()
        if 'S' == texto.capitalize():
            break
            
    
  
