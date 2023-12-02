#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
#cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
#de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Cadastro Trabalhador:

from datetime import datetime
dados={}
dados['Nome']= str(input('Nome: '))
nasc= int(input("Ano de Nascimento: "))
dados['Idade']= datetime.now().year - nasc
dados['CTPS']= int(input('Carteira de Trabalho (0 não tem): '))
#print(dados)
#REsultado no console:
#Nome: Daniel
#Ano de Nascimento: 1995
#Carteira de Trabalho (0 não tem): 22346
#{'Nome': 'Daniel', 'Idade': 28, 'CTPS': 22346}
if dados['CTPS']!= 0:
    dados['Contratação']= int(input('Ano de contratação: '))
    dados['Salário']= float(input('Salário: R$ '))
    dados['Aposentadoria']= dados['Idade']+(dados['Contratação']+35) - datetime.now().year
print(dados)
# Formatação:
for k, v in dados.items():
    print(f' {k} com o valor {v}.')
    
