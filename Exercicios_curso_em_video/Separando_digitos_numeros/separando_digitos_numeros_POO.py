# Separando digitos de um número: 
# POO:

class Separacao:
    def __init__(self):
        self.n = ''
        self.num = ''
        self.numero = 0
        self.number = ''
        self.number_2 = ''

    def primeira_forma(self):
        from time import sleep
        self.n=input('Informe um número de 0 a 9999: ')
        sleep(1)
        print('unidade:',self.n[-1:])
        sleep(1)
        print('dezena:',self.n[-2:-1])
        sleep(1)
        print('centena:',self.n[-3:-2])
        sleep(1)
        print('milhar:',self.n[-4:-3])
        sleep(1)

    def segunda_forma(self):
        self.num=input('Digite um número entre 0 e 9999: ')
        self.num = self.num[::-1]+'000'
        print(f'Unidades:{self.num[0]}\nDezenas:{self.num[1]}\nCentenas:{self.num[2]}\nMilher:{self.num[3]}.')

# o símbolo // faz a divisão e só pega o que esta antes da vírgula.
# o símbolo % faz a divisão e só pega o que esta depois da vírgula.
    def terceira_forma(self):
        from time import sleep
        print()
        self.numero=int(input('Informe um número: '))
        sleep(1)
        print(f'Unidade:{self.numero // 1 % 10}.')
        sleep(1)
        print(f'Dezena:{self.numero // 10 % 10}.')
        sleep(1)
        print(f'Centena:{self.numero // 100 % 10}.')
        sleep(1)
        print(f'Milhar:{self.numero // 1000 % 10}.')
        sleep(1)
        print()

    def quarta_forma(self):
        from time import sleep
        self.number=input('Digite um número: ')
        self.number_2=self.number.replace(self.number,'000'+self.number)
        sleep(1)
        print(f'Unidade:{self.number_2[-1]}')
        sleep(1)
        print(f'Dezena:{self.number_2[-2]}')
        sleep(1)
        print(f'Centena:{self.number_2[-3]}')
        sleep(1)
        print(f'Milhar:{self.number_2[-1]}')
        sleep(1)
        print()

    def iniciar(self):
        while True:
            from time import sleep
            print('Separação de dígitos em números\n')
            sleep(0.8)
            self.primeira_forma()
            sleep(1)
            print('Separação de dígitos em números\n2ºforma: ')
            self.segunda_forma()
            sleep(1)
            print('Separação de dígitos em números\n3ºforma: ')
            self.terceira_forma()
            sleep(1)
            print('Separação de dígitos em números\n4ºforma: ')
            self.quarta_forma()
            sleep(1)
            while True:
                continuar = input('Deseja continar? [1-SIM / 2-NÃO]')
                if continuar in ['1','2']:
                    break
                else:
                    print('Entrada inválida.')
            if continuar == '2':
                break
        print(f'Fim.')

if __name__=='__main__':
    separacao=Separacao()
    separacao.iniciar()
        
        
