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

# Desafio 3:
# Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. 
# Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto.
# Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros.
# Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e
# depois retorne uma mensagem adequada como mostra no exemplo a baixo

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
  def __init__(self, nome, numero, plano):
      self.nome = nome
      self.numero = numero
      self.plano = plano
# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
  def fazer_chamada(self, destinatario, duracao):
      custo_chamada = self.plano.custo_chamada(duracao)
      if self.plano.verificar_saldo() >= custo_chamada:
          self.plano.deduzir_saldo(custo_chamada)
          return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
      else:
          return "Saldo insuficiente para fazer a chamada."
# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
# TODO: Verifique se o saldo do plano é suficiente para a chamada.
# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
  def __init__(self, saldo_inicial):
    self.saldo = saldo_inicial
# TODO: Crie um método para verificar_saldo e retorne o saldo atual:
  def verificar_saldo(self):
    return self.saldo
# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
  def custo_chamada(self,duracao):
    return duracao * 0.10
# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
  def deduzir_saldo(self,valor):
    self.saldo -= valor 
# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
  def __init__(self, nome, numero, saldo_inicial):
    super().__init__(nome, numero, Plano(saldo_inicial))
# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())
# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())
# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))





