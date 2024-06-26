# Para converter o código do modelo funcional em um formato POO, podemos encapsular as funções e dados em uma classe.
# Lista Composta: Versão POO

class ListaComposta:
    def __init__ (self):

        self.pessoas = []
    
    def input_nome(self):
        while True:
            nome = input('Nome: ')
            if nome.isalpha():
                return nome
            else:
                print('Somente letras são permitidas.')

    def input_peso(self):
        while True:
            try:
                peso = float(input('Insira o peso: '))
                return peso
            except ValueError:
                print('Somente valores numéricos.')

    def lista_composta_1(self):
        pessoas = []
        while True:
            nome = self.input_nome()
            peso = self.input_peso()
            pessoas.append([nome,peso])
            while True:
                continuar = input('Quer continuar? [S/N]').strip().lower()[0]
                if continuar in ('s','n'):
                    break
                else:
                    print('Somente S para continuar ou N p/ parar.')
            if continuar == 'n':
                break
        print(f'\n Ao todo você cadastrou {len(pessoas)}\n')                                
        maior_peso = max([p for n, p in pessoas])
        print(f'O maior peso foi de {maior_peso:.1f}KG.'f'Peso de {[n for n,p in pessoas if p == maior_peso]}\n')
        menor_peso = min([p for n, p in pessoas])
        print(f'\nO menor peso foi de {menor_peso:.1f}KG.'f'Peso d {[n for n,p in pessoas if p == menor_peso]}\n')

    def lista_composta_2(self):
            lista_temp = []
            lista_prin = []
            maior_peso = 0
            menor_peso = 0

            while True:
                lista_temp.append(self.input_nome())
                lista_temp.append(self.input_nome())
                if len(lista_prin) == 0:
                    maior_peso = menor_peso = lista_temp[1]
                else:
                    if lista_temp[1] > maior_peso:
                        maior_peso = lista_temp[1]
                    if lista_temp[1] < menor_peso:
                        menor_peso = lista_temp[1] 
                lista_prin.append(lista_temp[:])
                lista_temp.clear()
                while True:
                        resposta = input('Quer continuar? [S/N]')
                        if resposta in 'Nn':
                            break
                        elif resposta in 'Ss':
                            break
                        else:
                            print('Somente S para continuar ou N para parar.')                                                                   
                if resposta in 'nN':
                    break
                return lista_prin, maior_peso, menor_peso

    def lista_composta_2_exibicao(self,lista_prin,maior_peso,menor_peso):

        print(f'\n Os dados foram: {lista_prin}.\nAo todo você cadastrou {len(lista_prin)} principal.')
        print(f'O maior peso foi de {maior_peso}KG.\nO menor peso foi de {menor_peso}KG.')
        print(f'O maior peso foi de: ',end='')
        for p in lista_prin:
            if p[1] == maior_peso:
                print(f'[{p[0]}]')
        print(f'O menor peso foi de: ',end='')
        for p in lista_prin:
            if p[1] == menor_peso:
                print(f'[{p[0]}]') 

    def lista_composta_3_init(self):

        pessoas_temp = [] 
        pessoas = []
        pesados = []
        leves = []

        while True:
            nome =  input('Nome: ')
            while not nome.isalpha():
                print('Nome deve conter somente letras')
                nome = input('Nome: ')
            while True:
                try:
                    peso = float(input('Peso: '))                
                    break
                except ValueError:
                    print('Peso deve ser um número válido.')
            self.lista_composta_3_processamento(pessoas_temp,pessoas,nome,peso,leves,pesados)
            if not self.lista_composta_3_saida():
                break
        self.lista_composta_3_exibicao(pesados,leves,pesados)

    def lista_composta_3_processamento(self,pessoas_temp,pessoas,nome,peso,leves,pesados):                        
        pessoas_temp.append(nome)
        pessoas_temp.append(peso)
        pessoas.append(pessoas_temp.copy())

        if peso >= 100:
            pesados.append(nome)
        if peso <= 70:
            leves.append(nome)

        pessoas_temp.clear()                        

    def lista_composta_3_saida(self):

        while True:
            resposta = input('Quer continuar? [S/N]').strip().lower()
            if resposta == 's':
                return True
            elif resposta == 'n':
                return False
            else:
                print('Resposta inválida. Digite S para sim e N para não.')

    def lista_composta_3_exibicao(self,pesados,leves,pessoas):

        print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
        print(f'Pessoas acima de 100KG: {pesados}')
        print(f'Pessoas abaixo de 70KG? {leves}')

    def menu(self):

        while True:
            try:
                menu = '''
        
        [1] -\tLista Composta - Versão 1 
        [2] -\tLista Composta - Versão 2
        [3] -\tLista Composta - Versão 3
        [4] -\tExecutar Tudo - 
        [5] -\tSair
         \nEscolha:  '''
                opcao = int(input(menu))
                if opcao in [1,2,3,4,5]:
                    return opcao 
                else:
                    print('Opção inválida. Somente entre os números 1 a 5.')                        
            except ValueError:
                print('Opção inválida. Inserir somente números inteiros.')                    

    @staticmethod
    def sair():
        import sys
        exit()
    def main(self):
        while True:
            try:
                opcoes = self.menu()
                if opcoes == 1:
                    print(f'{"+"*30}\n{"Lista Composta":^28}\n{"+"*30}')
                    self.lista_composta_1()
                elif opcoes == 2:
                    print(f'{"+"*30}\n{"Lista Composta - 2":^28}\n{"+"*30}')                                                    
                    lista_prin, maior_peso,menor_peso = self.lista_composta_2()
                    self.lista_composta_2_exibicao(lista_prin,maior_peso,menor_peso)                    
                elif opcoes == 3:
                    print(f'{"+"*30}\n{"Lista Composta - 3":^28}\n{"+"*30}')                    
                    self.lista_composta_3_init()
                elif opcoes == 4:
                    print(f'{"+"*30}\n{"Lista Composta":^28}\n{"+"*30}')                    
                    self.lista_composta_1()
                    print(f'{"+"*30}\n{"Lista Composta - 2 ":^28}\n{"+"*30}')
                    lista_prin,maior_peso,menor_peso = self.lista_composta_2()
                    self.lista_composta_2_exibicao(lista_prin,maior_peso,menor_peso)
                    print(f'{"+"*30}\n{"Lista Composta - 3":^28}\n{"+"*30}')
                    self.lista_composta_3_init()
                elif opcoes == 5:
                    self.sair()
                else:
                    print('Opção inválida.')                                        
            except ValueError:
                print('Somente números inteiros são permitidos.')

if __name__ == '__main__':
    lista=ListaComposta()
    lista.main()

