# Estudos da Ortografia:
# Tonicidade 
from colorama import Fore,Style,init,Back
import sys
from time import sleep
import keyboard
 

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
        paused = False
        def toggle_pause():
            nonlocal paused
            paused = not paused

        keyboard.on_press_key("space", lambda _: toggle_pause())
         
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

    def acentuacao(self):
        return '''[blue]Quando falamos de acentuação gráfica estamos falando do acento agudo e o cincunflexo, somente.[reset]
[blue]Onde o acento agudo vai marcar os sons abertos e o circunflexo vai marcar os sons fechados.[reset]
Na língua portuguesa temos somente três acentos: agudo, cincunflexo e o acento 'grave'o sinal indicativo de crase.
[bg_blue]O 'tio' '~' é uma marca léxica indicadora nasal mostrando que a palavra é pronunciada de forma nasal e não oral. Portanto, não insidem regras de acentuação gráfica.[reset]'''

    def acentuacao_2(self):
        return '''Acentuação Gráfica: Regra Especial 1:\n\nAcentuam-se os monossílabos tônicos terminados em 'a','e','o':
Exemplo: Chá , Fé, Só, Pó, Pé, Pá\n\n ATENÇÃO! Céu, Réu -> Não entram para a regra monossílabos tônicos por não terminarem em 'a','e','o'.
[red]CUIDADO: Monossílabo tônico não é palavra oxítona. Portanto, são regras diferentes.[reset]\n\n Por exemplo: 'Acentuam-se pela mesma regra a palavra Rapé e Pé.[bg_red][ERRADO][CADA UM TEM SUA REGRA][reset]         '''
    def acentuacao_3(self):
        return '''Acentuação Gráfica: Regra Especial 2:\n\nAcentuam-se os ditongos abertos [bg_blue]EU , EI , OI[reset] quando estiverem em posição [red]oxítona[reset]
Exemplo: Cha[bg_green]péu[reset], pas[bg_green]téis[reset], cor[bg_green]rói[reset] 
Acordo Ortográfico: 
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Ideia / i - [bg_white]de[reset] - ia. Tinha acento no 'dé'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Boia / [bg_white]bo[reset] - ia. Tinha acento no 'bó'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Geleia / ge - [bg_white]le[reset] - ia. Tinha acento no 'lé'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Joia / [bg_white]Jo[reset] - ia. Tinha acento no 'jó'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Europeia / eu - ro - [bg_white]pe[reset] - ia. Tinha o acento no 'pé'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdito. Ex: Androide / an - [bg_white]droi[reset] - de. Tinha acento no 'dró'.   
[bg_red]Atenção! Céu, Réu -> Mesma regra para ditongo aberto e não dos monosílabos tônicos por que não são terminados em 'a','e','o' e sim terminados em ditongo aberto.[reset]    '''

    def acentuacao_4(self):
        return '''Acentuação Gráfica: Regra Especial 3:\n\n Acentuam-se as vogais 'i' ou 'u' quando forem a segunda vogal de um hiato somente. Se 'i' ou u' forem a primeira vogal, não entra na regra;.
Exemplos: 
[blue]Saúde[reset] - s[bg_white]a - ú[reset] - de   [Ocorre o fenômeno HIATO em que duas vogais juntas são divididas por separação silábica.]
[blue]País[reset] - p[bg-white]a - í[reset]s   -    [Ocorre o fenômeno HIATO em que duas vogais juntas são divididas por separação silábica.]        
[bg_red]Exemplos que não resolvem:[reset]
[red]Sabíamos[reset] -> Sa - b[bg_white]í - a[reset] - mos [Ocorre o fenômeno HIATO também, porém a sílaba tônica está na antepenúltima sílaba, ou seja, proparoxítona certo. E a segunda vogal não é 'i' ou 'u' é 'a'. ] 
[red]Judiciário[reset] -> Ju - di - c[bg_white]i - á[reset] - rio / [Ocorre também o HIATO, porém a segunda vogal não é 'i' ou 'u', é 'a'.] 
[yellow]\nAcordo Ortográfico:[reset]
	- Feiura / fe[bg_white]i - u[reset] - ra / [Quando houver um hiato, antecedido por ditongo,e o hiato estiver em posição [bg_green]paroxítona[reset], ou seja,a tônica na penúltima sílaba, o acento deve ser retirado.] 
[blue]Exemplo de palavra que não perdeu acento e que entra na regra da vogal 'i' ou 'u' como segundo vogal do hiato:[reset]
[red]PIAUÍ[reset]- pi - [bg_white]au - í[reset] - [blue]O 'í' é a última tônica, ou seja, oxítona. Não perde acento.[reset] 
'''
    def acentuacao_5(self):

        return '''\nAcentuação Gráfica : Regra Especial 4: Acentos Diferenciais
[bg_red]Retirados pelo novo acordo ortográfico[reset][Partiu do pressuposto de que são classes gramaticais diferentes]
Para -  preposição sem acento / Pára verbo com acento - [bg_red]Acento diferencial Retirado:[reset] Agora é Para - Verbo
Pelo -  preposição + artigo   / Pêlo - Substantivo - [bg_red]Acento diferencial Retirado:[reset]    Agora é Pelo - Substantivo
Pela -  preposição + artigo   / Péla - Verbo - [bg_red]Acento diferencial Retirado:[reset]          Agora é Pela - Verbo
Pera -  preposição + artigo   / Pêra - Substantivo - [bg_red]Acento diferencial Retirado:[reset]    Agora é Pera - Substantivo        
Polo -  preposição + artigo   / Pólo - Substantivo - [bg_red]Acento diferencial Retirado:[reset]    Agora é Polo - Substantivo
\nAcentuação Gráfica : Acentos diferencias : Mantidos [blue]Partiu do pressuposto de que são da mesma classe gramatical.[reset]
Tem - Verbo na 3ºpessoa do singular
Têm - Verbo na 3ºpessoa do plural ( Manteve o acento )
[bg_red]( No caso do verbo 'ter' são monossílabos terminados em 'em'. Que não deveriam ser acentuados, a regra de retirar foi feita para diferenciar)\n[reset]
\nMantém - Com acento agudo na 3º pessoa do singular
Mantêm - Com acento circunflexo na 3º pessoa do plural
[bg_red]( No caso do verbo 'manter' são oxítonas terminadas em 'em', ela já vem acentuada de fábrica, está na regra da oxítonas.)\n[reset]
\nIntervém - Com acento agudo na 3º pessoa do singular 
Intervêm - Com acento circunflexo na 3º pessoa do plural\n
Vem - Verbo na 3ºpessoa do singular
Vêm - Verbo na 3ºpessoa do plural\n
Pode - Verbo - Presente
Pôde - Verbo - Pretérito\n
\n[bg_red]Exceção:[reset]\n
Por - Preposição
Pôr - Verbo\n
\n[bg_white]Acentuação Gráfica: Regra Especial 5[reset]
Acentos em vogais redobradas: todos retirados\nExemplo: Voo, veem, enjoo\n
[bg_red]Exceções[reset]\n\n[blue]Regra do Hiato: Não são acentuadas as vogais 'i'e 'u' quando formam hiato e são seguidos de M, N, NH, R ou Z.\n\n[reset]
Exemplo:\n\n JUIZ /  J[bg_white]U - IZ[reset] - [Ocorre hiato, e o [bg_white]'i' está seguido da consoante 'z'[reset],[bg_red]portanto não são acentuadas][reset]
RUIM / R[bg_white]U - IM[reset] - [Ocorre o hiato e o [bg_white]'i' está seguido da consoante'm'[reset],[bg_red]portanto não são acentuadas][reset]
RUIR / r[bg_white]u - ir[reset]- [Ocorre o hiato e o [bg_white]'i' está seguido da consoante 'm'[reset],[bg_red]portanto não são acentuadas][reset]
CONSTITUINTE / cons - ti - t[bg_white]u - in[reset] - te - [Ocorre o hiato e o [bg_white]'i' está seguido da consoante 'm'[reset],[bg_white]portanto não são acentuadas[reset]
RAINHA / r[bg_white]a - i[reset] - nha - [Ocorre o hiato e o [bg_white]'i' está seguido da consoante 'nh'[reset],[bg_white]portanto não è acentuado.\n\n[reset]
[red]ATENÇÃO![reset]\n\n[bg_green]Juízes[reset] por sua vez, no plural, possui acento. Na separação silábica da palavra, a letra 'í' se livra da consoante 'z' - ju -[bg_white]í[reset] - zes\n 
Assim ocorre também com a palavra [bg_green]RAIZ[reset], no plural, possui acento. Na separação silábica da palavra, a letra 'í' se isola da consoante 'z'. - ra - [bg_white]í[reset] - zes\n\n
[bg_yellow]Exceção: Sempre quando aparecer uma paroxítona terminada em 'n', se for ao plural , o acento deve ser retirado.[reset]
Exemplos: Hífen  - Hí  - fen / Hifens - Hi - fens ( Acento retirado para paroxítonas terminadas em 'n')\n
Pólen  - Pó - len / Polens - Po - lens (Acento retirado para paroxítonas terminadas em 'n')\n\n
Questões:\n\nAssinale a alternativa que apresenta apenas palavra que estão corretamente acentuadas, segundo a ortografia da língua portuguesa:
a) aliás - também - feiura - bárbaro:\n\n [a - li - [bg_white]ás[reset] - [red]Oxítona[reset] terminada com 'a' seguida da consoante 's'[bg_green][CORRETO][reset]
[também - [red]Oxítona[red] terminada em 'em' devidamente acentuada][reset]\n[feiura - fe[bg_white]i - u[reset] - ra - Vogais seperadas na separação silábica ocorrendo o HIATO, antecedido por ditongo 'e', [bg_green][CORRETO][reset]]
[bárbaro - [bg_white]bár[reset] - ba - ro / [red]Proparoxítona[reset] - sempre acentuada[bg_green][CORRETO][reset]]
b) vocês - enjoo  - asteróide - pássaro:\n\n [vo - [bg_white]cês[reset] -[red]Oxítona[reset] seguida de 's'[bg_green][CORRETO][reset]][en - [bg_white]joo[reset] - Vogais redobradas devem ser retirados a acentuação [bg_green][CORRETO][reset]]
[as - te - [bg_white]rói[reset] - de][[red]Paroxítona[reset] de ditongo aberto é retirado o acento.[bg_red][ERRADO][reset]][pás - sa - ro / [red]Proparoxítona[reset] devidamente acentuada de fábrica.] 
c) após  - vêem - geléia - médico:\n\n [a - [bg_white]pós[reset][red]Oxítona[reset]devidamente acentuada[bg_green][CORRETO][reset]][vê - em - Vogais redobradas, retirar acento[bg_red][ERRADO][reset]]
[ge - [bg_white]lé[reset] - ia / Penúltima tônica,[red]Paroxítona[reset] seguida de ditongo aberto é retirado o acento.[bg_red][ERRADO][reset]]
[[bg_white]mé[reset] - di - co / Proparoxítona devidamente acentuada.[bg_green][CORRETO][reset]]
d) pajé  - armazém - bocaiúva - trânsito:\n\n [pa - [bg_white]jé[reset] - [red]Oxítona[reset] terminada em 'e'[bg_green][CORRETO][reset][ar - ma - [bg_white]zem[reset]: [red]Oxítona[reset] que deveria ter o acento[bg_red][ERRADO][reset]
[bo - ca[bg_white]i - ú[reset] - va][Hiato em paroxítona antecedido por ditongo, então acento é retirado][bg_red][ERRADO][reset]]
[[bg_white]trân[reset] - si - to][[red]Proparoxítona[reset] devidamente acentuada.]
e) mocotó - perdôo - jóia - líquido: \n\n[mo - co - [bg_white][tó][reset] - [red]Oxítona[reset]: devidamente acentuada[bg_green][CORRETO][reset]][per - [bg_white]dôo[reset]-Redobro de vogais são retirados os acentos[bg_red][ERRADO][reset]]
[[bg_white]jó[reset] - ia][[red]Paroxítona[reset] ditongo aberto 'o',deve ser retirado o acento.[bg_red][ERRADO][reset]]
[bg_white]lí[reset] - qui - do / [red]proparoxítona[reset] devidamente acentuada.[bg_green][CORRETO][reset]] '''

    def questoes(self):

        return '''Questão 02:\n\nAssinale a alternativa em que a justificativa para o uso de acento gráfico está correta e a palavra entre parênteses também está corretamente acentuada
e com a mesma justificativa de uso:
a. Zodíaco: proparoxítona[CORRETO] - (Paranóico) - pa - ra - [bg_white]nói[reset] - co - Paroxítona que perde o acento, ditongo aberto 'ói'[ERRADO]
b. Imóvel: paroxítona terminada em 'l'[CORRETO][Se não tiver terminações: A(s),E(s),O(s),Em; está correto. (dócil)[dó - cil][Paroxítona terminada em 'l'][CERTO]
c. Céus: Oxítona terminada em ditongo no plural.[Monossílaba -[ERRADO]] (véu)-Monossílaba tônica
d. Astronômica: Oxítona terminada em 'a'.(evidência)[ERRADO - Astronômica é proparoxítona e 'evidência' é paroxítona terminada em ditongo 'ia']
e. Superfície: Proparoxítona terminada em ditongo decrescente.(série)[ERRADO - 'superfície' é uma Paroxítona terminada em ditongo 'ie' e 'série' é uma paroxítona também terminada em ditongo 'ie'.]\n\n
Questão 03:\n\nA organização Mundial da Saúde convocou uma reunião de urgência para tratar do vírus na Guiné Equatorial que já provocou morte de pessoas e obrigou o  país
a declarar alerta sanitário.\n\nAssinale a opção correta de acordo com as regras de acentuação gráfica.
a. 'Saúde','vírus'e 'país' são acentuadas pela mesma regra.[ERRADO][sa - ú - de / Acentua-se vogais 'i' ou 'u' quando forem a segunda vogal do hiato. O mesmo ocorre para 'país'. Ví - rus não ocorre hiato.)
b. 'Urgência' e 'Sanitário' são acentuadas por serem Proparoxítonas.[ERRADO][Nenhuma das palavras são proparoxítonas][Ambas as palavras são paroxítonas terminada em ditongo]
c. 'Saúde' e 'país' são acentuadas pela regra dos hiatos,envolvendo as vogais 'i' e 'u'.[CERTO]
d. 'Guiné','reunião' e 'já' são acentuadas por serem oxítonas terminadas em 'e','o' e 'a'.[ERRADO][A palavra 'reunião' não tem acento. e 'já' é monosílabo tônico]
e. 'Guiné' e 'já' são acentuadas por serem oxítonas terminadas em 'e' e 'a'.[ERRADO][A palavra 'já' entra na regra dos monosílabos tônicos.]\n
Questão 04:\n\nO emprego de acento na palavra 'memória' pode ser justificado por duas regras de acentuação distintas.[CORRETO]
[me - mó - ria / paroxítona terminada em ditongo ou me - mó - ri - a- eventual proparoxítona]\n
Questão 05:\n\nO emprego do circunflexo nos vocábulos 'entrevê' e 'pungência' justifica-se com base na mesma regra de acentuação gráfica.
[ERRADO - 'entrevê' é uma oxítona terminada em 'e' e 'pungência' é uma paroxítona terminada em ditongo, portanto não são as mesmas regras de acentuação gráfica]
Questão 06:\n\nA palavra 'está' recebe acento gráfico em decorrência da mesma regra que determina o emprego do acento no vocábulo 'três'.
[ERRADO / es - tá : oxítona terminada em 'a' e 'três'- monosílabas tônicas]\n
Questão 07:\n\nVocábulos como 'sinônimo' e 'rótulo' são acentuados por serem proparoxítonos.[CORRETO]\n
Questão 08:\n\nAs palavras 'famílias','auxílio' e 'área' recebem acento gráfico com base em justificativas gramaticais diferentes.[ERRADO][em justificativas iguais]
[São as mesma regra - 'famílias' paroxítona terminada em ditongo 'ia' terminada em s, 'auxilio' paroxítona terminada em ditongo 'io' e 'área', paroxítona terminada em ditongo 'ea']\n
Questão 09:\n\n As palavras 'Penitenciário','carcerária' e  'judiciário' recebem  acento gráfico com base na  mesma regra gramatical.[CORRETO]
[Penitenciário - Paroxítona terminada em ditongo, carcerária - Paroxítona terminada em ditongo, judiciário - Paroxítona terminada em ditongo]\n
Questão 10:\n\n  As palavras 'pó','só','céu' são acentuadas de acordo com a mesma regra gramatical.[ERRADO - Céu é acentuada por outra regra - Está na regra dos ditongos abertos]'''


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
                    [4]- Acentuação Gráfica
                    [5]- Questões
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
                        self.print_slow_2(self.acentuacao_2())
                        self.print_slow_2(self.acentuacao_3())
                        self.print_slow_2(self.acentuacao_4())
                        self.print_slow_2(self.acentuacao_5())
                        sleep(2)
                        self.dots()   
                    elif indice == 5:
                        self.print_slow_2(self.questoes())
                        sleep(2)
                        self.dots()
                        
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
Ex - Mesa / [bg_white]Me[reset] -  sa / Parede / pa - [bg_white]re[reset] - de / Quadro / [bg_white]Qua[reset] - dro - Item / [bg_white]I[reset] - tem           
[bg_red]*** Eu vou acentuar as paroxítonas que não terminam com A(s),E(s),O(s),EM(ns)[reset] -  Ex: Ca - [bg_white]rá[reset] - ter / [bg_white]Tá[reset] -  xi / [bg_white]Hí[reset] - fen, A - [bg_white]má[reset] - vel, [bg_white]Â[reset] - nus, [bg_white]Tó[reset] - rax, 
[bg_white]bí[reset] - ceps, [bg_white]ÁL[reset] - bum, [bg_white]ÓR[reset] - fã ***'''   

    def aviso_paroxitona_especial(self):
        
        return '''[bg_red]Paroxítonas terminadas em DITONGO : QUANDO DUAS VOGAIS SE JUNTAM SILABICAMENTE , a palavra é ACENTUADA![reset]
