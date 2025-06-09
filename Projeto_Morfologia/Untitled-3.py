from colorama import Fore, Style, Back, init
from time import sleep
import sys
import keyboard

class Morfologia:     
    def __init__(self):
        # Inicializa o Colorama
        init(autoreset=True)

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
        current_color = None
        i = 0
        paused = False

        def toggle_pause():
            nonlocal paused
            paused = not paused

        keyboard.on_press_key("space", lambda _: toggle_pause())

        while i < len(text):
            char = text[i]
            if char == '[':  # Verifica se encontrou um possível código de cor
                end_index = text.find(']', i + 1)
                if end_index != -1:
                    color_code = text[i + 1:end_index]
                    if color_code in color_codes:
                        current_color = color_codes[color_code]
                        i = end_index + 1
                        continue
            if current_color:
                sys.stdout.write(current_color + char)
                sys.stdout.flush()
            else:
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(0.06)
            while paused:
                sleep(0.1)
            i += 1
        print(Style.RESET_ALL)

    def preposicoes(self):
        return '''Classificações das preposições:
        
        [yellow]- abaixo de, acerca de, a fim de, ao lado de, apesar de, através de, de acordo com, em vez de, junto de, para com, perto de.[reset]
        [bg_red] A palavra 'afim' junto é adjetivo para qualificar o substantivo.'''

    def menu(self):
        self.print_slow('Bem Vindo aos estudos da Morfologia para concursos com o professor Márcio Wesley...')     
        while True:
            try:
                indice = int(input('''
Estudos da ortografia:
[0] - Preposições
[25]- SAIR

Escolha:   '''))
                if indice == 0:
                    self.print_slow_2(self.preposicoes())
                    self.dots()
                elif indice == 25:
                    self.print_slow('Saindo...')
                    break
                else:							
                    self.print_slow('Escolha inválida.')
            except ValueError:
                self.print_slow('Somente valores inteiros...')


if __name__ == '__main__':
    Morfologia = Morfologia()  # Criação correta da instância
    Morfologia.menu()          # Chamada ao método menu
