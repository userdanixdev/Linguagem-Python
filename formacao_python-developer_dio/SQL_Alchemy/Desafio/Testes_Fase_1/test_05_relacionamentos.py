# TESTE — Relacionamentos (Usuário ↔ Endereço)

def test_usuario_endereco(session):
    from src.models import Usuario, Endereco

    u = Usuario(nome="Patrick")
    e = Endereco(
        rua="Rua A",
        numero="10",
        bairro="Centro",
        cidade="SP",
        estado="SP",
        cep="71070-001",
        usuario=u
        )

    session.add(u)
    session.commit

    assert len(u.enderecos) == 1
    assert u.enderecos[0].cidade == "SP"        