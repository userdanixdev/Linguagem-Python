# TESTE — Transferência (transação atômica)

def test_transferencia_atomic(session):
    from src.models import Usuario, ContaCorrente, Historico_operacoes

    u1 = Usuario(nome="Daniel")
    u2 = Usuario(nome = "Marisa")
    session.add_all([u1,u2])
    session.commit()

    c1=ContaCorrente(saldo=200, usuario_id=u1.id)
    c2=ContaCorrente(saldo=100, usuario_id=u2.id)

    session.add_all([c1,c2])
    session.commit()

    Historico_operacoes.transferir(c1,c2,50, session)

    # Contas atualizadas:
    assert c1.saldo == 150
    assert c2.saldo == 150

    # Histórico Criado:

    registros = session.query(Historico_operacoes).all()
    assert len(registros) == 2

# Pytest acusa: • ImportError: cannot import name 'Historico_operacoes' from 'src.models'   
# Ou seja, não há modelos com a classe 'historico_operacoes' para ser testada. 
# Detalhe: Há outra informação importante:
# session = <sqlalchemy.orm.session.Session object at 0x00000237A457B380>
# Aqui também podemos identificar mais informações sobre a origem do problema
# Assim devemos adicionar à função teste um método teste que identifica o objeto 'session' como string.
    
    #def __str__(self,session): #<- Método especial para representar o objeto como strings
     #   return f"{self.__class__.__name__}:{[f'{chave}={valor}'for chave, valor in self.__dict__.items()]}"

if __name__ == "__main__":
    import pytest
    import io
    import sys
    import re
    import os

    # Nome do arquivo atual
    nome_arquivo = os.path.basename(__file__)                 
    nome_base = os.path.splitext(nome_arquivo)[0]             

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
