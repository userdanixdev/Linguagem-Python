ERRO CALL BACK TECLADO:

Se o programa "trava" ou para de responder ao mudar o teclado (ex: de ABNT para US), 
isso pode acontecer porque a biblioteca keyboard depende diretamente do layout físico e do mapeamento de teclas do sistema operacional. 
Alterar o layout do teclado pode causar problemas de mapeamento de scan_code ou name das teclas — 
e isso pode afetar os callbacks que você definiu.


Problema comum:
Você provavelmente registrou um hotkey ou monitoramento específico de tecla, e ao trocar o layout, 
o código escaneado (scan_code) não bate mais, ou o nome da tecla (event.name) muda, causando travamento ou parada do loop.


O problema:
A biblioteca keyboard depende do layout de teclado ativo no sistema operacional. 
Quando você muda de layout (ex: de PT-BR para US ou vice-versa), certas teclas mudam de posição ou mapeamento interno, especialmente:

"+" e "-" — que dependem da tecla Shift em alguns layouts

"ctrl+left" pode ser mapeado de forma diferente dependendo do layout

Esses atalhos deixam de ser reconhecidos porque o nome da tecla (+, -, etc.) muda ou não é mais válido para o novo layout. 
Isso pode fazer com que o keyboard gere exceções internamente ou pare de capturar eventos corretamente.


Soluções recomendadas:

Use scan_codes como alternativa segura
(Avançado, mais técnico, mas independe do layout). Exemplo:

keyboard.on_press_key(13, lambda _: toggle_pause())  # 13 pode ser a tecla 'enter', por exemplo.

Mas você precisaria usar um script para identificar os scan_codes corretos com seu layout preferido.

✔️ 3. Use try/except ao redor dos handlers
Isso evita que o programa morra silenciosamente se um erro for lançado dentro do callback:

keyboard.on_press_key("ctrl+space", lambda _: safe_call(toggle_pause))
E defina safe_call assim:

def safe_call(func):
    try:
        func()
    except Exception as e:
        print(f"Erro ao executar função: {e}")
4. Verifique se o evento ainda está sendo capturado
Você pode adicionar um log de debug para ver se o teclado está mesmo capturando após a troca:


keyboard.on_press(lambda e: print(f"Tecla: {e.name}"))
Isso te diz se a biblioteca ainda está funcional depois da mudança de layout.

posso colocar um layout padrão no keyboard no programa para evitar esse tipo de problema?

O ChatGPT disse:
Não — a biblioteca keyboard do Python não permite forçar um layout de teclado específico diretamente dentro do programa.
Ela simplesmente lê os eventos do sistema operacional, que são afetados pelo layout atual configurado no SO (Windows, Linux etc.).

Por que isso acontece?
A keyboard funciona em baixo nível, ouvindo os scan codes enviados pelo teclado físico. O sistema operacional traduz esses códigos com base no layout ativo. Ou seja:

A tecla física que está no lugar do + no layout ABNT pode ser outra no layout US.

Se você registrar "+" no código, o programa depende da tecla lógica que representa "+" — e isso muda com o layout.

Mapeie as funções com scan_code (avançado)
Você pode usar códigos físicos das teclas (não mudam com o layout):

keyboard.on_press_key(13, lambda _: toggle_pause())  # exemplo: tecla Enter
Mas isso exige que você descubra os códigos exatos com base no seu teclado físico.

Detecte o layout do SO e avise o usuário
Você pode detectar o layout no Windows com algo assim (requer pywin32):

import win32api
import win32con

def get_current_keyboard_layout():
    hkl = win32api.GetKeyboardLayout()
    layout_id = hkl & (2**16 - 1)
    return layout_id

print(get_current_keyboard_layout())

Como descobrir o scan_code de uma tecla:

import keyboard

print("Pressione qualquer tecla para ver o scan_code (ESC para sair):")

def show_scan_code(e):
    print(f"Tecla: {e.name} | Scan code: {e.scan_code}")
    if e.name == "esc":
        keyboard.unhook_all()
        print("Encerrado.")

keyboard.on_press(show_scan_code)

keyboard.wait()  # mantém o script rodando

O que o código faz?
Exibe no terminal o nome da tecla e o scan_code sempre que você pressiona algo.

Quando você pressionar ESC, ele encerra o monitoramento.

Exemplo da saída:

Tecla: a | Scan code: 30
Tecla: space | Scan code: 57
Tecla: + | Scan code: 13
Tecla: - | Scan code: 12
Tecla: left | Scan code: 75

Dica importante:
Os scan_codes não mudam com o layout — eles são ligados à posição física da tecla no teclado.

Isso é ideal se você quer estabilidade entre layouts (como ABNT e US), mas cuidado: 
o usuário ainda verá letras/símbolos diferentes dependendo do layout ativo.


Se seu objetivo é garantir que qualquer usuário, com qualquer layout de teclado, consiga usar seu programa sem erros,
usar scan_code é a melhor escolha — ele ignora o layout lógico do teclado e usa a posição física da tecla.






