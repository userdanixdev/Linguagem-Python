# TESTE — Transferência (transação atômica)

def test_transferencia_atomic(session):
    from src.models import Usuarios, ContaCorrente, Historico_operacoes

    u1 = Usuario(nome="Daniel")
    u2 = Usuario(nome = "Marisa")
    session.add_all([u1,u2])
    session.commit

    c1=ContaCorrente(saldo=200, usuario_id=u1.id)
    c2=ContaCorrente(saldo=100, usuario_id=u2.id)

    session.add_all([c1,c2])
    session.commit

    Historico_operacoes.transferir(c1,c2,50, session)

    # Contas atualizadas:
    assert c1.saldo == 150
    assert c2.saldo == 150

    # Histórico Criado:

    registros = session.query(Historico_operacoes).all()
    assert len(registros) == 2
