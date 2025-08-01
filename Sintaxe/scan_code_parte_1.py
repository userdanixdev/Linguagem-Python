Se seu objetivo é garantir que qualquer usuário, com qualquer layout de teclado, consiga usar seu programa sem erros,
usar scan_code é a melhor escolha — ele ignora o layout lógico do teclado e usa a posição física da tecla.

Etapa 1 — Detectar a tecla pressionada e seu scan_code logo no início
Assim que o usuário abre o programa, você pode pedir que ele pressione as teclas que serão usadas, apenas uma vez, 
para que você grave a posição física correta para o teclado dele.

Exemplo: Modo de configuração interativa
Aqui está um trecho de código que pede ao usuário para pressionar as teclas que o programa usará, e grava os scan_codes automaticamente:

import keyboard

scan_codes = {}

def capturar_tecla(nome_funcao):
    print(f"\nPor favor, pressione a tecla que você deseja usar para: {nome_funcao}")
    evento = keyboard.read_event()
    if evento.event_type == keyboard.KEY_DOWN:
        print(f"Tecla capturada: {evento.name} | Scan code: {evento.scan_code}")
        return evento.scan_code

# Capturando os códigos fisicamente pressionados
scan_codes['toggle_pause'] = capturar_tecla("⏸️  Pausar / Retomar")
scan_codes['go_back'] = capturar_tecla("⬅️  Voltar")
scan_codes['increase_speed'] = capturar_tecla("➕  Aumentar velocidade")
scan_codes['decrease_speed'] = capturar_tecla("➖  Diminuir velocidade")

# Mostrar os códigos capturados
print("\nTeclas configuradas:")
for acao, code in scan_codes.items():
    print(f"{acao}: scan_code = {code}")


O que esse código faz?
Solicita que o usuário pressione uma tecla para cada função.

Mostra o scan_code correspondente.

Você pode armazenar isso em um arquivo JSON, para salvar e reutilizar depois — se quiser, te mostro isso no próximo passo.



