# Aqui vão desafios práticos, progressivos e realistas para você evoluir seu projeto orientado a objetos + SQLAlchemy dentro do
# contexto de um sistema bancário.
# Cada desafio é pensado para treinar classes, métodos, relacionamentos, validações, transações, consultas mais avançadas e
# regras de negócio reais.

# DESAFIO 1 — Criar novos tipos de conta
# jetivo: Ampliar o modelo OO com classes derivadas e regras específicas.

# Sugestões de classes:
# ContaCorrente(Conta)
# ContaPoupanca(Conta)
# ContaInvestimento(Conta)

# Regras sugeridas:
  # ContaPoupança não permite mais de 3 saques/dia.
  # ContaCorrente permite limite especial (cheque especial).
  # ContaInvestimento aplica rentabilidade diária.

# Conceitos usados:
  # Herança
  # Polimorfismo
  # Métodos sobrescritos
  # Validação dentro das entidades

# FASE 1 — Fundamentos e Modelagem:
   # Estrutura inicial
   # Criar as entidades principais:
      # Usuario
      # Conta (abstrata)
      # Endereco
      # HistoricoOperacao

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha_hash = Column(String)

    contas = relationship("Conta", back_populates="usuario")

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Float, default=0.0)

    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="contas")

#FASE 2 — Herança (Tipos de Conta)
# Objetivo: Criar classes derivadas com regras diferentes:
  # ContaCorrente
  # ContaPoupanca
  # ContaInvestimento

class ContaCorrente(Conta):
    __tablename__ = "conta_corrente"
    id = Column(Integer, ForeignKey("conta.id"), primary_key=True)
    limite_especial = Column(Float, default=0.0)

# Regras Fase 2:
    # Corrente → pode ficar negativo até o limite especial
    # Poupança → limite de saques diários
    # Investimento → aplicar taxa de rendimento

    # Adicionar métodos “inteligentes” na entidade Conta:

    def depositar(self,valor):
        if valor <= 0:
          raise ValueError('Valor inválido')
        self.saldo += valor
    def sacar(self, valor):
        if valor <= 0:
          raise ValueError('Valor inválido')
        if not valor self.pode_sacar(valor):
          raise ValueError('Saldo insuficente')
        self.saldo -= valor
      # Cada tipo de conta sobrescreve pode_sacar.

# FASE 3 — Auditoria (Histórico de Operações)
    # Objetivo: Registrar cada operação na tabela HistoricoOperacao.
class Historico_operacoes(Base):
  __tablename__ = 'historico_operacao'
  id = Column (Integer, primary_key= True)
  conta_id = Column(Integer, ForeignKey('conta.id'))
  tipo = Column (String)
  valor = Column (String)
  data = Column (DateTime, default = func.now())
  status = Column (String)
  mensagem = Column(String)

  def registrar_operacao(self, tipo, valor, status, mensagem):
    return Historico_operacoes( 
      conta_id = self.id,
      tipo=tipo,
      valor=valor,
      status=status,
      mensagem=mensagem )

# FASE 5 — Transações Atômicas (Transferências)
    # Objetivo: Garantir atomicidade.
  def transferir(origem, destino, valor, session):
    with session.begin():
      origem.sacar(valor)
      destino.depositar(valor):

      session.add(origem.registrar_operacao('Transferência saída', valor, 'ok', 'transferido')
      session.add(destino.registrar_operacao(' Transferência saída',valor, 'ok', ' recebido')
                  #Se der erro → rollback automático.





                  
      
