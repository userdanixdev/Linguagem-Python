#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada,o programa deverá perguntar se o usuário quer ou não
#continuar. No final mostre:
#A - Quantas pessoas tem mais de 18 anos;
#B - Quantos homens foram cadastrados;
#C - Quantas mulheres tem menos de 20 anos.


tot18 = man_total = woman_total= 0
while True:                     #<-    # loop infinito
    idade=int(input('Idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=input('Sexo?[M/F] ').strip().upper()[0]
    if idade>=18:
        tot18 =  tot18 + 1
    if sexo == 'M':
        man_total = man_total + 1
    if sexo == 'F' and idade<20:
        woman_total= woman_total + 1        
    resposta=' '    
    while resposta not in 'SN':
        resposta=input('Quer continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N'and'n':
        break
print(f'Total de pessoas com mais de 18 ans: {tot18}')
print(f'Ao todo temos {man_total} homens cadastrados.')
print(f'Ao todo temos {woman_total} mulheres com menos de 20 anos.')

Results:

Idade: 22
Sexo?[M/F] m
Quer continuar? [S/N] s
Idade: 16
Sexo?[M/F] f
Quer continuar? [S/N] s
Idade: 12
Sexo?[M/F] m
Quer continuar? [S/N] n
Total de pessoas com mais de 18 ans: 1
Ao todo temos 2 homens cadastrados.
Ao todo temos 1 mulheres com menos de 20 anos.
==============================================================================

