from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, DateTime,func
from sqlalchemy.orm import relationship
from src.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha_hash = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    contas = relationship("Conta", back_populates="usuario")
class Conta(Base):

    __tablename__ = "contas"
    id = Column(Integer, primary_key=True,autoincrement=True)
    tipo_conta = Column(String(20))
    numero_conta = Column(String, unique=True)
    saldo = Column(Float, default=0.0)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario",back_populates="contas")

    # Fase 02: Métodos de depósito e saque ( Pytest acusou que não há esses métodos )
    # Além disso, classe pai 'Conta' não possui esses métodos para ser herdado da classe 'ContaCorrente'

    def depositar(self, valor):
        if valor  <= 0:
            raise ValueError("Valor inválido")
        self.saldo += valor
        return self.saldo
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido.")
        if valor > self.saldo:
            raise ValueError("Saldo Insuficiente")
        self.saldo -= valor
        return self.saldo

class ContaCorrente(Conta):
    __tablename__ = "conta_corrente"    
    id = Column(Integer, ForeignKey("contas.id"), primary_key=True)
    limite_especial = Column(Float,default=0.0)

    __mapper_args__ = {
        "polymorphic_identity": 'corrente',
    }
class Historico_operacoes(Base):
    __tablename__ = 'historico_operacao'
    id = Column (Integer, primary_key=True)
    conta_id = Column(Integer, ForeignKey('conta.id'),nullable=False)
    tipo_operacao = Column(String,nullable=False)
    valor = Column (Float, nullable=False)
    data = Column(DateTime, default=func.now())
    status = Column(String, default="Ok")
    mensagem = Column(String, nullable = True)
# Para que o teste seja validado é necessário criar dois métodos estáticos na classe 'histórico_operacoes':
# "registrar operacoes" primeiro e depois o método 'transferir'    
# Caso contrário o teste sempre dará o mesmo resultado: Não haverá transferência e a classe será inexistente
    @staticmethod
    def registrar_operacao(self, tipo, valor, status, mensagem):
        return Historico_operacoes(
            conta_id = self.id,
            tipo = tipo,
            valor = valor,
            status = status,
            mensagem = mensagem)
# Agora o método que irá validar o teste. De realizar transferências de fato.
    @staticmethod
    def transferir(origem, destino, valor, session):    
        """
        origem, destino: instâncias de Conta (persistidas ou anexadas à sessão)
        session: Session do SQL Alchemy      
        
        """
        with session.begin():
            origem.sacar(valor)
            destino.depositar(valor)
            # Variável 'histórico_saida' irá conter os registros de histórico:
            historico_saida = Historico_operacoes.registrar_operacao(
                conta_id = origem.id,
                tipo="Transferência Saída",
                valor = valor, status = "Ok",
                mensagem=f"Transferido para conta {origem.id}"
            )
            # Variável 'hist_entrada' irá conteer os registros de histórico:
            historico_entrada = Historico_operacoes.registrar_operacao(
                conta_id = destino.id,
                tipo = "Transferência Entrada",
                valor = valor,
                status = "Ok",
                mensagem = f"Recebido de conta: {origem.id}"
            )
            session.add([historico_saida,historico_entrada])