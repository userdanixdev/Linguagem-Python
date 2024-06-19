# Análise de dados:
# Versão 03:

contagem_homem = 0
contagem_18 = 0
contagem_mulheres_vinte = 0
while True:
    print('Cadastre uma pessoa')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [m/f] ').upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido. tente novamente')
    else:   
        if sexo == 'M' or 'F' and idade >= 18:
            contagem_18 += 1
        if sexo == 'M':
            contagem_homem +=1
        if sexo == 'F' and idade <= 20:
            contagem_mulheres_vinte += 1
    escolha=input('Quer continuar?[S/N]').upper().strip()[0]
    if escolha == 'N':
        break
    print(f'''Total de pessoas com mais de 18 anos: {contagem_18}
                Ao todo temos {contagem_homem} homens.
                Mulheres com menos de 20 anos temos {contagem_mulheres_vinte}''')
    
print(f'''Total de pessoas com mais de 18 anos: {contagem_18}
                Ao todo temos {contagem_homem} homens.
                Mulheres com menos de 20 anos temos {contagem_mulheres_vinte}''')
            
