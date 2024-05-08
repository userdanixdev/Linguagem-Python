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
