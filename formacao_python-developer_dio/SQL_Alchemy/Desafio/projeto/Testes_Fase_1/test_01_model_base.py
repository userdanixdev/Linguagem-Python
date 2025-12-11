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
    assert u.nome == "Daniel"

import os
import subprocess

def run_pytest():
    # 1. Caminho da pasta onde estão os testes
    test_dir = os.path.join(os.getcwd(), "Testes_Fase_1")

    if not os.path.exists(test_dir):
        print("❌ Diretório de testes não encontrado:")
        print(test_dir)
        return

    # 2. Entrar no diretório
    os.chdir(test_dir)
    print(f"📁 Entrando em: {test_dir}")

    # 3. Executar pytest (capturar saída)
    result = subprocess.run(
        ["pytest", "-q"],  # -q = quiet, saída mais limpa
        capture_output=True,
        text=True
    )

    # 4. Mostrar saída resumida
    print("\n📌 RESULTADO DOS TESTES:\n")

    if result.returncode == 0:
        print("✅ TODOS OS TESTES PASSARAM!")
    else:
        print("❌ Alguns testes falharam.")

    print("\n--- Saída do pytest ---")
    print(result.stdout)

    if result.stderr:
        print("\n--- Erros do pytest ---")
        print(result.stderr)


if __name__ == "__main__":
    run_pytest()

