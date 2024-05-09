# Em outras linguagens existem palavras reservadas para definir o nível de acesso aos atributos e métodos da classe.
# Em Python podemos usar convenções no nome do recurso, para definir se a variável é pública ou privada para definir se a variável é pública ou privada.
# Exemplo : Use o 'underline' para verificar se o atributo é privado.

class conta:
    def __init__(self,num_agencia,saldo=0):
        self._saldo= saldo
        self.num_agencia =  num_agencia
    def depositar(self,valor):
        self._saldo += valor
    def sacar(self,sacar):
        self._saldo -= saldo
        # Conceito de encapsulamento para criar um método de acessar o saldo.
    def mostrar_saldo(self):
        return self._saldo


conta = conta('0001',100)
conta.depositar(100)
print(conta._saldo) # Modo incorreto de ver o saldo. _saldo é uma variável privada.
# O modo correto é termos um método.
print(conta.num_agencia)
print(conta.mostrar_saldo())

# Propriedades de encapsulaento
class pessoa:
    def __init__(self,nome,ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento

pessoa = pessoa('Guilherme',1994)
print(f'nome: {pessoa.nome}\tIdade: {pessoa.idade}')
# O property irá transformar o método em atributo.



