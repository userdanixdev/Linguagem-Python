captura de teclas com modificadores:

import keyboard

# Suas funções
def toggle_pause():
    print("⏸️  Pausar / Retomar")

def go_back():
    print("⬅️  Voltar")

def increase_speed():
    print("➕  Aumentar velocidade")

def decrease_speed():
    print("➖  Diminuir velocidade")

# Etapa 1: Captura das teclas com modificadores
def capturar_tecla(nome_funcao, usar_modificador=False):
    print(f"\n➡️ Pressione a tecla para: {nome_funcao}")
    if usar_modificador:
        print("   (Segure o modificador desejado como Ctrl, Shift, Alt e pressione a tecla)")
    
    evento = keyboard.read_event()
    while evento.event_type != keyboard.KEY_DOWN:
        evento = keyboard.read_event()
    
    # Detecta o modificador se houver
    mod = None
    for m in ["ctrl", "shift", "alt"]:
        if keyboard.is_pressed(m):
            mod = m
            break

    print(f"✔️  Tecla '{evento.name}' capturada com modificador '{mod}' (scan_code = {evento.scan_code})")
    return (evento.scan_code, mod)

# Mapeia teclas com ou sem modificadores
print("🧩 Configuração das teclas:")
actions = {}
actions[capturar_tecla("⏸️  Pausar / Retomar", usar_modificador=True)] = toggle_pause
actions[capturar_tecla("⬅️  Voltar", usar_modificador=True)] = go_back
actions[capturar_tecla("➕  Aumentar velocidade", usar_modificador=True)] = increase_speed
actions[capturar_tecla("➖  Diminuir velocidade", usar_modificador=True)] = decrease_speed

# Etapa 2: Monitorar teclado
def on_key_event(e):
    for (code, mod), func in actions.items():
        if e.scan_code == code:
            if mod is None or keyboard.is_pressed(mod):
                func()

print("\n🎮 Programa ativo. Pressione ESC para sair.\n")
keyboard.on_press(on_key_event)
keyboard.wait("esc")
