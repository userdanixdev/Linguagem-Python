
# TESTE — criação da Conta (polimorfismo)
def test_conta_corrente(session):
    from src.models import Usuario, ContaCorrente

    u = Usuario(nome="João")
    session.add(u)
    session.commit()
# Nesse caso, o pytest acusa que ainda faltam argumentos nomeados para prencher.
# Mas o teste passou porque é para verificar a ContaCorrente
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

if __name__ == "__main__":
 import pytest
 import io
 import sys
 import re
 import os

    # Nome do arquivo atual
 nome_arquivo = os.path.basename(__file__)                 # test_criar_usuario.py
 nome_base = os.path.splitext(nome_arquivo)[0]             # test_criar_usuario

    # Nome final do relatório
 txt_file = f"{nome_base}.txt"

  # Captura saída do pytest
 buffer_out = io.StringIO()
 buffer_err = io.StringIO()

 stdout_original = sys.stdout
 stderr_original = sys.stderr

 sys.stdout = buffer_out
 sys.stderr = buffer_err

    # Executa pytest neste arquivo
 retorno = pytest.main([__file__, "-q"])

 sys.stdout = stdout_original
 sys.stderr = stderr_original

 saida = buffer_out.getvalue() + buffer_err.getvalue()

    # ================= CONTAGENS ======================
 passed = len(re.findall(r"\bpassed\b", saida, re.IGNORECASE))
 falhas = len(re.findall(r"\bFAILED\b", saida))
 erros = len(re.findall(r"\bERROR\b", saida))
 warnings = len(re.findall(r"\bwarning\b", saida, re.IGNORECASE))

 tipos_erros = re.findall(r"(\w+Error):\s(.+)", saida)

 tracebacks = re.split(r"=+.*=+", saida)
 tracebacks = [tb.strip() for tb in tracebacks if "Traceback" in tb]

    # ================= GERAR TXT ======================
 with open(txt_file, "w", encoding="utf-8") as f:

        f.write(f"===== RELATÓRIO DO ARQUIVO: {nome_arquivo} =====\n\n")

        f.write("===== RESUMO DO TESTE =====\n")
        f.write(f"Testes passados: {passed}\n")
        f.write(f"Testes falhados: {falhas}\n")
        f.write(f"Erros estruturais (pytest): {erros}\n")
        f.write(f"Warnings: {warnings}\n\n")

        f.write("===== TIPOS DE ERROS PYTHON =====\n")
        if tipos_erros:
            for tipo, msg in tipos_erros:
                f.write(f"• {tipo}: {msg}\n")
        else:
            f.write("Nenhum erro Python encontrado.\n")

        f.write("\n===== DETALHES DOS ERROS (TRACEBACKS) =====\n")
        if tracebacks:
            for i, tb in enumerate(tracebacks, 1):
                f.write(f"\n--- ERRO #{i} ---------------------------------\n")
                f.write(tb + "\n")
        else:
            f.write("Nenhum traceback encontrado.\n")

        f.write("\n===== SAÍDA COMPLETA DO PYTEST =====\n")
        f.write(saida)

 print(f"\n📄 Arquivo TXT gerado: {txt_file}\n")
