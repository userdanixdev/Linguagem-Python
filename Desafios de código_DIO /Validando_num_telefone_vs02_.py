import re
def validar_num_tel(num_tel):
    resposta = 'válido' if re.match(r'\(\d{2}\) 9\d{4}-\d{4}',num_tel)else 'inválido'
    return f'Número de telefone {resposta}.'
print(validar_num_tel(input('Insira o número de telefone: ')))
