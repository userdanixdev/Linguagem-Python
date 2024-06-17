# Analisador de textos:

# Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

print('analisar de textos')
nome=input('Digite seu nome completo: ').strip() # Remover os espaços
print(f'Seu nome em maiúscula é {nome.upper()}.')
print(f'Seu nome em minúsculo é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome)} letras.')
print(f'Seu nome sem os espaços tem ao todo {len(nome)-nome.count(' ')} letras.')
nome_dividido=nome.split() # O split separa, por padrão, em lista, as strings que estiverem separadas por espaços.
print(f'Seu primeiro nome é {nome_dividido[0]} e ele possui {len(nome_dividido[0])}.')
print()
print('A função replace pode substituir os espaços por qualquer coisa, nesse caso, por nada.')
print('Seu nome tem um total de ', len(nome.replace(' ', '')), 'letras')
print()
print('Analisador de textos: 2° forma')
x=input('Digite seu nome completo: ').strip()  # Removedor de espaços
print(f'''
        Seu nome em maiúsculas é {x.upper()}.
        Seu nome em minúsculas é {x.lower()}.
        Seu nome tem {len(x)-x.count(' ')} letras.
        Seu primeiro nome é {x.split()[0]} e tem {len(x.split()[0])} letras.
        ''')
print()
print('Uso do join para remover os espaços do comprimento do nome:')
print(f'Seu nome tem {(len("".join(nome.split())))} letras.')
print(f'Seu nome tem {(len("".join(nome)))} letras.')






