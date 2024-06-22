# Análise de dados:

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# Versão POO: As 3 versões encapsuladas, loop único e menu.

class Analise_Dados:
    def __init__(self):

        print('Analise de dados.')
        self.total_18 = 0
        self.homens = 0
        self.mulheres_menores_vinte = 0
        self.idade = 0
        self.sexo = ' '
        self.resp = ' '

    def programa_1(self):

        while True:
            try:
                    self.idade=int(input('Idade: '))
                    self.sexo=' '
                    while self.sexo not in 'MF':
                        self.sexo = input('Sexo: [M/F]: ').strip().upper()[0]
                    if self.idade >= 18:
                        self.total_18 += 1
                    if self.sexo == 'M':
                        self.homens += 1
                    if self.sexo == 'F' and self.idade < 20:
                        self.mulheres_menores_vinte += 1
                    self.resp = ' '
                    while self.resp not in 'SN':
                        self.resp = input('Quer continuar? [S/N]').strip().upper()[0]
                    if self.resp == 'N':
                        break
            except ValueError:
                print('Por favor, insira a idade válida.')

    def programa_1_exibir_dados(self):

        print(f'Total de pessoas com mais de 18 anos: {self.total_18}.')
        print(f'Ao todo temos  {self.homens} homens cadastrados.')
        print(f'E temos {self.mulheres_menores_vinte} mulheres com menos de 20 anos.')

    def programa_2(self):

        self.m = 0
        self.f = 0
        self.maiores = 0
        while True:
            print('Cadastro')
            self.idade = int(input('Digite sua idade: '))
            while self.idade < 1 or self.idade > 150:
                print('Digite uma idade entre 1 a 150.')
                self.idade = int(input('Digite a sua idade: '))
            if self.idade >= 18:
                self.maiores += 1
            self.sexo=input('Qual o seu sexo? ').strip().upper()[0]
            while self.sexo not in 'MF':
                print('Digite a opção correta.')
                self.sexo = input('Qual o seu sexo? [M/F]: ').strip().upper()[0]
            if self.sexo == 'M':
                self.m += 1
            elif self.sexo == 'F' and self.idade < 20:
                self.f += 1
            print()
            continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
            while continuar not in 'SN':
                print('Opção inválida.')
                continuar = input('Deseja continuar? ').strip().upper()[0]
            if continuar == 'N':
                break

    def programa_2_exibir_dados(self):

        print(f'{self.maiores} pessoas são maiores de 18 anos.\n{self.f} são mulheres com menos de 20 anos.\n{self.m} são homens.')

    def programa_3(self):

        self.contagem_homem=0
        self.contagem_18=0
        self.contagem_mulheres_vinte=0
        while True:
            print('Cadastre uma pessoa: ')
            self.idade=int(input('Idade: '))
            self.sexo=input('Sexo: [M/F] ').upper().strip()[0]
            if self.sexo not in 'MF':
                print('Sexo inválido. Tente novamente.')
            else:
                if self.idade >= 18:
                    self.contagem_18 += 1
                if self.sexo == 'M':
                    self.contagem_homem += 1
                if self.sexo == 'F' and self.idade < 20:
                    self.contagem_mulheres_vinte += 1
            escolha = input('Quer continuar: [S/N] ').upper().strip()[0]
            if escolha == 'N':
                break

    def programa_3_exibir_dados(self):

        print(f'''
                Total de pessoas com mais de 18 anos: {self.contagem_18}
                Ao todo temos {self.contagem_homem} homens.
                Mulheres com menos de 20 anos temos {self.contagem_mulheres_vinte}''')

    
    def repetir_operacoes(self,programa,exibir_dados):

        while True:
                try:
                    continuar = int(input('''

                            Repetir a operação ou sair?
                    [1] - Repetir                    
                    [2] - Sair
                    '''))
                    
                    if continuar == 1:
                         programa()
                         exibir_dados()
                    elif continuar == 2:
                        self.menu()
                        break
                    else:
                        print('Opção inválida. Somente 1 para repetir ou 2 para sair.')
                except ValueError:
                    print('Entrada inválida. Por favor, somente os números (1 e 2).')

    def menu(self):

        opcoes=int(input('''

                [1] - Programa 1 
                [2] - Programa 2
                [3] - Programa 3
                [4] - Sair
                
                
                '''))

        if opcoes == 1:
            self.programa_1()
            self.programa_1_exibir_dados()
            self.repetir_operacoes(self.programa_1,self.programa_1_exibir_dados)
        if opcoes == 2:
            self.programa_2()
            self.programa_2_exibir_dados()
            self.repetir_operacoes(self.programa_2,self.programa_2_exibir_dados)
        if opcoes == 3:
            self.programa_3()
            self.programa_3_exibir_dados()
            self.repetir_operacoes(self.programa_3,self.programa_3_exibir_dados)
        if opcoes == 4:
            self.sair()


                    
    @staticmethod
    def sair():
        import os
        exit()


if __name__=='__main__':
    analise=Analise_Dados()
    analise.menu()
                                    


                

        
