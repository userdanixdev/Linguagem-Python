
# Somando valores: Versão 6 : POO : Versão 02 : Comentada

class SomaValores:  # Toda classe deve receber um 'init' para construção. E deve receber, obrigatoriamente, atributos -
    def __init__(self):
        self.n1 = None   # Atributo de classe para armazenar o primeiro número
        self.n2 = None   # Atributo de classe para armazenar o segundo número
        self.soma = None # Atributo da classe para armazenar soma

# Depois do método contrutor 'init', devemos criar mais métodos,o método 'obter_valores' solicita os valores ao usuário e vai verificar se são numéricos.
# Converte as entradas para inteiros se forem válidas.

    def obter_valores(self):
        while True:   # Dentro do loop infinito, sempre que verdade, inserir dados. Se não for numérico, volta a ser numérico. Se for, continua, e a conversão para inteiro ocorre.
            n1=input('Insira um valor: ')
            n2=input('Insira um valor: ')
            if not (n1.isnumeric() and n2.isnumeric()):
                print('Somente números inteiros.')
                continue                  
            self.n1=int(n1)
            self.n2=int(n2)
            break   # Break no looping pq ele é infinito.

# Método que calcula a soma dos valores armazenados em 'self.n1' e 'self.n2' e mostra na tela formatado        
    def calcular_soma_resultado(self):
        self.soma = self.n1 + self.n2
        print(f'A soma entre o número {self.n1} + {self.n2} = {self.soma}.')

# Método que pode ser considerado o principal, para executar a Classe SomaValores:        
    def executar(self):
        self.obter_valores()
        self.calcular_soma_resultado()
        
# Quando um arquivo Python é executado, a variável especial '__name__' é definida. Se o arquivo é executado como o script principal.
# '__name__' é definido como '"__main__"'.
if __name__ == '__main__':
    import time
    time.sleep(1)
    print(f'{"+"*40}\n{"Somando valores":^38}\n{"Versão 06":^38}\n{"POO: Versão 02":^38}\n{"+"*40}')
    time.sleep(0.5)
    soma_valores=SomaValores()
    soma_valores.executar()
    time.sleep(1)
    print('Fim')
    
    
    
