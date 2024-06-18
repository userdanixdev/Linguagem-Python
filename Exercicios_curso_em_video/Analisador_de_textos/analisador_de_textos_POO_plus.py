# Analisador de textos:

# Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

# POO: Plus
  # Com adicionais como capitalize em cada nome e sobrenome e contagem de letras dos sobrenomes

class AnaliseNome:
    def __init__(self):
        self.nome = ''
        self.x = ''
        self.nome_dividido = ''

    def analise_textos_1(self):
        from time import sleep
        self.nome=input('Digite seu nome completo: ').strip().capitalize()
        sleep(0.9)
        print(f'Seu nome em maiúscula é {self.nome.upper()}.')
        sleep(0.8)
        print(f'Seu nome em minúsculo é {self.nome.lower()}.')
        sleep(0.9)
        print(f'Seu nome tem ao todo {len(self.nome)} letras.')
        sleep(0.8)
        print(f'Seu nome sem os espaços tem ao todo {len(self.nome)-self.nome.count(' ')} letras.')
        sleep(0.9)
        self.nome_dividido=self.nome.split() # O split separa, por padrão, em lista, as strings que estiverem separadas por espaços.
        print(f'Seu primeiro nome é {self.nome_dividido[0]} e ele possui {len(self.nome_dividido[0])} letras.')
        sleep(0.9)
        print(f'Seu segundo nome é {self.nome_dividido[1].capitalize()} e ele possui {len(self.nome_dividido[1])} letras.')
        sleep(0.9)
        print(f'Seu terceiro nome é {self.nome_dividido[2].capitalize()} e ele possui {len(self.nome_dividido[2])} letras.\n')       
               

        
    def analise_textos_2(self):
        self.x=input('Digite seu nome completo: ').strip().capitalize()
        print(f'''
        Seu nome em maiúsculas é {self.x.upper()}.
        Seu nome em minúsculas é {self.x.lower()}.
        Seu nome tem {len(self.x)-self.x.count(' ')} letras.
        Seu primeiro nome é {self.x.split()[0].capitalize()} e tem {len(self.x.split()[0])} letras.
        Seu segundo nome é {self.x.split()[1].capitalize()} e tem {len(self.x.split()[1])} letras.
        Seu terceiro nome é {self.x.split()[2].capitalize()} e tem {len(self.x.split()[2])} letras.
        ''')
        
    def casos_especiais(self):
        print('Podemos remover os espaços com o uso do (join)\nSendo assim nos mostra o comprimento real do nome.')
        self.x=input('Digite seu nome completo: ')
        print(f'Seu nome tem {(len("".join(self.nome.split())))} letras.')
        print('Sem o uso do split, temos o comprimento com os espaços maior, de 21 letras.')
        print(f'Comprimento com espaços, removendo a função split: {(len("".join(self.nome)))} letras. ')

    def casos_especiais_2(self):
        print('Uso da função replace, para substituir espaços como parâmetro e identificar com o (len) o tamanho real do nome.')
        self.x=input('Digite seu nome completo: ')
        print('Seu nome completo tem um total de ',len(self.x.replace(' ','')),'letras.\n')

    def iniciar(self):
        while True:
            from time import sleep
            print('Analisador de textos: 1\n')
            sleep(0.8)
            self.analise_textos_1()
            print('Analisador de textos: 2\n')
            sleep(0.8)
            self.analise_textos_2()
            sleep(0.5)
            print('Casos Especiais...\n')
            self.casos_especiais()
            sleep(0.8)
            print('\nCasos especiais 2\n')
            self.casos_especiais_2()
            sleep(1)
            while True:
                continuar=input('Gostaria de repetir ? [1-SIM / 2-NÃO]: ')
                if continuar in ['1','2']:
                    break
                else:
                    print('Entrada inválida. Somente 1 ou 2.')
            if continuar == '2':
                break
        print('Fim.')

if __name__ == '__main__':
    analise=AnaliseNome()
    analise.iniciar()
    
                            
                    
        
        
        
        
        
