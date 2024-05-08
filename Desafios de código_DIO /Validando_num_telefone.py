#Desafio
# Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente
# está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão.
# Desenvolva uma função programa que valide se um número de telefone tem o formato correto.
# Formato esperado:
# O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9.
# Lembre-se de respeitar os espaços entre os números quando preciso.

# Entrada:
# Uma string representando o número de telefone.
# Saída:
# Uma mensagem indicando se o número de telefone é válido ou inválido.

# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html
# Módulo 're' que fornece operações com expressões regulares.
import re
# Criar uma função chamada que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
# Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = '^\(\d{2}\) 9\d{4}-\d{4}$'
# '^' - Indica o início da string    (\d{2}\) -> Corresponde a dois digitos para código de área onde '\d' é um dígito e {2} indica que deve haver dois dígitos
# '\) para fechar o código área. '9' corresponde ao prefixo indicando o número de celular. \d{4} - quatro dígitos para a primeira parte do número após o '9'.
# '$' indica para finalizar a string.    
# A função 're.match()' verifica se o padrão definido corresponde ao número de telefone fornecido.
# O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern,phone_number):
      return 'Número de telefone válido'
    else:
      return 'Número de telefone inválido'
# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input('Informe o número de telefone: ')
# Chame a função com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)
# Imprime o resultado:
print(result)
  
    

    
