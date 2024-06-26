# Modelo funcional de todas as versões da pasta:

pessoas = []

def input_nome():

    while True:
        nome = input('Nome: ')
        if nome.isalpha():
            return nome
        else:
            print('Somente letras são permitidas.')

def input_peso():

    while True:
            try:
                peso = float(input('Insira o peso: '))
                return peso
            except ValueError:
                 print('Somente valores numéricos são permitidos.')


def lista_composta_1():
     
    pessoas = []
    while True:
          nome = input_nome()
          peso = input_peso()
          pessoas.append([nome,peso])
          while True:
               continuar = input('Quer continuar? [S/N]').strip().lower()[0]
               if continuar in ('s','n'):
                    break
               else:
                    print('Somente S para continuar ou N para parar...')
          if continuar == 'n':
               break
    print(f'\nAo todo você cadastrou {[len(pessoas)]}\n')                                          
    maior_peso = max([p for n,p in pessoas])
    print(f'O maior peso foi de {maior_peso:.1f}KG.',end='')
    print(f'Peso de {[n for n,p in pessoas if p == maior_peso]}\n')
    menor_peso = min([p for n,p in pessoas])
    print(f'O menor peso foi de {menor_peso:.1f}KG.',end='')
    print(f'Peso de {[n for n,p in pessoas if p == menor_peso]}')

def lista_composta_2(lista_prin,maior_peso,menor_peso):

     lista_temp = []
     lista_prin = []
     maior_peso = 0
     menor_peso = 0

     while True:
          lista_temp.append(input_nome())
          lista_temp.append(input_peso())
          if len(lista_prin) == 0:
               maior_peso = menor_peso = lista_prin[1]
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
                         print('Somente S para Continuar ou N para parar.')
               if resposta in 'Nn':
                break       
     return lista_prin,maior_peso,menor_peso                                    

def lista_composta_2_exibicao(lista_prin,maior_peso,menor_peso):

     print(f'\nOs dados foram: {lista_prin}.') 
     print(f'\n Ao todo você cadastrou {len(lista_prin)} principal.')
     print(f'O maior peso foi de {maior_peso}KG.') 
     print(f'O menor peso foi de {menor_peso}KG.')
     print(f'O maior peso foi de : ',end='')
     for p in lista_prin:
          if p[1] == maior_peso:
               print(f'[{p[0]}]')
     print(f'O menor peso foi de {menor_peso}KG. Peso de ', end='')               
     for p in lista_prin:
          if p[1] == menor_peso:
               print(f'[{p[0]}]')                

def lista_composta_3():
     
    pessoas_temp = []
    pessoas = []
    pesados = []
    leves = []

    while True:
         nome = input('Nome: ')
         while not nome.isalpha():
              print('Nome deve conter apenas letras.')
              nome = input('Nome: ')
         while True:
              try:
                   peso = float(input('Peso: '))              
                   break
              except ValueError:
                   print('Peso deve ser um número válido.')
         lista_composta_3_processamento(pessoas_temp, pessoas, nome, peso, leves, pesados)
         if not lista_composta_3_saida():
              break
    lista_composta_3_exibicao(pesados,leves,pessoas)              
                  

def lista_composta_3_processamento(pessoas_temp,pessoas,nome,peso,pesados,leves):

    pessoas_temp.append(nome)
    pessoas_temp.append(peso)        
    pessoas.append(pessoas_temp.copy())

    if peso <= 100:
        pesados.append(nome)
    elif peso <= 70:
        leves.append(nome)            

    pessoas_temp.clear()

def lista_composta_3_saida():

     while True:
          resposta = input('Quer continuar? [S/N]').strip().lower()
          if resposta == 's':
               return True
          elif resposta == 'n':
               return False
          else:
               print('Resposta inválida. Digite S para SIM  e N para não.')
     
def lista_composta_3_exibicao(pesados,leves,pessoas):

     print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
     print(f'Pessoas acima de 100KG: {pesados}')
     print(f'Pessoas abaixo de 70KG: {leves}')        

def menu():
    while True:
        try:
            menu='''
            +++++ MENU +++++
    [1] -\tLista Composta - Versão 1 
    [2] -\tLista Composta - Versão 2
    [3] -\tLista Composta - Versão 3
    [4] -\tExecutar Tudo - 
    [5] -\tSair
     \nEscolha:    '''
            opcao = int(input(menu))
            if opcao in [1,2,3,4,5]:
                 return opcao
            else:
                 print('Opção inválida. Escolha um número entre 1 e 5.')
        except ValueError:
            print('Opção inválida.Insira somente números inteiros.')    

def main():

     while True:
         try:                    
            opcoes = menu()
            if opcoes == 1:
                lista_composta_1()
            if opcoes == 2:
                lista_prin,maior_peso,menor_peso = lista_composta_2
                lista_composta_2_exibicao(lista_prin,maior_peso,menor_peso)
            if opcoes == 3:
                 lista_composta_3()              
                    
            if opcoes == 4:
                 pass
            if opcoes == 5:
                 break       
            else:
                 print('Opção inválida.')          
         except ValueError:
              print('Somente números inteiros são permitidos.')
                                                


