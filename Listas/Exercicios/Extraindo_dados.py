# EXTRAINDO DADOS DA UMA LISTA

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
 #   A) Quantos números foram digitados.
 #   B) A lista de valores, ordenada de forma decrescente.
 #   C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
while True:    ## LOOP WHILE PARA VARIOS VALORES infinitos ##
     valores.append(int(input('Digite o valor: ')))
     resp = input('Quer continuar? [S/N] ')
     if resp in 'Nn':
         break
        # Quantos números foram digitados? Logo abaixo:
print(f'Você digitou {len(valores)} elementos.')
    # Lista em ordem descrescente:
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}. ')
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista.')
     
     
                    
