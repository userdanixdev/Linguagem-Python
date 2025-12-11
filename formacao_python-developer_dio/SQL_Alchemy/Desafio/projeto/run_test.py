import os
import subprocess
import re
from datetime import datetime

def run_pytest():
    # ====== CONFIGURAÇÃO DO DIRETÓRIO ======
    test_dir = os.path.join(os.getcwd(), "Testes_Fase_1")

    if not os.path.exists(test_dir):
        print("❌ Diretório de testes não encontrado:")
        print(test_dir)
        return

    os.chdir(test_dir)
    print(f"📁 Entrando em: {test_dir}")

    # ====== EXECUTAR PYTEST ======
    result = subprocess.run(
        ["pytest", "-q"],
        capture_output=True,
        text=True
    )

    saida = result.stdout + "\n" + result.stderr

    # ====== CONTADOR DE EVENTOS ======
    erros = len(re.findall(r"ERROR|Error|Traceback|Exception", saida))
    falhas = len(re.findall(r"FAILED", saida))
    passed = len(re.findall(r"PASSED|passed", saida))
    warnings = len(re.findall(r"warning|Warning|WARN", saida))

    # ====== GERAR LOG POR DATA ======
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%Hh%Mmin%Ss")
    log_path = os.path.join(logs_dir, f"log_teste_{timestamp}.txt")

    # ===== CÓDIGOS ANSI =====
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    # ===== COLORIR A SAÍDA =====
    saida_colorida = ""
    for linha in saida.splitlines():

        # ERROS → Vermelho
        if any(kw in linha for kw in ["ERROR", "Error", "Traceback", "Exception"]):
            saida_colorida += f"{RED}{linha}{RESET}\n"
            continue

        # WARNINGS → Amarelo
        if any(kw in linha for kw in ["warning", "Warning", "WARN"]):
            saida_colorida += f"{YELLOW}{linha}{RESET}\n"
            continue

        # SUCESSOS → Verde
        if any(kw in linha for kw in ["PASSED", "passed"]):
            saida_colorida += f"{GREEN}{linha}{RESET}\n"
            continue

        # LINHAS NORMAIS
        saida_colorida += linha + "\n"

    # ===== GRAVAR LOG =====
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("===== RESUMO DO TESTE =====\n")
        f.write(f"✔ Testes passados: {passed}\n")
        f.write(f"❌ Testes falhados: {falhas}\n")
        f.write(f"💥 Erros estruturais: {erros}\n")
        f.write(f"⚠ Warnings: {warnings}\n\n")

        f.write("===== SAÍDA COMPLETA DO PYTEST =====\n")
        f.write(saida_colorida)

    # ===== PRINT RESUMO NO TERMINAL =====
    print("\n📌 RESULTADO DOS TESTES\n")
    print(f"✔ Passaram: {passed}")
    print(f"❌ Falharam: {falhas}")
    print(f"💥 Erros: {erros}")
    print(f"⚠ Warnings: {warnings}")
    print(f"\n📄 Log salvo em: {log_path}")


if __name__ == "__main__":
    run_pytest()
