# TESTE — Consultas (fase 2 futura)

def test_total_movimentado_por_cliente(session):
    from src.models import RelatoriosFinanceiros
    from src.models import Usuario, ContaCorrente, Historico_operacoes

    u = Usuario(nome="Daniel")
    session.add(u)
    session.commit()

    c = ContaCorrente(saldo=0, usuario_id=u.id)
    session.add(u)
    session.commit

    session.add(Historico_operacoes(conta_id=c.id, tipo_operacao="dep", valor=50))
    session.add(Historico_operacoes(conta_id=c.id, tipo_operacao="dep", valor=30))

    r = RelatoriosFinanceiros.test_total_movimentado_por_cliente(session)
    assert r[0].total == 80