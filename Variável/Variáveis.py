# Faça um programa em que deve perguntar o nome, a idade e crirar uma mensagem
#dizendo em qual ano ele irá aposentar. Considere que todos as pessoas irão se
#aposentar com 65 anos de idade.

nome=input('Me diga o seu nome: ')
idade = int(input('Me diga sua idade: '))
ano = str(2024-idade+65)
print('Olá,'+ nome + ' Você poderá se aposentar em '+ ano +'.')
