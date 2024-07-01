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

    def acentuacao(self):
        return '''[blue]Quando falamos de acentuação gráfica estamos falando do acento agudo e o cincunflexo, somente.[reset]
[blue]Onde o acento agudo vai marcar os sons abertos e o circunflexo vai marcar os sons fechados.[reset]
Na língua portuguesa temos somente três acentos: agudo, cincunflexo e o acento 'grave'o sinal indicativo de crase.
[bg_blue]O 'tio' '~' é uma marca léxica indicadora nasal mostrando que a palavra é pronunciada de forma nasal e não oral. Portanto, não insidem regras de acentuação gráfica.[reset]'''


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
                                       
                    [0]- Introdução                                       
                    [1]- Oxítona
                    [2]- Proparoxítona
                    [3]- Paroxítona
                    [4]- Acentuação
                    [5]- Regras Especiais                                       
                    [6]- Sair
                                       
                    \nEscolha:  '''))
                    if indice == 0:
                        self.print_slow_2(self.text_init())
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
                    elif indice == 4:
                        self.print_slow_2(self.acentuacao())
                        self.dots()   
                    elif indice == 5:
                        self.menu_2()
                        self.dots()                     
                    elif indice == 6:
                        self.print_slow('Saindo...')
                        break
                    else:
                        self.print_slow('Escolha inválida. Tente novamente')                        
                except ValueError:
                    self.print_slow('Somente valores inteiros.')                                                          
                
    def menu_2(self):
        self.dots()
        while True:
                try:
                    indice = int(input('''
                    Regras Especiais:
                                       
                    [0]- Oxítonas - Terminações mais frequentes: A(s),E(s),O(s),EM(ns)                                       
                    [1]- Paroxítonas - Terminações mais frequentes: A(s),E(s),O(s),EM(ns)                                       
                    [2]- Proparoxítona
                    [3]- Encontros Vocálicos
                    [4]- 
                    [5]- 
                    [6]- Sair
                                       
                    \nEscolha:  '''))
                    if indice == 0:
                        self.print_slow_2(self.Oxitona())
                        self.print_slow_2(self.regras_especiais())  
                        self.dots()          
                        sleep(2)                                 
                    if indice == 1:
                        self.print_slow_2(self.Paroxitona())
                        self.print_slow_2(self.regras_especiais_2())
                        self.print_slow_2(self.aviso_paroxitona_especial())
                        self.print_slow_2(self.encontros_vocálicos())
                        self.print_slow_2(self.sep_si_exemplo())
                        self.print_slow_2(self.aviso_paroxitona_especial_2())
                        self.dots()
                        sleep(2)
                    elif indice == 2:
                        self.print_slow_2(self.Proparoxitona())
                        #self.print_slow_2(self.regras_especiais_3())
                        self.print_slow_2(self.aviso())
                        self.dots()
                    elif indice == 3:
                        self.print_slow_2(self.encontros_vocálicos())
                        self.print_slow_2(self.separacao_silabica())
                        self.print_slow_2(self.sep_si_exemplo())
                        self.print_slow_2(self.aviso_paroxitona_especial_2())
                        self.print_slow_2(self.aviso())
                        self.dots()   
                    elif indice == 4:
                        self.print_slow_2(self.acentuacao())
                        self.dots()   
                    elif indice == 5:
                        pass
                        
                    elif indice == 6:
                        self.print_slow('Saindo...')
                        break
                    else:
                        self.print_slow('Escolha inválida. Tente novamente')                        
                except ValueError:
                    self.print_slow('Somente valores inteiros.')    

    def regras_especiais(self):

        return '''Para o menor grupo de palavras de língua portuguesa, as oxítonas. São acentuadas todas as palavras que possuem as terminações:
[yellow]A(s),E(s),O(s),EM(ns)[reset] - Ex: Paraná [bg_white]Termina com 'a'[reset], Café-Cafés[bg_white] Termina com 'e(s)'[reset], Mocotó - [bg_white]Termina com 'o',[reset] Armazém - [bg_white]Termina com 'm' e pode terminar com 'ens'[reset]
        '''
    def regras_especiais_2(self):

        return '''A maior parte das palavras da língua portuguesa são as [red]Paroxítonas.[reset] [bg_yellow]Não são acentuadas[reset] as palavras que possuem as terminações:
