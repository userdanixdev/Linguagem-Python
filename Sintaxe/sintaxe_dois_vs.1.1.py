from colorama import Fore, Style, Back, init
from time import sleep
import sys
import keyboard

class sintaxe_dois_:     
    def __init__(self):
        # Inicializa o Colorama
        init(autoreset=True)
        self.actions={}

# Etapa 1: Captura das teclas com modificadores
    def capturar_tecla(self, nome_funcao, usar_modificador=False):
        print(f"\n➡️ Pressione a tecla para: {nome_funcao}")
        if usar_modificador:
        	print("   (Segure o modificador desejado como Ctrl, Shift, Alt e pressione a tecla)")		
        evento = keyboard.read_event()
        while evento.event_type != keyboard.KEY_DOWN:
        	evento = keyboard.read_event()		
		 # Detecta o modificador se houver:
        mod = None
        for m in ["ctrl", "shift", "alt"]:
        	if keyboard.is_pressed(m):
                 mod = m
                 break		
        print(f"✔️  Tecla '{evento.name}' capturada com modificador '{mod}' (scan_code = {evento.scan_code})")
        return (evento.scan_code, mod)

# Mapeia teclas com ou sem modificadores
    def configurar_teclas(self):
        print("🧩 Configuração das teclas:")
		#actions = {}
        self.actions[self.capturar_tecla("⏸️  Pausar / Retomar", usar_modificador=True)] = self.toggle_pause
        self.actions[self.capturar_tecla("⬅️  Voltar", usar_modificador=True)] = self.go_back
        self.actions[self.capturar_tecla("➕  Aumentar velocidade", usar_modificador=True)] = self.increase_speed
        self.actions[self.capturar_tecla("➖  Diminuir velocidade", usar_modificador=True)] = self.decrease_speed

        keyboard.on_press(self.on_key_event)

