#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
#cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
#de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Cadastro Trabalhador:
#VERSÃO 02:

from datetime import date
data_atual=date.today().year
dados={}
dados['Nome']= str(input('Nome: ')).upper()
dados['Ano de Nascimento']= int(input("Ano de Nascimento: "))
#dados['Idade']= datetime.now().year - nasc
idade=data_atual-dados['Ano de Nascimento']
dados['CTPS']= int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS']!= 0:
    dados['Contratação']= int(input('Ano de contratação: '))
    dados['Salário']= float(input('Salário: R$ '))
    dados['Sexo']= str(input('Sexo:')).upper()
    #dados['Aposentadoria']= dados['Idade']+(dados['Contratação']+35) - datetime.now().year
    if dados['Sexo']=='M'or'm':
        if idade>=61:
            print('Você tem idade para se aposentar...')
        else:
            tempo_restante=61-idade
            print(dados['Nome'],'faltam',tempo_restante,'anos para se aposentar.')
elif dados['Sexo']=='F'or'f':
    if idade>=56:
        print(dados['Nome'],'Você já tem idade para se aposentar.')                        
    else:
        tempos_restante=56-idade
        print(dados['Nome'],'faltam',tempo_restante, 'anos para se aposentar.')
else:
    print('Fim do programa')                
print(dados)
# Formatação:
for k, v in dados.items():
    print(f' {k} com o valor {v}.')