[yellow]A(s),E(s),O(s),EM(ns)[reset] -[blue]Parte do pressuposto das terminações ter uma consoante anterior. [reset]
Ex - Mesa / Me -  [bg_white]sa[reset] / Parede / pa - re - [bg_white]de[reset] / Quadro / Qua - [bg_white]dro[reset] - Item / I - [bg_white]t[reset]em           
[bg_red]*** Eu vou acentuar as paroxítonas que não terminam com A(s),E(s),O(s),EM(ns)[reset] -  Ex: Ca - [bg_white]rá[reset] - ter / [bg_white]Tá[reset] -  xi / [bg_white]Hí[reset] - fen, A - [bg_white]má[reset] - vel, [bg_white]Â[reset] - nus, [bg_white]Tó[reset] - rax, 
[bg_white]bí[reset] - ceps, [bg_white]ÁL[reset] - bum, [bg_white]ÓR[reset] - fã ***'''   

    def aviso_paroxitona_especial(self):
        
        return '''[bg_red]Paroxítonas terminadas em DITONGO : QUANDO DUAS VOGAIS SE JUNTAM SILABICAMENTE , a palavra é ACENTUADA![reset]
Ex: A palavra 'necessário' = Quando duas vogais se juntam ocorre o fenômeno DITONGO terminada em 'io'. ne - ces - sá - [bg_white]rio[reset] - [blue]Terminada em ditong, por isso é acentuada.        '''

    def separacao_silabica(self):
        return '''Na separação silábica das [red]paroxítonas[reset] onde a tônica é a penúltima sílaba, além de ocorrer o fenômeno do [red]Ditongo[reset] para acentua-las.
Pode ocorrer outro caso em que a palavra paroxítona pode se tornar uma eventual [red]proparoxítona[reset]: [blue]Uma separação silábica diferente da clássica.[reset]
Na separação silábica moderna , [bg_white]separando o ditongo da separação clássica alterando a sílaba tônica para a antepenúltima se tornando uma eventual proparoxítona.[reset] '''

    def sep_si_exemplo(self):

        return '''\nATENÇÃO!\n 
Mesário -->  [bg_green]Separação clássica:[reset] me - [bg_white]sá[reset] - rio     ou 	  Separação alternativa: me - [bg_white]sá[reset] - ri - [bg_green]o[reset] : Separando o ditongo da separação clássica, alterando a ordem da sílaba tônica. Isolando a vogal. Deixando de ser a penúltima sílaba tônica(paroxítona) e sendo (antepenúltima) uma eventual proparoxítona.
Série ---->  [bg_green]Separação clássica:[reset] [bg_white]sé[reset] - rie    	     ou	    Separação alternativa: [bg_white]sé[reset] - ri - [bg_green]e[reset]    : Separando o ditongo da separação clássica, alterando a ordem da sílaba tônica. Isolando a vogal. Deixando de ser a penúltima sílaba tônica(paroxítona) e sendo (antepenúltima) uma eventual proparoxítona.
Bactéria ->  [bg_green]Separação clássica:[reset] bac - [bg_white]té[reset] - ria 	 ou	    Separação alternativa: bac - [bg_white]té[reset] - ri - [bg_green]a[reset]: Separando o ditongo da separação clássica, aletrando a ordem da sílaba tônica. Isolando a vogal. Deixando de ser a penúltima sílaba tônica(paroxítona) e sendo (antepenúltima) uma eventual proparoxítona.
'''
    def aviso_paroxitona_especial_2(self):

        return '''
        [bg_red]** A palavra paroxítona pode ter seu acento justificado com base nessas duas regras distintas. **[SIM]
				    [Terminada com ditongo crescente ou eventual proparoxítona][reset]'''
   
    def encontros_vocálicos(self):
        return '''[\n[red]Encontros vocálicos:[reset]\n\n[red]Ditongo:[reset] [blue] Quando temos duas vogais juntas identificados na separação silábica que permanecem juntas.[reset]
[red]Tritongo:[reset] [blue] Quando temos três vogais juntas na separação silábica permanecem juntas[reset]
[red]Hiato:[reset][blue] Quando temos vogais que na separação silábica não ficam juntas.[reset]         '''

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
[bg_red]\nSendo a sílaba tônica a antepenúltima, toda proparoxítona será acentuada.[reset]- [bg_yellow]LÂM[reset] PADA / LU - [bg_yellow]NÁ[reset] - TICA[reset]       '''


if __name__=='__main__':
        
    ortografia = Ortografia()
    ortografia.menu()
