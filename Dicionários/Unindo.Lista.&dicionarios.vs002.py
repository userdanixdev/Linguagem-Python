#Unindo dicionários e listas

#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários
#em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

#VERSÃO 002:

pessoas={}  # Dicionário pessoas
cadastro={} # Dicionário cadastro
total = 0
while True:
    cadastro['Nome']=input('Nome: ').capitalize() # Chave criada que recebe um valor do usuário
    while True:  # Um looping infinito após o outro para validação do sexo em que uma variável sexo deverá ser inserida pelo usuário 
        sexy=input('Sexo: ').upper()
        if sexy in 'MF':          # Condicional se a variável receber os caracteres 'MF', o dicionário cadastro recebe uma chave e o valor a variável inserida com o valor efetuado pelo usuário 
            cadastro['Sexo']=sexy # 
            break
        else:
            print('Erro. Responda apenas M ou F.')
            continue
    cadastro['idade']=int(input('Idade: '))   # Dicionário cadastro recebe 'idade' para o usuário digitar.
    pessoas[cadastro["Nome"]]=cadastro.copy() # Acessa o valor da chave 'nome' do dicionário cadastro. Mas o dicionário pessoas usa o dicionário e cria uma cópia
    while True:  # Looping infinito para variável de controle
        resp=input('Quer continuar?[S/N]: ').upper() # Criação de uma variável de controle
        if resp in 'SN':   
            break
        print('Erro. Responda apenas S ou N.')
    if resp in 'N':
        break
print(f' A) Ao todo foram cadastradas {len(pessoas)} pessoas.')
for chave, valor in pessoas.items():   # A função items irá retornar uma visão dos pares chave-valor no dicionário.
    total += valor['idade']            # A chave 'idade' irá acessar o valor adicionado um acumulador tot, variável para acumular soma das idades
media=total/len(pessoas)               # Calculo da média declarada em uma variável
print(f' B) A média da idade é: {media:.2f}')
print(f' C) As mulheres cadastradas foram: ')
for k,v in pessoas.items(): 
    if v['Sexo'] in 'F':             # Acessa o valor associado à chave 'sexo' 
        print(f'{k,}',end='')        # Saída que 'k' é o nome da pessoa.
print()

print(f' Lista das pessoas que estão acima da média: ')
for key, value in pessoas.items():   # O looping irá percorrer a chave e o valor do dicionário. 
    if value['idade']>=media:        # Condicional acessa o valor associado a 'idade' se for maior ou igual a média. 
        print(f'Nome={key};sexo={value["Sexo"]};idade={value["idade"]};')
        
        
        
    

        
      


