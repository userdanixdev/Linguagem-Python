# Grupo da Maioridade
#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.

from datetime import date
atual = date.today().year
tot_maior = 0
tot_menor = 0
for pessoa in range(1,8):
        nasc=int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
        idade = atual - nasc
        if idade >= 21:
            tot_maior = tot_maior + 1
        else:
            tot_menor = tot_menor + 1
print(f'Ao todo tivemos {tot_maior} pessoas maiores de idade.')
print(f'E também tivemos {tot_menor} pessoas menores de idade. ')

Result:
Em que ano a 1ª pessoa nasceu? 2000
Em que ano a 2ª pessoa nasceu? 1970
Em que ano a 3ª pessoa nasceu? 2005
Em que ano a 4ª pessoa nasceu? 1990
Em que ano a 5ª pessoa nasceu? 2010
Em que ano a 6ª pessoa nasceu? 1960
Em que ano a 7ª pessoa nasceu? 1940
Ao todo tivemos 5 pessoas maiores de idade.
E também tivemos 2 pessoas menores de idade. 
  ============================================================


