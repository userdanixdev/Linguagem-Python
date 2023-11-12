Exemplo simples de uma condição aninhada:

nome=str(input('Digite um nome:  '))
if nome == 'Daniel':
      print('Que nome legal, seu nome é bíblico!')
elif nome == 'Pedro' or nome== 'Maria' or nome == 'Paulo':
      print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
      print('São nomes de mulheres coroas.')
print(f'Tenha um bom dia, {nome}.')
====================================================================



