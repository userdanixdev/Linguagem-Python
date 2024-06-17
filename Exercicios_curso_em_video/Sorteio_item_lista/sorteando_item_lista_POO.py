# Sorteando um item da lista: POO

class Sorteio:
    def __init__(self):
        self.n1=''
        self.n2=''
        self.n3=''
        self.n4=''
        self.nome = ''
    def obter_valores(self):
        import random
        self.n1=input('Primeiro aluno: ')
        self.n2=input('Segundo aluno: ')
        self.n3=input('Terceiro aluno: ')
        self.n4=input('Quarto aluno: ')
        lista=[n1,n2,n3,n4]
        escolhido = random.choice(lista)
        print('O aluno escolhido foi, ',escolhido)
    def obter_valores_second(self):
        self.nome=[input('Digite um nome: ')for i in range(4)]
        escolha=random.choice(self.nome)
        print('O nome sorteado foi: ',escolha)

    def obter_valores_third(self):
        alunos=input('Nome dos alunos separados por vírgula: ').split(',')
        print(f'O nome dos alunos foi: {random.choice(alunos)}')

    def iniciar(self):
        while True:
            obter_valores()
            print()
            obter_valores_second()
            print()
            obter_valores_third()
            print()
            while True:
                continuar = input('Deseja continuar [1-SIM / 2-NÃO]')
                if continuar in ['1','2']:
                    break
                else:
                    print('Entrada inválida.')
            if continuar == '2':
                break
        print(f'Fim.')            

if __name__ == '__main__':
    sorteio=Sorteio()
    sorteio.iniciar()
