# Versão 04: Uso do Sample

from random import sample
# Vai samplear 5 números no alcance até 10:

a =  tuple(sample(range(10),5))
print(f'Os números sorteados foram: {a}\n O maior valor é {max(a)} e o menor é: {min(a)}.')
