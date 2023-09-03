#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#Versão02:
#Simplificada 
#Muito cuidado com a INDENTAÇÃO, DEVE ESTAR NA FORMA CORRETA#

saque=int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n5 = n1 = 0
while True:
    if saque >=50:
        saque = saque - 50
        n50 = n50 + 1
    else:
        if saque >= 20:
          saque = saque - 20
          n20 = n20+1
        else:
             if saque>=10:
              saque = saque - 10
              n10 = n10 +1
             if saque>= 5:
              saque = saque - 5
              n5 = n5 + 1
             else:
                  if saque >=1:
                    saque = saque - 1
                    n1 = n1+1
    if saque == 0:
         break
print(f'Vc receberá {n50} notas de 50,{n20} de 20,{n10} de 10 e {n1}de 1.')

