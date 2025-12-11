# FASE 1 — Fundamentos e Modelagem:
   # Estrutura inicial
   # Criar as entidades principais e os atributos de dados:
      # Usuario
      # Contas (abstrata)
      # Endereco
      # HistoricoOperacao

# 1° Passo: Criação das entidades Usuário e Contas
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String,nullable=False,unique=True)
    senha_hash = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)
    endereco = Column(String,nullable=False)
    telefone = Column(String, nullable=False)

    # Um usuário pode ter várias contas e vários endereços (relação 1:N -> contas)
    contas = relationship("Conta", back_populates="usuario")
    endereco = relationship("Enderecos", back_populates="usuario", cascade= "all, delete-orphan")

# 1° Passo: Criação das entidades Usuário e Contas ( 3 tipos de contas):

class Conta(Base):
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True, autoincrement = True)
    tipo_conta = Column(String(20)) # Diferenciar os tipos de contas
    numero_conta = Column(String)
    saldo = Column(Float, default=0.0)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="contas")
    __mapper_args__ = {
      "polymorphic_identity" : "conta",
      "polymorphic_on" : tipo_conta }
    
# Herança (Tipos de Conta)
# Objetivo: Criar classes derivadas com regras diferentes:
  # ContaCorrente
  # ContaPoupanca
  # ContaInvestimento

# Regras :
    # Corrente → pode ficar negativo até o limite especial
    # Poupança → limite de saques diários
    # Investimento → aplicar taxa de rendimento
    

class ContaCorrente(Conta):
    __tablename__ = "conta_corrente"
    id = Column(Integer, ForeignKey("contas.id"), primary_key=True)
    limite_especial = Column(Float, default=0.0)

    __mapper_args__ = {
      "polymorphic_identity" : 'corrente'
    }

    # Adicionar métodos “inteligentes” na entidade ContaCorrente:

    

# Classe de conta poupança regras:
# Regras sugeridas: Não tem limite especial, Tem rendimento mensal, Saque normal (mas pode ter carência opcional)

class ContaPoupança(Conta):
  __tablename__ = "conta_poupança"
  id = Column (Integer, ForeignKey("contas.id"), primary_key= True)
  rendimento_mensal = Column(Float, default = 0.005)
  __mapper_args__ = {
  "polymorfic_identity" : "poupanca"
  }
  def render(self):
    self.saldo += self.saldo * self.rendimento_mensal

# Criação da Conta Investimento. 
# Regras sugeridas: Rendimento depende de risco, Paga taxa para resgatar (ex.: 2%) e Aplicação e resgate com regras.

class ContaInvestimento(self):
    __tablename__= 'Conta_invest'
    id = Column (Integer, ForeignKey('contas.id'), primary_key=True)
    taxa_resgate = Column(Float, default=0.02)
    __mapper_args__ = {
        "polymorphic_identify": "investimento"
    }
    def resgatar(self, valor):
        valor_taxa = valor + (valor * self.taxa_resgate)        
        if valor_taxa > self.saldo:
            raise ValueError('Saldo insuficiente para resgate.')
        self.saldo -= valor_taxa
        return valor            

class Historico_operacoes(Base):
  __tablename__ = 'historico_operacao'
  id = Column (Integer, primary_key= True)
  conta_id = Column(Integer, ForeignKey('conta.id'))
  tipo_operacao = Column (String, nullable=False)
  valor = Column (String, nullable = False)
  data = Column (DateTime, default = func.now())
  status = Column (String)
  mensagem = Column(String)     

  def registrar_operacao(self, tipo, valor, status, mensagem):
        return Historico_operacoes(
            conta_id = self.id,
            tipo = tipo,
            valor = valor,
            status = status,
            mensagem=mensagem 
        )    
# Transações Atômicas (Transferências) Objetivo: Garantir atomicidade.        

  def transferir(origem, destino, valor, session):
        with session.begin():
            origem.sacar(valor)
            destino.depositar(valor)

            session.add(origem.registrar_operacao("Transferência saída", valor, "ok", "transferido"))
            session.add(destino.registrar_operacao("Transferência saída", valor, "ok", "Recebido"))


class Cartao(Base):
      __tablename__ = 'cartão'

      id = Column (Integer, primary_key=True)
      numero = Column (Integer)
      validade = Column(Float)
      cvv = Column (String)
      limite = Column ( Float )
      conta_id = Column(Integer, ForeignKey("conta.id"))
      conta = relationship('Conta')

      
# Entidade endereço dos clientes. Um cliente pode ter mais de um endereço e cada endereço pertence a somente 1 usuário:

class Endereco(Base):
    __tablename__= "enderecos"
    id = Column (Integer, primary_key=True)
    rua = Column(String(120), nullable=False)
    numero = Column(String(20),nullable=False)
    bairro = Column (String(80), nullable=False)
    cidade = Column (String(50), nullable=False)
    estado = Column (String(2), nullable=False)
    cep = Column (String(10), nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    # Relação reversa:
    usuario = relationship("Usuario", back_populates="enderecos")
    def __repr__(self):
        return f"-> Endereço {self.rua}, {self.numero}, {self.cidade}/{self.estado}>"



# Relatórios do Banco:
class RelatoriosFinanceiros:
    @staticmethod
    def total_movimentado_por_cliente(session):
        stmt = ( select (Usuario.nome, func.sum(Historico_operacoes.valor).label("total")).join(Usuario.contas).join(Conta.historico).group_by(Usuario.id))
        return session.execute(stmt).all()
    @staticmethod
    def ranking_cliente(session):
        stmt = (select(Usuario.nome, func.sum(Historico_operacoes.valor).label("total"))
        .join(Usuario.contas)
        .join(Conta.Historico_operacoes)
        .group_by(Usuario.id)
        .order_by(func.sum(Historico_operacoes.valor).desc()))
        return session.execute(stmt).all()

