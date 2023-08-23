#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa mostre a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade=0
mediaidade=0
totmulher20=0
maioridadehomem=0
for p in range(1,5):
    print(f'---------{p}ªpessoa ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade+=idade
    if p ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadedehomem = idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher20+= 1        
mediaidade=somaidade/4
print(f'A média da idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} com menos de 20 anos de idade. ')

Result:

---------1ªpessoa ---------
Nome: jessica
Idade: 23
Sexo [M/F]: f
---------2ªpessoa ---------
Nome: claudio
Idade: 12
Sexo [M/F]: m
---------3ªpessoa ---------
Nome: pedro
Idade: 150
Sexo [M/F]: m
---------4ªpessoa ---------
Nome: maria
Idade: 55
Sexo [M/F]: m
A média da idade do grupo é de 60.0 anos.
O homem mais velho tem 0 e se chama maria.
Ao todo são 0 com menos de 20 anos de idade. 
=========================================================================



