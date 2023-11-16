
# EXTRAINDO DADOS DA UMA LISTA

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
 #   A) Quantos números foram digitados.
 #   B) A lista de valores, ordenada de forma decrescente.
 #   C) Se o valor 5 foi digitado e está ou não na lista.

 # Versão 03 #

contador = 0
resposta = 's'
lista=[]
while resposta.lower()=='s':   # Se for qualquer outro caracter que não seja 's', o programa irá fechar
    lista.append(int(input('Digite um valor: ')))
    resposta = input('Quer continuar? [S/N]').lower()
    contador =  contador + 1
lista.sort(reverse=True)
print(f'Vc digitou {contador} elementos.\n E os valores em ordem decrescente foram: {lista}).')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não foi encontrado.')
                 
                 
