#variável de controle de repetição:
inicio=int(input('Digite o início: '))
fim=int(input('Difite o fim: '))
passo=int(input('Digite o passo: '))
for c in range(inicio,fim+1,passo):
    print(c)
print('FIM')

Results:
igite o início: 2
Difite o fim: 9
Digite o passo: 3
2
5
8
FIM
==============================================================================
#agora se inserirmos os comandos de entrada abaixo da estrutura inicial de repetição controlada temos:

#variável de controle de repetição:
for c in range(0,3):
    n=int(input('Digite um valor: '))
    print(c)
print('FIM')

Result:
Digite um valor: 5
Digite um valor: 4
Digite um valor: 3
FIM




