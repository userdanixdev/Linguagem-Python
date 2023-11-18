#Crie um programa onde o usuário possa digitar sete valores numéricos e
#cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#versao 02:

#Se colocamos a sub lista dos valores pares no indice 0 da lista principal e os valores
#impares na sub lista do indice 1, repare que bate com os valores do resto da divisão,
#um par qualquer vai dar resto = 0 e um impar qualquer resto = 1, então podemos
#ao invés de dar um valor fixo ao indice que o programa vai acessar da lista para
#adicionar o numero, colocar a propia operação de resto da divisão por 2.
#Em código fica assim (considerando que os numeros foram armazenados na lista valores,
#c é o contador dentro do for e numero é o valor que o usuario acaba de digitar.

#Combinando com a função sorted, podemos ordenar os valores nas listas dentro da propia
#função print, isso significa que da para fazer o exercicio inteiro em 6 linhas,
#abaixo ele inteiro:

valores=[[],[]]
for c in range(1,8):   # O 'c' dentro do laço for é o contador, limitado a 7.
    numero=int(input(f'Digite o valor {c}°: '))
    valores[numero % 2].append(numero)
print(f'Valores pares digitados: {sorted(valores[0])}. ')
print(f'Valores ímpares digitados: {sorted(valores[1])}. ')



