#Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#  B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Versão 2:

dados=list()
pessoas=list()
peso_total=list()
pessoas_maior_peso=list()
pessoas_menor_peso=list()

#Inserindo dados pelo usuário

while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    proximo=input('Quer continuar?[S/N]:').strip().upper()
    if proximo in 'nN':
        break
    

# Separando todos os pesos na lista>peso_total:
for peso in pessoas:
    peso_total.append(peso[1])
# Checando o peso máximo e o mínimo:
    maior_peso = max(peso_total)
    menor_peso = min(peso_total)

# Identificando os respectivos nomes de peso max/min:
for pes in pessoas:
    if pes[1] == maior_peso:
        pessoas_maior_peso.append(pes[0])
    if pes[1] == menor_peso:
        pessoas_menor_peso.append(pes[0])
print(f'{"="*20}\n Ao todo vc cadastrou {len(pessoas)}pessoa{"s" if len(pessoas)>1 else ""}.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {pessoas_maior_peso}.')
print(f'O menor peso foi de {menor_peso}Kg. Peso de{pessoas_menor_peso}.')
        
