
# TESTE — criação da Conta (polimorfismo)
def test_conta_corrente(session):
    from src.models import Usuario, ContaCorrente

    u = Usuario(nome="João")
    session.add(u)
    session.commit()

    cc = ContaCorrente(
        tipo_conta="corrente",
        numero_conta = "123",
        saldo = 100,
        usuario_id = u.id,
        limite_especial=500
    )
    session.add(cc)
    session.commit()

    assert cc.id is not None
    assert cc.limite_especial == 500