# Etapa 2: Monitorar teclado
    def on_key_event(self,e):
    	for (code, mod), func in self.actions.items():
        	if e.scan_code == code:
            	 if mod is None or keyboard.is_pressed(mod):
                	func()					

    def dots(self):
        for c in range(4):
            print(".", end='', flush=True)
            sleep(0.06)

    def print_slow(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        print()
        sleep(3)

    def print_slow_2(self, text):
        color_codes = {
            'blue': Fore.BLUE,
            'red': Fore.RED,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'white': Fore.WHITE,
            'reset': Style.RESET_ALL,
            'sublinhado': Style.DIM,
            'negrito': Style.BRIGHT,
            'bg_red': Back.RED,
            'bg_green': Back.GREEN,
            'bg_yellow': Back.YELLOW,
            'bg_blue': Back.BLUE,
            'bg_white': Back.WHITE
        }        

        # Pré-processa as linhas para melhor controle:
        lines = []
        current_line = ''
        i = 0
        while i < len(text):
            if text[i] == '[':
                end_index = text.find(']',i + 1 )
                if end_index != -1 and text [i+1:end_index] in color_codes:
                    current_line += text [i:end_index +1]
                    i = end_index + 1
                    continue
            current_line += text[i]
            if text[i] == '\n':
                lines.append(current_line)
                current_line = ''
            i += 1
        if current_line:
            lines.append(current_line)

        self.current_index = 0
        self.paused = False
        self.speed = 0.06  
        self;rewind_requested = False                                                                                    
        
    def toggle_pause():
        
        self.paused = not self.paused


    def go_back():
                
                if self.current_index > 0:
                    self.current_index -= 1
                    self.rewind_requested = True # Sinaliza para interromper a linha atual
                    sys.stdout.write("\033[F") # Move o cursor para a linha anterior
                    sys.stdout.write("\033[K")  # Limpa a linha
                    sys.stdout.flush()

    def increase_speed():
            
            self.speed = max(0.005, speed - 0.01) # 

    def decrease_speed():
            
            self.speed += 0.01

                                        
        #keyboard.add_hotkey("ctrl+space", lambda _: toggle_pause())
        #keyboard.add_hotkey("ctrl+left", lambda _: go_back())    
        #keyboard.on_press_key("f8", lambda _: increase_speed())    
        #keyboard.on_press_key("f7", lambda _: decrease_speed())

            while self.current_index < len(lines):
             line = lines[self.current_index]
             i = 0
             current_color = ''
             self.rewind_requested = False # Reseta o sinal de retorno antes de começar
             while i < len(line):
              if self.paused:
               sleep (0.1)
               continue
               if self.rewind_requested:
                break # Interrompe a linha se voltar foi pedido
                if line[i] == '[':
                 end_index = line.find(']', i + 1)
                if end_index != -1:
                 color_code = line [i + 1:end_index]
                if color_code in color_codes:
                 current_color = color_codes[color_code] 
                 i = end_index + 1
                 continue
                 sys.stdout.write(current_color + line[i])
                 sys.stdout.flush()
                 sleep(speed)
                 i += 1
                 if not self.rewind_requested:
                  self.current_index += 1 # Só avança se não foi pedido para voltar                    
				

             print(Style.RESET_ALL)
                
        

    def sintaxe_dois(self):
            return ''' 
            [blue]Sintaxe - Lingua Portuguesa:[reset]

[red]Questão 09.[reset] 


       CESPE, exemplo:
		ronomes relativos 	: [red]Troque o QUE pelo - O QUAL, A QUAL, OS QUAIS, AS QUAIS[reset]
eta.[reset]

                Portanto, 'que' é uma conjunção integrante.ronomes relativos 	: [red]Troque o QUE pelo - O QUAL, A QUAL, OS QUAIS, AS QUAIS[reset]
eta.[reset]             Portanto, 'que' é uma conjunção integrante.ronomes relativos 	: [red]Troque o QUE pelo - O QUAL, A QUAL, OS QUAIS, AS QUAIS[reset]
eta.[reset]       Portanto, 'que' é uma conjunção integrante.ronomes relativos 	: [red]Troque o QUE pelo - O QUAL, A QUAL, OS QUAIS, AS QUAIS[reset]
eta.[reset]

                Portanto, 'que' é uma conjunção integrante.

                    '''

    def osare (self):
        return '''
        Periodo Composto por Subordinação:


    TESTE:
	Os pronomes relativos 	: [red]Troque o QUE pelo - O QUAL, A QUAL, OS QUAIS, AS QUAIS[reset]
			[blue]eta.[reset]

                Portanto, 'que' é uma conjunção integrante.

        '...mas ele sempre fazia o [yellow]que[reset] a mulher lhe pedia...' ->             


                                

        '''        
    def menu (self):
                self.print_slow('Bem vindo aos estudos da sintaxe para concursos...')
                self.dots()
                while True:
                    try:        
                        indice = int(input('''
                        Estudos da sintaxe:

                        [1] - Introdução aos termos da oração do período composto
                        [2] - Exercícios de fixação: Período Composto
                        [3] - Oração Subordinada Adjetiva ( Restritiva e Explicativa )
                        [4] - Exercícios sobre orações subordinadas e coordenadas diversas
                        [5] - Introdução as orações subordinadas adjetivas
                        [6] - 
                        [0] - Sair

                        Escolha: '''))

                        if indice == 1:
                            self.print_slow_2(self.sintaxe_dois())
                        elif indice == 2:
                            self.print_slow_2(self.exercicios())     
                        elif indice == 3:
                            self.print_slow_2(self.osare()) 
                        elif indice == 4:
                            self.print_slow_2(self.exercicios_OS())
                        elif indice == 5:
                            self.print_slow_2(self.exercicios_OS())    
                        elif indice == 6:
                            self.print_slow_2(self.cn_aa())                                                                                          
                        elif indice == 0:
                            self.print_slow_2('Saindo...')                    
                            break
                        else:
                            self.print_slow('Escolha inválida. Tente novamente')
                    except ValueError:
                        self.print_slow('Somente valores inteiros')       

if __name__=='__main__':
     
    sintaxe = sintaxe_dois_()
    sintaxe.configurar_teclas() 
    sintaxe.menu()
