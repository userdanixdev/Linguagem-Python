# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Lista: Pares e Ímpares
# Versão 04:


def adicionar_elemento(lista):
    while True:
        try:
            numero = int(input('Digite um número para adicionar a lista: '))
            if numero % 2 == 0:
                lista[0].append(numero)
            else:
                lista[1].append(numero)
        except ValueError:
            print('Saindo da inserção de números.')                                                
            break


lista_numerica = [ [n for n in range (0,20) if n % 2 == 0] , [n for n in range (0,20) if n % 2 ==1] ]
adicionar_elemento(lista_numerica)        
