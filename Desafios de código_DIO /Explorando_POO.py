# Desafio
# Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone.
# Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe.
# Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos,
# sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

# TODO: Crie uma classe UsuarioTelefone.  
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
class UsuarioTelefone:
    def __init__(self,nome,numero,plano):
    self.nome = nome
    self.numero=numero
    self.plano=plano

        
    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
      

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario=UsuarioTelefone(nome,numero,plano)

print(usuario)

# Desafio#2:
# Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano.
# Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos,
# 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  
# 'mensagem_personalizada' para gerar uma mensagem personalizada.

Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
  def __init__(self,nome,saldo):
    self.nome = nome
    self.saldo = saldo

# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
  def verificar_saldo(self):
    if self.saldo < 10:
        return "Seu saldo está baixo. Recarregue e use os serviços do seu plano. "
    elif self.saldo >= 50:
        return "Parabéns! Continue aproveitando seu plano sem preocupações."
    else:
        return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 
    

# Classe UsuarioTelefone:
class UsuarioTelefone:
  def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
  def verificar_saldo(self):
      return self.plano.verificar_saldo()


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)
