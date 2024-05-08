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

def recomendar_plano(consumo_medio,plano_essencial,plano_prata,plano_premium):
  if consumo_medio <= plano_essencial:
    print( 'Plano Essencial Fibra - 50Mbps')
  elif plano_essencial < consumo_medio <= plano_prata:
    print( 'Plano Prata Fibra - 100Mbps')
  elif consumo_medio > plano_prata:
    print( 'Plano Premium Fibra - 300Mbps')
  else:
    print( 'Digite um valor válido')

def main():
  plano_essencial = 10
  plano_prata = 20
  plano_premium = 21
  while True:
    consumo_medio = float(input('Digite o consumo médio mensal de internet (em GB): '))
    if consumo_medio <=0:
      print('Digite um valor válido.')
    else:
      recomendar_plano(consumo_medio,plano_essencial,plano_prata,plano_premium)
      break

main()      
