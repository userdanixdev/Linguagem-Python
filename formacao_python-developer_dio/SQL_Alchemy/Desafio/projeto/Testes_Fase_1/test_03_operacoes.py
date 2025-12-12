# TESTE — depósitos e saques (regras básicas)
def test_depositar_sacar(session):
    from src.models import ContaCorrente,Conta
    cc = ContaCorrente( saldo = 100, limite_especial = 300)
    cc.depositar (50)
    assert cc.saldo == 150

    cc.sacar(100)
    assert cc.saldo == 50
# O pytest acusava que o saldo não existia. Não era definido. Sendo assim, declaramos a variável antes de saldo
# cc.saldo. Sendo assim, sem erros.
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
    