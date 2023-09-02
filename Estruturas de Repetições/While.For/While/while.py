A estrutura de repetição 'WHILE' produz laços indeterminados.
Estrutura básica:
c=1
while c<10:
  print(c)
  c = c+ 1
print('Fim')
===================================

Sem limites de valores. Por exemplo:
pela estrutura de repetição por variável de controle for in range(), devemos dizer
de onde vai até onde vai.
O WHILE não.
Exemplo:
n=1 
while n !n = 0:
  n = int(input('Digite um valor: '))
print('Fim')
Os resultados não terão FIM!!
===============================================
Exemplo02:
r = 'S'
while r == 'S':
  n = int(input('Digite um valor: '))
  r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')  
================================================
Exemplo03:
n = 1
while n !n = 0:
  n=int(input('Digite um valor: '))
print('Acabou')
==========================================
Exemplo04:
n = 1
par = impar = 0
while n != 0:
  n=int(input('Digite um valor: '))
  if n!=0:
      if n % 2 == 0:
          par = par + 1
      else:
          impar = impar + 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')
Resultado:
Digite um valor: 2
Digite um valor: 7
Digite um valor: 3
Digite um valor: 1
Digite um valor: 4
Digite um valor: 0
Você digitou 2 números pares e 3 números ímpares.

  ++++ A execução do laço somente então irá acabar quando o resultado digitado 
  for 0, enquanto não for , o programa irá sempre perguntar e contar os números
                     pares E impares.
=================================================================================





