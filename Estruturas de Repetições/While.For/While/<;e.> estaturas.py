#Construa um programa que receba uma lista contendo a estatura dos alunos.
#Crie um relatório que informe a:
#a.menor estatura
#b.maior estatura
#c.média das estaturas informadas

estatura=float(input('Estatura do aluno: '))
menor=estatura
maior=estatura
soma_estatura=0
soma_estatura += estatura
cont = 1
while True:
    estatura=float(input('Estatura do aluno: '))
    if estatura < 0:   # se for menor que 0 , laço será interrompido.
        break
    if estatura<menor:
        menor=estatura
    elif estatura>maior:
        maior=estatura
    cont +=1
    soma_estatura += estatura
print(f'{maior}m é a maior estatura. ')
print(f'{menor}m é a menor estatura. ')
media=soma_estatura/cont
print(f'Média das estaturas= {media}m. ')

Result:

Estatura do aluno: 1.75
Estatura do aluno: 1.79
Estatura do aluno: 1.79
Estatura do aluno: 1.80
Estatura do aluno: 1.74
Estatura do aluno: 1.84
Estatura do aluno: 0
Estatura do aluno: -85
1.84m é a maior estatura. 
0.0m é a menor estatura. 
Média das estaturas= 1.5299999999999998m. 
=========================================================

