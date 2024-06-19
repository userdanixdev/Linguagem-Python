# Classificando Atletas:
# POO: Versão 01
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
        elif seelf.idade > 19 and self.idade <= 25:
            print('Categoria: Sênior.')
        else:
            print('Categoria: Master.')

    def iniciar(self):
        while True:
            print('Classificando atletas.')
            self.programa_1_obter_dados()
            self.programa_1_exibir_dados()
            while True:
                continuar = input('Deseja repetir o processo? [1-SIM / 2-Não]: ')
                if continuar in ['1','2']:
                    break
                else:
                    print('Digite o comando válido. 1 ou 2.')
            if continuar == '2':
                break
            print('Fim.')

        
 if __name__=='__main__':
    classificando=Classificando_Atletas()
    classificando.iniciar()



    