Ex: A palavra 'necessário' = Quando duas vogais se juntam ocorre o fenômeno DITONGO terminada em 'io'. ne - ces - [bg_white]sá[reset] - r[bg_white]io[reset] - [blue]Terminada em ditong, por isso é acentuada.        '''

    def separacao_silabica(self):
        return '''Na separação silábica das [red]paroxítonas[reset] onde a tônica é a penúltima sílaba, além de ocorrer o fenômeno do [red]Ditongo[reset] para acentua-las.
Pode ocorrer outro caso em que a palavra paroxítona pode se tornar uma eventual [red]proparoxítona[reset]: [blue]Uma separação silábica diferente da clássica.[reset]
Na separação silábica moderna , [bg_white]separando o ditongo da separação clássica alterando a sílaba tônica para a antepenúltima se tornando uma eventual proparoxítona.[reset] '''

    def sep_si_exemplo(self):

        return '''\nATENÇÃO!\n 
Mesário -->  [bg_green]Separação clássica:[reset] me - [bg_white]sá[reset] - rio     ou 	Separação alternativa: me - [bg_white]sá[reset] - ri - [bg_green]o[reset] : Separando o ditongo da separação clássica, alterando a ordem da sílaba tônica. Isolando a vogal. Deixando de ser a penúltima sílaba tônica(paroxítona) e sendo (antepenúltima) uma eventual proparoxítona.
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
Grupo MAIOR das palavras da língua portuguesa: [red]PAROXÍTONA[reset] ->[bg_green]quando a sílaba tônica é a penúltima.[reset]
Grupo INTERMEDIÁRIO de palavras da língua portuguesa: [red]OXÍTONAS[reset] -> [bg_green]quando a sílaba tônica é a última.[reset]'''
    
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
