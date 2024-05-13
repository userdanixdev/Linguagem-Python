# Versão 3.1:
print(f'{'='*15}\n{"Situação Aluno"}\n{'='*15}')
entrada_1=input('Nome: ')  # Variável recebe entrada character do usuário
entrada_2=float(input('Média: ')) # Variàvel recebe entrada float do usuário
if entrada_2 <= 5:         # 1º condição para a variável, se satisfazer uma nova variável é criada com o valor de REPROVADO
    entrada_3 = 'Reprovado'
elif entrada_2 <= 6.9:     # 2º condição para para a mesma variável, se satisfazer a mesma variável recebe outro valor 
    entrada_3 = 'Recuperação'
else:
    entrada_3 = 'Aprovado' # Caso não satisfazer nenhuma das condições, recebe a variável recebe outro valor
# Cria-se uma variável do tipo dicionário e as variáveis dentro dos valores
ficha={'nome':entrada_1,'média':entrada_2,'status':entrada_3} # Declarar o nomes das chaves e incluir as variáveis nos valores
# Mostrar na tela os dados:
print(f'Nome do aluno:{ficha["nome"]}\nMédia do aluno:{ficha["média"]}\nStatus:{ficha["status"]}\nFIM')












    
    
