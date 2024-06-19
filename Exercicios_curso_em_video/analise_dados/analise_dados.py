# Análise de dados:
# Versão 01:

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('Analise de dados')
total_18 = 0
homens = 0
mulheres_menores_vinte = 0
while True:
            idade=int(input('Idade: '))
            sexo = ' '
            while sexo not in 'MF':
                sexo = input('Sexo: [M/F] ').strip().upper()[0]
            if idade >= 18:
                total_18 += 1
            if sexo == 'M':
                homens += 1
            if sexo == 'F' and idade < 20:
                mulheres_menores_vinte += 1
            resp =  ' '
            while resp not in 'SN':
                resp = input('Quer continuar? [S/N] ').strip().upper()[0]
            if resp == 'N':
                break
            
print(f'Total de pessoas com mais de 18 anos: {total_18}.')
print(f' Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres_menores_vinte} mulheres com menos de 20 anos.')

