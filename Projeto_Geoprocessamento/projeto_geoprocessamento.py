# Versão 01
from colorama import Fore, Style, Back, init
from time import sleep
import sys
import keyboard

class geoprocessamento:     
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

        # Pré-processa as linhas para melhor controle:
        lines = []
        current_line = ''
        i = 0
        while i < len(text):
            if text[i] == '[':
                end_index = text.find(']', i + 1)
                if end_index != -1 and text[i+1:end_index] in color_codes:
                    current_line += text[i:end_index + 1]
                    i = end_index + 1
                    continue
            current_line += text[i]
            if text[i] == '\n':
                lines.append(current_line)
                current_line = ''
            i += 1
        if current_line:
            lines.append(current_line)

        current_index = 0
        paused = False
        speed = 0.06  
        rewind_requested = False                                                                                    
        
        def toggle_pause():
            nonlocal paused
            paused = not paused

        def go_back():
            nonlocal current_index, rewind_requested
            if current_index > 0:
                current_index -= 1
                rewind_requested = True  # Sinaliza para interromper a linha atual
                sys.stdout.write("\033[F")  # Move o cursor para a linha anterior
                sys.stdout.write("\033[K")  # Limpa a linha
                sys.stdout.flush()

        def increase_speed():
            nonlocal speed
            speed = max(0.005, speed - 0.01)

        def decrease_speed():
            nonlocal speed
            speed += 0.01

                                        
        keyboard.on_press_key("space", lambda _: toggle_pause())
        keyboard.on_press_key("left", lambda _: go_back())    
        keyboard.on_press_key("+", lambda _: increase_speed())    
        keyboard.on_press_key("-", lambda _: decrease_speed())

        while current_index < len(lines):
            line = lines[current_index]
            i = 0
            current_color = ''
            rewind_requested = False # Reseta o sinal de retorno antes de começar
            while i < len(line):
                    if paused:
                        sleep(0.1)
                        continue
                    if rewind_requested:
                        break # Interrompe a linha se voltar foi pedido

                    if line[i] == '[':
                        end_index = line.find(']', i + 1)
                        if end_index != -1:
                            color_code = line[i + 1:end_index]
                            if color_code in color_codes:
                                current_color = color_codes[color_code]
                                i = end_index + 1
                                continue
                    sys.stdout.write(current_color + line[i])
                    sys.stdout.flush()
                    sleep(speed)
                    i += 1
            if not rewind_requested:
                current_index += 1  # Só avança se não foi pedido para voltar

        print(Style.RESET_ALL)
        
    def cartografia(self):
        return '''
            [blue]Aqui vai o conteúdo dos exercícios 1.[reset]
Cartografia faz parte da ciência geográfica.
'carto' -> Mapas / 'grafia' -> Escrita
Cartografia é a ciência, técnica e arte de representar graficamente a superfície terrestre (total ou parcial) em documentos cartográficos, como mapas, cartas e plantas.
Seu objetivo é transformar a realidade tridimensional da Terra em representações bidimensionais, com precisão, clareza e finalidade específica.
A forma real é geoide. O termo elipsoide também é chamado, para permitir os cálculos matemáticos.
Em outras formas é transformar o mapa 3D em 2D. Todo mapa é distorção da realidade. 
A Cartografia envolve a coleta, análise, interpretação e representação de dados geográficos para produzir mapas precisos e compreensíveis.
Além de representarr a geografia física, a cartografia também pode incluir informações sociais, econômicas e culturais, fornecendo uma visão abrangente de uma determinada área.

Pontos Cardeais

Os pontos cardeiais são as quatro principais direções de referência utilizadas na cartografia e na navegação: Norte, Sul, Leste e Oeste.
Eles são as principais direções que usamos para nos guiar em um mapa. Eles nos ajudam a entender onde estamos e a encontrar os diferentes lugares no mapa.
Existem os colaterias e os subcolaterias, cuidado para não confundir.

Existem diferentes formas de reprersentar os pontos cardeais. Podem variar dependendo do tipo de mapa ou contexto em que estão sendo usados. No entanto,
existem algumas convenções comuns, além das rosas do ventos, como por:

Por setas: uma forma comum de representar os pontos cardeais. O norte é geralmente representado por uma seta que aponta para cima, o Sul por uma seta para baixo.
O Leste é uma seta que aponta para a direita e o Oeste por uma seta que aponta para a esquerda.

Por Letras: Outra forma de representar os pontos cardeais é por meio de letras. O Norte é frequentemente indicado pela letra 'N', o SUL pela letra 'S'.
O "Leste" pela letra E(do inglês "East") e o "Oeste" pela letra "W"( do inglês 'WEST' )

Por linhas direcionais: Em alguns mapas, os pontos cardeais são representados por linhas direncionais em forma que assemelha com um sinal positivo. (MAIS)
A linha horizontal da esquerda pra direita representa as direções WEST a EAST e a linha vertical representa, de cima a baixo, o North a South.
ORIGEM dos pontos cardeais:

	Os pontos cardeais são determinados pela posição do sol em relação à Terra. Porque o sol é uma fonte natural de luz e fornece uma referência confiável
para a orientação espacial.

	O Leste (EAST):  é o lado onde o Sol nasce no horizonte pela manhã indica o Leste, com o braço direito stendido em sua direção.
	O OESTE (WEST):  o lado onde o sol se põe no horizonte indica o oeste.
	O Norte (NORTH): o lado que fica a sua frente ao estender o braço direito na direção do nascer do Sol.
	O Sul (South):   o lado em que fica em suas costas ao estender o braço direito na direção em que o Sol nasce.

Outras denominações importantes:

Além das designações convencionais: Norte, Sul, Leste e Oeste, existem outras de relevância que também são utilizadas para representar esses pontos de referência.

SETENTRIONAL: o termo 'setentrional' é frequentemente usado para designar o ponto cardeal Norte. A palavra deriva do latim 'septentrionalis', que significa "NORTE".
Ou "aquilo que está voltado para o Norte." Refere-se à região do céu onde a Estrela Polar (POLARIS) está localizada, indicando a direção norte.

MERIDIONAL: o nome 'meridional' é utilizado para representar o ponto cardeal "SUL". A palavra deriva-se do latim "meridies", que significa "meio-dia" ou "aquilo que
está voltado para o sul". Onde o Sol está no ponto mais alto duranta o dia.

ORIENTAL: o termo 'oriental' deriva do latim 'oriens' que significa 'nascente' ou 'aquilo que está voltado para o nascente', referindo-se a direção em que o Sol nasce
(LESTE)

OCIDENTAL: Já o termo 'ocidental' deriva do latim 'occidens' que significa 'poente' ou 'aquilo que está voltado para o poente', referindo-se à direção em que o Sol
se põe (OESTE)

PONTOS COLATERAIS E SUBCOLATERAIS

	-> Além dos pontos cardeais (norte, sul, leste e oeste) existem os pontos colaterais e subcolaterais que fornecem direções intermediárias
entre os pontos principais. Os pontos colaterais são frequentemente utilizados para indicar direções mais precisas em um mapa ou durante uma navegação.
São eles:

	Nordeste(NE): Localizado entre o Norte e o Leste, o Nordeste é uma direção intermediária que combina elementos do Norte e do Leste.
	SUDESTE(SE): Situado entre o Sul e o Leste, o Sudeste representa uma direção que mescla elemento do Sul e do Leste.
	Sudoeste(SO): Encontrado entre o Sul e o Oeste, o Sudoeste é uma direção intermediária que combina características do Sul e do Oeste.
	Noroeste (NO): Localizado entre o Norte e o Oeste. O Noroeste representa uma direção que combina elementos do Norte e o Oeste.

PONTOS SUBCOLATERAIS

	Além dos pontos colaterais, temos os pontos subcolaterais, que são são direções intermediárias adicionais entre os pontos colaterais. Eles são:

	Norte-Nordeste (NNE): Fica entre o Norte e o Nordeste.
	Leste-Nordeste (ENE): Fica entre o Leste e o Nordeste. ( Diagonal direita acima )
	Leste- Sudeste (ESE): Fica entre o Leste e o Sudeste. (Diagonal direita abaixo)
	Sul-Sudeste (SSE): Encontra-se entre o Sul e o Sudeste.
	Sul-Sudoeste(SSW): Fica entre o Sul e o Sudoeste. 
	Oeste-Sudoeste(WSW): Situa-se entre o Oeste e o Sudoeste. ( Diagonal esquerda abaixo )
	Oeste-Noroeste(WNW): Situa-se entre o Oeste e o Noroeste. ( Diagonal esquerda acima )
	Norte-Noroeste(NNW): Fica entre o Norte e o Noroeste.

Em resumo, os pontos colaterais fornecem direções intermediárias entre os pontos cardeais, permitindo uma orientação mais precisa.
Já os pontos subcolaterais oferecem direções adicionais e ainda mais detalhadas entre os pontos colaterais. Esses conceitos são úteis para descrever
com mais precisão em um mapa ou durante a navegação.

ROSA DOS VENTOS

A Rosa dos ventos é um elemento gráfico que representa a direção e a orientação em um mapa. Ela é representação circular que mostra os pontos cardeais
os pontos colaterais e o pontos subcolaterais. Ela é usada como uma ferramenta de referência para ajudar na orientação e navegação em um mapa. Ela permite
que você identifique rapidamente a direção em relação aos pontos cardeais, o que é essencial para traçar rotas, encontrar destinos e se deslocar com segurança.

            '''

    def exercicios_cart(self):
        return '''
            [blue]Aqui vai o conteúdo dos exercícios 1.[reset]
 Q1. Qual das seguintes afirmações está de acordo com o conceito de cartografia e a importância do estudos mapas?

a. A cartografia é o estudo dos fósseis e sua relação com a história da Terra.
b. O uso de mapas é restrito à geografia física e não tem relevância em outros campos.
c. A cartografia é uma ferramenta que permite analisar dados geográficos e obter insights sobre fenômenos que afetam a sociadade.
d. O estudo dos mapas é irrelevante na era digital, onde todas as informações estão disponíveis online.
e. A cartografia é útil apanas para fins estéticos e decorativos.

a. ERRADO. Não é essa a grande característica da cartografia.
b. ERRADO. Pelo contrário, em vários campos inclusive na medicina.
c. CORRETO. 
d. ERRADO. Alternativa muito restrita, temos diversos aplicativos e softawares como o WAZE que usam mapas e localização para diversos fins.
e. ERRADO. Não mesmo, para diversos fins.

Q2. (CESGRANRIO-2023/IBGE) No espaço aéreo brasileiro, uma aeronave se desloca, em linha reta, de Palmas, no Tocantins, para Brasília, no Distrito Federal.
De acordo com os pontos cadeais, essa aeronave descreve uma trajetória no sentido:

a. sul/norte
b. leste/oeste
c. norte/sul
d. nordeste/sudoeste
e. sudoeste/nordeste

Palmas está no NORTE e vai pro SUL, alternativa 'C'.

Q3. (CEPERJ-2015-SEDUC-RJ) Se os alunos observarem diariamente o nascer e o pôr do sol, perceberão a regularidade dos pontos de nascente e poente ficará
fácil a determinação dos pontos cardeais usando a seguinte convenção:

a. O norte é definido como o ponto à frente de quem, com os braços estendidos, aponta o Leste com a mão direita e o Oeste com a mão esquerda, ficando o Sul
às suas costas.
b. O Sul é definido como o ponto à frente de quem, com os braços estendidos, aponta o Leste com a mão direita e o Oeste com a mão esquerda, ficando o Norte às
suas costas.
c. O Norte é definido como o ponto à frente de quem, com os braços estendidos, aponta o Oeste com a mão direita e o Leste com a mão esquerda, ficando o Norte
às suas costas.
d. O Leste é definido como o ponto á frente de quem, com os braços estendidos, aponta o Sul com a mão direita e o Norte com a mão esquerda, ficando o Oeste às
suas costas.
e. O Oeste é definido como o ponto à frente de quem, com os braços estendidos, aponta o Norte com a mão direita e o Sul com a mão esquerda, ficando o Leste às
suas costas.


Resolução da questão.

a. Alternativa A a correta. O Norte é definido como o ponto à frente de quem, com os braços estendidos, aponta com a mão direita para o Leste e a mão esquerda ao OESTE.
Ficando o Sul pelas costas.
b. INCORRETO. O Sul não é definido ficando o Norte às suas costas e sim o Sul pelas Costas. As direções do Leste com a mão direita e o Oeste com a mão esquerda estão corretas.
Inclusive, a mão estendida para o Leste é onde nasce o Sol no horizonte pela manhã.
c. INCORRETO. O Norte é definido como o ponto à frente de quem, com os braços estendidos, aponta o Oeste com a mão ESQUERDA e não com a direita. E o Leste com a mão direita
e não com a ESQUERDA.
d. INCORRETO. O LESTE não é definido como o ponto à frente de nada. O Sul não apontamos com a mão direira e nem o Norte com a mão esquerda. Nem muito menos o Oeste
as nossas costas. O Leste é definido onde o Sol nasce no horizonte pela manhã, com o braço direito estendido em sua direção. O Oeste é definido onde o Sol se põe no 
horizonte. Que por sua vez, o Norte é definido como o ponto à frente e o Sul as suas costas.
e. INCORRETO. O Oeste é definido onde o Sol se põe no horizonte e com o braço direito estendido para a diração onde o Sol nasce no horizonte pela manhã.

Q4.(MPE-GO-2018) Os pontos cardeais são pontos de orientação no espaço terrestre determinados pela posição do sol. Sententrional e Meridional
são denominações que também são utilizadas para designar:

a. Norte e Sul
b. Leste e Oeste
c. Norte e Leste
d. Sul e Oeste
e. Sudeste e Noroeste.

CORRETA, respectivamente, a alternativa 'A'.

Q5. (CEBRASPE-2021/IBGE)

A figura nos mostra uma rosa dos ventos. Assinale a opção correta, a respeito desse tipo de representação:

a. Comumente utilizada durante as grandes navegações (séculos XIV ao XIX), a rosa dos ventos tornou-se uma representação obsoleta na atualidade, já que os sistema
de GPS utilizam informações referenciadas por setélite
b. A rosa dos ventos surgiu da necessidade de se indicar a escala dos mapas geográficos.
c. A rosa dos ventos é formada pelos pontos cardeais (norte, sul, leste, oeste) e pelos subcolaterais(nordeste,sudeste, noroeste,sudoeste)
d. A rosa dos ventos indica os pontos cardeais definidos a partir do nascer-do-sol (oeste) e pôr-do-sol(leste) e as localizações ocidental(norte) e oriental(sul)
em relação à linha do equador;
e. A rosa dos ventos, ou rosa náutica, é um desenho que indica a orientação e é utilizada no mostrador de bússulas, em mapas, plantas e maquetes.

a. INCORRETO. Apesar de ser comumente usada em grandes navegações nos séculos passados, ainda é usada e não é obsoleta. Ainda é usada em referências por
coordenadas.
b. INCORRETO. As rosas dos ventos serve para indicar localização e navegação e não escalas.
c. INCORRETO. Pode parecer correto, mas preste atenção. Os pontos subcolaterais não são os 'nordeste,sudeste,noroeste,sudoeste' esses são os colaterais.
Os subcolaterais são 'norte-nordeste', 'norte-noroeste','Sul-sudeste','sul-sudoeste','leste-nordeste','leste-sudeste','oeste-sudeste','oeste-noroeste'
São 8 pontos subcolaterais e não 4, que são os colaterais.
d. INCORRETO. O nascer-do-sol é Leste, com a mão indicando a direita e o pôr-do-sol é o OESTE. E as localizações ocidentais OCIDENTAL é OESTE e oriental é LESTE.
Norte é SETENTRIONAL e MERIDIONAL é SUL em relação à linha do equador.
e. CORRETO.

Q6.(MPE_GO-2020-SSE-AC) Na geogradia, a ideia de direção é entendida pela orietação que pode ter como base a rosa-dos-ventos, mas também coordenadas geográficas.
A rosa dos ventos é uma figura baseada em pontos cardeais, colaterais e subcolaterais. De acordo com a figura acima, identifique os pontos destacados

a. Sul-Sudeste, Norte-Noroeste, Norte-Nordeste, Sudoeste
b. Leste, Oeste, Norte-Nordeste, Sul-Sudoeste, Leste-sudeste
c. Leste, Sul, Oeste, Norte
d. Norte-Noroeste, Sul-Sudoeste, Leste-Sudeste, Oeste-Noroeste
e. Leste, Norte-Nordeste, Oeste, Leste-Sudeste

Os pontos destacados na imagem, o ponto 'B' está na diagonal esquerda acima indicando OESTE ao Norte.
O ponto 'C' está em diagonal direita acima, indicando Leste ao Norte
O ponto 'A' está indicando diagonal direita abaixo, Leste ao Sul
O ponto 'D' está indicando diagonal esquerda abaixo, Oeste ao Sul.

Todos os pontos estão usando subcolaterais e somente um ponto colateral. Sendo assim podemos eliminar as alternativas 'B','C','E'.
Sobrando assim, a alternativa 'A' e 'D'.

Na alternativa 'A', temos um ponto cardeal colateral 'Sudoeste' usado corretamente. Na imagem temos somente um ponto usando essa direção.
O restante são pontos subcolaterais. Portanto, alternativa CORRETA :'A'

Q7(FEPESE-2019/Prefeitura-Fraiburgo) Sobre a orientação no espaço geográfico, é correto afirmar:

1. A direção do sol a nascer ficou determinada como OCIDENTE.
2. Com base na observação da orientação do sol ao nascer e se pôr, foi determinado um conjunto de pontos de orientação que são chamados de pontos
cardeais: LESTE, OESTE, NORTE e SUL.
3. Com base nos pontos cardeais foram determinados direções intermediárias de pontos colaterais.

Assinale a alternativa que indica todas as afirmativas CORRETAS

a. É correta apenas a afirmativa 2
b. São corretas apenas as afirmativas 1 e 2
c. São corretas apenas as afirmativas 1 e 3
d. São corretas apenas as afirmativas 2 e 3
e. São corretas as afirmativas 1,2,3

1. Ocidente é onde o Sol se põe, ORIENTAL é onde o Sol nasce. Portanto, o item 1 está INCORRETO.
2. CORRETA
3. CORRETA

Alternativa 'D' a correta. São corretas apenas as afirmativas 2 e 3.

Q8. (MPE-GO/2018)

A rosa dos Ventos é formada por pontos cardeais, colaterais e subcolaterais. Qual é o significado do ponto subcolateral NNO?

a. Nordeste
b. Nor-Nordeste
c. Nor-Noroeste
d. Noroeste
e. Lés-nordeste

a. 'Nordeste' é ponto colateral. Não é a alternativa.
b. 'Nor-Nordeste' é um ponto subcolateral para indica para direção LESTE ao NORTE(ENE). Não é a alternativa que queremos.
c. 'Nor-Noroeste' é um ponto subcolateral que indica para a direção OESTE ao NORTE (NNO). É a alternativa CORRETA.
d. 'Noroeste' é ponto colateral. Não é a alternativa que queremos
e. 'Lés-nordeste'. Esse termo não existe.

Q9. (MPE-2017) A respeito das formas de orientação, criaram-se os pontos cardeais e os pontos colaterais. Dessa forma, assinale a alternativa que contenha
um ponto colateral.

a. Norte
b. Sul
c. Leste
d. Oeste
e. Sudeste

a. 'Norte' é ponto cardeal. Não é o gabarito.
b. 'Sul' é ponto cardeal. Não é o gabarito.
c. 'Leste' é ponto cardeal. Não é o gabarito da questão.
d. 'Oeste' é ponto cardeal. Não é o gabarito.
e. 'Sudeste' é ponto colateral. É o gabarito da questão.

Q10.(MPE-2017) Sobre a Rosa dos Ventos e os pontos cardeais e colaterais, julgue verdadeiras (V) ou falsas (F) as proposições:

I. Os pontos colaterais são 'nornordeste (NNE)', 'nor-noroeste(NNW)', 'sul-sudeste(SSE)', 'sul-sudoeste(SSW)','lés-nordeste(ENE)',
'léssudeste(ESE),'oés-sudeste (WSE)','oés-sudoeste(WSW)';
II. Os pontos cardeias são Norte(N),Sul(S),Leste(E),Oeste(W);
III. Nordeste(NE), Sudeste(SE) não são pontos colaterais;
IV. Noroeste(NW) e Sudoeste(SW) são pontos colaterais.


I. Esses são pontos subcolaterais. E mesmo assim, estão errados em suas abreviações. ERRADO (FALSO)
II. CORRETO
III. FALSO. São pontos colaterias sim.
IV. VERDADEIRO.

A sequência correta é:

a. F.V.F.V
b. F.V.V.F
c. V.V.F.V
d. F.V.F.F
e. V.V.V.F

Alternativa Correta é a : 'A'.

Q11.(CESGRANRIO-2016-IBGE) Os pontos intermediários nor-nordeste e su-sudoeste localizam-se, respectivamente, entre os pontos cardeais:

a. Norte e nordeste, sul e sudoeste.
b. norte e leste, sul e leste.
c. norte e sudeste, sul e sudoeste.
d. norte e leste, sul e oeste.
e. norte e oeste, sul e oeste.

'nor-nordeste' se localiza entre o ponto cardeal 'norte' e o 'leste'. Já o 'su-sudoeste' se localiza entre o ponto cardeal 'sul' e o 'oeste'.
Alternativa correta a letra 'D'.

Q12. (banca exclusiva) Imagine que você está em um local e o sol está se pondo à sua direita. Com base nessa informação, qual das seguintes alternativas indica
a direção em que você está voltado?

a. Norte
b. Sul
c. Leste
d. Oeste
e. Noroeste

Alternativa 'B'. Porque temos o braço direito indicando que estamos no LESTE ao nascer o sol. Mas na questão nos fala que a sua direita temos o Sol se pondo.
Então, temos o OESTE com o Sol se pondo e os polos ficam invertidos. A direção fica voltada para o SUL e não para o Norte.
          
            
            '''


    def coordenadas_geograficas(self):
        return '''
            [blue]Aqui vai o conteúdo dos exercícios 2.[reset]
COORDENADAS GEOGRÁFICAS:

As coordenadas geográficas são um sistema de REFERÊNCIA utilizado para determinar a localização precisa de um ponto na superfície da Terra. Elas são compostas
por duas medidas principais: LATITUDE E LONGITUDE. Ao fornecer as coordenadas geográficas de um ponto, é necessário especificar sua latitude e longitude
para obter uma localização precisa na superfície da Terra. Essas informações são cruciais em diversas áreas, como aviação, náutica, estudos geográficos,engenharias
e mapeamento topográfico como estudos de relevo, por exemplo.

	É possível obter a localização de Brasília por meio das coordenadas geográficas. A capital do Brasil possui as seguintes coordenadas:

Latitude 15° 47'33"S e Longitude 47°52'32"W. Além de uma altitude de aproximadamente 1.172 metros acima do nível médio do mar.            

Latitude:

	A latitude é uma medida angular, representada por linhas horizontais, que indica a distância de um ponto em relação a linha do Equador. Uma linha imaginária
que circunda a Terra no seu ponto mais largo. Ela é medida em graus e pode variar de 0° a 90°. Sendo 0° no Equador e aumentando em direção aos extremos da terra, os
polos Norte e Sul;

	As coordenadas de latitude são expressas em graus, minutos e segundos. Cada grau é dividido em 60 minutos. Cada minutos é dividido em 60 segundos.
Por exemplo: A latitude 40°30'20" representa: 40 graus, 30 minutos e 20 segundos.

	A latitude tem uma influência significativa no clima. Áreas próximas ao Equador tendem a ser mais quentes e úmidas, enquanto áreas próximas aos polos
têm climas mais frios.
	Além da linha latitudinal do Equador, temos outros linhas que são amplamente utilizadas para fins de referência. O Trópico de Câncer está localizado
a 23,5°N e o Trópico de Capricórino está licalizado a cerca de 23,5°S.

LONGITUDE

	A longitude é uma medida angular, vertical, que indica a distância de um ponto em relação ao meridiano de Greenwich, outra linha imaginária que atravessa
a cidade de Greenwich, em Londres. Ela é medida também em graus, de 0° a 180°. Sendo 0° no meridiano de Greenwich e aumentando tanto para Leste quanto para Oeste.
	As coordenadas também são expressas da mesma forma que as LATITUDES.
	A longitude está diretamente relacionada à determinação do FUSOS HORÁRIOS. Os fusos horários são áreas definidas na Terra que compartilham o mesmo horário.
A Terra é dividida em 24 fusos horários principais, cada um abrangendo uma faixa de 15° de longitude uma da outra, em sentido vertical.
	O primeiro fuso horário é baseado no meridiano de Greenwich (0° de longitude) e é conhecido como Tempo Universal Coordenado (UTC).
	A LID (Linha Internacional de Data) é localizada no grau 180° de longitude, uma linha imaginária onde ocorre a mudança de dia. Ao cruzar a linha do leste
para Oeste, ocorre uma mudança de dia, um avanço de um dia no calendário. Ao cruzá-la do Oeste para Leste, ocorre uma retrocesso de um dia.

Paralelos e Meridianos:

	Parelelos são linhas imaginárias que circundam a Terra de Leste a Oeste, paralelas a linha do Equador. Os paralelos são usados para medir a latitude.
O paralelo mais importante é o Equador, localizado a 0° de latitude que divide a Terra em dois hemisférios, Norte e Sul. Outros papalelos significativos são os
Trópicos de Câncer e Capricórnio, localizados a cerca de 23,5° de latitude Norte e Sul, respectivamente. Os círculos Polares Ártico e Antártico, são localizados
a cerca de 66,5° de latitude, Norte e Sul, respectivamente.

	Os Meridianos são linhas imaginárias que conectam os polos norte e sul da Terra e cruzam o Equador em ângulos retos. O meridiano mais importante é o do
Greenwich, localizado a 0° de longitude, que divide a Terra em dois hemisfério, Leste e Oeste. A longitude é medida em relação a esse meridiano e varia de 0° a 180°
para leste e oeste.

	ALTITUDES:

A altitude é a medida vertical da distância entre um ponto na superfície da Terra e o nível médio dos oceanos. Geralmente expressa em metros ou pés.
Ao considerarmos a altitude do Monte Everest, que é a montanha mais alta do mundo, podemos compreender sua elevação em relação ao nível médio dos 
oceanos. A altitude do Monte Everest é de aproximadamente 8.848 metros (29.029 pés) acima do nível do mar. 
	A altitude é uma informação crucial para determinar características geográficas, como montanhas, planaltos e vales, bem como para entender seu
impacto na climatologia, na formação de ecossistemas e na disponibilidade de recursos hídricos. Além disso, é também importante para atividades da aviação,
construção e turismo.

            '''
    def exercicios_coordenadas(self):
        return '''
            [blue]Aqui vai o conteúdo dos exercícios 2.[reset]
Q1. (FGV-2022/IBGE) As coordenadas geográficas consistem em um dos métodos mais eficientes de localização, pois permitem identifcar qualquer ponto da superfície
da Terra por meio de dois valores:

a. Perímetro e circunferência
b. órbita e altitude.
c. latitude e longitude
d. abscissa e ordenada
e. distância e altitude.

a. Permite identificar a área.
b. Permite identificar a distância e espaço.
c. CORRETO. São referência que são bastante eficientes na localização.
d. localização de termos matemáticos
e. Permite identificar a área.

Q2. (Banca Exclusiva) A latitude é uma medida angular que indica a distância de um ponto em relação a qual referência geográfica?

a. Meridiano de Greenwich
b. Equador
c. Polo Norte
d. Polo Sul
e. Linha internacional de Data

Alternativa correta a 'b'.

Q3 (banca exclusiva) Considerando o sistema de coordenadas geográficas, qual dos seguintes elementos é utilizado como ponto de referência para medir a longitude?

a. Trópico de Capricórnio
b. Meridiano de Greenwich
c. Linha internacional de Data
d. Círculo Polar Ártico
e. Linha do Equador

A trópico de Capricórnio e a linha do Equador são linhas verticais latitudinais, portanto, podemos eliminar essas alternativas.
A linha internacional de Data não é a referência para medir e sim, separar o dia da noite de Leste a Oeste.
O Meridiano de Greenwich é a linha vertical longitudinal para medir como referência. Alternativa 'B'.

Q4(OBJETIVA-2023-Prefeitura de Horizontina)

Para localizar lugares ou objetos com exatidão na superfície terrestre, usa-se um conjunto de linhas imaginárias traçadas sobre os mapas e globos. Essas linhas
são denominadas de paralelos e meridianos. Sendo assim, Marcar C para CERTAS e E para ERRADAS e, após, assinalr a alternativa que apresente a sequência correta.

( ) A linha do Equador é um paralelo que divide a Terra em duas partes iguais chamadas de hemisférios: Leste e o Oeste.
( ) Todos os meridianos são medidos a partir do meridiano de Greenwich, que corresponde a 0° e divide a Terra em dois hemisférios: o Norte e o Sul
( ) O trópico de Câncer é um paralelo situado no Hemisfério Norte.

a. C-C-E
b. E-E-C
c. C-E-C
d. E-C-E

Alternativa 'B' - E-E-C

Correções: A linha do Equador é uma linha paralela latitudinal que divide a Terra em duas partes iguais chamadas de hemisférios SUL e NORTE.
O meridiano de Greenwich, por convenção, divide a terra em hemisférios LESTE e OESTE.

Q5.(FEPESE-2022-Prefeitura de São José)

Analise as afirmativas abaixo sobre a localização e a orientação no globo terrestre.

1. Dispostos paralelamente em torno do globo terrestre e circundando-o no sentido leste-oeste encontramos os meridianos terrestres.
2. Linhas imaginárias que se estendem de um polo ao outro dividindo a Terra são os paralelos.
3. A linha do Equador envolve a Terra em sua porção mais larga, dividindo o planeta em dois hemisférios, o Norte e o Sul.
4. Todos os pontos situados num mesmo paralelo apresentam a mesma longitude.

1. ERRADO -> Se são paralelos, então não são meridianos terrestres. 
2. ERRADO -> São os meridianos (linhas verticais) que se estendem de um polo ao outro.
3. CORRETO  
4. ERRADO -> Não. Não terão as mesmas longitudes.

a. Apenas a afirmativa 3 a correta. 

Q6. (Instituto Acces-2017-Prefeitura de Itabira)

Observe a figura a seguir:

a. O ponto E é o mais setentrional e oriental da figura.
b. O ponto C é o mais meridional da figura, enquanto que o ponto A é o seu total oposto.
c. O ponto A está localizado nos hemisfério Norte e Leste.
d. O ponto B encontra-se a 0° de longitude Oeste e 80° de latitude Norte.

a. SIM (Setentrional é NORTE, ORIENTAL é LESTE)
b. Não, o ponto 'E' é o mais meridional da figura.
c. Não. No hemisfério Norte e Oeste.
d. Não. 40° de latitude ( linhas horizontais ) e 0° de longitude. ( linhas verticais )

Portanto, afirmativa 'A' a única correta.

Q7. (Avança-SP/2022-Prefeitura de Amparo) As linhas imaginárias são denominadas de paralelos e meridianos e levam em consideranção os pontos cardeais.
No caso dos paralelos temos as linhas horizontais que cortam o globo de ________, já os meridianos correspondem as linhas verticais que cortam de _______.

Assinale a alternativa que preenche corretamente as lacunas:

a. Norte a Oeste / Leste a Sul
b. Leste a Oeste / Norte a Sul
c. Norte a Sul / Leste a Oeste
d. Leste a Sul / Norte a Oeste
e. Centro Norte/ Centro Sul

Norte a Sul / Leste a Oeste <- Alternativa 'B'.

Q8. (FEPESE-2022-Prefeitura de Balneário Camburiú) Analise as afirmativas abaixo sobre a localização no espaço geográfico terrestre.

1. Os paralelos são linhas imaginárias horizontais que circundam o globo terrestre.
2. Os meridianos são linhas imaginárias verticais, medidos em graus e traçados do Polo Sul ao Polo Norte.
3. Os meridianos têm valor máximo de 190° no Hemisfério Leste.

Assinale a alternativa que indica todas as afirmativas corretas:

a. É correta apenas a afirmativa 1
b. É correta apenas a afirmativa 2
c. São corretas apenas as afirmativas 1 e 2
d. São corretas apenas as afirmativas 1 e 3
e. São corretas as afirmativas 1,2,3

1. CORRETA // 2.CORRETO. // 3. ERRADO. Tem valor máximo 180° em ambos os hemisférios: tanto LESTE como OESTE.


Alternativa 'C'.

Q9. (MPE-GO/2022) Coordenadas geográficas são a latitude e a longitude de um ponto no globo. Assim, considerando-se um hipotético ponto situado acima do círculo
do Equador e à esquerda do meridiano de Greenwich, é correto dizer que tem como coordenadas geográficas :

a. Sul e Leste
b. Norte e Oeste
c. Sul e Oeste
d. Norte e Leste

Alternativa 'B' -> Norte e Oeste

Q10. (CETREDE-2021/Prefeitura de Icapuí) As latitudes e longitudes têm máximas de graus, respectivamente:

a. 180° e  90°
b. 90° e 180°
c. 180° e 180°
d. 90° e 90°
e. 180° e 360°

As latitudes são linhas imaginárias horizontais que tem máxima de de graus de 90°.
As longitudes , são linhas imaginárias verticais que possuem máxima, em graus, de 180° até o LID

Portanto, alternativa 'B'.

Q11.(UFSM-2021) A cartografia é considerada a ciência que trata da criação, da produção, da difusão, da utilização e do estudo dos mapas.
Os fusos horários, também denominados zonas horárias, foram estabelecidos no ano de 1884, com o intuito de estabelecer diferentes horários, em função do
movimento de rotação da terra, sendo adotado mundialmente desde então. Partindo desta informação, o fuso referencial para a determinação das horas é:

a. Latitude.
b. Linhas do Equador.
c. Meridiano de Greenwich.
d. Trópico de Câncer.
e. Trópico de Capricórnio.

Sem dúvida, o Meridiano de Greenwich, onde temos o UTC. Uma linha imaginário, convencional, longitudinal e vertical, que possui, em graus, 180° até a LID.
O primeiro fuso horário é baseado no meridiano de Greenwich (0° de longitude) e é conhecido como Tempo Universal Coordenado (UTC).

Q.12 (CEBRASPE-2021-IBGE) O sistema de coordenadas Geográficas é utilizado para a localização de pontos fixos nos mapas. Cada lugar ou ponto da superfície 
terrestre corresponde a uma coordenada geográfica. Considerando esse sistema e a figura apresentada, assinale a opção correta.

a. Os pontos C e D se encontram nas mesmas coordenadas geográficas, porém em hemisférios diferentes.
b. O ponto C no mapa corresponde ao território brasileiro , estando localizado no hemisfério ocidental.
c. O ponto B, localizado na Ásia Central, está mais próximo do meridiano de Greenwich que o ponto C
d. O ponto C se encontra no hemisfério setentrional enquanto o ponto A se encontra no hemisfério meridional.
e. As coordenadas geográficas são definidas apenas pelos meridianos, por isso todos os pontos localizados no mapa se localizam sobre meridianos.

a. ERRADO. Coordenadas diferentes também. 
b. CORRETO. Hemisfério OCIDENTAL ( OESTE ) -> CORRETO.
c. ERRADO. O ponto C no mapa está mais próximo.
d. ERRADO. Setentrional é ao NORTE. A localização do ponto 'C' é no Brasil, portanto, Meridional. Já o ponto 'A' é setentrional , ou seja, ao NORTE.
e. ERRADO. Além dos meridianos , existem os paralelos. Para deixar mais precisa a localização.

Q13(CEBRASPE-2021/IBGE) A figura a seguir mostra uma visão esquemática do globo terrestre, centrada no polo norte. Considerando essa figura, assinale
a opção correta.

a. A longitude máxima é 90 graus.
b. O ponto A tem 90 graus de longitude OESTE.
c. O hemisfério ocidental fica entre ZERO e 180 graus LESTE.
d. A Linha do Equador corresponde a uma semicircunferência
e. A linha internacional de Data (LID) corresponde ao meridiano ZERO. 

a. INCORRETO. A longitude máximo é 180°
b. CORRETO.
c. INCORRETO. O hemisfério Ocidental fica entre ZERO e 180° OESTE.
d. INCORRETO. Não há linha do Equador nessa visão, mas de qualquer forma é um CIRCUNFERÊNCIA INTEIRA.
e. INCORRETO. Seja para LESTE ou OESTE corresponde a 180°.

Q14(CEBRASPE-2021-IBGE) As coordenadas geográficas constituem um dos elementos básicos dos mapas. Acerca desse assunto, assinale a opção correta:

a. A latitude máxima refere-se ao ângulo formado entre o plano da eclíptica e o eixo da Terra.
b. As medidas em graus entre um meridiano e outro indicam as latitudes, estabelecidas a partir de um ponto zero.
c. O valor de cada paralelo é determinado pelo ângulo formado entre o plano do equador e o meridiano de referência.
d. Por meio das coordenadas geográficas, é possível relacionar a distância real com a distância gráfica expressa nos mapas.
e. As coordenadas geográficas são determinadas com base na rede geográfica de linhas dispostas no sentido norte-sul e leste-oeste.

a. INCORRETO. A latitude (linhas horizontais) refere-se ao ângulo formado entre o plano perpendicular ao eixo da TERRA.
b. INCORRETO. O meridiano (linhas verticais) e outro não indicam as latitudes ( linhas horizontais ).
Os paralelos e outro indicam as latitudes como referência a linha do Equador a partir do grau 0°.
c. INCORRETO ->  O valor de cada paralelo NÃO. O meridiano de referência é o Greenwich, portanto, somente é determinante com um ângulo de referência.
d. INCORRETO -> Nem sempre. Existem outros meios de relacionar a distância real com a distância gráfica por meio das escalas.
e. CORRETA -> 

Q15(CEBRASPE/2024/CAGEPA) No sistema UTM (Universal Transversa de Mercator), dois pontos A e B estão localizados em um mesmo fuso e nas coordenadas (80 kmE; 7.000
kmN) e (100 kmE; 7.500 kmN), respectivamente. Nessa situação hipotética, o ponto A, em relação ao ponto B, está localizado no sentido:

• A noroeste.
• B nordeste.
• C sudoeste.
• D sudeste.
• E oeste.

Diferença nas coordenadas:
- Diferença Leste (Easting): 100-80=+20 km → B está mais a leste que A. Logo, A está mais a oeste que B.
- Diferença Norte (Northing): 7.500-7.000=+500 km → B está mais ao norte que A. Logo, A está mais ao sul que B.
Combinação das direções:
Se A está mais ao sul e mais a oeste em relação a B, então: 👉 A está a sudoeste de B.
Gabarito letra 'C'-> sudoeste 

Q16 ( CORREIOS) Um grupo de atletas corredores resolvem realizar uma trilha ecológica. Com auxílio do GPS, todo o grupo conseguiu completa a trilha.
O GPS é um sistema de posicionamento global em emite informações como a coordenada geográfica de um ponto. Sobre coordenadas geográficas é correto dizer:

a. as coordenadas são formadas por paralelos e meridianos.
b. os meridianos dividem a terra em dois hemisférios, norte e sul
c. os paralelos auxiliam na identificação da posição longitudinal
d. a latitude é medida a partir da linha do Equador e vai de 0° a 180°
e. quanto menor a latitude, menores são as temperaturas.

a. CORRETO
b. INCORRETO. Os meridianos são linhas verticais chamadas de longitudes. E medem a distância em graus a leste ou a oeste do Meridiano de Greenwich.
Vão de 0° a 180°. As linhas horizontais são as latitudes, são os paralelos e dividem a terra em dois hemisférios (Norte e Sul). Vão de 0° a 90°.
c. ERRADO. A posição longitudinais são linhas verticais  chamadas de meridianos, elas é que auxiliam na identificação dessas posições.
d. ERRADO. A latitude são linhas horizontais chamadas de paralelos e são medidas a partir da linha do Equador e vão de 0° a 90°.
Quem vai de 0° a 180° são os meridianos, com suas linhas verticais chamadas de longitudes.
e. ERRADO. Quanto mais próximo da Linha do Equador, maior será a incidência solar.

Q17.(UNIVIDA) Um sistema de coordenadas geográficas latitudinais e longitudinais são obtidas pela interseção de um meridiano com um paralelo,
normalmente representados em graus, minutos e segundos. Assim sendo, a latitude é medida tendo como referência o meridiano e Greenwich é a longitude
a partir da linha do Equador.

A informação acima está incorreta, porque:

a. Coordenadas geográficas só podem ser obtidas por meio de imagem satélite.
b. Tanto a latitude quanto a longitude se medem a partir dos paralelos terrestres.
c. Latitude tem como referência a linha do Equador e longitude o meridiano de Greenwich.
d. Os meridianos não compõem as coordenadas geográficas.
e. Numa coordenada geográfica não interseção entre paralelo e meridiano.

a. ERRADO. Existem outros meios de obter coordenadas. Não justifica
b. ERRADO. A latitude se mede com a interseão com a longitude em um ângulo de 90º.
c. CORRETO. A latitude são linhas horizontais que tem como referência a linha do Equador e a longitude são linha verticais paralelas que tem como referência
o meridiano de Greenwich
d. ERRADO. Os meridianos compõem as coordenadas geográficas sim.
e. ERRADO. Em uma coordenada deve haver interseção ( encontro )entre paralelos e meridianos completando um ângulo de 90°

GABARITO: 'C'

Q18. (FURB)Sobre as coordenadas geográficas, preencha os parênteses e registre V, para verdadeiro e F, para FALSO:

a. As coordenadas geográficas de um determinado ponto no espaço podem ser identificadas por meio do cruzamento de um paralelo e de um meridiano.
b. A localização das coordenadas geográficas pode ser feita mediante o uso de instrumentos e equipamentos cartográficos, sejam eles analógicos ou digitais.
c. As coordenadas geográficas são um sistema de linhas imaginárias que permitem a localização de qualquer ponto da superfície terrestre.

Assinale a alternatica com a sequência correta:

a. V-V-F
b. V-V-V
c. F-V-F
d. F-V-V
e. F-F-F

a. CORRETA. V // b.CORRETO // c. CORRETO. Portanto, a alternativa correta é: 'B' - V-V-V

Q19. De acordo com as coordenadas geográficas, os ____ são linhas imaginárias que cotam a Terra no sentido norte-sul, ligando um polo ao outro.
Os _____ são linhas imaginárias que circula a Terra no sentido leste-oeste. Assinale a alternativa correta, respectivamente:

a. paralelos/pontos geográficos
b. meridianos/pontos geográficos
c. paralelos/meridianos
d. meridianos/paralelos
e. pontos geográficos/paralelos

Os MERIDIANOS são linhas imaginárias que cortam a Terra no sentido norte-sul, ligando um polo ao outro.
Os PARALELOS são linhas imaginárias que circulam a Trra no sentido leste-oeste.

Portanto, gabarito letra: 'D'

Q20(IBFC) O Equador, metade do caminho entre os polos, forma um grande círculo que separa o Hemisfério Norte e Sul. 
O Equador fica na latitude____a linha de referência para medir a latitude em grau norte ou grau sul. O polo norte e o polo sul são as latitudes máximas em cada hemisfério.
Assinale a alternativa que preencha corretamente a lacuna:

a. ZERO GRAU (0°)
b. 90°
c. 180°
d. 270°
e. 360°

O Equador fica na latitude 0°. Alternativa 'A'.

Q21. Para determinar a longitude de um local, é necessário conhecer:

a. A distância em relação ao Polo Norte.
b. A distância em relação ao Polo Sul
c. A distância em relação à linha do Equador.
d. A distância em relação ao Meridiano de Greenwich.
e. A distância em relação ao Meridiano De Paris.

Alternativa 'D' -> Para determinar a longitude de um local, é necessário interceder paralelamente com a linha do Equador para se obter coordenadas geográficas.
Mas nesse caso, primeiramente, conhecer a distância em relação ao Meridiano de Greenwich.

Q22. Analise as afirmativas abaixo em relação à localização do Brasil.

1. Com relação ao meridiano de Greenwich, o Brasil localiza-se totalmente no hemisfério oeste
2. O Brasil esta com uma grande parte do território no hemisfério meridional.
3. A maior parte do território brasileiro fica compreendida entre o Equador e o Trópico de Capricórnio.

Assinale a alternativa que indica todas as afirmativas corretas:

a. Apenas a 1
b. Apenas a 1,2,3
c. Apenas as 1, 3
d. Todas estão incorretas.

1. CORRETA / 2.CORRETO (Hemisfério Meridional = SUL) 3. CORRETO

Alternativa 'B'.
            
            
            '''            
    def projecoes_cartograficas(self):
        return '''
            [blue]Aqui vai o conteúdo dos exercícios 3.[reset]
            Projeções cartográficas são métodos utilizados para representar a superfície curva da Terra em um plano bidimensional, como um mapa.
PROJEÇÕES CARTOGRÁFICAS

Leitura e Interpretações de Mapas

	A leitura de mapas é a habilidade de interpretar informações e compreender as representações gráficas presentes em um mapa.
	Envolve a compreensão dos símbolos, cores, linhas e outros elementos cartográficos utilizados para representar características geográficas
como rios, montanhas, estradas, cidades e áreas temáticas específicas.
	Por meio da leitura de mapas, é possível obter informações sobre a localização, distribuição, relações espaciais e outras características geográficas
de uma determinada área.

PROJEÇÃO CILÍNDRICA:

	Neste tipo de projeção, a superfície da Terra é projetada em um cilindro que envolve o globo terrestre. Uma das vantagens de usar a projeção cilíndrica
é que ela preserva as formas e as direções das áreas próximas ao equador. Isso significa que as formas dos continentes e países nas latitudes mais baixas são
representadas com maior precisão. A linha do Equador é beneficiada com isso.

	Conforme as latitudes mais próximas dos polos SuL e Norte a deformação são maiores, ou seja, são mais distorcidas.

PROJEÇÃO CÔNICA
	
	Nesse tipo de projeção, a superfície da Terra é projetada em um cone, sendo usada para representar áreas geográficas que estão mais próximas aos polos.
Uma das vantagens da projeção cônica é a preservação das formas e proporções em regiões de média latitude.

PROJEÇÃO PLANA/AZIMUTAL

	Neste tipo de projeção, a superfície da Terra é projetada em um plano que tangencia um ponto central. Essas projeções têm maior precisão nas áreas próximas
ao ponto de tangência e distorcem as áreas mais distantes.

TIPOS DE MAPAS

	Mapa geopolítico:
	Representa as fronteiras e os limites territoriais de países, estados, províncias, cidades e outros entes políticos. É útil para entender a organização 
política de uma região.

	Mapa topográfico:

	Mostras as características físicas e elevações da superfície da Terra, como montanhas, vales, rios e lagos. É útil para atividades ao ar livre, planeja-
mento de rotas e estudos geográficos.

	Mapa temático:

	Concentra-se em um tema específico, como clima, população, uso do solo, vegetação, economia, transporte ou qualquer outro aspecto geográfico. É útil para
analisar dados e padrões relacionados a um determinado tema.

	Mapa rodoviário:

	 Apresenta redes de estradas, rodovias, ruas e vias de transporte. É útil para nevegação e planejamento de viagens.

	Mapa Náutico:

	Elaborado para a navegação marítima, exibe informações relevantes para os marinheiros, como rotas, profundidades, faróis, correntes e perigos.
É essencial para a navegação segura em mares e oceanos.

	Mapa de relevo

	Utiliza técnicas de sombreamento e cores para representar as formas tridimensionais da da Terra. É útil pra entender a topografia e a geomorfologia
de uma área. 

	Mapa climático: Indica os padrões climáticos e as características meteorológicas de uma região, como temperatura, precipitação, ventos e pressão atmos-
férica. É útil para estudar o clima e a meteorologia.

	Mapa de uso de solo: Mostra a distribuição e o tipo de atividades humanas em uma área, como áreas urbanas, rurais, industriais, comerciais e residencias.
É útil para o planejamento urbano e a gestão do território.

Toda mapa tem área, forma e distância. 

Se por exemplo, escolhe manter a forma então podemos classificar o mapa  como CONFORME.
Se por exemplo, escolher manter a área então podemos classificar o mapa como EQUIVALENTE.
Se por exemplo, escolher manter as distâncias então podemos classificar o mapa como EQUIDISTANTE.
Se por exemplo, escolher distorcer tudo, então podemos classificar o mapa como AFILÁTICO. Ex: O mapa mundi
Projeção: Projetar a terra pro papel. Utiliza-se formas geométricas da matemática para conseguir o melhor resultado em questão.
A cilíndrica, cônica e a plana/azimutal.

A cilíndrica a projeção tem o nome de MERCATOR (Séc.XVI) e GALL & PETERS.(Século XIX & 1970)
A MERCATOR elaborada no século XVI em um período de grandes nagevações e expansão europeia. Então a visão do mapa é eurocêntrica. Portanto, ele distorce
a área e manter a forma. Portanto, o mapa é CONFORME.
Já a projeção cilíndrica de PETERS tem valor dos países subdesenvolvidos. O formato é distorcido e mantem a área. Sendo a área  EQUIVALENTE.

Sendo assim, vamos a um exercicio. A projeção que representará uma região próxima à Linha do Equador com a menor distorção da escala principal é:

A projeção cilíndrica a qual a linha do Equador é onde tem menos distorção. Abraçado de Leste a Oeste. E não de Norte a Sul.
Em Cartografia, os paralelos são linhas traçadas , às latitudes, paralelas à linha do Equador. Em que variam de 0° para 90° nos polos SUL e NORTE.
Em Cartografia, o Meridiano de Greenewich (XIX) é uma referência o qual por convenção é traçado o meio da esfera global da Terra.   
Nem toda Cartografia é um mapa. Existem outras representações do mundo real 3D.

CROQUI, Plantas, mapas topográficos e anamorfoses.

Mapa Croqui é uma mapa mas não possui título, sem escalas, convenções, orientação. É uma forma de representar o espaço sem rigor cartográfico.
Ex: Salas de aula, sala de cinema.

Plantas usadas também em Engenharia. São tipos de representação de escala GRANDE. Ou seja, possui bastante detalhes. Ex: Planta de uma casa, bairro, cidade.

Mapas topográficos:

São tipos de mapas em que cada linha traçada é uma ISOÍPSIAS. Elas são as curvas de nível.
Regras das isoípsias. Uma curva jamais corta a outra. Elas não traçam uma a outra.
Quanto maior a proximidade das linhas de nível, as isoípsias, maior a inclinação.

Mapas anamórficos:

A anamorfose é a transfomação cartográfica espacial em que a forma dos objetos é distorcida, de forma a realçar o tema. A área das unidades espaciais
às quais o tema se refere é alterada de forma proporcional ao respectivo valor.

Ex: Casos de dengue ( Uma determinada região fica maior, proporcional ao respectivo valor quantititivo, por exemplo, do que em outros lugares )

Todo mapa precisa ter:

- Título
- Mapa
- Legenda
- Orientação

Escalas:

A compreensão das escalas é fundamental para a leitura e interpretação de mapas. As escalas representam a relação ( de proporção na escala numérica )
entre dimensões reais do mundo e sua representação em um mapa. Elas nos permitem compreender o tamanho, a distância e a proporção dos elementos
geográficos retratados. Ao olhar um mapa, é importante verificar a escala utilizada, pois ela determinará a relação entre as medidas no mapa e as medidas
reais no terreno. Observe os exemplos:

Relação matemática entre a medida no mapa e a medida real no terreno.
Numérica (1:10.000) -> Uma fração
Gráfica -> Barras com números que não são proporcionais, usam medidas diferentes. ( KM X CM ) (CM / KM)

Textual (1 cm → 100 m)

Classificação:

Grande escala (1:10.000 ou maior) – mais detalhes.

Média escala (1:25.000 a 1:100.000).

Pequena escala (1:250.000 ou menor) – menos detalhes.

Exemplo:
1 : 50.000
→ 1 cm no mapa representa 50.000 cm no terreno
→ 50.000 cm = 500 m = 5 km

Escala grande (número pequeno depois dos dois pontos)

Ex.: 1:1.000, 1:2.000, 1:5.000

Mostram muitos detalhes
Usadas para: plantas, projetos urbanos, loteamentos
Cobrem pequenas áreas

Escala média

Ex.: 1:25.000, 1:50.000, 1:100.000

Usadas em cartas topográficas
Detalhamento moderado

Escala pequena (número grande depois dos dois pontos)

Ex.: 1:250.000, 1:1.000.000
Poucos detalhes
Usadas em mapas de estados, países e continentes, rios, mares
Cobrem grandes áreas

Um mapa está na escala 1:100.000.
Se o rio tem 3 cm no mapa:

1 cm → 100.000 cm → 1 km
3 cm → 3 km

Ou seja, escala PEQUENA.

Outro exemplo:

No terreno, duas cidades estão a 20 km de distância.
Na escala 1:250.000, qual será a distância no mapa?

1 cm → 250.000 cm → 2,5 km
20 km ÷ 2,5 km/cm = 8 cm

Escala PEQUENA

Obtenção de imagens:

	- Sensoriamento remoto por aerofotogrametria -> locais pequenos, lugares
	- Sensoriamento remoto por satélite -> Países, continentes

A escala geográfica é uma redução e proporcional.
Mas outras escalas podem ser de ampliação, em outras áreas.

Existem dois tipos de escalas -> A gráfica ( as medidas não são proporcionais )
A escala numérica é proporcional. ( Usam as mesmas medidas proporcionais )

Na escala numérica a realidade é reduzida. Ou seja, há uma relação de proporção.

10³- 10²-10¹ -10-10¹- 10²-10³
km - hm -dam- m- dm -cm -mm

Na cartografia , as unidades de medidas usadas será de KM-->CM que será de 5 zeros.
Para transformar de KM para CM, irá colocar 5 à esquerda.
Para CM em KM é retirar os 5 zeros

Exemplo:

10.000 CM para KM: Retire 5 zeros: 1 km

Escala grande para áreas pequenas, com muitos detalhes
Escala pequena são pouco detalhes, área grande. Ex: Mapa Mundi

Quanto menor o denominador da escala, maior será a escala.

Vale destacar que o uso de escalas possui limitações. Entre as principais, destaca-se que elas são usadas para representar medidas lineares e não levam em 
consideração a curvatura da Terra. Essas limitações são inerentes ao processo de representação tridimensional do nossa planeta em um mapa bidimensional.
Cada tipo de projeção cartográfica tem suas próprias características e áreas onde é mais precisa.

Escala Gráfica:

	A Escala gráfica é uma linha reta marcada em unidades de distância reais, geralmente em quilômetros ou milhas, que está presente no mapa.
Por exemplo: se a escala gráfica mostra que 1 centímetro equivale a 1 KM, então uma distância medida de 5 centímetros no mapa será igual a uma distância de
5 KM na realidade.

Escala verbal:

	A escala verbal utiliza palavras para descrever a relação entre o mapa e a realidade. Por exemplo, uma escala verbal pode ser "1 centímetro no mapa
representa 1 quilômetro na realidade".

Resumen:  Quanto maior o denominador, menor a escala, menos detalhes. Quanto menor o denominador MAIOR a escala, mais detalhes.

LEGENDAS:

	As legendas são fundamentais em mapas, pois fornecem informações adicionais e auxiliam na interpretação correta das representações cartográficas.
Uma legendas é uma seção ou uma área específica do mapa que contém símbolos, cores, linhas, letras ou outras formas de representação gráfica acompanhadas
de textos descritivos. A principal função da legenda é fornecer uma chave de interpretação para os elementos simbólicos presentes no mapa. Ela ajuda a identifica
e compreende o significado dos símbolos presentes no mapa. Ela ajuda a identificar e compreender o significado dos símbolos cartográficos utilizados, como ícones
representando rios, áreas, estrada, pontos de interesse. Além disso, a legenda pode indicar a escala utilizada no mapa, infomações sobrre coordenadas geográficas,
unidades de medida e outra referências.

	Azul -> Hidrografia
	Cinza -> Urbano
	Vermelho -> Muito Elevado/quente
	Amarelo -> Elevado 
	Amarelo Claro -> Elevado Moderado
	Verde Claro -> Elevação Moderada
	Verde -> Elevação Baixa/ Vegetação

CONVENÇÕES:

	Existe para facilita a representação cartográfica, foi criado um sistema de símbolos conhecidos como convenções cartogáficas. Os símbolos foram
escolhidos de forma a conter um ceto grau de compreensão e intuição de seu significado, possibilitando a leitura da informação contida no mapa por qualquer
pessoa em qualquer parte do mundo. Se agente quer representa uma área edificada, então usaremos esse símbolo, por exemplo. Se a equipe quiser representar
uma capital com uma bola e no fundo uma bola preta, então usaremos esse símbolo.

Projeções Cartográficas

O que seria? A meneira de apartir de distorções escolhidas e calculadas representar o mapa.
O fomato do planeta terra é GEOIDE.

1. Projeção cilíndrica: Grande característica em que os Paralelos(linhas horizontais) e Meridianos (linhas verticais) formam ângulos de 90°.
2. Projeção Cônica: Somente um hemisfério por vez , distorce pouco as áreas temperadas. Entre 23° a 66°.
3. Projeção Azimutal/plana/polar: Centro de projeção, pouco distorcido. As áreas periféricas terão maior distorção.
Grande utilizado para utilização geopolítica. A logo da ONU é AZIMUTAL. Bastante ideológico. Em que valoriza os países desenvolvidos.

Todo o mapa é distorcido, e irá depender da intenção ideológica.

Um mapa pode ser equivalente: Preserva-se a área representada.
Um mapa pode ser equidistante: Preserva-se distâncias de continentes
Um mapa conforme: Preserva-se as formas.

Autores dos mapas mais importantes:

MERCATOR X PETERS

Mercator:

A ideia do mapa era pra ajudar os navegantes. Mapa cilíndrico e conforme, preservando as formas.
Usado em grandes navegações e eurocêntrico.
As áreas são exageradas nas latitudes e coloca a europa no centro do mapa.

Mapa de Peters:

Cilíndrico e equivalente, ou seja, as áreas são valorizadas e sua ideologia era eurocêntrica também.
Utilizando na Guerra Fria.

CURVAS de nível: ISOÍPSA

São linhas que unem pontos de mesma altitude.
'''
    def exercicios_proj_car(self):
        return '''

Q1 (IBADE-2020-SEE-AC) Leia e analise as afirmativas a seguir.

I. Paralelos e meridianos são representados em um cilindro que é planificado.
II. O ponto de tangência se torna o centro do mapa que apresenta deformações conforme é afastado.
III. Cone tangente a superfície terreste com maiores deformações na base e no vértice

As definições acima fazem referência aos conceitos de projeção:

a. Lambert - cilíndria - cônica
b. Cônica - Azimutal - Cônica
c. Cilíndrica - azimutal - cônica
d. Peters - Mercator - cilíndrica
e. Mercator - cilíndrica - cônica

Alternativa 'C'

Q2(CPCON/2017/Prefeitura de Riacho da Cruz)
A principal característica da projeção azimutal ou polar é:

a. reforçar o formato geoide do planeta com um plano de projeção cilíndrico.
b. valorizar a representação precisa das zonas temperadas
c. atenuar as deformações nas áreas próximas ao ponto de tangência
d. apresentar com rigor as formas dos continentes localizados sobre a Linha do Equador
e. veicular informações ignoradas por projeções de caráter eurocêntrico.

a.  Não. A projeção azimutal é plana.
b.  Não é a principal característica.
c. CORRETO.
d. Projeção cilíndrica.
e. Não.

Q3 (FEPESE-2018-Companhia Águas de Joinville)
Essa projeção apresenta a Terra como se ela fosse vista a grande distância. Esses mapas resultam da projeção de uma parte da superfície sobre um plano.
Essa projeção não conserva as formas nem as áreas corretas. Formas e áreas sofrem distorções crescentes à medida que aumenta a distância do centro da projeção.
Mas ela cumpre a finalidade a que se propõe revelando os azimutes exatos dos pontos cartografados em relação ao ponto central do mapa. Essa projeção oferece
um conjunto de utilidades práticas ligadas basicamente ao deslocamento a partir de um único ponto do globo. É empregada por governos municipais de cidades
importantes, para determinar as rotas mais curtas para qualquer parte do mundo. A projeção descrita acima é a:

a. Projeção de Peters
b. Projeção equivalente
c. Projeção de Mercator
d. Projeção Azimutal Ortográfica 
e. Projeção Cilíndrica Conforme

O mapa de Mercator mantêm as formas, sendo uma mapa CONFORME.
O mapa de Peters mantêm as as áreas, sendo um mapa EQUIVALENTE. 
O enunciado nos diz que não conserva as formas nem áreas. Podemos assim, eliminar as alternativas 'a','b','c'.
Podendo ser a cilíndrica mas não é conforme porque para ser um mapa conforme precisa manter as formas. Não mantêm as áreas, portanto, não pode ser um mapa equivalente.
Sendo assim, sobra somente a altenativa 'D', uma projeção Azimutal Ortográfica.

Q1.(IBFC/2023/SEAD-GO)
Usando uma régua, um pesquisador mediu em um mapa uma distância de 14cm. 
A escala numérica do mapa mostrava 1:50.000. Diante dessas informações, assinale a alternativa que aponta a distância no terreno, de forma correta:

a. 700.000 cm
b. 7.000 cm
c. 70 km
d. 700 m
e. 700.000 m

1 cm -- 50.000 cm
14cm -- ???

14*50.000 = 700.000 cm 

LEGENDAS:

	As legendas são fundamentais em mapas, pois fornecem informações adicionais e auxiliam na interpretação correta das representações cartográficas.
Uma legendas é uma seção ou uma área específica do mapa que contém símbolos, cores, linhas, letras ou outras formas de representação gráfica acompanhadas
de textos descritivos. A principal função da legenda é fornecer uma chave de interpretação para os elementos simbólicos presentes no mapa. Ela ajuda a identifica
e compreende o significado dos símbolos presentes no mapa. Ela ajuda a identificar e compreender o significado dos símbolos cartográficos utilizados, como ícones
representando rios, áreas, estrada, pontos de interesse. Além disso, a legenda pode indicar a escala utilizada no mapa, infomações sobrre coordenadas geográficas,
unidades de medida e outra referências.

	Azul -> Hidrografia
	Cinza -> Urbano
	Vermelho -> Muito Elevado/quente
	Amarelo -> Elevado 
	Amarelo Claro -> Elevado Moderado
	Verde Claro -> Elevação Moderada
	Verde -> Elevação Baixa/ Vegetação

QUESTÃO 02.
Qual a função principal de uma legenda em um mapa?

a. Indicar a localização exata do ponto de interesse.
b. Mostrar a escala utilizada no mapa.
c. Fornecer informações adicionais sobre os elementos simbólicos do mapa
d. Apresentar coordenadas geográficas precisas
e. Identificar os limites políticos das regiões representadas.

a. NÃO. GPS ou coordenadas geográficas podem ser usadas.
b. NÃO. A escala é uma legenda mas não é uma resposta completa.
c. SIM. Informações adicionais sobre elementos simbólicos do mapa é uma resposta mais completa.
d. NÃO. 
e. Não somente políticos. Muito restrito.

CONVENÇÕES:

	Existe para facilita a representação cartográfica, foi criado um sistema de símbolos conhecidos como convenções cartogáficas. Os símbolos foram
escolhidos de forma a conter um ceto grau de compreensão e intuição de seu significado, possibilitando a leitura da informação contida no mapa por qualquer
pessoa em qualquer parte do mundo. Se agente quer representa uma área edificada, então usaremos esse símbolo, por exemplo. Se a equipe quiser representar
uma capital com uma bola e no fundo uma bola preta, então usaremos esse símbolo.

Questão 03. (CETREDE/2019/Prefeitura de São Gonçalo do Amarante)
Qual seria a escala numérica da mesma?

0    50  100  150
|____|____|____|

a. 1: 150.000
b. 1: 1.500.000
c. 1: 50.000
d. 1: 5.000
e. 1: 500.000

1 --- ???
1 --- 50 metros ( 5.000 cm )

Na escala gráfica temos uma proporção de cada 1 metro equivale a 50 metros. Transformando em escala numérica temos que adicionar 3 000
de metro para centímetros adicionamos '000' zeros, então 50 metros é 5.000 cm.
Resposta 'D' em escala numérica.

Questão (VUNESP/2016/UNESP) A escala cartográfica define a proporcionalidade entre a superfície do terreno e sua representação no mapa,
podendo ser apresentada de modo gráfico ou numérico.
A escala numérica corresponder à escala gráfica apresentada é:

615   0   615   1230   1845km
|_____|____|_____|_______|

a. 1: 184500000
b. 1: 615000
c. 1: 1845000
d. 1: 123000000
e  1: 61500000

1 --- 615KM
1 --- ???CM

(KM para CM, adicione 5 números zeros '00.000') Sendo assim temos: 615.00.000. Alternativa 'E'

ou podemos fazer: 1 M ---> 100 cm //  1km ---> 1000 m // Sendo assim: 1km = 100.000 cm 

1 cm = 100.000 cm
615 cm = ??  ( = 61.500.000 cm )

Questão (INSTITUTO EXCELÊNCIA/2017/PREFEITURA_JUINA_MT)

A escala cartográfica tem duas formas de ser representada: a numérica e a gráfica. Assinale a alternativa CORRETA que define a representação numérica da escala.

a. É a mais comum e está presente quase sempre em mapas de pequena escala, ou seja, aqueles em que grandes superfícies do planeta estão representadas, por exemplo,
nos Atlas e mapas-múndi.
b. Está presente sempre em mapas de grande escala, ou seja, aqueles em que pequenos espaços está representados, por exemplo, nas plantas de casas, trilhas curtas
e mapas urbanos.
c. Facilita a medida direta de distâncias sobre o mapa e não exige uma régua ou qualquer outro instrumento, uma vez que a própria escala gráfica é uma medida
escalar que pode ser diretamente para o mapa, seja po um compasso ou por uma linha
d. Nenhuma das alternativas

Na alternativa 'A'. As escalas numéricas estão presente quase sempre em mapas de pequena escala. Afirmação mais completa sobre escalas numéricas.
Na alternativa 'B' temos escalas gráficas para representar melhor locais pequenos, mas também usa-se escala numérica de grande escala.
Na alternativa 'C' é uma escala gráfica.

Questão (VENESP/2016/UNESP) Num mapa de escala gráfica representado por 1:20.000.000, a capital São Luiz se distancia 7 cm da capital baiana.
Qual é a distância real em linha reta entre as duas capitais?

a. 140km
b. 285,7km
c. 310km
d. 1400km

1cm = 20.000.000 cm
7cm = ????? cm

20*7 = 140.000.000 cm ( Converção para KM, retirar 5 zeros '00000' = 1400km )

Portanto, a afirmativa correta é a 'D'. A distância real entre as duas cidades é de 1.400 km.

Questão (??) Em um mapa na escala 1:250.000, a distância de 125 km entre duas cidades será de

• A - 5 cm.
• B - 10 cm.
• C - 20 cm.
• D - 40 cm.
• E - 50 cm.

1 cm = 250.000 cm para km (retirar 5 zeros)= 2,5km
1 cm  = 2,5 km
?? cm = 125 km
50 cm = 125 km

125/2.5 = 50 cm

Alternativa 'E'

Q1.(CEBRASPE) Na representação de determinada superfície terrestre no plano, é necessário adotar uma superfície que sirva de referência, garantindo
uma concordância das coordenadas na superfície esférica da Terra. Na situação em que as coordenadas referidas a um determinado sistema de referência
geodésico são representadas no plano adotando-se a figura geométrica elipsoide e as coordenadas referidas a ele são denominadas latitude e longitude,
tem-se o sistema de coordenadas:

a. Tranversais
b. Cartesianas
c. ortogonais
d. geodésicas
e. planas

a. ERRADO. 'transversais' é um termo que aparece em projeções cartográficas em mapas. Não são um sistema usado em geodésia.
b. ERRADO. O sistema cartesiano usa x,y,zw em relação a um ponto de origem. É usado em cálculos geodésicos sim, mas em coordenadas UTM.
Não correspondem as coordenadas latitude e longitude, que são angulares.
c. ERRADO
d. CORRETO
e. As coordenadas planas são obtidas por projeções cartográficas como UTM, em que a superfície curva da Terra é projetada em um plano,
dadas em metros com os eixos x,y. Não em graus de latitude e longitude.
Alternativa correta: 'D'

Q2.(FUNDATEC) Um casal, ao resolver marcar junto, decide comprar uma casa em Criciúma. Para isso, eles buscam por toda a cidade uma residência
em que a frente do imóvel receba diretamente a luz solar no turno da manhã e o quintal ( fundo da casa ) receba diretamente essa iluminação natural
(luz do sul) durante o período da tarde. Das casas apresentadas na imagem acima, qual preenche corretamente os requisitos?

 A imagem, a rosa dos ventos está inversa. O sol nasce no leste, se põe a OESTE. Portanto, a casa em que recebe a luz de frente é LESTE, a esquerda.
porque a rosa dos ventos está inversa. E no fundo, a luz do sol se pondo, OESTE. DIREITA ( porque a rosa dos ventos está INVERSA)
Portanto, casa 04. 

Q3.(FUNCERN) O instituto Brasileiro de Geografia e estatistica (IBGE) define uma escala cartográfica como a proporção entre a superfície terrestre e
sua representação. As escalas são definidas de acordo com o que estará sendo representado nos mapas e podem ser maiores ou menores, conforme o nível de
detalhamento necessário. Sendo assim, uma escala de:

a. 1:7.000 é maior que a escala 1:40.000 e apresenta mais detalhes da superfície representada.
b. 1:7.000 é menor que a escala de 1:40.000 e apresenta menos detalhes da superfície representada
c. 1:7.000 é menor que a escala 1:40.000, sendo utilizada para representar áreas menores, como, por exemplo, em cartas cartográficas.
d. 1:7.000 é maior que a escala 1:40.000, sendo utilizada para representar áreas mais extensas, como, por exemplo, em mapas de representação do globo.

a. CORRETO
b. INCORRETO  A escala 1:7.000 não é menor
c. INCORRETO  A escala 1:7.000 não é menor, mas o restante está correto.
d. INCORRETO. A escala 1:7.000 é maior sim, mas não é utilizada para áreas extensas.

Q4. Considerando a divisão do planeta em hemisférios Oeste e Leste, através da linha imaginária disposta verticalmente sobre o globo terrestre,
o Brasil está totalmente inserido a Oeste do ______. Com base nele calculamos os fusos horários.

a. trópico de capricornio
b. tropico de cancer
c. meridiano de greenwich
d. linha do equador

c. Meridiano de greenwich, onde temos as longitudes, com linhas imaginárias verticais com referência ao meridiano que variam de 0° a 180º de leste a Oeste.

Q5. (MPE-GO)Assinale a alternativa incorreta quantos aos pontos contidos na rosa dos ventos:

a. Os pontos cardeais são pontos de orientação no espaço terrestre os quais estão relacionados com a posição do sol
b. Os pontos cardeais assim são chamados porque são os melhores indicadores de direção. O nome cardeal é originado do latim 'cardinalis', que significa
'principal' ou 'essencial'. Em inglês, cardinal points. Essas orientações geográficas são separadas por um ângulo de 90°. A melhor maneira de se orientar
é sabendo onde o sol nasce e onde se põe, leste e oeste, respectivamente.
c. O ponto cardeal Nordeste (NE) existe para indicar a região que fica no meio entre o Norte e o Leste.
d. A rosa dos ventos ou rosa náutica é uma representação dos pontos cardeais, colaterais e subcolaterais que geralmente aparece em bússolas, em mapas,
plantas, croquis e em espaços públicos para orientação dos pedestres.

a. CORRETA
b. CORRETA
c. INCORRETA. O ponto Nordeste é colateral e não cardeal.
d. CORRETA


Q6.(CONSULPLAN) Para que não houvesse o risco de ficar sem acesso à internet e, consequentemente, sem um mapa, um dos membros da família comprou um mapa
da cidade com os principais pontos turísticos, hotéis e restaurantes, com escala 1:250.000, para que a família se localizasse na cidade enquanto estivesse
por lá. Se a distância entre o ponto turístico a ser visitado e o restaurante for 2 centímetros, a distância real entre estes dois pontos é de:

a. 0,05 km
b. 0,5 km
c. 5,0 km
d. 50,0 km

1 cm : 2,5 km
2 cm : ???

2,5 x 2 = 5,0 km Alternativa 'C'

Q7.(SELECON) Um grupo de pesquisadores do IBGE foi convidado para mapear um trajeto que, em um mapa de escala cartográfica 1:300.000, mede 3cm.
A distância real do trajeto é de:

a. 7 km
b. 9 km
c. 12 km
d. 15 km
e. 21 km

1 cm : 3 km
3 cm : ?? km

3x3 = 9 KM Alternativa 'B'

Q8(SELECON) Com base nas coordenadas geográficas contidas no mapa, Brasília está localizada nos hemisférios:

a. Setentrional e Ocidental
b. Meridional e Ocidental
c. Setentrional e Oriental
d. Meridional e Oriental
e. Ocidental e Oriental

Brasília está no hemisfério Meridional ( ao sul ) e Ocidental ( OESTE ) Alternativa 'B'

Oriental é LESTE e Setentrional é ao NORTE.

Q9(SELECON) Trata-se de uma projeção conforme, caracterizada pela conservação das formas dos territórios e distorção de seus tamanhos, principalmente
daqueles países situados mais distantes da Linha do Equador. Os paralelos e meridianos consistem em linhas retas que se cruzam e formas ângulos retos.
Ela é até hoje empregada no desenvolvimento de cartas náuticas, que são utilizadas nas navegações.

a. cônica
b. azimutal
c. cilíndrica de Peters
d. cilíndrica de Marcator
e. cilíndrica de Robinson

a. ERRADO. Usada em regiões de médias latitudes e não preserva formas globais.
b. ERRADO. Azimutal é usada para representar áreas a partir de um ponto central. ( polos )
c. ERRADO. A de Peters é EQUIVALENTE, preserva áreas e não é conforme.
d. CORRETO. A de Marcator preserva formas dos territórios mas distorce os tamanhos, especialmente em altas latitude.
Os paralelos e meridianos se cruzam em linhas retas com angulos de 90° e é usado em navegações.
e. ERRADO. A de Robinson é uma projeção de compromisso, nem conforme e nem equivalente
 

            '''            
    def geodesia(self):
        return '''
            [blue]Aqui vai o conteúdo dos exercícios 4.[reset]
            Geodésia é a ciência que estuda a forma e as dimensões da Terra, bem como a determinação precisa das posições na superfície terrestre.

Noções básicas de geodésia:
Formas da terra:

	Diversos modelos foram adotados ao longo da história. Não existe modelo errado, tudo depende do contexto histórico e da aplicação.
	Assim, o primeiro modelo é chamado de geoidal, é o mais aproximado da forma real, podendo ser determinado pelas medidas gravimétricas, 
ou seja, medidas da força da gravidade, explicado a seguir. O geoide não pode ser definido matematicamente pois é afetado pelas variações da densidade dos
elementos constituintes da crosta terrestre. Além da distribuição irregular das massas terrestres e oceânicas.
	Devido às irregularidades da superfície terrestre, utilizam-se modelos para a sua representação, mais simples, outros regulares e geométricos e que se
aproximam da forma real para efetuar os cálculos. Cada modelo tem a sua aplicação e quanto mais complexa a figura empregada para a representação da Terra,
mais complexo serão os cálculos sobre esta superfície. A forma da Terra gira em torno do seu eixo e movendo-se dentro do sistema solar. E o resultado da interação
de forças internas e externas tais como: gravidade, força centrífuga e a constituição diferente dos materiais que a formam a geoide ao longo de milhares de anos.
As forças tectônicas provocam modificações na superfície, que se traduzem por irregularidades topográficas, sobre as quais são realizados os mapeamentos, 
medições e estudos das mais variedades.

Geoide:

	É a forma física real, que sofre frequentes alterações devido a natureza (campo gravitacional do planeta terra, movimentos tectônicos, condições climáticas,
erosões, etc) e à ação do homem, portanto, não serve para definir forma sistemática da Terra. Portanto, a zona de contato da superfície terrestre topográfica e
o geoide que defini-se o nível zero das altitudes. Em resumo, a força gravitacional age sobre a terra vão definir a forma irregular do planeta. O equilíbrio
desse potencial gravitacional é o que gera a forma física da Terra. Mantendo os oceanos e a divisão dos continentes mantendo uma relação de equilíbrio do planeta.
	Portanto, o geoide é a superfície equipotencial gravitacional que mais se aproxima da superfície formada pelo prolongamento dos oceanos (nível médio dos mares)
sob os continentes. Essa supefície sofre variações conforme ocorrem alterações no campo gravitacional terrestre e, portanto, não segue leis matemáticas que permitam
um modelamento da Terra. Ainda assim é empregado como referência para a determinação das altitudes. 

	A Gravimetria é um método de medida da gravidade em divesos pontos distribuidos do planeta Terra. Para que apartir dessas medições se alcançem um modelo
de ação gravitacional equilibrado. Portanto, a Gravimetria é um método da Geodésia física que determina os níveis do campo gravitacional da Terra e, com isto,
determinar o geoide. A densidade de pontos é muito importante para a determinação do geoide. Quanto mais pontos de medição gravimétrica existirem na superfície 
terrestre, mais precisa é aquela figura geoidal.

	A incidência nos pontos gravitacionais é perpendicular a superfície da terra deverá ser ortométrica (distância contada sobre a vertical)
Pelas altitudes ortométricas (ângulo reto) a ação da gravidade nesses pontos é que teremos a determinação de uma superficíe equipontencial. Essa superfície
equipotencial é chamada de um modelo geoide.

Em média, coincide com o valor médio do nível médio das águas do mar, por isso é usado para medições
de altitudes  (altimetria). A superfície geoidal é mais irregular que qualquer outra superfície. A superfície varia entre os +8.850 m (Monte Everest) e -11.000m 
(Fossa das Marianas). O geoide varia apenas cerca de +-100 m além das superfície do elipsoide de referência.

	Modelo Elipsoide
Como o geoide é uma superfície matematicamente indefinida, as reduções ou transferências de dados a ele são inconsistentes, e para um mapeamento preciso de 
grandes áreas é necessária a consideração de uma figura geométrica regular. Assim, chega-se na figura matematicamente definida como um elipsoide.
A elipsoide é a representação matemática mais próximas da forma da Terra. Esse método é utilizado para GNSS e Geodésia Celeste, inclusive. (tecnologias novas)

O modelo Elipsoide de revolução é o nome que se dá a uma figura gerada pela rotação de uma elipse sobre um de seus eixos(de norte a sul da esfera). Eixo polar (Norte e Sul) 
é menor do que o eixo equatorial ( horizontal ) que por sua vez também possui semi-eixo. A relação entre o semi-eixo maior (equatorial) e o semi-eixo menor (polar)
é o que define a chamada excêntricidade em que ocorre o achatamento da elipsoide. A posição deste elipsoide em relação à Terra, bem como sua forma e tamanho,
constituem um conjunto de parâmetros definidos a partir do elipsoide ao seu ajustamento com a geoide onde são usualmente denominados Datum Geodésico. 
Uma elipsoide de revolução pode ser determinado para melhor se adaptar a uma região, país ou continente, evitando a ocorrência de desníveis geoidais muito exagerados.
Em geral, cada país adotou um elipsoide como referência para os trabalhos geodésicos e topográficos. Atualmente existem pelo menos 50 elipsoides existentes
utilizados pelo mundo, sendo alguns mais conhecidos: SAD-69, WGS-84, SIRGA-2000. 
Essas siglas, sempre encontradas no mapas, são elipsoides de revolução. Elas ilustram a referência utilizada para usar em trabalhos cartográficos.
Sendo assim, a superfície elipsoidal, que é obtido a partir do elipsoide de revolução, é uma figura matemática constante. Então, cada país ou região, para estudos
de mapeamento, por exemplo, é estabelecer qual é o elipsoide de referência para o mapeamento naquele local.

	O semi-eixo do WGS 1984 possui um eixo equatorial, em metros, 6.378.137. O eixo polar possui, em metros, 6.356.752.3142.
Foram usados equipamentos novos como GPS, GNSS, RTK para o datum WGS 1984.

DATUM:

	A posição do elipsoide em relação a terra, bem como sua forma e tamanho, constituem um conjunto de parâmetros que são usualmente denominados de DATUM
GEODÉSICOS. Datum corresponde a um ponto ou plano de referência para levantamento verticais e horizontais, os quais estabelecem as posições de feições sobre
a terra.

DATUM PLANIMÉTRRICO:

	É o ponto em uma região de melhor coincidência do elipsoide de referência ao geoide, onde o desvio da vertical é nulo ou mínimo. O conhecimento do
desvio da vertical é importante para a escolha do datum planimétrico do sistema geodésico de apoio ao levantamento cartográfico de um país.
	Nos referenciais clássicos a determinação do ponto de origem (topocêntrico) se da pelo relacionamento entre coordenadas geodésicas e astronômicas
utilizando as condições de La Place: 

		 Ψa - Ψg = e (componente meridiana)
		(λa-λg).cos(g) = η (componente 1° vertical)	

No ponto de origem do sistema eram realizadas medidas astronômicas para determinar latitude, longitude e azimute astronômico o qual se 
determinava as coordenadas geodésicas de partidade para o referencial.

DATUM ALTIMÉTRICO:

	Ponto fixo fundamentado e solidamente materializado, cuja altitude sobre o nível do mar é utilizado como partida de referência das altitudes que
determinam os nivelamentos.

SISTEMA GEODÉSICO DE REFERÊNCIA:

	SGR são estruturas constituídas por estações geodédicas materializadas na superfície terrestre, com coordenadas que servem de referência para os
levantamentos topográficos e geodésicos a serem realizados no território de interesse. Isso, constitui-se a infra-estrutura de referência para novos
posicionamentos a serem efetuados. No Brasil, o órgão responsável em estabelecer esses sistemas de referência é o IBGE.

	REDES de sistema geodésico de referência ALTIMÉTRICO E PLANIMÉTRICO:

O sistema geodésico de referência brasileira possui milhares de redes altimétricas ou verticais. As 'RRNN' são as referências de nível, onde os pontos cuja a altitude 
ao nível do mar é conhecida. Para uso de mapas topográficos, é utilizado o método ortométrico, em que calcula a distância entre o geoide até a superfície terrestre,
denominada 'H'. Além disso, temos a altitude elipsoidal 'h', sendo a altitude da elipsoide de revolução até a superfície terrestre, as medições são feitas com GPS.
E o 'N' é a ondulação geoidal, entre o geoide e o elipsoide. Sendo assim, temos a fórmula para obter a altitude ortométrica: 'H ≅ h + N'
O datum altimétrico usado no Brasil oficial é o Marégrafo de Imbituba/SC, desde 1958.

	O datum planimétrico ou horizontal é definido como a forma e tamanho de um elipsoide, bem como sua posição relativa ao geoide. Cada país adota um elipsoide
como referência, o qual se aproxima do geoide da região considerada. O Brasil adota o elipsoide do Sistema Geodésico de Referência de 1980. (GRS80)
A adoção de um referencial topocêntrico, onde o ponto de origem e orientação está na superfície terrestre e não no centro da terra.

Com a evolução nas tecnologias, houve reajuste no SAD69(1996). Com o advento do SIRGAR 2000 a definição/orientação do SIRGAS2000 é geocêntrica: adota um referencial
que tem a origem dos seus três eixos cartesianos localizada no centro de massa da Terra. Parecido com o WGS84, é internacional.  Adota o mesmo sistema geodésico de 
referência, geocêntrico também, e tem o objetivo de fornecer posicionamento e navegação em qualquer parte do mundo. O Google Earth utilizada o datum WGS84.

	A rede planimétrica clássica, onde possui também, milhares de redes, são compostos por vértices de triangulação em que devem ser intervisíveis. 
Usado muito até os anos 90 até implantarem as estações GNSS. Hoje em dia, o Brasil também possui uma rede de monitoramento contínuo dos sistemas GNSS em vários
pontos do Brasil.

	Os sistema geodésico brasileiro era planimétrica clássica, o SAD 69 (South American Datum 1969), o modelo da Terra era o elipsóide internacional de 1967 (GRS 67)
Sua origem era topocêntrica com vértice de Chuá. 

Hoje o sistema de referência é geocêntrico para as Américas, SIRGA2000, usado o modelo geoide, um elipsoide 
internacional de 1980 (GRS 80), a sua origem era o centro da massa da Terra (Elipsoide Geocêntrico)

As três superfícies da Geodésia:

A superfície verdadeira (superfície equipotencial de referência): geoide (datum vertical);
A superfície matemática: elipsoide (datum horizontal e referência vertical); 
A superfície física: terrestre (onde são realizadas as medições). 

Onde temos :

'h': altitude geométrica (elipsoidal) cuja distância vertical medida sobre a normal (perpendicular ao elipsoide) entre o ponto medido e uma superfície de
referência elipsoidal.
'H': altitude ortométrica (geoidal) cuja distância é medida da geoide ou nível do mar até a superfície física, independe do elipsoide de referência e tem 
seu maior significado físico.
'N': a ondulação gravitacional geoidal cuja distância entre a superfície geoidal (verdadeira) à superfície elipsoidal de referência, perpendicular sobre
um segmento de reta entre os pontos.

SISTEMAS GEODÉSICOS REGIONAIS

	Os sistemas geodésicos regionais é um referencial adaptado a uma região (país ou continente) devido à limitação dos métodos de posicionamento utilizado.
Permite a possibilidade de existência de mais de um sistema de referência em cada região ou país. Por exemplo: Chuá-Astro Datum, South American Datum 1969 (SAD69)
e Córrego Alegre.

SISTEMA GEODÉSICO GLOBAL

	
	O advento dos satélites artificiais para posicionamento possibilitou o desenvolvimento prático dos sistemas de referência geocêntricos, como 
por exemplo, o WGS84 e o ITRS (International Terrestrial Reference System) em suas mais diversas realizações e densificações.
	O ITRS2000 é uma densificação e deu origem ao sistema SIRGAS2000, sendo ambos compatíveis entre os sistemas. Possuem as mesmas características.
	Os sistemas geodésico global são adequados às modernas técnicas de posicionamento, possibilitando levantamentos globais. Como exemplo pode-se destacar
os sistemas globais de navegação por Satélite (GNSS - Global Navigation Satellite System). A origem do sistema é o centro de massa da Terra ( geocêntrico )
Exemplos são: World Geodetic System 1984 - WGS84; Internacional Terrestrial Reference System - ITRS e o Sistema de Referência Geocêntrico para as Américas
-SIRGAS 2000.

International Terrestrial Reference System (ITRS):
	
	O ITRS é um sistema de referência moderno que define matematicamente como representar posições na Terra.
Ele rotaciona com a Terra em seu movimento no espaço. Cada realização do ITRS é especificada em coordenadas cartesianas X,Y e Z.

	- Eixo Z aponta na direção do CTP( Conventional Terristrial Pole = Polo Norte Terrestre Convencional)
	- Eixo X aponta para a direção média do meridiano de Greenwich
	- Eixo Y aponta para o leste, perpendicular ao eixo X 

O ITRS é realizado a partir de um conjunto de coordenadas e velocidades observadas por GNSS,LLR, GPS, SLR, VLBI e DORIS. 
Cada realização é denominada de International Terrestrial Reference Frame (ITRF), na prática + ano de realização.
É atualizado periodicamente (2000,2008,2014,2020...)
Em resumo, os posicionamentos GNSS modernos estão, na prática, referidos ao ITRS/ITRF.

	Os ITRS são importantes para mapas globais, referência de posicionamento preciso e controle de placas tectônicas.
Eles monitoram a elevação do nível do mar, mudanças climáticas e deformações na terra.

SIRGAS 2000

	Em 25 de fevereiro de 2015 o SIRGAS 2000 foi adotado, em definitivo, como referencial geodésico oficial no Brasil. Os parêmetros são detalhados abaixo:

	1. Época de referência: 2000,4
	2. Elipsoide: GRS80
	3. Semi-eixo maior: 6.378.137 m
	4. Achatamento: 1/298,257222101
	5. Origem: Centro de Massa da Terra

Atualmente o sistema WGS84 é compatível com o SIRGAS 2000

SISTEMA GEODÉSICO BRASILEIRO:

O sistema Geodésico Brasileiro adotou oficialmente 3 referênciais:

	Córrego Alegre; SAD69; SIRGA2000

Sistemas de referência geodésico usados no Brasil:

Córrego Alegre (1911): Ajustamento da rede planimétrica na década de 40
- Época de Referência: 1911
- Elipsoide: Hayford (Internacional 1924)
- Semi-eixo maior: a = 6.378.388 m
- Achatamento: f = 1/297
- Origem: Ajustado a observações astronômicas locais no Brasil ( topocêntrico )
- Ondulação geoidal: N = 0
- Observação: Foi o primeiro sistema oficial, usado até os anos 1970.
- Coordenadas do ponto de origem:
	A = 19"50'15,14"s e B = 48"57'42,75"W

Os componentes de desvio da vertical foram nulas, dessa forma a normal e a vertical são coincidentes nesse ponto, sendo assim, o elipsoide
é paralelo ao geoide no vértice Córrego Alegre. A ondulação geoidal também é nula, fazendo com que o elipsoide seja coindidente com o geoide
no ponto origem. As realizações do CA foram nos anos de 1961,1970 e 1972. Para fins de transformações de coordenadas, portanto podem ser
agrupadas em uma única realização. Sendo as realizações dos anos 70 estatisticamente iguais.

2. Astro Datum Chuá (1961)
- Época de Referência: 1961
- Elipsoide: Internacional 1924
	- Semieixo maior: 6.378.388 m
	- Achatamento: 1/297
- Origem: Ajustado a observações astronômicas na região de Chuá (MG) -> Topocêntrico
- Observação: Teve uso limitado e regional, principalmente em Minas Gerais. NÃO FOI OFICIALMENTE USADO, FOI TIDO COMO UM ENSAIO PARA O SAD69.

3. SAD69 (South American Datum 1969) : Foi adotado oficialmente no Brasil em 1977 em susbtituição ao Córrego Alegre.
- Época de Referência: 1969
- Elipsoide: Internacional 1967
	- Semieixo maior: a = 6.378.160 m (menor do que CA)
	- Achatamento: f = 1/298,25 (menor que CA)
- Origem: Posicionado astronômico no vértice de Chuá (MG). Ajustado ao continente sul-americano (topocêntrico)
- Observação: Foi o sistema oficial do Brasil de 1979 até 2015, amplamente usado em cartografia.
- Ondulação geoidal: N = 0
- Coordenadas do ponto de origem:

	A(latitude astronômica) = 19"45'41,34"S e B(longitude astronômica) = 48"06'07,80"W
	A(astro-geodésico) = 19"45'41,6527"S  e   B(longitude astro-geodésica) = 48"06'04,0639"W  ( desvio da vertical )
	AZA = 271"30'05,42" e AZ = 271"30'04,05"

Os componentes de desvio da vertical do datum SAD69 foram determinados por métodos astro-geodésicos como:
componente meridiana ξ= 0,31" e η (componente vertical)η = -3,52" de arco. 

Sendo assim, o ponto da geoide com a elipsoide não são paralelos em função do desvio da vertical.

As realizações foram ocorridas na décadas de 70, cobrindo grande parte do território brasileiro com dados GPS e TRANSIT. Proporcionando um custo menor
e rapidez nos levantamentos. Oferecendo uma melhor qualidade geométrica com novas tecnologias sendo realizado o SAD69/96.

ξΨψωη

ζ= 0,31 ξΨψωη

4. WGS84 (World Geodetic System 1984)
- Época de Referência: 1984 (atualizações periódicas)
- Elipsoide: WGS84
- Semieixo maior: 6.378.137 m
- Achatamento: 1/298,257223563
- Origem: Centro de Massa da Terra (geocêntrico)
- Observação: Sistema global usado pelo GPS; compatível com o SIRGAS2000.

5. SIRGAS2000 (Sistema de Referência Geocêntrico para as Américas, adotado em 2015): Foi adotado com a motivação de um referencial único para o 
continente Sul-americano com técnicas modernas com 67 estações distribuídas em 11 países da América do Sul. Posteriormente, o projeto SIRGAS foi
expandido para a América Central, do Norte e Caribe. A segunda realização da rede continental ocorreu em maio de 2000 contando com 184 estações
estabelecidas em países das três Américas, sendo 21 delas localizadas no Brasil. Atualmente, o SIRGAS está materializado por uma rede de estações
GNSS de monitoramente contínuo (SIRGAS-CON) formada por cerca de 400 estações.
- Época de Referência: 2000,4
- Elipsoide: GRS80
- Semieixo maior: a = 6.378.137 m
- Achatamento: f = 1/298,257222101
- Origem: Centro de Massa da Terra (Geocêntrico)
- Observação: Sistema oficial do Brasil desde 25/02/2015; compatível com WGS84.
- Estações de referência: redes planimétricas em 21 etações da rede continental SIRGAS2000.

Assim, a evolução foi: Córrego Alegre → Astro Datum Chuá → SAD69 → WGS84 → SIRGAS2000.


'''

    def exercicios_geodesia(self):
        return '''
QUESTÕES – ITRS / ITRF / SISTEMA GEODÉSICO GLOBAL
1. (CESPE)

O ITRS é um sistema de referência geodésico global que possui origem no centro de massa da Terra, orientado pelo meridiano de Greenwich e pelo polo norte geográfico.

Certo ou Errado?

CERTO

2. (FGV) O ITRF representa:

a) O elipsoide utilizado pelos sistemas GNSS.
b) A materialização prática do ITRS em uma época e com coordenadas de estações.
c) O modelo geoidal adotado para nivelamento.
d) O datum vertical global.

Alternativa 'B'

3. (CESPE) O ITRF é atualizado regularmente devido a movimentos tectônicos da crosta terrestre, marés e deformações continentais.

Certo ou Errado?

CERTO

4. (IBGE) Sobre o ITRS, assinale a alternativa correta:

a) É um sistema bidimensional baseado em latitudes geocêntricas.
b) É definido com origem na superfície do elipsoide de referência.
c) É tridimensional e geocêntrico, com origem no centro de massa da Terra.
d) É equivalente ao sistema UTM.

Alternativa 'C'

5. (ESA / Militar) O eixo Z do ITRS aponta para:

a) A interseção do Equador com o Meridiano de Greenwich
b) O polo norte geográfico
c) A direção do meridiano 180°
d) O centro do elipsoide WGS84

Alternativa 'B'

6. (CESGRANRIO) O WGS84, utilizado pelo GPS, nas versões mais recentes é alinhado com qual materialização do ITRS?

a) ITRF2000
b) ITRF2008
c) ITRF2014
d) Não é alinhado com o ITRF

Alternativa 'C'

7. (CESPE) O ITRS é considerado um sistema fixo à crosta terrestre, ignorando movimentos das placas tectônicas.

Certo ou Errado?

ERRADO.  

8. (FGV) Qual rede de observação NÃO contribui para a realização do ITRF?

a) VLBI
b) SLR
c) DORIS
d) NMEA

Alternativa 'D'

As redes que contribuem para o ITRF são:
- VLBI (Very Long Baseline Interferometry) → usa radiotelescópios para medir distâncias entre antenas.
- SLR (Satellite Laser Ranging) → mede distâncias até satélites usando pulsos de laser.
- DORIS (Doppler Orbitography and Radiopositioning Integrated by Satellite) → usa efeito Doppler para posicionamento.
- GNSS (Global Navigation Satellite Systems, como GPS, GLONASS, Galileo) → também contribuem.
Já o NMEA (National Marine Electronics Association) não é uma técnica de observação geodésica, mas sim um formato de protocolo de dados usado para transmitir informações de receptores GPS e outros equipamentos de navegação.


9. (IBGE) As diferenças entre WGS84 e ITRF2020, em suas versões atuais, são da ordem de:

a) Quilômetros
b) Metros
c) Milímetros
d) Não podem ser comparadas

Alternativa 'C'.
Diferenças entre WGS84 e ITRF2020
- O WGS84 (World Geodetic System 1984) é o sistema de referência global usado pelo GPS.
- O ITRF2020 (International Terrestrial Reference Frame 2020) é um sistema de referência mais preciso e atualizado, 
baseado em observações geodésicas modernas (VLBI, SLR, GNSS, DORIS).
- Ambos são sistemas globais de referência, e suas diferenças nas versões atuais são muito pequenas, da ordem de milímetros a poucos centímetros, 
devido às atualizações periódicas que mantêm o WGS84 alinhado ao ITRF.

20 Questões sobre o Sistema Geodésico Global – ITRS / ITRF
Questões de múltipla escolha

10. O ITRS é definido como um sistema de referência:

A) Inercial
B) Determinado por observações GNSS, SLR, VLBI e DORIS
C) Baseado apenas em coordenadas UTM
D) Exclusivo para a América do Sul

- A) Inercial ❌ Não. O ITRS é um sistema terrestre, não inercial.
- B) Determinado por observações GNSS, SLR, VLBI e DORIS ✅ Correto. Essas são exatamente as quatro técnicas que contribuem para a realização do ITRF, que materializa o ITRS.
- C) Baseado apenas em coordenadas UTM ❌ Não. UTM é apenas uma projeção cartográfica, não define o sistema de referência.
- D) Exclusivo para a América do Sul ❌ Não. O ITRS é global, válido para todo o planeta.


11. O ITRF representa:

A) O datum vertical global
B) O conjunto de realizações periódicas do ITRS
C) Um sistema de projeção cartográfica
D) Um modelo geoidal local

- A) O datum vertical global ❌ Não. O ITRF é horizontal e tridimensional, não apenas vertical.
- B) O conjunto de realizações periódicas do ITRS ✅ Correto. O ITRF representa justamente as realizações periódicas do ITRS.
- C) Um sistema de projeção cartográfica ❌ Não. Projeções cartográficas são outra coisa (ex.: UTM).
- D) Um modelo geoidal local ❌ Não. O geóide é um modelo físico da superfície equipotencial da Terra, não o ITRF.

12.A principal característica do ITRS é ser:

A) Fixo à crosta terrestre
B) Fixo ao centro de massa da Terra
C) Fixo ao centro geométrico da crosta continental
D) Dependente de marés oceânicas

Alternativa 'B'

- A) Fixo à crosta terrestre ❌ Não, pois considera toda a Terra, não apenas a crosta.
- B) Fixo ao centro de massa da Terra ✅ Correto. Essa é a definição fundamental do ITRS.
- C) Fixo ao centro geométrico da crosta continental ❌ Não, seria uma limitação incorreta.
- D) Dependente de marés oceânicas ❌ Não, marés não definem o sistema.

✅ Resposta correta: B – Fixo ao centro de massa da Terra


13.O ITRF é atualizado periodicamente porque:

A) Há necessidade de ajustar fusos UTM
B) A crosta terrestre é estática
C) A crosta terrestre se movimenta continuamente
D) O GNSS perde precisão após alguns anos

C – A crosta terrestre se movimenta continuamente.

- A) Há necessidade de ajustar fusos UTM ❌ Não tem relação com o ITRF.
- B) A crosta terrestre é estática ❌ Errado, justamente o contrário.
- C) A crosta terrestre se movimenta continuamente ✅ Correto. Essa é a razão da atualização periódica.
- D) O GNSS perde precisão após alguns anos ❌ GNSS continua funcionando, mas precisa ser alinhado ao sistema atualizado.


14. Um exemplo de realização do ITRS é:

A) WGS84
B) SAD69
C) ITRF2014
D) SIRGAS2000

ITRS e suas realizações
- O ITRS (International Terrestrial Reference System) é o sistema de referência terrestre internacional.
- Sua realização prática ocorre por meio do ITRF (International Terrestrial Reference Frame), que é atualizado periodicamente (ITRF2000, ITRF2008, ITRF2014, ITRF2020...).
- Portanto, um exemplo de realização do ITRS é justamente uma versão do ITRF.

- A) WGS84 ❌ É um sistema geodésico global usado pelo GPS, mas não é uma realização direta do ITRS.
- B) SAD69 ❌ É um datum geodésico antigo usado na América do Sul, não relacionado ao ITRS.
- C) ITRF2014 ✅ Correto. É uma das realizações oficiais do ITRS.
- D) SIRGAS2000 ❌ É um sistema de referência geodésico para a América do Sul, alinhado ao ITRF, mas não é uma realização oficial do ITRS.

✅ Resposta correta: C – ITRF2014


15.O ITRS define:

A) Apenas a orientação dos eixos
B) Apenas o elipsoide
C) Origem, escala e orientação
D) Apenas o datum vertical

O ITRS (International Terrestrial Reference System) é o sistema de referência terrestre internacional, mantido pelo IERS.
Sua definição inclui:
- Origem: no centro de massa da Terra (incluindo oceanos e atmosfera).
- Escala: coerente com medições físicas globais.
- Orientação: alinhada com o eixo de rotação da Terra e o plano equatorial.
Portanto, o ITRS não define apenas eixos, nem apenas o elipsoide, nem apenas datum vertical. Ele é mais completo.

Portanto, alternativa C

16.A origem do ITRS está localizada:

A) No centro geométrico da crosta
B) No centro de massa da Terra
C) No equador
D) No meridiano de Greenwich

Resposta mais certa seria a alternativa 'B', no centro da massa da terra.

17. A orientação dos eixos do ITRS segue:

A) A rotação da Terra
B) O sistema cartesiano clássico: X → equador/Greenwich, Y → 90ºE, Z → polo
C) O sistema UTM
D) A direção dos cinturões tectônicos

Alternativa 'B', sem dúvida.

18. O ITRF é obtido por:

A) Modelagem matemático-analítica sem observações
B) Ajustamento combinado de diversas técnicas espaciais
C) Única estação de rastreio GNSS
D) Observações apenas de satélites GPS

Alternativa 'B'

19. O ITRF2014 foi sucedido por:

A) ITRF2020
B) WGS90
C) SAD96
D) SIRGAS95

- A) ITRF2020 ✅ Correto. É a versão que sucedeu o ITRF2014.
- B) WGS90 ❌ Não existe como sistema oficial.
- C) SAD96 ❌ Datum sul-americano antigo, não relacionado ao ITRF.
- D) SIRGAS95 ❌ Sistema de referência geodésico da América do Sul, mas não é sucessor do ITRF.

'''

    def geoprocessamento(self):
        return '''

GEOPROCESSAMENTO 
	
	O SIG (Sistemas de informação geográfica) é a tecnologia que une a informação geográfica à informação descritiva. 
O SIG possibilita a capacidade de visualizar, manipular, analisar e transformar informações geográficas. Os componentes de um SIG existentes como as máquinas(hardware),
softwares (algortimos, scripts), banco de dados (dataware), pessoas qualificadas, dados (localização dos rios, territórios, matas) e 
métodos, procedimentos assim como, saber aplicar e transformar os dados em valor são o que definem o termo GEOPROCESSAMENTO.

1. Banco de dados geográficos / 2. Gerencia de dados espaciais / 3. Consulta e análise/visualização(plotagem)/Entrada/integração de dados/ 4. Interface
A aplicação de visualização de Web Services são: Google Earth/Open Street Maps/Waze. É um tipo de geoprocessamento que está vinculado ao consumo de dados.
Mas não permite fazer análises complexas.

	A estrutura do SIG é composta por CAMADAS. Todos os sotfwares, hoje em dia, são compostas por Layers. Cada camada, cada elemento da paisagem
representa várias informação. Cada camada, cada layers poderá ser alterado. Uma carta topográfica, por exemplo, todas as informações estão mapeadas em uma só
camada. No SIG, podemos ir além, aprofundar em cada camada. Existem 2 tipos de camadas (layers) no SIG. O vetor e o raster que podemos colocar em um SIG.
	O arquivo vetorial são todos os dados representados por pontos, linhas e áreas (polígono) Colocar atributos nos vetores. Um ponto vetorial pode ser 
uma árvore, uma casa. Agora um arquivo vetorial de linha poderia ser um rio, um córrego. Agora um tipo de vetor tipo área poderia ser um lago, um sítio.
	Os formatos de arquivos de layers vetoriais são os: shapefile(.shp) o mais universal. Podendo ser por tabelas (.tab) e o formatos CAD(.dwg;.dgn;.dfx)
Mas o específico para SIG é o SHAPEFILE.(.shp) O qual é formado por três arquivos, o ".shp", que indica a geometria, o '.dbf', que contém a tabela de atributos e o '.SHX', indexador de arquivo. ( que vai indexar o 'shp' ao 'dbf' )
Tendo esses três arquivos, qualquer softwares de processamento irá reconhecer. Salvando o arquivo completo, gera-se o arquivo '.prj'
Elementos do arquivo '.dbf':

	É uma tabela com colunas e as linhas com seus atributos. Um dos elementos serão uma coluna com os tipos de geometria e o valor da geometria.
Em termos de prova, o Google Earth não é um SIG. Os tipos de dados, além da geometria, podem vim: 'string' -> Dados textuais / 'Integer' -> Números inteiros
/ 'float/double' -> Números Decimais / 'byte' -> número inteiro de 6 bits (0 a 255) 

Os arquivos KML estão mais associados ao google earth , ( KML -> keyhole Markup Language ), o KMZ agrupa varios kmls dentro dele.
O formato é open source e agrega atributos de elementos, traz uma estrutura de metadados mas não funciona como tabela de banco de dados. (.db)
Interoperabilidade do arquivo permite usar em sofwares de SIG, ele é nativo do Google Earth. Mesmo podendo ser gerado por SIGs também.

	Os dados vetoriais representam geometrias que são pontos(marcadores de locais no espaço [par de coordenadas associado][sem dimensões, sem área], linhas e polígonos(áreas)
As linhas e polígonos possuem espaço. As linhas são unidimensionais (comprimento) e que permitem analises de ocupação no espaço.
	Os arquivos de RASTER é outro formato em que são imagens geradas por satélites, radares, foto aéreas. Só que para se tornar um RASTER, a imagem
deverá ser GEORREFERENCIADA a um sistema de coordenadas. Uma referência espacial. Sem essas informações, ela será uma simples imagem.
	Os formatos são: GeoTIFF(.tif) <- Geradas imagens por satélites // JPEG(.jpg) // bitmap(.bmp). O mais conhecido mesmo é o TIFF.
	Os dados a serem funcionais precisam ter uma referência espacial. Ou seja, são layers associados a sistemas de coordenadas e projeções cartográficas.
Justamente para medir distâncias, definir escalas, medir áreas. Sem referência espacial não há possibilidade de fazer análises no SIG.
Os valores numéricos dos arquivos raster são atribuidos aos Pixels em que permite a realização de operações aritméticas.
Os arquivos de dados 'raster' é composta por uma matriz contínua de dados com valores numéricos atribuídos aos Pixels.

Arquivos geopackage:

	São arquivos de código aberto (OPEN GEOSPATIAL CONSORTIUM) em que um único arquivo pode armazenar diversas camadas de dados espaciais e atributos.
Baseado em SQlite. Inclusive, 'raster'.
As coordenadas em que falamos são as coordenadas geográficas ( latitudes e longitudes (GMS) ) e as coordenadas planas ou cartesianas (UTM - Universal Transversa de Marcator )
As vantagens do SIG é centralizar as funções de gestão de banco de dados, CAD (desenho assistido por computador) (Computer Aided Design) e análises espaciais.
Além disso, relações topológicas e espaciais, relações matemáticas (relação de diferentes atributos, elementos geográficos) e geoestatística (correlação espacial)
	Com o SIG poderemos gerar mapas digitais e físicos. Medir as distâncias e áreas entre pontos, entre linhas e permite calcular áreas.
	Geração de bases cartográficas vetoriais como pontos ( cidades, municípios, parada de ônibus ), linhas ( rodovias, falhas geológicas, rios, córregos )
e áreas ( rios, lagos, florestas, lotes, limites de cidades e estados )
	O SIG também faz GEOPROCESSAMENTOS. Os dados poderão ser transformados em novas infomações. O geoprocessamento de dados vetoriais, por exemplo,
recorte, união, raios, extração de áreas. ( apagar um limite sobreposto a outro )
	Os dados matriciais, são os rasters. Em que podemos fazer álgebra de mapas e reclassificação. Ligado ao sensoriamento remoto.
	O SIG permite também fazer análises 3D. Visualizações trimensionais (MDE - Modelos digitais de elevação), imagens de satélites e fotos aéreas.
	Cálculos de volume ( cruzamento de área ) / Calcular as distâncias topográficas ( leva em consideração as deformidades do relevo )
	Gerenciamento de dados geográficos ( Consultas espaciais ( atributos dos dados -> Descrição dos dados geográficos ); consultas de localização
entre objetos de regiões. 
	Geração de simbologias ( Atribuis legendas, convenções Ex: prédios acima de 7 pavimentos, bairros acima de 1000 habitantes )

	Os softwares:

	Os softwares proprietários são pagos: ArcGIS e MaphInfo. (ESRI)
	Os softwares gratuito: SPRING  (INPE) [ voltado para o sensoriamento remoto ]
	Os softwares livres: alterar códigos e colaborativo (plugins [python]( QGIS e gvSIG ) <- EMBRAPA, INCRA (FOSS)
	

            '''
    def exercicios_geo_proc(self):
        return'''
Questões de GEOPROCESSAMENTO:

Q1. Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - IPHAN - Geoprocessamento - 2025
O desenvolvimento tecnológico das aeronaves remotamente pilotadas e dos sensores que podem ser nelas embarcados permitiu aprimorar processos que, antes, 
eram executados empregando aeronaves de grande porte e imagens de satélite.
Assinale a opção que apresenta uma desvantagem do emprego de drones no planejamento da recuperação de áreas degradadas em decorrência de um deslizamento de terra, em comparação com as imagens de satélite.

A.Ausência de nuvens.
B.Estabilidade da plataforma.
C.Flexibilidade na captura de dados.
D.Geração de modelos tridimensionais de alta precisão.
E.Resolução espacial.


B) Estabilidade da plataforma.

Explicação:

Estabilidade da plataforma: Aeronaves de grande porte e satélites geralmente operam em altitudes elevadas e são projetados para manter uma estabilidade considerável durante a aquisição de imagens. Isso minimiza distorções geométricas nas imagens, facilitando a sua georreferenciação e análise precisa. Drones, especialmente os de menor porte, podem ser mais suscetíveis a ventos e turbulências em baixas altitudes, o que pode comprometer a estabilidade da plataforma de imageamento e gerar imagens com maior distorção geométrica, dificultando a criação de mosaicos precisos e modelos 3D confiáveis para o planejamento da recuperação.
Vamos analisar as outras opções para entender por que não são desvantagens dos drones em comparação com satélites para essa aplicação específica:

A) Ausência de nuvens: Esta é geralmente uma vantagem dos drones. Eles podem voar abaixo da cobertura de nuvens, enquanto as imagens de satélite podem ser obscurecidas por elas.
C) Flexibilidade na captura de dados: Drones oferecem muito mais flexibilidade em termos de horários de voo, ângulos de captura e revisitas à área, o que é uma grande vantagem em relação à órbita fixa dos satélites.
D) Geração de modelos tridimensionais de alta precisão: Drones, com o uso de técnicas fotogramétricas, são capazes de gerar modelos 3D de altíssima resolução e precisão, frequentemente superiores aos modelos derivados de imagens de satélite.
E) Resolução espacial: Drones operam em altitudes mais baixas, permitindo a captura de imagens com resolução espacial muito superior às imagens de satélite, o que é crucial para o detalhamento necessário no planejamento da recuperação de áreas degradadas.

Q2. Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de Canaã dos Carajás - Agente de Serviços Técnicos Ambientais - 2025
Com relação aos tipos de dados em Geoprocessamento, analise as afirmativas a seguir e assinale (V) para a verdadeira e (F) para a falsa.

( ) Os dados temáticos admitem tanto representação matricial quanto vetorial; são dados referentes à temática a ser abordada no Sistemas de Informações Geográficas (SIG), podendo ser dados estatísticos, de vegetação, de uso do solo, de geologia, entre outros.
( ) Os modelos digitais de elevação (MDE) representam as altitudes da superfície topográfica agregada aos elementos geográficos existentes sobre ela, como cobertura vegetal e edificações.
( ) As imagens de sensoriamento remoto admitem tanto representação matricial quanto vetorial; são dados referentes à temática a ser abordada no SIG, podendo ser dados estatísticos, de vegetação, de uso do solo, de geologia, entre outros.

As afirmativas são, respectivamente,

A. F – V – F.
B. F – V – V.
C. V – F – F.
D. V – V – F.
E. F – F – V.

Gabarito Correto: Alternativa D - V, V, F
Vamos analisar cada uma das afirmativas para entender o porquê dessa escolha:

1. Primeira Afirmativa: "Os dados temáticos admitem tanto representação matricial quanto vetorial; são dados referentes à temática a ser abordada no Sistemas de Informações Geográficas (SIG), podendo ser dados estatísticos, de vegetação, de uso do solo, de geologia, entre outros."
Essa afirmativa é verdadeira. Os dados temáticos em Geoprocessamento são informações espaciais que podem ser representadas tanto na forma matricial (raster) quanto vetorial. Eles são usados para representar diferentes temas ou camadas de informações no SIG, como vegetação, uso do solo, entre outros. Essa flexibilidade permite integrar diversas fontes de dados para análise geoespacial.
2. Segunda Afirmativa: "Os modelos digitais de elevação (MDE) representam as altitudes da superfície topográfica agregada aos elementos geográficos existentes sobre ela, como cobertura vegetal e edificações."
Essa afirmativa é verdadeira. Os modelos digitais de elevação (MDE) são usados para representar a elevação do terreno. Eles geralmente incluem informações sobre a superfície topográfica, mas não integram automaticamente elementos como cobertura vegetal ou edificações. Entretanto, o enunciado sugere uma agregação que é comumente representada em modelos mais complexos, como o Modelo Digital de Superfície (MDS). A compreensão correta do termo aqui é fundamental.
3. Terceira Afirmativa: "As imagens de sensoriamento remoto admitem tanto representação matricial quanto vetorial; são dados referentes à temática a ser abordada no SIG, podendo ser dados estatísticos, de vegetação, de uso do solo, de geologia, entre outros."
Essa afirmativa é falsa. As imagens de sensoriamento remoto são tipicamente representadas em formato matricial (raster) e não em formato vetorial. Elas capturam dados de áreas extensas e são essenciais para análises que requerem a avaliação de grandes superfícies, como imagens de satélite. Diferenciar entre tipos de representação é crucial para a correta interpretação e utilização dos dados no SIG.
Estratégia para Interpretação: Ao analisar questões de Geoprocessamento, lembre-se de distinguir entre formatos de dados (matricial x vetorial) e entender o contexto de aplicação de cada tipo de dado. Sempre busque verificar se há pegadinhas relacionadas à terminologia técnica.

Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IPHAN - Geoprocessamento - 2025
O Geoprocessamento permite a extração de informações valiosas a partir de diferentes conjuntos de dados geográficos. 
Considere os seguintes produtos relacionados ao contexto do licenciamento ambiental.

I. Os mapas de localização de empreendimentos.
II. Os modelos de dispersão de poluentes atmosféricos.
III. A sobreposição de dados temáticos para análise de vulnerabilidade ambiental.

Empregando apenas técnicas de geoprocessamento, está correto o que se afirma em

A. I, apenas.
B. I e II, apenas.
C. I e III, apenas.
D. II e III, apenas.
E. I, II e III.

Fundamentação: Modelos de dispersão de poluentes são complexos e envolvem simulações que podem usar dados geográficos, mas não são exclusivamente produtos de geoprocessamento.
A modelagem de dispersão de poluentes envolve cálculos complexos e simulações que utilizam dados meteorológicos e topográficos, além de técnicas de geoprocessamento.
Análise: O item C considera os itens I e III. Ambos são produtos que podem ser obtidos exclusivamente por técnicas de geoprocessamento. A sobreposição de dados temáticos para análise de vulnerabilidade ambiental é uma aplicação direta de SIG, que permite a integração e análise de múltiplas camadas de dados. Está de acordo com o gabarito da banca.

Fundamentação: A sobreposição de dados temáticos é uma técnica de geoprocessamento que permite a análise integrada de diferentes camadas de informação geográfica.
A análise de vulnerabilidade ambiental por sobreposição de dados é uma prática comum em geoprocessamento, utilizando SIG para integrar e analisar dados espaciais.

GABARITO: 'C'

Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - IPHAN - Geoprocessamento - 2025
Monitorar a integridade de áreas licenciadas geralmente é um grande desafio, tendo em vista as geralmente amplas extensões geográficas e a diversidade de temas 
a serem analisados continuamente.
Assinale a opção que apresenta a principal vantagem do uso do geoprocessamento no monitoramento contínuo de áreas licenciadas, 
especialmente em áreas sensíveis.

A.Eliminação da incerteza nos dados, garantindo resultados sempre acurados.
B.Produção de mapas de alta precisão para visualização de dados complexos.
C.Emprego de dados geográficos disponibilizados gratuitamente na Web.
D.Diminuição dos custos operacionais, uma vez que elimina a necessidade de trabalhos de campo.
E.Facilidade de uso, permitindo que qualquer pessoa, sem conhecimento técnico, realize o monitoramento.

Análises:

A.  A eliminação da incerteza nos dados não é uma vantagem garantida do geoprocessamento. Embora o geoprocessamento possa melhorar a precisão dos dados, 
ele não elimina completamente as incertezas, que podem advir de várias fontes, como erros de medição e limitações dos dados de entrada. 
Portanto, este item não está de acordo com o gabarito da banca.

B. A produção de mapas de alta precisão para visualização de dados complexos é uma das principais vantagens do geoprocessamento. 
Ele permite a integração e análise de grandes volumes de dados geográficos, resultando em representações visuais precisas e detalhadas. 
Esta capacidade é crucial para o monitoramento de áreas licenciadas, especialmente em áreas sensíveis, onde a precisão é essencial. Este item está de acordo com o gabarito da banca.

C. Embora o uso de dados geográficos gratuitos seja uma vantagem do geoprocessamento, não é a principal vantagem no contexto de monitoramento contínuo de 
áreas licenciadas. A disponibilidade de dados gratuitos pode reduzir custos, mas a precisão e a capacidade de análise são mais críticas

D.A diminuição dos custos operacionais é uma vantagem potencial do geoprocessamento, mas não elimina completamente a necessidade de trabalhos de campo, 
que ainda podem ser necessários para validação e coleta de dados primários. 

E.A facilidade de uso do geoprocessamento é relativa, pois, embora existam ferramentas amigáveis, o monitoramento eficaz geralmente requer conhecimento técnico especializado.

Alternativa 'B' a CORRETA.

Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - IPHAN - Geoprocessamento - 2025
No contexto do licenciamento ambiental, o planejamento de medidas mitigadoras visa atenuar os efeitos dos impactos ambientais prognosticados em 
decorrência da implantação, operação, manutenção ou, até mesmo, desativação de determinado empreendimento.

Nessa etapa, o geoprocessamento pode auxiliar na

I. definição da melhor localização para a disposição final de resíduos sólidos.
II. criação de corredores ecológicos para conectar fragmentos florestais.
III. identificação de áreas com maior potencial para o desenvolvimento de atividades compensatórias.

Está correto o que se afirma em

A.I, apenas.
B.I e II, apenas.
C.I e III, apenas.
D.II e III, apenas.
E.I, II e III.

Alternativa 'E' a CORRETA.

O item E está de acordo com o gabarito da banca. 
O geoprocessamento pode, de fato, auxiliar na definição da melhor localização para a disposição final de resíduos sólidos (I), 
na criação de corredores ecológicos para conectar fragmentos florestais (II) e na 
identificação de áreas com maior potencial para o desenvolvimento de atividades compensatórias (III). 
Essas aplicações são comuns em estudos ambientais, onde a análise espacial é crucial para a tomada de decisões informadas. 
Fontes como livros de geoprocessamento e estudos de caso em licenciamento ambiental corroboram essa análise.


Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - IPHAN - Geoprocessamento - 2025
Ferramentas de geoprocessamento tornaram-se indispensáveis para o estudo de áreas vulneráveis. Essas ferramentas permitem integrar dados geoespaciais, 
como informações topográficas, uso do solo e características climáticas, para criar modelos e mapas que auxiliam no planejamento urbano e na mitigação de 
desastres naturais, como deslizamentos e enchentes.

Assinale a opção que descreve corretamente uma aplicação do geoprocessamento no monitoramento e gestão de riscos ambientais.

A.O uso de sensores para medir a qualidade do ar em tempo real.
B.A coleta de amostras de solo para análise laboratorial.
C.A geração de mapas temáticos para identificar áreas suscetíveis a deslizamentos.
D.A realização de entrevistas com moradores para entender riscos locais.
E.A construção de barreiras físicas para prevenção de enchentes.

a. O uso de sensores para medir a qualidade do ar em tempo real não está diretamente relacionado ao geoprocessamento, 
que se concentra na análise e visualização de dados geoespaciais. Sensores de qualidade do ar são mais associados a sistemas de monitoramento ambiental, mas não necessariamente ao geoprocessamento. 
Portanto, não está de acordo com o gabarito da banca.

b.A coleta de amostras de solo para análise laboratorial é uma prática comum em estudos ambientais, mas não envolve diretamente o uso de geoprocessamento. 
O geoprocessamento se refere à manipulação e análise de dados espaciais, enquanto a coleta de amostras é uma atividade de campo. 
Assim, não está de acordo com o gabarito da banca.

c.A geração de mapas temáticos para identificar áreas suscetíveis a deslizamentos é uma aplicação clássica do geoprocessamento. 
Essa tecnologia permite a integração e análise de dados geoespaciais para criar representações visuais que auxiliam na identificação de áreas de risco. 
Está de acordo com o gabarito da banca. Fontes: livros de geoprocessamento e sistemas de informação geográfica (SIG).

d.A realização de entrevistas com moradores para entender riscos locais é uma técnica qualitativa de coleta de dados, 
mas não envolve o uso de geoprocessamento. O geoprocessamento se concentra na análise de dados espaciais e não em métodos de pesquisa qualitativa. 
Portanto, não está de acordo com o gabarito da banca.

e.A construção de barreiras físicas para prevenção de enchentes é uma medida de engenharia civil e não uma aplicação direta do geoprocessamento. 
O geoprocessamento pode auxiliar no planejamento dessas estruturas, mas a construção em si não é uma aplicação dessa tecnologia. 
Assim, não está de acordo com o gabarito da banca.

Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - IPHAN - Analista Ambiental - 2025
O mapeamento geoespacial e o geoprocessamento podem ser usados, por exemplo, na identificação de áreas de patrimônio cultural e na análise de impactos ambientais.

Relacione os conceitos a seguir listados às suas respectivas definições.

1. Sensores Remotos
2. Sistemas de Informações Geográficas
3. Fotointerpretação

( ) É um sistema de captação, armazenamento, processamento, análise e exibição de informações georreferenciadas.
( ) É definida como o ato de examinar imagens fotográficas com a finalidade de identificar objetos e deduzir seus significados.
( ) São equipamentos que captam e registram a energia refletida ou emitida pelos elementos da superfície terrestre.

Assinale a opção que indica a relação correta, na ordem apresentada.

A.3 – 1 – 2.
B.3 – 2 – 1.
C.2 – 1 – 3.
D.1 – 3 – 2.
E.2 – 3 – 1.

Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - IPHAN - Antropologia - 2025
Relacione os conceitos do âmbito do georreferenciamento com suas respectivas definições.

1. Geoprocessamento
2. Consulta Espacial
3. Sensoriamento Remoto
4. Cartografia

( ) Ciência e arte de representar graficamente a superfície terrestre por meio de mapas e projeções.
( ) Técnica de coleta de dados da superfície terrestre por sensores em satélites, aviões ou drones, sem contato direto.
( ) Análise de relações espaciais entre objetos geográficos, como sobreposição, proximidade e zonas de influência.
( ) Conjunto de técnicas computacionais para analisar e processar dados geográficos, gerando informações espaciais.

Assinale a opção que indica a relação correta, segundo a ordem apresentada.

A.1, 3, 2 e 4.
B.1, 4, 2 e 3.
C.4, 2, 3 e 1.
D.2, 4, 3 e 1.
E.4, 3, 2 e 1.

Alternativa 'E' A COORRETA.

Ano: 2025 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - IPHAN - Geoprocessamento - 2025
De acordo com a legislação, as Áreas de Preservação Permanente (APP) são áreas no entorno das nascentes e dos olhos d’água perenes, 
qualquer que seja sua situação topográfica, no raio mínimo de 50 (cinquenta) metros.

Assinale a opção que indica, em Geoprocessamento, o nome dado ao(s) polígono(s) definido(s) a partir da vizinhança de uma feição no terreno limitada por um valor máximo de distância.

A.Buffer Zone.
B.Polígonos de Delaunay.
C.Polígonos de Voronoi.
D.Overlay.
E.Tesselação.

a. buffer zone. 
nálise: O termo 'Buffer Zone' refere-se a uma área delimitada ao redor de uma feição geográfica, como um ponto, linha ou polígono, 
com base em uma distância especificada. Esta técnica é amplamente utilizada em Geoprocessamento para criar zonas de proteção ou influência, 
como no caso das APPs mencionadas no enunciado. Está de acordo com o gabarito da banca.

A técnica de 'Buffer' é fundamental em análises espaciais para criar zonas de influência ao redor de feições geográficas, 
sendo uma ferramenta essencial em softwares de SIG (Sistemas de Informação Geográfica).

Análise da alternativa B:
Análise: Os 'Polígonos de Delaunay' são utilizados em triangulações para criar uma rede de triângulos a partir de um conjunto de pontos, 
não sendo aplicáveis para delimitar áreas de influência baseadas em distância. Não está de acordo com o gabarito da banca.
Fundamentação: A triangulação de Delaunay é uma técnica de geoprocessamento que conecta pontos para formar triângulos, garantindo que nenhum ponto esteja dentro 
do círculo circunscrito de qualquer triângulo.
A triangulação de Delaunay é usada para criar malhas de triângulos a partir de um conjunto de pontos, sendo útil em modelagem de superfícies e 
análise de redes.

Análise da alterntiva 'C':

nálise: Os 'Polígonos de Voronoi' são utilizados para dividir um espaço em regiões baseadas na proximidade a um conjunto de pontos, 
mas não são usados para criar zonas de influência baseadas em uma distância fixa. Não está de acordo com o gabarito da banca.
Fundamentação: Os diagramas de Voronoi particionam um espaço em regiões onde cada ponto dentro de uma região está mais próximo de um ponto específico 
do que de qualquer outro.
Os polígonos de Voronoi são usados para dividir um espaço em regiões de proximidade, sendo aplicáveis em análises de vizinhança e alocação de recursos.

Análise da alternativa 'D':
Análise: O termo 'Overlay' refere-se a uma operação de geoprocessamento que combina múltiplas camadas de dados para analisar interseções e sobreposições, 
não sendo específico para delimitar áreas de influência por distância. Não está de acordo com o gabarito da banca.
Fundamentação: Overlay é uma técnica de análise espacial que combina diferentes camadas de dados geográficos para identificar interseções e sobreposições.
A operação de overlay é usada para combinar camadas de dados geográficos, permitindo análises complexas de interseção e sobreposição de informações espaciais.

Análise da altenativa 'E':

Análise: A 'Tesselação' refere-se à divisão de um espaço em formas geométricas sem sobreposição ou lacunas, como em mosaicos, 
e não é usada para criar zonas de influência baseadas em distância. Não está de acordo com o gabarito da banca.
Fundamentação: Tesselação é a divisão de um espaço em formas geométricas repetitivas, como quadrados ou hexágonos, sem sobreposição.
A tesselação é usada em geoprocessamento para criar grades regulares de análise, como em modelos de elevação digital ou mapas de calor.

Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - EPE - Analista de Pesquisa Energética - Área Meio Ambiente/ Geoprocessamento/ Meio Físico - 2024
Considerando os diferentes tipos de classificações de dados em geoprocessamento, é correto afirmar que os dados cadastrais

A.descrevem a distribuição espacial de uma grandeza geográfica, expressa de forma qualitativa.
B.distinguem cada elemento como um objeto geográfico com atributos, podendo ter várias representações gráficas em diferentes escalas.
C.associados a serviços de utilidade pública, como água, luz e telefone, ou redes de drenagem e rodovias.
D.representam quantitativamente uma grandeza que varia continuamente no espaço, como altimetria ou teor de minerais.
E.são obtidos por satélites ou fotografias aéreas, armazenados como matrizes de pixels.

Alternativa 'b' A CORRETA.

A - ERRADA: é de forma QUANTITATIVA
Análise: Os dados cadastrais não descrevem a distribuição espacial de uma grandeza geográfica de forma qualitativa. 
Essa descrição é mais adequada para dados temáticos, que representam fenômenos geográficos qualitativos, como tipos de solo ou uso do solo. 
Portanto, esta opção não está de acordo com o gabarito da banca.
Fundamentação: Dados temáticos são aqueles que descrevem a distribuição espacial de uma grandeza geográfica de forma qualitativa.
De acordo com a literatura de geoprocessamento, dados temáticos são utilizados para representar fenômenos geográficos qualitativos, como tipos de vegetação, uso do solo, etc.
B - CORRETO: Os dados cadastrais distinguem cada elemento como um objeto geográfico com atributos, podendo ter várias representações gráficas em diferentes 
escalas. Esta definição está correta e de acordo com o gabarito da banca.
Fundamentação: Dados cadastrais são aqueles que identificam e descrevem objetos geográficos específicos, como propriedades, edificações, etc., com atributos detalhados.
Segundo a literatura de geoprocessamento, dados cadastrais são utilizados para representar objetos geográficos específicos com atributos detalhados, como propriedades, edificações, etc., 
e podem ser representados em diferentes escalas.

C - ERRADA: não necessariamente o esses serviços, mas por exemplo georreferenciar logradouros, rodovias, setores censitários, redes de drenagem e etc., podendo colocar informações quantitativas e qualitativas de cada elemento na tabela de atributos.
D - ERRADA: os dados cadastrais são dados para informações vetoriais.
E - ERRADA: são obtidos nos órgãos públicos e às vezes georreferenciadas, a partir da criação de pontos, linhas e polígonos, sobre as imagens de satélites.
Os dados cadastrais não são obtidos por satélites ou fotografias aéreas e armazenados como matrizes de pixels. Esta descrição é mais adequada para dados 
raster. Portanto, esta opção não está de acordo com o gabarito da banca.
Fundamentação: Dados raster são aqueles obtidos por satélites ou fotografias aéreas e armazenados como matrizes de pixels.
De acordo com a literatura de geoprocessamento, dados raster são utilizados para representar informações obtidas por satélites ou fotografias aéreas, 
armazenadas como matrizes de pixels.

Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura - Fiscal Ambiental - 2024
As rochas podem ser classificadas de acordo com o seu processo de formação.

O mármore, o quartzito, o xisto e o gnaisse são exemplos de rochas

A.aluvionares.
B.sedimentares.
C.metamórficas.
D.ígneas intrusivas.
E.ígneas extrusivas.


O item A sugere que as rochas são aluvionares. Rochas aluvionares são formadas por sedimentos transportados por água, como em leitos de rios, 
e não se aplicam às rochas mencionadas. Portanto, não está de acordo com o gabarito da banca.
Fundamentação: Rochas aluvionares são depósitos sedimentares formados por processos de sedimentação em ambientes aquáticos.
Rochas aluvionares são formadas por sedimentos transportados e depositados por água corrente, como em leitos de rios.

O item B classifica as rochas como sedimentares. Rochas sedimentares são formadas pela deposição e compactação de sedimentos, 
o que não é o caso das rochas mencionadas, que são metamórficas. Portanto, não está de acordo com o gabarito da banca.
Fundamentação: Rochas sedimentares são formadas pela compactação e cimentação de sedimentos ao longo do tempo.
Rochas sedimentares são formadas pela deposição de material mineral ou orgânico na superfície da Terra e sua subsequente compactação.

O item C corretamente classifica as rochas como metamórficas. Mármore, quartzito, xisto e gnaisse são formados por processos de metamorfismo, 
onde rochas preexistentes são alteradas por pressão e temperatura. Está de acordo com o gabarito da banca.
Fundamentação: Rochas metamórficas são formadas pela transformação de rochas preexistentes sob condições de alta pressão e temperatura.
Rochas metamórficas, como mármore, quartzito, xisto e gnaisse, são formadas a partir de rochas preexistentes que sofrem 
alterações mineralógicas e texturais devido a condições de alta pressão e temperatura.

O item D sugere que as rochas são ígneas intrusivas. Rochas ígneas intrusivas, como granito, são formadas pelo resfriamento lento do magma 
no interior da Terra, o que não se aplica às rochas mencionadas. Portanto, não está de acordo com o gabarito da banca.
Fundamentação: Rochas ígneas intrusivas são formadas pelo resfriamento e solidificação do magma abaixo da superfície terrestre.
Rochas ígneas intrusivas, como granito, são formadas quando o magma se resfria lentamente no interior da crosta terrestre, 
resultando em cristais grandes e visíveis.

O item E classifica as rochas como ígneas extrusivas. Rochas ígneas extrusivas, como basalto, são formadas pelo resfriamento rápido do magma na superfície 
da Terra, o que não é o caso das rochas mencionadas. Portanto, não está de acordo com o gabarito da banca.
Fundamentação: Rochas ígneas extrusivas são formadas pelo resfriamento rápido do magma na superfície terrestre.
Rochas ígneas extrusivas, como basalto, são formadas quando o magma atinge a superfície da Terra e se resfria rapidamente, 
resultando em cristais pequenos e finos.

Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de Caraguatatuba - PEB II - Geografia - 2024
O sensoriamento remoto é a técnica de obtenção de informações acerca de um objeto, área ou fenômeno localizado na Terra, 
sem que haja contato físico com o mesmo. As informações podem ser obtidas através de radiação eletromagnética, 
gerada por fontes naturais (sensor passivo), como o Sol, ou por fontes artificiais (sensor ativo), como o radar.
Disponível em: https://atlasescolar.ibge.gov.br/Acesso: 09 out. 2023

A utilização da técnica apresentada viabiliza aplicações em áreas como:

I. Monitoramento ambiental, permitindo o mapeamento, a avaliações e a gestão de danos em áreas de desmatamento ou afetadas por desastres naturais.
II. Planejamento urbano, criando mapas temáticos sobre o uso e ocupação territorial, direcionando decisões sobre zoneamento e desenvolvimento de infraestrutura.
III. Agricultura de precisão, possibilitando estimativa de produção agrícola, determinação de áreas de preservação de mananciais e controle de doenças ou pragas.

Está correto o que se afirma em

A. I, apenas.
B. III, apenas.
C. I e II, apenas.
D. II e III, apenas.
E. I, II e III.

Alternativa 'E', as três estão corretas.

Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de Belo Horizonte - Engenheiro - Área: Geografia - 2023
O Sensoriamento Remoto usa ferramentas que tem como função captar imagens e informações da superfície terrestre. 
Uma de suas técnicas está associada à captação de fotografias aéreas por aviões ou VANTs (veículos aéreos não tripulados) que 
podem ser utilizadas para a produção de mapas e cartas.

Assinale a opção que indica o nome dessa técnica.

A.Aerofotogrametria.
B.Cartografia aérea.
C.Sistema de posicionamento global.
D.Localização de pontos à superfície.

Alternativa A

Ano: 2022 / Banca: Fundação Getúlio Vargas - FGV /Prova: FGV - TCE TO - Auditor de Controle Externo - Área: Engenharia Ambiental - 2022
A respeito da resolução em sensoriamento remoto, é correto afirmar que:

A.o vetor para a resolução espacial é o principal elemento das imagens de sensores remotos;
B.cada pixel de um sensor remoto representa uma mesma dimensão de uma área para a resolução espacial;
C.na resolução radiométrica, o nível de cinza representa a intensidade média de energia magnética emitida ou refletida;
D.na resolução radiométrica, cada sensor pode armazenar todos os tons cinzas;
E.a resolução temporal corresponde ao tempo de processamento de imagens de uma área.

A. Falsa. O pixel, e não o vetor, é o principal elemento das imagens de sensores remotos.
B. Verdadeira. Cada pixel de um sensor remoto representa uma mesma dimensão de área na resolução espacial.
C. Falsa. Na resolução radiométrica, o nível de cinza representa a intensidade média de energia eletromagnética emitida ou refletida.
D. Falsa. Na resolução radiométrica, cada sensor tem uma capacidade limitada de armazenar tons de cinza, que depende do número de bits usados.
E. Falsa. A resolução temporal se refere à frequência de revisita de um sensor a uma mesma área, e não ao tempo de processamento de imagens.


Ano: 2022 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TCE TO - Auditor de Controle Externo - Área: Engenharia Ambiental - 2022
A respeito dos gráficos dos tipos raster e vetor, é correto afirmar que:

A.a imagem vetor é formada por pequenas peças denominadas pixels;
B.a imagem raster é utilizada quando se necessita de transições suaves de cores e tons;
C.a imagem vetor apresenta perdas de nitidez com o aumento da sua escala;
D.a imagem raster é utilizada quando se trata de logotipo e textos;
E.a imagem vetor ocupa mais espaço de armazenamento se comparada com a raster.

Alternativa "B' a correta.

Diferenças entre imagens vetoriais e raster

Imagens raster são compostas por pixels (A), ou seja, uma grade de pequenos quadrados coloridos. Portanto, alternativa A, ERRADA
Imagens vetoriais são compostas por formas geométricas definidas matematicamente, como linhas, curvas e polígonos.
Imagens raster perdem qualidade quando ampliadas, pois ficam pixelizadas (C).
Imagens vetoriais podem ser ampliadas indefinidamente sem perda de qualidade, pois são redefinidas matematicamente.
Imagens raster tendem a ter arquivos maiores, especialmente quando possuem muitos pixels.
Imagens vetoriais têm arquivos menores, pois armazenam apenas as fórmulas matemáticas (E).
Imagens raster são melhores para fotos e imagens com muitos detalhes e gradientes de cor.
Imagens vetoriais são melhores para logotipos, ilustrações, gráficos, ícones e designs (D) que precisam ser escalados.
Imagens raster permitem edição pixel a pixel, útil para manipulação de fotos.
Imagens vetoriais permitem editar as formas geométricas, útil para designs vetoriais.

Formatos de arquivo:
Imagens raster comuns: JPEG, PNG, GIF, TIFF.
Imagens vetoriais comuns: SVG, EPS, AI, PDF.


Ano: 2022 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TCE TO - Auditor de Controle Externo - Área: Engenharia Ambiental - 2022
Para inserir uma imagem não referenciada a um sistema de Informação Geográfica (SIG), é necessário:

I. Escolher pelo menos dois pontos de controle da imagem a ser georreferenciada.
II. Estabelecer o relacionamento da imagem não georreferenciada e coordenadas conhecidas da imagem de referência.
III. Realizar o reposicionamento da imagem com os parâmetros da imagem a ser georreferenciada.

Está correto somente o que se afirma em:

A. I;
B. II;
C. III;
D. I e II;
E. II e III;

Vamos analisar as afirmativas sobre como inserir uma imagem não referenciada em um Sistema de Informação Geográfica (SIG):
I. Incompleta. Para georreferenciar uma imagem, é necessário escolher mais de dois pontos de controle (geralmente quatro ou mais) na imagem a ser 
georreferenciada e identificar suas coordenadas conhecidas na imagem de referência.
II. Correta. O processo de georreferenciamento estabelece a relação entre os pontos de controle da imagem não georreferenciada e suas coordenadas 
conhecidas na imagem de referência, geralmente uma imagem já georreferenciada ou com coordenadas reais.
III. Incompleta. Após estabelecer o relacionamento entre os pontos de controle, o SIG realiza uma transformação geométrica para reposicionar a imagem não 
georreferenciada, alinhando-a com as coordenadas da imagem de referência. No entanto, a afirmativa não menciona que essa transformação geométrica é 
baseada em algoritmos matemáticos que minimizam os erros entre os pontos de controle.

Ano: 2022 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TCE TO - Auditor de Controle Externo - Área: Engenharia Ambiental - 2022
Sobre os dados de sensoriamento remoto, analise as afirmativas abaixo a respeito dos benefícios para os levantamentos de recursos naturais:

I. Sua visão sinótica permite ver grandes extensões de área em uma mesma imagem.
II. Sua resolução espacial permite a obtenção de informações sobre um alvo na natureza em distintas regiões.
III. Sua resolução espectral permite a coleta de informações em diferentes épocas do ano e em anos distintos.

Está correto somente o que se afirma em:

A. I;
B. II;
C. III;
D. I e II;
E. II e III;

Alternativa 'A", correta somente o item I.

Resolução:

I. Verdadeira. O geoprocessamento, por meio de técnicas como sensoriamento remoto, permite uma visão sinótica, ou seja, a capacidade de visualizar 
grandes extensões de área em uma mesma imagem. Isso possibilita a análise e o monitoramento de fenômenos em escalas regionais e globais.
II. Falsa. A resolução espacial do geoprocessamento se refere à capacidade de distinguir detalhes em uma imagem, ou seja, a menor unidade de área 
que pode ser identificada. Isso permite obter informações sobre alvos na natureza, mas não necessariamente em distintas regiões.
III. Falsa. A resolução espectral do geoprocessamento se refere à capacidade de coletar informações em diferentes faixas do espectro eletromagnético. 
Isso permite a obtenção de dados em diferentes épocas do ano e em anos distintos, possibilitando o monitoramento e a análise de fenômenos ao longo do tempo.

Em resumo:

A visão sinótica permite visualizar grandes extensões de área.
A resolução espacial se refere à capacidade de distinguir detalhes em uma imagem.
A resolução espectral permite a coleta de informações em diferentes faixas do espectro eletromagnético ao longo do tempo.

Ano: 2022 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 17 - Analista Judiciário - Àrea Apoio Especializado: Arquitetura - 2022
Dentre a extensa faixa de possíveis aplicações de Sistemas de Informação Geográfica (SIG), considere:

I. Detecção: delimitação de objetos, representação da realidade.
II. Descrição e análise da estrutura: quantificação da configuração espacial e diversidade do espaço.
III. Planejamento de Paisagens: preparo de planos, detecção da condição atual, desenvolvimento de cenários, sistemas de apoio a tomadas de decisão (SDSS – Spatial Decision Support Systems).
IV. Análise de uso do solo: detecção de tipos de uso e suas mudanças (Change Detection).

Está correto o que se afirma em

A.IV, apenas.
B.I, II e III, apenas.
C.I, II, III e IV.
D.I, II e IV, apenas.
E.I, III e IV, apenas.

Todas as afirmaticas estão corretas.
Fundamentação: O SIG é uma ferramenta que permite a análise de dados geográficos e suas relações espaciais. 
Isso inclui a detecção de objetos e a representação da realidade, a descrição e análise da estrutura espacial, 
o planejamento de paisagens e a análise de uso do solo. Portanto, todas as aplicações apresentadas no enunciado estão corretas.
Referência: Longley, P.A., Goodchild, M.F., Maguire, D.J., Rhind, D.W. (2011). Geographic Information Systems and Science. 3rd Edition. Wiley.

A análise de uso do solo é uma aplicação importante do SIG, pois permite identificar e monitorar mudanças no uso do solo ao longo do tempo. 
Isso pode ser útil para planejamento urbano, conservação ambiental, entre outros.

O SIG pode ser usado para planejar paisagens, pois permite a visualização e análise de dados geográficos, 
o que pode ajudar na tomada de decisões sobre o uso do solo e a conservação de paisagens.
Referência: Longley, P.A., Goodchild, M.F., Maguire, D.J., Rhind, D.W. (2011). Geographic Information Systems and Science. 3rd Edition. Wiley.

A descrição e análise da estrutura é uma aplicação importante do SIG, pois permite quantificar a configuração espacial e a diversidade do espaço, 
o que pode ser útil para uma variedade de propósitos, incluindo planejamento urbano e conservação ambiental.

Ano: 2022 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 17 - Analista Judiciário - Àrea Apoio Especializado: Arquitetura - 2022
Nos Sistemas de Informação Geográfica (SIG), um modelo de dados geográficos consegue:

I. Suportar relacionamentos espaciais.
II. Representar dados alfanuméricos.
III. Determinar o valor do Erro Médio Quadrático (EMQ) admitido, que varia consoante a escala do documento, não podendo ultrapassar valores limites definidos.
IV. Sobrepor as operações de Overlay, com a união das interseções existentes, e depois colocar todas as entidades em uma classe de saída.

Está correto o que se afirma em

A. II, III e IV, apenas.
B. I e II, apenas.
C. I, II, III e IV.
D. I e IV, apenas.
E. I e III, apenas.

Alternativa 'B', somente o item I e II, corretos.

Análises:

A fundamentação para esta análise é baseada no entendimento de que um modelo de dados geográficos em um SIG tem a capacidade de suportar relacionamentos espaciais e representar dados alfanuméricos, conforme afirmado nas afirmações I e II.
A fundamentação para esta análise é baseada no entendimento de que o EMQ é uma medida de precisão estatística, não uma função de um modelo de dados geográficos em um SIG. Portanto, a afirmação III é incorreta.
O que é um pouco ambígua e pode não ser uma função direta de um modelo de dados geográficos em um SIG.
Fundamentação: A fundamentação para esta análise é baseada no entendimento de que a operação de Overlay é uma função de um SIG, mas não necessariamente uma função direta de um modelo de dados geográficos.

Ano: 2018 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - COMPESA - Assistente de Gestão - Área Técnico Operacional - 2018 
Ao se trabalhar com um Sistema de Informações Geográficas (GPS), é fundamental definir o datum que será utilizado, que é definido como sendo:

A.o intervalo temporal para coleta de dados dos satélites.
B. a unidade de medida para distâncias.
C. a frequência das ondas emitidas pelos satélites.
D. o sistema geodésico de referência.
E. a precisão requerida na localização.

Alternativa 'D'

O DATUM é um termo muito utilizado quando se quer fazer menção ao sistema de referência. 
Do plural data, cujo nome vem do latim dado, que se refere a detalhe. Modelo matemático teórico da representação da superfície da Terra 
utilizado pelos cartógrafos em um determinado mapa ou carta. 
O DATUM disponibiliza o ponto de referência a partir da representação gráfica dos paralelos e meridianos.
A diferença de um DATUM para o outro estão baseadas em modelos matemáticos distintos da forma e dimensões da Terra, bem como da projeção representada.
Mundialmente falando existem vários DATA (plural de DATUM), O IBGE definiu o SIRGAS2000 (Sistema de Referência Geocêntrico para as Américas) 
como o Sistema Geodésico Brasileiro oficial.

Ano: 2018 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - DPE AM - Assistente Técnico de Defensoria - Área Técnico em Agrimensura - 2018
Nos trabalhos de georreferenciamento, os vértices cujas coordenadas são obtidas a partir da sua ocupação física e estão localizados na divisa do imóvel ao longo de acidentes físicos ou geográficos são do tipo

A. M.
B. V.
C. O.
D. P.
E. Geométrico.

Gabarito letra 'D', vértice tipo 'P'.
A assertiva correta é a letra D. Os vértices tipo P, ou seja os marcos não materializados, são aqueles em que as coordenadas são obtidas a partir de sua ocupação física, está localizada na divisa do imóvel, 
em casos de acidentes artificiais ou naturais, que são cursos d’água, estradas de rodagem e de ferro, linhas de transmissão, oleoduto, gasoduto etc. 
Estes vértices tipo P não precisam ser materializados no terreno, mais deve haver a ocupação física. 
Sendo que esses vértices não podem existir no início e no fim de tal limite (margem do rio, da estrada, dentre outros), 
sendo nos extremos desses limites utilizado um vértice tipo M.

Ano: 2018 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - COMPESA - Assistente de Saneamento - Área Técnico Operacional - 2018 
Com referência ao Sistema de Referência Geocêntrico para as Américas (SIRGAS2000), analise as afirmativas a seguir.

I. Desde 25 de fevereiro de 2015, o SIRGAS2000 tem sido utilizado oficialmente no Brasil, admitindo-se também o uso oficial dos referenciais SAD 69 (South American Datum, 1969) e Córrego Alegre (CA).
II. A definição/orientação do SIRGAS2000 é geocêntrica, ao passo que as do SAD69 e as do CA são topocêntricas.
III. Ao migrar do sistema SAD 69 para o SIRGAS2000, as coordenadas que representam a posição dos objetos sofrem alterações, que em média são da ordem de 65m.

Está correto o que se afirma em

A. II, somente.
B. III, somente.
C. I e II, somente.
D. II e III, somente.
E. I, II e III.

O Item I está errado. Foram oficiais o SAD69 e o Córrego Alegre. Agora, foi adotado somente o SIRGAS2000.
O item II está correto.

Ano: 2018 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - DPE AM - Assistente Técnico de Defensoria - Área Técnico em Agrimensura - 2018
São utilizações dos Sistemas de Informações Geográficas em estudos ambientais:

A. mapeamento populacional, diagnóstico de radioisótopos e avaliação de efeito pepita.
B. avaliação de impacto ambiental, mapeamento populacional e diagnóstico de radiofrequência.
C. mapeamento temático, diagnóstico ambiental e avaliação de impacto ambiental.
D. avaliação de efeito pepita, mapeamento temático e diagnóstico de radioisótopos.
E. avaliação de radiofrequência, mapeamento temático e diagnóstico de radioisótopos.

a. diagnóstico de radioisótopos não uma utilização dos SIG e nem avaliação de efeito pepita.
b. diagnóstico de radiofrequência não é de uso fundamental de um SIG
c. CORRETO 
d. ERRADO
e. ERRADO.

Ano: 2018 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - DPE AM - Assistente Técnico de Defensoria - Área Técnico em Agrimensura - 2018
O Geoprocessamento procura representar fenômenos geográficos e sua distribuição sobre a superfície da Terra. 
As características de uma região geográfica são moldadas por um conjunto de fatores, assim, o clima, as formações geológicas, o relevo, 
o solo e a vegetação formam uma totalidade inter-relacionada. 
O traçado de pontos de correspondência entre o relevo e o solo ou o solo e a vegetação de uma região, denomina-se

A. correlação temática.
B. correlação espacial.
C. correlação temporal.
D. correlação topológica.
E. sistema de informações geográficas.

Alternativa 'A' a correta.
A assertiva mais prudente é a letra A, correlação temática: as características de uma região geográfica são moldadas por um conjunto de fatores. 
Assim, o clima, as formações geológicas, o relevo, o solo, a vegetação formam uma totalidade interrelacionada. 
Deste modo, pode-se traçar pontos de correspondência entre o relevo e o solo ou o solo e a vegetação de uma região

Ano: 2018 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - DPE AM - Assistente Técnico de Defensoria - Área Técnico em Agrimensura - 2018
NÃO faz parte de um Sistema de Informações Geográficas − SIG:

A. interface com usuário.
B. interpolador filológico.
C. função de processamento gráfico e de imagens.
D. entrada e integração de dados.
E. armazenamento e recuperação de dados (organizados sob a forma de um banco de dados geográficos).

Alternativa 'B'.
A assertiva que se adequa é a alternativa B,Interpolação é o método de aproximar os valores dos conjuntos discretos. 
Em matemática, denomina-se interpolação o método que permite construir um novo conjunto de dados a partir de um conjunto discreto de dados 
pontuais previamente conhecidos. Em engenharia e ciência, dispõe-se habitualmente de dados pontuais obtidos a partir de uma amostragem ou de um experimento. 
Tal conjunto de dados pontuais (também denominado conjunto degenerado) não possui continuidade, e isto muitas vezes torna demasiado irreal 
a representação teórica de um fenômeno real empiricamente observado.

Ano: 2018 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - DPE AM - Assistente Técnico de Defensoria - Área Técnico em Agrimensura - 2018
Na aplicação de técnicas de georreferenciamento, o posicionamento também pode ser efetuado por topografia clássica.

A.triangulação.
B.poligonação.
C.trilateração.
D.irradiação.
E.triangulateração.

A assertiva correspondente as pesquisas é a letra E .
A- A determinação de coordenadas, a partir do método da triangulação, é obtida por meio da observação de ângulos formados entre os alinhamentos de vértices 
intervisíveis de uma rede de triângulos.
B-O método também é chamado de levantamento por poligonação, pois consiste em percorrer o contorno de um polígono (poligonal de base), 
saindo de um ponto inicial e retornando a ele, medindo os ângulos e as distâncias dos lados que o compõem, 
bem como os alinhamentos formados pelos vértices do polígono e o polígono real (perímetro) e os demais alinhamentos que compõem o levantamento 
dos detalhes o serem levantados.
C-A trilateração é um processo para determinar o posicionamento de algo, a forma como são feitos os cálculos. 
O cálculo faz uso de 3 pontos de referência para determinar a posição do elemento, como acontece com os sistemas de GPS (Global Positioning System).
D-O método da irradiação se baseia na determinação de coordenadas a partir da observação de ângulos e distâncias ou azimutes e distâncias. 
A determinação de coordenadas do ponto de interesse é realizada a partir da observação da distância entre um dos vértices conhecidos 
até o vértice de interesse, bem como do ângulo formado entre o alinhamento do vértice de interesse e o alinhamento dos vértices conhecidos
E-Na triangulateração são observados ângulos e distâncias entre os vértices intervisíveis de uma rede de triângulos , 
função da praticidade em se medir distâncias e ângulos com estações totais, aliada à possibilidade de processamento automatizado de um grande volume de dados, 
a triangulateração, quando comparada com a trilateração e triangulação, se destaca por possibilitar uma melhor precisão e melhor análise estatística das observações e das coordenadas, 
tendo em vista o elevado número de observações redundantes.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
Deseja-se representar uma bacia hidrográfica a partir dos cursos d’água que a compõem.

Considerando que os cursos d’água são representados como linhas, a representação deve preservar a(s) seguinte(s) propriedade(s) topológica(s):

A.conectividade;
B.conectividade e orientação;
C.orientação;
D.orientação e contiguidade;
E.conectividade, orientação e contiguidade.

Alternativa 'B'

Para resolvermos a questão, devemos ter em mente que a hidrografia é representada por linhas – e não por pontos ou polígonos. 
Tendo em vista que dentro de uma bacia, rios afluentes SEMPRE deságuam nos rios principais, é necessário que haja CONECTIVIDADE entre as linhas. 
Do mesmo modo, os rios SEMPRE nascem em áreas mais altas e deságuam em áreas mais baixas, portanto, há ORIENTAÇÃO – um fluxo contínuo de mão única. 
A alternativa que melhor expressa essa ideia é a B.
Poderíamos ficar tentados a marcar a alternativa E. Porém, devemos lembrar que CONTIGUIDADE é uma regra aplicada somente a POLÍGONOS. 
Quando dizemos, por exemplo, que uma área é contígua à outra, isso significa que suas superfícies são contínuas. 
No caso da questão, procurou-se representar a bacia hidrográfica “a partir dos cursos d’água”, ou seja, a partir das linhas.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
A grandeza empregada na construção da assinatura espectral de um objeto denomina-se:

A. absortância;
B. transmitância;
C. reflectância;
D. espalhamento;
E. irradiância.

A assinatura espectral é a intensidade relativa com a qual um alvo reflete ou emite a radiação eletromagnética incidente 
sobre ela nos diferentes comprimentos de onda do espectro eletromagnético. Esta intensidade é também definida como reflectância.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
A projeção de Mercator é muito conhecida pelo seu emprego na navegação, diferenciando-se da projeção utilizada no sistema UTM pela 
superfície de projeção cilíndrica ser tangente à superfície de referência na primeira e secante na última projeção. 
A projeção de Mercator é também caracterizada por preservar:

A.os ângulos em torno dos pontos e possuir o eixo do cilindro inclinado em relação ao eixo da Terra;
B.as grandes áreas e possuir o eixo do cilindro perpendicular ao eixo da Terra;
C.os ângulos em torno dos pontos e possuir o eixo do cilindro perpendicular em relação ao eixo da Terra;
D.as áreas em geral e possuir o eixo do cilindro inclinado em relação ao eixo da Terra;
E.as distâncias e possuir o eixo do cilindro perpendicular em relação ao eixo da Terra.

A assertiva correta é a letra C. projeção de Mercator é uma projeção cartográfica desenvolvida por Gerhard Mercator no ano de 1569. 
Trata-se de uma projeção do tipo cilíndrica conforme, caracterizada pela conservação das formas dos territórios e distorção de seus tamanhos, 
principalmente daqueles países situados mais distantes da Linha do Equador. 
Os paralelos e meridianos, na projeção de Mercator, consistem em linhas retas que se cruzam e formam ângulos retos. 
Ela é até hoje empregada no desenvolvimento de cartas náuticas, que são utilizadas nas navegações.

A.Menciona que o eixo do cilindro é inclinado.Um cilindro com eixo inclinado se refere a uma projeção Oblíqua.

B.Menciona preservar as grandes áreas. Preservar áreas é a característica de uma projeção equivalente ou de áreas iguais (exemplo: Projeção de Peters).

D.Menciona preservar as áreas em geral e possuir o eixo do cilindro inclinado .Áreas em geral está errado (Mercator é conforme, não equivalente). 
Eixo inclinado está errado (seria Oblíqua).

E. Menciona preservar as distâncias. Preservar distâncias é a característica de uma projeção equidistante (exemplo: Projeção Cilíndrica Equidistante). 
Mercator não preserva distâncias, que ficam muito distorcidas à medida que se afasta do Equador.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
Com o desenvolvimento de aplicações de Sistemas de Informações Geográficas (SIG), a representação de feições passou a considerar, além da geometria, as propriedades topológicas intrínsecas aos tipos de feições existentes.

Uma propriedade topológica empregada em aplicações de SIG é:

A. a distância entre feições pontuais;
B. a distância entre feições representadas por polígonos;
C. a área de feições representadas por polígonos;
D. a orientação de feições representadas por curvas;
E. o ângulo formado por duas feições representadas por curvas.

A assertiva correta é a letra D.Em cartografia, as curvas de nível são representações do relevo produzidas através da utilização de linhas imaginárias 
(chamadas de linhas altimétricas, quando na superfície, e linhas batimétricas, quando abaixo do nível do mar). 
Elas possuem o mérito de representar em uma superfície plana os desníveis e a declividade topográfica. 
O emprego da técnica de curvas de nível é recomendado em áreas com escala grande, ou seja, em áreas pequenas, em que o nível de detalhamento costuma ser maior. 
Assim, podemos ter a área de uma vertente sendo representada separando-se as altitudes ordenadamente, de forma que cada altitude representa uma linha do mapa

Veja mais sobre "Curvas de Nível" em: https://brasilescola.uol.com.br/geografia/curvas-nivel.htm


Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
A linguagem mais comum para elaboração de consultas em bancos de dados é a SQL. Ao elaborar uma consulta nessa linguagem, 
emprega-se a cláusula WHERE quando se deseja:

A.especificar a tabela onde será realizada a consulta;
B.especificar o diretório onde os dados estão armazenados;
C.especificar o endereço IP onde os dados estão armazenados;
D.especificar condições a que as instâncias selecionadas devem atender;
E.extrair a geometria do objeto selecionado na consulta.

a. Não
b. Não
c. Não
d. CORRETO. A cláusula WHERE é especificar condições a que as instâncias selecionadas devem atender
e. Não.


Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
Ao analisar um modelo conceitual de um SGBD orientado a objetos, observou-se a ocorrência de uma classe abstrata.

Em termos práticos, isso significa que:

A.as instâncias dessa classe pertencem a subclasses;
B.a classe possui apenas métodos, mas não atributos;
C.as instâncias dessa classe são formadas por agregação;
D.a classe representa uma associação entre outras classes;
E.a classe é temporária, sendo criada e apagada de acordo com o contexto.

A assertiva correta é a letra A.
As classes abstratas somente podem ser estendidas, sendo que a criação de um objeto a partir da mesma é um procedimento evitado. 
Além disso, caso um ou mais métodos abstratos estejam presentes nessa classe abstrata, a classe filha será, então, forçada a definir tais métodos, 
pois, caso contrário, a classe filha também se tornará abstrata.

A classe abstrata ou subclasse irá herdar métodos e instância da classe primária.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
O termo álgebra de mapas foi popularizado por Dana Tomlin, em 1990, referindo-se a diversas operações sobre dados raster.

Um exemplo de operação de vizinhança de álgebra de mapas é:

A.reclassificação;
B.operação de álgebra de camadas;
C.geração de declividade;
D.geração de mapas de custo-distância;
E.superposição de camadas.

A assertiva correta é a letra C.Para a elaboração de mapas de declividade, frequentemente dividimos a declividade em classes que facilitam 
compreensão de como é o relevo da região. A declividade, por padrão, é calculada em graus, mas a maioria dos estudos utilizam 
classes de declividade em porcentagem. 

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
O PMGB especifica uma seção destinada ao registro dos metadados relacionados à qualidade de dados geoespaciais.

Sobre os metadados da seção de Qualidade, é correto afirmar que:

A.o relatório de linhagem é obrigatório para quaisquer produtos;
B.a linhagem pode ser documentada apenas por uma declaração textual;
C.todos os relatórios sobre elementos de qualidade são obrigatórios;
D.o metadado nível hierárquico diz respeito à classificação da qualidade dos dados avaliados;
E.cada relatório sobre elementos de qualidade deve vir acompanhado do respectivo resultado de conformidade.


A assertiva correta é a letra B. A Informação sobre os processos ou dados de base utilizados na construção dos dados especificados no âmbito,
 ou declaração relativa ~ ausência de conhecimento sobre o histórico. A "Declaração" é a descrição geral sobre o conhecimento do produto sobre 
o histórico de produção de um CDG. Na "Fonte dos Dados" podem ser discriminados as vários dados de basE que deram origem ao CDG (Conjunto de Dados Geográficos) 
com as respectivas resoluções espaciais E extensões geográficas. Quando o CDG for uma imagem o denominado de escala não se aplica. 
Na "Etapa do Processo" podem ser discriminados os vários processamentos efetuados para obter o CDG. 
Na "Declaração" os processos e fontes de dados podem ser descritos textualmente.

Disponível :https://biblioteca.ibge.gov.br/visualizacao/livros/liv83691.pdf

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
Com a oferta de telefones celulares equipados com rastreadores GPS e de aplicativos capazes de armazenar as coordenadas obtidas por esses dispositivos, 
é possível reconstituir as trajetórias percorridas pelo usuário de tais aplicativos.
Caso a empresa desenvolvedora de um aplicativo deseje armazenar as trajetórias dos seus usuários para futuras análises, 
preservando as propriedades topológicas e minimizando o espaço de armazenamento, recomenda-se adotar a seguinte estrutura de dados:

A.matricial, armazenando uma trajetória por arquivo;
B.matricial, armazenando todas as trajetórias de um mesmo dia;
C.vetorial, armazenando as trajetórias como linhas;
D.vetorial, armazenando as trajetórias como pontos ordenados;
E.textual, armazenando os atributos e as coordenadas separados por vírgulas (CSV).

Preservando as propriedades topológicas e minimizando o espaço de armazenamento, a alternativa 'C'.
As unidades vetoriais estão caracterizadas pelo fato de que a sua localização geográfica pode ser definida independentemente e de forma muito precisa, 
mediante suas relações topológicas. As camadas vetoriais são úteis para descrever os diferentes elementos do terreno, tais como: 
estradas, rede hidrográfica, limites administrativos, etc.Para isso se armazenam uma série de pontos (X, Y) que descrevem a localização dos elementos (pontos), 
ou sua trajetória (linhas) ou limites (polígonos) mediante uma sequência de pontos unidos por linhas retas sendo elas simples ou soltas estão compostas 
por pontos com suas correspondentes X, Y e pelo menos um valor de Z para o atributo de toda a linha.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
A ponderação pelo inverso da distância (IDW) é a interpolação espacial mais empregada e intuitiva em análise espacial, a qual:

A.aplica um método exato de interpolação;
B.utiliza pesos negativos no caso da existência de picos;
C.emprega a lei de Tobler somente para os pontos interpolados situados muito próximos dos pontos observados;
D.obtém valores interpolados, cujos valores são menores que os menores valores observados em todo o conjunto de dados nas depressões;
E.altera os valores da grandeza nos valores observados para suavizar a superfície gerada.

A assertiva correta é a letra A. Os interpoladores podem também variar quanto à transição (abrupta ou gradual), 
ao seu caráter (determinístico ou probabilístico) e quanto à exatidão, sendo caracterizados como exatos ou inexatos, neste sentido, 
destaca-se que interpoladores exatos respeitam os dados existentes, enquanto os inexatos ou aproximados assumem incertezas (erros) nos dados existentes.

Análise da alternativa 'B':
O IDW não utiliza pesos negativos, mesmo na presença de picos. Os pesos são sempre positivos e inversamente proporcionais à distância. 
Não está de acordo com o gabarito da banca.
Fundamentação: Os pesos no IDW são calculados como o inverso da distância elevada a uma potência, geralmente positiva, o que garante que os pesos sejam sempre 
positivos. No método IDW, os pesos são calculados como 1/d^p, onde d é a distância e p é a potência, geralmente um valor positivo, 
garantindo que os pesos sejam sempre positivos.

Análise da alternativa C:

A Lei de Tobler, que afirma que 'tudo está relacionado a tudo o mais, mas coisas mais próximas estão mais relacionadas do que coisas distantes', 
é uma base conceitual para o IDW, mas não é aplicada apenas a pontos muito próximos. Não está de acordo com o gabarito da banca.
A Lei de Tobler é um princípio geral em geografia que fundamenta a ideia de que a proximidade espacial influencia a relação entre os dados.
A Lei de Tobler é frequentemente citada em geografia e geoprocessamento para justificar a importância da proximidade espacial na análise de dados.

Análise da alternativa 'D':

O IDW não garante que os valores interpolados sejam menores que os menores valores observados em depressões. Os valores interpolados dependem dos pesos e
 dos valores dos pontos conhecidos. Não está de acordo com o gabarito da banca.
Fundamentação: O método IDW calcula valores interpolados com base em uma média ponderada, e não há garantia de que esses valores sejam menores ou 
maiores que os valores observados.
Os valores interpolados pelo IDW são uma média ponderada dos valores conhecidos, e a interpolação não impõe limites específicos em relação aos valores 
observados.

Análise da alternativa E:
O IDW não altera os valores observados para suavizar a superfície. Os valores observados permanecem inalterados, e a suavização 
ocorre naturalmente pela ponderação. Não está de acordo com o gabarito da banca.
Fundamentação: O método IDW utiliza os valores observados como estão e calcula os valores interpolados com base na ponderação pela distância.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
O provedor de um serviço web precisa informar ao usuário os recursos disponíveis para que o usuário possa compor sua requisição de forma adequada.

A operação especificada nos serviços web de mapas para atender a essa demanda é:

A.GetCapabilities;
B.GetFeature;
C.GetMap;
D.GetFeatureInfo;
E.GetMetadata.

Aassertiva correta é a letra A.
A especificação OpenGIS WMS (OGC, 2006) define um serviço para a produção de mapas dinâmicos na Web. Neste sentido, o mapa é uma representação 
visual dos dados geográficos e não os dados de fato. Os mapas produzidos são representações geradas em formatos de imagem, como PNG, GIF e JPEG, 
ou em formatos vetoriais, como o SVG. Quando o cliente requisita um mapa utilizando o serviço, um conjunto de parâmetros deve ser informado ao servidor: 
as camadas desejadas, os estilos que devem ser aplicados sobre as camadas, a área de cobertura do mapa, a projeção ou sistema de coordenadas geográficas, 
o formato da imagem gerada e também o seu tamanho.

• GetCapabilities: obtém os metadados do servidor, que descrevem o conteúdo e os valores dos parâmetros aceitos. A reposta do servidor a esta 
requisição é um documento XML formatado de acordo com o esquema capabilities_1_3_0.xsd disponível em http://schemas.opengis.net/wms/1.3.0.
Disponível em :http://www.dpi.inpe.br/cursos/ser300/Referencias/SIGAndBancoDadosGeograficos.pdf

O item B, 'GetFeature', não está de acordo com o gabarito da banca. 'GetFeature' é uma operação associada ao Web Feature Service (WFS), 
que permite a recuperação de dados geográficos vetoriais. Embora seja uma operação importante em serviços de geoprocessamento, não é a operação que descreve 
as capacidades de um serviço web de mapas.
Fundamentação: A operação 'GetFeature' é parte do padrão WFS do OGC, que é utilizado para acessar e manipular dados geográficos vetoriais.
O padrão WFS do OGC define a operação 'GetFeature' como um meio de recuperar dados geográficos vetoriais de um serviço web, permitindo consultas 
espaciais e não espaciais sobre os dados disponíveis.

O item C, 'GetMap', não está de acordo com o gabarito da banca. 'GetMap' é uma operação do WMS que permite a obtenção de mapas renderizados como imagens. 
Embora seja uma operação central para a visualização de mapas, não é a operação que fornece informações sobre as capacidades do serviço.
Fundamentação: A operação 'GetMap' é definida pelo padrão WMS do OGC e é utilizada para solicitar mapas como imagens de um serviço web.
No contexto do WMS, a operação 'GetMap' permite que os usuários solicitem mapas renderizados em formatos de imagem, especificando 
parâmetros como a área geográfica, camadas a serem exibidas e o sistema de referência espacial.

O item D, 'GetFeatureInfo', não está de acordo com o gabarito da banca. 'GetFeatureInfo' é uma operação do WMS que permite obter informações 
detalhadas sobre elementos específicos em um mapa renderizado. Esta operação é utilizada para consultas interativas, mas não 
para descrever as capacidades do serviço.
Fundamentação: A operação 'GetFeatureInfo' é parte do padrão WMS do OGC e é utilizada para obter informações adicionais sobre elementos em um mapa.
A operação 'GetFeatureInfo' permite que os usuários cliquem em um mapa renderizado para obter informações detalhadas sobre os elementos 
geográficos exibidos, como atributos de feições específicas.

No item E 'GetMetadata' não é uma operação padrão definida pelo OGC para serviços web de mapas. Embora o termo 'metadata' seja relevante 
em contextos de geoprocessamento, a operação padrão para descrever as capacidades de um serviço é 'GetCapabilities'.


Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
Com o aumento da oferta de acesso à internet, abriu-se a oportunidade de disponibilizar dados geográficos por meio de serviços web, 
expandindo o acesso para aplicativos, navegadores e softwares de geoprocessamento.
Nesses serviços, o usuário envia uma requisição contendo a operação desejada e os parâmetros necessários para a consulta. 
Após o processamento por parte do servidor, os dados são enviados para o usuário conforme as particularidades do serviço.

O protocolo para envio de requisições e transmissão dos dados processados pelo servidor é:

A. FTP;
B. HTTP;
C. SCP;
D. SMTP;
E. TCP.

Analisando as alternativas:
- A. FTP (File Transfer Protocol) → usado para transferência de arquivos, não para requisições de páginas.
- B. HTTP (HyperText Transfer Protocol) → protocolo da web, responsável por enviar requisições do cliente (navegador) ao servidor e receber os dados processados (como páginas HTML).
- C. SCP (Secure Copy Protocol) → usado para cópia segura de arquivos entre sistemas, não para requisições web.
- D. SMTP (Simple Mail Transfer Protocol) → usado para envio de e-mails.
- E. TCP (Transmission Control Protocol) → protocolo de transporte que garante entrega confiável de pacotes, mas não é o protocolo de aplicação responsável por requisições ao servidor.

Portanto, alterntiva 'B'.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
Texto 1 - O decreto que instituiu a Infraestrutura Nacional de Dados Espaciais (INDE) determinou a elaboração de um conjunto padronizado de metadados geoespaciais para a disseminação dos produtos já disponíveis no âmbito de todos os órgãos e entidades do Poder Executivo federal. Em 2009, foi disponibilizado o Perfil de Metadados Geoespaciais Brasileiro (PMGB) onde os metadados são apresentados organizados por seções.

Segundo o texto 1, de acordo com o PMGB, o preenchimento dos metadados é obrigatório:

A. para todos os metadados;
B. para os metadados do perfil sumarizado;
C. nos casos previstos no dicionário de dados;
D. apenas para a seção Identificação;
E. apenas para dados produzidos após a homologação do PMGB.

A assertiva correta é a letra C.
O dicionário de dados serve como um ponto de partida, de comum acordo, objetivo e sem ambiguidades, a partir do qual é possível se reconstruir 
o contexto em que a informação foi coletada, melhorando significativamente a qualidade das análises de dados construídas a partir dos dados coletados.

Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
Em virtude da demanda pelo processamento de dados geográficos, foram desenvolvidas extensões espaciais complementares a Sistemas Gerenciadores de Bancos de Dados 
(SGBD) disponíveis no mercado.
Uma extensão espacial para SGBD disponível na atualidade é:

A. MySQL;
B. PostGIS; <-
C. PostgreSQL;
D. Oracle;
E. QGIS.

A assertiva correta é a letra B.
Um dos pontos fortes desse SGBD é seu potencial de extensibilidade, o que possibilitou o desenvolvimento de uma extensão geográfica mais completa, 
chamada PostGIS sendo é uma extensão espacial gratuita e de Sua construção é feita sobre o sistema de gerenciamento de banco de 
dados objeto relacional (SGBDOR) PostgreSQL, que permite o uso de objetos GIS (Sistemas de Informação Geográfica) ser armazenado em banco de dados. 
PostGIS inclui suporte para índices espaciais GiST e R-Tree, além de funções para análise básica e processamento de objetos GIS.
Disponível em :http://www.dpi.inpe.br/livros/bdados/cap8.pdf


Ano: 2017 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista Censitário - Área: Geoprocessamento - 2017
O projeto de um SGBD para emprego em SIG se divide em várias fases, de modo a prover os dados geográficos de forma eficiente para atender 
adequadamente às demandas próprias da aplicação.

Nesse contexto, é elaborado o Modelo Entidade-Relacionamento como resultado do(a):

A. coleta e análise de requisitos;
B. projeto conceitual;
C. projeto lógico;
D. projeto físico;
E. projeto executivo.

A assertiva correta é a letra B.
Este é o modelo ER de alto nível em que contém o detalhe menos granular mas estabelece o escopo global do que está para ser incluído dentro 
do conjunto do modelo. O modelo ER conceitual normalmente define entidades de dados de referência mestre que são comumente usadas pela organização. 
Desenvolver um modelo ER conceitual de amplitude corporativa é útil para suportar a documentação da arquitetura de dados para uma organização. 
Um modelo ER conceitual pode ser usado como a fundação para um ou mais modelos de dados lógicos (ver abaixo). 
O propósito do modelo ER conceitual é então estabelecer a comunalidade de metadados estruturais para as entidades de dados mestre entre o 
conjunto de modelos ER lógicos. O modelo de dados conceitual pode ser usado para formar comunais entre modelos ER como uma base para integração 
de modelo de dados.

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Uma instituição precisa determinar as coordenadas de 5 novas estações. Para a execução do levantamento, são consideradas as seguintes condicionantes:

- todas as linhas entre as 5 estações devem ser levantadas;
- cada linha deverá ser levantada em 3 sessões distintas;
- em cada seção só poderão ser aproveitados os vetores independentes;
- mediante a logística existente, em um dia somente será possível medir uma única sessão;
- serão empregados no levantamento 5 rastreadores, e todos deverão ser usados em todas as sessões.

Diante desse contexto, o levantamento das estações por GPS deverá, teoricamente, ser feito no seguinte número de dias:

A.9;
B.8;
C.7;
D.5;
E.3.

Número de estações: 5
Linhas entre todas as estações: Como todas as estações devem estar conectadas, o número total de linhas (ou vetores) é de 10 linhas a serem medidas.
Sessões: Cada linha deve ser levantada em 3 sessões distintas, então o total de sessões a serem realizadas é: 10×3=30 
Vetores independentes por sessão: Cada sessão só pode ter vetores independentes, mas há 5 rastreadores, que podem medir no máximo 4 vetores independentes por sessão (pois uma estação fica fixa e as outras formam vetores).
Número de sessões por dia: Apenas 1 sessão pode ser realizada por dia.
Agora, considerando que cada sessão mede 4 vetores independentes, o número total de sessões necessárias para cobrir os 30 levantamentos é:

30/4=7,5. Como não é possível ter meio dia de medição, arredondamos para 8 dias.

Resposta: 8 dias

O trabalho com levantamentos GPS requer uma compreensão integrada de várias disciplinas, notadamente Estatística, Astronomia, Geodésia e Eletrônica. 
Os satélites se movem no espaço, portanto existe a necessidade de relacionar dois diferentes sistemas de coordenadas, 
um fixado no espaço (Sistema Inercial - SI) e outro fixado na Terra (Sistema Terrestre - ST). 
O tempo é um aspecto fundamental que entra no GPS de duas formas, a saber: 1) serve para relacionar os dois sistemas de coordenadas, 
tendo em vista que o ST acompanha a rotação da Terra enquanto o SI permanece imóvel; 
2) a escala de tempo dos sinais transmitidos formam toda a base para as medições GPS


Ano: 2016 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEMA - Analista Ambiental - Área Hidrológo Duplicado com 25676. - 2016
O sistema de distribuição de água de um município geralmente é ilustrado por linhas em SIG. Essas linhas são representadas 
topologicamente como os arcos de um grafo orientado, e os demais componentes estão concentrados em seus nós. 
Em Geoprocessamento, o serviço de distribuição de água representa um exemplo de tipo de dado denominado:

A.Imagem.
B.Raster.
C.Rede.
D.Temático.
E.Cadastral.

REDE -> 'C'

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Feições do mundo real são mais bem modeladas como Objetos Geográficos por possuírem uma geometria, um conjunto de propriedades (atributos que definem o seu estado) 
e um conjunto de métodos (que definem o seu comportamento). Na área do conhecimento de Sistemas em Computação e Informática, 
uma grande mudança ocorreu com o surgimento do paradigma da Orientação a Objetos, que permitiu uma evolução nos SIG. De acordo com esse paradigma:

A.tipos abstratos são organizados a partir de Herança e Identidade;
B.classes implementam tipos abstratos que descrevem conjuntos de objetos;
C.herança organiza as instâncias;
D.identidade ou polimorfismo organiza as classes de objetos;
E.identidade ou polimorfismo significa o compartilhamento de código e estrutura.

A assertiva correta é a letra B.
Em programação e na orientação a objetos, uma classe é um Tipo abstrato de Dados (TAD); ou seja, uma descrição que abstrai um conjunto de objetos 
com características similares (um projeto do objeto), é um código da linguagem de programação orientada a objetos que define e implementa um novo 
tipo de objeto, que terão características (atributos) que guardaram valores e, também funções específicas para manipular estes. 
Formalmente, é um conceito que encapsula abstrações de dados e procedimentos que descrevem o conteúdo e o comportamento de entidades do mundo real, 
representadas por objetos. De outra forma, uma classe pode ser definida como uma descrição das propriedades ou estados possíveis de um conjunto de objetos, 
bem como os comportamentos ou ações aplicáveis a estes mesmos objetos. A classe é um elemento primordial de um diagrama de classes; 
modelagem importante na programação orientada a objetos.

Ano: 2016 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEGEP - Analista Ambiental - Área Geoprocessamento - 2016 
A distância em linha reta entre as cidades de São Luis (MA) e Codó (MA) é de aproximadamente 220 quilômetros. Em um mapa planimétrico do Estado do Maranhão essa distância corresponde a 2,2 centímetros. A escala desse mapa é de

A.1:100.000.
B.1.000.000.
C.1:10.000.000.
D.1:10.000.
E.1:1.000.

2,2 cm = 220 km
1,0 cm = ???

220 = 2,2x
220/2,2 = x
100 km = x

1,0 cm = 100 km
1,0 cm = 10.000.000 cm
ALternatica 'C'


Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Independentemente da definição aceita para Infraestrutura de Dados Espaciais (IDE), em todas deve comparecer, como parte integrante de uma IDE, 
um conjunto de serviços. Dentre eles, serviços para mapas ou, mais genericamente, para os dados Geoespaciais. 
Entendendo um serviço web para mapas como aquele que permite qualquer indivíduo interagir com os dados espaciais, está de acordo com esse serviço:

A. apresentar alto investimento de implementação, minimizado pela criação de uma IDE, pois a instituição responsável tem aporte de recursos das instituições parceiras;
B. empregar computadores robustos, com grande capacidade de armazenamento e gerenciamento de dados, muita memória RAM, no mínimo 256MB, e facilidades para acesso remoto;
C. permitir acesso a metadados, além da construção de mapas segundo especificações do usuário;
D. usar diferentes padrões proprietários, de maneira a facilitar e permitir acesso a bases heterogêneas de dados;
E. usar plataformas computacionais, padrões de interface e linguagens de programação específicas, de maneira a serem interoperáveis com outros sistemas.

A assertiva correta é a letra C.. 
A construção de metadados sobre os mapas tem a função de explicitar, por exemplo, as fontes originais dos dados, de modo que o usuário possa 
escolher os produtos a serem utilizados segundo o grau de erro aceitável para a sua aplicação.
Disponível em :http://csr.ufmg.br/geoprocessamento/publicacoes/Metadados.pdf

Ano: 2016 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEGEP - Analista Ambiental - Área Geoprocessamento - 2016 
O sistema de coordenadas Universal Transversa de Mercator − UTM é regido por funções matemáticas que possibilitam a sua 
representação em um plano bidimensional. Com relação ao sistema de coordenadas UTM,

A. o mundo é dividido em 60 fusos, onde cada um se estende por 3° de longitude.
B. para cada fuso é associado um sistema cartesiano métrico de referência.
C. a quadrícula do sistema de coordenadas UTM pode assumir valores negativos em seus extremos.
D. é representado por uma projeção secante e cônica de Mercator.
E. é usado preferencialmente entre as latitudes 80°N e 84°S.

Altenativa CORRETA - 'B'

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
A capacidade de modelar e solucionar problemas em SIG's é muito valorizada devido às potencialidades de integração e análise de dados espaciais e estatísticos, 
e de geração de produtos diferenciados, entre outros. Entre os requisitos que podem viabilizar ou inviabilizar projetos, encontra-se:

A. a validade e a confiabilidade das informações geradas ser maior que a dos dados de entrada;
B. a forte dependência do compartilhamento de dados entre sistemas distintos;
C. a padronização de metadados ser um fator crítico para a operação do sistema em si próprio;
D. o sistema em si (software), que representa o principal custo no total de um projeto;
E. o conjunto de dispositivos (hardware), que representa a parcela mais vultosa em um projeto.

A assertiva correta é a letra B. 
Como a tendência de cada organização é adotar o GIS que melhor atende às suas necessidades, a inexistência de normas e 
padrões para troca de informação geográfica faz com que seja muito mais difícil compartilhar dados e racionalizar esforços de levantamento e 
tratamento de informações entre usuários de sistemas distintos. 
Algumas propostas de solução vêm sido colocadas, mas ainda será necessário algum tempo até que este problema seja resolvido.
 A situação que pode ocorrer é aquela em que todos os usuários dispõem do mesmo GIS, mas os métodos e padrões utilizados para a coleta e 
a manutenção dos dados inviabilizam sua utilização em conjunto. Por exemplo, um dos usuários pode ter um grau de exigência maior com 
relação à precisão cartográfica que os demais. Outros problemas que podem impedir ou inviabilizar o intercâmbio de informações incluem diferenças 
de sistemas de projeção ou de datum, unidades de medida, métodos para produção de estimativas, e ainda diferenças entre os conceitos 
utilizados por cada usuário na criação e manutenção de seus dados. Para completar, ainda poderão existir dificuldades no que diz 
respeito às políticas de disponibilização dos dados adotadas por cada usuário: mídia de gravação, política de comercialização de dados, 
limitações quanto ao repasse dos dados para terceiros, e assim por diante.

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Tecnologista - Área Engenharia Cartográfica - 2016
O processo de construção de dados espaciais atualmente tem forte componente digital. O processo fotogramétrico não poderia ser diferente. 
Dentre as diversas fases que constituem todo esse processo, tem relevância a de Restituição Digital. 
Nesse sentido, é correto afirmar sobre a Restituição Digital que:

A. é uma fase com restrições, pois como as imagens são bidimensionais, a restituição ficará restrita ao espaço 2D;
B. a fase de georreferenciamento das imagens digitais elimina a fase de fototriangulação, pois através dela as imagens já se encontram associadas ao sistema terrestre;
C. a construção de modelos digitais de superfície e a ortorretificação das imagens são possíveis depois da execução da Restituição Digital;
D. o cálculo da paralaxe estereoscópica é fundamental para sua execução;
E. por ser um processo totalmente digital, não necessita realizar as fases de orientação interior e exterior.

Paralaxe é o deslocamento aparente de um referencial, causado pelo deslocamento do observador. Um exemplo de paralaxe pode ser obtido quando 
uma câmara aérea que está acoplada ao avião em movimento, obtém uma cena e segundos depois volta a obtê-la em posição diferente. 
Haverá deslocamentos das posições das imagens de uma foto para a outra, e estes serão diretamente, proporcionais à altura do terreno. 
Estes deslocamentos, nas imagens, apresentam-se paralelos à linha de vôo e são conhecidos como paralaxe estereoscópica. 
O sentido positivo na medida das paralaxes de um ponto coincide com o sentido positivo das coordenadas cartesianas deste ponto.
Disponível em :http://www.inf.ufsc.br/~aldo.vw/visao/1999/aline/foto.html

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Uma das atribuições do IBGE consiste em executar levantamentos censitários e estatísticos, como, por exemplo, de população e renda. 
Essas coletas geram grandes quantidades de dados que necessitam ser agrupados e associados a outras entidades (setores, municípios ou estados) 
para adequada representação e visualização nos chamados mapas temáticos de coropletas. Esse mesmo tipo de mapa é indicado para a representação de:

A. altitudes, climas e vegetação;
B. altitudes, solos e temperatura;
C. altitudes, solos e vegetação;
D. climas, temperatura e vegetação;
E. climas, solos e vegetação.

Mapa coroplético ou mapa coropleto é um tipo de mapa temático: um mapa coroplético representa normalmente uma superfície estatística 
por meio de áreas simbolizadas com cores, sombreamentos ou padrões de acordo com uma escala que representa a proporcionalidade da variável 
estatística em causa, como por exemplo a climas, solos e vegetação.
Disponível em :https://pt.wikipedia.org/wiki/Mapa_coroplético

Alternativa correta: 'E'

Ano: 2016
Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEGEP - Analista Ambiental - Área Geoprocessamento - 2016 
Mosaicos, fotocartas e cartas imagens, embora possuindo uma legenda, a exemplo dos outros documentos cartográficos, 
não explicitam com o mesmo detalhe dos mapas de linhas os alvos imageados, daí a importância de se estabelecer convenções para serem utilizadas 
na cartografia e facilitar a leitura de qualquer pessoa. Com base nas convenções cartográficas básicas, é correto afirmar:

A. As áreas sujeitas a inundação são representadas por área com fundo tracejado em azul, enquanto que, os brejos ou pântanos são semelhantes as áreas sujeitas a inundação, porém é incorporada a vegetação também na cor azul.
B. Rodovias são representadas nas cores vermelha ou vermelha e branca, enquanto que o relevo na cor mostarda.
C. Ferrovias são representadas pela cor amarela.
D. A cobertura vegetal é representada pela cor verde, enquanto que, os brejos ou pântanos pela cor verde musgo.
E. Os limites internacionais, estaduais e municipais são representados pela cor preta, enquanto que, as propriedades rurais pela cor marrom.

Alternativa A correta:

As áreas sujeitas a inundação são representadas por área com fundo tracejado em azul, enquanto que os brejos ou pântanos são semelhantes às áreas 
sujeitas a inundação, porém é incorporada a vegetação também na cor azul. Esta convenção é amplamente utilizada em cartografia para diferenciar 
áreas com características distintas de inundação e vegetação.
As convenções cartográficas são padrões estabelecidos para representar diferentes elementos geográficos em mapas. 
A cor azul é frequentemente usada para representar água e áreas relacionadas, como inundações e pântanos.

O item B não está de acordo com o gabarito da banca. Embora as rodovias sejam frequentemente representadas em vermelho ou vermelho e branco, 
o relevo não é representado pela cor mostarda. O relevo geralmente é representado por curvas de nível e sombreamento para indicar elevações e depressões.
Fundamentação: A representação de rodovias em vermelho é uma convenção comum, mas a cor mostarda não é utilizada para representar relevo em convenções 
cartográficas padrão.
Rodovias são representadas nas cores vermelha ou vermelha e branca, enquanto o relevo é representado por curvas de nível e sombreamento, 
não pela cor mostarda.

O item C não está de acordo com o gabarito da banca. Ferrovias não são representadas pela cor amarela. Em convenções cartográficas, 
ferrovias são geralmente representadas por linhas pretas ou cinzas com marcas transversais que indicam os trilhos.
Fundamentação: A cor amarela não é utilizada para representar ferrovias em convenções cartográficas padrão.
Ferrovias são representadas por linhas pretas ou cinzas com marcas transversais, não pela cor amarela.

O item D não está de acordo com o gabarito da banca. A cobertura vegetal é de fato representada pela cor verde, mas brejos ou pântanos 
não são representados pela cor verde musgo. Eles são geralmente representados por uma combinação de azul e símbolos de vegetação.
Fundamentação: A cor verde é utilizada para representar cobertura vegetal, mas brejos ou pântanos são representados por uma combinação de azul 
e símbolos de vegetação, não pela cor verde musgo.
A cobertura vegetal é representada pela cor verde, enquanto brejos ou pântanos são representados por uma combinação de azul e símbolos de vegetação.

O item E não está de acordo com o gabarito da banca. Os limites internacionais, estaduais e municipais são geralmente representados por linhas de 
diferentes estilos (pontilhadas, tracejadas, contínuas) e cores, como preto ou vermelho. As propriedades rurais não são representadas pela cor marrom; 
essa cor é mais comumente usada para representar elevações e relevo.
Fundamentação: A representação de limites administrativos utiliza diferentes estilos de linhas e cores, enquanto a cor marrom é utilizada para relevo, 
não para propriedades rurais.
Os limites internacionais, estaduais e municipais são representados por linhas de diferentes estilos e cores, enquanto a cor marrom é utilizada para 
representar elevações e relevo, não propriedades rurais.

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
O Geoprocessamento pode exercer ações que visem, por exemplo, a contribuir, garantir e facilitar, dentre outras, a divisão do território. 
Nesse sentido, a mudança do referencial geodésico brasileiro para o SIRGAS2000 influenciou:

A. as divisas naturais, pois as feições fisicamente não mudaram;
B. a área territorial do país, já que essa é dependente de coordenadas;
C. a definição das linhas secas empregadas como limite territorial, pois elas não são dependentes de coordenadas;
D. a definição das Regiões Integradas de Desenvolvimento, pois são fruto da cooperação entre os governos federal, estadual e municipal;
E. a constituição das Mesorregiões Geográficas, pois elas são estabelecidas por municípios adjacentes, pertencentes à mesma UF (Unidade da Federação).

A assertiva correta é a letra B.
O SIRGAS2000 permitirá maior precisão no mapeamento do território brasileiro e na demarcação de suas fronteiras. 
Além disso, a adoção desse novo sistema pela América Latina contribuirá para o fim de uma série de problemas originados na discrepância 
entre as coordenadas geográficas apresentadas pelo sistema GPS e aquelas encontradas nos mapas utilizados atualmente no continente.
Disponível em:https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/12907-asi-mudanca-do-referencial-geodesico-vira-lei


Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Tecnologista - Área Engenharia Cartográfica - 2016
O processamento de imagens digitais pode ter várias abordagens em termos de sequência de processamento. Mas, de modo geral, podem-se identificar 
3 agrupamentos de operações a executar. São eles: o pré-processamento das imagens; as técnicas de realce – e, nesse grupo, 
podem-se distinguir as técnicas de transformação nos domínios radiométrico e espacial; e as técnicas de classificação. 
Para a construção de um mapa temático que tem como níveis de informação o solo, a hidrologia e a vegetação, o responsável pelo processamento empregou:

A. as operações de correção das imagens, a técnica de realce componentes principais e a técnica de classificação temática por rede neural;
B. a operação de correção atmosférica, a técnica de realce supervisionada, por ser mais precisa do que a não supervisionada, e a técnica de classificação temática por rede neural;
C. a operação de correção geométrica, a técnica de realce operações aritméticas e a técnica de classificação temática saturação de cores;
D. a operação de correção de ruídos, a técnica de realce máxima verossimilhança e a técnica de classificação temática distância de Mahalanobis;
E. as operações de correção das imagens, a técnica de realce filtros de convolução e a técnica de classificação temática por fusão de imagens.

A assertiva correta é a letra A.
Para que a precisão cartográfica seja introduzida em imagens de sensoriamento remoto, faz-se necessário que essas imagens digitais sejam corrigidas, 
segundo algum sistema de coordenadas. A transformação de uma imagem de modo que ela assuma as propriedades de escala e de projeção de um mapa é chamada 
de correção geométrica Esse tipo de correção pode ser executado em um sistema de processamento digital de imagens. 
Uma rede neural artificial (RNA) é um sistema de processamento de informação que possui algumas características de desempenho em comum com as redes neurais 
biológicas. Os modelos neurais artificiais têm como principal fonte de inspiração as redes neurais biológicas (Silva, 1998).Bufo (2000) define 
uma rede neural como uma técnica matemática realizada, dentro de um fluxograma seqüencial de cálculo projetado, para obter resultados a partir 
de entradas de dados, independente da lei que rege esses resultados. As redes neurais artificiais oferecem recursos quando outros meios matemáticos 
podem ser impotentes. Disponível em :https://www.scielo.br/j/cagro/a/8dzRLp58cpv9PrzPVpVWLWC/?lang=pt


Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Na produção de dados geoespaciais, as fotografias aéreas estão entre os inúmeros produtos que podem ser classificados como imagem. 
Outro exemplo é o Mosaico, a respeito do qual, é correto afirmar que:

A. a qualidade de sua construção é dependente, basicamente, da ligação geométrica entre feições e da continuidade radiométrica dos níveis de cinza ou das cores;
B. sua construção se restringe ao espaço imagem, e não é possível sua transformação para o espaço objeto, sua principal desvantagem;
C. devido à extensão da área imageada, apresenta pouca qualidade posicional, dadas as distorções das lentes usadas nas câmaras fotogramétricas;
D. teve forte aplicabilidade em sua forma analógica, o que não acontece na forma digital devido ao uso atual da visão computacional;
E. as informações métricas obtidas através dele têm uso expedito, já que não podem ser ortorretificadas.

A assertiva correta é a letra A ,Os mosaicos da fotogrametria são compostos por dois elementos:

- dados dos vértices
- dados das texturas

Os dados dos vértices são guardados em consequentes níveis de detalhe, sendo apenas requisitado aquele que mais se adequa à visualização. 
Por exemplo, a visualização num ecrã de um quarteirão irá trazer um detalhe baixo dos edifícios, mas se a visualização se concentrar num edifício 
em específico, o nível de detalhe deste será o máximo. O mesmo procedimento acontece com os dados das texturas. Apenas são transferidas as 
texturas necessária ao nível da visualização. Este processo permite otimizar bastante o volume de dados transferidos, assim como a velocidade 
de renderização da cena em 3D no cliente.
Disponível em :https://www.novageo.pt/novageo/displayArticles?numero=38158&realismo_com_fotogrametria_mosaicos

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Entre as características das imagens geradas pelo sensoriamento remoto, encontra-se a resolução. Sobre os diversos tipos de resolução, é correto afirmar que:

A. a resolução espacial é função direta da altitude e da orientação do sensor, seja ele passivo ou ativo;
B. a resolução espectral é função da quantidade de bandas do sensor e de quanto é o intervalo de cada banda. Portanto, quanto maior forem os intervalos espectrais, maior será a resolução espectral do sensor;
C. a resolução temporal diz respeito à repetitividade do imageamento, função das características orbitais dos sensores, constituindo um valor que não pode ser alterado;
D. a resolução azimutal é típica dos sensores ativos, sendo função da razão entre a velocidade do sensor e da variação de uma certa frequência, conhecida por efeito Doppler;
E. a resolução radiométrica é aquela que descreve a capacidade do sensor de distinguir a intensidade do sinal emitido pelo alvo. Quanto maior for a diferença entre os sinais emitidos, maior será a resolução.

A assertiva correta é a letra D. 
A resolução azimutal é função do comprimento da antena empregada. Como ilustração, uma antena de 10 m, sem usar o princípio de abertura sintética, 
apresentaria resolução em torno de 5 km. Ou, para se obter a resolução de 25 m, tipicamente encontrada nos satélites ERS e ENVISAT, 
seria preciso uma antena com comprimento de 4 km. O processo de síntese de abertura da antena tira então vantagem do fato do satélite 
estar se deslocando para simular uma antena de maior comprimento, sendo empregado vários retornos da energia retroespalhada de uma mesma região 
em instantes diferentes ao longo do deslocamento do SAR. Como o satélite está se deslocando ao longo de sua trajetória, as variações da 
frequência do pulso recebido pelo sensor (Doppler shift) são empregadas para determinar a posição do alvo.
Disponível em:https://www.scielo.br/j/rbg/a/sZ3NpwZ4VDFrY6FYnxWqbcL/?lang=pt


Ano: 2016 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEGEP - Analista Ambiental - Área Geoprocessamento - 2016 
A utilização de ferramentas computacionais para a análise e modelagem espacial do relevo é comumente realizada por inúmeros pesquisadores no Brasil, 
especialmente a partir da disponibilização dos dados do radar Shuttle Radar Topography Mission − SRTM, o qual tem por objetivo 
o fornecimento de informações altimétricas da superfície terrestre. Sobre SRTM, é correto afirmar que:

A. os dados referentes à América do Sul foram disponibilizados na resolução espacial de 1 arco de segundo (~ 90 m), 
no sistema de coordenadas Lat/Long e Datum WGS84.
B. no Brasil, os dados SRTM foram disponibilizados em uma grade regular de 10 metros.
C. faz parte do conjunto de produtos disponibilizados pelo LANDSAT 5.
D. a estrutura de dados disponibilizada está no formato vetorial.
E. gerou um modelo digital de elevação de aproximadamente 80% do Globo terrestre entre as latitudes 54°S e 60°N.

a. Os dados SRTM referentes à América do Sul foram disponibilizados na resolução espacial de 3 arcos de segundo (~90 m), e não de 1 arco de segundo (~30 m).
Portanto, a afirmação está incorreta. 
Fundamentação: A resolução espacial de 1 arco de segundo (~30 m) foi disponibilizada apenas para os Estados Unidos. 
Para o restante do mundo, incluindo a América do Sul, a resolução é de 3 arcos de segundo (~90 m).
Fonte: NASA SRTM Data Release Notes.

b.  No Brasil, os dados SRTM não foram disponibilizados em uma grade regular de 10 metros. A resolução padrão para os dados SRTM é de 3 arcos de segundo (~90 m)
para a maioria das regiões fora dos Estados Unidos.
Fundamentação: A resolução de 10 metros não é uma característica dos dados SRTM. A resolução padrão é de 3 arcos de segundo (~90 m) para a maioria das regiões globais.
Fonte: NASA SRTM Data Release Notes.

c.O SRTM não faz parte do conjunto de produtos disponibilizados pelo LANDSAT 5. O SRTM é uma missão específica de radar para obtenção de dados altimétricos, 
enquanto o LANDSAT 5 é um satélite de observação da Terra que captura imagens multiespectrais.
Fundamentação: O SRTM e o LANDSAT 5 são missões distintas com objetivos diferentes. O SRTM é focado em dados altimétricos, enquanto o LANDSAT 5 
é voltado para imagens multiespectrais.
Fonte: NASA SRTM e LANDSAT 5 Mission Overviews.

d.Os dados SRTM são disponibilizados no formato raster, e não no formato vetorial. O formato raster é adequado para representar dados contínuos como elevações.
Fundamentação: A estrutura de dados SRTM é raster, o que significa que os dados são organizados em uma grade regular de células, cada uma representando uma elevação.
Fonte: NASA SRTM Data Release Notes.

e. CORRETA.A afirmação está correta. O SRTM gerou um modelo digital de elevação que cobre aproximadamente 80% do globo terrestre, entre as latitudes 54°S e 60°N.
Fundamentação: O SRTM foi projetado para mapear a maior parte da superfície terrestre, cobrindo áreas entre as latitudes 54°S e 60°N, o que corresponde a cerca de 80% do globo.
Fonte: NASA SRTM Mission Overview.

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Uma determinada instituição, ou mesmo um profissional liberal, necessita de dados cartográficos. 
A Infraestrutura Nacional de Dados Espaciais (INDE) é uma opção para suprir essa necessidade, porque possibilita:

A. comprar o insumo de interesse;
B. investigar se existe a disponibilidade de empresas para serviços cartográficos;
C. obter os dados via comunicação direta com a CONCAR;
D. ter acesso a dados e seus metadados;
E. lançar uma concorrência entre as instituições que a integram.

A assertiva correta é a letra D. 
Na prática, os metadados visam descrever, localizar, facilitar a recuperação e gerência de um recurso de informação. 
Assim, para que os metadados, escritos segundo o perfil de Metadados Geoespaciais do Brasil (MGB), possam, efetivamente, alcançar esses propósitos, 
o perfil MGB foi implantado em um software chamado Geonetwork. 
O GeoNetwork é um catálogo de metadados livre, de código aberto, distribuído, inicialmente, pela FAO/ONU. Essas características (livre e de código aberto) 
permitiram que o mesmo fosse customizado para atender as necessidades brasileiras.Por estar aderente aos padrões adotados na INDE e por ser um software de 
livre distribuição, o GeoNetwork é a ferramenta recomendada no plano de ação para a implantação da INDE para carga e gestão de metadados geoespaciais . 
Entre as principais características do catálogo estão:

A utilização de protocolos e ferramentas que permitem a implantação de uma rede distribuída de metadados entre diferentes nós participantes de uma rede;
A implementação de níveis de segurança permitindo a definição de grupos e papéis e seus privilégios para a edição, consulta e disseminação de metadados;
Uma interface globalizada, que permite o acesso aos metadados nos idiomas português-br, inglês e espanhol;
A recuperação dos metadados através de mecanismos de busca avançada, que permitem a busca por elementos como as categorias de informação 
(ex: Solos, Altimetria, Vegetação, etc), retângulo envolvente do produto documentado, palavra-chave, etc.;
A carga e exibição de metadados nos principais padrões internacionais: ISO-19115/ 19139, FGDC e Dublin-Core;
A adesão a padrões de serviços OGC (Open Geospatial Consortium).


Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Para uso adequado da tecnologia de posicionamento GPS, é necessário diferenciar o que é uma observável, um modelo matemático e um método de posicionamento. 

Trata-se de um método de posicionamento:


A. ambiguidade;
B. dupla diferença de fase;
C. efemérides precisas;
D. pseudodistância;
E. estação virtual.

Análise das questões:
- A – Ambiguidade: parâmetro a ser estimado, não é método.
- B – Dupla diferença de fase: técnica de modelagem para eliminar erros, não é método de posicionamento.
- C – Efemérides precisas: dado/modelo orbital, não é método.
- D – Pseudodistância: observável medida pelo receptor, não é método.
- E – Estação virtual: sim, é um método de posicionamento (utilizado em redes de referência GNSS para gerar dados sintéticos próximos ao usuário, 
permitindo posicionamento em tempo real com alta precisão).


O que é a Estação Virtual?
- É um método de posicionamento diferencial que utiliza uma rede de estações de referência GNSS.
- Em vez de o usuário depender de uma única estação base próxima, o sistema cria uma estação “virtual” exatamente nas proximidades do receptor móvel.
- Essa estação virtual gera dados sintéticos como se houvesse uma base física ali, permitindo correções muito mais precisas.

⚙️ Como funciona
- Rede de referência: várias estações GNSS fixas enviam seus dados para um centro de controle.
- Processamento: o centro calcula os erros (ionosfera, troposfera, órbita, relógio) e modela o ambiente.
- Criação da VRS: o sistema gera observáveis simuladas de uma estação fictícia próxima ao usuário.
- Correções: o receptor móvel recebe essas correções em tempo real (RTK – Real Time Kinematic).

🎯 Vantagens
- Alta precisão: coordenadas com erro centimétrico ou milimétrico.
- Maior cobertura: não depende de estar perto de uma estação física.
- Eficiência: reduz custos e aumenta a confiabilidade em levantamentos topográficos, engenharia e geodésia.

📌 Exemplo prático
Imagine que você está fazendo um levantamento topográfico em Goiás.
- Sem VRS: precisaria instalar uma base física próxima.
- Com VRS: basta conectar-se à rede GNSS, que cria uma estação virtual ao seu lado, fornecendo correções instantâneas para seu receptor.

Ano: 2016 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEGEP - Analista Ambiental - Área Geoprocessamento - 2016 
Um Modelo Numérico de Terreno − MNT é uma representação matemática computacional da distribuição de um fenômeno espacial que ocorre dentro de uma região 
da superfície terrestre. Com relação ao MNT,

A. não é usado para análises de corte-aterro para projeto de estradas e barragens.
B. o processo de geração de um modelo numérico de terreno pode ser dividido em 2 etapas: a primeira é a aquisição das amostras ou amostragem e a segunda é a geração do modelo propriamente dito ou interpolação.
C. só pode ser representado por equações analíticas jamais por uma rede (grade) de pontos.
D. não pode ser obtido a partir de pontos coletados em campo.
E. não serve para representar dados geofísicos.

Alternativa "B".
Análise das alternativas:
A -> ❌ Incorreto. O MNT é justamente usado para cálculos de corte e aterro em obras de engenharia.
B -> CORRETO
C -> Incorreto. O MNT pode ser representado por grades regulares ou irregulares de pontos, além de equações.
D -> Incorreto. Pode sim ser obtido diretamente de levantamentos topográficos.
E -> Incorreto. O MNT pode representar não só relevo, mas também fenômenos geofísicos (ex.: variação de campo magnético, gravimetria).

Ano: 2016 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - IBGE - Analista - Área Geoprocessamento - 2016
Ao se modelar um problema a ser solucionado com auxílio de um Banco de Dados Geográficos, ou um SIG, durante a elaboração do Projeto Lógico, 
deve-se ter especial atenção:

A. à linguagem de implementação, às estruturas de dados e aos objetivos do sistema;
B. aos requisitos do usuário, ao domínio da aplicação e aos objetivos do sistema;
C. aos requisitos do usuário, aos objetivos do sistema e à linguagem de implementação;
D. aos requisitos do usuário, ao domínio da aplicação e às estruturas de dados;
E. ao domínio da aplicação, aos objetivos do sistema e às estruturas de dados.

A assertiva correta é a letra B.

Requisitos do usuário

• Declarações em linguagem natural e também em diagramas sobre as funções que o sistema deve fornecer e as restrições sob as quais deve operar.

● Requisitos do sistema

• Um documento estruturado que estabelece detalhadamente as funções e as restrições de sistema. 
Escrito como um contrato entre o cliente e o desenvolvedor do software.

● Especificação do software • Uma descrição detalhada do software que serve como base para projeto e a implementação. Escrito para os desenvolvedores

Disponível em :https://www.dcce.ibilce.unesp.br/~ines/cursos/eng_soft/aula04.pdf

Ano: 2016 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEGEP - Analista Ambiental - Área Geoprocessamento - 2016 
O Geodatabase é um banco de dados que armazena informações espaciais e de atributos. 
As informações espaciais e de atributos podem ser relacionadas por meio de identificadores comuns chamados de

A. dados alfanuméricos.
B. contigência.
C. algoritmos.
D. geocódigos.
E. operadores algébricos.

A alternativa "A" -> Geocódigos.


Ano: 2016 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEGEP - Analista Ambiental - Área Geoprocessamento - 2016 
Através de um SIG, é possível fazer o monitoramento do avanço de pastagens sobre a Floresta Amazônica. Esse monitoramento é obtido através do formato:

A. poligonal.
B. raster.
C. isogonal.
D. vetorial.
E. digital.

O formato raster é o mais adequado para monitoramento ambiental em grandes áreas, como a Floresta Amazônica, pois permite a análise de imagens de satélite e dados contínuos. 
Está de acordo com o gabarito da banca.
Fundamentação: O formato raster é composto por uma matriz de células ou pixels, cada um com um valor específico, permitindo a análise de imagens 
de satélite e dados contínuos.
O formato raster é amplamente utilizado em SIG para monitoramento ambiental, pois permite a análise de imagens de satélite e dados contínuos, 
sendo ideal para grandes áreas como a Floresta Amazônica.

Ano: 2014 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - DPE RJ - Técnico Superior Especializado em Engenharia de Agrimensura - 2014
Considerando o Sistema Global de Navegação por Satélite, analise as afirmativas abaixo, atribuindo V para afirmativa verdadeira e F para falsa.

As coordenadas geográficas são calculadas nos receptores por meio da projeção das cartesianas no elipsoide WGS84.

O código P enviado pelo satélite tem um período de 295 dias, sendo modulado em ambas as portadoras.

Os satélites GPS emitem continuamente somente duas frequências de rádio.

A sequência correta é:

A. V, F, F.
B. V, V, V.
C. V, F, V.
D. V, V, F.
E. F, V, V.

A primeira afirmação é verdadeira, pois as coordenadas geográficas são calculadas nos receptores GPS por meio da projeção das coordenadas cartesianas no elipsoide WGS84, 
que é o sistema de referência geodésico utilizado pelo GPS. 
A segunda afirmação é falsa, pois o código P (Precise) não tem um período de 295 dias; ele é um código de alta precisão usado em 
aplicações militares e não está relacionado a um período de 295 dias. 
A terceira afirmação é falsa, pois os satélites GPS emitem mais de duas frequências de rádio, sendo as principais L1 e L2, 
mas também há a L5 em satélites mais recentes.


Ano: 2014 /Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - DPE RJ - Técnico Superior Especializado em Engenharia de Agrimensura - 2014
Os diversos DOPs (Dilution of Precision), frequentemente usados em navegação e no planejamento de observações GNSS, 
auxiliam na indicação da precisão dos resultados que serão obtidos. Um dos fatores dos quais os DOPs dependem é:

A. a precisão da observação de pseudodistância, expressa pelo erro equivalente do usuário.
B. a variação do posicionamento vertical do receptor, expressa pelo VDOP.
C. a variação temporal de coleta nas estações, expressa pelo TDOP.
D. a precisão da observação da fase da onda portadora.
E. a precisão expressa pelo HDOP com relação aos locais de coleta das observações.


Ano: 2008 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - Prefeitura de São Paulo - Especialista em Meio Ambiente - Área Geografia - 2008
Sobre o Sistema UTM (Universal Transversa de Mercator), considere:

I. É um sistema de representação plana da Terra, em forma de um elipsóide, em que são utilizados cilindros transversos secantes.
II. O Meridiano Central (MC) é uma ordenada móvel, pois cada fuso terá um M C.
III. Para evitar valores negativos, são acrescidos 10.000.000 metros às ordenadas do Hemisfério Norte e 700.000 metros às abscissas.
IV. A Terra é dividida em 60 fusos de 6 graus de longitude e em zonas de 4 graus de latitude.
V.  O número de fusos não deve estar atrelado às especificações do acordo da Carta Internacional do Mundo ao Milionésimo.

Está correto o que se afirma APENAS em

A. I, III e IV.
B. I, II e IV.
C. II, III e V.
D. II, IV e V.
E. III, IV e V.

Gabarito 'B'.

Sistema UTM: avaliação das assertivas
I   — Correta: O UTM usa a projeção de Mercator Transversa sobre um elipsóide de referência, com fator de escala 0,9996 no meridiano central, 
o que equivale a um cilindro transversal secante.
II  — Incorreta: Cada fuso tem seu próprio meridiano central, mas chamá-lo de “ordenada” é errado. No UTM, a ordenada é a coordenada Norte (y), 
e o meridiano central está associado ao eixo das abscissas (x), com falsa origem de 500.000 m.
III — Incorreta: Para evitar valores negativos, no UTM adiciona-se 10.000.000 m às ordenadas no Hemisfério Sul (não no Norte). 
E a falsa abscissa padrão é 500.000 m, não 700.000 m.
IV  — Incorreta: São 60 fusos de 6° de longitude, correto; porém as bandas de latitude do UTM têm 8° (não 4°).
V   — Incorreta: O número de fusos (60) decorre justamente da divisão de 360° por 6°, alinhada historicamente às convenções cartográficas internacionais 
(a Carta Internacional ao Milionésimo adotava 6° em longitude), ou seja, a relação existe.


Ano: 2008 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - Prefeitura de São Paulo - Assistente de Suporte Técnico - Área Suporte e Infra-estrutura / Agrimensura - 2008
O levantamento pelo método GPS é recomendado para:

A. transformação de coordenadas.
B. transporte de coordenadas.
C. correção de coordenadas.
D. caminhamento de poligonais.
E. transporte de cotas.

- A – transformação de coordenadas
❌ Não é a finalidade principal do levantamento GPS. Transformação é um processo matemático posterior.
- B – transporte de coordenadas
✅ Correto. O GPS é recomendado para transportar coordenadas de pontos conhecidos para pontos novos, garantindo precisão e eficiência.
- C – correção de coordenadas
❌ Correções podem ocorrer, mas não é o objetivo principal do levantamento.
- D – caminhamento de poligonais
❌ Poligonais são métodos clássicos de topografia, não a aplicação típica do GPS.
- E – transporte de cotas
❌ O GPS pode fornecer altitudes, mas o transporte de cotas é mais confiável com nivelamento geométrico.


Ano: 2007 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - MPU - Analista - Área Pericial Geografia - 2007

Dentre os tipos de resolução que caracterizam as imagens obtidas por sensoriamento remoto são consideradas muito importantes: 
a resolução espectral, a resolução espacial e a resolução radiométrica.

A resolução radiométrica indica

A. a que faixa do espectro eletromagnético correspondem os processamentos fotográficos efetuados, assim como o número de medidas.
B. o número de medidas registradas referentes a determinadas áreas e a determinados pixels.
C. os valores digitais registrados para cada banda e essa, por sua vez, é definida como uma seleção de comprimentos de onda do espectro eletromagnético.
D. os valores digitais registrados por cada pixel, o qual representa a menor unidade de informação em uma imagem.
E. o sistema sensor, que é determinado pela órbita da plataforma e pela amplitude imageada em cada passagem.


A -> Isso descreve resolução espectral, não radiométrica.
B -> Fala em “número de medidas registradas por área/pixel”, que aparenta se referir a frequência ou quantidade de amostragens, 
mas isso não representa resolução radiométrica. Resolução radiométrica é sobre níveis de cinza (quantização), não número de medidas.
C -> Isso é definição de resolução espectral (divisão do espectro em bandas), não radiométrica.
D -> Esta é a definição correta de resolução radiométrica. Radiometria = número de níveis de energia que cada pixel pode registrar (ex.: 8 bits → 256 níveis).
E -> Fala de órbita e de área imageada → relacionado à resolução temporal (revisita)

A resolução radiométrica mede a capacidade do sensor de discriminar níveis de energia, representados pelos valores digitais de cada pixel → Alternativa D.


Ano: 2006 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEPLOG MA - Analista Ambiental - Área Geografia - 2006
A definição do georreferenciamento das representações gráficas é:

A. conversão de um sistema de coordenadas geográficas para coordenadas UTM.
B. obtenção da declinação magnética de mapas e imagens.
C. modificação do azimute de referência de mapas ou imagens.
D. alteração do elipsóide de conferência e da reambulação dos mapas.
E. associação de um sistema de coordenadas conhecido a um mapa ou imagem de satélite.

Altenativa "E" - Associação de um sistema de coordenadas conhecido a um mapa ou imagem de satélite.

Ano: 2006 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEPLOG MA - Analista Ambiental - Área Geografia - 2006

A análise do índice de vegetação é uma das técnicas mais utilizadas em processamento de imagens para obtenção de informações sobre a biomassa. 
Considerando as características espectrais dos diversos sistemas sensores orbitais, as bandas utilizadas para obtenção deste índice correspondem à radiação

A. do infravermelho médio e do infravermelho termal.
B. do verde e do infravermelho próximo.
C. azul e do infravermelho próximo.
D. do infravermelho médio e do infravermelho próximo.
E. do vermelho e do infravermelho próximo.

O NDVI (Normalized Difference Vegetation Index) é o índice mais usado para estimar biomassa e vigor da vegetação.
Ele se baseia na diferença entre a reflexão no infravermelho próximo (NIR) e a reflexão no vermelho (RED):

- Vermelho (RED): a vegetação absorve fortemente essa faixa para realizar fotossíntese.
- Infravermelho próximo (NIR): a vegetação reflete bastante nessa faixa devido à estrutura celular das folhas.

Essa diferença é o que permite discriminar áreas com maior ou menor biomassa.

E – vermelho e infravermelho próximo ✅ Correto. Essa é a combinação clássica para cálculo do NDVI e outros índices de vegetação.

- NDVI é o mais usado mundialmente, simples e eficiente.-> Vermelho (RED) e Infravermelho Próximo (NIR)
Estimar biomassa, vigor da vegetação, monitoramento agrícola
- EVI é preferido em florestas tropicais e áreas com vegetação densa, pois evita saturação. Azul (BLUE), Vermelho (RED), Infravermelho Próximo (NIR)
Corrige efeitos atmosféricos e saturação em áreas densamente vegetadas
- SAVI é útil em regiões semiáridas, onde o solo exposto influencia bastante.Vermelho (RED) e Infravermelho Próximo (NIR)
Minimiza influência do solo em áreas com vegetação esparsa
- GNDVI é ótimo para monitorar saúde da planta e detectar deficiências nutricionais.
Verde (GREEN) e Infravermelho Próximo (NIR)
Estimar teor de clorofila, monitoramento de estresse hídrico

Ano: 2006 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - SEPLOG MA - Analista Ambiental - Área Geografia - 2006
Quando um fluxo de energia eletromagnética incide sobre um objeto pode ocorrer a transmitância, que pode ser explicada por:

A. parte da radiação incidente consegue atravessar o objeto, se o material é transparente.
B. parte da radiação incidente consegue atravessar o objeto, se o material for opaco.
C. reflexão difusa, se o material for translúcido.
D. reflexão especular, se o material for translúcido.
E. parte da energia incidente é absorvida pelo objeto.

Alternativa "A"

B -> INCORRETO - Se for opaco, não atravessa.
C -> Isso é reflexão, não transmitância.
D -> Também é reflexão, não transmitância.
E._> Isso é absorção, não transmitância.

Resposta correta: A – parte da radiação incidente consegue atravessar o objeto, se o material é transparente. 
            
       
        '''            

    def menu (self):
                self.print_slow('Bem vindo aos estudos de geoprocessamento...')
                self.dots()
                while True:
                    try:        
                        indice = int(input('''
                        Estudos de geoprocessamento:

                        [1] - Cartografia
                        [2] - Exercícios 
                        [3] - Coordenadas Geográficas
                        [4] - Exercícios 
                        [5] - Projeções Cartograficas
                        [6] - Exercícios
                        [7] - Geodésia
                        [8] - Exercícios
                        [9] - Geoprocessamento
                        [10]- Exercícios
                        [0] - Sair

                        Escolha: '''))

                        if indice == 1:
                            self.print_slow_2(self.cartografia())
                        if indice == 2:
                            self.print_slow_2(self.exercicios_cart())     
                        if indice == 3:
                            self.print_slow_2(self.coordenadas_geograficas()) 
                        if indice == 4:
                            self.print_slow_2(self.exercicios_coordenadas())
                        if indice == 5:
                            self.print_slow_2(self.projecoes_cartograficas())    
                        if indice == 6:
                            self.print_slow_2(self.exercicios_proj_car()) 
                        if indice == 7:
                            self.print_slow_2(self.geodesia())  
                        if indice == 8: 
                            self.print_slow_2(self.geod_a())
                        if indice == 9:
                            self.print_slow_2(self.geoprocessamento())  
                        if indice == 10:
                            self.print_slow_2(self.exercicios_geo_proc())                                                                                                                                                  
                        if indice == 0:
                            self.print_slow_2('Saindo...')                    
                            break
                        else:
                            self.print_slow('Escolha inválida. Tente novamente')
                    except ValueError:
                        self.print_slow('Somente valores inteiros')       

if __name__=='__main__':
     
    Geoprocessamento = geoprocessamento()
    Geoprocessamento.menu()

                
