# Criando lista de equipamentos versão 02:
# Essa versão é com dicionário:

equipamentos={}
equipamentos['Nome - 1']=input('Insira o nome do equipamento: ')
equipamentos['Nome - 2']=input('Insira o nome do equipamento: ')
equipamentos['Nome - 3']=input('Insira o nome do equipamento: ')
print(equipamentos)
for i,equip in enumerate(equipamentos):
  print(f'Equipamento {i} : {equipamentos[equip]}')
  

