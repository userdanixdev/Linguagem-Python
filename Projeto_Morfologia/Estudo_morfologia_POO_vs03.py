from time import sleep
import textwrap
import sys
import pyttsx3
from colorama import Fore,Style,init,Back
import keyboard

class Morfologia():

    def __init__(self):

        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',150)
        # Para iniciar o colorama:
        init(autoreset=True)

    def speak(self,text):

        self.engine.say(text)
        self.engine.runAndWait()

    def print_slow_2(self,text):

        color_codes = {
            'blue':Fore.BLUE,
            'red':Fore.RED,
            'green':Fore.GREEN,
            'yellow':Fore.YELLOW,
            'white':Fore.WHITE,
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
        paused = False
        def toggle_pause():
            nonlocal paused
            paused = not paused

        keyboard.on_press_key("space",lambda _:toggle_pause())

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
            while paused:
                sleep(0.1)
            i += 1
        print(Style.RESET_ALL)                                                                                    

    def texto_inicial(self):
        return '''Uma língua se estrutura em torno de verbos e substantivos.\nEssas são as palavras centrais.'''

    def verbo(self):
        return '''Verbo: São palavras que podem indicar ação,fenômenos,posse.'''

    def substantivo(self):
        return '''Substantivo: O nome em que damos as coisas,seres ou conjuntos de seres e objetos,ideias,estados,sentimentos
Em volte deles, existem as classes gramaticais que sempre o acompanham: artigo,pronome,adjetivo,numeral e locução adjetiva.\nAssim como o verbo é acompanhado pelo advérbio.  
                NOTA: O ADJETIVO É A PALAVRA QUE CARACTERIZA O SUBSTANTIVO, ATRIBUINDO-LHES QUALIDADE E DEFEITOS\n
Exemplos:\n\nEle é [bg_white]triste[reset] <- [bg_white]Triste[reset] é um [bg_white]adjetivo[reset] dele\n\nEle tem [bg_white]tristeza[reset] <- [bg_white]Tristeza[reset] é um sentimento de estado, um [bg_red]substantivo.[reset]
Ela é [bg_white]alegre[reset] <- [bg_white]Alegre[reset] é [bg_green]adjetivo[reset] dela\n\nEla tem [bg_white]alegria[reset] <-- Um sentimento de [bg_white]alegria[reset], um sentimento de estado, um [bg_red]substantivo.[reset]\n
Outro Exemplo importante:\n\n[bg_green]O jovem brasileiro conta com o Estado da Criança e do Adolescente.[reset]\n\n[blue]Pelo contexto da oração o brasileiro é uma qualidade do brasileiro que tem o benefício do Estado.[reset]
[bg_blue]Jovem é o substantivo na oração.[reset][blue] Nem todos os jovem contam com o benefício.[reset]\n\n[bg_green]Entre os turistas havia um jovem brasileiro e um velho japonês, os dois jovens encantados com a paisagem.[reset]\n\n
[red]Substantivos:[reset][blue]'turistas','jovem','velho','jovens'[reset] <- O numeral dois ao lado da palavra 'jovens' ajuda a identificar os substantivos\n
[red]Adjetivos:[reset][blue]'brasileiro'[reset] -[bg_white]qualificação[reset] e 'japonês' está qualificando o velho.\n\nUm brasileiro jovem tem expectativa de vida de 72 anos, enquanto um japonês jovem tem 81 anos.\n
[blue]Pelo contexto da frase, a palavra 'brasileiro' agora é o substantivo e 'jovem' é um atributo do brasileiro. Assim como o 'japonês' é o substantivo a qual o adjetivo é 'jovem'.[reset]\n\n
PC-Vunesp:\n\nNa frase: ''...pareça mais um olhar ....'', a palavra olhar é um substantivo,(Como o artigo 'um' está acompanhando a palavra 'olhar', portanto é um subs.)\nComo na frase:
a) Quero olhar bem em seus olhos e dizer tudo que sinto.[Nesse caso são dois verbos: 'quero' e 'olhar'-Locução Adverbal][bg_red][ERRADO][reset]\n
b) O jovem nem se dignou olhar para trás.[dignou = verbo,olhar = verbo][bg_red][ERRADO][reset]\n
c) Ela se pôs a olhar carinhosamente para o amado.[a = preposição de ligação 'pôs' ao 'olhar' que é verbo mesmo][bg_red][ERRADO][reset]\n
d) Esse teu olhar quando encontra o meu fala te tantas coisas [TEU=PRONOME,acompanha o substantivo, portanto é subs][bg_green][CORRETO][reset]\n
e) QUando você olhar para mim serei a pessoa mais feliz do mundo..[ERRADO]
'''

    def subs_exemplos(self):

        return '''Exemplos:\n\n[blue]Muitos livros,muitas revistas.[reset]\n[red]Subs:[reset]'livros'\n[red]Subs:[reset] 'revistas',\n'muitas/muitos':[red]Pronome Indefinido[reset][bg_white](quantidade indefinida)[reset] e não Advérbio.
[blue]Livros muitos novos,revistas muito velhas[reset]\n [bg_white]'livros'[reset]:[red]substantivo[reset],\n[bg_white]'muito':[reset][red]advérbio de intensidade para reforçar o adjetivo de livros que são 'novos'[reset]
Assim como [bg_white]'revistas':[reset][red]substantivo[reset],\n[bg_white]'muito':[reset][red]advérbio de intensidade para reforçar o adjetivo de 'revistas' que são 'velhas'.[reset]
[blue]Tenho livros demais[reset]\n\n[red]Verbo:[reset][bg_white]'tenho'[reset],\n[bg_white]'livros':[reset][red]Substantivo[reset],\n[bg_white]'demais'[reset]:[red]Pronome Indefinido pq a palavra 'demais' se relaciona com 'livros' que é substantivo.[reset]\n\n
[blue]Eram bastantes ideias interessantes[reset]\n\n[red]Verbo:[reset][bg_white]'Eram'[reset],\n[red]Substantivo:[reset][bg_white]'ideias'[reset],\n[red]Adjetivo:[reset][bg_white]'interessantes'[reset] que qualifica o nome 'ideias',\n[bg_white]'bastantes':[reset][red] Pronome Indefinido[reset]
[yellow]A quantidade é indefinida de idéias e além disso ela possui sua relação com idéias que é substantivo e não com 'eram', o verbo.[reset]\n\n
[blue]Eram idéias bastante interessantes[reset]\n\n[red]Verbo:[reset][bg_white] 'eram'[reset]\n[red]Substantivo:[reset][bg_white]'ideias'[reset],\n[red]Adjetivo:[reset][bg_white]'interessantes'[reset] está qualificando idéias que é substantivo porem a palavra 'bastante'.\n
[yellow]Veja que mudou de forma e relação, agora a relação é com o adjetivo 'interessantes' e não mais com 'idéias', portanto,virou um advérbio de intensidade.[reset]'''

    def chamada(self):
        return ''' [bg_red]A GRAMÁTICA É A FORMA COMO É ESCRITA, SEU SENTIDO E RELAÇÃO[reset] '''

    def verbos_exemplos(self):
        return '''Exemplos:\n\n[bg_white]Estudei demais[reset]\n\n[red]Verbo:[reset][bg_white]'estudei'[reset],\n[bg_white]'demais':[reset][red]Advérbio de intensidade[reset]\n\n[bg_white]Tenho livros demais[reset]\n\n[red]Verbo:[reset]'tenho',\n'livros'[red]:substantivo[reset],
'demais'[red]:Pronome Indefinido por que a palavra 'demais' se relaciona com o substantivo 'livros' e não com o verbo 'ter' de 'tenho'.[reset]'''

    def classes_gramaticais(self):
        return  '''[blue]Em torno dos verbos e substantivos outras classes gramaticais aparecem relacionadas a eles.[reset]'''

    def classes_gramaticais_substantivo(self):
        return '''As classes gramaticais que acompanham o Substantivo:\n[red]Artigo:[reset][yellow] define e particulariza o substantivo[reset]\n[red]Adjetivo:[reset][yellow] Qualidade de um substantivo, características de um ser
[red]Pronome:[reset][yellow] Substitui ou acompanha o nome[reset]\n[red]Numeral:[reset][yellow] Quantidade ou posição do nome em sequência.[reset]\n
        [bg_red]SEMPRE IRÃO ESTAR ACOMPANHADAS DO SUBSTANTIVO[reset]
[bg_rd]Locuções Adjetivas para substantivos: São grupos de duas ou mais palavras com o valor de uma só. A locução adjetiva está associada ao substantivo enquanto a locução adverbial está associada ao verbo.[reset]
'''

    def exemplo_locucao_adjetiva_adverbial(self):
        return '''Exemplo de locução adverbial:\n\n[blue]Os meus dois muito jovens amigos de Goiás chegaram bem cedo de bicicleta.[reset]\n[red]Substantivo:[reset][yellow]'amigos'[reset],\n[red]Numeral:[reset][yellow]'dois'[reset],\n[red]Artigo:[reset][yellow]'os'[reset],
[red]Adjetivo:[reset][yellow]'jovens'[reset],\n[red]Advérbio:[reset][yellow]'muito'[reset]\n[red]Locução Adjetiva:[reset][yellow]'de Goiás'[reset],[blue] a palavra 'de Goiás' está associada a 'amigos' substantivo e núcleo da oração.[reset]\n
[blue]Chegaram bem cedo de bicicleta:[reset]\n[red]Verbo:[reset][yellow]'chegaram'[reset],\n[red]Advérbio:[reset][yellow]'cedo'[reset],\n[red]Advérbio:[reset][yellow]'bem'[reset],\n[red]Locução Adverbial:[reset][yellow]'de bicicleta[reset]\n\n
[blue]O passeio com amigos é agradável.[reset]\n\n[red]Substantivo:[reset]'O passeio' ao lado do artigo 'o'.\n[yellow]'com 'amigos':[reset][red]Locução Adjetiva(preposição + substantivo)[reset]'''

    def ex_loc_adv(self):

        return ''' Exemplo:\n\n[blue]Os meus amigos chegaram cedo de Goiânia.[reset]\n[yellow] Nesse sentido,a relação 'de Goiânia' é com o verbo 'chegaram', portanto é uma locução Adverbial.[reset]\n\n
[blue]Passear com amigos é mais agradável.[reset]\n\n[red]Verbo:[reset][bg_white]'passear'[reset],\n[bg_white]'com amigos':[reset][red]Locução Adverbial pois está acompanhando o verbo passear.[reset]
'''
    def classes_gramaticais_verbo(self):
        return '''[bg_yellow]Advérbio: Pode ser o satélite do verbo, ou seja, sempre o acompanha. Além disso pode ser satélite de outro satélite.[reset]'''

    def outras_classes(self):
        return ''' Existem os conectores, palavras responsáveis pela ligação entre as palavras. Isoladamente, encontramos a interjeição para indicar sentimentos '''

    def exemplos_verbos(self):
        return '''Palavras que indicam ação. Ex: (cantei o hino)\nestado - Ex: (estou alegre)\nfenômenos - Ex: (choveu)\nPosse - Ex: (tenho um livro)'''

    def print_slow(self,text):

        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.05)
        print()
        sleep(3)

    def format_and_print(self,text):

        wrapper = textwrap.TextWrapper(width=80)
        formatted_text = wrapper.fill(text=text)
        self.print_slow(formatted_text)

    def exemplo_1(self):

        return '''Exemplo:\n\n[blue]Os meus dois jovens amigos goianos chegaram cedo.[reset]\n
[red]Substantivo:[reset][yellow] 'amigos' central da oração.[reset]\nPalavras relacionadas ao nome em torno do substantivo:\n[bg_white]'jovens'[reset]: [red]Adjetivo[reset]\n[bg_white]'dois':[reset][yellow]quantidade EXATA de amigos : Numeral[reset]
[bg_white]'os':[reset][red]artigo[reset] -\n\n[bg_red] ** Nem sempre o artigo estará ao lado do substantivo **[reset]\n[bg_white]'goianos':[reset][yellow]Adjetivo para o nome amigos[reset]\n[red]Verbo:[reset][bg_white]'chegaram'[reset][red]Advérbio:[reset][bg_white]'cedo'[reset]- que tem sua relação com chegaram -
                    '''
    def tripe(self):
        return '''\n\n[bg_white]A GRAMÁTICA É A FORMA COMO É ESCRITA, SEU SENTIDO E RELAÇÃO.[reset]'''

    def exemplo_2(self):

        return ''''Exemplo 2:\n\n [blue]Os meus dois muito jovens amigos goianos chegaram bem cedo.[reset]'
[red]Substantivo:[reset][yellow] Amigos[red]\n [blue]Seus satélites são:[reset]\n[red]Artigo:[reset][bg_white]'os'[reset],\n[red]Pronome:[reset][bg_white]'meus'[reset],\n[red]Numeral:[reset][bg_white]'dois'[reset],\n[red]Adjetivo:[reset][bg_white]'Jovens'[reset],\n[red]Adjetivo:[reset][bg_white]'goianos'[reset]
[yellow]A palavra 'muito' está associada com jovens. Note que 'jovens'(adjetivo) já é satélite associado com o nome amigos (substantivo).
Portanto 'muito' é um advérbio. Para reforçar o adjetivo 'jovens'. O advérbio é de intensidade.
O verbo 'chegaram' tem como satélite após a palavra, a outras palavra 'cedo', seu único satélite, que só pode ser advérbio de tempo 'cedo'.
A palavra 'bem' está associada com 'cedo' de 'bem cedo'. A palavra 'bem' é um satélite de 'cedo', o 'bem' reforça o advérbio 'cedo' com outro advérbio 'bem', advérbio de intensidade.[reset]'''

    def dica_1(self):

        return ''' [blue]O único advérbio que pode ser satélite do verbo, do adjetivo ou de outro advérbio é o advérbio de INTENSIDADE.
Os demais advérbios vão se relacionar com o verbo.[reset][yellow] Serão os advérbios de:\nTEMPO\nLUGAR\nMODO\nCausa\nMeio\nInstrumento\nFinalidade\nConcessão.[reset]'''

    def exemplo_verbo(self):

        return '''Exemplo : \n[blue]Ele trabalha bem.[reset]\n\n[red]Análise Morfológica:[reset]\n[yellow]Ele:[reset][red]Pronome[reset]\n[yellow]trabalha:[reset][red]Verbo[reset]\n[red]Advérbio:[reset][bg_white] bem [reset][blue](advérbio de modo associado ao verbo 'trabalha'[reset]
\nExemplo:\n[blue]Ele acordou bem tarde.[reset]\n[red]Análise Morfológica:[reset]\n[bg_white]Ele:[reset][red]Pronome[reset]\n[red]Verbo:[reset][bg_white] acordou[reset]\n[red]Advérbio:[reset][bg_white]bem[reset] -[red]Advérbio de intensidade que por sua vez está associado ao advérbio 'tarde' para reforçar\nAdvérbio:'tarde'-Advérbio de tempo associado ao verbo nuclear 'acordou'.[reset]
NOTA: A palavra 'bem' poderia ser advérbio de modo relacionada ao verbo 'acordou' mas a palavra 'tarde' está no contexto.
[yellow]Devido a isso a palavra 'bem' é de advérbio de intensidade por reforçar outro advérbio.[reset]'''
    
    def menu(self):
        while True:
            try:    
                indice =  int(input('''
                Estudos da Morfologia:
                
                [1]- Texto Inicial
                [2]- Verbo
                [3]- Substantivo
                [4]- Classes Gramaticais
                [5]- Sair
                \nEscolha:  '''))

                if indice == 1:
                    self.print_slow_2(self.texto_inicial())
                    self.print_slow_2(self.tripe())
                elif indice == 2:     
                    self.print_slow_2(self.verbo())
                    self.print_slow_2(self.exemplo_verbo())
                    self.print_slow_2(self.dica_1())
                    self.print_slow_2(self.tripe())
                elif indice == 3:
                    self.print_slow_2(self.substantivo())
                    self.print_slow_2(self.exemplo_1())
                    self.print_slow_2(self.exemplo_2())
                    self.print_slow_2(self.subs_exemplos())
                    self.print_slow_2(self.dica_1())
                    self.print_slow_2(self.tripe())
                elif indice == 4:
                    self.print_slow_2(self.classes_gramaticais())
                    self.menu_2()
                elif indice == 5:
                    self.print_slow('Saindo..')
                    break
                else:
                    self.print_slow('Escolha inválida. Tente novamente.')
            except ValueError:
                self.print_slow('Somente valores inteiros.')

    def menu_2(self):
        while True:
            try:
                opcao = int(input('''
                Classes Gramaticais:
                
                [1] - Classes Gramaticais: Substantivo
                [2] - Classes Gramaticais: Verbos
                [3] - Outras classes
                [4] - Voltar
                \nEscolha:  '''))

                if opcao == 1:
                    self.print_slow_2(self.classes_gramaticais_substantivo())
                    self.print_slow_2(self.exemplo_locucao_adjetiva_adverbial())
                    self.print_slow_2(self.dica_1())
                elif opcao == 2:
                    self.print_slow_2(self.classes_gramaticais_verbo())
                    self.print_slow_2(self.exemplo_verbo())
                    self.print_slow_2(self.ex_loc_adv())
                    self.print_slow_2(self.exemplo_locucao_adjetiva_adverbial())
                    self.print_slow_2(self.dica_1())
                elif opcao == 3:
                    self.print_slow_2(self.outras_classes())
                    self.print_slow_2(self.dica_1())
                elif opcao == 4:              
                    self.menu()
                    break
                else:
                     print('Escolha inválida. Tente novamente.')
            except ValueError:
                  print('Somente valores inteiros.')


if __name__=='__main__':
    morfologia = Morfologia()
    morfologia.menu()
                


