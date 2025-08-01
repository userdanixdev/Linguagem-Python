O que é o "monitoramento de teclas"?
O monitoramento de teclas (também chamado de key listening ou event hook) serve para que o seu programa responda a eventos do teclado 
em tempo real, ou seja:

"Quando o usuário apertar uma determinada tecla, o programa deve executar uma ação automaticamente."

O monitoramento é o coração da interação em tempo real com o teclado. Sem ele, o programa não "reage" ao que o usuário faz.

import keyboard

# Funções que serão chamadas quando teclas forem pressionadas:
def toggle_pause():
    print("⏸️  Pausar / Retomar")

def go_back():
    print("⬅️  Voltar")

def increase_speed():
    print("➕  Aumentar velocidade")

def decrease_speed():
    print("➖  Diminuir velocidade")

# Etapa 1: Captura das teclas
def capturar_tecla(nome_funcao):
    print(f"\n➡️ Pressione a tecla para: {nome_funcao}")
    evento = keyboard.read_event()
    while evento.event_type != keyboard.KEY_DOWN:
        evento = keyboard.read_event()
    print(f"✔️  Tecla '{evento.name}' capturada para '{nome_funcao}' (scan_code = {evento.scan_code})")
    return evento.scan_code

# Capturando os códigos das teclas
print("🧩 Configuração inicial das teclas (pressione uma tecla para cada função):")
scan_code_pause = capturar_tecla("⏸️  Pausar / Retomar")
scan_code_back = capturar_tecla("⬅️  Voltar")
scan_code_plus = capturar_tecla("➕  Aumentar velocidade")
scan_code_minus = capturar_tecla("➖  Diminuir velocidade")

# Etapa 2: Monitorar teclas durante a execução
def on_key_event(e):
    if e.scan_code == scan_code_pause:
        toggle_pause()
    elif e.scan_code == scan_code_back:
        go_back()
    elif e.scan_code == scan_code_plus:
        increase_speed()
    elif e.scan_code == scan_code_minus:
        decrease_speed()

print("\n🎮 Teclas prontas! Agora o programa está ativo. Pressione ESC para sair.\n")

# Inicia o monitoramento
keyboard.on_press(on_key_event)
keyboard.wait("esc") 
# O programa ficará ativo até que o usuário pressione ESC

“Se as teclas já foram configuradas... por que continuar monitorando?”
Porque configurar as teclas é só a primeira parte. Isso apenas informa ao programa quais scan_codes ele deve observar.
Mas o monitoramento em tempo real é o que permite que o programa reaja quando essas teclas forem realmente pressionadas.

Resumo objetivo:
Etapa	O que faz	Quando acontece
capturar_tecla()	Descobre qual tecla o usuário quer usar	No início do programa
keyboard.on_press()	Escuta o teclado o tempo todo	Durante a execução do programa
on_key_event()	    Reage quando uma tecla específica é pressionada	Sempre que uma tecla for pressionada

O que são modificadores?
Modificadores são teclas que, combinadas com outras, ativam atalhos especiais:

Modificador	Exemplo                	Significado
Ctrl	    Ctrl + Space	        Atalho de pausa
Shift	    Shift + +	            Talvez Aumentar Velocidade
Alt	Alt + Left Arrow	            Voltar                                                                                        

