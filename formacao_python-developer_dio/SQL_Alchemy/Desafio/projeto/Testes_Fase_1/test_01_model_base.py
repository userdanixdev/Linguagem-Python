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


#if __name__ == "__main__":
    #import pytest

    # Arquivo atual
    #test_file = __file__

    # Arquivo de log TXT
    #log_file = "resultado_teste.txt"

    # Captura a saída do pytest (como string)
    #from io import StringIO
    #import sys

    #buffer = StringIO()
    #sys_stdout_original = sys.stdout
    #sys.stdout = buffer

    #retorno = pytest.main([test_file, "-q"], plugins=None)

    # Restaura saída original
    #sys.stdout = sys_stdout_original

    # Conteúdo capturado
    #pytest_output = buffer.getvalue()

    # Grava no arquivo TXT
    #with open(log_file, "w", encoding="utf-8") as f:
        #f.write(pytest_output)
        #f.write("\n")

#        if retorno == 0:
#            f.write("TESTE PASSOU COM SUCESSO ✔\n")
#        else:
#            f.write("ERROS FORAM ENCONTRADOS ❌\n")
#
#    print(f"Teste executado. Veja o log em: {log_file}")

# ============================
#   EXECUÇÃO INDIVIDUAL DO TESTE
# ============================
# ============================================================
#  GERADOR DE LOGS INDIVIDUAIS DO TESTE (TXT + HTML COLORIDO)
# ============================================================

if __name__ == "__main__":
    import pytest
    import io
    import sys
    import re
    import html as html_escape
    from datetime import datetime

    # Arquivos com data/hora
    base_name = "resultado_teste"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_file = f"{base_name}_{timestamp}.txt"
    html_file = f"{base_name}_{timestamp}.html"

    # Captura saída
    buffer_out = io.StringIO()
    buffer_err = io.StringIO()

    stdout_original = sys.stdout
    stderr_original = sys.stderr

    sys.stdout = buffer_out
    sys.stderr = buffer_err

    # Executa pytest apenas neste arquivo
    retorno = pytest.main([__file__, "-q"])

    sys.stdout = stdout_original
    sys.stderr = stderr_original

    saida = buffer_out.getvalue() + buffer_err.getvalue()

    # ================= CONTAGENS ======================
    passed = len(re.findall(r"\bpassed\b", saida, re.IGNORECASE))
    falhas = len(re.findall(r"\bFAILED\b", saida))
    erros = len(re.findall(r"\bERROR\b", saida))
    warnings = len(re.findall(r"\bwarning\b", saida, re.IGNORECASE))

    tipos_erros = re.findall(r"\b([A-Za-z_]+Error)\b", saida)
    tipos_contagem = {}
    for t in tipos_erros:
        tipos_contagem[t] = tipos_contagem.get(t, 0) + 1

    # =================================================
    # 1) GERAR TXT (SEM CÓDIGOS DE COR ANSI)
    # =================================================
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write("===== RESUMO DO TESTE =====\n")
        f.write(f"Testes passados: {passed}\n")
        f.write(f"Testes falhados: {falhas}\n")
        f.write(f"Erros estruturais (pytest): {erros}\n")
        f.write(f"Warnings: {warnings}\n\n")

        f.write("===== TIPOS DE ERROS PYTHON =====\n")
        if tipos_contagem:
            for tipo, qtd in tipos_contagem.items():
                f.write(f"• {tipo}: {qtd} ocorrência(s)\n")
        else:
            f.write("Nenhum erro Python encontrado.\n")

        f.write("\n===== SAÍDA COMPLETA DO PYTEST =====\n")
        f.write(saida)

    # =================================================
    # 2) GERAR HTML COLORIDO
    # =================================================

    def line_to_html(line):
        esc = html_escape.escape(line)

        # Erros fortes
        if any(x in line for x in ["FAILED", "ERROR", "Traceback", "Exception"]):
            return f'<div class="err">{esc}</div>'

        # Warnings
        if "warn" in line.lower():
            return f'<div class="warn">{esc}</div>'

        # Passou
        if "passed" in line.lower():
            return f'<div class="ok">{esc}</div>'

        # Normal
        return f'<div class="plain">{esc}</div>'

    css = """
body { font-family: Arial; background:#f2f2f2; padding: 20px; }
h1 { font-size:20px; }
.summary { background:white; padding:15px; border-radius:6px; margin-bottom:10px; }
.err { color:#b00020; background:#ffe5e5; padding:4px 8px; border-left:4px solid #b00020; margin:2px 0; white-space:pre-wrap; }
.warn { color:#8a6d0a; background:#fff6d5; padding:4px 8px; border-left:4px solid #e0b400; margin:2px 0; white-space:pre-wrap; }
.ok { color:#1b7a24; background:#eaffea; padding:4px 8px; border-left:4px solid #3ccb4a; margin:2px 0; white-space:pre-wrap; }
.plain { background:white; padding:4px 8px; margin:2px 0; white-space:pre-wrap; }
.logblock { background:white; padding:10px; max-height:70vh; overflow:auto; border-radius:6px; }
"""

    html_linhas = [line_to_html(l) for l in saida.splitlines()]

    with open(html_file, "w", encoding="utf-8") as f:
        f.write("<!doctype html><html><head><meta charset='utf-8'>")
        f.write(f"<title>Relatório de Testes - {timestamp}</title>")
        f.write(f"<style>{css}</style>")
        f.write("</head><body>")

        f.write(f"<h1>Relatório de Testes - {timestamp}</h1>")

        f.write("<div class='summary'>")
        f.write(f"<b>Passaram:</b> {passed} &nbsp;&nbsp; ")
        f.write(f"<b>Falharam:</b> {falhas} &nbsp;&nbsp; ")
        f.write(f"<b>Erros:</b> {erros} &nbsp;&nbsp; ")
        f.write(f"<b>Warnings:</b> {warnings}<br><br>")

        f.write("<b>Tipos de erros:</b> ")
        if tipos_contagem:
            f.write(", ".join(f"{t}({q})" for t, q in tipos_contagem.items()))
        else:
            f.write("Nenhum")
        f.write("</div>")

        f.write("<div class='logblock'>")
        for linha in html_linhas:
            f.write(linha)
        f.write("</div>")

        f.write("</body></html>")

    print(f"\n📄 Arquivo TXT gerado em: {txt_file}")
    print(f"🌐 Arquivo HTML gerado em: {html_file}\n")