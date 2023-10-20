#num=(2,5,9,1)
#num[2]=3
#print(num)
#Resultado:
#    TypeError: 'builtin_function_or_method' object does not support item assignment
#Obs: a tupla é imutável.

# Agora entre colchetes é uma lista tornando-se multável.
num=[2,5,9,1]
num[2]=3
print(num)
Result: [2, 5, 3, 1] # LISTA MUTÁVEL.
print('='*15)

# Usando alguns métodos na prática:
num.append(7) #---> Adicionar VALOR 7 AO ELEMENTO.
#num.sort() #---> Coloca em ordem.
print(num)
Result: [1, 2, 3, 5, 7]
print('='*15)
num.sort(reverse=True)  # Reposiciona os valores na ORDEM INVERSA
print(num)
print('='*15)
Result: [7, 5, 3, 2, 1]
# Utilizando o contador de elementos 'len':
print(f'Esse lista tem {len(num)} elementos.')
'''Result: Essa lista tem 5 elementos.'''
# Adicionar valores:
print('+'*15)
num.insert(2,0)  # Seleciona em qual lugar o elemento deve estar , no exemplo a seguir o elemento '0' irá ficar na posição '2' da lista
print(num)
'''Resultado: [7, 5, 0, 3, 2, 1] '''
print('='*15)
------------------------------------------------------------------
# Para remoção de elementos:
num.pop()  #'''---- Irá por padrão, eliminar o último elementos''' , TAMBÉM A POSSIBILIDADE DE ESCOLHER QUAL ELEMENTO COMO PARÂMETRO 
                                                                        # ACRESCENTADO DA VÍRGULA
print(num)
'''Resultado: [7, 5, 0, 3, 2] '''
print('='*15)
num.remove(2) #----> Elimina da esquerda pra direita. Elimina o primeiro elemento da lista.
print(num)
''' Resultado: [7, 5, 0, 3] '''
print('='*15)
'''num.remove(4)'''  #----> O 4 não está na lista, irá dar erro. Então:
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
'''Resultado:     Não achei o número 4'''
print('+'*15)

# Listas em Python:

valores=list(range(4,11))  # range pode criar uma estrutura de lista de repetição organizada:
print(valores)
'''Resultado:
        [4, 5, 6, 7, 8, 9, 10]'''

# Exemplo aplicado com laço 'for':
valores=[]
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores: #---> Para cada valor 'v' em 'valores'
    print(f'{v}...') #end='') #--> o (END='') põe na mesma linha.
'''resultado: 5...9...4...'''
# Outra forma conceitual aplicada:
print('-'*15)
for c,v in enumerate(valores):   # Tanto a chave 'c' quanto o valor 'v' são enumerados
    print(f'Na posição {c} encontrei o valor {v}!')
'''Resultado:
Na posição 0 encontrei o valor 5!
Na posição 1 encontrei o valor 9!
Na posição 2 encontrei o valor 4!    '''
# Ler valores do teclado e colocar na lista:
for cont in range(0,5):
    valores.append(int(input('Digite um valor: \n')))
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
   # print(valores.append)
Result:
Na posição 3 encontrei o valor 5!
Na posição 4 encontrei o valor 8!
Na posição 5 encontrei o valor 10!
Na posição 6 encontrei o valor 11!
Na posição 7 encontrei o valor 12!
   
    

    
    
    
