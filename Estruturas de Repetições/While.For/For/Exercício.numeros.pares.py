#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
#daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(0,7):
    num=int(input(f'Digite o {c} valor: '))
    if num%2==0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma foi {soma}.')
   
            
Result:
Digite o 0 valor: 5
Digite o 1 valor: 3
Digite o 2 valor: 1
Digite o 3 valor: 1
Digite o 4 valor: 9
Digite o 5 valor: 7
Digite o 6 valor: 8
Você informou 1 números pares e a soma foi 8.
================================================================================================
Versão02:

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
#daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

soma=0
cont=0
for c in range(1,8):
    num=int(input(f'Digite o {c}° valor: '))
    if num%2==0:
        soma = num + soma
        cont = cont + 1
print(f' Vc informou {cont} números pares e a soma entre eles foi {soma}.')
Result:
Digite o 1° valor: 5
Digite o 2° valor: 6
Digite o 3° valor: 7
Digite o 4° valor: 8
Digite o 5° valor: 9
Digite o 6° valor: 10
Digite o 7° valor: 11
 Vc informou 3 números pares e a soma entre eles foi 24.
     =========================================================================================




