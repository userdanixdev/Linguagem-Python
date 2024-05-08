# Desafio:
# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal 
# com base em seu consumo mensal de dados.
# Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'.
# Crie uma função chamada 'recomendar_plano' para receber o consumo médio mensal de dados informado pelo cliente,
# além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

'''Planos Oferecidos:

- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.'''

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input('Insira o consumo médio mensal de internet: '))
# Criar uma função para receber o consumo médio mensal:
def recomendar_plano(consumo):
  if consumo <= 10:
    return ' Plano Essencial Fibra - 50Mbps '
  if consumo >= 10 and consumo <=20:
    return ' Plano Prata Fibra - 100Mbps '
  if consumo > 20:
    return ' PLano Premium Fibra - 300Mbps '

# Chamar a função com o consumo inserido para imprimir o resultado:
print(recomendar_plano(consumo))
