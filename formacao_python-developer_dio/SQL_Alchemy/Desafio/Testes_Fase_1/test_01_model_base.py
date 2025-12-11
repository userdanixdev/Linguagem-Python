def test_criar_usuario(session):
    from src.models import Usuario

    u = Usuario(
        nome = "Daniel",
        email = "daniel@gmail.com",
        senha_hash = "abc123",
        data_nascimento = "1990-01-01"
    )
    session.add(u)
    session.commit()

    assert u.id is not None

