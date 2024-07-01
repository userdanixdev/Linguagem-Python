# Estudos da Ortografia:
# Tonicidade 
import colorama
import colorsys
import pyttsx3

class Ortografia():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',150)
    
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def Oxitona(self):

        reset = "\033[0m"
        bold = "\033[1m"
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"

        return f'''{bold}Oxítona:{reset}\n Palavras que quando a sílaba tônica é a última: -->{red}Além{reset} ->{red}A-lém{reset} /{blue} Parati{reset} -> pa-ra-ti / {yellow}País{reset} -> Pa-ís '''

    def Paroxitona(self):
        return '''Paroxítona:\n Quando a sílaba tônica é a penúltima --> Mesa -> me-sa / Responsável -> res-pon-sá-vel / Saúde -> Sa-ú-de'''    
    
    def Proparoxitona(self):
        return '''Proparoxítona:\n Quando a sílaba tônica é a antepenúltima'''