# Somando valores : Versão 06: Comentada

while True:    # Looping sempre que verdade , inserir valores nas variáveis abaixo:
  n1=input('Insira um valor: ')
  n2=input('Insira outro valor: ')
  if not (n1.isnumeric() and n2.isnumeric()):   # Condicional se não for numerico. msg de erro até que seja verdade.
    print('Somente números inteiros.')
    continue  # Sendo verdade, continua, e a variável soma recebe as variáveis convertidas em números inteiros.
  soma=int(n1)+int(n2)
  print(f'A soma entre o número {n1} + {n2} = {soma}.' )
  break
