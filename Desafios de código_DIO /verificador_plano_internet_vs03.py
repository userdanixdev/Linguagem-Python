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


def recomendar_plano(referencia):
  resposta = {'Essencial':50,'Prata':100,'Premium':300}
  index = 0 if referencia <= 10 else 1 if referencia <= 20 else 2
  return f'Plano {list(resposta)[index]} Fibra - {list(resposta.values())[index]}Mbps'
consumo = float(input('Me informe o consumo médio mensal da sua internet: '))
print(recomendar_plano(consumo))                
