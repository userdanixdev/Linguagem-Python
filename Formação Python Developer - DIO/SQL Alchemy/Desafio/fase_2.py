# Fase 02:
# Regras de negócio dentro das entidades:
  # métodos sobrescritos pode_sacar
  # lógica de limite especial lógica de rendimento mensal, cálculo de resgate com taxa e atomicidade com Session.

# Implementação dos serviços:
  # Serviço de transações
  # Serviço de relatórios (consultas avançadas)
      # Consultas avançadas do banco como: total movimentado por cliente, ranking de clientes por movimentação
        # e histórico filtrado por período e saldo consolidado.

# 1° Passo: Criação das entidades Usuário e Contas
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullalbe=True)
    email = Column(String,nullalbe=True)
    senha_hash = Column(String, nullalbe=True)
    data_nascimento = Column(String, nullalbe=True)
    endereco = Column(String,nullalbe=True)
    telefone = Column(String, nullalbe=True)

    # Um usuário pode ter várias contas e vários endereços (relação 1:N -> contas)
    contas = relationship("Conta", back_populates="usuario")
    endereco = relationship("Endereço", back_populates="usuario", cascade= "all, delete-orphan")

# 1° Passo: Criação das entidades Usuário e Contas ( 3 tipos de contas):
class Conta(Base):
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True, autoincrement = True)
    tipo_conta = Column(String(20)) # Diferenciar os tipos de contas
    numero_conta = Column(String)
    saldo = Column(Float, default=0.0)

    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="contas")
    __mapper_args__ = {
      "polymorfic_identity" : "conta",
      "polymorfic_on" : tipo_conta }

# Fase 2: Métodos de domínio básicos (podem ser sobrescritos nas filhas)      

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError (" Valor inválido")
        self.saldo += valor

    def pode_sacar(self, valor):
        # regra genérica: só pode sacar até o saldo (filhas podem sobrescrever)
        return self.saldo >= valor

    def sacar(self,valor):
        if valor <= 0:
            raise ValueError("Vallor inválido")
        if not self.pode_sacar(valor):
            raise ValueError("Saldo insuficiente")            
        self.saldo -= valor

    def __repr__(self):
        return f"< Conta {self.numero_conta} - {self.tipo_conta} - Saldo: {self.saldo}>"     

class ContaCorrente(Conta):
    __tablename__ = "conta_corrente"
    id = Column(Integer, ForeignKey("conta.id"), primary_key=True)
    limite_especial = Column(Float, default=0.0)

    __mapper_args__ = {
      "polymorfic_identity" : 'corrente'
    }

    # FASE 2: Adicionar métodos “inteligentes” na entidade ContaCorrente:
    def pode_sacar(self,valor):
      # Uso do limite especial:
      return (self.saldo + (self.limite_especial or 0.0)) >= Valor
    # opcional sobrescrita do saque para manter logs específicos na entidade
    def sacar(self, valor):
      if valor <= 0:
        raise ValueError("Valor inválido.")
      if not self.pode_sacar(valor):
        raise ValueError("Limite insuficiente")        
      self.saldo -= valor        

# Classe de conta poupança regras:
# Regras sugeridas: Não tem limite especial, Tem rendimento mensal, Saque normal (mas pode ter carência opcional)

class ContaPoupança(Conta):
  __tablename__ = "conta_poupança"
  id = Column (Integer, ForeignKey("contas.id"), primary_key= True)
  rendimento_mensal = Column(Float, default = 0.005)
  __mapper_args__ = {
  "polymorfic_identity" : "poupanca"
  }
  # Fase 02: Rendimento Mensal
  def render(self):
    self.saldo += self.saldo * (self.rendimento_mensal or 0.0)
# Exemplo simplificado: bloquear mais de N saques (a lógica de data fica melhor em serviço)
  def pode_sacar(self, valor, limite_saques_diarios = 3):
    if self.saques_dia >= limite_saques_diarios:
      return False
    return self.saldo >= valor

  def sacar (self, valor):
    if valor <= 0:
      raise ValueError('Valor inválido')
    if not self.pode_sacar(valor):
      raise ValueError("Saque não permitido (limite diário ou saldo)")
    self.saldo -= valor
    self.saques_dia += 1      

# Criação da Conta Investimento. 
# Regras sugeridas: Rendimento depende de risco, Paga taxa para resgatar (ex.: 2%) e Aplicação e resgate com regras.

class Conta_Investimento(self):
    __tablename__= 'Conta_invest'
    id = Column (Integer, ForeignKey('contas.id'), primary_key=True)
    taxa_resgate = Column(Float, default=0.02) # Fase 02: Métodos e regras de negócio
    __mapper_args__ = {
        "polymorfic_identity": "investimento"
    }
    # Fase 02: Resgate
    def resgatar(self, valor):
        valor_taxa = valor + (valor * (self.taxa_resgate or 0.0))        
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

  # Relação:
  conta = relationship("Conta",beckref = "historico")
# Fase 02:
  def __repr__(self):
    return f"< Histórico {self.id}, - Conta {self.conta_id} - {self.tipo_operacao} {self.valor}"
# Fase 02: Método estático ( ficam preferencialmente em serviços (ex.: services/relatorios.py)
  @staticmethod  
  def registrar_operacao(self, tipo, valor, status, mensagem):
        return Historico_operacoes(
            conta_id = self.id,
            tipo = tipo,
            valor = valor,
            status = status,
            mensagem=mensagem 
        )    
# Transações Atômicas (Transferências) Objetivo: Garantir atomicidade.
# Método utilitário que pode residir também em um serviço (recomendado),mas aqui deixamos como helper estático marcado como FASE 2.
  @staticmethod  
  def transferir(origem, destino, valor, session):
        """
        origem, destino: instâncias de Conta (persistidas ou anexadas à sessão)
        session: Session do SQLAlchemy
        """
        with session.begin():
            origem.sacar(valor)
            destino.depositar(valor)
            # Variável que irá conter os registros de histórico.
            historico_saida = Historico_operacoes.registrar_operacao(
                conta_id = origem.id,
                tipo="Transferência Saída",
                valor = valor, status = "OK",
                mensagem = f" Transferido para conta {origem.id}"
            )
            historico_entrada = Historico_operacoes.registrar_operacao(
                conta_id = destino.id,
                tipo = "Transferência Entrada",
                valor=valor,
                status = "Ok",
                mensagem = f"Recebido de conta: {origem.id}"
            )
            session.add([historico_saida,historico_entrada])

# Fase 02: Vincular o cartão à conta.
class Cartao(Base):
      __tablename__ = 'cartoes'

      id = Column (Integer, primary_key=True)
      numero = Column (Integer)
      validade = Column(Float)
      cvv = Column (String)
      limite = Column ( Float )
      conta_id = Column(Integer, ForeignKey("conta.id"))
      conta = relationship('Conta', backref="cartoes")

      # Implementações da FASE 02:
      def bloquear(self):
            # Implementar a lógica de bloqueio ( campo status poderia ser adicionado)
            pass
      def __repr__(self):
            return f" < Cartão: {self.numero} - Conta {self.conta_id}"

# Entidade endereço dos clientes. Um cliente pode ter mais de um endereço e cada endereço pertence a somente 1 usuário:

class Endereco:
    __tablename__= "enderecos"
    id = Column (Integer, primary_key=True)
    rua = Column(String(50), nullable=False)
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
        .join(Conta.historico)
        .group_by(Usuario.id)
        .order_by(func.sum(Historico_operacoes.valor).desc()))
        return session.execute(stmt).all()


