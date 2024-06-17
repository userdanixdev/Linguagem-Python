# Sorteando um item na lista:

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo
# o nome do escolhido.

# POO:  Versão 03
# Métodos aprimorados:
  # Validações das letras, lsita embaralhada na tela


class Sorteio:
    def __init__(self):
        self.n1=''
        self.n2=''
        self.n3=''
        self.n4=''
        self.nome = ''

    def obter_valores(self):
        import random
        while True:
            self.n1 =input('Primeiro aluno: ')
            if self.n1.isalpha() and len(self.n1) >= 4:
                break
            else:
                print('Por favor,insira um nome válido.(somente letras)(minimo 4).')
        while True:
            self.n2=input('Segundo aluno: ')
            if self.n2.isalpha()and len(self.n2) >= 4:
                break
            else:
                print('Por favor, insira um nome válido. Somente letras(minimo 4).')
        while True:
            self.n3=input('Terceiro aluno: ')
            if self.n3.isalpha()and len(self.n3) >= 4:
                break
            else:
                print('Por favor, insira um nome válido. Somente letras(minimo 4).')
        while True:
            self.n4=input('Quarto aluno: ')
            if self.n4.isalpha() and len(self.n4) >= 4:
                break
            else:
                print('Por favor, insira um nome válido. somente letras(minimo 4).')
        lista = [self.n1, self.n2, self.n3, self.n4]
        escolhido = random.choice(lista)
        print("O aluno escolhido foi:", escolhido)

    def obter_valores_2(self):
        import random
        def validate_name(prompt):
            while True:
                name=input(prompt).strip()
                if name.isalpha() and len(name) >= 4:
                    return name
                else:
                    print('Por favor,insira um nome válido(somente letras e mínimo 4 letras).')
        self.n1 = validate_name('Primeiro aluno: ')
        self.n2 = validate_name('Segundo  aluno: ')
        self.n3 = validate_name('Terceiro aluno: ')
        self.n4 = validate_name('Quarto aluno: ')
        lista = [self.n1, self.n2, self.n3, self.n4]
        random.shuffle(lista)
        print('Lista embaralhada:',lista)
        escolhido = random.choice(lista)
        print("O aluno escolhido foi:", escolhido)
        
    def obter_valores_second(self):
        import random
        def validate_name(prompt):
            while True:
                name=input(prompt).strip()
                if name.isalpha():
                    return name
                else:
                    print('Por favor,insira um nome válido, somente letras e no mínimo 4.')
        self.nome=[validate_name('Digite um nome: ')for i in range(4)]
        random.shuffle(self.nome)
        print('Lista embaralhada:',self.nome)
        escolha=random.choice(self.nome)
        print('O nome sorteado foi: ',escolha)

    def obter_valores_third(self):
        import random
        def validate_name(prompt):
            while True:
                names_input=input(prompt).strip()
                names = names_input.split(',')
                if all(name.strip().isalpha() and len(name.strip()) >= 4 for name in names):
                    return [name.strip() for name in names]
                else:
                    print('Por favor,insira um nome válido, somente letras ou no mínimo 4.')
        alunos=validate_name('Nome dos alunos separados por vírgula: ')
        if alunos:
            random.shuffle(alunos)
            print('Lista embaralhada:',alunos)
            escolhido = random.choice(alunos)
        print(f'O nome do aluno sorteado foi: {escolhido}')

    def iniciar(self):
        while True:
            print(f'{'+'*15}\n{"SORTEIO":^14}\n{"1ºforma":^14}\n{'+'*15}')
            self.obter_valores_2()
            print()
            print(f'{'+'*15}\n{"SORTEIO":^14}\n{"2ºforma":^14}\n{'+'*15}')
            self.obter_valores_second()
            print()
            print(f'{'+'*15}\n{"SORTEIO":^14}\n{"3ºforma":^14}\n{'+'*15}')
            self.obter_valores_third()
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
