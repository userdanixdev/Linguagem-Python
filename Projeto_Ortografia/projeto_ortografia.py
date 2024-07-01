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
            'reset':Fore.RESET
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
        self.print_slow(self.text_init())
        while True:
                try:
                    indice = int(input('''
                    Estudos da Ortografia:
                    [1]- Oxítona
                    [2]-Sair
                    []
                    []
                    []
                    \nEscolha: '''))
                    if indice == 1:
                        self.print_slow(self.Oxitona())
                        self.print_slow(self.aviso())
                    elif indice == 2:
                        self.print_slow('Saindo...')
                        break
                    else:
                        self.print_slow('Escolha inválida. Tente novamente')                        
                except ValueError:
                    self.print_slow('Somente valores inteiros.')                                                          
                
            
    
    def text_init(self):
        
        return f'''\nACENTUAÇÃO GRÁFICA : PRINCÍPIOS\n\nMenor Grupo de palavras da língua portuguesa:{self.sublinhado}{Back.YELLOW}{Fore.RED}PROPAROXÍTONAS{Style.RESET_ALL} ->{self.sublinhado} {Back.GREEN}quando a sílaba tônica é a antepenúltima.{Style.RESET_ALL}
Grupo intermediário das palavras da língua portuguesa: PAROXÍTONA -> quando a sílaba tônica é a antepenúltima.
Grupo MAIOR de palavras da língua portuguesa: PAROXÍTONAS -> quando a sílaba tônica é a última.'''
    
    def aviso(self):
        
        return f'''\t\n\t\t\t{self.sublinhado}ATENÇÃO! TODA PROPAROXÍTONA É ACENTUADA'''
        
    def Oxitona(self):        
        
        return f'''{self.f_amarelo}Oxítona:{self.reset}\n Palavras que quando a sílaba tônica é a última: -->{self.f_branco}{self.red}Além{self.reset} -> A-lém /{self.f_branco}{self.blue} Parati{self.reset} -> pa-ra-ti /{self.f_branco}{self.yellow}País{self.reset} -> Pa-ís '''

    def Paroxitona(self):
        return f'''{self.f_amarelo}Paroxítona:{self.reset}\n Quando a sílaba tônica é a penúltima --> {self.f_branco}{self.red}Mesa{self.reset} -> me-sa /{self.f_branco}{self.red} Responsável{self.reset} -> res-pon-sá-vel /{self.f_branco}{self.red} Saúde{self.reset} -> Sa-ú-de'''    
    
    def Proparoxitona(self):
        return f'''{self.f_amarelo}Proparoxítona:{self.reset}\n Quando a sílaba tônica é a antepenúltima'''


if __name__=='__main__':
        
    ortografia = Ortografia()
    ortografia.menu()