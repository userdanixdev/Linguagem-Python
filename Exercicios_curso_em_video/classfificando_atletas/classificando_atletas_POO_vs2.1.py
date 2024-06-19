# Classificando atletas:
# POO: Versão 2.1:

class Classificando_Atletas:
    def __init__(self):
        
        self.nasc = 0
        self.idade = 0
        
    def programa_1_obter_dados(self):
        
        from datetime import date
        atual = date.today().year
        self.nasc=int(input('Qual o ano do seu nascimento? '))
        self.idade = atual - self.nasc

    def programa_1_exibir_dados(self):
        
        print(f'Sua idade é de {self.idade} ano(s).')
        if self.idade <= 9:
            print('Categoria: MIRIM.')
        elif self.idade > 9 and self.idade <=14:
            print('Categoria: Infantil.')
        elif self.idade > 14 and self.idade <=19:
            print('Catgoria: Junior')
        elif self.idade > 19 and self.idade <= 25:
            print('Categoria: Sênior.')
        else:
            print('Categoria: Master.')

    def iniciar(self):
        while True:
            print('Classificando atletas.\n')
            self.programa_1_obter_dados()
            self.programa_1_exibir_dados()
            print('\nClassificando atletas: Versão 02\n')
            self.programa_2_obter_dados()
            self.programa_2_variaveis_()
            self.programa_2_calculo_idade()
            self.programa_2_exibir_dados()
            while True:
                continuar = input('Deseja repetir o processo? [1-SIM / 2-Não]: ')
                if continuar in ['1','2']:
                    break
                else:
                    print('Digite o comando válido. 1 ou 2.')
            if continuar == '2':
                break
        print('Fim.')

    def programa_2_obter_dados(self):
        
        while True:
                try:
                    nascimento=input('Informe sua data de nascimento(dd/mm/aaaa): ')
                    self.dia,self.mes,self.ano=map(int,nascimento.split('/'))
                    if len(nascimento) == 10 and nascimento[2] == '/' and nascimento[5] == '/':
                        break
                    else:
                        print('Formato incorreto. Insira o formato correto: dd/mm/aaaa.')
                except ValueError:
                    print('Insira uma entrada válida.')
                    
    def programa_2_variaveis_(self):
        
        self.mirim = range(0,10)
        self.infantil = range(11,15)
        self.junior = range(16,20)
        self.senior = range(21,25)
        
    def programa_2_calculo_idade(self):
        
        from datetime import date
        self.ano = self.ano
        self.mes = self.mes
        self.dia = self.dia
        self.hoje = date.today()
        self.idade = self.hoje.year - self.ano - ((self.hoje.month,self.hoje.day)<(self.mes,self.dia))

    def programa_2_exibir_dados(self):
        
        print(f'A idade é {self.idade}.')
        if self.idade in self.mirim:
           print('Atleta Mirim')
        elif self.idade in self.infantil:
           print('Atleta Infantil')
        elif self.idade in self.junior:
           print('Atleta Junior')
        elif self.idade in self.senior:
           print('Atleta Sênior')
        else:
           print('Atleta Master')
        

if __name__=='__main__':
    classificando=Classificando_Atletas()
    classificando.iniciar()



    
