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
            sleep(0.06)
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
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Ideia / i - [bg_green]de[reset] - ia. Tinha acento no 'dé'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Boia / [bg_green]bo[reset] - ia. Tinha acento no 'bó'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Geleia / ge - [bg_green]le[reset] - ia. Tinha acento no 'lé'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Joia / [bg_green]Jo[reset] - ia. Tinha acento no 'jó'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdido. Ex: Europeia / eu - ro - [bg_green]pe[reset] - ia. Tinha o acento no 'pé'.
Se a posição da sílaba tônica é paroxítona, ou seja, a penúltima sílaba, o acento é perdito. Ex: Androide / an - [bg_green]droi[reset] - de. Tinha acento no 'dró'.   
[bg_red]Atenção! Céu, Réu -> Mesma regra para ditongo aberto e não dos monosílabos tônicos por que não são terminados em 'a','e','o' e sim terminados em ditongo aberto.[reset]    '''

    def acentuacao_4(self):
        return '''Acentuação Gráfica: Regra Especial 3:\n\n Acentuam-se as vogais 'i' ou 'u' quando forem a segunda vogal de um hiato somente. Se 'i' ou u' forem a primeira vogal, não entra na regra;.
Exemplos: 
[blue]Saúde[reset] - s[bg_green]a - ú[reset] - de   [Ocorre o fenômeno HIATO em que duas vogais juntas são divididas por separação silábica.]
[blue]País[reset] - p[bg-white]a - í[reset]s   -    [Ocorre o fenômeno HIATO em que duas vogais juntas são divididas por separação silábica.]        
[bg_red]Exemplos que não resolvem:[reset]
[red]Sabíamos[reset] -> Sa - b[bg_green]í - a[reset] - mos [Ocorre o fenômeno HIATO também, porém a sílaba tônica está na antepenúltima sílaba, ou seja, proparoxítona certo. E a segunda vogal não é 'i' ou 'u' é 'a'. ] 
[red]Judiciário[reset] -> Ju - di - c[bg_green]i - á[reset] - rio / [Ocorre também o HIATO, porém a segunda vogal não é 'i' ou 'u', é 'a'.] 
[yellow]\nAcordo Ortográfico:[reset]
	- Feiura / fe[bg_green]i - u[reset] - ra / [Quando houver um hiato, antecedido por ditongo,e o hiato estiver em posição [bg_green]paroxítona[reset], ou seja,a tônica na penúltima sílaba, o acento deve ser retirado.] 
[blue]Exemplo de palavra que não perdeu acento e que entra na regra da vogal 'i' ou 'u' como segundo vogal do hiato:[reset]
[red]PIAUÍ[reset]- pi - [bg_green]au - í[reset] - [blue]O 'í' é a última tônica, ou seja, oxítona. Não perde acento.[reset] 
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
\n[bg_green]Acentuação Gráfica: Regra Especial 5[reset]
Acentos em vogais redobradas: todos retirados\nExemplo: Voo, veem, enjoo\n
[bg_red]Exceções[reset]\n\n[blue]Regra do Hiato: Não são acentuadas as vogais 'i'e 'u' quando formam hiato e são seguidos de M, N, NH, R ou Z.\n\n[reset]
Exemplo:\n\n JUIZ /  J[bg_green]U - IZ[reset] - [Ocorre hiato, e o [bg_green]'i' está seguido da consoante 'z'[reset],[bg_red]portanto não são acentuadas][reset]
RUIM / R[bg_green]U - IM[reset] - [Ocorre o hiato e o [bg_green]'i' está seguido da consoante'm'[reset],[bg_red]portanto não são acentuadas][reset]
RUIR / r[bg_green]u - ir[reset]- [Ocorre o hiato e o [bg_green]'i' está seguido da consoante 'm'[reset],[bg_red]portanto não são acentuadas][reset]
CONSTITUINTE / cons - ti - t[bg_green]u - in[reset] - te - [Ocorre o hiato e o [bg_green]'i' está seguido da consoante 'm'[reset],[bg_green]portanto não são acentuadas[reset]
RAINHA / r[bg_green]a - i[reset] - nha - [Ocorre o hiato e o [bg_green]'i' está seguido da consoante 'nh'[reset],[bg_green]portanto não è acentuado.\n\n[reset]
[red]ATENÇÃO![reset]\n\n[bg_green]Juízes[reset] por sua vez, no plural, possui acento. Na separação silábica da palavra, a letra 'í' se livra da consoante 'z' - ju -[bg_green]í[reset] - zes\n 
Assim ocorre também com a palavra [bg_green]RAIZ[reset], no plural, possui acento. Na separação silábica da palavra, a letra 'í' se isola da consoante 'z'. - ra - [bg_green]í[reset] - zes\n\n
[bg_yellow]Exceção: Sempre quando aparecer uma paroxítona terminada em 'n', se for ao plural , o acento deve ser retirado.[reset]
Exemplos: Hífen  - Hí  - fen / Hifens - Hi - fens ( Acento retirado para paroxítonas terminadas em 'n')\n
Pólen  - Pó - len / Polens - Po - lens (Acento retirado para paroxítonas terminadas em 'n')\n\n
Questões:\n\nAssinale a alternativa que apresenta apenas palavra que estão corretamente acentuadas, segundo a ortografia da língua portuguesa:
a) aliás - também - feiura - bárbaro:\n\n [a - li - [bg_green]ás[reset] - [red]Oxítona[reset] terminada com 'a' seguida da consoante 's'[bg_green][CORRETO][reset]
[também - [red]Oxítona[red] terminada em 'em' devidamente acentuada][reset]\n[feiura - fe[bg_green]i - u[reset] - ra - Vogais seperadas na separação silábica ocorrendo o HIATO, antecedido por ditongo 'e', [bg_green][CORRETO][reset]]
[bárbaro - [bg_green]bár[reset] - ba - ro / [red]Proparoxítona[reset] - sempre acentuada[bg_green][CORRETO][reset]]
b) vocês - enjoo  - asteróide - pássaro:\n\n [vo - [bg_green]cês[reset] -[red]Oxítona[reset] seguida de 's'[bg_green][CORRETO][reset]][en - [bg_green]joo[reset] - Vogais redobradas devem ser retirados a acentuação [bg_green][CORRETO][reset]]
[as - te - [bg_green]rói[reset] - de][[red]Paroxítona[reset] de ditongo aberto é retirado o acento.[bg_red][ERRADO][reset]][pás - sa - ro / [red]Proparoxítona[reset] devidamente acentuada de fábrica.] 
c) após  - vêem - geléia - médico:\n\n [a - [bg_green]pós[reset][red]Oxítona[reset]devidamente acentuada[bg_green][CORRETO][reset]][vê - em - Vogais redobradas, retirar acento[bg_red][ERRADO][reset]]
[ge - [bg_green]lé[reset] - ia / Penúltima tônica,[red]Paroxítona[reset] seguida de ditongo aberto é retirado o acento.[bg_red][ERRADO][reset]]
[[bg_green]mé[reset] - di - co / Proparoxítona devidamente acentuada.[bg_green][CORRETO][reset]]
d) pajé  - armazém - bocaiúva - trânsito:\n\n [pa - [bg_green]jé[reset] - [red]Oxítona[reset] terminada em 'e'[bg_green][CORRETO][reset][ar - ma - [bg_green]zem[reset]: [red]Oxítona[reset] que deveria ter o acento[bg_red][ERRADO][reset]
[bo - ca[bg_green]i - ú[reset] - va][Hiato em paroxítona antecedido por ditongo, então acento é retirado][bg_red][ERRADO][reset]]
[[bg_green]trân[reset] - si - to][[red]Proparoxítona[reset] devidamente acentuada.]
e) mocotó - perdôo - jóia - líquido: \n\n[mo - co - [bg_green][tó][reset] - [red]Oxítona[reset]: devidamente acentuada[bg_green][CORRETO][reset]][per - [bg_green]dôo[reset]-Redobro de vogais são retirados os acentos[bg_red][ERRADO][reset]]
[[bg_green]jó[reset] - ia][[red]Paroxítona[reset] ditongo aberto 'o',deve ser retirado o acento.[bg_red][ERRADO][reset]]
[bg_green]lí[reset] - qui - do / [red]proparoxítona[reset] devidamente acentuada.[bg_green][CORRETO][reset]] '''

    def questoes(self):

        return '''Questão 02:\n\nAssinale a alternativa em que a justificativa para o uso de acento gráfico está correta e a palavra entre parênteses também está corretamente acentuada
