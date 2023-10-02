#Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

# Versão para escolher quantos números serão analisados e aparecer as posições
# dos três:

#versão 04:

print('-'*30)
quantidade=int(input('Digite quantos númneros você quer analisar: '))
print('-'*30)
nums=()  #<<<<--- Tuplas vazias
pares=()  #<----Tuplas vazias
for contador in range(0,quantidade):
    num=int(input('Digite um número: '))
    if num % 2==0:
        pares += (num,)  # <---- Preenchimento das tuplas
        nums += (num,)   #<-----Preenchimento das tuplas
print('-'*30)

noves=nums.count(9)
tres=nums.count(3)
pos_tres=-1
poses_tres=()
for contador_0 in range(0,tres):
    pos_tres=nums.index(3,pos_tres +1)
    poses_tres += (pos_tres,)
print(f'O valor 9 apareceu {noves} vez(es).')    
if nums.count(3)!=0:
 print(f'O valor 3 apareceu na(s) posição(ões){tres}.')
if len(pares)>0:
    print(f'Os valores pares digitados foram {pares}.')                
               
               
