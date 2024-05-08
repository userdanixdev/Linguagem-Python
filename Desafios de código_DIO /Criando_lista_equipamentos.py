# Desafio:
# Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa.
# O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede,
# em seguida, exibir essa lista de equipamentos. 
# Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

# Criar uma lista de itens:
itens=[]
# Criar um looping para adicionar três itens:
for c in range(3):
  item = input('Insira aqui os equipamentos: ')   # Os itens seráo armazenados na variável item
  itens.append(item)  # Todos os itens armazenados na variável 'item' serão adicionados na lista 'itens'
# Exiba a lista de itens:
print('Lista de Equipamentos: ')
for item in itens: # Loop que percorre cada item da lista itens
  print(f'- {item}')