e com a mesma justificativa de uso:
a. Zodíaco: proparoxítona[CORRETO] - (Paranóico) - pa - ra - [bg_green]nói[reset] - co - Paroxítona que perde o acento, ditongo aberto 'ói'[ERRADO]
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

    def hifen(self):
        return '''\n\nBem vindo aos estudos do emprego do Hífen:\nDefinição de Hífen:\n [blue]- Marcar a união de vocábulos entre palavras compostas ou palavras formadas por prefixo + radical[reset]
[yellow]- O hífen serve para marcar ênclise e mesóclise(colocações pronominais)[reset]\n[green]- Serve também para marcar a separação silábica.[reset]\n[red]Existem dois tipos de emprego do hífen na ortografia brasileira:[reset]\n         
[yellow]Hífen com 'prefixos': Prefixo + hífen + palavra(radical)[reset] e o Hífen sem 'prefixos':palavra + hífen + palavra.[reset]\n\n
[bg_green]Hífen com 'prefixos': Prefixo + hífen + palavra(radical)[reset]\nPrefixo é um afixo, o Afixo é uma forma presa da lingua portuguesa em que ele pode não existir sozinho como palavra.
[yellow]Afixos são parasitas que se juntam a uma palavra existente. Existe dois tipos de afixos:[reset]\n[blue]Os afixos que são colocados antes da palavra: Ele é chamado de prefixo.[reset]\n[blue]E os afixos que são colocados depois das palavras: Ele é chamado de sufixo[reset]
[green]Mas como estamos falando do uso do hífen, só nos interessa o uso do prefixo. [reset]\n
Exemplo:\n\n [bg_green]'Pré-escola'[reset]\nO [bg_green]'pré'[reset] na lingua portuguesa não existe. Para que o 'pré' exista eu preciso adicionar uma palavra: pré- [bg_green]escola[reset], pré - [bg_green]infância[reset], pré - [bg_green]história.[reset]
[yellow]Visto os exemplos Eu vou precisar de uma palavra existente para adicionar o prefixo.[reset]\nExemplos:
[blue]- Super[reset]
[yellow]- Anti[reset]
[green]- Micro[reset]
[blue]- Anti [reset]
[blue]- Inter[reset]
[yellow]- Sub[reset]
[green]- Pré[reset]
[blue]- Vice[reset]
[yellow]- Ex [reset]\n\n[bg_red][TODAS ESSES PREFIXOS PRECISAM ESTAR JUNTOS COM UMA PALAVRA][reset]\n\n
[red]Regras especiais 01:[reset]\n
[red]Palavras iniciadas com 'H':[reset][blue]homem ,  herói,  histamínico[reset][green]  sempre colocará hífen antes da palavra para o prefixo entrar :[reset]
[bg_green]super[reset] [bg_yellow]-[reset] homem ,  [bg_green]super[reset][bg_yellow]-[reset] herói, [bg_green]anti[reset][bg_yellow]-[reset]histamínico
[bg_red]**Existe um único caso na língua portuguesa em que isso é diferente: Sub-humano ou subumano . São aceitas as duas formas**[reset]\n\n
[red]Regras especiais 2:[reset]\nDe acordo com o acordo ortográfico temos:\n [red]Prefixos terminados em VOGAL:[reset]
\n[yellow]Se o prefixo terminado em vogal for igual ao radical ( igual a palavra ) será separado por hífen.[reset]\n[yellow]Se o prefixo terminado em vogal for diferente do radical( da palavra) será juntado,será unido. Sem o uso do hífen.[reset]\n\n
Exemplos de uso:\nMicr[bg_green]o-o[reset]ndas - Repare que o prefixo 'micro' é terminado em vogal [bg_green]'o'[reset] e o radical [bg_green]'ondas'[reset] é iniciado por [bg_green]'o'[reset].\n[bg_red] De acordo com o novo acordo ortográfico, será separado por hífen o prefixo terminado em vogal igual ao do radical da palavra.[reset]
\nAnt[bg_green]i-i[reset]nflamatório - Repare que o prefixo [bg_green]'anti'[reset] é terminada na vogal [bg_green]'i'[reset] e o radical [bg_green]'infla...'[reset] é iniciada com a vogal [bg_green]'i'[reset].[bg_red] Portanto, será separado por hífen o prefixo terminado em vogal igual ao do radical da palavra.[reset]
\nE quando que vou unir? Sem o uso do hífen?\n[blue]De acordo com a nova ortografia se o prefixo terminado em vogal for diferente do radical da palavra...  será juntado, será unido. Sem o uso do hífen.\n\n[reset]\n
\n[red]Exemplo:[reset][yellow]autoescola[reset]\n A palavra autoescola o prefixo [bg_green]'auto'[reset] termina com [bg_green]vogal[reset] e o radical da palavra [bg_green]'escola'[reset] inicia com a vogal [bg_green]'e'[reset].[blue] Portanto, de acordo com a nova ortografia brasileira, será juntada, será unida a palavra, sem uso do hífen, em que o prefixo terminado em vogal seja diferente da vogal inciada pelo radical.[reset]\n
[red]Caso Especial 1:[reset]\n\n[blue]Se o prefixo terminado em vogal e o radical da palavra ser iniciado por consoante, será feita a união do prefixo com a palavra, sem o uso do hífen.[reset]\n\n
[red]Exemplo:[reset] [bg_green]antitetânica[reset] - o prefixo [bg_green]'anti'[reset] termina com a vogal [bg_green]'i'[reset] e o radical da palavra [bg_green]'tetânica'[reset] inicia com a consoante [bg_green]'t'[reset], sendo assim, será feita a união do prefixo com a palavra, sem o uso do hífen.\n
[bg_red]Exceção:[reset]\n\n[yellow]Palavras com o radical iniciadas com a consoante 'R' ou 'S' é obrigatório duplicá-las na união do prefixo com a palavra.[reset]\n\n
Exemplo:\n[bg_green]Minissaia[reset] - O prefixo [bg_green]'mini'[reset] terminado com uma vogal [bg_green]'i'[reset] e o radical da palavra [bg_green]'saia'[reset] iniciada com uma consoante [bg_green]'S'[reset], terá sua letra duplicada e unida ao prefixo.\n
[red]Atenção! Seria um problema para a língua portuguesa, em relação a pronúncia da palavra unida, de acordo com o caso especial : minisaia.[reset]\n
Exemplo 2:\n [bg_green]Antirrábica[reset] - O prefixo [bg_green]'anti'[reset] terminado com vogal e o radical da palavra [bg_green]'rábica'[reset] iniciada com a consoante [bg_green]'R'[reset], terá sua letra duplicada e unida ao prefixo. \n
[red]Exceção 2:[reset]\n\n[bg_green]O ÚNICO prefixo que não irá se separar e vai se unir é o 'co'. Único que mesmo sendo vogais iguais ao do radical HAVERÁ A UNIÃO.[reset]\n
Exemplos: [bg_green]Coor[reset]denação,  [bg_green]coop[reset]eração\n\nRegra Especial 3:\n\nSe o prefixo terminado em CONSOANTE for [bg_green]IGUAL[reset] A CONSOANTE do radical da palavra, o prefixo e a palavra serão separadas por hífen.\n
Exemplo:\n\nA palavra 'Inter-regional', o prefixo [bg_green]'inter'[reset] terminado com a consoante [bg_green]'r'[reset] e a palavra [bg_green]'regional'[reset] iniciada com a consoante [bg_green]'r'[reset] devem ser separadas por hífen.\n
[bg_green]Se o prefixo terminado em CONSOANTE for DIFERENTE da CONSOANTE do radical da palavra, o prefixo e a palavra seráo unidos, sem o uso do hífen.[reset]\n
\nExemplo:\n\nA palavra 'hipermercado', seu prefixo é [bg_green]'hiper'[reset] terminado com a consoante [bg_green]'r'[reset] e a palavra [bg_green]'mercado'[reset] iniciada com a consoante [bg_green]'m'[reset] devem ser [bg_green]UNIDAS[reset], sem o uso do hífen.\n
[red]Exceção:[reset]\n[yellow]Na palavra 'Sub-raça' se for pela regra com o acordo ortográfico, ocorre um prejuízo da língua portuguesa causando uma mudança na pronúncia.\n[reset]
[bg_red]Portanto no caso da palavra 'sub-raça' haverá hífen para não alterar a pronúncia da palavra.[reset]\n
[bg_green]Se o prefixo terminado em CONSOANTE se encontrar com uma VOGAL no radical da palavra, o prefixo e a palavra serão unidos, sem o uso do hífen.[reset]\n
Exemplo:\n\nA palavra 'superinteressante', seu prefixo [bg_green]'super'[reset] terminado com a consoante [bg_green]'r'[reset] e o radical da palavra interessante iniciada com VOGAL [bg_green]'i'[reset] deverão ser unidos, sem o uso do hífen.\n
Casos Especiais 4:\n\nPrefixos terminados em som com consoantes nasais: 'm' e 'n'.\n[blue]Caso um prefixo tenha a consoante com sons nasais 'm' ou 'n', automaticamente irá contaminar o som do radical da palavra caso tenha uma Vogal de início.[reset]\n
Exemplo:\n\n[yellow] Pan - Americano[reset] / O [bg_green]'n'[reset] do prefixo [bg_green]'pan'[reset] irá contaminar o som nasal da vogal [bg_green]'a'[reset] da palavra [bg_green]'Americano'[reset], sendo obrigatório a separação por hífen.\n
[blue]Caso um prefixo que tenha a consoante com som nasal 'm' ou 'n', automaticamente irá contaminar o som do radical da palavra caso tenha uma consoante de início.[reset]\n
Exemplo:\n\n [yellow]Circum-meridiano[reset] / O [bg_green]'m'[reset] do prefixo [bg_green]'circum'[reset] irá contaminar o som nasal da consoante [bg_green]'m'[reset] de [bg_green]'meridiano'[reset], sendo obrigatório a separação por hífen.\n
Casos Especiais 5:\n\nPrefixos que sempre exigem hífen:\n\nQuais são os prefixos que sempre exigem hífen?\n
[yellow]EX[reset]
[blue]SEM[reset] 
[green]ALÉM[reset]
[yellow]AQUÉM[reset]
[blue]RECÉM[reset]
[green]PÓS[reset]
[yellow]PRÉ[reset]
[blue]PRÓ[reset]
[green]VICE[reset]
[bg_red][TODOS ESSES PREFIXOS SEMPRE VÃO EXIGIR OBRIGATORIAMENTE O EMPREGO DO HÍFEN][reset]
	                [bg_green][ex, sem, além, aquém, recém, pós, pré, pró, vice][reset]

'''
    def hifen_2(self):
        return '''\n\n Hífen entre palavras: Palavra + hífen + palavra\n[blue]São palavras compostas em que os integrantes da composição possuam:A primeira palavra existe sozinha e após o hífen, a segunda palavra também existe sozinha.[reset]\n
1. Sílaba tônica própria\n2. Unidade de significado (duas palavras que juntas formam uma palavra com outro significado)\n3. Ausência de conectivo (preposição)\n
Exemplos: sexta-feira ,   mesa-redonda,  criado-mudo,  beija-flor,   casca-grossa,  ferro-velho\n\n[bg_green]Tendo os 3 elementos, o uso do hífen será aplicado.[reset]\n\n[bg_green]Quando é um substantivo composto, o uso do hífen é aplicado.[reset]
Acordo Ortográfico:\nNão se usa mais o hífen em certas palavras que perderam a noção de composição: girassol,mandachuva,pontapé,paraquedas.\n
Acordo Ortográfico 2:\n[blue]Não se usa hífen em palavras dotadas de elementos de ligação (preposição):[reset]\n
[yellow]Azeite de dendê[reset] -[blue]Com preposição, sem o uso do hífen.[reset]\n[yellow]Água de coco[reset] -[blue] Com preposição, sem o uso do hífen.[reset]
[yellow]Dia a dia[reset] -[blue] Com preposição, sem o uso do hífen.[reset]\n[yellow]Calcanhar de Aquiles[reset] -[blue] Com preposição, sem o uso do hífen.[reset]
[yellow]Pão de ló[reset] - [blue]Com preposição, sem o uso do hífen.[reset]\n[yellow]Fim de semana - Com preposição, sem o uso do hífen.[reset]
[yellow]Corpo a corpo[reset] -[blue] Com preposição, perdeu o uso do hífen.[reset]\n[yellow]Mão de obra[reset] -[blue]Com preposição, sem o uso do hífen.[reset]
[red]Exceção:[reset] \n[yellow]água-de-colônia [reset]-[blue] Continua com hífen[reset]\n[yellow]cor-de-rosa[reset] -[blue] Continua com hífen[reset]
[yellow]mais-que-perfeito[reset] -[blue] Continua com hífen [reset]\n[yellow]pé-de-meia[reset] -[blue] Continua com hífen[reset]\n[yellow]gota-d'agua.[reset] -[blue] Continua com hífen[reset]
Além de nomes de espécies botânicas ou zoológicas: [bg_green]Também recebem hífen[reset]\n[yellow]gato-do-mato[reset] -[green] Espécie zoológica[reset] -[blue] Com preposição e hífen[reset]
[yellow]andorinha-de-rabo-branco[reset][green] - Espécie Zoológica -[reset][blue] Com preposição e hífen[reset]\n[yellow]cravo-da-índia[reset][green] - Espécie botânica com preposição[reset][blue] e uso do hífen.[reset]
[yellow]dente-de-leão[reset] -[green] Espécie botânica [reset] [blue]com preposição e uso do hífen.[reset]\n
Uso do hífen nas palavras [red]MAL e BEM:[reset]\nApós a palavra 'mal' emprega-se o hífen quando a palavra a seguir for iniciada por [yellow]vogal[reset], a letra [yellow]H[reset] ou a [yellow]letra L[reset]
Exemplo:\n [bg_green]mal-estar[reset] - Após a palavra 'mal' temos uma palavra com radical vogal 'e', aplica-se o hífen. 
[bg_green]mal-humorado[reset] - Após a palavra 'mal' temos uma palavra com radical consoante 'H', aplica-se o hífen.
[bg_green]mal-limpo[reset] - Após a palavra 'mal' temos uma palavra com radical consoante 'L', aplica-se o hífen.
[bg_green]malcriação[reset] - Após a palavra 'mal' temos uma palavra com radical consoante 'C', NÃO aplica-se o hífen.
[bg_green]malcheiroso[reset] - Após a palavra 'mal' temos uma palavra com radical consoante 'C', NÃO aplica-se o hífen.\n
[blue]Após a palavra BEM[reset], emprega-se o hífen quando a palavra for iniciada em [bg_green]VOGAIS[reset] e [bg_green]CONSOANTES.[reset]
Exemplo:\n[yellow]bem-aventurado[reset],\n[yellow]bem-estar[reset],\n[yellow]bem-vindo[reset],[yellow]bem-casado[reset]\n,[yellow]bem-nascido[reset]
[red]CUIDADO. Existem palavras em que existem a forma com hífen e sem hífen no verbo do infinito[reset]\n
[yellow]benfazer ou bem-fazer[reset]   -  Ocorre a mudança da letra 'n' para o 'm'. Se for junto, sem o hífen, usa-se 'n'. Se for com hífen, usa-se 'M'
[yellow]benquerer ou ben-querer[reset] -  Ocorre a mudança da letra 'n' para o 'm'. Se for junto, sem o hífen, usa-se 'n'. Se for com hífen, usa-se 'M'
[yellow]bendizer ou bem-dizer[reset]   -  Ocorre a mudança da letra 'n' para o 'm'. Se for junto, sem o hífen, usa-se 'n'. Se for com hífen, usa-se 'M'\n
[blue]Uso do hífen após a palavra não ou quase:[reset]\n[yellow]Sempre dispensam o hífen[reset]\n[bg_green]Exemplo: quase crime, quase nada, não comprimento, não engajado.[reset]
'''
    def hifen_questoes(self):

        return '''Segundo o novo acordo ortográfico a palavra que deveria ser grafada com hífen é:
a. corréu [ERRADO][Não há hífen por ser duas consoantes iguais e o uso do prefico 'co']
b. antiimperalista [CORRETO][Nesse caso, como o prefixo 'anti' termina com vogal e o radial da palavra 'imperalista também, ocorre o uso do hífen]
c. minissaia[ERRADO][Não ocorre o uso do hífen para essa palavra, por ser um radical de consoante S recebe o dobro da vogal e a união da palavra]
d. antissocial[ERRADO][Não há necessidade de hífen pela regra especial do radical da palavra ser iniciado com 'S', recebe o dobro e união do prefixo com a palavra]
e. supermercado[errado][Não há necessidade de hífen para essa palavra por que quando um prefixo terminado em consoante é diferente da consoaante do radical da palavra ocorre uma união]\n\n
2. No último período do primeiro parágrafo, a substituição de 'antidireito' por anti-direito faria o texto ficar em desacordo com a ortografia oficial vigente no Brasil.\n
[green][CORRETA][A Questão está correta em dizer que ficara em desacordo com a ortografia oficial vigente, quando há uma vogal terminado no prefixo e o radical da palavra for consoante, há união da palavra][reset]\n
3. No último período do primeiro paragráfo, o emprego do hífen em 'ético-jurídicos' em 'grandes desafios ético-jurídicos' é facultativo, razão por que estaria igualmente correta a grafia eticojurídicos.
[red][ERRADO][Como são duas palavras que formam uma só, desafios 'éticos-juríficos', a grafia com hífen é a única correta. Unir as palavras está errado.][red]\n
4. Assinale a alternativa que apresenta todas as palavras grafadas com hífen corretamente:\n A.[blue]boto-cor-de-rosa[reset],[yellow]pé-de-meia[reset],[green]erva-doce[reset],[blue]micro-ondas[reset]:
\n[blue]boto-cor-de-rosa[reset]: [bg_green][CORRETO][reset][green][Mantém o hífen em palavras com o nome de espécie zoológica][reset]\n[blue]pé-de-meia[reset][bg_green][CORRETO][reset][green][Pela preposição 'de' não deveria ter hífen, porém há um exceção na regra da ortografia, pé-de-meia manteve o hífen][reset]
[blue]erva-doce[reset][bg_green][CORRETO][reset][green][Nome de espécie botânica, uso correto do hífen][reset]\n[blue][micro-ondas][reset][yellow][prefixo terminado em vogal com a mesma vogal do radical da palavra, uso correto do hífen][reset][bg_green][CORRETO][reset]\n
B.[blue]peixe-boi[reset],[yellow]auto-escola[reset],[green]co-fundador[reset],[blue]ultrasom[reset]:\n\n[yellow]peixe-boi[reset][green][CORRETO][reset][Grafia correta]\n[yellow]auto-escola[reset][bg_red][ERRADO][reset][red][Devemos juntar as palavras, sem o uso do hífen quando temos uma vogal terminada no prefixo diferente da vogal iniciada no radical]
[yellow]co-fundador[reset][bg_red][ERRADO][reset][red][Devemos juntar todas as palavras com o prefixo 'co', sem usar o hífen][reset]\n[yellow]ultrasom[reset][bg_red][ERRADO][reset][red][Devemos duplicar as letras com o radical da palavra iniciadas com R ou S, o correto seria 'ultrassom'][reset]
C.[blue]super-claro[reset],[yellow]pé-de-moleque[reset],[green]co-orientador[reset],[blue]anti-higiênico[reset]:\n\n[yellow]super-claro[reset][bg_red][ERRADO][reset][red][O prefixo terminado em consoante é diferente da consoante do radical iniciado da palavra, portanto, é união. Sem uso do hífen.][reset]
[yellow]pé-de-moleque[reset]:[bg_red][ERRADO][reset][red][A palavra perdeu seu hífen, não está na exceção, a grafia correta agora é 'Pé de moleque']\n[yellow]Co-orientador[reset][bg_red][ERRADO][reset][red]O prefixo 'CO' deve ser unido, sempre.[reset]
[yellow]anti-higiênico[reset][bg_green][CORRETO][reset][greeb][Além do prefixo 'anti' ser obrigatório o uso do hífen, a palavra começa com 'H',poranto,, uso do hífen correto.][reset]
D.[blue]mini-saia[reset],[yellow]curta-metragem[reset],[green]carro-forte[reset],[blue]anti-semitismo[reset]:\n
[yellow]mini-saia[reset][bg_red][ERRADO][reset][red][A grafia está errada, consoantes inciadas em R ou S no radical da palavra devem ser duplicadas e o prefixo unida a palavra][reset]
[yellow]curta-metragem[reset][bg_green][CORRETO][reset][green][A grafia está correta para duas palavras que significam uma só]\n[yellow]carro-forte[reset][bg_green][CORRETO][reset][A grafia está correta para as duas palavras que significam uma só]
[yellow]anti-semitismo[reset][bg_red][ERRADO][reset][green][Radical da palavra iniciado com 'S' é duplicado e unido ao prefixo][reset]
E.[blue]pau-de-arara[reset],[yellow]camisa-de-força[reset],[green]pimenta-doreino[reset],[blue]agro-industrial[reset]:\n\n
[yellow]pau-de-arara[reset]:[bg_red][ERRADO][reset][O correto seria sem o hífen, 'pau de arara', sem os hífens]\n[yellow]camisa-de-força[reset][bg_red][ERRADO][reset][red][Palavra composta com preposição, grafia incorreta. Sem o uso do hífen, o correto seria camisa de força.][reset]
[yellow]pimenta -doreino[reset]:[bg_red][ERRADO][reset] O correto seria pimenta-do-reino, mesmo com preposição é uma espécie botânica. De acordo com novo acordo ortográfica, mantém o hífen.
[yellow]agro-industrial[reset]:[bg_red][ERRADO][reset]O prefixo 'agro' possui a vogal 'o' diferente da vogal 'i' do radical da palavra 'industrial', portando é união da palavra. Uso incorreto do hífen.\n
5. Analise as afirmativas a seguir e dê valores Verdadeiro ou Falso:\n
Usa-se o hífen se a última letra do prefixo e a primeira do elemento seguinte foram iguais. Ex: anti- inflacionário, micro-ondas.[bg_green][CORRETO][reset]\n
Não se usa hífen nas palavras compostas. Ex: médicocirurgião,anoluz.[bg_red][ERRADO][reset][red][Usa-se o hífen em palavras compostas, médico-cirurgião, ano-luz][reset]\n
Dobra-se a consoante, sem hífen , se o prefixo terminar por vogal e o elemento seguinte começa com R ou S. Exemplo: ultrassom, suprarrenal.[bg_green][CORRETO][reset][Uso correto da regra especial]

        '''
    def escrita_word_s(self):

        return ''''\nOrtografia Oficial - Escrita:\n
[red]Palavras escritas com S: O emprego do S -[reset] \n\nNo processo de derivação do verbo para o substantivo são escritos com S substantivos abstratos originados de verbos cujas terminações :
[yellow]DER, DIR, TIR, TER, MIR e GIR[reset] são retiradas. Tais vocábulos derivados terminarão com [green]SÃO OU SSÃO[reset]:\n\n-Preten[red]der[reset] >> preten[red]são[reset]\nApreen[red]der[reset] >> apreen[red]são[reset]
-compreen[red]der[reset] >> compreen[red]são[reset]\n-expan[red]dir[reset] >> expan[red]são[reset]\n-Agre[red]dir[reset] >> agres[red]são[reset]\n-Inver[red]ter[reset] >> Inver[red]são[reset]
- Permi[red]tir[reset] >> Permis[red]são[reset]\nImpri[red]mir[reset] >> Impres[red]são[red]\nRepri[red]mir[reset] >> Repres[red]são[reset]\n-Asper[red]gir[reset] >> Asper[red]são[reset]\n-Submer[red]gir[reset] >> Submer[red]são[reset] 
[blue]Tem palavras do verbo em que em seu subtantivo abstrato apresentará a terminação 'ção' usado no lugar do 'R'.[reset]
competi[red]r[reset] >> Competi[red]ção[reset]\nate[red]r[reset] >> aten[red]ção[reset]\nRete[red]r[reset] >> Reten[red]ção[reset]\nFundi[red]r[reset] >> fundi[red]ção[reset]\nReparti[red]r[reset] >> Reparti[red]ção[reset]\n
\nNa indicação de títulos , denominação ou origem emprega-se a letra 'S' nos sufixos ÊS,ESA,ESIA,ISA:\n\ningl[red]ês[reset],ingl[red]esa[reset]\nfranc[red]ês[reset],franc[red]esa[reset]\n-burgu[red]ês[reset],burgu[red]esa[reset],burgue[red]sia[reset]
\nfregu[red]ês[reset],fregue[red]sia[reset],fregu[red]esa[reset]\n-poet[red]isa[reset],\nbaron[red]esa[reset],\nprinc[red]esa[reset]\n
Para os substantivos abstratos que dão nome a qualidade os quais derivam de adjetivos empregam-se os sufixos EZ,EZA:\n\n[red] Adejtivo:[reset] belo    >>   beleza :[red] Substantivo [reset]\n[red]Adjetivo:[reset] certo   >> certeza[reset]:[red] Substantivo[reset]\n
[red]Adjetivo:[reset] mole    >>  moleza:[red] Substantivo  [reset]\n[red]Adjetivo:[reset] pobre   >> pobreza:[red] Subs[reset]\n[red]Adjetivo:[reset] frio   >> frieza: [red]Subs [reset]\n[red] Adjetivo:[reset] frígido >> frigidez:[red] Subs [reset]\n[red] Adjetivo:[reset] macio   >>  maciez:[red] Subs [reset]
[red]Adjetivo:[reset] ácido   >>  acidez: [red]Subs[reset]\n [red]Adjetivo:[reset] pálido  >> palidez: [red]Sub[reset],[red]Adjetivo:[reset] polido  >> polidez: [red]Subs[reset]\n
São também grafados com S os sufixos gregos ASE,ESE,ISE,OSE:\nExemplos:\n\n fase,  aférese, catequese, ascese, análise, eletrólise, micose, lordose, metamorfose\n\n
[red]Exceções:[reset]\n\n [yellow]Deslize é com a letra 'Z[reset]\n[yellow]Gaze é com a letra 'Z'.[reset]\n[yellow]Deslizar é com a letra 'Z'.[reset]\n[yellow]Liso é com a letra 'S'.[reset]\n 
[blue]São grafadas com S as formas dos verbos QUERER, PÔR e seus derivados:[reset]\nExemplo:\n\n[yellow]Quisera[reset] eu ter essa sorte! (3º pessoa do singular pretérito mais-que-perfeito 'quisera' do verbo no infinito querer)\n
Sempre[yellow] quiseram viajam,mas nunca puderam.[reset] (3º pessoa do plural do pretérito mais-que-perfeito 'quiseram' do verbo no infinito querer)\nQuando você [yellow]quiser[reset] o livro de volta,é só me avisar. (3º pessoa do singular no futuro do subjuntivo 'quiser' do verbo no infinito quer)
Se de fato ela [yellow]quisesse[reset],terminaria o namoro.(3º pessoas do singular do futuro do subjuntvo 'quisesse' do verbo no infinito querer)
[yellow]Puseram[reset] a culpa do amanhecer no pobre galo.(3º pessoa do plural do indicativo pretérito-mais-que-perfeito 'puseram' do verbo no infinito pôr)\nEle se [yellow]propusera[reset] a ajudar antes mesmo de a situação se agravar.(3º pessoas do singular do modo indicativo no tempo pretério-mais-que-perfeito 'propusera' do verbo no infinito propôr)
Quando eu [yellow]compuser[reset] uma canção, será de amor.(1º pessoa do singular do modo subjuntivo do futuro 'compuser' do verbo no infinito compor)\nSe eu [yellow]dispusesse[reset] de mais tempo, revisaria todo o assunto.(1º pessoa do singular do modo subjuntivo do tempo pretérito Imperfeito 'dispusesse' do verbo no infinito dispor)
[bg_green]Emprega-se 'S' após ditongos:[reset]\n\nExemplos: \n\n c[green]oi[reset]sa, l[green]ou[reset]sa, p[red]au[reset]sa, c[yellow]au[reset]sa, f[yellow]ai[reset]são.\n
Nomes escritos com S é grafado com S a terminação ISAR:\nExemplo:\n\nAnáli[yellow]s[reset]e   >>  anal[yellow]isar[reset]\navi[yellow]s[reset]o     >> av[yellow]isar[reset]\nLi[yellow]s[reset]o  >>  al[yellow]isar[reset]\nimprovi[yellow]s[reset]o >> improv[yellow]isar[reset]
parali[yellow]s[reset]ia >> paral[yellow]isar[reset]\n\npesqui[yellow]s[reset]a  >> pesqu[yellow]isar[reset]\n[bg_red]Atenção as exceções:[reset]\n\n[yellow]-- Sintetizar[reset] (apesar de ser [green]Síntese[reset])\n--[yellow] Batizar[reset] (apesar de [yellow]Batismo[reset] )
-- [yellow]Hipnotizar[reset] (apesar de [yellow]Hipnose[reset])\n--[yellow]Catequizar[reset](apesar de [yellow]Catecismo[reset])
[red]Se a palavra não estentar a letra 'S', o verbo associado a ela não apresentará tal letra, e sim Z no sufixo IZAR.[reset]\n
[yellow]ameno[reset] 	 >>  amenizar/amenização\n[yellow]banal[reset] 	 >>  banalizar/banalização\n[yellow]civil[reset] 	 >>  civilizar/civilização\n[yellow]canal[reset]    >>  canalizar/canalização\n[yellow]concreto[reset] >>  concretizar/concretização\n[yellow]capital[reset]  >>  capilizar/capitalização\n\n
[yellow]hospital[reset] >>  hospitaliza/hospitalização\n [yellow]suave[reset] 	 >>  suavizar/suavização.\n
[red]Substantivo grafado com S de origem, mantém-se tal letra nos vacábulos e nos diminutivos:[reset]chinês  >>  chinesinho\nfrancês >>  francesinha
japonês >>  japonesesinhos\nmesa	>>  mesinha\npires 	>>  piresinho\nTaís	>>  Taisinha\n\n [red]Se o termo originário não apresentar 'S', o vocábulo derivado deve ser grafado com Z.[reset]\n
Arroz >> arrozinho/arrozal\nCão   >> cãozinho/cãozito\nCafé  >> cafezinho/cafezal\nCaju  >> cajuzeiro\nFlor  >> florzinha\nGol   >> golzinho\nLugar >> lugarzinho'''

    def escrita_word_g(self):

        return '''\nOrtografia - Escrita : Palavras Escritas com G:

a. Emprega-se a letra G nas terminações: [yellow]ágio, égio, ígio, ógio, ugio[reset]\n\nExemplos:\n\n [green]sufrágio,  sortilégio, litígio, relógio, refúgio.[reset]\n\n
b. São também grafadas com G as terminações: [yellow] agem, igem, ugem, ege, oge[reset]\n\nExemplos:\n\n[green]Imagem,  lavagem,   fuligem,  vertigem,  penugem,  herege,  bege,  doge\n\n
[red]Exceção:[reset]\n [green]pajem[reset][Essa palavra a grafia correta dela é [bg_green]pajem[reset].]\n
c.Também se grafam com G os verbos terminados em [yellow]GER e GIR[reset]:\nExemplos:\n\n[green]Eleger, mugir, submergir, aspergir[reset]\n
[red]Casos especiais:[reset]\n\nPalavras de origem indígena, africana,árabe ou exótica são escritas com J:\n\nVeja exemplos:\n\n Alfor[yellow]je[reset],bei[yellow]ju[reset],[yellow]je[reset]quitibá,[yellow]je[reset]rimum, 
[yellow]ji[reset]boia[red] Lembrando que jiboia perdeu o acento devido a ser uma paroxítona terminada em ditongo[reset],[yellow]ji[reset]rau, [yellow]jiu-ji[rest]tsu,
man[yellow]je[reset]ricão,man[yellow]je[reset]rona,pa[yellow]jé[reset]\n\n\nNaturalmente, serão escritas com J palavras derivadas de outras cuja a grafia é também da letra J:\n
[yellow]azulejo[reset]  >>  azulejista\n,[yellow]brejo[reset] >> brejeiro,\n[yellow]canja[reset] >> canjica,\n[yellow]caranguejo[reset]  >> caranguejeira,\n
[yellow]cereja[reset]   >> cerejeira,\n[yellow]cerveja[reset]  >> cervejeiro,\n[yellow]encorajar[reset]  >> encorajei,encorajamento,\n[yellow]laranja[reset]  >> laranjeira
[yellow]loja[reset]  >> lojista   
'''
    def escrita_word_x(self):
        return'''\nOrtografia - Escrita: Palavras Escritas com X:\n\na.[blue]Palavras de origem tupi, africana, exótica são grafadas com X:[reset]\n\n
\nExemplo:\n\n[yellow] Abacaxi, araxá, muxoxo, orixá, xamã, xavante, xucro...[reset]\n\nb. Emprega-se o X depois de ditongos:\n\nExemplos:\n\n
Afr[yellow]ou[reset]xar,  b[yellow]ai[reset]xada,  b[yellow]ai[reset]xela,  b[yellow]au[reset]xita,  c[yellow]ai[reset]xa,  c[yellow]ai[reset]xão, c[yellow]ai[reset]xote,  d[yellow]ei[reset]xar,  desl[yellow]ei[reset]xo,  f[yellow]ai[reset]xa,  f[yellow]ei[reset]xe,  fr[yellow]ou[reset]xo,
g[yellow]uei[reset]xa,  mad[yellow]ei[reset]xa,  r[yellow]ou[reset]xinol\n\n[bg_red]ATENÇAO![reset]\n[red]Tome cuidado com a exceção cau[yellow]cho[reset], da borra[yellow]cha[reset]. \n
As palavras derivadas do pneu, por exemplo: recau[yellow]ch[reset]utar , recau[yellow]ch[reset]utado, recau[yellow]ch[reset]utagem são escritas com [yellow]'CH'[reset].
c. Emprega-se o X após o radical 'EN':\nExemplo:\n\n[yellow]Enx[reset]ada,  [yellow]enx[reset]aguar,  [yellow]enx[reset]aqueca,  [yellow]enx[reset]ame,   [yellow]enx[reset]ergar,  [yellow]enx[reset]ofre, 
[yellow]enx[reset]oval, [yellow]enx[reset]urrada,\n\n[red]Exceções para o radical 'EN': [reset]\n\n[red]Os termos [reset][yellow]enchente,encher[reset] tem origem do vocábulo [yellow]cheio[reset],[red] o que explica a grafia do CH[reset].
[red]O termo [reset][yellow]enchumaçar[reset][red]tem origem da palavra[reset][yellow] chumaço[reset][blue] porção de metéria prima mole como algodão, daí a explicação da grafia com ch.[reset]
\n[red]Regra Especial:[reset]\n\n Depois de [yellow]AN,IN,ON,UN[reset] emprega-se e regra o 'CH':\n\n [yellow]an[reset]chova, g[yellow]an[reset]cho, [yellow]in[reset]chaço,pech[yellow]in[reset]cha, c[yellow]on[reset]cha, p[yellow]on[reset]che,
\nEm aumentativos ou diminutivos escrevem-se com CH os sufixos acho,achão,icho,ucho:\n bon[yellow]achão[reset],gord[yellow]ucho[reset], papel[yellow]ucho[reset], rab[yellow]icho[reset], ri[yellow]acho[reset]        '''
  
    def palavra_variacao(self):
        return '''\n\nOrtografia - Palavras que tem mais de uma forma:\n\nExistem algumas palavras na Língua Portugues cuja grafia pode variar. Muitas vezes, as bancas examinadoras empregam tais vocábulos com a reta intenção de confundir o 
condidato no momento da prova. A seguir tem uma lista exemplificativa de palavra com dupla grafia.\n
[yellow]abaixar[reset] = [yellow]baixar[reset]\n[yellow]abdome[reset] = [yellow]abdômen[reset]\n[yellow]afeminado[reset] = [yellow]efeminado[reset]
[yellow]aluguel[reset] = [yellow]aluguer[reset]\n[yellow]arrebitar[reset] = [yellow]rebitar[reset]\n[yellow]arremedar[reset] = [yellow]remedar[reset]
[yellow]assobiar[reset] = [yellow]assoviar[reset]\n[yellow]assoprar[reset] = [yellow]soprar[reset]\n[yellow]bêbado[reset] = [yellow]bêbedo[reset]
[yellow]besoiro[reset] = [yellow]besouro[reset]\n[yellow]bilhão[reset] = [yellow]bilião[reset]\n[yellow]bílis[reset] = [yellow]bile[reset]
[yellow]biscoito[reset] = [yellow]biscouto[reset]\n[yellow]bravo[reset] = [yellow]brabo[reset]\n[yellow]cãibra[reset] = [yellow]câimbra[reset]
[yellow]carnegão[reset] = [yellow]carnicão[reset]\n[yellow]carroçaria[reset] = [yellow]carroceria[reset]\n[yellow]catinga[reset] = [yellow]caatinga[reset]
[yellow]catorze[reset] = [yellow]quatorze[reset]\n[yellow]catucar[reset] = [yellow]cutucar[reset]\n[yellow]chipanzé[reset] = [yellow]chimpanzé[reset]
[yellow]cociente[reset] = [yellow]quociente[reset]\n[yellow]cotizar[reset] = [yellow]quotizar[reset]\n[yellow]covarde[reset] = [yellow]cobarde[reset]
[yellow]deficit[reset] = [yellow]défice[reset]\n[yellow]degelar[reset] = [yellow]desgelar[reset]\n[yellow]demonstrar[reset] = [yellow]demostrar[reset]
[yellow]dependurar[reset] = [yellow]pendurar[reset]\n[yellow]diabete[reset] = [yellow]diabetes[reset]\n[yellow]dois[reset] = [yellow]dous[reset]
[yellow]emagrecer[reset] = [yellow]esmagrecer[reset]\n[yellow]empanturrar[reset] = [yellow]empaturrar[reset]\n[yellow]enfarte,enfarto,infarte[reset] = [yellow]infarto[reset]
[yellow]engambelar[reset] = [yellow]engabelar[reset]\n[yellow]entretenimento[reset] = [yellow]entretimento[reset]\n[yellow]enumerar[reset] = [yellow]numerar[reset]
[yellow]espuma[reset] = [yellow]escuma[reset]\n[yellow]estalar[reset] = [yellow]estralar[reset]\n[yellow]exorcizar[reset] = [yellow]exorcismar[reset]
[yellow]flauta[reset] = [yellow]frauta[reset]\n[yellow]flecha[reset] = [yellow]frecha[reset]\n[yellow]flocos[reset] = [yellow]frocos[reset]
[yellow]geringonça[reset] = [yellow]gerigonça[reset]\n[yellow]gorila[reset] = [yellow]gorilha[reset]\n[yellow]hemorroidas[reset] = [yellow]hemorroides[reset]
[yellow]impingem[reset] = [yellow]impigem[reset]\n[yellow]imundícia,imundície[reset] = [yellow]imundice[reset]\n[yellow]lantejoula[reset] = [yellow]lentejoula[reset]
[yellow]limpar[reset] = [yellow]alimpar[reset]\n[yellow]lisonjear[reset] = [yellow]lisonjar[reset]\n[yellow]louça[reset] = [yellow]loiça[reset]
[yellow]louro[reset] = [yellow]loiro[reset]\n[yellow]macaxeira[reset] = [yellow]macaxera[reset]\n[yellow]maçom[reset] = [yellow]mação[reset]
[yellow]maquiagem[reset] = [yellow]maquilagem[reset]\n[yellow]marimbondo[reset] = [yellow]maribondo[reset]\n[yellow]marino[reset] = [yellow]marinho[reset]
[yellow]menosprezo[reset] = [yellow]menospreço[reset]\n[yellow]mobiliar,mobilhar[reset] = [yellow]mobilar[reset]\n[yellow]neblina[reset] = [yellow]nebrina[reset]
[yellow]nenê,neném[reset] = [yellow]nenen[reset]\n[yellow]oiro[reset] = [yellow]ouro[reset]\n[yellow]parêntese[reset] = [yellow]parêntesis[reset]
[yellow]percentagem[reset] = [yellow]porcentagem[reset]\n[yellow]percentual[reset] = [yellow]porcentual[reset]\n[yellow]peroba[reset] = [yellow]perova[reset]
[yellow]pitoresco[reset] = [yellow]pinturesco[reset]\[yellow]plancha[reset] = [yellow]prancha[reset]\n[yellow]pólen[reset] = [yellow]polem[reset]
[yellow]protolizar[reset] = [yellow]protocolar[reset]\n[yellow]quadriênio[reset] = [yellow]quatriênio[reset]\n[yellow]rádio[reset] = [yellow]radium[reset]
[yellow]radioatividade[reset] = [yellow]radiatividade[reset]\n[yellow]rastro[reset] = [yellow]rasto[reset]\n[yellow]registro[reset] = [yellow]registo[reset]
[yellow]relampear,relampejar,relampadejar,relampaguear[reset] = [yellow]relampadar,relampar[reset]\n[yellow]remoinho,redemoinho[reset] = [yellow]rodamoinho[reset]
[yellow]ridiculizar[reset] = [yellow]ridicularizar[reset]\n[yellow]salobra[reset] = [yellow]salobre[reset]\n[yellow]seção[reset] = [yellow]secção[reset]
[yellow]selvageria[reset] = [yellow]selvajaria[reset]\n[yellow]silueta[reset] = [yellow]silhueta[reset]\n[yellow]sobressalente[reset] = [yellow]sobresselente[reset]
[yellow]sutil[reset] = [yellow]subutil[reset]\n[yellow]taberna[reset] = [yellow]taverna[reset]\n[yellow]televisar[reset] = [yellow]televisionar[reset]
[yellow]terremoto[reset] = [yellow]terramoto[reset]\n[yellow]tesoura[reset] = [yellow]tesoira[reset]\n[yellow]tesouro[reset] = [yellow]tesoiro[reset]
[yellow]touro[reset] = [yellow]toiro[reset]\n[yellow]toucinho[reset] = [yellow]toicinho[reset]\n[yellow]tríade[reset] = [yellow]tríada[reset]
[yellow]trilhão[reset] = [yellow]trilião[reset]\n[yellow]varrer[reset] = [yellow]barrer[reset]\n[yellow]vassoura[reset] = [yellow]bassoura[reset]
[yellow]várzea,várgea,vargem[reset] = [yellow]varge[reset]\n[yellow]volibol[resetr] = [yellow]voleibol[reset] \n
'''
    def abreviacoes(self):
        return '''\n\nOrtografia - Abreviaturas:\n
[bg_green]Abreviatura é a representação de uma palavra por meio de algumas de suas sílabas ou letras, normalmente são finalizadas por um ponto final.[reset]
[yellow]Mas podem apresentar também barras ou sobrelevação.[reset]
Exemplo:\n\n
[yellow]Sr.[reset] = [yellow]senhor[reset]
[yellow]S.A ou S/A[reset] = [yellow]sociedade anônima[reset]
[yellow]n.[reset] = [yellow]número[reset]
[yellow]prof.ª[reset] = professora
[yellow]Dr.ª[reset] = Doutora

[blue]A abreviatura mantém a acentuação originária da palavra[reset]
Exemplo:\n\n
[yellow]séc.[reset] = século
[yellow]pág.(ou p.)[reset] = página

[blue] Para plurarizar abreviatura, normalmente se acrescenta 's'.[reset]
Exemplo:\n\n
[red] arts.[reset] = artigos
[red] sécs.[reset] = séculos
[red] págs. (ou pp.)[reset] = páginas
[red] fls.[reset] = folhas

[bg_red]Atenção[reset][bg_yellow]Quando a abreviatura refere-se a unidades de medidas, fixadas por convenções internacionais[reset]\n
[bg_red]Não se utiliza o ponto final nem 's' para plural.[reset]\n

Ele chegou às 14[red]h.[reset]       e logo iniciou a reunião. [bg_red](Errado)[reset]
Ele chegou às 14[red]hs.[reset]      e logo iniciou a reunião. [bg_red](Errado)[reset]
Ele chegou às 14[red]:00[reset]      e logo iniciou a reunião.[bg_red](Errado)[reset]
Ele chegou às 14[red]:30h[reset]     e logo iniciou a reunião.[bg_red](Errado)[reset]
Ele chegou às [green]14h[reset]      e logo iniciou a reunião.[bg_green](Correto)[reset]
Ele chegou às [green]14h30[reset]    e logo iniciou a reunião.[bg_green](Correto)[reset]
Ele chegou às [green]14h30min[reset] e logo iniciou a reunião.[bg_green](Correto)[reset]


'''
    def siglas(self):

        return '''\nSIGLAS:\n\n - 
[blue]Enquanto as abreviaturas normalmente se referem a uma palavra e são finalizadas por ponto, as siglas referem-se a:[reset]\n
\n[bg_green]órgãos[red], [bg_green]instituições[reset] ou [bg_green]expressões substantivas[reset] e [bg_yellow]são grafadas sem ponto ao final.[reset]
Exemplo:\n\nTST, TRT, DVD, CD, UnB, OAB, Senai, FGTS, CTPS\n
a. [bg_red]Siglas não recebem acento.[reset]\nExemplo:\n\nPetrobras, Telebras\n\n
b.[blue]O plural de siglas faz-se com um simples acréscimo da letra 'S' no final[reset]\n\nExemplo:\n\n
CD[yellow]s[reset],  PM[yellow]s[reset],  TRT[yellow]s[reset]\n
[bg_red]As siglas formadas por até três letras são grafadas em maiúsculas.[reset]\n[green]TRT,  STF,  OAB,  GDF[reset]\n
[bg_green]As siglas formadas por mais de três letras podem ser grafadas com todas as letras maiúsculas.[...]Ou com a inicial maiúscula apenas e as demias minúsculas, mas só se puderem ser pronunciadas como uma só palavra[reset]
Exemplos:\n\n[yellow]INCRA, UNESCO, FIESP, EMBRATUR[reset] ou [green]Incra, Unesco, Fiesp, Embratur[reset]
[bg_red]Se as siglas formadas por mais de três letras que não puderem ser pronunciadas como uma palavra, também se grafarão em maiúsculas.[reset]
[bg_green]ABTN,  INSS,  BNDES,  FGTS,  CTPS[reset]\n
c. [bg_green]Na primeira citação[reset], [yellow]a expressão designada deve vir escrita por extenso, dee forma completa e correta, sempre antes da sigla que após a forma completa a sigla deve estar entre parênteses.[reset]
Exemplo:\n\n [bg_yellow]Imposto Predial e Territorial Urbano(IPTU)[reset]

'''
    def trema(self):

        return '''\n\nOrtografia - Trema:\n
	- Não se usa mais o trema(¨)Shift + 6, sinal que era colocados sobre a letra 'u' para indicar que ela deve ser pronunciada nos grupos GUE, QUE, QUI.
Exemplo:\n\n
Como era: [yellow]Agüentar[reset]  	    Como fica: [yellow]Aguentar[reset]
Como era: [yellow]Argüir[reset]    	    Como fica: [yellow]Arguir[reset]
Como era: [yellow]Bilíngüe[reset]  	    Como fica: [yellow]Bilíngue[reset]
Como era: [yellow]cinqüenta[reset] 	    Como fica: [yellow]cinquenta[reset]
Como era: [yellow]delinqüente[reset] 	Como fica: [yellow]delinquente[reset]
Como era: [yellow]eloqüente[reset] 	    Como fica: [yellow]eloquente[reset]
Como era: [yellow]ensangüentado[reset]  Como fica: [yellow]ensanguentado[reset]
Como era: [yellow]eqüeste[reset] 	    Como fica: [yellow]equestre[reset]
Como era: [yellow]freqüente[reset] 	    Como fica: [yellow]frequente[reset]
Como era: [yellow]lingüeta[reset] 	    Como fica: [yellow]lingueta[reset]
Como era: [yellow]qüinqüenio[reset]     Como fica: [yellow]quinquênio[reset]
Como era: [yellow]sagüi[reset] 		    Como fica: [yellow]sagui[reset]
Como era: [yellow]sequëncia[reset]      Como fica: [yellow]sequência[reset]
Como era: [yellow]seqüestro[reset]      Como fica: [yellow]sequestro[reset]
Como era: [yellow]tranqüilo[reset]      Como fica: [yellow]tranquilo[reset]

[bg_green]Naturalmente a pronúncia das palavras que perderam o trema permanece inalterada. Em outros termos, nos grupos GUE, GUI, QUE, QUI das palavras apresentadas.[reset]
[bg_green]O 'u' continua sendo pronunciado de forma átona.[reset]\n
[bg_red]\n O trema parmanece nas palavras estrangeiras e em suas derivadas. Exemplo: Müller, Mülleriano[reset]
'''

    def inicias_maiusculas(self):

        return '''Ortografia:
Empregos de iniciais Maiúsculas:

a. Emprega-se inicial maiúscula principalmente quando se faz referência a nome próprio: Nome especificado, individualizado a qual pode ser nome de pessoas,
apelido, entidades, lugares, órgãos.

Exemplo:\n\n Nomes: João, Ana Maria, Chico, 
Apelidos: Tiquinho,  Guto,  Vavá
Entidades: Associação dos Magistrados do Brasil
Órgãos: Departamento de Trânsito, Tribunal Regional Federal da 1ºRegião
Lugares: São Bernardo do Campo, Campinas, Aeroporto Internacional De Brasília, Catedral Metropolitana de Brasília, Santuário Nacional da Nossa Senhora Aparecida
Senado Federal
[bg_green]Caso o nome apresente ideia geral, não definida, usa-se minúscula.[reset]
[bg_red]Os termos Estado, Nação, País com inicial maiúscula são empregados para a referência à organização política geral.[reset]
Exemplo:\n\n
É dever do [bg_green]Estado[reset] garantir educação de qualidade a todos os cidadãos.\n
O [bg_green]País[reset] tem de assumir o compromisso de erradicar a pobreza.\n
[red]Quando empregadas como adjetivo  apresentam inicial minúscula.[reset]\nExemplo:\n[blue]O estado de São Paulo é responsável por boa parte da economia do Brasil[reset]
[blue]O Brasil é um país contrastante em suas desigualdades sociais.[reset]

b. Emprega-se iniciais maiúsculas na indicação de dispositivo legal determinado:\n
[yellow]A Lei n.[reset]8.112/1990 estabelece...\n
[yellow]O Decreto n. [reset]15, de 20 de maio de 1987, prevê...\n
[yellow]O Enunciado n.[reset]do TST determina...\n
[bg_red]Emprega-se inicial maiúscula apenas para o nome do normativo especificado.[reset]
Exemplo:\n[bg_green]...na forma da Lei n. 8.112/1990.[reset]
[bg_red]Partes como artigos, incisos, alíneas emprega-se minúsculos.[reset]\nExemplo:\n[bg_green]...na forma do art. 5°,XX,da CF.[reset]

c. Emprega-se inicial maiúscula facultativa nos casos seguintes:\n
	- Em nome de obras literárias [blue](bibliônimos)[reset], nos vocábulos que se apresentam após o primeiro termo.\n
Exemplo: [yellow]O morro dos ventos uivantes[reset] ou [yellow]O Morro dos Ventos Uivantes[reset]\n
[yellow]Memórias de um sargento de milícias[reset] ou [yellow]Memórias de um Sargento de Milícias[reset]\n
[yellow]O primo Basílio[reset] ou [yellow]O Primo Basílio[reset]
	- Em [yellow]hagiônimos[reset] [blue](nomes sagrados)[reset] e em [yellow]axiônimos[reset] [blue](forma cortês, reverencial de tratamento)[reset]\n
Exemplo:\n\n [yellow]ressureição[reset] ou [blue]Ressureição[reset]
[yellow]santo Expedito[reset] ou [blue]Santo Expedito[reset]
[yellow]doutor João[reset] ou [yellow]Doutor João[reset]
[yellow]professor Evanildo[reset] ou [yellow]Professor Evanildo[reset]
[yellow]administração pública[reset] ou [yellow]Administração Pública[reset]\n
	- Semelhantemente empregam-se iniciais maiúsculas facultativas em nomes de cargos políticos, religiosos e militares, bem como em forma de tratamento.(mesmo que abreviadas)
Exemplo:\n\n [yellow]juiz ou Juiz[reset]\n\n , [yellow]ministro ou Ministro[reset],[yellow]bispo ou Bispo[reset],[yellow] padre ou Padre[reset]
[yellow]vossa excelência[reset] ou [yellow]Vossa Excelência[reset] - (v.ex.ª ou V.Ex.ª)
[blue]excelentíssima senhora[reset] ou [yellow]Excelentíssima Senhora[reset] - (exma.srª ou Exma.Srª)\n\n
[bg_green]- Em redação oficial , em vista da formalidade do texto, emprega-se preferencialmente as formas com iniciais maiúsculas. -[reset]\n
	- Miúsculas facultativas também são empregadas nos nomes de domínio do saber, cursos e disciplinas, bem como doutrinas, religiões, escola de pensamento.\n
Exemplo:\n\n
[yellow]língua portuguesa ou Língua Portuguesa[reset]
[yellow]física ou Física[reset]\n
[yellow]medicina ou Medicina [reset]\n
[yellow]teosofia ou Teosofia [reset]\n
[yellow]positivismo ou Positivismo[reset]\n
[yellow]naturalismo ou Naturalismo[reset]\n
[yellow]cristianiismo ou Cristianismo[reset]\n 
[yellow]imperialismo ou Imperialismo [reset]\n
	- Na indicação de logradouros públicos, as iniciais maiúsculas também são facultativas:\n
Exemplo:\n
[yellow]rua das Palmeiras ou Rua das Palmeiras[reset]
[yellow]avenida Pau Brasil ou Avenida Pau Brasil[reset]
[yellow]edifício Ceará ou Edifício Ceará[reset]
[yellow]túnel Rebouças ou Túnel Rebouças[reset]
[yellow]palácio da Alvorada ou Palácio da Alvorada[reset]'''

    def uso_do_hifen(self):
        return '''Ortografia - Uso do hífen - Versão do Professor Gustavo Silva\n
	- Algumas regras do uso do hífen foram alteradas pelo novo Acordo Ortográfico. Mas, como se trata ainda de matéria relativamente complexa para alguns
para facilitar a compreensão. Apresentamos um resumo das regras que orientam o uso do hífen com os prefixos mais comuns, assim como as novas orientações estabelecidas
pelo Acordo.\n
\n[red]Hífen com prefixos:[reset] Palavras formadas por prefixos ou por elementos que podem funcionar como prefixos:\n
Exemplo:\n\n[bg_green]aero, agro, além, ante, anti, aquém, arqui, auto, circum, co, contra, eletro, entre, ex, extra, geo, hidro, hiper, infra, inter, intra, macro, micro
mini, multi, neo, pan, pluri, proto, pós, pré, pró, pseudo, retro, semi, sobre, sub, super, supra, tele, ultra, tele, ultra, vice[reset]
[bg_red]Uso sempre do hífen[reset]\n
a. Após os prefixos [bg_green]além, aquém, recém, pré, pró, pós, sem, ex e vice.[reset][bg_red]Usa-se sempre o hífen.[reset]
[blue]Exemplos:[reset]\n\n [yellow]além[reset] [bg_green] - [reset]mar\n
[yellow]além[reset] [bg_green] - [reset]túmulo
[yellow]aquém[reset] [bg_green] - [reset]mar
[yellow]recém[reset] [bg_green] - [reset]casado
[yellow]recém[reset] [bg_green] - [reset]nascido
[yellow]pré[reset] [bg_green]  - [reset]história
[yellow]pré[reset] [bg_green]  - [reset]vestibular
[yellow]pró[reset] [bg_green]  - [reset]europeu
[yellow]pós[reset] [bg_green]  - [reset]graduação
[yellow]sem[reset] [bg_green]  - [reset]terra
[yellow]ex[reset]  [bg_green]   - [reset]aluno
[yellow]ex[reset]  [bg_green]   - [reset]prefeito
[yellow]ex[reset]  [bg_green]   - [reset]presidente,
[yellow]vice[reset] [bg_green] - [reset]rei

[bg_red]Novamente os préfixos que sempre vão precisar de um hífen para completar a palavra:[reset]\n
[bg_red] além, aquém, recém, pré, pró, pós, sem, ex, vice [reset]

b. Independentemente do prefixo, ele sempre será separado por hífen de palavra iniciada por 'h'.
Exemplo:\n\n
[yellow]anti-h[reset]igiênico, [yellow]anti-h[reset]istórico, [yellow]contra-h[reset]istamínico, [yellow]macro-h[reset]istória, [yellow]mini-h[reset]otel, [yellow]micro-h[reset]ábitos, [yellow]micro-h[reset]orários, [yellow]multi-h[reset]omologação, [yellow]proto-h[reset]istória,
[yellow]pseudo-h[reset]omen, [yellow]semi-h[reset]omogênio, [yellow]sem-h[reset]onestidade, [yellow]sobre-h[reset]umano, [yellow]super-h[reset]omen, [yellow]supra-h[reset]umanitário, [yellow]ultra-h[reset]umano, [yellow]ultra-h[reset]umilhantes
[bg_red]- O vocabulário Ortográfico da Língua Portugues registra as seguintes exceções: subumano ou sub-humano, coerdeiro ou co-herdeiro.[reset]

Prefixos terminados em Vogal:
[bg_green]a. Não se usa o hífen quando o prefixo termina em vogal diferente da vogal com que se inicia o segundo elemento.[reset]
Exemplo:\n\n
aer[yellow]oe[reset]spacial,\n\nagr[yellow]oi[reset]ndustrial,\n\nant[yellow]eo[reset]tem,\n\nant[yellow]io[reset]ntem,\n\nant[yellow]ie[reset]ducativo,
aut[yellow]oe[reset]ducativo,\n\naut[yellow]oa[reset]prendizagem,\n\n[aut[yellow]oe[reset],\n\naut[yellow]oe[reset]strada,\n\naut[yellow]oe[reset]strada,
aut[yellow]oi[reset]nstrução,\n\nc[yellow]oa[reset]utor,\n\nc[yellow]oe[reset]dição,\n\nextr[yellow]ae[yellow]scola,infr[yellow]ae[reset]strutura,\n\n
plur[yellow]ia[reset]nual,\\nsem[yellow]ia[reset]berto,\n\nsem[yellow]a[reset]berto,\n\nsem[yellow]ia[reset]nalfabeto,\n\nsem[yellow]ie[reset]sférico,
sem[yellow]io[reset]paco\n\n
[bg_green]b. Não se usa o hífen quando o prefixo termina em vogal e o segundo elemento começa por R ou S. Nesse caso, duplicam-se essas letras.[reset]\n
Exemplo:\n\nant[yellow]irr[reset]ábico,\n\nant[yellow]irr[reset]acismo,\n\nant[yellow]irr[reset]eligioso,\n\nant[yellow]irr[reset]ugas,\n\nb[yellow]iorr[reset]itmo
contr[yellow]arr[reset]egra,\n\ncontr[yellow]ass[reset]eno,\n\nc[yellow]oss[reset]eno,\n\ninfr[yellow]ass[reset]om,\n\nmicr[yellow]oss[reset]istema,\n\n
min[yellow]iss[reset]aia,\n\nmult[yellow]iss[reset]ecular,\n\nne[yellow]orr[reset]ealismo,\n\nne[yellow]oss[reset]imbolista,\n\nsem[yellow]irr[reset]eta\n
ultr[yellow]arr[reset]esistente.\n
[bg_green]d. Quando o prefixo termina por vogal, usa-se o hífen se o segundo elemento começar pela mesma vogal.[reset]\n
ant[yellow]i - i[reset]bérico,\n\nant[yellow]i - i[reset]mperalista,\n\nant[yellow]i - i[reset]nflacionário,\n\nant[yellow]i - i[reset]nflamatório,\n\n
aut[yellow]o - o[reset]bservação,\n\ncontr[yellow]a - a[reset]lmirante,\n\ncontr[yellow]a - a[reset]tacar,\n\ncontr[yellow]a - a[reset]taque,\n\n
micr[yellow]o - o[reset]ndas,\n\nmicr[yellow]o - o[reset]ndas,\n\nmicr[yellow]o - ô[reset]ndas,\n\nmicr[yellow]o - ô[reset]nibus,\n\nsem[yellow]i -i[reset]nternato,
sem[yellow]i - i[reset]nterno,\n\n
[bg_red]O prefixo 'co' aglutina-se com o segundo elemento, mesmo quando este se inicia por o:\n[reset][bg_red]coobrigar[reset]\n[bg_red]coobrigação[reset]
[bg_red]cooperar[reset],\n\n[bg_red]cooptar[reset],\n\n[bg_red]coocupante[reset]
[bg_green] O prefixo RE também se aglutina com o segundo elemento, mesmo quando este se inicia por e:[reset]\n
[bg_red]reedição, reeducação, reelaborar, reeleger, reembolso, reexame.[reset]\n\n
[bg_green]PREFIXO TERMINADO EM CONSOANTE[reset]
a. Não se usa o hífen quando o prefixo termina em consoante diferente da consoante com que se inicia o segundo elemento.\n
Exemplos:\n\n
hipe[yellow]rm[reset]ercado,\n\ninte[yellow]rm[reset]unicipal,\n\nsupe[yellow]rd[reset]edicado,\n\nsupe[yellow]rp[reset]roteção,\n\n
hipe[yellow]rc[reset]aprichoso\n
b. Não se usa o hífen quando o prefixo terminado em consoante é seguido de palavra iniciada por vogal.\n
Exemplo:\n\n
hipe[yellow]ra[reset]cidez,\n\nhipe[yellow]ra[reset]tivo,\n\ninte[yellow]re[reset]scolar,\n\ninte[yellow]re[reset]stadual,\n\ninte[yellow]re[reset]stelar,\n\n
inte[yellow]re[reset]studantil,\n\nsupe[yellow]ra[reset]migo,\n\nsupe[yellow]ra[reset]quecimeto,\n\nsupe[yellow]re[reset]conômico,\n\nsupe[yellow]re[reset]xigente,
supe[yellow]ri[reset]nteressante,\n\nsupe[yellow]ro[reset]timismo.\n
c. Quando o prefixo termina por consoante, usa-se o hífen se o segundo elemento começar pela mesma consoante.
hipe[yellow]r - r[reset]equintado,\n\ninte[yellow]r - r[reset]egional,\n\nsu[yellow]b - b[reset]ibliotecário, supe[yellow]r - r[reset]acista, supe[yellow]r - r[reset]eacionário,
supe[yellow]r - r[reset]esistente,\n\nsupe[yellow]r - [reset]omântico\n\n
[bg_green]Com o prefixo 'sub',usa-se o hífen também diante da palavra iniciada por 'R': sub-região, sub-raça.[reset]\n\n
[bg_green]Com os prefixos 'circum' e 'pan', usa-se o hífen diante da palavra iniciada por 'm','n' e 'vogal'.[reset]\n\n
Exemplos:\n\n circu[yellow]m - n[reset]avegação,\npa[yellow]n - a[reset]mericano\n

[bg_green]Hífen em Palavras Compostas e Outros Casos[reset]
[blue] Na prefixação, une-se o fragmento(prefixo) a uma palavra para se formar uma segunda palavra. Na composição, unem-se duas ou mais palavras para se criar
um novo vocábulo, o dito composto.[reset]\n
a. Emprega-se o hífen nos topônimmos iniciados pelos adjetivos [yellow]grã, grão[reset] ( Grã-Bretanha, Grão-Pará ) ou por forma verbal ([yellow]Abre[reset]-Campos,
[yellow]Passa[reset]-Quatro,[yellow]Quebra[reset]-Costas,[yellow]Quebra[reset]-Dentes,[yellow]Traga[reset]-Mouros,[yellow]Trinca[reset]-Fortes.\n
[bg_green]Ou cujo os elementos estejam ligados por artigo(Albergaria-a-Velha, Baía de Todos-os-Santos, Entre-os-Rios).[reset]
[bg_red] outros topônimos compostos devem ser escritos como elementos separados, sem hífen: América do Sul, Belo Horizonte, Cabo Verde, Castelo Branco[reset]\n\n
[bg_red] O topônimo 'Guiné-Bissau' é, contudo, uma exceção consagrada pelo uso.[reset]\n

b. Emprega-se o hífen nas palavras compostas por 'justaposição' que não contêm formas de ligação e cujos elementos, de natureza nominal, numeral, verbal constituem
uma unidade sintagmática e semântica e mantêm acento próprio, podendo também dar-se o caso de o primeiro elemento estar reduzido.\n
Exemplo:\n\n[yellow]ano-luz[reset],\n[yellow]arcebispo-bispo[reset],[yellow]arco-íris[reset],\n[yellow]decreto-lei[reset],\nmédico-cirúrgico,\n
[yellow]tenente-coronel[reset],\n[yellow]tio-avô[reset],\nturma-piloto,\n[yellow]alcaide-mor[reset],\namor-perfeito,\n[yellow]guarda-norturno[reset],\n
[yellow]mato-grossense[reset],\nnorte-americano,\n[yellow]porto-alegrense[reset],\nsul-africano,\n[yellow]afro-asiático[reset],\nafro-luso-brasileiro,\n
azul-escuro,\n[yellow]luso-brasileiro[reset],\nprimeiro-ministro,\n[yellow]primeiro-sargento[reset],\n[yellow]primo-infecção[reset],\nsegunda-feira,\nconta-gotas,
\nfinca-pé,\n[yellow]guarda-chuva[reset]\n
[bg_green]\nCertas composições, perderam a noção de composição, agora grafam-se como:[yellow]girassol[reset],\n[yellow]madressilva[reset],\nmandachuva,\npontapé,\n
paraquedas\n,[yellow]paraquedista[reset]\n
[bg_green]c. Não se emprega hífen em locuções substantivas e adjetivas que trazem elemento conectivo como preposição ou conjunção:[reset]\n
[yellow]dia a dia, cão de guarda, olho de sogra,fim de semana, pôr do sol, mão de obra, pé de moleque, cor de vinho, cor de mel.[reset]\n\n
[bg_green]O hífen é empregado em vocábulos que designam espécies botânicas ou animais:[reset]\n [yellow]dente-de-leão, copo-de-leite[reset],\n[yellow]pimenta-do-reino[reset]
cravo-da-índia,\n andorinha-da-serra,\n [yellow]lebre-da-patagônia[reset],\n olho-de-boi,\n [yellow]bico-de-papagaio...[reset]
[bg_red]ATENÇÃO! O HÍFEN FOI MANTIDO EM CASOS JÁ CONSAGRADOS:[reset]\n [yellow]água-de-colônia[reset],\n[yellow]cor-de-rosa[reset],\n[yellow]mais-que-perfeito[reset]
ao deus-dará,\n [yellow]à queima-roupa[reset],\n[yellow]pé-de-meia[reset],\npé-d'água,\n pau-d'alho,\n[yellow]gota-d'água[reset],\ncola-de-sapateiro,\n[yellow]pão-de-leite[reset],\narco-da-velha.
[bg_green]OUTROS CASOS:[reset]\n\n
Deve-se usar o hífen com os [bg_green]sufixos[reset] de origem tupi-guarani:açu, guaçu e mirim.\n
Exemplo: \n\n[yellow]amoré-guaçu, anajá-mirim, capim-açu[reset]\n\n
b.Deve-se usar o hífen para ligar duas ou mais palavras que ocasionalmente se combinam, formando não propriamente vocábulos, mas encadeamentos vocabulares.\n\n
Exemplos:\n\nponte Rio-Niterói, eixo Rio-São Paulo\n\n
c. Embora o Novo Acordo Ortográfico não tenha feito menção expressa ao uso do hífen após as palavras [yellow]não[reset] e [yellow]quase[reset] como função prefixa,
a Academia Brasileira de Letras em uma de suas manifestações acerca do acordo, decidiu excluir o emprego do hífen nesses casos.\n\n
Exemplos:\n\nnão-agressão,\n não alinhado,\nnão conhecimento,\nnão fumante,\nquase delito,\nquase irmão\n\n
d. Como prefixo, a palavra [blue]'bem'[reset] exige [yellow]sempre hífen[reset]:	bem-arrumando, [yellow]bem-afortunado[reset], bem-aceito,[yellow]bem-sucedido[reset]
[yellow]bem-humorado[reset],\nbem-estar,\n [yellow]bem-estar[reset]\n\n
[red]Exceções:[reset]\n\nHá compostos em que bem aglutina-se com o segundo elemento: \n\n[yellow]benfeito[reset], [yellow]benfazer[reset], [yellow]benfeitor[reset],  [yellow]benquerer[reset],  [yellow]benquisto[reset]\n\n
[bg_green]Por sua vez, o prefixo 'mal' exige hífen antes de 'vogal','h','l':[reset]\n\n [yellow]mal-a[reset]cabado,  [yellow]mal-a[reset]gradecido, [yellow]mal-h[reset]umorado, [yellow]mal-i[reset]ntencionado, [yellow]mal-l[reset]avado, [yellow]mal-e[reset]star, [yellow]mal-e[reset]ntendido.\n\n
[blue]Nos demais casos, escreve-se sem hífen, com aglutinação: [reset]\n\n[bg_green]malcriado[reset], [bg_green]malfeito[reset], [bg_green]malsucedido[reset]
'''

    def acentuacao_grafica(self):
        return '''\nOrtografia - Acentuação Gráfica -\n
	- A nova ortografia trouxe mudanças na acentuação de algumas palavras, sobretudo em vocábulos paroxítonos. Em seguida, apresentam-se as regras
ainda vigentes e as alterações trazidas pelo Novo Acordo Ortográfico.\n\n A acentuação gráfica que nos importa para as provas de concurso diz respeito ao emprego do acento agudo(´) e do acento circunflexo(^). Desse modo, cabe destacar que o til(~) não é acento.\n Por exemplo então que podemos afirmar
implicamente que NÃO SÃO ACENTUADAS as palavras como mãe, mão, são, balão, etc.
	- Regras ainda vigentes: [bg_green]Monossílabas Tônicas (Oxítonas Monossilábicas)[reset].
[bg_green]Monossílabos são vocábulos que possuem tão somente uma sílaba.[reset]
No caso de tais palavras apresentarem autonomia fonética e semântica, são denominados tônicos, situação na qual [bg_green] serão acentuadas se terminarem em A(s),E(s),O(s).[reset]\n\n [yellow]Eis exemplos: pá(s),fé(s),cós,pó(s).[reset]\n
[bg_red] São considerados monossílabos tônicos as formas verbais assimiladas com pronomes oblíquos átonos, sendo assim recebem acento.[reset]\n
Exemplos:\n\n [yellow]dá[reset]-lo,\n [yellow]sê[reset]-lo,\n[yellow]pô[reset]-los\n
[bg_green]Palavras que possuem duas sílabas são denominadas dissílabas, assim como as trissílabas possue três sílabas, e as polissílabas possuem quatro sílabas ou mais. Caso tais vocábulos possuam como sílaba pronunciada mais fortemente(sílaba tônica) a última, são denominadas de oxítonas.[reset]\n
[bg_red]Oxítonas[reset]:\n[blue]As palavras oxítonas serão acentuadas quando terminarem em A(s),E(s),O(s),EM,ENS.[reset]\n
Vejamos exemplos: ca[yellow]já[reset], pa[yellow]vê[reset], ji[yellow]ló[reset], vin[yellow]tém[reset], para[yellow]béns[reset]\n
[bg_red]São consideradas palavras oxítonas as formas verbais assimiladas com pronomes oblíquos átonos, recebem acento.[reset] \n
[red]Vejamos alguns exemplos:[red]\n com[yellow]prá[reset]-las,\n ven[yellow]dê[reset]-lo,\ncom[yellow]pô[reset]-los.\n\n
[bg_red]Paroxítonas:[reset]\n
As palavras paroxítonas possuem a penúltima sílaba tônica. A regra de acentuação desses vocábulos é a mais extensa, por abarcar todas as outras terminações
diferentes das terminaçlões das oxítonas.\nDessa forma acentua-se palavras paroxítonas terminadas em:\n
[bg_green]i(s)[reset] - [yellow]tá[reset]xi(s), [yellow]jú[reset]ri(s);
[bg_green]US [reset]  - [yellow]ô[reset]nus, [yellow]bô[reset]nus, [yellow]tô[reset]nus;
[bg_green]R [reset]   - re[yellow]vól[reset]ver, ca[yellow]rá[reset]ter;
[bg_green]X [reset]   - [yellow]tó[reset]rax,[yellow]fê[reset]nix,[yellow]cá[reset]lix
[bg_green]N [reset]   - [yellow]hí[reset]fen, ab[yellow]dô[reset]men, [yellow]pó[reset]len;
[bg_green]L [reset]   - [yellow]fós[reset]sil, [yellow]rép[reset]til, pro[yellow]jé[reset]til;
[bg_green]UM,UNS[reset]   - [yellow]ál[reset]bum, [yellow]fó[reset]rum, [yellow]ál[reset]buns;
[bg_green]ON(s) [reset]   - [yellow]elé[reset]tron(s), [yellow]fó[reset]ton(s);
[bg_green]PS [reset]    - [yellow]bí[reset]ceps, [yellow]trí[reset]ceps, [yellow]fór[reset]ceps;
[bg_green]ÃO/Ã[reset]   - [yellow]ór[reset]gão, [yellow]ór[reset]fão, [yellow]or[reset]fã;
[bg_green]DITONGO [reset]   - [yellow]jó[reset]quei, [yellow]tê[reset]nue, ci[yellow]ên[reset]cia;\n
[blue]Tome cuidado com as palavras[reset][red] caráter,júnior e sênior[reset] [blue]que no singular tem acentuação justificada pela regra das paroxítonas com
terminação 'R'.[reset][red]Mas no plural, porém, tais vocábulos têm a sílaba tônica deslocada e deixam de ser acentuadas.[reset]\n
ca[yellow]rá[reset]ter = caracteres\n
[yellow]jú[reset]nior = juniores
[yellow]sê[reset]nior = seniores\n
Os vocábulos [red]hífen, abdômen, pólen[reset] possuem duas formas de pluralização. Fique atento a isso, pois, a depender da forma adotada,
a acentuação pode ou não ser empregada.\n Exemplo:\n [yellow]Hí[reset]fen >> hifens ([red]perdi o acento[reset]) ou hífenes (Outra forma pluralizada com acentuação)\n
[yellow]pó[reset]len    >> polens ([red]perdi a acentuação com essa pluralização[reset] ou pólenes([blue]Com acentuação plurarizada[reset])\n
ab[yellow]dô[reset]men  >> abdomens ([red]Perdi acentuação com essa pluralização[reset]) ou abdômenes([blue]Com acentuação plurarizada[reset])\n
[bg_green]Fique atento às variantes oxítonas da palavra paroxítona RÉPTIL E PROJÉTIL, pois as formas de pluralização e acentuação são diversas.[reset]\n
[yellow]ré[reset]ptil   >> répteis - (manteve a regra de acentuação das paroxítonas)
rep[yellow]til[reset]   >> rep[yellow]tis[reset]     - Sílaba tônica agora é a última, tanto no singular quanto no plural
pro[yellow]jé[reset]til >> pro[yellow]jé[reset]teis  - Manteve a regra de acentuação das paroxítonas
proje[yellow]til[reset] >> proje[yellow]tis[reset]   - Agora a palavra tanto no singular quanto no plural são oxítonas.

[red]Proparoxítonas:[reset]\n\n As palavras proparoxítonas são aquelas cuja sílaba tônica é a antepenúltima. Na língua portuguesa, todas as palavras proparoxítonas
são acentuadas.\n\n Exemplos:\n [yellow]Mé[reset]dico, [yellow]gê[reset]nero, [yellow]hé[reset]tero.\n
[bg_green]Fique atento para as palavras 'espécimen','júpiter','lúcifer' pois elas apresentam plural com deslocamento de sílaba tônica, fato que interfere na acentuação gráfica.[reset]\n
es[yellow]pé[reset]cimen >> es[yellow]pé[reset]cimens ou espécimenes ([red]Apesar do deslocamento, continua proparoxítona[reset])
[yellow]jú[reset]piter   >> [yellow]jú[reset]piteres 
[yellow]lú[reset]cifer   >> lu[yellow]cí[reset]feres ([red]Apesar do deslocamento da sílaba tônica, continua proparoxítona.[reset])\n
[red]>> Paroxítonas:[reset]\n\n Paroxítonas terminadas em ditongos crescentes podem ter autonomia silábica para o último fonema vocálico. Mudando a tonicidade entre
os vocábulos paroxítonas e proparoxítonas.\n Exemplo:\n\n his[yellow]tó[reset]ria >> his-tó-ria ou his-tó-ri-a
[yellow]gê[reset]-nio([red]Paroxítona[reset]) >> [yellow]gê[reset]-ni-o ([red]Proparoxítona eventual[reset])\n[yellow]sé[reset]-rie ou [yellow]sé[reset]-ri-e ([red]Proparoxítona Eventual[reset])\n
[yellow]á[reset]-gua([red]Paroxítona[reset]) >> [yellow]á[reset]-gu-a ([red]Eventual proparoxítona[reset])\nCon[yellow]tí[reset]nuo([red]Paroxítona[reset]) >> con-[yellow]tí[reset]-nuo ou con-[yellow]tí[reset]-nu-o([red]Eventual Proparoxítona[reset])\n
[blue]Resumindo...[reset]\n
[yellow] As bancas consideram que tais palavras paroxítonas como médico é acentuada com base em uma regra diferente da palavra história (proparoxítona acidental)[reset]\n
[red]Regras Alteradas[reset]\n
[red]Vogal Tônica do Hiato[reset]\n
Acentua-se o 'i' ou 'u' tônicos do hiato quando tais vogais se encontram sozinhas ou acompanhadas de 's' na sílaba.\n
Exemplo:\n\nba-[yellow]ú[reset] - Oxítona que mantêm o acento no 'u' tônico do hiato e se encontra sozinha.\n
sa-[yellow]í[reset]-da - Paroxítona que recebe acento no 'i' por ser tônica de hiato e se encontra sozinha.\n
dis-tri-bu-[yellow]í[reset]-das - Paroxítona que recebe acento no 'i' por ser tônica de hiato sozinha.\n
sa-[yellow]ú[reset]-de - Paroxítona que recebe acento no 'u' por ser tônica de hiato sozinha.\n
Pi-au-[yellow]í[reset] - Oxítona que recebe acento no 'i' por ser tônica de hiato sozinha.\n
Lu-[yellow]ís[reset] - Oxítona que recebe acento no 'i' por ser tônica de hiato acompanhada de s.\n
Ta-[yellow]ís[reset] - Oxítona que recebe acento no 'i' por ser tônica de hiato acompanhada de s.\n
[bg_red]Não haverá acentuação se as citadas vogais vierem seguidas de 'nh' ou acompanhadas de outra letra diferente de 's'.[reset]\n
Exemplos:\n Rainha (r[green]a - [yellow]i[reset] - nha)- [red]Tônica 'i' com hiato porém seguida de 'nh'[reset] - [bg_green]Não recebe acentuação[reset]\n
bainha (b[green]a[reset] - [yellow]i[reset] - nha)-[red]Tônica 'i' com hiato porém seguida de 'nh'[reset] - [bg_green]Não recebe acentuação.[reset]\n
ventoinha (ven - t[green]o[reset] - [yellow]i[reset] - nha) - [red] Tônica 'i'com hiato porém seguida de 'nh'[reset] - [bg_green]Não recebe acentuação.[reset]\n
tainha (t[green]a[reset] - [yellow]i[reset] - nha) - [red] Tônica 'i' com hiato porém seguida de 'nh'[reset] - [bg_green]Não recebe acentuação.[reset]\n
juiz (j[green]u[reset] - [yellow]iz[reset]) - [red] Tônica com hiato porém seguida de 'z'. - [bg_green]Não recebe acentuação.[reset]\n
ruim(r[green]u[reset] - [yellow]im[reset]) - [red] Tônica 'i' com hiato porém seguda de 'm'. - [bg_green]Não recebe acentuação.[reset]\n

[bg_red]A nova ortografia determinou a dispensa da acentuação em hiatos antecedidos de ditongos em palavras 'paroxítonas'.[reset]\n
Exemplos:\n\n f[green]ei[reset] - [yellow]ú[reset] - ra :: [blue]Dispensa da acentuação em hiatos antecedidos de ditongos em palavras paroxítonas. [reset]
c[green]au[reset] - [yellow]í[reset] - la		        :: [blue]Dispensa da acentuação em hiatos antecedidos de ditongos em palavras paroxítonas. [reset]
b[green]ai[reset] - [yellow]ú[reset] - ca 		        :: [blue]Dispensa da acentuação em hiatos antecedidos de ditongos em palavras paroxítonas. [reset]
bo - c[green]ai[reset] - [yellow]ú[reset] - va	        :: [blue]Dispensa da acentuação em hiatos antecedidos de ditongos em palavras paroxítonas. [reset]
b[green]oi[reset]- [yellow]ú[reset] - na		        :: [blue]Dispensa da acentuação em hiatos antecedidos de ditongos em palavras paroxítonas. [reset]

[bg_green] Vale destacar novamente que tal alteração destina-se a palavras paroxítonas.[reset]\n
[bg_green] Se a palavra for oxítona e o 'i' ou 'u' estiverem em posição final (seguidos de 's'), o acento permanece.[reset]\n\n[bg_green]Exemplo: tuiuiú, Piauí[reset]\n
[bg_green]DITONGOS ABERTOS:[reset]\n
	- Os ditongos EI,OI,EU podem apresentar pronúncia fechada ou aberta. Vejam-se estes exemplos: rei, boi, meu. (sons fechados)
Agora méis, mói, réu devemos empregar o acento agudo para assegurar a pronúncia aberta de tais ditongos, como se vê nos exemplos abaixo:
\nan[yellow]éis[reset],  her[yellow]ói[reset],  corr[yellow]ói[reset],  c[yellow]éu[reset],  chap[yellow]éu[reset] - [blue]São palavras oxítonas[reset]
[green]A nova ortografia determinou a dispensa da acentuação em tais ditongos com pronúncia aberta em palavras paroxítonas.[reset]
As mudanças:\na - p[yellow]ói[reset]- a (do verbo apoiar) >> apoia\n\na - p[yellow]ói[reset]- o (verbo apoiar) >> apoio\n\nb[yellow]ói - [reset]a\n\nCo - r[yellow]éi[reset] - a
[green]estréia[reset] :: es - tr[yellow]éi[reset] - a  // Ditongo aberto 'éi' portanto sem acentuação. [bg_green]estreia[reset]\n
[green]geléia[reset]  :: ge - l[yellow]éi[reset] -  a   // Ditongo aberto 'éi' portanto sem acentuação.[bg_green]geleia[reset]\n
[green]heróico[reset] :: he - r[yellow]ói[reset] - co  // Ditongo aberto 'ói' portanto sem acentuação. [bg_green]heroico[reset]\n
[green]idéia[reset]   :: i  - d[yellow]éi[reset] -  a   // Ditongo aberto 'éi' portanto sem acentuação.[bg_green]ideia[reset]\n
[green]jóia[reset]    :: j[yellow]ói[reset] - a // Ditongo aberto 'ói' portanto sem acentuação.[bg_green]joia[reset]\n
[green]platéia[reset] :: pla - t[yellow]éi[reset] - a // Ditongo aberto 'éi' portanto sem acentuação.[bg_green]plateia[reset]\n
[bg_re] Regras para as palavras somente paroxítonas.[reset]\n
[bg_green]Continuam acentuadas as palavras oxítonas e monossílabos tônicos terminados em 'éis', 'éu', 'éus', 'ói', 'óis'.\n\n papéis, troféu, herói, heróis[reset]
[bg_red] Acentos Diferenciais [reset]
[blue] Os acentos diferencias servem para diferenciar vocábulos de verbo ([yellow]pôr) de uma preposição ([yellow]por)[reset].\n
[green] Com o novo acordo ortográfico determinou que não mais se deve usar o acento que diferenciava pares como:[reset]\n
[yellow] pára/para, péla(s)/pela(s), pêlo(s)/pelo(s), pólo(s)/polo(s) e pêra/pera.[reset]\n
Exemplos:\n
[blue]Antes do acordo:[reset] Chuva [yellow]pára[reset] o trânsito no centro.   :: [blue]Como fica:[reset] Chuva [yellow]para[reset] o trânsito no centro.\n
[blue]Antes do acordo:[reset] Ele era o [yellow]pólo[reset] passivo da relação. :: [blue]Como fica:[reset] Ele era o [yellow]polo[reset] passivo na relação.\n
[blue]Antes do acordo:[reset] Nem todos entendem o jogo de [yellow]pólo.[reset] :: [blue]Como fica:[reset] Nem todos entendem o jogo de [yellow]pólo[reset].\n
[blue]Antes do acordo:[reset] Por que você não [yellow]péla[reset] esses [yellow]pêlos[reset]? :: [blue]Como fica:[reset] Por que você não [yellow]pela[reset] esses [yellow]pelos[reset]?\n
[blue]Antes do acordo:[reset] Nunca gostei de [yellow]pêra.[reset] :: [blue]Como fica:[reset] Nunca gostei de [yellow]pera.[reset]\n
[bg_red]ATENÇÃO![reset]\n
[bg_green] Permanece o acento diferencial em 'pôde/pode'.[reset]\n
[yellow]pôde[reset] - É a forma do passado do verbo poder (pretérito perfeito do indicativo), na 3º pessoa do singular\n
[yellow]pôde[reset] - É a forma do presente do indicativo, na 3º pessoa do singular.\n
Exemplo: \n\n
Na semana passada, ela não [yellow]pôde[reset] conversar com o chefe, mas nesta ela [yellow]pode[reset].
[bg_green] Permanece também o acento diferencial em pôr/por.[reset] [blue]Pôr é verbo[reset]e [blue]por é preposição.[reset].\n
Exemplo:\n\n\t [yellow]Por[reset] mim, você já pode [yellow]pôr[reset] as barbas de molho. Vai sobrar para você!\n
[bg_red]ATENÇÃO![reset]\n
É  [bg_green]facultativo[reset]  o uso do acento circunflexo para diferenciar as palavras  [bg_green]forma / fôrma.[reset] Em alguns casos, o uso do acento deixa a frase mais clara.
Exemplo: \n\n Até hoje, não entendi a [yellow]forma[reset] de usar esta [yellow]fôrma[reset]
É  [bg_green]facultativo[reset]  o uso do acento circunflexo para diferenciar as palavras  [bg_green]demos [reset]([blue]Pretérito Perfeito do Indicativo[reset] / [bg_green]dêmos[reset]([blue]Presente do subjuntivo[reset].[green] Em alguns casos, o uso do acento deixa a frase mais clara.[reset]
Exemplo:\n\n Já [yellow] demos[reset] o prazo necessário para a resolução do problea. Ainda assim, talvez [yellow]dêmos[reset] outra chance para quem não se manifestou tempestivamente.

Outros casos:\n\n Palavras Terminadas em [bg_green]EEM e OO(s)[reset]:
[bg_red] Não se usa mais acento das palavras terminadas em 'eem' e 'oo(s)'.[reset]
Exemplo:\n\n
[blue]Como era:[reset]crêem (verbo crer)   [blue]Como fica:[reset] [yellow]creem[reset]
[blue]Como era:[reset]dêem  (verbo dar)    [blue]Como fica:[reset] [yellow]deem[reset]
[blue]Como era:[reset]lêem  (verbo ler)    [blue]Como fica:[reset] [yellow]leem[reset]
[blue]Como era:[reset]vêem  (verbo ver)    [blue]Como fica:[reset] [yellow]veem[reset]
[blue]Como era:[reset]dôo   (verbo doar)   [blue]Como fica:[reset] [yellow]doo[reset]
[blue]Como era:[reset]enjôo   (verbo doar) [blue]Como fica:[reset] [yellow]enjoo[reset]
[blue]Como era:[reset]magôo   (verbo doar) [blue]Como fica:[reset] [yellow]magoo[reset]
[blue]Como era:[reset]perdôo  (verbo doar) [blue]Como fica:[reset] [yellow]perdoo[reset]
[blue]Como era:[reset]povôo   (verbo povoar)[blue]Como fica:[reset] [yellow]povoo[reset]
[blue]Como era:[reset]vôos    (verbo povoar)[blue]Como fica:[reset] [yellow]voos[reset]
[blue]Como era:[reset]zôo     (verbo povoar)[blue]Como fica:[reset] [yellow]zoo[reset]

[bg_green]Permanecem os acentos que diferenciam o singular do plural dos verbos 'ter' e 'vir'. Assim como seus derivados(manter, deter, conter, convir, intervir, advir)[reset]\n
Vamos aos exemplos:\n\n
Ele não [yellow]tem[reset] chance contra nós.// Eles não [yellow]têm[reset] chance contra nós.\n
A mercadoria [yellow]vem[reset] de avião. // As mercadorias [yellow]vêm[reset] de avião.\n
Ele [yellow]provém[reset] da Europa. // Eles [yellow]provêm[reset] da Europa.\n
O chefe [yellow]detém[reset] a palavra final. // Os chefes [yellow]detêm[reset] a palavra final.\n
Tal medida [yellow]convém[reset] a todos. // Tais medidas [yellow]convêm[reset] a todos.\n
[bg_green] Eliminação do Acento Agudo do 'u' Tônico dos grupos GUE e GUI.[reset]
Semelhantemente ao que ocorreu com o trema que foi dispensado QUE, QUI, GUE, GUI cujo 'u' fosse pronunciado de modo átono.\n
O novo acordo ortográfico dispensou o uso do acento agudo no 'u' tônico dos grupos GUE e GUI. Tal acentuação ocorria no presente do indicativo dos verbos 'arguir' e 'redarguir.'\n
Exemplo:\n\n[blue]Como era:[reset]eu argúo // [blue]Como fica:[reset]eu arguo
[blue]Como era:[reset]tu argúis    // [blue]Como fica:[reset]tu arguis
[blue]Como era:[reset]nós argüimos // [blue]Como fica:[reset]nós arguimos
[blue]Como era:[reset]vós argüis   // [blue]Como fica:[reset]nós arguis
[blue]Como era:[reset]eles argúem  // [blue]Como fica:[reset]nós arguem

Verbos Terminados em GUAR, QUAR e QUIR:
- Há uma variação na pronúncia dos verbos nessas terminações. Se forem pronunciadas com o 'a' ou 'i' tônico, essas formas devem ser acentuadas.
Se pronunciadas com o 'u' tônico, essas formas deixam de ser acentuadas.
Exemplo:\n\n
[blue]Verbo enxaguar: [reset] en[yellow]xá[reset]guo, en[yellow]xá[reset]guas, en[yellow]xá[reset]gua, en[yellow]xá[reset]guam, en[yellow]xá[reset]gue, en[yellow]xá[reset]gues, en[yellow]xá[reset]guem\n
[blue]Verbo delinquir:[reset] de[yellow]lí[reset]nquo, de[yellow]lí[reset]ques, de[yellow]lín[reset]quem, de[yellow]lín[reset]qua, de[yellow]lín[reset]quas, de[yellow]lín[reset]quam
[bg_red] Se forem pronunciadas com o 'u' tônico, essas formas deixam de ser acentuadas, sendo a tônica a ser pronunciada mais forte[reset]
[blue]Verbo Enxaguar :[reset] enxa[yellow]gu[reset]o, enxa[yellow]gu[reset]a, enxa[yellow]gu[reset]am, enxa[yellow]gu[reset]e, enxa[yellow]gu[reset]em
[blue]Verbo Delinquir:[reset] delin[yellow]quo[reset], delin[yellow]qu[reset]es, delin[yellow]qu[reset]e, delin[yellow]qu[reset]em, delin[yellow]qu[reset]as, delin[yellow]qu[reset]am
[bg_red]No Brasil a pronúncia mais corrente é a primeira, aquela com 'a' e 'i' tônicos.[reset]
[bg_green] Fique atento a outras palavras que oscilam em sua acentuação, tendo duas formas corretas:[reset]
acr[green]ó[reset]bata  ou  acrobata\n
a[green]ló[reset]pata   ou alopata\n
ambr[green]ó[reset]sia  ou ambrosia\n
anidrido ou a[green]ní[reset]drido\n
autopsia ou au[green]tó[reset]psia\n
biopsia ou bi[green]ó[reset]psia\n
bo[green]ê[reset]mia ou boemia\n
cli[green]tó[reset]ris  ou cl[green]í[reset]tores\n
e[green]lé[reset]trodo  ou eletrodo\n
hier[green]ó[reset]glifo ou hieroglifo\n
hom[green]í[reset]lia ou homilia\n
Madagascar ou Madag[green]á[reset]scar\n
necr[green]ó[reset]psia ou necropsia\n
ortoepia ou orto[green]é[reset]pia\n ( estudo da correta pronúncia das palavras )
Oce[yellow]â[reset]nia ou Oceania\n
s[yellow]ó[reset]ror ou soror ( forma de tratamento usada para freiras )
trans[green]í[reset]stor ou transistor (componente eletrônico )
xerox  ou x[green]é[reset]rox
z[green]â[reset]ngão ou zangão
zenite ou z[yellow]ê[reset]nite (ponto ou grau mais elevado)\n
[bg_green] As bancas examinadoras empregam em suas questões palavras que podem ser acentuadas ou não a depender do significado contextual que elas assumem.[reset]
Exemplo:\n\n
am[yellow]é[reset]m       = ([green]sim, resposta litúrgica[reset])  >> [yellow]amem[reset]    = ([green]flexão do verbo amar[reset]) 
an[yellow]á[reset]lise    = ([green]nome da ação[reset])             >> [yellow]analise[reset] = ([green]flexão do verbo amar[reset]) 
at[yellow]é[reset]        = ([green]preposição[reset])		         >> [yellow]ate[reset]     = ([green]flexão do verbo atar[reset])
bab[yellow]á[reset]       = ([green]cuidadora[reset])		         >> [yellow]baba[reset]    = ([green]flexão do verbo babar[reset])	
contribu[yellow]í[reset]  = ([green]verbo no pretérito[reset])       >> [yellow]contribui[reset]    = ([green]verbo no presente[reset])	
do[yellow]í[reset]do      = ([green]que dó, de dores[reset])  	     >> [yellow]doido[reset]   = ([green]louco[reset])	
[yellow]fá[reset]brica    = ([green]prédio, instalação[reset])  	 >> [yellow]fabrica[reset] = ([green]flexão do verbo fabricar[reset])	
flu[yellow]í[reset]do     = ([green]particípio de fluir[reset])  	 >> [yellow]fluido[reset] = ([green]líquido[reset])	
fo[yellow]tó[reset]grafo  = ([green]atividade[reset])  	 	  >> [yellow]fotografo[reset] = ([green]flexão de fotografar[reset])	
his[yellow]tó[reset]ria   = ([green]narração[reset])  	 	  >> [yellow]historia[reset] = ([green]flexão do verbo historiar[reset])	
in[yellow]í[reset]cio     = ([green]começo[reset])  	 	  >> [yellow]inicio[reset] = ([green]flexão do verbo iniciar[reset])	
m[yellow]á[reset]goa      = ([green]ressentimento[reset])  	  >> [yellow]magoa[reset] = ([green]flexão do verbo magoar[reset])	
m[yellow]é[reset]dico     = ([green]atividade[reset])  	 	  >> [yellow]medico[reset] = ([green]flexão do verbo medicar[reset])	
m[yellow]ú[reset]sica     = ([green]composição[reset])  	  >> [yellow]musica[reset] = ([green]flexão do verbo musicar[reset])	
neg[yellow]ó[reset]cio    = ([green]atividade[reset])  	 	  >> [yellow]negocio[reset] = ([green]flexão do verbo negociar[reset])	
n[yellow]ú[reset]mero     = ([green]quantidade[reset])  	  >> [yellow]numero[reset] = ([green]flexão do verbo numerar[reset])	
p[yellow]ú[reset]blico    = ([green]que é exposto[reset])	  >> [yellow]publico[reset] = ([green]flexão do verbo publicar[reset])	
s[yellow]á[reset]bia      = ([green]inteligente[reset]) 	  >> [yellow]sabia[reset] = ([green]flexão do verbo saber[reset])	
sabi[yellow]á[reset]      = ([green]ave[reset])  	 	  >> [yellow]sabia[reset] = ([green]flexão do verbo saber[reset])	
secret[yellow]á[reset]ria = ([green]atividade[reset])		  >> [yellow]secretaria[reset] = ([green]flexão do verbo secretariar[reset])		 

'''

    def separacao_silabica_2(self):

        return '''Ortografia - Separação Silábica - Professor Elias Santana -\n

Para ter uma correta separação silábica, é importante se pautar em algumas regras:

[bg_red]1º regra: - Toda sílaba deve conter uma vogal.[reset]

B[yellow]o[reset] - l[yellow]a[reset]  - Cada sílaba da palavra 'bola' tem uma vogal.

Outro exemplo:
Psicóloga - Não podemos deixar o 'p' sozinho, lembre-se de que toda sílaba precisa ter uma vogal.
Então para separar a palavra psicóloga temos: ps[yellow]i[reset] - c[yellow]ó[reset] - l[yellow]o[reset] -g[yellow]a[reset]

[bg_green]bíceps[reset] - Lembre-se de que 'ps' de bíceps não é uma sílaba. A letra 'p' e 's' são duas consoantes. É fundamental E REGRA NÚMERO 1 ter ao menos uma vogal na separação silábica.
A separação correta então é: bi - [yellow]ceps[reset]

[bg_red]Regra número 2: Toda sílaba deve conter apenas uma vogal[reset] \n
[blue]Ditongo: [reset]  - Duas vogais juntas que na separação silábica não se separam, porém, respectivamente, um ditongo é formado por uma vogal e uma semivogal na separação silábica ou semivogal e vogal, respectivamente.
[blue]Tritongo: [reset] - Três vogais juntas que na separação silábica não se separam, porém, respectivamente um tritongo é formado por duas semivogais e uma vogal.

Ditongo Crescente: 
Formado por uma SEMIVOGAL e uma VOGAL, respectivamente. Exemplo: A palavra necessário // ne -  ces - sá - r[yellow]io[reset] - A letra 'i' é SEMIVOGAL e a letra 'o' é uma VOGAL.
Outro exemplo de ditongo crescente: A palavra 'série' //  sé - r[yellow]ie[reset] - A letra 'i' é SEMIVOGAL e a letra 'e' é uma VOGAL. 

Ditongo Descrescente:
Formado por uma VOGAL e SEMIVOGAL, respectivamente. Exemplo: saudade / [yellow]sau[reset] - da - de  :: Temos na separação silábica a letra 'a' VOGAL e 'u' SEMIVOGAL, ou seja, Ditongo Descrescente.
chapéu / cha - [yellow]péu[reset] :: Temos na separação silábica, a letra 'é' VOGAL e 'u' SEMIVOGAL, ditongo descrescente.

Atenção - A letra 'a' sempre será VOGAL. Nunca será semivogal. \n
A letra 'i' e 'u' são predominantemente SEMIVOGAIS.\n
A letra 'e' e 'o' são predominantemente vogais.

Exemplo: A palavra 'série' - sé - [yellow]rie[reset] - Veja que na separação silábica da palavra ocorre um ditongo em que a letra 'i' é predominantemente SEMIVOGAL seguida da letra 'e' que é predominantemente VOGAL, portanto é um ditongo CRESCENTE.\n
Outro exemplo: A palavra 'mãe', que é monossílaba, mas possui um ditongo. A letra 'a' é vogal sempre, e a letra 'e' apesar de ser predominantemente vogal, agora passa a ser SEMIVOGAL. \n
A palavra 'mão' - Palavra monossílaba com ditongo em que a letra 'a' que sempre será vogal e a letra 'o' que é predominantemente vogal passa a ser SEMIVOGAL. Sendo assim, um ditongo CRESCENTE.\n
Atenção para não confundir nos casos da palavra 'FUI' e 'VIU' em que ambos são DITONGOS DESCRESCENTES.\n
No caso da palavra 'FUI' o som mais forte é a letra 'u', portanto a letra 'u' será a vogal e a letra 'i' é semivogal. Ditongo descrescente.\n
No caso da palavra 'VIU' o som mais forte é a letra 'i', portanto a letra 'i' será a vogal e a letra 'u' a semivogal. Ditongo descrescente também\n

No caso dos TRITONGOS:
A palavra PARAGUAI // pa - ra - [yellow]guai[reset] :: Na sílaba 'guai' eu só tenho uma VOGAL, a letra 'a'. E as letras 'u' e 'i' como sendo SEMIVOGAIS.\n\n

[bg_red]Regra 03: Separar os HIATOS CORRETAMENTE[reset]
[blue]O fenômenos Hiato são duas vogais juntas que na separação silábica se separam.[reset]\n
Exemplo: saída :: s[green]a -[reset] [yellow]í[reset] - da\n 
prejuízo :: pre - j[yellow]u - í[reset] - zo //\n
Israel   :: is - r[yellow]a - e[reset]l //\n

[bg_red]Regra 04: Separam-se alguns dígrafos da língua portuguesa:[reset][bg_green] RR,  SS,  SC,  SÇ.[reset] 
Exemplo: [green]carro[reset] :: ca[yellow]r - r[reset]o - Dígrafos separados por possuir 'RR'.\n
[green]possível[reset] :: po[yellow]s - s[reset]í - vel - Dígrafos separados por possuir 'SS'.\n
[green]nascer[reset] :: na[yellow]s -  c[reset]er :: Dígrafos separados por possuir 'SC'.\n
[green]cresça[reset] :: cre[yellow]s - ç[reset]a :: Dígrafos separados por 'SÇ'.\n

[bg_red]CUIDADO - Separar palavras em que usam prefixos:[reset]\n
Bisavó  :: bi - sa - vó   :: [yellow]   O prefixo 'bis' seguida de vogal do radical da palavra 'a' de 'avó' -[reset][blue] A junção ocorrerá pela última consoante do prefixo e a primeira vogal do radical.[reset]\n
Bisneto :: bis - ne - to  :: [yellow] Agora o prefixo 'bis' terminada em consoante seguida de uma consoante no radical da palavra, ocorre a separação silábica entre elas.[reset]\n

Veja outro exemplo para ficar mais claro:\n
A palavra [green]transatlântico[reset] :: O prefixo 'trans' termina em consoante 's' e o radical da palavra inicia com 'a', portanto, ocorre a junção dessas letras na separação silábila:\n\n  tran - [yellow]sa[reset] - tlân - ti - co\n
A palavra [green]transfusão[reset]     :: O prefixo trans' termina em consoante 's' e o radical da palavra inicia com consoante 'f', sendo assim ocorre a separação do prefixo da palavra na separação silábica:\n\n [yellow]trans[reset] - fu - são\n

Outras palavras para melhor fixação:\n
A palavra [green]sublinhar[reset]  :: Utiliza o prefixo 'sub' que termina com 'b' de consoante. E o radical da palavra inicia com 'l', outra consoante. Na separação silábica ocorre a separação entre as vogais: su[yellow]b - l[reset]i - nhar\n
A palavra [green]subemprego[reset] :: Utiliza o prefixo 'sub' que termina com 'b' de consoante. E o radical da palavra inicia com 'e' de VOGAL. Na separação silábica ocorre portanto a junção entre a consoante e a vogal: su - [yellow]bem[reset] - pre - go\n

[bg_green]Translinealidade[reset] Palavras com hífen em que ao separar a palavra colocar outro hífen embaixo da linha.
'''

    def questoes_concurso(self):
        return '''Questões de concurso - Geral -
001 - Instituto AOCP/ITEP-RN/Perito Criminal/área geral/2021:
Assinale a alternativa em que todas as palavras apresentam a mesma regra de acentuação gráfica.

a) destruída - critério - obediência:
[yellow][Des - tru - í - da][reset]  -       [blue]Paroxítona com vogal 'i' tônica, mantêm acentuação. Lembre-se que acentua-se o 'i' ou 'u' tônicos do hiato quando tais vogais se encontram sozinhas ou acompanhadas de 's' na sílaba.[reset]
[yellow][cri - té - ri - o][reset]      -    [blue]Proparoxítona acentuada corretamente, terminada em ditongo.[reset]
[yellow][o - be - di - ên - cia][reset] - [blue] Paroxítona acentuada corretamente, terminada em ditongo.[reset]
[bg_red]Alternativa 'a' incorreta pois as palavras não possuem as mesmas regras de acentuação[reset]

b) contemporâneo - indivíduo - critério:
[yellow][con - tem - por - râ - neo][reset] - [blue]Paroxítona acentuada corretamente, terminada em ditongo.[reset]
[yellow][in - di - ví - duo][reset] - 	      [blue]Paroxítona acentuada corretamente,terminada em ditongo.[reset]
[yellow][cri - té - rio][reset] - 	      [blue]Paroxítona acentuada corretamente,terminada em ditongo.[reset]
[bg_green]Alternativa 'b' a correta, as três palavras possuem as mesmas regras de acentuação gráfica.[reset]

c) destruída - princípio - indivíduo:
[des - tr[reset]u - í - da][reset]    -  [blue]Paroxítona acentuada corretamente devido ao hiato[reset]
[prin - [yellow]cí - pio][reset]      -  [blue]Paroxítona acentuada corretamente, terminada em ditongo.[reset]
[in - di - [yellow]ví - duo][reset]   -  [blue]Paroxítona acentuada corretamente, terminada em ditongo.[reset]
[bg_red]Alternativa incorreta porquê as palavras possuem regras diferentes: a palavra destruída e individuo são paroxitonas e princípio é proparoxitona.[reset]

d) âmbito - album - hábito:
[yellow][âm - bi - to][reset] - [blue]Proparoxítona acentuada corretamente.[reset] 
[yellow][ál - bum][reset]     - [blue]Paroxítona acentuada corretamente[reset]
[yellow][há - bi - to][reset] - [blue]Proparoxítona acentuada corretamente[reset]
[bg_red][Alternativa incorreta por quê as palavras âmbito e hábito possuem a regra de acentuação das proparoxítonas, que sempre são acentuadas. A palavra álbum continua com acento por ser paroxítona terminada em 'um','uns'.[reset]

e) âmbito - código - nível:
[yellow][âm - bi - to][reset] - [blue]Proparoxítona acentuada corretamente.[reset]
[yellow][có - di - go][reset] - [blue]Proparoxítona acentuada corretamente.[reset]
[yellow][ní - vel][reset]     - [blue]Paroxítona acentuada corretamente.[reset]
[bg_red][Alternativa incorreta por que a palavra 'nível' é paroxítona][reset]

002 - (INSTITUTO AOCP/CÂMARA DE TERESINA PI/ASSISTENTE LEGISLATIVO/2021):
Assinale a alternativa em que os pares de palavras são acentuados de acordo com a mesma regra:

a) Até - porquê - [bg_red]Possuem regras diferentes, 'até' é oxítona terminada em 'E'. 'Porquê' recebe acento pois se trata de um substantivo.[reset]
b) Não - têm [bg_red]Possuem regras diferentes, til não é acento e sim uma nasalização. 'têm' = acento diferencial.[reset]
c) Implicações - construídos: o til não é acento e sim uma marca de nasalização.\n[red][cons - tru -[reset][yellow] í[reset] - dos][reset][paroxítona com vogal tônica sozinha antecedido de hiato]\n Portanto possuem regras diferentes
d) É - até [bg_red]Possuem regras diferentes,letra 'é' monossilábicos, 'até' oxítona terminada em 'E'.[reset]
e) Edifícios - equilíbrio: [green]CORRETA[reset]
[e - di - [yellow]fí[reset] - ci - os] [e - qui - [yellow]lí[reset] - bri - o][blue]Possuem a mesma regra de acentuação, ambas são proparoxítonas, terminadas em ditongo.[reset]

003 -(INSTITUTO AOCP/PREFEITURA DE JOÃO PESSOA PB/ENGENHEIRO/2021):
Qual alternativa apresenta todas as palavras corretamente grafadas quanto à ortografia e à acentuação gráfica?
a) Ciência, sindrome, botânica, antídoto, farmaco.
[ci  - [yellow]ên[reset]  - cia][Eventual proparoxítona com o isolamento da vogal 'a' - Paroxítona]
[[red]sin[reset] - dro - me][bg_red][ERRADO][reset][blue][Proparoxítona que é obrigatório o acento][reset]
[bo  - [yellow]tâ[reset]  - ni - ca][Proparoxítona corretamente acentuada]
[an  - [yellow]tí[reset]  - do - to][Proparoxítona corretamente acentuada]
[[yellow]far[reset] - ma  - co][bg_red][ERRADO][reset][Propaxoxítona sem acento, incorreto.]
[bg_red]Alternativa 'a' incorreta pois apresenta palavras que estão incorretas quanto a ortografia e acentuação gráfica.[reset]

b) Sintomático; pessonha, infecção, fármaco, síndrome:
[sin - to - [yellow]má[reset] - ti - co][blue]Palavra proparoxítona acentuada corretamente.[reset]
[bg_red]A palavra peçonha está escrita incorretamente, não é peçonha e sim peçonha.[reset]
[in - fec - [yellow]ção[reset]] :: Palavra oxítona terminada em 'ão' devidamente acentuada.
[[yellow]fár[reset] - ma - co]  :: Proparoxítona acentuada corretamente.
[[yellow]sín[reset] - dro - me] :: Proparoxítona acentuada corretamnte.
[bg_red] No geral temos uma palavra incorreta, portanto a alternativa não é a correta.[reset]

c) Peçonha, fármaco, orgânico, infecção, sintomático:
[pe - [yellow]ço[reset] - nha] ::  Ortografia correta.
[[yellow]fár[reset] - ma - co] ::  Proparoxítona acentuada corretamente.
[or - [yellow]gâ[reset] - ni - co] :: Proparoxítona acentuada corretamente.
[in - fec - [yellow]ção[reset]]  :: Oxítona acentuada corretamente e sua grafia está correta.
[sin - to - [yellow]má[reset] - ti - co] :: Proparoxítona acentuada corretamente.
[bg_green] Alternativa c está correta.[reset]

d)Botânica, infexão, sintomatico, antidoto, orgânico:
[bo - [yellow]tâ[reset] - ni -ca ] :: Proparoxítona acentuada corretamente
[bg_red] A palavra 'infexão' infelizmente sua grafia esta incorreta.[reset].
sintomatico - [bg_red]A acentuação está ausente na sílaba 'ma', sendo a sílaba tônica na posição de proparoxítona.[reset].
an - ti - do - to :: [bg_red]A acentuação está ausente na sílaba 'ti', sendo a sílaba tônica na posição de proparoxítona.[reset]
or - gâ - ni - co :: Palavra devidamente acentuada. Proparoxítona.
[bg_red] A alternativa 'd' está incorreta conforme os erros acima.[reset]

e)Organico, peçonha, botanica, ciência, sintomatico:
[red] A palavra orgânico precisa de acento.[reset]
[green] Peçonha está corretamente grafada.[reset]
[red]botanica está faltando acentuação no 'a' [reset]
ciência está corretamente grafada.
[red]sintomatico está faltando acentuação no 'a' da sílaba 'ma'[reset]
[bg_red]A alternativa 'e' está incorreta devido a vários erros.[reset]

004 - (INSTITUTO AOCP/PREFEITURA DE JOÃO PESSOA PB/TÉCNICO EM RADIOLOGIA/2021):
Considerando as regras de acentuação dos vocábulos em Língua Portugues, assinale a alternativa cujo termo destacado receba acento pelo mesmo motivo
que 'antropológica' empregado no texto...'a família sob uma perspectiva antropológica, é um grupo social concreto...'
a)A [yellow]família[reset], sob uma perspectiva antropológica, é um grupo social concreto..'
b)Essas relações sociais podem contribuir para a prevenção do adoecimento mental, podendo fazer parte de uma macanismo chamado [yellow]'resiliência'.[reset]
c)Todavia, o estado emocional do outro [yellow]também[reset] precisa ser levado em consideração.
d) A abordagem não [yellow]empática[reset] desse sofrimento pode desgastar ainda mais as relações interpessoais.[green][CORRETA][reset]
e) Oferecer ajuda com diálogo aberto e uma visão menos estigmatizada do sofrimento mental, pode ser um grande passo para uma relação [yellow]saudável.[reset]

Vejamos as alternativas:\n\n
Na alternativa 'a': a acentuação de 'antropológica' recebe acento pelo mesmo motivo de 'família'?
[yellow]an - tro - po - ló - gi - ca[reset]			:: [bg_green]Proparoxítona devidamente acentuada. [reset]
Na alternativa 'a': fa - [yellow]mí[reset] - lia		:: [blue]É uma paroxítona terminada em ditongo que pode ser uma eventual proparoxítona.[reset]
Na alternativa 'b': re - si - li - [yellow]ên[reset] - cia      :: [blue]Paroxítona terminada em ditongo que pode ser uma eventual proparoxítona.[reset]
Na alternativa 'c': tam - [yellow]bém[reset] 	        	:: [red]Oxítona terminada em 'em' que recebe outra regra da proparoxítona antropológica.[reset]
Na alternativa 'd': 'em - [yellow]pá[reset] - ti - ca'		:: [green]Proparoxítona que recebe a mesma regra de antropológica.[reset]
Alternativa 'e': sau - [yellow]dá[reset] - vel 			:: [red]Paroxítona terminada em 'l' com acentuação correta mas não é a mesma regra das proparoxítonas.[reset]

005 - (INSTITUTO AOCP/IPE PREV/ANALISTA EM PREVIDÊNCIA/DIREITO/EDITAL N.002/2022):
Assinale a alternativa em que os termos destacados foram acentuados de acordo com a mesma norma gramatical:
a)O surpreendente efeito da positividade [yellow]'tóxica'[reset] na [yellow]'saúde'[reset] mental.[bg_red][ERRADO][reset]
[yellow]tó[reset] - xi - ca :: Proparoxítona com acentuação obrigatória. :: Sa - [yellow]ú[reset] - de // Paroxítona com acentuação correta na tónica 'u'
[bg_red]Portanto normas gramaticais diferentes para acentuação[reset]
b)Pode parecer [yellow]'contraditório'[reset] mas a positivdade pode ser [yellow]'tóxica'[reset].
con - tra - di - [yellow]tó[reset] - r[yellow]io[reset] :: [blue]Paroxítona[reset] terminada em ditongo continua com acentuação. // [yellow]tó[reset] - xi - ca :: Proparoxítona com acentuação obrigatória.
[bg_red]Alternativa errada por que as regras para acentuação são diferentes. [reset].
c) O [yellow]psicólogo[reset] da saúde Antonio Rodellar, especialista em transtornos de ansiedade e hipnose [yellow]clínica[reset], prefere falar em 'emoções desreguladas' do que 'negativas'.
psi - [yellow]có[reset] - lo - go :: Proparoxítona acentuada de forma correta. // [yellow]clí[reset] - ni - ca :: Proparoxítona acentuada de forma correta.
[bg_green] A alternativa C está correta pois as palavras possuem as mesma regra de acentuação gráfica.[reset].
d) [yellow]'Gutierrez'[reset] acredita que houve um aumento do positivismo tóxico nos [yellow]'últimos'[reset] anos, mas principalmente durante a pandemia.
gu - t[yellow]i - e[reset]r - rez :: Paroxítona com hiato sem acentuação, correto. // [yellow]úl[reset] - ti - mos :: Proparoxítona acentuada corretamente.
[bg_red] As palavras possuem regras de acentuação diferentes.[reset].
e) Como aplicar isso na [yellow]prática[reset]. Em vez de dizer 'não pense nisso, seja positivo' diga 'me diz o que [yellow]você[reset] está sentindo, eu te escuto.'
[yellow]prá[reset] - ti - ca :: Proparoxítona acentuada corretamente. // vo - [yellow]cê[reset] :: Oxítona acentuada corretamente.
[bg_red]Mesmo com as palavras acentuadas corretamente possuem suas regras diferentes.[reset]
006 - (IBFC/PREFEITURA DE DOURADOS MS/TOPÓGRAFO/2022):
Sabe-se que os vocábulos podem ser analisados quanto à acentuação e à separação silábica. Assinale, dentre as alternativas, aquela que corresponde à seguência abaixo:
Oxítona dissílaba - proparoxítona polissílaba - oxítona trissílaba
a) é - Atlântico - você [bg_red][ERRADA][reset][é uma uma palavra monossílaba] :: atlântico é uma proparoxítona polissílaba :: você é uma dissílaba oxítona
b) também - Atlântico - Guarujá [green][CORRETA][reset]
c) porquê - paradisíaca - Pérola [bg_red][ERRADA][reset] [por - quê]Dissílaba oxítona :: pa - ra - di - sí - a - ca // 6 sílabas - polissilábica proparoxítona
pérola - proparoxítona - trissilábica
d) já - paradisíaca - pérola[bg_red][ERRADA][reset] - 'já' é monossilábica e as outras duas palavras estão corretas de acordo com a ordem.

007 -(IBFC/PREFEITURA DE DOURADOS MS/TOPÓGRAFO/2022). Em relação à acentuação oficial há uma sequência de palavras retiradas do texto e que foram acentuadas
como ´oxítona - paroxítona - proparoxítona'. Assinale então a alternativa em que haja essa sequência:
a) retórica - importância - será: [bg_red][ERRADO][reset] // re - [yellow]tó[reset] - ri - ca :: Proparoxítona
im - por - [yellow]tân[reset] - cia :: Paroxítona por ter a sílaba tônica na penúltima sílaba e eventual proparoxítona: im - por - tân - ci - [yellow]a[reset]
se - [yellow]rá[reset] :: oxítona, tônica na última sílaba 
b) será - importância - retórica: [bg_green][CORRETA][reset] :: se - [yellow]rá[reset] :: Tônica na última sílaba - oxítona
im - por - tân - cia :: Paroxítona por ter a sílaba tônica na penúltima sílaba e eventual proparoxítona: im - por - tan - ci - [yellow]a[reset]
[bg_green]De acordo com a sequência do enunciado a alternativa correta é a 'b'.[reset]
c) importância - será - retórica:[bg_red][ERRADO][reset] importância não é oxítona e sim paroxítona, será é oxítona e retórica é proparoxítona :: 
d) retórica - será - importância:[bg_red][ERRADO][reset] retórica é proparoxítona , será é oxítona e importância é paroxítona.
008-. (IBFC/AFEAM/ESPECIALISTA DE FOMENTO/ADMINISTRAÇÃO/2022) Assinale a alternativa correta em referência à ortografia e à acentuação.
I  - Difícil é uma palavra oxítona, portanto acentuada na última sílaba.
II - Lógica é uma palavra proparoxítona, portanto acentuada na antepenúltma sílaba.
II - Intagíveis recebe o acento diferencial na penúltima sílaba para registrar a sua forma no plural.
Estão corretas as afirmativas:
a) I apenas [bg_red][ERRADO][reset][Difícil é uma palavra paroxítona]
b) II apenas [bg_green][CORRETO][reset][Corretamente acentuada por ser proparoxítona]
c) III apenas [bg_red][ERRADO][reset][Acento diferencial foram retirados em verbos e palavra não é verbo e sim um substantivo]
d) I e III apenas[bg_red][ERRADO][reset]

009. (IBFC/CÂMARA DE FRANCA SP/MOTORISTA/2022) Atente à acentuação das palavras em destaque, nas estruturas retiradas do texto:
I   - Joana é professora de [yellow]ginástica[reset]
II  - Ele é pouco [yellow]confortável[reset]
III - Ele tem [yellow]três[reset] filhas
Identifique dentre as alternativas abaixo, a única em que o padrão de acentuação segue ao das palavras em destaque:
a) caráter, sábado, cortês:
gi - [yellow]nás[reset] - ti - ca é [blue] Proparoxítona [reset] e ca - [yellow]rá[reset] - ter é [blue]Paroxítona.[reset].[bg_red][ERRADO][reset]
[yellow]sá[reset] - ba - do  -> [blue]Proparoxítona[reset] e con - for - tá - vel é [blue]Paroxítona[reset][bg_red][ERRADO][reset]
cor - [yellow]tês[reset] :: [blue]Oxítona[reset]  e três é [blue]oxítona monossílaba[reset][bg_red][ERRADO][reset]
b) freguês, sólido, éter:
fre - [yellow]guês[reset] :: [blue]Oxítona[reset] e ginástica é propaxorítona[bg_red][ERRADO][reset]
[yellow]só[reset] - li - do é [blue]Proparoxítona[reset] e confortável é paroxítona.[bg_red][ERRADO][reset]
[yellow]é[reset] - ter é paroxítona e três é oxítona monossilábica.
c) pássaro,vulnerável,pés:
[yellow]pás[reset] - sa - ro é [blue]Proparoxítona[reset] e ginástica também.[bg_green][CORRETO][reset]
vul - ne - [yellow]rá[reset] - vel é paroxítona e confortável também[bg_green][CORRETO][reset]
pés é oxítona monossilaba e três também[bg_green][CORRETO][reset]
d) máquina, afável, português:
[yellow]má[reset] - qui - na // Proparoxítona e ginástica também.[bg_green][CORRETO][reset]
a - [yellow]fá[reset] - vel // Paroxítona e confortável também[bg_green][CORRETO][reset]
por - tu - [yellow]guês[reset] // Oxítona trissilaba e três é oxítona monossilaba.[bg_red][ERRADO][reset]
[bg_green] Alternativa C a correta.[reset]\n
10 -(IBFC/EBSERH/TÉCNICO EM CONTABILIDADE/2022) - O novo acordo ortográfico da língua portuguesa alterou a acentuação de algumas palavras. No entanto, 'réis'
conserva o acento que recebia em função de seu ditongo aberto. Dentre as palavras abaixo, assinale a que apresenta INDEVIDAMENTE o acento gráfico.
a) herói [Correto, manteve o acento]
b) céu [Monossílaba que manteve o acento]
c) dói [Monossílaba que manteve o acento]
d) véu [Monossílaba que manteve o acento]
e) jibóia [bg_red]ERRADO[reset] -  Palavra perdeu o acento com ditongo antecedido por hiato.

011- (IADES/CRF/AUXILIAR L/SERVIÇOS GERAIS/2017): A palavra sofá obedece a mesma regra de acentuação gráfica que a palavra:
a) babá [bg_green][CORRETO][bg_green][A palavra babá é oxítona que obedece a mesma regra de acentuação gráfica.[reset]
b) árvore [Propaxoxítona que possue regra diferente de acentuação do que a palavra 'sofá']
c) índio [Paroxítona que recebe acentuação com regra diferente da palavra 'sofá']
d) sílaba [Proparoxítona que recebe regra de acentuação diferente da palavra 'sofá']
e) família [Paroxítona terminada em ditongo com regra diferente para a palavra 'sofá'-oxítona]

012-(IADES/AL-GO/REVISOR ORTOGRÁFICO/2019) - Com base na norma-padrão da língua portuguesa, assinale a alternativa que apresenta palavras acentuadas
segundo a mesma regra gramatical:

a) 'tradição' e 'língua': [tra - di - [yellow]ção[reset]] - Sílaba tônica na última - Oxítona // [yellow]lín[reset] - gua - Tônica na penúltima sílaba, Paroxítona.
b)'prosódia' e 'gravatá': [pro - [yellow]só[reset] - dia] - Sílaba tônica na penúltima sílaba. - Paroxítona // gra - va - [yellow]tá[reset] - Tônica na última sílaba - Oxítona
c)'porém' e 'junção': po - [yellow]rém[reset] // Oxítona -- jun - [yellow]ção[reset] -- Oxítona :: Só que o tio não é considerado acento.
d)'independência' e 'raríssimos': in - de - pen - [yellow]dên[reset] - cia :: Paroxítona -- ra - [yellow]rís[reset] - si - mos :: Proparoxítona
e) 'países' e 'traíra': pa - [yellow]í[reset] - ses //Paroxítona :: Tra - [yellow]í[reset] - ra // paroxítona  :: Alternativa Correta

013 -(IADES/SEASTER PA/TÉCNICO DE ENFERMAGEM/2019):
Considerando as palavras do texto, é correto afirmar que exemplificam uma oxítona e uma paroxítona acentuada graficamente os vocábulos:

a) 'população' e 'políticas' - po - pu - la - ção [til não é acento] // [po - lí - ti - cas ][Proparoxítona]
b) 'é' e 'dimensões' // monossílaba tônica oxítona - // di - men - sões -- oxítona porém, o til não é acento.
c) 'Pará' e 'Assistência' -- pa - rá -- Oxítona // as - sis - tên - cia[Paroxítona][bg_green][CORRETO][reset]
d) 'região' e indígenas' -- re - gi - ão // Oxítona -- in - dí - ge - nas [Proparoxítona]
e) 'Pará' e 'étnica' pa - rá[oxítona] // ét - ni - ca [Proparoxítona]

014. (IADES/AL-GO/POLICIAL LEGISLATIVO/2019) Acerca das regras de acentuação vigentes, assinale a alternativa que indica vocábulo acentuado em conformidade
com a regra das palavras paroxítonas:

a) sofá - [oxítona]
b) país - [oxítona]
c) contribuísse // con - tri - [yellow]bu[reset] - ís - se - [proparoxítona][A sílaba tônica é a antepenúltima]
d) escavação    // es - ca - va - ção       - [oxítona]
e) água // - [paroxítona]

015. (IADES/CAU-RO/ASSISTENTE ADMINISTRATIVO/2018 - Assinale a alternativa que corresponde a palavras acentuadas de acordo com a mesma regra.

a) Resiliência e potência // re - si - li - ên - cia [Paroxítona terminada em ditongo crescente] -- po - tên - cia [Paroxítona terminada em ditongo crescente]
b) Solução e você -// so - lu - ção [oxítona terminada em 'ão'] -- vo - cê[oxítona terminada em 'e']
c) Lição e resiliência -- li - ção[oxítona - terminada em 'ão'] -- re - si - li - ên - cia[Paroxítona terminada em ditongo crescente]
d) único e revisão [ú - ni - co][Proparoxítona] //  re - vi - são [Oxítona terminada em 'ão']
e) você e já [vo - cê]--// Oxítona terminada em 'e' // já [oxítona terminada em a]

016.(FGV/CODEBA/ADMINISTRADOR/2010)Assinale a palavra que foi acentuada seguindo a mesma regra que três:

[green] A palavra três é acentuada pela regra dos monossílabos tônicos em que serão acentuados aqueles terminados em A,E,O seguidos ou não de S.[reset]

a) prevê : [red]não segue a mesma regra porquê 'prevê' são duas sílabas[reset]
b) Até : [red]'a-té' são duas sílabas[reset]
c) além : [red]'a-lém' são duas sílabas[reset]
d) é : [bg_green]CORRETO[reset]
e) país :  duas sílabas, hiato.

017.(FGV/SEFAZ-MS/ANALISTA DE TECNOLOGIA DA INFORMAÇÃO/1º PROVA/2006) 
Assinale a alternativa em que o vocábulo não tenha sido acentuado pela mesma regra que os demais.

a) atrás : oxítona
b) lá : monossílabos tônicos [bg_green]CORRETO[reset]
c) ninguém : oxítona
d) vovó : oxítona
e) você : oxítona

018. (FGV/PREFEITURA DE SALVADOR BA/AUXILIAR DE SERVIÇOS GERAIS/2017) Assinale a opção que apresenta as duas palavras que estão acentuadas corretamente:

a) Família/economía - [red][Economia sem acento][reset]
b) Máquina/Vôo - [red]voo sem acentuação[reset]
c) Aliás/vêem - [red]veem sem acento[reset]
d) Caráter/cooperatíva - [red]cooperativa[reset]
e) Saída/termômetro - saída - hiato // termômetro = proparoxítona

019.(FGV/ALERJ/ESPECIALISTA LEGISLATIVO/REGISTRO DE DEBATES/2017) Os vocábulos cuja acentuação gráfica pode ser justificada simultaneamente por duas regras são:
a) herói / papéis: [red] ambas as palavras são acentuadas conforme a regra dos ditongos abertos (ói,éi)[reset]
b) econômico / histórico: [red] ambos os vocábulos são proparóxítonas acentuadas[reset]
c) pátria / tênue : [bg_green] Os vocábulos podem ser acentuadas pela regra das paroxítonas terminadas em ditongo e acidentalmente pela regra das propaxoxítonas eventuais. Podendo ser chamadas ainda de relativas, acidentais ou aparentes.[reset]
d) gás / três: [red]ambas as palavras são acentuadas pela regra dos monossílabos tônicos.
e) têm / vêm : ambos os vocábulos são acentuados pela regra do acento diferencial.

020. (FGV/MPE-BA/ASSISTENTE TÉCNICO/ADMINISTRATIVO/2017) Obedecem a mesma regra:

a) científicas/reúne : ci - en - tí - fi - cas // proparoxítona :: re - ú - ne // Paroxítona: hiato [red]Regras diferentes[reset]
b) saúde/hábito : sa - ú - de // Paroxítona com hiato // há - bi - to :: Proparoxítona
c) saudável/índice : sau - dá - vel [paroxítona] // ín - di - ce [proparoxítona]
d) cardíacos/será: car - dí - a - cos :: paroxítona com hiato // se - rá :: oxítona
e) família/cardápios: fa - mí - lia :: [paroxítona terminada em ditongo] // car - dá - pios :: Paroxítona também terminada em ditongo. [bg_green]CORRETO[reset]

021.(IBADE/INOVA CAPIXABA/ASSISTENTE SOCIAL/2022) As palavras TÉCNICO, TÊM, IDEIA e ESTRATÉGIA, respectivamente, recebem ou não o acento pelo mesmo motivo que:

a) científico - vêm - assembleia - ciência
téc - ni - co = Proparoxítona
ci - en - tí - fi - co = Proparoxítona

vêm / têm = acentos diferenciais
assembleia e ideia = perderam o acento pela regra do ditongo aberto antecedido de hiato.
ci - ên - cia // Paroxítona terminada em ditongo // estratégia // es - tra -  té - gia :: Paroxítona terminada em ditongo [bg_green]CORRETO[reset]

b) tecnológico - sofá - papeis - história:

tec -  no - ló - gi - co: Proparoxítona // téc - ni -  co // Proparoxítona
têm :: acento diferencial // so - fá : Oxítona
ideia :: perdeu acento // papeis continua com acento
estratégia // es - tra - té - gia :: Paroxítona terminada em ditongo

c) método - crêem - trofeu - domínio:
mé - to - do :: Proparoxítona // técnico :: Proparoxítona
crêem :: perdeu o acento // têm :: Acento diferencial
ideia :: perdeu o acento e troféu ( ditongo aberto ) ainda possui acento
estratégia :: Paroxítona terminada em ditongo e domínio é paroxítona terminado em ditongo.
 
d) crítico - lêem - estreia - européia:
crí - ti - co: Proparoxítona e técnico também
lêem perdeu o acento. agora é leem. e têm ainda mantêm o acento.
européia perdeu o acento por ser terminado em ditongo antecedido de ditongo.
e) época - prevêem - plateia - vitoria :
época :: Proparoxítona e técnico também
prevêem perdeu o acento, vem do verbo prever derivado do verbo ver.
plateia ditongo antecedido de hiato, perdeu o acento na paroxítona.
vitória paroxítona terminada em ditongo.

022. (IBADE/PREFEITURA DE COSTA MARQUES RO/ENGENHEIRO AGRÔNOMO/2022) Como a palavra “ideia”, a grafia está de acordo com as regras de acentuação em:

a) serie [red] série é uma paroxítona terminada em ditongo que continua com acento[reset]
b) assembleia [bg_green] Perdeu o acento terminada em ditongo antecedido de hiato[reset]
c) papeis [red] Ditongo abertos continuam com acento[reset]
d) heroi [red] Continua com acento por ser ditongo aberto [reset]
e) eles tem [red] Acento diferencial deve ser usado para diferenciar  [reset]

[Vamos relembrar que antes da palavra 'ideia' era acentuada. Hoje não é mais. Ocorre que os ditongos abertos (éi,ói) deixaram de ser acentuados na penúltima sílaba
tônica e passaram a ser acentuados na última sílaba tônica. O mesmo evento aconteceu com a palavra 'assembleia'.]

Ditongos abertos:
c[yellow]éu[reset], v[yellow]éu[reset]
id[yellow]ei[reset]a
plat[yellow]ei[reset]a
an[yellow]éi[reset]s
pap[yellow]éi[reset]s
d[yellow]ói[reset]
r[yellow]ói[reset]
her[yellow]oi[reset]co
jib[yellow]oi[reset]a

Veja que são acentuados apenas aqueles que estão na última sílaba tônica.

023. (IBADE/PREFEITURA DE COSTA MARQUES RO/MICROSCOPISTA/2022) Como a palavra “creem”, que não recebe acento, também não será acentuada a seguinte palavra:

a) saida - recebe acento pela regra do hiato com vogal 'i' isolada
b) area  - recebe acento pela regra da paroxítona terminada em ditongo.
c) eles veem (verbo ver) - não recebe acento
d) eles vem (verbo vir)  - recebe acento pelo uso do acento diferencial
e) eles tem (verbo ter)  - recebe acento pelo uso do acento diferencial

024.(IBADE/PREFEITURA DE SOORETAMA ES/PROFESSOR MAE-I/ENSINO FUNDAMENTAL ANOS INICIAIS/2022) Marque as palavras que recebem o acento gráfico pela mesma regra:

a)'número','climáticos','históricas' <- Pelo visto, são acentuadas por serem proparoxítonas
b)'incêndios','área,'avós' <- Proparoxítona terminada em 'os', paroxítona terminada em ditongo e uma oxítona termminada em 'os', todas com regras diferentes;
c)'número','incêndios','média' <- Proparoxítona acentuada corretamente terminada em 'o', proparoxítona acentuada terminada em 'os' e 'média' paroxítona terminada em ditongo
d)'climáticos','média','avós'  <- Proparoxítona terminada em 'os', 'média' paroxítona terminada em ditongo, 'avós' oxítona terminada em 'os'.
e)'históricas','área','média'  <- Proparoxítona terminada em 'as', 'área' paroxítona terminada  em ditongo, 'média' paroxítona terminada em ditongo

025.(IBADE/PREFEITURA DE SOORETAMA ES/PROFESSOR MAE-I/EDUCAÇÃO INFANTIL/2022) Marque as palavras que recebem o acento gráfico pela mesma regra:

a) 'necessária','estratégias','níveis'      <- Paroxítona terminada em ditongo // Paroxítona terminada em ditongo  // ní - veis :: paroxítona terminada em ditongo [bg_green]CORRETA[reset]
b) 'pandêmica','estratégias','níveis'       <- Proparoxítona // Paroxítona terminada em ditongo // Paroxítona terminada em ditongo.
c) 'coronavírus','pandêmica','níveis'       <- Paroxítona terminada em 'US' // Proparoxítona  // Paroxítona terminada em ditongo.
d) 'pandêmica','necessária','estratégias'   <- Proparoxítona // Paroxítona terminada em ditongo // Paroxítona terminada em ditongo.
e) 'coronavírus','necessária','estratégias' <- Paroxítona terminada em 'us'// Paroxítona terminada em ditongo  // Paroxítona terminada em ditongo.

026. (IBADE/ISE-AC/AGENTE SOCIOEDUCATIVO/2021) Assinale a sequência em que as palavras são acentuadas pela mesma regra:

a) alguém, álbum, dendê [red][regras diferentes] // oxítona, paroxítona, oxítona[reset]
b) egoísta, baú, cafeína [bg_green][CORRETO][reset] // eg[yellow]o - ís[reset]- ta (hiato) // b[yellow]a - ú[reset] ( hiato ) // ca - f[yellow]e - í[reset] - na (hiato)
c) próximo, imóvel, último [red][regras diferentes][reset] // proparoxítona, i - [yellow]mó[reset] - vel :: Paroxítona //  [yellow]úl[reset] - ti - mo :: Proparoxítona
d) revólver, ningúem, através [red][regras diferentes] // Paroxítona, nin - guém [Oxítona] // Oxítona [reset]
e) chapéu, refém, você [red] cha [reset]- [green]péu[reset] - Acentuação gráfica por ser ditongo aberto. re - [red]fém[reset] - Oxítona e vo - cê = oxítona. 

027. (IBADE/SEE-AC/PROFESSOR BRASILITA P2/2020) Marque a alternativa que descreve a acentuação da palavra salário:

a) monossílabo tônico
b) paroxítona terminada em ditongo [bg_green] CORRETA [reset]
c) proparoxítona
d) oxítona terminada em vogal oral 'o'
e) hiato em posição paroxítona

028. (IBADE/SEE-AC/PROFESSOR PNS/P2/2020) Observe as formas destacadas em “Ocorrem normalmente na entrada ou [bg_green]saída[reset] do [bg_green]prédio[reset], ou ainda quando os professores não estão
por perto.” e assinale a alternativa com as mesmas regras de acentuação.
[red] saída  = hiato [reset]
[red] prédio = paroxítona terminada em ditongo [reset]

a) céu / vítima [red][regras de acentuação diferentes][reset]  // [blue]Céu = Ditongo aberto[reset] // [blue]Vítima = proparoxítona[reset]
b) média / próprias : [yellow]mé[reset] - d[yellow]ia[reset]   // Paroxítona terminada em ditongo // [yellow]pró[reset] - pr[yellow]ias[reset] // Paroxítona terminada em ditongo
c) célula / média [red] Regras de acentuação diferentes[reset] // [yellow]cé[reset] - lu - la = Proparoxítona // [yellow]mé[reset] - d[green]ia[reset] // Paroxítona terminada em ditongo
d) baú / mídia [bg_green] 'ba - ú' e 'sa - í - da' // regra do hiato // [blue]'Mídia' e 'prédio' Paroxítonas terminadas em ditongo... [reset]
e) açúcar / mídia [red] a - [reset][yellow]çú[reset][red] - car = Paroxítona e 'ar' // mídia = paroxítona terminada em ditongo[reset]

029. (IBADE/SEE-AC/PROFESSOR MEDIADOR P1/2020) O vocábulo “grávida” é acentuado pela regra ortográfica descrita em:

a) proparoxítona a ser sempre acentuada [bg_green]CORRETO[reset]
b) paroxítona a ser sempre acentuada
c) oxítona a ser sempre acentuada
d) paroxítona terminada em vogal 'a' deve ser sempre acentuada
e) oxítona terminada em vogal 'a' deve ser sempre acentuada

030. (IBADE/SEE-AC/ASSISTENTE EDUCACIONAL/2020) Assinale a alternativa que possua vocábulo acentuado pela mesma justificativa empregada em [blue]terapêutico[reset]:
te - ra - pêu - ti - co = Proparoxítonas
a) saúde [red] Justificativas diferentes [reset] // sa - ú - de [acentuada por regra do hiato]
b) benefícios:  be - ne - fí - cios Paroxítona
c) esquizofrênico: es - qui - zo - [yellow]frê[reset] - ni - co // Proparoxítona [bg_green]CORRETA a C[reset]
d) até : dissílaba oxítona
e) responsável: res - pon - [yellow]sá[reset] - vel // Paroxítona.

031. (IBADE/SEE-AC/PNS P2/LÍNGUA PORTUGUESA/2020) “Próprio” é palavra usada no texto, qual a justificativa para seu emprego de acentuação:

[red]pró - prio[reset]

a) proparoxítona [bg_red]ERRADO[reset]
b) paroxítona terminada em vogal 'o'. [bg_red]ERRADO[reset]
c) paroxítona terminada em ditongo [bg_green]CORRETO[reset]
d) hiato em posição paroxítona [bg_red]NÃO POSSUI HIATO[reset]
e) hiato em posição oxítona [bg_red]NÃO POSSUI HIATO[reset]

032. (IBADE/PREFEITURA DE LINHARES-ES/TÉCNICO PEDAGÓGICO/2020) No trecho “Fui checar na minha lista de [bg_green]excluídos..[reset]”,
 a palavra destacada é acentuada pela mesma razão que:\n
[blue]A palavra 'excluídos' - ex - clu - í - dos [é uma paroxítona acentuada por regra de hiato][reset]

a) bíceps   - [red] Essa palavra é uma paroxítona. A palavra 'excluídos' - ex - clu - í - dos [é uma paroxítona acentuada por regra de hiato]
b) anzóis   - [red] An - z[reset][green]óis[reset] Acentuada por ser ditongo aberto em oxítona 'ói' 
c) límpido  - [red] Proparoxítona [reset]
d) calvície - Paroxítona terminada em ditongo
e) egoísta  - e - g[yellow]o - í[reset]s - ta // Paroxítona terminada em vogal com hiato [bg_green]Alternativa correta[reset]

033. (IBADE/CÂMARA DE PORTO VELHO RO/TAQUÍGRAFO/2018) O acento gráfico da palavra [bg_green]“dará”[reset] é justificado pela mesma regra que determina a acentuação da palavra:

a) dá [red][monossilaba tônica diferente da acentuação de 'dará' oxítona dissilaba][reset]
b) você [bg_green]CORRETO[reset]
c) várias [red] Errado por ser paroxítona[reset]
d) adorável [red] Errado por ser paroxítona[reset]
e) grajaú [red] Gra - ja -[reset][yellow] ú [reset] Regra de acentuação mantida

034. (IBADE/IDAF-AC/ENGENHEIRO AGRÔNOMO/2020) Assinale a alternativa contendo vocábulos acentuados pela mesma regra:

a) exílio / divórcio / gírias: e - [yellow]xí[reset] - l[yellow]io[reset] - Paroxítona terminada em ditongo // di - [yellow]vór[reset] - c[green]io[reset] // Paroxítona terminada em ditongo // [yellow]gí[reset] - r[green]ia[reset]s // Paroxítona terminada em ditongo  [bg_green]CORRETA[reset]
b) pôsteres / exílio / país: [yellow]pôs[reset] - te - res // Proparoxítona // e - xí - lio [paroxítona terminada em ditongo] // pa - ís[Hiato]
c) órfãos / há / princípio: [yellow]ór[reset] - fãos // Paroxítona terminada em ditongo // 'há' monossílaba // prin - [yellow]cí[reset] - p[green]io[reset] :: Paroxítona terminada em ditongo  
d) mênstruo / pôsteres / há : [yellow]mêns[reset] - tr[green]uo[reset] // Paroxítona // [yellow]pôs[reset] - te - res :: Proparoxítona // 'há'- monossílaba
e) exílio / país / órfãos: e - [yellow]xí[reset] - l[green]io[reset] :: paroxítona terminada em ditongo /// pa - ís :: HIATO // [yellow]ór[reset] - fãos :: Paroxítona terminada em ditongo    

035. (CESPE/CEBRASPE/PC-RO/DATILOSCOPISTA POLICIAL/2022) Assinale a opção em que as palavras destacadas do texto são acentuadas graficamente de acordo com a mesma
regra de acentuação gráfica.

a) rentável e época [red]Possuem regras diferentes , um é paroxítona e outra é proparoxítona[reset]
b) substituídos e vários [red] paroxítona com hiato e 'vários' paroxítona terminada em ditongo, portanto regras diferentes[reset]
c) contribuíram e econômico [red] Paroxítona com hiato e 'econômico' é uma proparoxítona, regras diferentes [reset]
d) contribuíram e substituídos [bg_green] Possuem a mesma regra de acentuação [reset][bg_green][CORRETO][reset]
e) também e histórico [red] Oxítona e 'histórico' é proparoxítona.

036. (CESPE/CEBRASPE/SEED-PR/PROFESSOR/SÉRIES INICIAIS/2021) Os vocábulos [bg_green]“países” e “línguas”[reset] possuem a mesma classificação quanto à tonicidade, porém um difere
do outro quanto à regra empregada para a utilização do acento agudo. Assinale a opção que
indica a correta classificação desses vocábulos quanto à tonicidade e que explica corretamente as regras de acentuação aplicadas a eles.

a) Ambos os vocábulos são paroxítonos, contudo “línguas” é acentuado porque sua última sílaba contém um ditongo crescente átono, ao passo que “países” é acentuado porque sua sílaba
tônica forma um hiato com a vogal da sílaba anterior. [bg_green]CORRETO[reset]

b) Ambos os vocábulos são proparoxítonos, contudo “línguas” é acentuado porque sua última sílaba contém um ditongo decrescente átono, ao passo que “países” é acentuado porque sua
última sílaba termina com “s”.[bg_red]ERRADO[reset]

c) Ambos os vocábulos são paroxítonos, contudo “línguas” é acentuado porque sua última sílaba termina com “s”, ao passo que “países” é acentuado porque sua sílaba tônica forma um hiato
com a vogal da sílaba anterior.[bg_red]ERRADO[reset]

d) Ambos os vocábulos são oxítonos, contudo “línguas” é acentuado porque tem três sílabas, ao passo que “países” é acentuado porque sua sílaba tônica contém um ditongo crescente.[bg_red]ERRADO[reset]

e) Ambos os vocábulos são proparoxítonos, contudo “línguas” é acentuado porque tem duas sílabas, ao passo que “países” é acentuado porque tem três sílabas.[bg_red]ERRADO[reset]
  

037. (CESPE/UEPA/AGENTE ADMINISTRATIVO/2008) Assinale a opção em que todas as palavras estão acentuadas segundo a mesma regra.

a) parênteses, próxima, múltiplas: pa - [yellow]rên[reset] - te - ses // [yellow]pró[reset] - xi - ma // [yellow]múl[reset] - ti - plas :: Proparoxítonas [bg_green] CORRETO [reset] 
b) várias, audiência, ninguém: [yellow]vá[reset] - r[green]ia[reset]s  :: au - di - [yellow]ên[reset] - c[yellow]ia[reset] :: paroxítonas terminadas em ditongo já a palavara ninguém é oxítona.
c) época, obrigadíssimo, está: '[yellow]é[reset] - po - ca' , 'o - bri - ga - [yellow]dís[reset] - si - mo' são proparoxítona e 'está' é oxítona.
d) vício, vírus, é: [yellow]ví[reset] - c[green]io[reset] - Paroxítona terminada em ditongo e 'ví - rus' paroxítona terminada com 'us' e 'é' monossilaba tônico.

038. (CESPE/CEBRASPE/PC-PB/PAPILOSCOPISTA E TÉCNICO EM PERÍCIA/2009) Assinale a opção que apresenta palavras cuja acentuação não se explica pela mesma regra.

a) Belém - Pará - até [blue] As três palavras são oxítonas.[reset]
b) violência - própria - delinquência [blue] vio -[reset][yellow] lên[reset][blue] - cia[reset] - Paroxítona terminada em ditongo. // [yellow]pró[reset] - pria[reset] // Paroxítona terminada em ditongo. // de - lin - [yellow]quên[reset] - c[blue]ia[reset] :: Paroxítona terminada em ditongo
c) constituída - vândalos - subterfúgios : cons - ti - t[yellow]u - í[reset] - da [Paroxítona com hiato] // [yellow]vân[reset] - da - los :: Proparoxítona // sub - ter - [yellow]fú[reset] - g[blue]io[reset]s :: paroxítona terminada em ditongo. [bg_green]CORRETA[reset]
d) protegê-los - vivê-las - estará: pro - te - [yellow]gê[reset] - los // vi - [yellow]vê[reset]-las // es - ta  - [yellow]rá[reset]
e) cidadãos - situação - estarão: Nenhuma das palavras são acentuadas, o til (~) é um sinal de nasalização.

039. (CESPE/INMETRO/CARGOS DE NÍVEL MÉDIO/2010) A palavra “últimos” recebe acento gráfico por ser proparoxítona. Também é acentuada em decorrência da mesma regra a palavra:

a) saúde [red] Recebe acentuação gráfica por outros motivos, por ser proveniente de hiato [reset]
b) confiáveis [red] con - fi - á - veis :: Hiato [reset] 
c) relevância [red] re - le - vân - cia :: paroxítona terminada em ditongo. [reset]
d) irreversível [red] ir - re - ver - sí - vel ::  Paroxítona terminada em 'el'[reset]
e) técnicas [red] téc[reset] -  ni - cas :: Proparoxítona[bg_green]CORRETO[reset]

040. (CESPE/TJ-RR/AUXILIAR ADMINISTRATIVO/2006) Assinale a opção em que as palavras apresentadas são acentuadas com base em diferentes regras gramaticais.

a) 'preparatória' e 'judiciário': pre - pa - ra - [yellow]tó[reset] - r[yellow]ia[reset] :: Paroxítona terminada em ditongo. // ju - di - [yellow]ciá[reset] - rio:  Paroxítona terminada em ditongo.
b) 'cúpula' e 'ética': [yellow]cú[reset] - pu - la  Proparoxítona e '[yellow]é[reset] - ti - ca' :: Proparoxítona
c) 'código' e 'eletrônica': [yellow]có[reset] - di - go Proparoxítona e 'e - le - [yellow]trô[reset] - ni - ca':: Proparoxítona
d) 'países' e 'critério': pa - [yellow]í[reset] - ses Hiato // cri - [yellow]té[reset] - r[blue]io[reset] :: Paroxítona terminada em ditongo.

041.(QUADRIX/PRODAM-AM/ASSISTENTE/2022) Justifica-se com base na mesma regra de acentuação o emprego do acento nas palavras:

a) 'já' e 'é': [bg_green]São baseadas na mesma regra de acentuação[reset]
b) 'despertá-la' e 'imóvel': des - per - [yellow]tá[reset]-la :: Oxítona e i - [yellow]mó[reset] - vel :: Paroxítona terminada em 'el' [red]Regras diferentes´[reset]
c) 'trêmulas' e 'vê' : [yellow]trê[reset] - mu - las :: Proparoxítonas e vê monossílaba tônica. [red] Regras totalmente diferentes[reset]
d) 'tédio' e 'há': [yellow]té[reset] - d[green]io[reset] :: Paroxítona terminada em ditongo e 'há' monossílaba tônica, [red]regras totalmente diferentes[reset]
e) 'céu' e 'também': [blue]Céu[reset] Ditongo aberto para acentuação que continua e tam - [yellow]bém[reset] oxítona para 3º pessoa do singular.

042. (QUADRIX/CRBIO-6ª REGIÃO/AUXILIAR DE SERVIÇOS GERAIS/2021) Justifica-se, com base na mesma regra de acentuação, o emprego do acento nas palavras :

a) 'mamíferos' e 'climáticas' 
ma - [yellow]mí[reset] - fe - ros [blue][Proparoxítona][reset] e cli - [yellow]má[reset] - ti - cas :: Proparoxítona [bg_green]CORRETO[reset]
b) 'ciências' e 'só':
ci - [yellow]ên[reset] - cias :: Paroxítona e 'só' monossílaba tônica, [red]regras diferentes[reset]
c) 'também' e 'têm':
Oxítona dissílaba com acento diferencial e 'têm' monossílaba também usado como acento diferencial, portanto possuem a mesma regra.
d) 'zoólogo' e 'notável':
[yellow]zoó[reset] - lo - go ::  Proparoxítona // 'no - [yellow]tá[reset] - vel' :: Paroxítona terminada em 'el'. [red] Regras diferentes[reset]
e) 'únicos'  e 'você':
[yellow]ú[reset] - ni - cos // Proparoxítona e 'você' oxítona, portanto [red] regras diferentes[reset]

043. (QUADRIX/CRBIO-6ª REGIÃO/AUXILIAR DE SERVIÇOS GERAIS/2021) Assinale a alternativa que apresenta uma palavra do texto que obrigatoriamente deve ser acentuada, por
ser proparoxítona.

a) água [red] Não é proparoxítona e sim paroxítona.[reset]
b) constituída - cons - ti - t[yellow]u - í[reset] - da :: paroxítona com hiato
c) móveis :  [yellow]mó[reset] - veis :: Paroxítona terminada em ditongo 
d) vítimas : [yellow]ví[reset] - ti - mas :: [blue]Proparoxítona[reset] [bg_green]CORRETA.[reset].
e) até : a - [yellow]té[reset] [blue]Oxítona[reset]

044. (QUADRIX/CRP-MG/ASSISTENTE ADMINISTRATIVO/2021) Assinale a alternativa em que as palavras destacadas do texto são acentuadas graficamente de acordo com a mesma
regra de acentuação gráfica.

a) fórum, coronavírus, ciêntíficos:
[yellow]fó[reset] - rum :: Paroxítona ; co - ro - na - [yellow]ví[reset] - rus :: Paroxítona ; ci - ên - [yellow]tí[reset] - fi - cos :: Proparoxítona

b) distúrbios, área, agência:
dis - [yellow]túr[reset] - bios :: Paroxítona terminada em ditongo ; [yellow]á[reset] - r[green]ea[reset] :: Paroxítona terminada em ditongo ; a - [yellow]gên[reset] - c[green]ia[reset] :: paroxítona terminada em ditongo. [bg_green]CORRETO[reset] 

c) destruídas, famílias, início:
des - tr[yellow]u - í[reset] - das [blue]Paroxítona com hiato[reset]; fa - [yellow]mí[reset] - l[green]ia[reset]s ::  Paroxítona terminada em ditongo.// i - [yellow]ní[reset] - c[green]io[reset] :: paroxítona terminada em ditongo

d) saúde, último, número:
s[yellow]a - ú[reset] - de :: Paroxítona com hiato //  [yellow]úl[reset] -  ti - mo :: Proparoxítona // [yellow]nú[reset] - me - ro // Proparoxítona

e) têm, também, há:
têm - acento diferencial usado em verbos mantidos //  tam - [yellow]bém[reset] :: Oxítona dissilaba // há - monossílaba tônica

045. (QUADRIX/CRMV-MT/ASSISTENTE ADMINISTRATIVO/2016) A palavra “está” é acentuada:

a) para diferenciar de 'esta' [red]Trata-se de uma oxítona[reset]
b) para se ter certeza de que se trata de um pronome[red] Não, trata-se de um verbo [reset]
c) por ser monossílaba[red]Não é[reset]
d) porque é uma oxítona terminada em 'a'.[bg_green]CORRETO[reset]
e) porque todas as proparoxítonas o são [red] Não é proparoxítona[reset]

046. (QUADRIX/SESC-DF/CIRURGIÃO DENTISTA/2018) São acentuadas graficamente de acordo com a mesma regra de acentuação gráfica as palavras:

a) magnéticas, ressonâncias, órgãos:
mag - [yellow]né[reset] - ti - cas :: Proparoxítona //  res - so - [yellow]nân[reset] - cias :: Paroxítona terminada em ditongo // [yellow]ór[reset] - gãos :: paroxítona terminada em ditongo
b) vêm, têm, nós:
acento diferencial, acento diferencial e monossílaba ditongo aberto
c) mandíbula, concluída, construídos:
man - [yellow]dí[reset] - bu - la ::  Proparoxítona // con - cl[yellow]u - í[reset] - da :: Paroxítona com hiato // cons - tr[yellow]u - í[reset] - dos :: Paroxítona com hiato
d) cópias, terapêuticas, construídos:
[yellow]có[reset] - p[green]ia[reset]s :: Paroxítona terminada com ditongo // te - ra - [yellow]pêu[reset] - ti - cas :: Proparoxítona // cons - tr[yellow]u - í[reset] - dos :: Paroxítona com hiato
e) porém, precisará, está:
po - [yellow]rém[reset] Oxítona // pre - ci - sa - [yellow]rá[reset] :: Oxítona // es - [yellow]tá[reset] :: [blue]Oxítona[reset][bg_green]CORRETO[reset]

[bg_red] Lembrando que segundo a gramática tradicional normativa, receberão acento as oxítonas terminadas em A, E, O, EM seguidas ou não de S.[reset]

047. (QUADRIX/SESC-DF/MOTORISTA/2018) São acentuadas graficamente de acordo com a mesma regra de acentuação gráfica as palavras:

a) ecológico e sustentável:
eco - [yellow]ló[reset] - gi - co :: Proparoxítona //  sus - ten - [yellow]tá[reset] - vel :: Paroxítona terminada em 'el' 
b) patrimônio e além:
pa - tri - [yellow]mô[reset] - nio :: paroxítona terminada em ditongo // a - [yellow]lém[reset] :: Oxítona 
c) espécies e também:
es - [yellow]pé[reset] - c[green]ie[reset]s :: paroxítona terminada em ditongo //  tam - [yellow]bém[reset] - Oxítona 
d) País e Poconé:
p[yelow]a - í[reset]s - Oxítona com hiato // po - co - [yellow]né[reset] - Oxítona
e) está e Poconé:
es - [yellow]tá[reset] - [blue]Oxítona // po - co - [yellow]né[reset] :: Oxítona [bg_green]CORRETA[reset] [blue]São acentuadas pela mesma regra[reset]

048. (QUADRIX/CFP/2015) Quanto à palavra “experiências”, assinale a alternativa que contenha somente palavras do texto acentuadas pelo mesmo motivo:

ex - pe - ri - [yellow]ên[reset] - c[green]ia[reset]s = [blue]paroxítona terminada em ditongo[reset]

a) Ciência, responsáveis, parâmetros:
ci - [yellow]ên[reset] - c[green]ia[reset] - [blue]Paroxítona terminada em ditongo[reset]
res - pon - [yellow]sá[reset] - v[green]ei[reset]s - [blue] Paroxítona terminada em ditongo[reset] 
pa - [yellow]râ[reset] - me - tro // [blue] Proparoxítona[reset]

b)Equívocos, científico, responsáveis:
e - [yellow]qui[reset] - vo - cos // Proparoxítona
ci - en - [yellow]tí[reset] - fi - cos // Proparoxítona
res - pon - [yellow]sá[reset] - v[green]ei[reset]s // Paroxítona terminada em ditongo

c) Área, histórias, ciência:
[yellow]á[reset] - r[green]ea[reset] // Paroxítona terminada em ditongo
his - [yellow]tó[reset] - r[green]ia[reset] // paroxítona terminada em ditongo
ci - [yellow]ên[reset] - c[green]ia[reset] // paroxítona terminada em ditongo

[bg_green] ALTERNATIVA C, CORRETA.[reset]

d) fértil, incluíram, ruídos
[yellow]fér[reset] - til // Paroxítona
in - cl[yellow]u - í[reset] - ram // Paroxítona com hiato
r[yellow]u - í[reset] - dos // Paroxítona com hiato

e)Confiáveis, ciência, dramática
con - f[yellow]i - á[reset] - v[green]eis[reset] // Paroxítona terminada em ditongo
ci - [yellow]ên[reset] - c[green]ia[reset] // Paroxítona terminada em ditongo
dra - [yellow]má[reset] - ti - ca // Proparoxítona

049. (QUADRIX/PREFEITURA DE JATAÍ GO/PSICÓLOGO/2019) São acentuados graficamente de acordo com a mesma regra de acentuação gráfica os vocábulos:

a) vêm, é, também: [red] ERRADO [reset]
b) áreas, território, ocorrências:
[yellow]á[reset] - r[green]ea[reset]s // Paroxítona terminada em ditongo
ter - ri - [yellow]tó[reset] - r[green]io [reset] // Paroxítona terminada em ditongo
o - cor - [yellow]rên[reset] - c[green]ias[reset] // Paroxítona terminada em ditongo

c) eficácia, imprescindível, urbanística:
e - fi - [yellow]cá[reset] - c[yellow]ia[reset] // Paroxítona terminada em ditongo
im - pres - cin - [yellow]dí[reset] - vel // Paroxítona 
ur - ba - [yellow]nís[reset] - ti - ca // Proparoxítona

d) saúde, distribuídos, viária
s[yellow]a - ú[reset] - de // Paroxítona com hiato
dis - tri - b[yellow]u - í[reset] - dos // paroxítona com hiato
v[yellow]i - á[reset] - r[green]ia[reset] // Paroxítona terminada em ditongo

e) crítico, distribuídos,fundiária
[yellow]crí[reset] - ti - co // Proparoxítona
dis - tri - b[yellow]u - í[reset] - dos // paroxítona com hiato
fun - d[yellow]i - á[reset] - r[green]ia[reset] // Paroxítona com hiato

[bg_green] Alternativa B [reset]

050.(QUADRIX/PREFEITURA DE CRISTALINA GO/RECEPCIONISTA/2019) Assinale a alternativa que apresenta uma palavra acentuada pelo mesmo motivo que é acentuado o
vocábulo “sustentável”.

[red]Sustentável : sus - ten - tá - vel[reset][blue]Paroxítona[reset]

a) estará - [red]Oxítona[reset]
b) disponível - [bg_green]Paroxítona[reset]
c) econômico - [red] Proparoxítona [reset]
d) fábricas - [red] Proparoxítona [reset]
e) máximo - [red] Proparoxítona [reset]

051.(CONSULPLAN/CODEVASF/TÉCNICO EM DESENVOLVIMENTO REGIONAL/ENFERMAGEM DO TRABALHO/2008) As palavras [bg_green]há, preparatórios e títulos [reset] são acentuadas da
mesma razão que, respectivamente:

[red] há = monossílabo tônico[reset]
[red] preparotório = Paroxítona terminada em ditongo[reset]
[red] títulos = Proparoxítonas[reset]
 
a) família, só, harém:

fa - [yellow]mí[reset] - l[green]ia[reset] // Paroxítona terminada em ditongo
só - Monossílaba tônica
harém - Oxítona

b) só, aparências, simpática:
só - monossílaba tônica
a - pa - r[yellow]ên[reset] - c[green]ia[reset]s // Paroxítona terminada em ditongo
sim - [yellow]pá[reset] - ti - ca // Proparoxítona // 

c) até, harém, ninguém:
a - [yellow]té[reset] // Oxítona
ha - [yellow]rém[reset] // Oxítona
nin - [yellow]guém[reset] // Oxítona

d) pó, lágrimas, existência :
pó // Monossílaba tônica
[yellow]lá[reset] - gri - mas // Proparoxítona
e - xis - [yellow]tên[reset] - c[green]ia[reset] // paroxítona terminada em ditongo

e) princípio, após, música :
prin - [yellow]cí[reset] - p[green]io[reset] // Paroxítona terminada em ditongo
a - [yellow]pós[reset] // Oxítona
[yellow]mú[reset] - si - ca // Proparoxítona

[bg_green] Alternativa B a correta [reset]

052.(CONSULPAM/PREFEITURA DE NOVA OLINDA CE/AGENTE ADMINISTRATIVO/2015)
Assinale a alternativa que indica corretamente a regra de acentuação:

a) País  - Acentuam-se as palavras oxítonas terminadas em 'i', seguido ou não de 's'. [bg_red]ERRADO -- Oxítona com hiato e vogal isolada mantem o acento [reset]
b) Séria - Acentuam-se as palavras paroxítonas terminadas em ditongo, seguido ou não de 's'. [bg_green] CORRETO [reset]
c) Praticá-la - Acentuam-se as palavras monossílabicas terminadas em 'a' , seguido ou não de 's'[bg_red] A palavra é uma oxítona[reset]
d) Judiciário - Acentuam-se as vogais tônicas dos hiatos, seguidas ou não de 's', na sílaba tônica.[bg_red] Paroxítona terminada em ditongo, se a vogal tônica fosse 'i' ou 'u' do hiato perderia o acento [reset]

053. (CONSULPAN/PREFEITURA DE NOVA OLINDA CE/PROFESSOR/PORTUGUÊS/2015)
Assinale a alternativa INCORRETA sobre a acentuação das palavras do texto:

a) A palavra 'país' é oxítona. [bg_green] lembre-se que é uma palavra oxítona pela sua tonicidade, mas pela regra de acentuação o termo é um hiato.
b) A palavra 'precário' é uma proparoxítona [bd_red] INCORRETA[reset]
c) As palavras 'tóxica', 'pública' e 'trágico' são acentuadas por serem proparoxítonas.
d) A palavra 'saúde' é acentuada pela mesma regra que 'miúdo.' [blue] Certo, ambas são palavras pela regra do hiato.[reset]

054. (CONSULPAN/PREFEITURA DE NOVA OLINDA CE/PROCURADOR/2015) Assinale a alternativa em que ambas as palavras são acentuadas devido à mesma regra gramatical:

a) Vírus = paroxítona - Espécie [bd_white]CORRETA -- Mas a primeira é terminada em 'us' e a segunda em ditongo [reset]
b) Imunodeficiência - Fotográfico [red] Regras diferentes, a primeira é paroxítona terminada em ditongo e a segunda é proparoxítona.
c) Aí - Intermediário // [red] Regras diferentes[reset]. A primeira é monossílaba e a segunda é paroxítona terminada em ditongo
d) Cânceres = Pânico  // Ambas proparoxítonas [bg_green] CORRETO[reset]

055. (CONSULPLAN/HOB/2014) Assinale a alternativa em que todas as palavras foram acentuadas pelo mesmo motivo:

a) saúde - boné - distraídas [red] Acentuadas por motivos diferentes[reset]
b) remédio - possível - fúria [bg_green] Acentuadas por serem paroxítonas[reset][red]porém a palavra 'possível' é terminada em 'el', REGRA GERAL[reset]
c) alguém - homogêneo - número [red] Acentuadas por motivos diferentes[reset]
d) músculos - diagnóstico - públicas [bg_green] Acentuadas por serem proparoxítonas[reset]

056. . (CONSULPLAN/PREFEITURA DE JUATUBA MG/AUXILIAR DE ADMINISTRAÇÃO/2015)
As palavras transcritas do texto estão, quanto à acentuação, devidamente justificadas, EXCETO:

a) último - proparoxítona
b) nós - monossílaba tônica
c) irá - oxítona terminada em 'a'
d) lágrima - paroxítona terminada em 'a' [bg_red] ERRADO -- é uma proparoxítona[reset]

057. (CONSULPLAN/PREFEITURA DE PATOS DE MINAS MG/PROFESSOR DE EDUCAÇÃO
BÁSICA/LÍNGUA PORTUGUESA/2015) Em relação à acentuação das palavras [bg_green]“você”, “elétrica”, “saída”, “artísticos”, [reset]é correto afirmar que:

a) duas delas são dissílabas [bg_red] ERRADO, somente 'você'[reset]
b) todas elas foram acentuadas pelo mesmo motivo [bg_red] Cada um tem sua regra [reset]
c) apenas uma delas é acentuadas por apresentar ditongo [bg_red] Nenhuma apresenta ditongo[reset]
d) apenas duas delas foram acentuadas pelo mesmo motivo [bg_green] Sim, CORRETO // 'elétrica' e 'artísticas' são acentuadas pela mesma regra[reset]

058. (CONSULPLAN/PREFEITURA DE PATOS DE MINAS MG/MOTORISTA VEÍCULO LEVE/2015) A palavra “psicológico”, transcrita do texto, é acentuada pelo mesmo motivo
que a seguinte palavra:
[red]psi - co - [reset][yellow]ló[reset] - gi - co = [blue]Proparoxítona[reset]

a) Saúde.[bg_red] Tônica paroxítona com hiato
b) Países.[bg_red] Tônica paroxítona com hiato
c) Vítimas.[bg_green]CORRETA[reset] [blue] Proparoxítona[reset]
d) Violência.[bg_red] Paroxítona terminada em ditongo [reset]

059. CONSULPLAN/PREFEITURA DE VENDA NOVA DO IMIGRANTE ES/PROFESSOR PB/LÍNGUA PORTUGUESA/2016) A opção que apresenta um vocábulo do texto acentuado graficamente
por razão DISTINTA das demais é:

a) Sábio. [blue]Paroxítona terminada em ditongo[reset]
b) História. [blue]Paroxítona terminada em ditongo[reset]
c) Radiância. [blue]Paroxítona terminada em ditongo[reset]
d) Construída [blue]Paroxítona com hiato [reset][bg_green] CORRETA [reset]

060. (CONSULPLAN/CÂMARA DE BELO HORIZONTE MG/TÉCNICO LEGISLATIVO II/2018) Das alternativas apresentadas, em apenas uma o uso do acento gráfico é aplicado no par
por razão distinta, nos demais a regra que justifica um uso também justifica o outro. Que alternativa é essa?

a) “há” e “é”. [bg_green] Ambos aplicados justificando o outro, monossílabos tônicos[reset]
b) “água” e “possível”. [bg_red] Paroxítona terminada em ditongo e a segunda terminada em 'el', regra geral.[reset]
c) “após” e “também”. [bg_whte] Ambos são oxítonas [reset]
d) “árida” e “inóspita”. [bg_green] Proparoxítonas terminadas em vogal[reset]

061. (CESPE/POLÍCIA MILITAR DE ALAGOAS/2018) O emprego do acento gráfico nas palavras “Dói”, “só” e “nós” justifica-se pela mesma regra de acentuação.
[bg_red] 'dói' recebe acento por ser ditongo aberto, 'sós' e 'nós' são monossílabos tônicos [reset]

062. (CESPE/BNB/2018) Os vocábulos “trás”, “é” e “nós” recebem acento gráfico em obediência à mesma regra de acentuação.
[bg_green] Ambos recebem por ser monossílabos tônicos, em que são acentuadas aqueles terminados em A, E, O seguidos ou não de S.[reset]

063. (CESPE/PC-GO/2016) Julgue: As formas verbais “torná-la” e “fazê-la” recebem acentuação gráfica porque se devem acentuar todas as formas verbais combinadas a pronome enclítico.
[bg_red] Recebem acentuação por serem oxítonas e não por terem pronomes [reset]

064. (CESPE/PC-GO/2016) Julgue: A mesma regra de acentuação justifica o emprego de acento em “à” e “é”.
[bg_red] Regras diferentes, 'à' com sinal indicativo de crase é uma regra, o 'é' è monossílabo tônico, portanto regras diferentes.[reset]

065. (CESPE/TELEBRÁS/2015) A palavra “está” recebe acento gráfico em decorrência da mesma regra que determina o emprego do acento no vocábulo “três”.
[bg_green] Não porquê está é oxítona e três é monossílaba tônica, portanto regras distintas [reset]

066. (CESPE/IBAMA/2012) As palavras “pó”, “só” e “céu” são acentuadas de acordo com a mesma regra de acentuação gráfica.
[bg_red] As palavras 'pó' e 'só' são acentuadas por terem um única sílaba tônica, já 'céu' possui ditongo aberto, por isso mantem o acento. Portanto, possuem regras diferentes;[reset]

067. (CESPE/FUB/2016) O arquiteto Oscar Niemeyer transformou as ideias em prédios. A ausência de acento agudo em “ideias” está em conformidade com as regras ortográficas vigentes.
[bg_green] CORRETO [reset] [bg_green] Lembrando que os ditongos abertos deixaram de ser acentuadas na penúltima sílaba e passaram a levar acento na última;[reset]

068. (CESPE/PRF/NÍVEL SUPERIOR/2012) As formas “patrimônio” e “polícia” são acentuadas em decorrência da mesma regra de acentuação.
[bg_green] CORRETO //  ambas são paroxítonas terminadas em ditongo [reset]

069. (CESPE/DEFENSORIA PÚBLICA DA UNIÃO/2016) Os vocábulos “caráter”, “intransferível” e “órgãos” são acentuados em decorrência da regra gramatical que classifica as palavras
paroxítonas.
[bg_green] CORRETO [reset] São acentuadas as paroxítonas terminadas em i/is, us, r, l, x,n, um/uns, ão/ãos, ã/ãs, ps, on/ons[reset]

070. (CESPE/AUDITOR DO TCU/2015) As palavras “líquida”, “público” e “órgãos” obedecem à mesma regra de acentuação gráfica.
[bg_red] órgãos é paroxítona e as demais são proparoxítonas.[reset]

071. (CESPE/FUB/2015) Os acentos gráficos das palavras “bioestatística” e “específicos” têm a mesma justificativa gramatical.
[bg_green] CORRETO -- Ambas são proparoxítonas [reset]

072. (CESPE/TRF - 1ª REGIÃO/ANALISTA/2017) O emprego de acento na palavra “memória” pode ser justificado por duas regras de acentuação distintas.
[bg_green] Pode sim, tanto como eventual proparoxítona como paroxítona[reset]

073. (CESPE/STF/ANALISTA JUDICIÁRIO/2013) O emprego do acento gráfico em “remédios” pode ser justificado com base em duas regras distintas de acentuação.
[bg_green] pode sim, tanto como eventual proparoxítona como paroxítona[reset]

074. (CESPE/SUPREMO TRIBUNAL MILITAR/2011) A regra de acentuação gráfica que justifica o emprego do acento gráfico em “aeroportuário” é a mesma que justifica o emprego do
acento em “meteorológica”
[bg_red] ERRADO - A primeira é uma paroxítona terminada em ditongo e a segunda palavra é uma proparoxítona.[reset]

075. (CESPE/PRF/AGENTE ADMINISTRATIVO/2012) As palavras “Polícia”, “Rodoviária” e “existência” recebem acento gráfico porque são paroxítonas terminadas em ditongo crescente.
[bg_green] CORRETO - Ditongo crescente porque vai da semivogal para vogal (i > a) [reset]

076. (CESPE/PGE-PE/ANA. JUDICIÁRIO DE PROCURADORIA/2019) O emprego de acento agudo nas palavras “juízo”, “extraídos” e “período” justificase pela mesma regra de acentuação gráfica
[bg_red] As duas primeiras palavras sim, pela regra do hiato.  A palavra período ( pe - rí - o - do ) é proparoxítona por regra geral.[reset]

077. (CESPE/FUB/2015) Os acentos gráficos das palavras “países” e “políticas” têm a mesma justificativa gramatical.
[bg_red] ERRADO -- Países tem a justificativa de ter a vogal 'i' ou 'u' com acentuação pela regra do hiato em paroxítonas e 'políticas' por ser proparoxítona. Portanto, regras diferentes.[reset]

078. (CESPE/PC-GO/2016) O vocábulo “período” é acentuado em razão da regra que determina que se acentuem palavras paroxítonas com vogal tônica i formadora de hiato.
[bg_red] A afirmação estaria correta se a palavra fosse paroxítona, mas ela é proparoxítona [reset]

079. (CESPE/TRT 17ª REGIÃO/TÉCNICO JUDICIÁRIO/2013) Os vocábulos “juízes” e “país” são acentuados de acordo com regras de acentuação gráfica distintas.
[bg_red] ERRADO - A primeira por ser paroxítona de hiato com vogal 'i' e a segunda também. // [reset]

080. (CESPE/MINIS. DA SAÚDE/REDAÇÃO DE TEXTOS/ADAPTADA) As palavras “veículos”, “títulos” e “fantásticas” são acentuadas de acordo com a mesma regra de acentuação gráfica.
[bg_green] Proparoxítonas acentuadas corretamente [reset]

081. (CESPE/ANTT/ADAPTADA) O emprego do acento gráfico em “política”, “veículo” e “público” deve-se à mesma regra de acentuação gráfica.
[bg_green] CORRETO - Ambas são proparoxítonas [reset]

082. (CESPE/AUFC/CONTROLE EXTERNO/2013) Julgue o seguinte item. Os vocábulos “assistência”, “potável” e “elétrica” são acentuados de acordo com a mesma regra de acentuação gráfica.
[bg_red] ERRADO [reset] \n as - sis - [yellow]tên[reset] - c[green]ia[reset] :: Paroxítona terminada em ditongo \n po - [yellow]tá[reset] - vel :: paroxítona terminada em 'el' // E - [yellow]lé[reset] - tri - ca :: Proparoxítona

083. (CESPE/CONSELHO NACIONAL DE JUSTIÇA/2013) A mesma regra de acentuação gráfica justifica o emprego de acento gráfico nas palavras “construída” e “possíveis”.
[bg_red] ERRADO [reset] - Regras diferentes // cons - tr[yellow]u - í[reset] - da : Paroxítona com hiato para justificar o acento e pos - [yellow]sí[reset] - v[green]ei[reset]s :: Paroxítona terminada em ditongo

084. (CESPE/TRT DF E TO/2013) As palavras “países”, “famílias” e “níveis” são acentuadas de acordo com a mesma regra de acentuação gráfica.
[bg_red] ERRADO [reset] - 'p[yellow]a - í[reset] - ses' recebe acentuação por hiato e as outras por terem terminações em ditongo.Portanto, regras diferentes.

085. (CESPE/DEPEN/2015) Julgue o próximo item, relativo às ideias e às estruturas linguísticas do texto. As palavras “indivíduos” e “precárias” recebem acento gráfico com base em
justificativas gramaticais diferentes.
[bg_green] CORRETO -- Ambas são paroxítonas terminadas em ditongo e recebem a mesma justificativa gramatical.[reset]
in - di - [yellow]ví[reset] - duos e pre - [yellow]cá[reset] - rias

086. (CESPE/DEPEN/2015) As palavras “Penitenciário”, “carcerária” e “Judiciário” recebem acento gráfico com base na mesma regra gramatical.
[bg_green] CORRETO - Ambas as palavras possuem o acento gráfico por terem a mesma regra gramatical, paroxítonas terminadas em ditongo.[reset]

087. (CESPE/CPRM/GEOLOGIA/2015) A ocorrência de hiato justifica o emprego do acento agudo nas vogais i e u nas palavras “construída” e “conteúdos”.
[bg_green] CORRETO [reset]

088. (CESPE/ TCE RO/2013) As palavras “providências” e “fortalecê-los” recebem acento gráfico com base em regras gramaticais diferentes.
[bg_green] CORRETO - A primeira por ser paroxítona terminada em ditongo e a segunda por ser oxítona terminada em pronome.[reset]

089. (CESPE/SUFRAMA/2014) A palavra “prejuízos” recebe acento gráfico porque todas as proparoxítonas devem ser acentuadas.
[bg_red] ERRADO - a palavra pre - j[yellow]u - í[reset] - zos é uma [blue] Paroxítona com hiato [reset]e não um proparoxítona.

090. (CESPE/CAIXA ECONÔMICA FEDERAL/MÉDICO/2014) O emprego do acento gráfico em “incluíram” e “número” justifica-se com base na mesma regra de acentuação.
[bg_red]ERRADO [reset] // in - cl[yellow]u - í[reset] - ram // Paroxítona com hiato e 'número' é proparoxítona, portanto regras diferentes.[reset]

091. (CESPE/PM-CE/2014) O emprego do acento gráfico na palavra “atrás” justifica-se com base na mesma regra que justifica o emprego do acento gráfico em “fiéis”
[bg_red]ERRADO[reset] [blue]A palavra 'atrás' é oxítona e a palavra 'fiéis' recebe acento por ter ditongo aberto.[reset]

092. (CESPE/ICMBIO/2014) A mesma regra de acentuação gráfica se aplica aos vocábulos “Brasília”, “cenário” e “próprio”.
[bg_green] As três palavras aplicam-se a mesma regra de acentuação gráfica, paroxítonas terminadas em ditongo.[reset]

093. (CESPE/AG. ADM./CADE/2014) Os vocábulos “sabíamos” e “procurávamos” recebem a mesma regra de acentuação gráfica.
[bg_green] CORRETO [reset] sa - [yellow]bí[reset] - a - mos :: Proparoxítona // pro - cu - [yellow]rá[reset] - va - mos :: Proparoxítona 

094. (CESPE/ANATEL/ADMINISTRATIVO/2014) O emprego do acento gráfico em “indústria” e “rádio” justifica-se com base na mesma regra de acentuação.
[bg_green] CORRETO [reset] [blue] Ambas são paroxítonas terminadas em ditongo[reset]

095. (CESPE/CEF/ENGENHARIA AGRONÔMICA/2014) O emprego do acento gráfico nas palavras “metálica”, “acúmulo” e “imóveis” justifica-se com base na mesma regra de acentuação. 70.
[bg_red] ERRADO [reset] - As duas primeiras são proparoxítonas. Agora a palavra 'imóveis' é paroxítona terminada em ditongo.\n
me - [yellow]tá[reset] - li - ca // a - [yellow]cú[reset] - mu - lo :: Proparoxítonas
i - [yellow]mó[reset] - v[green]ei[reset]s :: Paroxítona terminada em ditongo

096. (CESPE/POLÍCIA FEDERAL/2014) Os termos “série” e “história” acentuam-se em conformidade com a mesma regra ortográfica.
[bg_green] CORRETO [reset] [yellow]sé[reset] - r[green]ie[reset] :: Paroxítona terminada em ditongo
his - [yellow]tó[reset] - r[green]ia[reset] :: Paroxítona terminada em ditongo

097. (CESPE/ANTAQ/2014) O emprego de acento gráfico em “água”, “distância” e “primário” justifica-se pela mesma regra de acentuação.
[bg_green] CORRETO [reset] [yellow]á[reset] - g[green]ua[reset] :: Paroxítona terminada em ditongo
dis - [yellow]tân[reset] - c[green]ia[reset] :: Paroxítona terminada em ditongo
pri - [yellow]má[reset] - r[green]io[reset]  :: Paroxítona terminada em ditongo

098. (CESPE/TJ-ES/2011) Os vocábulos “analítica” e “teríamos” recebem acento gráfico com base na mesma regra de acentuação.
a - na - [yellow]lí[reset] - ti - ca
te - [yellow]rí[reset] - a - mos
[bg_green] CORRETO - Ambas são proparoxítonas[reset]

099. (CESPE/ANAC/2012) As palavras “início” e “série” recebem acento gráfico com base em regras gramaticais distintas.
i - [yellow]ní[reset] - c[green]io[reset] :: Paroxítona terminada em ditongo
[yellow]sé[reset] - r[green]ie[reset] :: Paroxítona terminada em ditongo
[bg_green] ERRADO -- Recebem acentos por terem a mesma regra gramatical[reset]

100. (CESPE/ANAC/2012) Os termos “Três” e “Vã” são acentuados em decorrência de igual justificativa gramatical.
[bg_red] ERRADO [reset] O til (~) não é acento, e sim um som nasal.
'''

    def menu(self):
        #self.print_slow_2(self.text_init())
        #self.print_slow_2(self.aviso())
        #sleep(2)
        self.print_slow('Bem vindo aos estudos da Ortografia Brasileira para concursos...')
        self.dots()
        while True:
                try:
                    indice = int(input('''
                    Estudos da Ortografia:
                                       
                    [0] - Introdução                                       
                    [1] - Oxítona
                    [2] - Proparoxítona
                    [3] - Paroxítona
                    [4] - Acentuação
                    [5] - Regras Especiais
                    [6] - Uso do Hífen - Prefixos + Radical
                    [7] - Uso do Hífen - Radicais 
                    [8] - Questões de Hífen    
                    [9] - Escrita - Letra S 
                    [10]- Escrita - Letra G
                    [11]- Escrita - Letra X  
                    [12]- Palavras com Formas Variantes   
                    [13]- Abreviações  
                    [14]- Siglas  
                    [15]- Emprego de inicais maiúsculas 
                    [16]- Trema   
                    [17]- Uso do Hífen - Versão Prof. Gustavo Silva    
                    [18]- Acentuação Gráfica - Professor Gustavo Silva   
                    [19]- Separação silábica - Professor Elias Santana          
                    [20] - Questões de concurso - Acentuação Gráfica                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                    [21]- Sair
                                       
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
                        self.print_slow_2(self.hifen())
                        self.dots()  
                        sleep(1)    
                    elif indice == 7:
                        self.print_slow_2(self.hifen_2())
                        self.dots()
                        sleep(1)    
                    elif indice == 8:
                        self.print_slow_2(self.hifen_questoes())
                        sleep(1)
                        self.dots()  
                    elif indice == 9:
                        self.print_slow_2(self.escrita_word_s())   
                        self.dots()                                                                                                                            
                        sleep(1)
                    elif indice == 10:
                        self.print_slow_2(self.escrita_word_g())
                        self.dots()
                        sleep(1)     
                    elif indice == 11:
                        self.print_slow_2(self.escrita_word_x())
                        sleep(1)
                        self.dots()
                        sleep(1)     
                    elif indice == 12:
                        self.print_slow_2(self.palavra_variacao())                                                              
                        sleep(1)
                        self.dots()
                        sleep(1)
                    elif indice == 13:
                        self.print_slow_2(self.abreviacoes())
                        sleep(1)
                        self.dots()
                        sleep(1)     
                    elif indice == 14:
                        self.print_slow_2(self.siglas())
                        sleep(1)
                        self.dots()
                        sleep(1)     
                    elif indice == 15:
                        self.print_slow_2(self.inicias_maiusculas())
                        sleep(1)
                        self.dots()
                        sleep(1)     
                    elif indice == 16:
                        self.print_slow_2(self.trema())
                        sleep(1)
                        self.dots()
                        sleep(1)     
                    elif indice == 17:
                        self.print_slow_2(self.uso_do_hifen())   
                        self.dots()
                        sleep(1)                                                                                                 
                    elif indice == 18:
                        self.print_slow_2(self.acentuacao_grafica())
                        self.dots()
                        sleep(1)
                    elif indice == 19:
                        self.print_slow_2(self.separacao_silabica_2())                        
                        self.dots()
                        sleep(1)
                    elif indice == 20:
                        self.print_slow_2(self.questoes_concurso())
                        self.dots()
                        sleep(1)                        
                    elif indice == 21:
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
[yellow]A(s),E(s),O(s),EM(ns)[reset] - Ex: Paraná [bg_green]Termina com 'a'[reset], Café-Cafés[bg_green] Termina com 'e(s)'[reset], Mocotó - [bg_green]Termina com 'o',[reset] Armazém - [bg_green]Termina com 'm' e pode terminar com 'ens'[reset]
        '''
    def regras_especiais_2(self):

        return '''A maior parte das palavras da língua portuguesa são as [red]Paroxítonas.[reset] [bg_yellow]Não são acentuadas[reset] as palavras que possuem as terminações:
[yellow]A(s),E(s),O(s),EM(ns)[reset] -[blue]Parte do pressuposto das terminações ter uma consoante anterior. [reset]
Ex - Mesa / [bg_green]Me[reset] -  sa / Parede / pa - [bg_green]re[reset] - de / Quadro / [bg_green]Qua[reset] - dro - Item / [bg_green]I[reset] - tem           
[bg_red]*** Eu vou acentuar as paroxítonas que não terminam com A(s),E(s),O(s),EM(ns)[reset] -  Ex: Ca - [bg_green]rá[reset] - ter / [bg_green]Tá[reset] -  xi / [bg_green]Hí[reset] - fen, A - [bg_green]má[reset] - vel, [bg_green]Â[reset] - nus, [bg_green]Tó[reset] - rax, 
[bg_green]bí[reset] - ceps, [bg_green]ÁL[reset] - bum, [bg_green]ÓR[reset] - fã ***'''   

    def aviso_paroxitona_especial(self):
        
        return '''[bg_red]Paroxítonas terminadas em DITONGO : QUANDO DUAS VOGAIS SE JUNTAM SILABICAMENTE , a palavra é ACENTUADA![reset]
Ex: A palavra 'necessário' = Quando duas vogais se juntam ocorre o fenômeno DITONGO terminada em 'io'. ne - ces - [bg_green]sá[reset] - r[bg_green]io[reset] - [blue]Terminada em ditong, por isso é acentuada.        '''

    def separacao_silabica(self):
        return '''Na separação silábica das [red]paroxítonas[reset] onde a tônica é a penúltima sílaba, além de ocorrer o fenômeno do [red]Ditongo[reset] para acentua-las.
Pode ocorrer outro caso em que a palavra paroxítona pode se tornar uma eventual [red]proparoxítona[reset]: [blue]Uma separação silábica diferente da clássica.[reset]
Na separação silábica moderna , [bg_green]separando o ditongo da separação clássica alterando a sílaba tônica para a antepenúltima se tornando uma eventual proparoxítona.[reset] '''

    def sep_si_exemplo(self):

        return '''\nATENÇÃO!\n 
Mesário -->  [bg_green]Separação clássica:[reset] me - [bg_green]sá[reset] - rio     ou 	Separação alternativa: me - [bg_green]sá[reset] - ri - [bg_green]o[reset] : Separando o ditongo da separação clássica, alterando a ordem da sílaba tônica. Isolando a vogal. Deixando de ser a penúltima sílaba tônica(paroxítona) e sendo (antepenúltima) uma eventual proparoxítona.
Série ---->  [bg_green]Separação clássica:[reset] [bg_green]sé[reset] - rie    	     ou	    Separação alternativa: [bg_green]sé[reset] - ri - [bg_green]e[reset]    : Separando o ditongo da separação clássica, alterando a ordem da sílaba tônica. Isolando a vogal. Deixando de ser a penúltima sílaba tônica(paroxítona) e sendo (antepenúltima) uma eventual proparoxítona.
Bactéria ->  [bg_green]Separação clássica:[reset] bac - [bg_green]té[reset] - ria 	 ou	    Separação alternativa: bac - [bg_green]té[reset] - ri - [bg_green]a[reset]: Separando o ditongo da separação clássica, aletrando a ordem da sílaba tônica. Isolando a vogal. Deixando de ser a penúltima sílaba tônica(paroxítona) e sendo (antepenúltima) uma eventual proparoxítona.
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
        
        return '''[red]Oxítona:[reset]\n[blue]Palavras que quando a sílaba tônica é a última:[reset] -->[bg_blue]Além[reset] ->  A -[bg_green]lém[reset] /  [bg_blue]Parati[reset] -> pa - ra - [bg_green]ti[reset] /   [bg_blue]País[reset] -> Pa - [bg_green]ís[reset] '''

    def Paroxitona(self):
        return '''[red]Paroxítona:[reset]\n[blue]Quando a sílaba tônica é a penúltima:[reset] --> [bg_blue]Mesa[reset] ->[bg_green] me[reset] - sa /[bg_blue]Responsável[reset] -> res-pon-[bg_green]sá[reset]-vel /[bg_blue]Saúde[reset] -> Sa -[bg_green]ú[reset]- de'''    
    
    def Proparoxitona(self):
        return '''[red]Proparoxítona:[reset]\nQuando a sílaba tônica é a antepenúltima : [bg_blue]Exército[reset] -> E - [bg_green]xér[reset] - ci - to 
[bg_red]\nSendo a sílaba tônica a antepenúltima, toda proparoxítona será acentuada.[reset]- [bg_yellow]LÂM[reset] PADA / LU - [bg_yellow]NÁ[reset] - TICA[reset]       '''


if __name__=='__main__':
        
    ortografia = Ortografia()
    ortografia.menu()
