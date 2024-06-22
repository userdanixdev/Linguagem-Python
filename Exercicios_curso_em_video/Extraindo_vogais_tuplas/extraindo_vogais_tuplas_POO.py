# Extraindo vogais de uma tupla:
# POO: Versão 01

class Extraindo_vogais:
    def __init__(self):
        self.palavras =('aprender','programar','linguagem','python','curso',
                        'gratis','estudar','praticar','trabalhar','mercado',
                        'programador','futuro')
        self.vogais =  ('a','e','i','o','u')

    def programa_1(self):

        for p in self.palavras:
            print(f'\nNa palavra {p.upper()} temos: ',end='')
            for letra in p:
                if letra.lower() in 'aeiou':
                    print(letra,end='/')

    def programa_2(self):

        for p in range(0,len(self.palavras)):
            for c in range(0,len(self.palavras[p])):
                if c == 0:
                    print(f'\nNa palavra {self.palavras[p].upper()} temos: ',end='/')
                if self.palavras[p][c] in 'aeiou':
                    print(f'{self.palavras[p][c]}',end='/')

    def programa_3(self):

        for palavra in self.palavras:
            print(f'\nNa palavra {palavra.upper()} temos: ',end='/')
            for letra in palavra:
                if letra.lower() in self.vogais:
                    print(letra,end='/')

    def programa_4(self):

        contagem = 0        # contador para númeral
        vogais_find = ''    # contador de strings
        for c in range(0,len(self.palavras)):
            for d in range(0,len(self.palavras[c])):
                if self.palavras[c][d] in self.vogais:
                    contagem += 1
                    vogais_find += self.palavras[c][d]
            print(f'Na palavra: {self.palavras[c]} tem {contagem} vogais. São elas: {vogais_find}')
            contagem = 0    # Sempre zerar a contagem para não somar as vogais
            vogais_find = '' # Sempre zerar as strings para não somar
            

    def opcoes(self):

        opcao=int(input('''

                Extraindo vogais de uma tupla:
                
                [1] - Programa 1 -
                [2] - Programa 2 -
                [3] - Programa 3 - 
                [4] - Programa 4 -
                [5] - Executar tudo -
                [6] - Sair
                Digite a opção:
                '''))

        if opcao == 1:
                  self.programa_1()
        if opcao == 2:
                  self.programa_2()
        if opcao == 3:
                  self.programa_3()
        if opcao == 4:
                  self.programa_4()
        if opcao == 5:
                  self.iniciar()
        if opcao == 6:
                  self.sair_programas()

    





if __name__== "__main__":

    extract=Extraindo_vogais()
    extract.opcoes()
    

        

                    

        
                    
        
