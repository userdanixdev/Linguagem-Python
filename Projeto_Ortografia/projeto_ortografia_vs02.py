# Estudos da Ortografia:
# Tonicidade 
from colorama import Fore,Style,init,Back
import sys
from time import sleep


class Ortografia():
    def __init__(self):
                 
        # Para iniciar o colorama:
        init(autoreset=True)
               
        # Para iniciar a voz:
        #self.engine = pyttsx3.init()
        #self.engine = setProperty('rate',150)
    
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    
    def dots(self):
        for c in range(4):
            print(".",end='',flush=True)
            sleep(0.06)

    def print_slow(self,text):
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        print()
       #self.speak(text)
        sleep(2)

    def print_slow_2(self,text):
        color_codes = {
            'blue':Fore.BLUE,
            'red':Fore.RED,
            'green':Fore.GREEN,
            'yellow':Fore.YELLOW,
            'write':Fore.WHITE,
            'reset':Fore.RESET,
            'sublinhado':Style.DIM,
            'negrito':Style.BRIGHT,
            'bg_red':Back.RED,
            'bg_green':Back.GREEN,
            'bg_yellow':Back.YELLOW,
            'bg_blue':Back.BLUE,
            'bg_white':Back.WHITE
        }
        current_color = None
        i = 0
        while i < len(text):
            char = text[i]
            if char == '[': # Verifica se encontrou um possível código de cor
                end_index = text.find(']',i+1)
                if end_index != -1:
                    color_code = text[i+1:end_index]
                    if color_code in color_codes:
                        current_color = color_codes[color_code]
                        i = end_index +1 
                        continue
            if current_color:
                sys.stdout.write(current_color+char)
                sys.stdout.flush()
            else:
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(0.06)
            i += 1
        print(Style.RESET_ALL)                                                                                            

    def menu(self):
        self.print_slow_2(self.text_init())
        self.print_slow_2(self.aviso())
        sleep(2)
        self.print_slow('Bem vindo aos estudos da Ortografia Brasileira para concursos...')
        self.dots()
        while True:
                try:
                    indice = int(input('''
                    Estudos da Ortografia:
                    [1]- Oxítona
                    [2]- Proparoxítona
                    [3]- Paroxítona
                    [4]
                    [5]- Sair
                    \nEscolha: '''))
                    if indice == 1:
                        self.print_slow_2(self.Oxitona())
                        self.print_slow_2(self.aviso())
                        self.dots()
                    elif indice == 2:
                        self.print_slow_2(self.Proparoxitona())
                        self.print_slow_2(self.aviso())
                        self.dots()
                    elif indice == 3:
                        self.print_slow_2(self.Paroxitona())
                        self.print_slow_2(self.aviso())
                        self.dots()                                                
                    elif indice == 5:
                        self.print_slow('Saindo...')
                        break
                    else:
                        self.print_slow('Escolha inválida. Tente novamente')                        
                except ValueError:
                    self.print_slow('Somente valores inteiros.')                                                          
                
            
    
    def text_init(self):
        
      return '''ACENTUAÇÃO GRÁFICA : PRINCÍPIOS\n\nMenor Grupo de palavras da língua portuguesa:[red]PROPAROXÍTONAS[reset] ->[red][bg_green]quando a sílaba tônica é a antepenúltima.[reset]
Grupo intermediário das palavras da língua portuguesa: [red]PAROXÍTONA[reset] ->[bg_green]quando a sílaba tônica é a antepenúltima.[reset]
Grupo MAIOR de palavras da língua portuguesa: [red]PAROXÍTONAS[reset] -> [bg_green]quando a sílaba tônica é a última.[reset]'''
    
    def aviso(self):
        
        return '''\t\n\t\t\t[bg_red]ATENÇÃO! TODA PROPAROXÍTONA É ACENTUADA'''
        
    def Oxitona(self):        
        
        return '''[red]Oxítona:[reset]\n[blue]Palavras que quando a sílaba tônica é a última:[reset] -->[bg_blue]Além[reset] ->  A -[bg_white]lém[reset] /  [bg_blue]Parati[reset] -> pa - ra - [bg_white]ti[reset] /   [bg_blue]País[reset] -> Pa - [bg_white]ís[reset] '''

    def Paroxitona(self):
        return '''[red]Paroxítona:[reset]\n[blue]Quando a sílaba tônica é a penúltima:[reset] --> [bg_blue]Mesa[reset] ->[bg_white] me[reset] - sa /[bg_blue]Responsável[reset] -> res-pon-[bg_white]sá[reset]-vel /[bg_blue]Saúde[reset] -> Sa -[bg_white]ú[reset]- de'''    
    
    def Proparoxitona(self):
        return '''[red]Proparoxítona:[reset]\nQuando a sílaba tônica é a antepenúltima : [bg_blue]Exército[reset] -> E - [bg_white]xér[reset] - ci - to 
[bg_red]\nSendo a sílaba tônica a antepenúltima, toda proparoxítona será acentuada.[reset]- [bg_yellow]LÂM[reset]PADA / LU[bg_yellow]NÁ[reset]TICA[reset]       '''


if __name__=='__main__':
        
    ortografia = Ortografia()
    ortografia.menu()