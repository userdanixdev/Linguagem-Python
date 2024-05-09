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




