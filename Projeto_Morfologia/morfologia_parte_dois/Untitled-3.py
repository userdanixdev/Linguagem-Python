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
        output_text = []

        def toggle_pause():
           nonlocal paused
           paused = not paused

        def go_back():
                nonlocal i
                if i > 0:
                    i -= 1  
                    last_char = output_text.pop()
                    if last_char == '\n':
                        sys.stdout.write("\033[F\033[K")  # Move para a linha anterior e apaga
                    else:
                        sys.stdout.write("\b \b")  # Apaga o último caractere
                    sys.stdout.flush()

        keyboard.on_press_key("space", lambda _: toggle_pause())
        keyboard.on_press_key("left", lambda _: go_back())     
        #keyboard.on_press_key("space", lambda _: toggle_pause())

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
            output_text.append(char)
            sleep(0.06)
            while paused:
                sleep(0.1)
            i += 1
        print(Style.RESET_ALL)

    def preposicoes(self):
        return '''Classificações das preposições:
        
        - essenciais: a, ante, após, até, com, contra, de, desde, em, entre, para, per, perante, por, sem, sob, sobre, trás.
        - acidentais: afora, conforme, consoante, durante, exceto.
        
        Locução prepositiva:
        [yellow]- abaixo de, acerca de, a fim de, ao lado de, apesar de, através de, de acordo com, em vez de, junto de, para com, perto de.[reset]
        
        [bg_red] A palavra 'afim' junto é adjetivo para qualificar o substantivo.
        Emprego das preposições:

        - Combinação:
                ao ( 'a' preposição + 'o' artigo)
                aos ( 'a' preposição + 'os' artigo no plural)
                aonde ( 'a' preposição + 'onde' pronome relativo)
        - Contração: Mudança das palavras --

                do    ( de + o  )
                dum   ( de + um )
                desta ( de + esta)

[bg_red] Não se deve contrair a preposição 'de' com o artigo que encabeça o sujeito de um verbo...[reset]

    [bg_red] O sujeito da oração deve se iniciar SEM preposição: [reset]

    Está na hora DA onça beber água. [bg_red] ERRADO [reset] - [green] a onça é o sujeito

    Está na hora DE A onça beber água. [bg_red] CORRETO [reset] - [green] a onça é o sujeito       

[bg_red]A preposição não pode ser a primeira palavra do sujeito, o sujeito deve ser iniciado com um artigo ou pronome.[reset]

    Chegou a hora DELE sair. [bg_red] ERRADO [reset] - [red] Não se deve colocar a preposição para fazer parte do sujeito da oração.

    Chegou a hora DE ELE sair. [bg_green] CERTO [reset] - [green] O correto é ele sair...[reset]

As preposições assumem estes valores:

de lugar: ver DE PERTO.
de origem: ele vem DE Brasília.
de causa: morreu DE fome.
de assunto: falava DE futebol.
de meio: veio DE trem.
de posse: casa DE Paulo.
de matéria: chapéu DE palha.

[bg_yellow] A preposição pode ser a mesma palavra mas o sentido é diferente dependendo do contexto. [reset]

Segue exemplos:

    Ele queria antiguidades NO museu. [blue] [ no = preposição 'em' + artigo 'o'] [reset]

[green] A preposição acima 'em' é de contato próximo, de estar dentro. Ou seja, ele vai vender DENTRO do museu. [reset]

    Ele queria vender antiguidades AO museu. [blue] [ 'a' preposição + 'o' artigo ] 

[green] A preposição 'a' é de a caminho de fora para dentro, em destino. O sentido muda para que o museu que irá comprar.[reset]

Identificar as locuções prepositivas:

    - Apesar de João ter saído cedo, de acordo com as instruções de seu pai, não chegou a tempo.

    Locuções prepositivas: [blue] apesar de, de acordo com [reset]

    - Em vez de Marcia ficar perto de mim, ela preferiu ficar junto de ti.

    Locuções prepositivas: [blue] em vez de, perto de, junto de [reset]
        '''
    def adjetivo (self):
        return ''' Adjetivos: Professor Marcio Wesley:

A palavra 'adjetivo' significa 'colocado ao lado de', 'justaposta a':
    é a palavra que qualifica e passa características ou atributos do substantivo.

Há conjuntos de palavras que tem valor de adjetivo: são as preposições adjetivas.

    As locuções são normalmente formadas por uma preposição e um substantivo ou por uma preposição e um advérbio.

        O passeio de carro.

        'de carro'  => preposição + substantivo -> locução adjetiva
        'o passeio' -> substantivo

O adjetivo concorda em gênero com o substantivo a que se refere: FLEXÃO DE GÊNERO

    Um comportamento estranho. //     Uma atitude estranha.

    Um jornalista ativo.       //     Uma jornalista ativa.

    Os adjetivos biformes possuem uma forma para o gênero masculino e outra para o feminino.

    [bg_red] Nos adjetivos compostos formados por dois adjetivos, apenas o último elemento sobre flexão:[reset]
    [bg_red] Se for em número, plural. Flexiona somente o último elemento:

    cidadãos luso-brasileiros // cidadãs luso-brasileiras

    Cidadão luso-brasileiro / cidadã luso-brasileira
    Casaco verde-escuro // saia verde-escura
    consultório médico-dentário // clínica médico-dentária

    O 'surdo-mudo' varia os dois elementos para os gêneros:

        Rapaz surdo-mudo / Moça surda-muda

Existem também os adjetivos  que apresentam uma unica fforma tanto para o masculino como feminino: OS UNIFORMES.

    Pássario frágil / ave frágil
    Ator ruim / atriz ruim
    Empresa agrícola / planejamento agrícola
    Homem audaz / mulher audaz

    ATENÇÃO! [bg_red] São uniformes os adjetiuvos compostos em que o segundo elemento é substantivo! [reset]\n
    [bg_red] Também são invariáveis os compostos 'azul-marinho' e 'azul-celeste'[reset]\n

        Casaco amarelo-limão / camisa amarelo-limão -> [blue] limão é substantivo [reset]
        carro verde-garrafa  / bicicleta verde-garrafa -> [blue] garrafa é substantivo [reset]
        papel verde-mar      / tinta verde-mar -> [blue] mar é substantivo [reset]

        FLEXÃO DE GRAU DO ADJETIVO:

        Servem para comparar ou intensificar as características que atribuem. O comparativo e superlativo.

            Grau Comparativo:

        Compara-se a mesma característica atribuida a dois ou mais seres ou duas ou mais caracteríticas atribuidas a um mesmo ser.

        Comparativo de igualdade: Ele é [yellow] tão exigente quanto [reset] justo.

                                    Ele é [yellow] tão exigente quanto [reset] (ou como) seu irmão.           

                                    
        [bg_red]ATENÇÃO! o GRAU COMPARATIVO PODE SER DE DUAS QUALIDADES DE UMA PESSOA [reset]

        Comparativo de superioridade: Estamos [yellow] mais atentos (do) que [reset] eles.

                                        Estamos [yellow] mais atentos (do) que [reset] ansiosos.  

        ATENÇÃO. A partícula 'do' é facultativa, não altera o sentido e nem as normas.                                         
                
        ATENÇÃO! [bg_red] O grau de comparação é para o adjetivo e não ao substantivo! [reset]                                            

                Fulano é [yellow]muito[reset] inteligente -> 'muito' é o grau comparativo de superioridade ao adjetivo 'inteligente'
                              

        Comparativo de inferioridade: Somos [yellow] menos passivos (do) que [reset] eles

                                        Somos [yellow] menos passivos (do) que [reset] tolerantes.   

Tanto os graus comparativos de inferioridade e de superioridade existem as formas analíticas e sintéticas.

    Os adjetivos BOM, MAU,  GRANDE , PEQUENO em sua forma sintética de superioridade ficariam:

        MELHOR, PIOR, MAIOR, MENOR de coisas diferentes.

        Essa solução é [yellow] melhor (do) que[reset] a outra.  <- [bg_red] Não utiliza BOM, são coisas diferentes. [reset]

            Minha voz [yellow]é pior (do) que[reset] a sua. <- [bg_red] Não usa MAU, comparação de duas pessoas. [reset]

            O descaso pela miséria é [yellow]maior (do) que[reset] o senso humanitário. <- [bg_red] Não utiliza GRANDE, a frase está comparando coisas diferentes. [reset]

            A preocupação social é [yellow] menor (do) que [reset] a ambição individual. <- [bg_red] Não utiliza PEQUENO, a frase está comparando coisas diferentes. [reset]

                Grau comparativo de superioridade analítico:

As formas analíticas do grau comparativo de superioridade devem ser usadas quando se comparadas a 2 características do mesmo ser:

        Forma correta -> Ele é [yellow] mais bom (do) que [reset] inteligente. <- [green] 'mais' -> advérbio + 'bom' adjetivo. [reset]

            [blue] Portanto, grau comparativo de superioridade analítico. [reset]
        
        Todo corrupto é [yellow] mais mau (do) que [reset] esperto. <- [green] 'mais' -> advérbio + 'mau' adjetivo. [reset]

            [blue] Portanto, grau comparativo de superioridade analítico. [reset]            

        Meu salário é [yellow] mais pequeno (do) que [reset] justo. <- [green] 'mais' -> advérbio de intensidade + 'pequeno' adjetivo. [reset]

            [blue] Portanto, grau comparativo de superioridade analítico. [reset]

        [bg_red] ATENÇÃO! Atente-se para não confundir 'menor' com grau comparativo de INFERIORIDADE. NÃO É! [reset]
        [bg_red] 'menor' é grau comparativo de SUPERIORIDADE que equivale a 'mais pequeno' -> adverbio + adjetivo [reset]

        Grau superlativo:

        Característica atribuída pelo adjetivo que é intensificada de forma RELATIVA ou ABSOLUTA.

O grau superlativo relativo pode exprimir  SUPERIORIDADE ou INFERIORIDADE e é sempre expresso de forma analitica:

    Grau superlativo de superioridade: Ele é [yellow]o mais atento[reset] de todos.

                                        Ele é [yellow]o mais exigente[reset] de todos os irmãos.

[bg_red] ATENÇÃO! O GRAU SUPERLATIVO RELATIVO É UMA RELAÇÃO QUE UMA PESSOA TEM COM OS OUTROS SERES. [reset] 

    Grau superlativo de INFERIORIDADE: Ele é [yellow]o menos atento[reset] de todos.

                                        Ele é [yellow]o menos exigente[reset] de todos os irmãos.

    O grau superlativo absoluto analítico:

        muito bom, bom demais

    O grau superlativo absoluto sintético:

        belíssimo, bonérrimo                                               
                           
        FGV/BANESTES: Técnico em segurança do trabalho

A frase que não apresenta qualquer forma de superlativação de um adjetivo é:

a. Sou estraordiariamente paciente desde que as coisas sejam feitas do meu jeito.
b. A lealdade a um partido reduz o maior dos homens ao nível mesquinho das massas.
c. O ouro é um metal amarelo ultra-apreciado.
d. Uma besteira menor, consciente, pode impedir uma besteira grande pra cachorro, inconsciente.

a. Sou estraordiariamente paciente desde que as coisas sejam feitas do meu jeito.

    [yellow] 'extraordianariamente' é um advérbio que está reforçando o adjetivo 'paciente' - Grau de superlativo analítico absoluto [reset]

b. A lealdade a um partido reduz o maior dos homens ao nível mesquinho das massas.

    [yellow] 'a lealdade'   => substantivo [reset]
    [yellow] 'a um partido' => é substantivo [reset]
    [yellow] 'a um partido' => é substantivo [reset]
    [yellow] 'reduz' => verbo [reset]
    [yellow] 'o maior dos homens' => adjetivo superlativo de superioridade referindo aos 'aos homens' que por sua vez é substantivo [reset]
    [yellow] 'nível' => substantivo [reset]
    [yellow] 'mesquinho' => adjetivo para o substantivo 'nível

c. O ouro é um metal amarelo ultra-apreciado.

    [yellow] Substantivos: 'o ouro', 'um metal' [reset]
    [yellow] Verbo : 'é' do verbo SER [reset]
    [yellow] Adjetivos: 'amarelo', 'ultra-apreciado' qualificando o substantivo 'metal'. 'ultra' é prefixo de grau superlativo [reset]

d. Uma besteira menor, consciente, pode impedir uma besteira grande pra cachorro, inconsciente.

    [yellow] besteira : substantivo [reset]
    [yellow] 'menor' : adjetivo que qualifica 'besteira' [reset]
    [yellow] 'consciente' : adjetivo que qualifica 'besteira' tambem [reset]
    [yellow] 'grande' : adjetivo para qualificar 'besteira' [reset]
    [yellow] 'pra cachorro' : adjetivo para itensificar 'grande' [reset]

e. Veja o meu caso: saí do nada e cheguei à extrema pobreza.

    [yellow] Adjetivo: 'extrema' [reset]
    [yellow] Substantivo: 'pobreza' [reset]

    [bg_yellow] A letra 'e' não recebe reforço para o adjetivo ou algum superlativo. [reset]

Exercício:

    a. Várias clínicas ________ (médico-cirúrgico) foram fiscalizadas durante a semana.\n
        [bg_red]Quando são dois adjetivos, a última palavra que sobre flexão de número: 'médico-cirúrgicas'\n[reset]
a. Várias clínicas [green]médico-cirúrgicas[reset] foram fiscalizadas durante a semana.

    b. Ele é um excêntrico. As paredes de sua casa são _________(amarelo-canário).
        [bg_red] Observe que 'canário' é um substantivo, o nome de um pássaro. Portanto, não sofre flexão.[reset]
b. Ele é um excêntrico. As paredes de sua casa são [green]amarelo-canário.[reset]

c. Suas camisas costumam ser __________________(amarelo-ouro). <- Observe que a segunda palavra é um substantivo 'ouro'.
         [bg_red] Portanto, nenhuma palavra sofre flexão.[reset]
    c. Suas camisas costumam ser [green]amarelo-ouro.[reset]

d. Além disso, ele costuma exibir uma boina _____________________(amarelo-limão). Apelidaram-no 'Amarelão'.\n
    [bg_red]A palavra 'limão' é substantivo. Portanto sem flexão, forma fixa mesmo.[reset]\n
    d. Além disso, ele costuma exibir uma boina [green]amarelo-limão.[reset]\n
    
e. Os métodos ______________(empregado) pelos especialistas não têm sido ______(eficaz).
    e. Os métodos [green]empregados[reset] pelo especializados não têm sido [green]eficazes.[reset]

f. Várias entidades _________(latino-americano) de defesa dos direitos ________(humano) protestaram contra as ações____________(policial).\n
[bg_red]Quando temos dois adjetivos 'latino-americano' somente a última palavra sofre alteração.[reset\n]
Várias entidades [green]latino-americanas[reset] de defesa dos direitos humanos protestaram contra as ações policiais.

g. Alguns torneios _________(esportivo)________________(afro-asiático) foram ________________(suspenso) devido à falta de empresas _________(patrocinador)\n
Alguns torneios esportivos [green]afro-asiáticos[reset] foram suspensos devido à falta de empresas patrocinadoras.\n
[bg_red]Repare que 'afro-asiático' são dois adjetivos, somente a última palavra flexiona.[reset]

h. Mulheres_______(surdo-mudo) fizeram um protesto contra a discriminação de que são vítimas quando procuram emprego.\n
[bg_red]A palavra 'surdo-mudo' são dois adjetivos. Somente o último flexiona. Há uma exceção nessa palavra: RARIDADE[reset]
Mulheres surdas-mudas fizeram um protesto contra a discriminação de que são vítimas....

i. Os documentos do ano passado estão nas pastas___________________(azul-marinho) a palavra 'azul-marinho' é invariável.
Os documentos do ano passado estão nas pastas azul marinho.
Os deste ano, nas pastas azul-celeste. ( também é invariável )

j. Os documentos do ano passado estão nas pastas___________________(azul-marinho) a palavra 'azul-marinho' é invariável.
    Os documentos do ano passado estão nas pastas azul marinho.
        Os deste ano, nas pastas azul-celeste. ( também é invariável )

k. Ela tem cabelos ___________________________(castanho-escuro) e olhos _________________(azul-turquesa).
    Quando temos duas palavras adjetivas somente a última varia.
    Ela tem cabelos [green]castanho-escuros[reset] e olhos azul-turquesa. ( Azul turquesa não tem variação na língua portuguesa, possui forma fixa.)

l. Aquelas cortinas ________________________(vermelho-sangue) dão um tom trágico ao ambiente. 
    [bg_red]'vermelho-sangue' - a palavra 'sangue' é substantivo, portanto a palavra composta não sofrerá alteração.[reset]
        Aquelas cortinas [green]vermelho-sangue[reset] dão um tom trágico ao ambiente. 

FGV: técnico de segurança do trabalho

A frase em que a substituição dos termos sublinhados por um adjetivo é feita de forma adequada:
        
a. Um beijo [yellow]de minha mãe[reset] fez de mim um pintor / maternal; [bg_red][ERRADO][reset] 
    [blue]É uma mãe específica, 'minha' pronome possessivo. seria MATERNAL no sentido geral.[reset]

b. O importante na obra [yellow]de arte[reset]: o espanto / arteira;[bg_red][ERRADO][reset] 
        [blue] Obra artística [reset]

c. Toda arte é imitação [yellow]da natureza[reset] / naturalista;[bg_red][ERRADO][reset] 
    [blue]se a natureza é imitada, ela é complemento nominal[reset] - [red]Sendo assim, não é locução adjetiva.[reset]
    [blue] Repare que não tem qualificação da arte , nem para a imitação. A 'imitação' substantivo é o que ele sofre. O passivo. 

d. Apreciar os defeitos [yellow]do próximo[reset] é ter talento? / alheios;[bg_green][CORRETO][reset] 

e. Avalia-se a inteligência [yellow]de um indivíduo[reset] pela quantidade de incertezas que ele é capaz de suportar / individualista
    [blue] Se fosse 'individual' tudo bem, individualista é egoísmo.[reset]

FGV: analista legislativo

'Essa segunda descrição é [yellow]mais[reset] detalhada e demonstra [yellow]mais[reset] observação. Naturalmente, se eu estive procurando tal pessoa,
a partir dessa descrição detalhada, posso encontrá-la com [yellow]mais[reset] facilidade. 

a. Os três vocábulos pertencem a três classes diferentes.
b. Os três vocábulos pertencem à mesma classe gramatical.
c. As duas últimas ocorrências documentam a classe dos pronomes.
d. As duas primeiras ocorrências documentam a classe dos advérbios.
e. A segunda ocorrência documenta uma classe gramatical diferente das demais.

...'segunda [blue]descrição[reset] é [yellow]mais[reset] [green]detalhada...'[reset]    

'descrição'  -> substantivo
' detalhada' -> adjetivo que qualifica o substantivo 'descrição'
'mais' -> itensifica o adjetivo com um advérbio de intensidade
    [bg_yellow] O primeiro 'mais' da frase é advérbio [reset]

'... demonstra [yellow]mais[reset] observação...'    

'demonstra' = verbo
' mais ' => um pronome indefinido para observação, que pode acompanhar ou substituir o substantivo em questão
' observação' -> substantivo

    [bg_yellow] O segundo 'mais' da frase é um pronome indefinido [reset]

'...encontrá-la com [greenn]mais[reset] facilidade.'    

'facilidade' -> substantivo
' mais' -> pronome indefinido para o substantivo 'facilidade'

[bg_yellow] O mais da terceira frase é um pronome indefinido. portanto a resposta correta é a letra C [reset]

Outra questão de concurso:

O vôo de Santos Dumont foi fruto de uma idéia revolucionária, assim como os micro-computadores e a rede que hoje chamamos de internet.

No texto, o segmento 'ideia revolucionaria' poderia ter trocado a ordem de suas palavras (revolucionária ideia) sem que isso modificasse suas classes gramaticais
isso pode ocorrer:

a. nova escultura
b. jovem professora
c. imigrante trabalhador
d. velho pescador
e. fanático marxista

a. nova escultura. [ A letra A não modifica suas classes gramaticais. ]

    nova - substantivo // escultura -> adjetivo

    Escultura nova - 
    escultura -> substantivo
    nova -> Adjetivo

b. jovem professora  
    
c. imigrante trabalhador    
d. velho pescador
e. fanático marxista'''        

    def locucao_adjetiva (self):
        return '''Locução Adjetiva : Prof Marcio Wesley\n
        Compõem a preposição 'de' + substantivo.
A locução adjetiva pode significar um adjetivo correspondente, porém, a locução não preserva o sentido ao substituir um pelo outro.

    A greve [yellow]de professores[reset] tem tomado proporções incontroláveis. 
    O movimento [yellow]docente[reset] se justifica em face da inércia do governo.

    Conselhor de pai (paterno) / conselho paterno

    'conselho' -> substantivo
    'de pai'   -> preposição + substantivo = [yellow] locução adjetiva [reset]

    Inflamação da boca (bucal) / inflamação bucal

    'inflamação' -> substantivo
    ' da boca' -> preposição + substantivo => [yellow]locução adjetiva [reset]

    Jornal de ontem

    'jornal' -> substantivo
    'de ontem' -> locução adjetiva -> preposição + advérbio

    CUIDADO ! duas palavras juntas e combinadas -> preposição + advérbio -> locução adjetiva mesmo 'ontem' sendo advbérbio
        
    
        Gente de longe

        'gente' -> substantivo
        'de longe' -> preposição 'de' + advérbio 'longe' -> locução adjetiva

        CUIDADO ! duas palavras juntas e combinadas -> preposição + advérbio -> locução adjetiva mesmo 'ontem' sendo advbérbio'''

    def artigo(self):
        return '''Artigo:
        
        Canção Mínima:
        No mistério do Sem-fim,
        Equilibra-se um planeta.
        E, no planeta, um jardim, e, no jardim, um canteiro, no canteiro, uma violeta, e, sobre ela, o dia inteiro,
        entre o planeta e o sem-fim, a asa de uma borboleta.
        
Nesse jogo de retomadas e acréscimos, os substantivos surgem inicialmente precedidos pelo artigo um (um planeta, um jardim)
e depois pelo artigo o (no planeta, no jardim). A diferença que essa troca de artigo estabelece constitui passagem do particular para o geral.
[bg_red][ERRADO]- 'um' planeta, artigo indefinido que expressa algo geral, 'um' jardim, artigo indefinido que expressa algo geral.[reset]\n
[bg_yellow] E, no planeta ( em + o ) algo particular, 'no' jardim ( em + o ) algo particular. A questão inverteu a afirmação.[reset]

A introdução do substantivo 'asa', no último verso do poema, precedido pelo artigo 'a', rompe o processo indicado na questão anterior, produzindo
o efeito de retomar o texto como um todo. [bg_red]ERRADO[reset]\n

Relacionando o título do poema e o percurso indicado pelo jogo de retomadas e acréscimos, é possível sugerir que esta é a forma gramatical de apontar
a interpenetração do universal com o particular. [bg_green]CORRETO[reset]\n

O artigo quando antepostos a palavras de qualquer classe gramatical, os artigos as transformam em substantivos. Chama-se de DERIVAÇÃO IMPRÓPRIA.

[bg_red] Atenção [reset] - A derivação imprópria somente muda a classe da palavra e não a escrita, a escrita é a mesma. [reset]\n
	É [yellow]um falar[reset] que não tem fim. [blue][falar é verbo, como o artigo esta anteposto, transforma em substantivo][reset]

	O assalariado vive [yellow]um sofrer[reset] interminável. [blue][sofrer é verbo, como o artigo esta anteposto, transforma em substantivo][reset]
[blue]	[assalariado é o participio do verbo assalariar - com o artigo 'o' anteposto, por derivação imprópria, é substantivo.][reset]

	[yellow]O aqui e o agora[reset] nem sempre se conjugam favoravelmente.
[blue] 'aqui' é advérbio de lugar [reset] - Virou um substantivo.

    Artigo Indefinido:\n
O artigo indefinido é no sentido geral, genérico. Indica seres da mesma espécie.
	Assume as formas: um, uma, uns, umas

	Queria ter [yellow]um[reset]cachorro, [yellow]um[reset] gato. [yellow] uns [reset] tucanos e [yellow] umas [reset] araras.\n
    Artigo Definido:\n
Artigo Definido: indica seres da mesma espécie com seu sentidoo particularizante. com sentido especifico.
	Assume as formas: o, a, os, as

	Meu vizinho gosta muito de animais: você precisa ver [yellow]o[reset] cachorro, [yellow]a[reset] gata, [yellow]os[reset] tucanos, [yellow] as [reset] araras.

    COMBINAÇÕES:

é frequente a combinação dos artigos definidos e indefinidos com preposições:

preposição 'a' + artigo definido  'o'  = ao
preposição 'a' + artigo definido  'os' = aos
preposição 'a' + artigo definido  'a'  = à
preposição 'a' + artigo definido  'as' = às
preposição 'de' + artigo definido 'o'  = do
preposição 'de' + artigo definido 'os' = dos
preposição 'de' + artigo definido 'a'  = da
preposição 'de' + artigo definido 'as' = das

preposição 'de' + artigo indefinido 'um'   = dum
preposição 'de' + artigo indefinido 'uma'  = duma
preposição 'de' + artigo indefinido 'uns'  = duns
preposição 'de' + artigo indefinido 'umas' = dumas

preposição 'em' + artigo definido 'o'   = no
preposição 'em' + artigo definido 'a'   = na
preposição 'em' + artigo definido 'os'  = nos
preposição 'em' + artigo definido 'as'  = nas

preposição 'em' + artigo indefinido 'uma'   = numa
preposição 'em' + artigo indefinido 'umas'  = numas
preposição 'em' + artigo indefinido 'um'    = num
preposição 'em' + artigo indefinido 'uns'   = nuns

preposição 'por(per)' + artigo definido 'os'  = pelos
preposição 'por(per)' + artigo definido 'o'   = pelo
preposição 'por(per)' + artigo definido 'as'  = pelas
preposição 'por(per)' + artigo definido 'a'   = pela

[bg_red] ATENÇÃO! [reset]

Eu vejo pessoas [yellow]pelo o[reset] coração [bg_red]FORMA ESCRITA ERRADA[reset]\n
[green] Repare que 'pelo' já tem o artigo na combinação, por + o. Atenção! [reset]
 
	[yellow]A forma correta é Eu vejo pessoas pelo coração.[reset]

    Exercício para fixação:

Comente o valor dos artigos destacados:

a. Estou levando produtos d[yellow]a[reset] região.
[blue] região específica , a região , usando o artigo definido 'a' com preposição.[reset] - [bg_green] FORMA CORRETA [reset]

b. O menino estava tão encabulado que não sabia o que fazer com [yellow]as[reset] mãos.\n
[blue] Muitas pessoas colocam o pronome possessivo 'suas' em '...com as suas mãos. é PLEONASMO.\n Pode retirar o pronome sem prejuízo gramatical.[reset]\n
[bg_blue] Deixe o artigo definido fazer o seu papel de especificador. [reset]\n
	    Ontem eu machuquei a [yellow]minha[reset] mão. [bg_red][ERRADO][reset]\n
	[blue] Ontem eu machuquei[reset] a mão. - [bg_green][CERTO][reset] - [yellow] Sem o pronome possessivo [reset]

c. Em poucos instantes, pôs-se a chorar e a chamar pel[yellow]a[reset] mãe. [bg_green] CORRETO [reset]
[blue] Mãe específica da pessoa especificada pelo artigo definido 'a' + preposição 'por' = 'pela' [reset]

e. Aquele era [yellow]o[reset] momento de minha vida. [bg_green] CORRETO [reset]
[blue] Artigo definido 'o' para um momento único.[reset]

f. Aquilo sim é que é [yellow]um[reset] homem.
[blue] 'um' no sentido único, mesmo sendo artigo indefinido [reset]

g. Deve ter passado [yellow]uma[reset] meia hora desde que ele saiu.
[blue] Artigo indefinido 'uma', valores aproximados [reset]

h. Ela tem [yellow]um[reset] talento!
[blue] 'um' serve com intensidade, mesmo sendo artigo indefinido [reset]

i. Ele é [yellow]o[reset] homem, ela é [yellow]uma[reset] mulher.
[blue] artigo definido 'o' para o 'homem' , no sentido único e 'uma' artigo indefinido para uma mulher qualquer.[reset]

Veja as diferenças de significados dos artigos:

a. 	Todo dia ele faz isso. -> [blue] qualquer dia em geral [reset]
	
	Todo [yellow]o[reset] dia ele faz isso -> [blue] Com artigo 'o'. Este dia é um dia único e específico com sentido de dia inteiro [reset]

b. 	Pedro não veio. -> [blue] Pedro qualquer [reset]

	[yellow]O[reset] Pedro não veio. -> [blue]Com o artigo, Pedro amigo, conhecido, aquele pedro [reset]

c. 	Essa caneta é minha. [blue] Umas das minhas canetas [reset]

	Essa caneta é [yellow]a[reset] minha.  -> [blue]Com o artigo 'a', uma caneta específica, única [reset]

d.	O dirigente sindical apresentou reivindicações dos trabalhadores na reunião. -> [blue]  Sem o artigo no plural, siginifica algumas, não todas as reivindicações...[reset]
	
	O dirigente sindical apresentou [yellow]as[reset] reivindicações dos trabalhadores na reunião -> [blue] com o artigo no plural 'as' todas as reivindicações [reset]

e. 	Chico Buarque, grande compositor brasileiro, é também escritor. -> [blue] Podemos ter outros escritores além de Chico Buarque [reset]
	
	Chico Buarque, [yellow]o[reset] grande compositor brasileiro, é também escritor. -> [blue] Com o artigo ele é o único grande compositor brasileiro. [reset]

Questão:

'... foram intimados a comparecer...'

'...não a fizeram...'

'...a sua oração...'

As três ocorrências do 'a' são, respectavamente:

a. preposição, pronome, preposição
b. artigo, artigo, preposição
c. pronome, artigo, preposição
d. preposição, pronome, artigo
e. artigo, pronome, pronome

O artigo deve aparecer ao lado do substantivo escrito...\n
O pronome fica no lugar da palavra, dos nomes, do substantivo... \n
A preposição serve para conectar e não sofre variação...\n

'...fora intimados a comparecer...' -> [yellow]preposição para ligação, [reset]
'... não a fizeram..' -> [yellow]quem não faz não faz algo, portanto, o pronome está substituindo alguém ou algo que não fizeram[reset]
'...a sua oração...'  -> [yellow]'oração' é substantivo que está acompanhado do artigo 'a'.  'sua' é um pronome possessivo.[reset]

Questão CEBRASPE/PRF:

'Nesse processo, desenvolveram-se os vários campos de saber vinculados aos sistemas de justiça criminal, polícia e prisão, voltados para
a identificação, para a explicação e para a prevenção....'

A coerência e os sentidos do texto seriam mantidos caso fosse suprimido o artigo 'os' no trecho 'desenvolveram-se os varios campos de saber..'

Com o artigo no plural significa que todos os campos do saber.
Agora, desenvolveram-se vários campos do saber , sem o artigo, significa que nem todos os campos do saber, somente alguns. Mudando o sentido.
[bg_red]ERRADO[reset] - Mantem a coerência mas o sentido NÃO!

DEPEN - Com o uso do artigo definido na contração 'do' em 'do projeto civilizador oitocentista', pressupõe que a autora parte do princípio
de que os leitores tenham conhecimento prévio acerca desse projeto.

No primeiro parágrafo não diz a respeito do projeto, porém, com a preposição 'de' + 'o' artigo infere que os leitores tenham conhecimento
prévio acerca do projeto. [bg_green]ITEM CORRETO[reset]

FGV:
A frase abaixo em que há erro no emprego ou na ausência do artigo definido é:

a. Não importa se o gato é preto ou branco, desde que ele pegue os ratos.
b. As grandes ideias sempre encontram os homens que as procuram.
c. As ideias concordam bem mais entre si do que os homens.
d. Todo o dia em que se trabalha é um dia perdido.
e. A virtude premeditada é a virtude do vício.

a. Não importa se o gato é preto ou branco, desde que ele pegue os ratos.[bg_green]CORRETO[reset]
[green] Artigo 'o' acompanhando o substantivo 'gato' e artigo 'os' acompanhando o substantivo 'ratos'.[reset]

b. As grandes ideias sempre encontram os homens que as procuram.[bg_green]CORRETO[reset]
[green] artigos 'as' referente ao substantivo 'ideias'. 'grande' é adjetivo. artigo 'os' para o substantivos 'homens'[reset]
[green] 'as' pronome referindo as 'ideias'[reset]

c. As ideias concordam bem mais entre si do que os homens.[bg_green]CORRETO[reset]
[green] 'as' artigo no plural significa totalidade que acompanha o substantivo 'ideias'[reset]
[green] 'os' artigo que acompanha o substantivo 'homens'[reset]

d. Todo o dia em que se trabalha é um dia perdido.[bg_red]ERRADO[reset]
[red]o artigo indefinido 'um' acompanha o substantivo 'dia' no sentido geral, genérico.[reset]
[blue] se fosse 'o' dia' perdido, artigo definido, estaria correto [reset]
[green] Todo dia é qualquer dia [reset]. Todo o dia é um só dia em particular, o dia todo. [reset]

e. A virtude premeditada é a virtude do vício.[bg_green]CORRETO[reset]
[blue] Todos os artigos acompanhando o substantivo. [reset]'''        

    def pronomes (self):
        return '''Pronomes:
        
- Substitui e ou acompanha o nome.

        	Pedro acordou tarde. [yellow]Ele[reset] ainda dormia, quando sua mãe o chamou.
            
    [blue]Pronomes[reset]: [yellow]Ele[reset] = Pedro (só substitui) // 'Sua' = mãe de pedro e acompanha o substantivo 'mãe' // 'O' pronome = Pedro (só substitui Pedro)

Pronome substantivo / pronome adjetivo:

Quando um pronome é empregado junto de um substantivo, ele é chamado de pronome adjetivo.
Quando um pronome aparece isolado, sozinho na frase, ele é chamado de pronome substantivo.

Ex: 
	[yellow]Ninguém[reset] pode adivinhar [yellow]suas[reset] vontades?
	
	[yellow]Ninguém[reset] -> [blue]pronome substantivo (pois está sozinho)[reset]
	[yellow]suas[reset]    -> [blue]pronome adjetivo ( acompanha o substantivo 'vontades')[reset]

	Encontrei [yellow]minha[reset] caneta mas não [yellow]a[reset] apanhei.

	[yellow]minha[reset]   -> [blue]pronome adjetivo ( está acompanhando o substantivo 'caneta' )[reset]
	[yellow]a[reset]       -> [blue]pronome substantivo ( está sozinho e substituindo alguém no discurso dentro contexto )[reset]


Teste: (1) pronome substantivo (2) pronome adjetivo

	[yellow]Estas[reset] montanhas escondem tesouros.
		- 2 pronome adjetivo porque acompanha o substantivo 'montanhas'

	[yellow]Aquilo[reset] jamais se repetirá. 
		- 1 pronome substantivo, isolado. Se refere a algo ou alguém que não aparece.

	[yellow]Qualquer[reset] pessoa [yellow]o[reset] ajudaria.
		- 'qualquer' -> 2 pronome adjetivo que acompanha o substantivo 'pessoa'
		- 'o' -> 1 pronome isolado, referindo-se a uma pessoa, substituindo-a, pronome substantivo.

	[yellow]Nossa[reset] esperança é que [yellow]ele[reset] volte.
		- 'nossa' -> 2 pronome adjetivo que está acompanhando o substantivo 'esperança'
		- 'ele' -> 1 pronome substantivo que está isolado, substituindo uma pessoa, alguém.

Questão:
	Assinale a alternativa em que o termo exerça, no texto, papel de adjetivo:

a. antropólogo  
O antropólogo Jesus Contreras e a antropóloga Mabel Gracia compreendem a cultura alimentar...
	- Nesse caso 'antropólogo' é substantivo, o artigo 'o' está definindo como substantivo.

b. cultura
De igual forma, a compartilharmos uma cultura, Contreras e Gracia afirmam que tendemos a atuar de forma similar como fazemos com a comida,
ou seja, somos guiados por orientações, preferências e sanções autorizadas por determinada cultura.
'uma cultura' - substantivo, 
determinada cultura - a palavra 'determinada' é adjetivo que qualifica o substantivo 'cultura'

c.essa ( pronome desmonstrativo )
Em diálogo com [yellow]essa perspectiva[reset], a antropóloga Maria Emília Pacheco, acessora da ONG fase e integrante do Fórum Brasileiro...'
'perspectiva' = substantivo
'essa' = pronome demonstrativo com papel de adjetivo.

d. adjetivo.
'...e não como um adjetivo.' ( artigo indefinido 'um', substantivo = 'adjetivo' acompanhada do artigo )

e. saberes
'...ela é fonte produtora de saberes,competências e programas de comportamento.'

'saberes', 'competências', 'programas de comportamento' = substantivo. 

[bg_green] Alternativa C, a correta [reset]

17. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP / Prova: IDCAP - Prefeitura de Vila Rica - Fonoaudiólogo - 2024

Isso' causa lesões, como ruptura de tímpanos, aneurismas e até costelas quebradas.
Morfologicamente, pelo contexto da frase, o vocábulo destacado trata-se de pronome:

A. Indefinido adjetivo
B. Demonstrativo adjetivo.
C. Demonstrativo substantivo.
D. Indefinido substantivo.

'isso' é um substantivo demonstrativo. 'isso' está substituindo um termo ou ideia anterior expressa, funcionando como substantivo mesmo. 
Isolado, sem qualificação.

'''

    def pronome_pessoal (self):
        return '''Em uma comunicação tem que ter o EMISSOR, RECEPTOR e a MENSAGEM.
	 As pessoas gramaticais: EMISSOR  -> 1º pessoa
			         RECEPTOR -> 2º pessoa
				 MENSAGEM -> 3º pessoa
                 
Pronomes pessoais do caso reto: Função de sujeito // O pronome que tem função de sujeito usa-se para conjugar VERBO.
    [green]eu[reset] estudo / [green]tu[reset] estudas / [green]ele[reset] estuda / [green]nós[reset] estudamos / [green]vós[reset] estudais / [green]eles[reset] estudam
Pronomes pessoais do caso oblíquo: não são sujeitos de uma oração.

[yellow]Pronomes pessoais do caso reto: EU, TU, ELE, Nós, vós, eles[reset] <- [blue] Pronomes pessoais do caso reto 1º pessoa do discurso.[reset]

Pronome do caso oblíquo átono e tônico: Não é sujeito da oração.

O pronome de caso oblíquo Tônico -> Vem com preposição:

        comigo ( preposição 'com' + ego)
        para mim ( preposição 'para' + pronome 'mim')
        de ti ( preposição 'de' + pronome 'ti')
        contigo  ( preposiçãao  'com' +  pronome 'ti')
        sobre si, consigo, entre ele, sobre ela

	- ÁTONO   -> Não vem preposição escrita:

        			me, te, se, o, a, lhe <- Singular
          			nos, vos, se, os, as , lhes  <- Plural  

                      [bg_red] Lembrando! [reset]

[bg_yellow]Um pronome pessoal é pronome reto quando exerce a função de sujeito da oração.[reset]\n
[bg_yellow]Um pronome pessoal oblíquo quando exerce função que não seja a de sujeito da oração.[reset]\n
                      
    Exemplos:

		[yellow]Ela[reset] pediu ajuda para [yellow]nós[reset]

        'ela' -> pronome pessoal do caso reto ( exercendo função de sujeito na frase)
        'nós' -> pronome pessoal oblíquo ( não é sujeito da oração)

  		[yellow]Nós[reset] jamais [yellow]a[reset] prejudicamos
          
        'nós' -> pronome pessoal do caso reto ( na frase o pronome exerce função de sujeito, portanto é do caso reto)
        'a'   -> pronome pessoal do caso oblíquo átono ( sem preposição )


        [bg_red]Os pronomes oblíquos átonos: nunca aparecem precedidos de preposição![reset]

    	A vida [yellow]me[reset] ensina a ser realista.

        ' a vida' -> substantivo e sujeito da oração // 'me' então é pronome pessoal oblíquo átono.
        
		A vida ensina [yellow]a você[reset] coisas importantes.

            'a você' -> 'você' é pronome e 'a' é preposição. ' a você' é a mesma função de 'me'

            [bg_red]Os pronomes oblíquos tônicos: sempre aparecem precedidos de preposição![reset]

            Os pronomes oblíquos tônicos: sempre aparecem precedidos de preposição!

	            Ela jamais iria [yellow]sem mim[reset]

	'sem mim' = 'sem' -> preposição + 'mim' pronome obliquo tônico

Os pronomes oblíquos tônicos precedidos de preposição 'com' combinam-se com 'ela' => comigo, contigo, consigo, conosco, convosco

[bg_red] Os pronomes oblíquos átonos : me, nos, te, vos, se -> podem indicar ação praticada pelo próprio sujeito. Tais pronomes são chamados de pronomes reflexivos.[reset]

	Eu [yellow]me[reset] machuquei. 'me' - ( a mim mesmo ) => [yellow]pronome reflexivo[reset]

    Os pronomes oblíquos tônicos: SI e CONSIGO são sempre reflexivos.

    	Márcia só pensa em [yellow]si[reset] -> ( pensa nela mesma ) <- [yellow] Pronome substantivo reflexivo pessoal do caso oblíquo tônico [reset]

       	Ele trouxe [yellow]consigo[reset] o livro -> ( com ele mesmo ) <- [yellow] Pronome adjetivo reflexivo pessoal do caso oblíquo tônico [reset]
           
	Maneiras erradas:

    	Marcos, eu preciso falar consigo [bg_red](ERRADO)[reset]
        [red] Não como seria 'contigo', além de ser pronome reflexivo em que pratica a ação é o próprio sujeito. [reset]
            [red] 'consigo' => preposição 'com' + pronome 'ti' referindo a 2º pessoa do discurso. [reset]
                    [green] O correto seria '... eu preciso falar contigo [reset] -> [blue]preposição 'com' + pronome pessoal oblíquo tônico[reset]
                        [yellow] Além disso os pronomes pessoais tônicos precisam anteceder preposição [reset]\n

        	Eu gosto muito de SI, minha amiga. [bg_red](ERRADO)[reset]            
            [red] 'SI' é pronome reflexivo, quem pode praticar a ação é o próprio sujeito.[reset]\n
            [red] Precisa de um pronome que refira a 2º pessoa do discurso, 'ti', pronome oblíquo tônico da 2º pesssoa que não é reflectivo. [reset]
            
            Emprego e colocação :

            Os pronomes pessoais oblíquos átonos:

                [yellow]o, a, os, as[reset] -> [blue]somente no lugar de trechos SEM preposição inicial.[reset]

                [yellow]lhe, lhes[reset]    -> [blue]somente no lugar de trechos COM preposição inicial.[reset] Preposições: a / de / para 

                Veja:
                Exemplo lhe,lhes:
                Devemos dar valor [yellow]aos pais[reset] -> 'a' - preposição + artigo 'os' -> Devemos dar-[yellow]lhes[reset] valor

                Exemplo o, a, os, as:
                Amo [yellow]os[reset] pais -> Amo-[yellow]os[reset] [blue] Repare que só tem o artigo, sem preposição, então usa-se os pronomes 'o','a','os','as'[reset]                    

                Apertei os pregos [yellow]da caixa[reset]  -> Apertei-[yellow]lhe[reset] os pregos.  [blue] Repare que tem preposição 'de' + artigo 'a' = 'da', então usa-se os pronomes 'lhe', 'lhes'.[reset]

                Apertei [yellow]os pregos da caixa.[reset] -> Apertei-[yellow]os[reset] - [blue] Artigo 'os' de pregos, pelo contexto 'os pregos da caixa' - assim podemos substituir por 'os' - Apertei-os.[reset]
                
                        [bg_red] ATENÇÃO! CUIDADO! [reset]

                        [bg_yellow]Existem pronomes que podem ficar no lugar de trechos COM ou SEM preposição: ME, TE, SE, NOS, VOS.[reset]

                        Eu [yellow]te[reset] amo / \n
                        Eu [yellow]a[reset] amo /\n
                        Dei - [yellow]lhe[reset] amor -> Dar algo a alguem...\n
                        Dei - [yellow]te[reset] amor /-> 

                        [bg_yellow] Repare que os pronomes estão em sua colocação correta e forma escrita correta [reset]

                        [red]Formas ERRADAS:[reset]

                    	Eu lhe amo / Dei-a amor -> O pronome 'a' não serve para o termo preposicionado, lembrando que o 'lhe' representa a preposição 'a'.
                        
                            O pronome LHE somente empregado para termos preposicionados.

        RESUMO:

        Pronomes 'o', 'a', 'os', 'as' - Função principal 'Objeto Direto' 

O objeto direto é um termo da oração que completa o sentido de um verbo transitivo direto, ligando-se a ele sem preposição.

O objeto direto é um complemento verbal, juntamente com o objeto indireto. O objeto indireto é um complemento verbal que é obrigatoriamente acompanhado por preposição

Visitei [yellow]os[reset] amigos   -> Visitei-[yellow]os[reset] \n
Visitamos [yellow]os[reset] amigos -> Visitamo-[yellow]los[reset] [blue] Final 's','n','z' perdem o final e sofre uma adaptação no pronome[reset]\n
Reformara[yellow]m a casa[reset]   -> Reformara[yellow]m-na[reset] [blue]Não é preposição + pronome: 'em'+'a'. É somente um adaptação.[reset]\n

Pronomes 'lhe','lhes' - Função principal - 'Objeto Indireto' :

O objeto indireto é um complemento verbal que é obrigatoriamente acompanhado por preposição:

	Informe [yellow]aos[reset] clientes o prazo -> Informe-lhes o prazo [blue] 'a' preposição + artigo 'os' => uso do pronome 'lhes' para substituição.[reset]
	Deram mais atenção a essa causa -> Deram-lhe mais atenção [blue] 'a' preposição + pronome demonstrativo 'essa' => uso do pronome 'lhe'[reset]
	Compare: Informe aos clientes [yellow]o prazo[reset] -> Informe-o aos clientes [blue] somente o artigo 'o' para substantivo 'prazo' -> uso do pronome 'o', sem preposição.[reset]

ME, TE, SE, NOS, VOS - Função principal de objeto direto quanto indireto:

	Os amigos [yellow]me[reset] visitaram.
	O professor [yellow]nos[reset] informou o prazo.
	Deram-[yellow]me[reset] mais atenção.


[bg_red]Mais um lembrete das preposições:[reset]
	
	[bg_yellow] a, ante, após, até, com, contra, de, desde, em, entre, para, per, perante, por, sem, sob, sobre, trás [reset]


ME, TE, SE, NOS, VOS - Função principal de objeto direto quanto indireto 

	Os amigos [yellow]me[reset] visitaram.
	O professor [yellow]nos[reset] informou o prazo.
	Deram-[yellow]me[reset] mais atenção.'''
            
    def colocacao_pronominal(self):
        return '''Sofrem alterações na grafia os pronomes com o verbo terminados em -R, -S, -Z diante dos pronomes o, a, os, as:
            
            	Veja: Vamos [yellow]cantar[reset] os hinos. -> [yellow]Final -R[reset]
                
                      Vamos cantá-los. ( o verbo cantar fica oxítona com final 'a' acentuada e o substantivo 'os hinos' pelo pronome pessoal oblíquo átono 'os' acrescentando a letra 'l' )

              		Cantamos os hinos -> Final -S // 'os hinos' -> substantivo para qual usamos o pronome pessoal do caso oblíquo átono 'os' acrescentando o 'l'.
                     
                     Cantamo-los <- Não acentua o verbo pois a sílaba tônica está no 'ta'- paroxítona e retira o S e acrescenta o pronome 'los'.

                     Fiz o relatório -> Terminação -Z retira e 'o relatório' substantivo a qual será substituido pelo pronome pessoal do caso oblíquo átono 'o' acrescentado de 'l'.

                        Fi-lo.

[bg_yellow] Sons nasais com finais -M, -ÃO, -ÕE DIANTE DOS PRONOMES O, A, OS, AS:[reset]

    Veja: Eles cantam os hinos. 

            'cantam' -> verbo com terminação -M
            'os hinos' -> substantivo que será substituido por pronome pessoal do caso oblíquo átono 'os' + alteração gráfica => 'nos'

                Eles cantam-nos.

                As alterações são: NO, NA, NOS, NAS

            Pais dão presentes aos filhos                

                'dão' -> verbo com som nasal , DAR
                'presentes' -> substantivo que poderá ser substituido por 'os' presentes

            Pais dão-nos aos filhos                

            Põe o livro aqui 

            'põe' -> final do verbo com som nasal.
            'o livro' -> substantivo que será substituido pelo pronome pessoal do caso oblíquo 'o' + alteração gráfica 'no'
            
            Põe-no aqui.

Questões:

	1. S. Leopoldo - RS, Advogado
A substituição das palavras grifadas pelo pronome está incorreta em:

A. 'que transpõe [yellow]um conceito moral[reset] - que o transpõe. [blue] Depois do verbo transpor seria 'transpõe-no' [reset]
										[yellow] 'que o transpõe'[reset] pronome antes, forma correta também [reset]

        [green] final do verbo com som nasal.[reset]
        [green] um conceito moral [reset] -> Pronome pessoal do caso oblíquo átono 'o' Se colocar o pronome depois do verbo seria 'transpõe-no' por regra.
        [green] Somente depois que a alteração ortografica acontece no pronome de 'o' para 'no' -> 'transpõe-no' [reset]                                        
        [green] A forme 'que o transpõe' está correta também, porém sem alteração ortográfica devido ao pronome estar antes do verbo [reset]

B. Em 'a democracia convida a um perpétuo exercício de reavaliação. Isso quer dizer que, para bem funcionar, [yellow]exige crítica. [reset]
Substituir 'exige crítica' por exige-a. [bg_green][CORRETO][reset]

C. 'o que expõe [yellow]o Brasil[reset]' - [green]o que o expõe.[reset] [bg_green][CORRETO][reset] [blue] Só irá alterar o pronome DEPOIS do verbo - 'expõe-no'[reset]

D. 'seria extirpar [yellow]suas camadas iletradas[reset]' - seria extirpar-lhes [bg_red][ERRADO][reset] 
		[blue] O pronome 'lhes' só fica correto no lugar de termo com preposição inicial [reset]
        [green] 'suas' é um pronome possessivo, sem preposição ao termo sublinhado. [reset]
		[bg_yellow] Seria extirpá-las [reset] - Oxítona com acentuação e perde o '-R' e adiciona a alteração ortográfica 'l' em 'las'[reset]

E. 'mais apto a exercer [yellow]a crítica[reset] - [green]mais apto a exercê-la[reset] [bg_green][CORRETO][reset]

        [green] Não confundir 'a crítica' com preposição', é um substantivo. [reset]
        [green] Verbo no final -R retira o r e adiciona o pronome pessoal do caso oblíquo átono 'o' com alteração ortográfica 'lo'[reset]
                                                                                  
    
    Colocação dos pronomes oblíquos átonos: ME, TE, SE, NOS, VOS, O, A, OS, As, LHE, LHES

        [bg_yellow] PRÓCLISE [reset]
        Pronome ANTES do verbo chama-se próclise: Eu te amo. // Você [yellow]me[reset] ajudou\n
        [bg_yellow] ÊNCLISE [reset]
        Pronome DEPOIS do verbo chama-se ênclise: Eu amo-te // Você [yellow]ajudou-me[reset].
        [bg_yellow] MESÓCLISE [reset]
        Pronome no MEIO da estrutura do verbo chama-se mesóclise: Amar-[yellow]te[reset]-ei // Ajudar-[yellow]te[reset]-ia.

        [bg_red]Regras básicas:[reset]\n
        	- Não iniciar oração com pronome oblíquo átono\n
        	- Não escrever tais pronomes após verbo no particípio:  Tenho  dedicado-me [bg_red](ERRADO)[reset]
		                                    						Tenho-me dedicado. [bg_green](CORRETO)[reset]\n
        	- Não escrever esses pronomes após verbo no futuro: Ele faria-me um favor. [bg_red](ERRADO)[reset]
							    Ele me faria um favor [bg_green](CORRETO)[reset]
    
            Próclise :

            Sabemos que próclise é o pronome que vem ANTES de verbo.

            Mas existem casos de próclise obrigatória, a facultativa e a proibida.

            Próclise Obrigatória: ( pronomes antes do verbo )

	1. Advérbios ( Frases em que contem advérbios, os pronomes devem ficar obrigatoriamente antes do verbo )
	2. Negações  ( Frases em que contem negações, os pronomes devem ficar obrigatoriamente antes do verbo )
	3. Conjunções Subordinativas ( que, se, quando, embora )
	4. Pronomes relativos (que, o qual, onde, quem, cujo )
	5. Pronomes demonstrativos ( este, esse, aquele, aquilo )
	6. Pronomes indefinidos (algo, algum, tudo, todos, vários )
	7. Exclamações ( Deus te abençoe! )
	8. Interrogações ( perguntas diretas ou indiretas )
	9. Prep: 'em' + Verbos no gerúndio ( exemplo: Em se tratando de Português, todo cuidado é pouco. )

Julgue os itens seguintes, quanto à colocação pronominal:

a. Jamais devolver-te-ei aquela fita. 
b. Deus pague-lhe esta caridade!
c. Tenho dedicado-me ao estudo das plantas.
d. Ali fazem-se docinhos e salgadinhos
e. Te amo, Maria!
f. Algo vos perturba?

a. Jamais devolver-te-ei aquela fita. [bg_red][Jamais é advérbio de negação e advérbio de tempo] - Próclise obrigatória[reset] - Portanto está errado.
	[blue] O correto seria: Jamais [reset][yellow]te[reset] [blue]devolverei aquela fita[reset]

b. Deus pague-lhe esta caridade! - [bg_red]ERRADO[reset][yellow][Frase com exclamação é para ter próclise obrigatória - ou seja, pronome antes do verbo.][reset]
    [blue] Deus [yellow]lhe[reset] pague esta caridade [reset]

c. Tenho dedicado-me ao estudo das plantas. [bg_red] Verbo no particípio, próclise obrigatória [reset]
    [blue] Tenho [yellow]me[reset] dedicado ao estudo das plantas. [reset] - [green] Pronome antes do verbo no particípio [reset]

d. Ali fazem-se docinhos e salgadinhos. [red] Ali se fazem docinhos e salgadinhos.[reset] [bg_red] Advérbio é próclise obrigatória [reset]
        [green] 'ali' é advérbio de lugar [reset]        

e. Te amo, Maria! [red] Início de oração com pronome oblíquo átono, ERRADO.[reset] - 
            [blue] O correto é: Amo te, Maria! [reset]
            [green] O pronome pessoal do caso reto EU não irá exigir próclise, portanto é correto também: EU TE AMO & EU AMO-TE[reset]

f. Algo vos perturba? [Próclise por ser pergunta, mas o termo está correto. Próclise obrigatória pronome antes do verbo.] [bg_green] CORRETO [reset]

Julgue quanto a colocação pronominal:

a. Eu me feri.
b. Eu feri-me.
c. Eu não feri-me.
d. O rapaz que ofendeu-te foi repreendido.
e. Em me chegando a notícia, tratarei de divulgá-la.

a. Eu me feri. [bg_green][CORRETO - Próclise facultativa][reset]
b. Eu feri-me. [bg_green][CORRETO - Ênclise facultativa][reset]
c. Eu não feri-me. [red] Palavras negativas o pronome deve vir antes, Próclise obrigatória [reset] [bg_red] ERRADO [reset]
d. O rapaz que ofendeu-te foi repreendido. [bg_red] Pronome relativo 'que', Próclise obrigatória, [reset] - [bg_red] ERRADO [reset]
				[green] O rapaz que te ofendeu foi repreendido.[reset]
e. Em me chegando a notícia, tratarei de divulgá-la. [bg_green] CORRETO[reset] -> preposição 'em' + pronome + verbo no gerúndio, correto. Próclise obrigatória.

Questão: Quadrix/CRF-RR

Essas iniciativas não se restringem à população brasileira, pois aproximadamente 60% da população mundial recorre, quase que exclusivamente, às plantas medicinais
como recurso terapêutico. Confirmando essa informação, a organização mundial da Saúde (OMS) estima que 85% da população dos países em desenvolvimento utilizem
as plantas medicionais nos cuidados primários de saúde.

    A posposição do elemento 'se' à forma verbal 'restringem' mantém a correção gramatical e os sentidos textuais.

    [bg_red] Colocar depois o elemento 'se' depois do verbo não mantém a correção gramatical pela palavra negativa 'não'. Pode até manter o sentido, mas por regra, não.[reset]
    [bg_red] Próclise obrigatória. [reset] [bg_red] ERRADO [reset]

    Colocação de pronomes na locução verbal - 2 ou mais verbos combinados.

	Se não houver caso de próclise, o pronome oblíquio está livre. Tanto antes do verbo, no meio ou depois.
	Se houver caso de próclise, o pronome só pode ficar antes do verbo auxiliar ou após o verbo principal.

	Lembrando em não começar uma oração com pronomes obliquos átonos.
	Não colocar pronomes oblíquos nos verbos no modo particípio e nem no verbo no futuro do presente e no pretérito.


Colocação de pronomes na locução verbal - 2 ou mais verbos combinados.

	Se não houver caso de próclise, o pronome oblíquio está livre. Tanto antes do verbo, no meio ou depois.
	Se houver caso de próclise, o pronome só pode ficar antes do verbo auxiliar ou após o verbo principal.

	Lembrando em não começar uma oração com pronomes obliquos átonos.
	Não colocar pronomes oblíquos nos verbos no modo particípio e nem no verbo no futuro do presente e no pretérito.


Exemplos:


	Elas lhe querem obedecer. 

	[yellow]'querem obedecer'[reset] -> [blue]locução verbal  [reset]
	[yellow] verbo principal:[reset] -> [blue]'obedecer'[reset] - Verbo principal é sempre o último. [bg_green]CORRETO[reset]
	 [yellow]verbo auxiliar:[reset]   [blue]'querem' - 	[reset]
		[green] Na frase temos um caso de próclise, em regra deverá ficar antes do verbo auxiliar e não do verbo principal.[reset]

        	Elas querem-lhe obedecer.

[red]	Não há caso de próclise na frase, portanto o pronome pessoal do caso oblíquo átono é livre para onde quiser ficar.[reset]

        	Elas querem obedecer-lhe.

	[red] Não há caso de próclise na frase, portanto o pronome pessoal do caso oblíquo átono é livre para onde quiser ficar.[reset]

        	Elas não querem-lhe obedecer. [bg_red]ERRADO[reset] [red]O pronome só pode ficar antes do verbo auxiliar ou após o verbo principal [reset]
					[bg_red] Não pode ficar no meio [reset]
	[bg_green]Além disso a próclise é obrigatória para frases negativas, portanto há duas formas corretas.[reset]

    			[green] Elas não lhe querem obedecer [reset] <- Próclise obrigatória ( antes do verbo auxiliar )
			[green] Elas não querem obedecer-lhe [reset] <- ênclise facultativa ( após o verbo principal )

            	Elas não querem obedecer-lhe. [bg_green]CORRETO[reset]

            	Elas não lhe querem obedecer. [bg_green]CORRETO[reset] A palavra negativa vai puxar o pronome. [reset]

    [bg_red] ATENÇÃO! [reset]

        Verbos no infinitivo fica indiferente aos casos de próclise.

        Veja: É importante não se [yellow]irritar[reset] à toa. 

                    [green]Repare que o verbo 'irritar' está no infinitivo.[reset]

                    [bg_yellow]Portanto a próclise é facultativa nesses casos.[reset]

                    É importante não [yellow]irritar-se[reset] à toa. [bg_green] Também está certo.[reset]

    Outros exemplos:

        	Encontrará lavrado o campo.  [red] 'encontrará' - verbo no futuro e o outro no particípio [reset]
					[red] 'lavrado' - verbo no particípio [reset]

		'o campo' -> substantivo que o pronome pessoal do caso oblíquo átono será substituido por 'o', pois está sem preposição.
								se tivesse com preposição seria o 'lhe'
		' encontrará' -> verbo no futuro

		Encontrará-o lavrado. [bg_red]ERRADO[reset] Precisa de adaptação
		Encontrará-lhe lavrado. [bg_red]ERRADO[reset] Não pode ser 'lhe', precisa de preposição
		Encontrará-lhe-á lavrado. [bg_red]ERRADO[reset] Não pode ser 'lhe', precisa de preposição
		lhe encontrará lavrado. [bg_red]ERRADO[reset] Não pode ser 'lhe', precisa de preposição
		
		Encontrá-lo-á lavrado [bg_green] CORRETO [reset]
        
            [yellow] encontrá ( oxítona ) + pronome 'o' + final do verbo 'a' // encontrá-lo-á [reset] 

Mais questões:

Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Turuçu - Enfermeiro - 2024 
Em “________ orientou-a”, para que o pronome “a” tenha que ficar, obrigatoriamente, após o verbo, a lacuna deve ser preenchida por qual das opções a seguir?

A.Sempre
B.Ninguém
C.Não
D.Antes,

A questão aborda a colocação pronominal, especificamente a próclise, ênclise e mesóclise, que são regras de colocação dos pronomes átonos em relação ao verbo. 
No caso específico, a questão pede que o pronome 'a' seja colocado obrigatoriamente após o verbo, o que caracteriza a ênclise. 
A ênclise é obrigatória em início de oração, após pausas e após certas palavras que atraem o pronome para depois do verbo.

 O item 'Sempre' é uma palavra que atrai o pronome para antes do verbo, caracterizando a próclise. 'sempre' é advérbio portanto é próclise obrigatória.
Portanto, a frase ficaria 'Sempre a orientou', o que não atende à exigência da questão.

 O item 'ninguem' é pronome indefinido quee atrai para antes do verbo, caracterizando próclise.

 O item 'não' é uma palavra negativa que atrai o pronomme para antes do verbo, caracteriznado próclise obrigatória.

 O item 'Antes,' seguido de vírgula, cria uma pausa que obriga a colocação do pronome após o verbo, resultando em 'Antes, orientou-a'.


Ano: 2024 / Banca: MS Concursos / Prova: MS Concursos - SAAE Manhuaçu - Ajudante Administrativo - 2024

Considerando as normas de colocação pronominal, assinale a alternativa que contém a frase gramaticalmente correta.

A.Jamais esquecerei-me daqueles momentos que passamos juntos.
B.Não aceitaram-me naquele emprego.
C.“Se vai a primeira pomba despertada”.
D.Dar-me-iam água para lavar as mãos?

Gabarito 'D'.

A questão aborda as normas de colocação pronominal na língua portuguesa, um tópico fundamental da gramática que trata 
da posição dos pronomes oblíquos átonos (me, te, se, nos, vos) em relação aos verbos. 
A correta colocação pronominal é essencial para a construção de frases gramaticalmente corretas e compreensíveis. 
As normas de colocação pronominal incluem a próclise, a mesóclise e a ênclise.

[red]O item 'A' está errado.[reset] A presença do advérbio 'jamais' no início da frase exige a próclise, ou seja, 
o pronome oblíquo átono deve ser colocado antes do verbo, resultando em 'Jamais me esquecerei daqueles momentos que passamos juntos.'
A próclise é usada quando há palavras ou expressões que atraem o pronome para antes do verbo, como negações (não, nunca, jamais), 
conjunções subordinativas (que, como, se), pronomes relativos (que, quem), pronomes indefinidos (algum, nenhum), advérbios, entre outros.

[red]Item 'B' está errado.[reset] Pois a presença da negação 'não' exige a próclise, e o pronome oblíquo átono deve ser colocado antes do verbo, 
formando 'Não me aceitaram naquele emprego.'

[red]O item 'C' está errado.[reset] A análise de colocação pronominal foca na posição dos pronomes oblíquos átonos em relação aos verbos. Frases que não contêm pronomes oblíquos átonos não são aplicáveis à regra de colocação pronominal.
Porém, é errado iniciar frases com a colocação de pronomes obliquos. Por regra.

[bg_green]O item 'D' é a única correta.[reset] A frase 'Dar-me-iam água para lavar as mãos?' está de acordo com o gabarito da banca, 
pois segue corretamente a regra de colocação pronominal. \n
Neste caso, utiliza-se a mesóclise, que é a inserção do pronome no meio do verbo, aplicável a verbos no futuro do presente ou no futuro do pretérito, como em 'dar-me-iam'.
A mesóclise é utilizada quando o verbo está no futuro do presente ou no futuro do pretérito e não há nenhuma palavra que exija a próclise. 
A inserção do pronome no meio do verbo reflete a correta aplicação das regras de colocação pronominal em contextos futuros sem palavras atrativas.

Ano: 2024 / Banca: FUNDEP Gestão de Concursos - FUNDEP / Prova: FUNDEP - HRTN - Médico - Área Anestesiologia - 2024 

Releia este trecho:

[yellow]“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Se disfarça de preguiça ou distração [...].”[reset]


Respeitadas as regras de colocação pronominal, o trecho pode ser reescrito, sem alteração no seu sentido, como:

A.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarçar-se-ia de preguiça ou distração [...].”
B.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarça se de preguiça ou distração [...].”
C.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarça-se de preguiça ou distração [...].”
D.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Se disfarça-se de preguiça ou distração [...].”


[bg_green]Gabarito alternativa 'D'.[reset]

O item 'A' apresenta a forma [yellow]'Disfarçar-se-ia'[reset], que é uma mesóclise, usada em orações com verbos no futuro do presente ou futuro do pretérito. 
No entanto, a frase original está no presente do indicativo, o que torna essa reescrita inadequada. Mudando o sentido.

O item 'B' os pronomes enclíticos são aqueles que se unem ao verbo, formando uma única palavra com ele. Em português, isso é mais comum com os pronomes pessoais oblíquos átonos. Quando usados encliticamente, eles aparecem depois do verbo.

Exemplos de Pronomes Enclíticos:

[blue]Encontrar-me-ão[reset] -> (Eles me encontrarão)

[blue]Dizer-te-ei[reset] -> (Eu te direi)

[blue]Ajudar-nos-á[reset] -> (Ela nos ajudará)

Regras de Uso:

- São usados em construções afirmativas.

- Não são usados após palavras negativas, advérbios, pronomes relativos ou conjunções subordinativas.

[yellow]Observações:[reset]

Na língua formal e escrita, o uso dos pronomes enclíticos é bastante comum, especialmente para manter a eufonia (som agradável) da frase.

Em contextos informais ou na fala cotidiana, é mais comum o uso da próclise (pronome antes do verbo) ou da ênclise (pronome entre a partícula negativa e o verbo).


O item 'C' é o correto. Apresenta a forma [yellow]'Disfarça-se'[rset], que está correta, pois o pronome 'se' está corretamente posicionado após o verbo, 
formando uma ênclise. Esta reescrita mantém o sentido original da frase e respeita as regras de colocação pronominal. 

[red]O item D apresenta a forma 'Se disfarça-se', que é incorreta, pois há uma duplicação desnecessária do pronome 'se'. A forma correta seria 'disfarça-se'. [reset]

Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - Prefeitura de São Bernardo do Campo - Inspetor - 2024 

A colocação pronominal atende à norma-padrão em:

A. A casa devia já ser velha; os tetos baixos e o soalho carunchoso tremiam quando me movimentava, arrastando os chinelos.
B. Na rua estreita e tortuosa, todos se conheciam, e o mesmo padeiro servia as famílias, sempre demorando-se de palestra pelas escadas.
C. Tão logo mudei para a nova casa, a primeira coisa que pude notar na vizinhança foi que não encontrava-se uma cara bonita, por ali.
D. Pelos buracos do rodapé, apareciam as baratas, que espalhavam-se de noite aos rebanhos, em cata de alimento para sobreviverem.
E. Me mudei para uma casa que nada tinha de confortável e resguardada, era apenas alta e mais clara que o primeiro andar da rua do Sol.

[bg_green] O item 'A' é o gabarito da questão.[reset]

No item 'A', '... tremiam [yellow]quando[reset] [blue]me[reset] movimentada....'

O pronome [yellow]'me'[reset] está corretamente posicionado antes do verbo 'movimentava', seguindo a regra da próclise, que é comum após conjunções subordinativas e advérbios e entre outros.

[yellow]A palavra "quando" é uma conjunção subordinativa temporal. Ela é usada para introduzir orações subordinadas que indicam uma circunstância de tempo relativa à ação principal da oração. Em outras palavras, "quando" conecta uma ação a um momento específico.[reset]

Exemplos de Uso de "Quando":

[yellow]Quando[reset] eu cheguei, ele já tinha saído. <- 'quando' -> [blue]conjunção subordinativa temporal[reset]

Nós vamos à praia [yellow]quando[reset] o tempo estiver bom. <- 'quando' -> [blue]conjunção subordinativa temporal[reset]

[yellow]Quando[reset] eu era criança, adorava brincar no parque. <- 'quando' -> [blue]conjunção subordinativa temporal[reset]

[red]Função Gramatical:[reset]

[blue]Conjunção Subordinativa Temporal:[reset] Estabelece uma relação temporal entre a oração principal e a subordinada.

[red]Observações:[reset]

[blue]"Quando" pode também ser usado em perguntas diretas ou indiretas, mas nesse caso, ele funciona como um advérbio interrogativo:[reset]

[yellow]Quando[reset] você vai chegar?

Não sei [yellow]quando[reset] ele vem.

O item 'B' está errado. Na frase 'Na rua estreita e tortuosa, todos se conheciam, e o mesmo padeiro servia as famílias, [yellow]sempre demorando-se [reset]de palestra...'
O pronome 'se' deveria estar antes do verbo 'demorando', [blue]formando a próclise obrigatória'sempre se demorando'.[reset]
[yellow]O advérbio de tempo 'sempre' no início da oração puxa o pronome antes do verbo, tornando a próclise obrigatória.[reset]

O item 'C' está errado.

A frase '...foi que [red]não[reset] [yellow]encontrava-se[reset] uma cara bonita, por ali.' Apresenta um erro de colocação pronominal. \n
O correto seria 'não se encontrava', utilizando a próclise. [red]Por regra, palavra negativas puxam o pronome para si, deixando o caso de próclise obrigatória.[reset]

O item 'D' está errado.

Na frase 'Pelos buracos do rodapé, apareciam as baratas, [yellow]que espalhavam-se[reset] de noite...'
O pronome 'se' deveria estar antes do verbo 'espalhavam', formando a próclise obrigatória, por regra, o pronome relativo 'que' o puxa.  -> [yellow]'se espalhavam'.[reset]
[red]Início de oração com pronome relativo, por regra, torna a próclise obrigatória.[reset]

[yellow]Me mudei[reset] para uma casa que nada tinha de confortável e resguardada, era apenas alta e mais clara que o primeiro andar da rua do Sol.' 
apresenta um erro de colocação pronominal. O correto seria 'Mudei-me', utilizando a ênclise.

Os pronomes pessoais oblíquos átonos em português incluem: [blue]me, te, se, lhe, nos, vos, lhes, o, a, os, as.[reset]
[red]Não devem ser utilizados no início de uma oração ou frase. [reset]

Exemplos Correto e Incorreto:

[red]Incorreto:[reset] [yellow]Me ajude [reset]com isso. <- [green]Próclise equivocada pelo contexto.[reset]

[blue]Correto:[reeset] [yellow]Ajude-me[reset] com isso. <- [green]ênclise obrigatória[reset]

[red]Incorreto:[reset] [yellow]Te espero [reset]na entrada. <- [green]Próclise equivocada pelo contexto.[reset]

[blue]Correto:[reset] [yellow]Espero-te[reset] na entrada. <- [green]ênclise obrigatória[reset]

[bg_green]Alternativas:[reset]

[blue]Próclise:[reset] Uso do pronome antes do verbo, geralmente precedido por palavras que atraem a próclise (palavras negativas, advérbios, pronomes relativos, etc.)

[red]Exemplo:[reset] Não me diga isso.

[blue]Ênclise:[reeset] Uso do pronome após o verbo, normalmente no início de frases ou após pausas.

[red]Exemplo:[reset] Diga-me a verdade.

[blue]Mesóclise:[reset] Uso do pronome no meio do verbo, em formas verbais futuras (mais comum em linguagem formal e escrita).

[red]Exemplo:[reset] Dizer-te-ei amanhã.

Ano: 2024 // Banca: CRS - Polícia Militar de Minas Gerais - CRS PMMG / Prova: CRS - PMMG - PM MG - Soldado Pós-Edital - 2024 - 5º Simulado

Identifique a alternativa em que ocorreu a correta substituição da expressão em destaque em “que nomeasse professor de desenho na Bahia o cidadão argentino Hector Bernabó” (l. 20-21) por um pronome oblíquo átono.

A. que nomeasse-lhe professor de desenho na.
B. que lhe nomeasse professor de desenho na.
C. que nomeasse-o professor de desenho na.
D. que o nomeasse professor de desenho na.

Gabarito da questão é a alternativa 'D'.

O item 'A' a substituição '[yellow]que nomeasse-lhe[reset] professor de desenho na...' está [red]incorreta.[reset] 
O pronome 'lhe' é utilizado SOMENTE para substituir 'objetos indiretos', enquanto o verbo 'nomear' é transitivo direto. Quem 'nomea', nomea algo ou 'para' alguem, exige um objeto direto. 
Portanto, a substituição não está de acordo com a regência verbal correta.

	O uso do pronome 'lhe' é para verbos que Exigem Preposição: (objeto indireto )

Exemplo: [yellow]Darei[reset] uma resposta [yellow]a ele.[reset] => [yellow]lhe[reset] darei uma resposta.

			[yellow]'darei'[reset] = verbo flexionado em que equm da algo, da algo a alguem ( verto transitivo ) <- [blue] sujeito da oração[reset]
			[yellow]'a ele'[reset] = preposição + pronome pessoal do caso reto 'ele' / objeto indireto ( com preposição )

			[yellow]lhe[reset] darei uma resposta. <- [blue]pronome em que substitui o objeto indireto 'a ele'[reset]

Exemplo: Vou contar [yellow]para ela[reset] o que aconteceu. => Vou [yellow]lhe[reset] contar o que aconteceu.

		[yellow]'vou contar'[reset] -> locução verbal sujeito da oração / quem conta conta algo, para alguém -> [red]verbo transitivo[reset]
		[yellow]'para ela' [reset]  -> preposição + pronome pessoal do caso reto 'ela => [red]objeto indireto  [reset]

[bg_red]No item 'b' também está inadequado o uso do pronome 'lhe' em próclise.[reset] Pelo mesmo motivo de uso inadequado.

					B. que [yellow]lhe[reset] nomeasse professor de desenho na...

	O pronome pessoal oblíquo átono 'lhe' é usado para orações em que o verbo transitivo exige objeto indireto, ou seja, com preposição inclusa.

[red]O item 'C' está inadequado o uso em ênclise pela oração iniciar com pronome relativo 'que' em que atrai o pronome.[reset]
			[bg_green]	O uso correto é com próclise obrigatória. Antes do verbo [reset]

[bg_green]Afirmativa 'D' a correta.[reset]

A substituição 'que o nomeasse professor de desenho na...' está correta. O pronome 'o' é adequado para substituir o objeto direto 'cidadão argentino Hector Bernabó', 
e sua posição antes do verbo 'nomeasse' está de acordo com a norma culta da Língua Portuguesa. Este item está de acordo com o gabarito da banca.

14.Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - Autoridade Portuária de Santos - Técnico Eletricista - 2024 
Assinale a alternativa redigida em conformidade com a norma-padrão de emprego e colocação dos pronomes.

A.O professor de português conheceu a literatura angolana e decidiu que iria estudar-lhe com mais profundidade.
B.Nunca lhe tinham contado que, na China, havia uma região em que as pessoas falavam a língua portuguesa.
C.Não convidaram-o para o curso de história da língua portuguesa que era ministrado na faculdade.
D.Estavam contentes por aprender sobre os diferentes sotaques do português e escutar-los ao vivo.
E.Ainda que faltassem-no informações sobre Moçambique, o poeta decidiu embarcar para o país africano.

O gabarito é letra 'B'.

O item 'A' está incorreto. 'O professor de português conheceu a literatura angolana e decidiu [yellow]que iria estudar-lhe[reseet] com mais profundidade.'

"lhe" é um pronome pessoal oblíquo átono que funciona como complemento indireto, ou seja, substitui objetos indiretos introduzidos por preposições como "a" ou "para". 
No entanto, na frase fornecida, o verbo "estudar" pede um complemento direto, 'quem estuda estuda o quê?' Não é um complemento indireto.	

Verbo "estudar": É um verbo transitivo direto, ou seja, precisa de um complemento direto (algo que se estuda, 'a literatura'), e não de um complemento indireto.
[blue]Uso Correto de "lhe": Deve ser usado com verbos que exigem complemento indireto, como "dar", "enviar", "oferecer", etc.[reset]

[blue]Frase Correta:[reset] O professor de português conheceu a literatura angolana e decidiu que iria [yellow]estudá-la[reset] com mais profundidade.

[blue]Portanto, ao corrigir a frase, substituímos "lhe" por "a", concordando com "literatura", que é feminino singular: "estudá-la".[reset] 
[blue]Isso garante que a frase esteja gramaticalmente correta e clara.[reset]

	Quando o verbo exige um objeto direto, usamos "o, a, os, as" dependendo do gênero e número do complemento direto.
	Os pronomes "o", "a", "os" e "as" são pronomes pessoais oblíquos átonos. Eles são usados como complementos diretos

	Para o complemento indireto, usamos "lhe, lhes".

Sofrem alterações na grafia os pronomes com o verbo terminados em -R, -S, -Z diante dos pronomes o, a, os, as:
            
            	Veja: Vamos [yellow]cantar[reset] os hinos. -> [yellow]Final -R[reset]
                
Vamos cantá-los. ( o verbo cantar fica oxítona com final 'a' acentuada e o substantivo 'os hinos' pelo pronome pessoal oblíquo átono 'os' acrescentando a letra 'l' )

[yellow]Cantamos os hinos[reset] -> Final -S // 'os hinos' -> substantivo para qual usamos o pronome pessoal do caso oblíquo átono 'os' acrescentando o 'l'.
                     
[yellow]Cantamo-los[reset] <- Não acentua o verbo pois a sílaba tônica está no 'ta'- paroxítona e retira o S e acrescenta o pronome 'los'.

Fiz o relatório -> Terminação -Z retira e 'o relatório' substantivo a qual será substituido pelo pronome pessoal do caso oblíquo átono 'o' acrescentado de 'l'.

[yellow]Fi-lo.[reset] <- 'lo' pronome que substitui 'o relatório' <- substantivo

[blue]Portanto, ao corrigir a frase, substituímos "lhe" por "a", concordando com "literatura", que é feminino singular: "estudá-la". [reset]


[bg_green]Item correto.[reset] [yellow]Nunca lhe[reset] tinham contado que, na China, havia uma região em que as pessoas falavam a língua portuguesa.

Além da próclise ser obrigatória pelo fato do advérbio puxar o pronome. O pronome "lhe" está empregado corretamente como complemento indireto.

O verbo "contar" é transitivo direto e indireto, o que significa que ele pode exigir:

 um objeto direto ([blue]o que é contado?[reset]) e um objeto indireto (a quem se conta algo: [blue]ele ou ela[reset]).

[red]Complemento Direto:[reset] [yellow]que, na China, havia uma região em que as pessoas falavam a língua portuguesa.[reset]

[red]Complemento Indireto:[reset] O pronome "lhe" substitui o complemento indireto "a ele" ou "a ela".

Exemplo: Nunca contaram [yellow]a ele/ela[reset] que...  <- 'a' -> preposição / 'ele/ela' => pronome pessoal do caso reto

[blue]Com Pronome:[reset] Nunca [yellow]lhe[reset] contaram que...

[bg_red]O item C apresenta um erro de colocação pronominal. [reset]
		[red]Não convidaram-o[reset] para o curso de história da língua portuguesa que era ministrado na faculdade.

O correto seria [yellow]'Não o convidaram [reset]para o curso de história da língua portuguesa que era ministrado na faculdade'.

[blue]O pronome oblíquo átono 'o' deve vir antes do verbo em orações negativas. [reset]  [red] Por regra, é próclise obrigatória[reset]


[red]O item D apresenta um erro na colocação do pronome 'los'.[reset]

		Estavam contentes por aprender sobre os diferentes sotaques do português e [red]escutar-los[reset] ao vivo.

O correto seria [yellow]'e escutá-los ao vivo'[reset], [blue]pois o pronome oblíquo átono deve ser ligado ao verbo por hífen quando este está no infinitivo impessoal.[reset]


[red] O item 'E' está incorreto.[reset]

			Ainda que [yellow]faltassem-no[reset] informações sobre Moçambique, o poeta decidiu embarcar para o país africano.

	[red]Verbo "faltar": É um verbo transitivo indireto, que exige um complemento indireto (usualmente precedido pela preposição "a").[reset]
		[blue]Ele é indireto porque ele requer um complemento introduzido por uma preposição para completar seu sentido.[reset]

						[bg_red]Objeto Indireto: "Lhe" (a ele, ao poeta)[reset]

Exemplos:

Sem Complemento:

"Faltam informações." (A frase é compreensível, mas incompleta. Precisamos saber a quem ou a quê essas informações estão faltando.)

Com Complemento Indireto:

"Faltam informações ao professor." (Aqui, "ao professor" é o complemento indireto. [blue]'ao' -> preposição 'a' + artigo 'o' )[reset]

"Faltam dois dias para a viagem." (Aqui, "para a viagem" é o complemento indireto.) [blue]'para' -> preposição [reset]

"no": A combinação "no" não é apropriada porque "o" é um pronome oblíquo que substitui objetos diretos, e não é precedido por "a". O verbo "faltar" exige um objeto indireto.

"lhe": Este pronome é usado corretamente para objetos indiretos, substituindo "a ele" ou "a ela". [bg_red]Objeto Indireto: "Lhe" (a ele, ao poeta)[reset]

15. Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN / Prova: IDECAN - Agente da Mobilidade Urbana Pós-Edital - 2024 - 1º Simulado

Com base no trecho "Mas aí lhe tiraram a roça." do texto fornecido, avalie as alternativas a seguir quanto à colocação pronominal adequada e escolha a correta.

A. Mas aí tiraram-lhe a roça, refletindo a colocação pronominal mesoclítica, adequada ao contexto formal da escrita.
B. Tiraram-lhe a roça aí, demonstrando o uso correto da próclise, influenciado pela presença de uma palavra negativa.
C. Mas aí a roça lhe tiraram, ilustrando uma ênclise, que é inadequada pela presença de palavra atrativa anterior.
D. A colocação pronominal em "lhe tiraram" é um exemplo correto de próclise, influenciada pela conjunção subordinativa "Mas".

Gabarito 'D'

O item A sugere que a frase 'Mas aí tiraram-lhe a roça' é um exemplo de mesóclise. No entanto, isso é incorreto. A mesóclise ocorre quando o pronome é colocado no meio do verbo.

O item B sugere que a frase 'Tiraram-lhe a roça aí' é um exemplo de próclise, influenciada pela presença de uma palavra negativa. No entanto, isso é incorreto. A próclise ocorre quando o pronome é colocado antes do verbo.

O item C sugere que a frase 'Mas aí a roça lhe tiraram' é um exemplo de ênclise. No entanto, isso é incorreto. 
A ênclise ocorre quando o pronome é colocado após o verbo, mas a presença da palavra 'Mas' no início da frase atrai o pronome para antes do verbo (próclise).

O item D sugere que a colocação pronominal em 'lhe tiraram' é um exemplo correto de próclise, influenciada pela conjunção subordinativa 'Mas'. 
Isso está correto. A próclise ocorre quando o pronome é colocado antes do verbo, e a presença da conjunção 'Mas' no início da frase atrai o pronome para essa posição.



        '''                  
    def pronome_possessivo(self):
        return '''Os pronomes pessoais do caso reto conjugam os verbos e tem função de sujeito da oração.

        EU, TU, ELE, Nós, Vós, Eles <- Cada pronome pessoal pode ser representado pelos pronomes possessivos.

        A função principal do pronome possessivo é associar alguma coisa com seu dono.

        [yellow]eu[reset]   -> [yellow]meu,minha,meus,minhas - 'Meu lápis'[reset]

[yellow]tu[reset]   -> [yellow]teu, tua, teus, tuas[reset]

[yellow]ele[reset]  -> [yellow]seu, sua, seus, suas[reset]

[yellow]nós[reset]  -> [yellow]nosso, nossa, nossos,  nossas - 'nosso livro' ou 'nós temos um livro'[reset]

[yellow]vós[reset]  -> [yellow]vosso, vossa, vossos, vossas[reset]

[yellow]eles[reset] -> [yellow]seu, sua, seus, suas[reset]


        Por exemplo:

            Para cada pronome pessoal do caso reto temos pronomes possessivos específicos:

                - Para associar 1º pessoa do discurso, pronome pessoal EU temos: MEU, MINHA, MEUS, MINHAS
                        
                        Exemplos: Meu lápis, Minhas roupas, meu tênis.

                - Para associar a 2º pessoa do discurso do pronome pessoal TU temos: TEU, TUA, TEUS, TUAS

                        Exemplos: Teu lápis, tua casa, tuas ideias
                
                - Para associar a 3º pessoa do discurso a que se refere ao pronome pessoal ELE, temos: SEU, SUA, SEUS, SUAS

                        Exemplos: Seu lápis, sua ideia, seus livros, suas roupas

                - Para associar a 1º pessoa do discurso no plural a que se refere o pronome pessoal do caso reto:
                    temos: nosso, nossa, nossos, nossas
                                

      [blue]O pronome possessivo deve concordar com o substantivo.[reset]

		Nós temos [yellow]nossa[reset] ideia - [yellow]O pronome 'nossa' é possessivo e concorda em gênero em 'ideia' - palavra feminina.[reset]
                                        
Os pronomes possessivos 'seu(s)' e 'sua(s)' podem se referir tanto à 2º pessoa (pessoa com quem se fala) como à 3º pessoa (pessoa de quem se fala)

        		Sua casa foi vendida [blue](sua = de você)[reset]    <- [green] 2º pessoa do discurso [reset]
        		Sua casa foi vendida [blue](sua = dele, dela)[reset] <- [green] 3º pessoa do discurso [reset]

Os pronomes 'seus' e 'suas' são usados tanto para 3º pessoa do singular quanto para 3º pessoa do plural:

		Ana recebeu [yellow]sua[reset] notícia. [blue]( 'notícia' = de outra pessoa ou da própria 'ana')[reset]
 
		Ana e João receberam [yellow]sua[reset] notícia. [blue]( 'notícia' = de outra pessoa ou deles <- podendo ser duas ou mais notícias)[reset]

[bg_green] Os pronomes possessivos podem em muitos casos ser substituidos por pronomes oblíquos equivalentes. [reset]

		A chuva molha-[yellow]me[reset] o rosto. [blue]( 'me' pronome oblíquo átono que pode significar 'meu' = molha 'meu' rosto, pronome possessivo)[reset]

   		A chuva molha-[yellow]lhe[reset] o rosto. [blue]( 'lhe' pronome oblíquo átono que pode significar 'seu' = molha seu rosto, pronome possessivo) [reset]


O pronome possessivo 'seu' refere-se gramaticalmente ao substantivo, podendo estar do lado do substantivo. 
Porém é a concordância que o pronome está fazendo é em relação ao possuidor da ideia.
A referência de pronome possessivo é o possuidor e não o substantivo que o acompanha.
           
           
Questão de concurso:

Quadrix/CRN-8:
	Uma dieta saudável e equilibrada é importante para apoiar o sistema imunológico do seu corpo e a má nutrição pode comprometê-lo.
    Procure comer uma grande variedade de frutas e legumes para garantir que você obtenha todos os nutrientes de que seu sistema imuno-
    lógico precisa.
O pronome possessivo 'seu' (linha 19) refere-se ao

a. sistema imunológico
b. leitor
c. corpo
d. termo 'dieta'
e. micronutriente.

Alternativa 'B'.  O pronome possessivo 'seu' refere-se gramaticalmente ao substantivo 'corpo', ao lado do substantivo. 
Porém a referência que o pronome está fazendo é em relação ao 'leitor' possuidor da ideia. '... que você obtenha todos...'
A referência de pronome possessivo é o possuidor e não a 'coisa possuida' o substantivo que o acompanha.

    'Corpo' é a coisa possuida, a concordância.
    Referência em pronomes possessivos em questões de concurso é o possuidor.

	
       '''                  
            
    def pronome_indefinido(self):
        return '''Pronomes indefinidos:
        
        Apontar coisas ou objetos que tem sentido vago, sem definição, sem saber o que é:
        
algum, alguns - algumas, alguma - alguém

nenhum, nenhuns, nenhuma, nenhumas - ninguém

todo, todos, toda, todas - tudo

outro, outras, outra, outras - outrem

muito, muitos, muita, muitas - nada

pouco, poucos, pouca, poucas, -- cada

certo, certos, certa, certas - algo

tanto, tantos, tanta, tantas

quanto, quantos, quanta, quantas

qualquer - quaisquer

[bg_red] Cuidado para confundir! [reset]
	Muitos livros <- acompanha o substantivo 'livros' portanto é pronome indefinido que pode variar em numero e gênero.
	Tenho livros muito antigos -> 'antigos' é uma qualificação para o substantivo 'livros' sendo assim, 'muito' é um advérbio de intensidade sem variação.

    [bg_red] ATENÇÃO! [reset]
    certo amigo <- 'amigo' -> substantivo / 'certo' -> algum amigo, um pronome indefinido
    amigo certo <- 'amigo' -> substantivo / 'certo' -> adjetivo

    [bg_red] ATENÇÃO! [reset]

    Encontrei alguma ajuda [blue]( a frase está afirmativa, indefinida  )[reset]

	Encontrei ajuda alguma [blue]( o sentido muda, para uma negação, ou seja, não encontrou nenhuma ajuda, pelo sentido geral da frase.)[reset]
			[yellow]O 'alguma' continua pronome indefinido nas duas frases.[reset]

            
Existem locuções formadas por mais de uma palavra, chamadas de locuções pronominais - as mais comuns são:

	qualquer um, 
	todo aquele que,
	um ou outro,
	cada um,
	seja quem for

		[yellow]Seja qual for[reset] o resultado, não desistiremos. [blue]( locução pronominal indefinida )[reset]

        [bg_red] Pronomes e numerais podem ter papel de adjetivo [reset]'''   

    def pronome_interrogativo(self):
        return '''Os pronomes interrogativos:
        
        PRONOMES INTERROGATIVOS:

	São aqueles empregados para fazer uma pergunta direta ou indireta.
Os pronomes interrogativos são os seguintes:

	[green]Que, quem, qual, quais, quanto(s), quanta(s)[reset]

Exemplo:

	[yellow]Que[reset] horas são? [blue]( frase interrogativa direta )[reset]
	
	Gostaria de saber [yellow]que[reset] horas são. [blue]( interrogativa indireta )[reset] 'que' será pronome interrogativo.
		
	[yellow]Quantas[reset] crianças foram escolhidas? [blue]( interrogativa direta )[reset] 'quantas' será pronome interrogativo.
'''

    def pronome_relativo(self):
        return '''Pronomes Relativos:
        
        Serve para transmitir duas informações a respeito de algo ou alguém.
        
        Eu conheço o menino. O menino caiu no rio.
        
        Para evitar a repetição do substantivo 'menino' podemos utilizar o pronome relativo 'que' 
        
            	Eu conheço o menino [yellow]que[reset] caiu no rio.
                
        [bg_yellow]Observa-se que a palavra 'que' substitui a palavra 'menino' e junta duas frases.[reset]

            [blue] Ao mesmo tempo que substitui a palavra que está repetindo, relaciona duas frases em uma. [reset]

            [bg_green] Quando a questão pergunta sobre o que se refere o pronome, está querendo dizer a quem está substituindo [reset]

    [bg_yellow]Pronomes relativos são os que se referem a um substantivo anterior a eles, substituindo-o na oração seguinte.[reset]

    Exemplo comum de um pronome relativo:

	        Eu visitei a cidade. Você nasceu na cidade.

	        Eu visitei a cidade. Você nasceu na cidade. <- 'na cidade' => 'na' -> preposição 'em' + artigo 'a'.

	Eu visitei a cidade [yellow]onde[reset] você nasceu.
	Eu visitei a cidade [yellow]em que[reset] você nasceu.
	Eu visitei a cidade [yellow]na qual[reset] você nasceu.

	[blue]em + a qual / em + a / em + que = pronomes relativos com preposição[reset]

    Os pronomes relativos variáveis masculinos são:

            o qual; os quais; cujo; cujos; quanto; quantos

    Os pronomes relativos variáveis feminino são:

            a qual, as quais, cuja, cujas, quanta, quantas

    Os pronomes relativos Invariáveis:

	        que, quem, onde, como

    O pronome relativo 'que' pode ser substituível por 'o qual', 'a qual', 'os quais', 'as quais'.

            Já li o livro [yellow] que [reset] comprei <- Já li o livro [yellow]o qual[reset] comprei                

    [bg_red] A palavra 'que' pode ser pronome relativo, pronome interrogativo, conjunção integrante [reset]

    [bg_red] ATENÇÃO! [reset]

        Os pronomes relativos 'que' e 'qual' é necessário colocar a preposição 'em' exigida em alguns verbos:

            Nascer ( quem nasce, nasce EM algum lugar )

            Você comprou o livro. Eu gosto do livro. [red] É necessária a colocação preposicional 'de' exigida pelo verbo 'GOSTAR' [reset]
                [red] Por que quem gosta gosta de alguma coisa [reset]
    
    O pronome demonstrativo possui valor substantivo 'o','a','os','as'

        [yellow] o = aquele / aquilo <- pronome demonstrativo substantivo[reset]
        [blue] a = aquela / <- pronome demonstrativo substantivo[reset]
        [green] os = aqueles <- pronome demonstrativo substantivo[reset]
        [red] as = aquelas <- pronome demonstrativo substantivo[reset]

        Exemplo:

            Ele sempre consegue [yellow]o[reset] [blue]que[reset] deseja.

            'o'   = pronome demonstrativo -> 'aquele' / 'aquilo' <- pronome demonstrativo substantivo
            'que' = pronome relativo -> 'o qual' -> pronome relativo variável masculino

                Ele sempre consegue [yellow] aquilo [reset] [green] o qual [reset] deseja.

[bg_red] ATENÇÃO! [reset] 

    QUANTO, QUANTOS, QUANTA, QUANTAS são pronomes relativos se estiverem precedidos dos pronomes indefinidos TUDO, TANTO(s), TANTA(S), todos(s), toda(s)
mas eles são pronomes indefinidos.

	Sempre obteve [yellow]tudo quanto[reset] quis.

    'tudo'   -> Pronome indefinido 
    'quanto' -> Pronome relativo,  mas precisa ser precedido de um pronome indefinido.

[bg_red] ATENÇÃO! [reset]

        O relativo 'quem' só é usado em relação a pessoas e sempre precedido de preposição.

            O professor [yellow] de quem [reset] você gosta chegou. [blue] O pronome retoma o termo anterior.[reset]

            Outro exemplo:

            O professor [yellow] a quem [reset] você citou, chegou.

            [bg_red]Pronome 'quem' deve vir preposicionada.[reset]

            [bg_red] ATENÇÃO! [reset]

            [bg_red] O verbo citar não necessita de preposição, ou seja, não pedi preposição como o verbo gostar, gosta de quem? [reset]\n
            [bg_red] Quando o verbo em uma frase pedi preposição é um verbo transitivo indireto (VTI)[reset]
            [bg_red] Quando o verbo em uma frase não pedi preposição é um verbo transitivo direto (VTD)[reset]

            [bg_yellow] Pronome relativo CUJO [reset]

            O pronome relativo 'cujo' é empregado entre dois substantivos com o esquema de DONO + pronome + COISA.
                e assim estabelecendo entre eles uma relação de posse, substituindo o termo anterior com sentido de posse.
                e equivale a 'do qual', 'da qual', 'dos quais', 'das quais'.

        Compramos o terreno cuja frente está murada. ( cuja frente = frente do qual )
        Compramos o terreno do qual frente está murada.

        O livro cujas páginas estão rasgadas sumiu. / 'livro' = dono // 'páginas' = coisa

        [bg_red] ATENÇÃO! [reset] \n
        [bg_red] O pronome relativo 'cujo' sempre se refere ao termo anterior [reset]\n
        [bg_red] O pronome relativo deve concordar com o termo posterior em número e gênero [reset]               \n
        [bg_red] Os pronomes relativos sempre vão se referir ao termo anterior [reset]\n
        [bg_red] Depois do pronome 'CUJO' não se usa artigo! [reset]

        [red]Pronome relativo sempre tem a referência dele antes.[reset]\n
        [bg_red]O que tem depois do cujo não é referência e sim a CONCORDÂNCIA.[reset]

        PREFRB,adm - 
        À semelhança do Brasil, o Acre compõe-se de uma grande diversidade de povos indígenas, cujas situações frente à sociedade nacional também são muito variadas.

        a. A substituição de 'cujas' por 'as quais' mantém a correção gramatical do período e as relações lógicas originais.

        Pronome relativo 'cujas' refere-se aos 'povos indígenas'. Sempre vai dar relação de posse. E irá concordar com o termo posterior.
    	O pronome relativo 'as quais' combina com antecedende e se refere a ele. 'as quais' não é relação de posse e sim retomada.
			[bg_red]Se fosse possível trocar seria 'os quais' por ser palavra masculina mas não teria relação de posse.[reset]
		Mas a relação lógica deixa de ser de posse quando retiramos o pronome relativo 'cujo'. E simplesmente uma retomada.

        Se fosse possível trocar, seria 'os quais' pela concordância é com a palavra antecedente.
            Ao retirar o pronome relativo de posse 'cujas' pelo 'as quais' muda a lógica que deixa de ter a ideiia de posse.
                Ou seja, tanto na correção gramatical quanto na relação lógica original.
                        Questão ERRADA

    EMPREGO DO 'CUJO':

        Exemplos:

            Observo os povos indígenas [yellow]cujo[reset] líder é guerreiro.	\n	
'cujo' -> concorda com o substantivo masculino singular posterior 'líder'. ideia de posse. 
			E o pronome relativo 'cujo' tem a referência anterior - 'povos indígenas' 
                        
         	Observo os povos indígenas [yellow]cuja[reset] cultura é milenar.
'cuja' -> concorda com o substantivo posterior 'cultura' palavra feminina - 'a cultura'
			A referência anterior - 'povos indígenas'

           	Observo os povos indígenas [yellow]cujos[reset] líderes são guerreiros.
'cujos' -> concorda com o substantivo posterior 'líderes' palavra masculina e no plural. 
			A referência é anterior 'povos indígenas'

[bg_red]CUIDADO! ESTRUTURAS INADEQUADAS AS SEGUINTES:[reset]

	Observo os povos indígenas [red]que o[reset] líder é guerreiro. [bg_red]( relação de posse não pode ser expressa por 'que o', 'que a' )[reset]
	Observo os povos indígenas [red]que o[reset] líder deles é guerreiro. [bg_red][ERRADO][reset] [red] ideia de posse entre si é cujo [reset]

    [bg_yellow] Para ligar dos substantivos com relação de posse entre si, somente é correto o uso do pronome relativo CUJO e suas variações.[reset]
                    [bg_red] É UMA REGRA! [reset]

(PMVSEMUS, médico) 
	Preocupam-se mais com a AIDS do que os meninos e as meninas da ´África do Sul, [yellow]onde[reset] a contaminação segue em ritmo alarmante. 
Chegam até a se apavorar mais com a gripe do frango do que as crianças chinesas, que conviveram com a epidemia. 

Preservam-se as ideias e a correção gramatical do texto ao se substituir o pronome 'onde' por 'cuja' apesar de o texto tornar-se menos formal. 

[green]pronome relativo 'onde' é ideia e sentido de lugares.[reset]
[green]pronome relativo 'cuja' é ideia de posse entre dono e a coisa possuida.[reset]

[bg_red] Além disso, depois do pronome relativo 'onde' tem um artigo 'a' determinando o substantivo 'contaminação'[reset]
		[bg_red] Lembrando que não pode utilizar artigos depois do 'cujo' e suas variações.[reset]
        [bg_red] QUESTÃO ERRADA! [reset]
 
        [bg_red] ATENÇÃO! [reset]

            [bg_yellow] O pronome relativo ONDE equivale a 'EM QUE'. [reset]

                    Conheci o lugar [yellow]onde[reset] você nasceu.

                    Conheci o lugar [yellow] em que [reset] você nasceu.
                    
Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura do Município de Valinhos - Professor II - Área Matemática - 2024 

O pronome demonstrativo que introduz o excerto “Esse é o principal indicador do interesse de um indivíduo por um cheiro.” atua, no contexto em que ocorre, como um elemento de coesão textual de referenciação. Isso porque é empregado para:

A. introduzir um novo elemento na sequência textual.
B. retomar um elemento já mencionado na sequência textual.
C. estabelecer uma relação de hiponímia com outro elemento da sequência textual.
D. estabelecer uma relação de hiperonímia com outro elemento da sequência textual.
E. estabelecer uma relação de sinonímia com outro elemento da sequência textual.

Gabarito letra 'B'.

O item A sugere a substituição de 'no qual' por 'em que' e 'que' por 'as quais'. 
A substituição está correta, pois 'em que' é uma forma válida de pronome relativo que retoma 'relatório' e 'as quais' retoma 'tragédias', mantendo a coesão e a concordância adequadas.

Pronome relativo retoma algo dito anteriormente.

Pronome demonstrativo também. Os pronomes demonstrativos dão ideia de espaço presente, passado ou passado distante.

Espaço presente: este (1° pessoa)

Espaço Passado: Esse (2° Pessoa)

Espaço Passado muito distante: Aquele "dia"(3° Pessoa)  

35. Ano: 2024 / Banca: Comissão Permanente de Concursos da Universidade Estadual da Paraíba - CPCON UEPB / Prova: CPCON UEPB - UEPB - Nutricionista - 2024 

Assinale a alternativa que contém uma frase, na qual ocorre o uso do pronome relativo:

A. “Desde o momento em que ouvi aquelas palavras do médico — tremor essencial —, fiquei ...”
B. “... Fiquei confiante em que poderia lidar com a situação.”
C. “... surgiram até boatos infundados de que seria Parkinson.”
D. “O médico recomendou um medicamento diário e mudança de hábitos, já que a condição, no meu caso, não é genética.”
E. “Hoje, reconheço que estou bem graças à minha obstinação em ficar saudável.”

Gabarito letra 'A'.

Pronomes relativos são aqueles que retomam um termo anterior, chamado de antecedente, e introduzem uma oração subordinada adjetiva. 
Eles têm a função de conectar duas orações, evitando a repetição de palavras e proporcionando coesão ao texto.

			A. “Desde o momento [yellow]em que[reset] ouvi aquelas palavras do médico — tremor essencial —, fiquei ...”		

O item 'A'. Contém o pronome relativo 'que', que retoma o substantivo 'momento'. 
O pronome 'que' introduz uma oração subordinada adjetiva explicativa, explicando o momento específico em que o sujeito ouviu as palavras do médico.


				B. “... Fiquei confiante [yellow]em que[reset] poderia lidar com a situação.”

		O 'que' nesta frase é uma conjunção integrante, que introduz uma oração subordinada substantiva objetiva direta.

				C. “... surgiram até boatos infundados [yellow]de que[reset] seria Parkinson.”

		O 'que' aqui é uma conjunção integrante, introduzindo uma oração subordinada substantiva completiva nominal.
	
				D. “O médico recomendou um medicamento diário e mudança de hábitos, [yellow]já que[reset] a condição, no meu caso, não é genética.”

		Contém a expressão 'já que', que é uma locução conjuntiva causal, e não um pronome relativo.

				 “Hoje, reconheço [yellow]que[reset] estou bem graças à minha obstinação em ficar saudável.”

		contém o 'que' como uma conjunção integrante, introduzindo uma oração subordinada substantiva objetiva direta.


                  '''

    def pronome_demonstrativo(self):
        return '''Pronomes demonstrativos:\n
        
        	- Apontar ou indicar a posição ou lugar dos seres em relação às três pessoas gramaticais.
            A 1º pessoa é o emissor 
            A 2º pessoa é o receptor
            A 3º pessoa é o assunto.
            
            		[yellow]Aquela[reset] casa é igual à nossa.\n
                O pronome demonstrativo 'aquela' refere-se a distância. 3º pessoa.

                Os pronomes demonstrativos:

                    este, esta, estes, estas -> isto
                    esse, essa, esses, essas -> isso
                    aquele, aquela, aqueles, aquelas -> aquilo
                    o, a, os, as -> o

        [bg_red]Podem funcionar como pronomes demonstrativos: o, os, a, as, mesmo, mesma, semelhante, semelhantes, tal, tals[reset]

	Chegamos hoje, não [yellow]o[reset] sabias? [blue](o = isto)[reset]

    	Quem diz [yellow]o[reset] que quer, ouve [yellow]o[reset] que não quer [blue](o = aquilo)[reset]

	[blue]Podemos substituir por 'aquilo' pronome demonstrativo também:[reset]
	Quem diz [yellow]aquilo[reset] que quer, ouve [yellow]aquilo[reset] que não quer.

    	[yellow]Tais[reset] coisas não se dizem em público. [blue]( tais = estas )[reset]

        Outros exemplos:

	O livro que você trouxe não é [yellow]o[reset] que te pedi. [blue] Note que 'o' equivale ao pronome demonstrativo 'aquele'[reset]

	A revista que você trouxe não é [yellow]a[reset] que te pedi. [blue] Note que 'a' equivale ao pronome demonstrativo 'aquela'[reset]

	Pode fazer [yellow]o[reset] que você quiser. [blue] Note que 'o' equivale a 'aquilo'.[reset]

            Regra dos pronomes demonstrativos:

        Conceito básico: Servem para referêcia a objetos em relação as pessoas que participam de um diálogo ( pessoas do discurso )

        REGRA:

            - Primeira pessoa: eu / nós .-> Deve-se empregar ESTE,ESTA,ISTO com referência a objeto próximo de quem fala.
            - Segunda pessoa: tu / vós / você. ->  Deve-se empregar ESSA,ESSA,ISSO com referência a objeto próximo de quem ouve.
          	- Terceira pessoa: ele, ela, eles, elas.->  Deve-se empregar AQUELE,AQUELA,AQUILO com referência a objeto distante tanto de quem fala, como de quem ouve.
            
- Primeira pessoa: eu / nós -> Deve-se empregar ESTE,ESTA,ISTO com referência a objeto próximo de quem fala.              

        Esta camisa que estou usando.

- Segunda pessoa: tu / vós / você. ->  Deve-se empregar ESSA,ESSA,ISSO com referência a objeto próximo de quem ouve.

        Esses óculos que estão no seu rosto.

- Terceira pessoa: ele, ela, eles, elas.->  Deve-se empregar AQUELE,AQUELA,AQUILO com referência a objeto distante tanto de quem fala, como de quem ouve.        


        
Exemplo 1:
		
		Correspondência do Governador para o Presidente da Assembleia Legislativa.
	Senhor Presidente,

	Solicito a V.Exa que ESSA Casa Legislativa analise com urgência o projeto que destina verba para reforma do Ginásio Estadual Américo de Almeida.

		[blue]Note que o remetente é:[reset] [yellow]GOVERNADOR [reset]
		[blue]Note que o destino é:[reset] [yellow]Presidente da Assembleia Legislativa [reset]

		[blue] '...que ESSA Casa Legislativa...'[reset] : [yellow] PRONOME DEMONSTRATIVO 'ESSA' em referência ao objeto próximo de quem ouve.[reset]

	Resposta do Presidente da Assembleia Legislativa para o Governador.
Senhor Governador,
	
	Informo a V.Exa que [yellow]esta[reset] Casa colocará em pauta na quarta-feira próxima a análise do projeto que destina verba para reforma do Ginásio Américo de Almeida.
	[yellow]Essa[reset] Governadoria pode aguardar informativo na quinta-feira.

	[yellow] Agora o pronome demonstrativo 'ESTA' no contexto da frase é referido ao objeto próximo de quem está falando, que no caso é 'a casa'.[reset]
	[blue] '... ESSA Governadoria pode...' [reset] => [green] 'essa' pronome demonstrativo ao objeto próximo de quem ouve. [reset]


[bg_red] ATENÇÃO! [reset]

	'NESTA' é uma contração de 'em' + 'esta'. É união de palavras. [red]Não é PRONOME.[reset] -  [green]'esta' é pronome e 'em' é preposição.[reset
	

		Aqui [yellow]nesta[reset] sala onde estamos, às vezes escutamos vozes vindas [yellow]daquela[reset] sala onde estão tendo aula de Finanças Públicas.

        'DAQUELA' contração da preposição 'de' + o pronome demonstrativo -> 'aquela'.
                [bg_red] Atenção! Portanto não é pronome e sim uma união.[reset]

                
[bg_yellow]        Situação especial: Pronome demonstrativo para termos anteriores e posteriores. [reset]

	REGRA:

	Para termos a serem mencionados: este, esta, isto. ( termo posteriores )

	Para termos já mencionados: esse, essa, isso. ( termo anterior )

    PRÁTICA:

	Recebemos _____ correspondências: um ofício e um memorando.[blue]( nesse caso, é um termo a ser mencionado ... [reset][yellow]'recebemos estas correspondências' )[reset]
	______ documentos serão arquivados. ( [blue]concordar com o plural de substantivos para termos já mencionados [reset] -> 'esses' , [yellow]'esses documentos..'[reset])
	______ procedimento atende a  __________ finalidade: permitir consulta posterior. [blue]'esse' procedimento atende a...' -> Termo mencionado 'esse', 'essa'[reset]
	'a ______ finalidade: permitir consulta posterior. -> [blue]termo a serem mencionados: este, esta, isto[reset]
		[yellow]'esta' finalidade: permitir consulta posterior.[reset]

[bg_red] ATENÇÃO! [reset]

	[blue]O pronome demonstrativo 'este' se refere ao último termo tendo dois ou mais termos na frase e o retoma.[reset]

	'... ofício e memorando. [yellow]Este[reset] documento será...' [green]( o pronome demonstrativo 'este' retoma o 'memorando' )[reset]

	[blue]O pronome demonstrativo 'esses' se refere aos termos presentes na frase.[reset]

	'... ofício e memorando.... [yellow]Esses[reset] documentos serão...' [green]( o pronome demonstrativo 'esses' retoma os dois termos em questão, ofício e memorando )[reset]

	[blue]O pronome demonstrativo 'aquele' se refere ao primeiro termo. O mais distante.[reset]

	'...ofício e memorando. [yellow]Aquele[reset] documento será...' [green]( o pronome demonstrativo 'aquele' se refere e retoma o 'ofício', o termo mais distante )[reset]
	
[bg_red]PARA REFERÊNCIA A TERMOS ANTERIORES SEPARADAMENTE:[reset]

[blue]Para referência ao primeiro mencionado:[reset] [yellow]aquele, aquela, aquilo.[reset]
[blue]Para referência ao último mencionado:[reset] [yellow]este, esta, isto.[reset]
[blue]Para referência ao termo entre o primeiro e o último:[reset] [yellow]esse, essa, isso.[reset]

	Gosto mais de pamonha do que de pequi, ou seja, prefiro __________ a___________.
	Gosto mais de pamonha do que de pequi, ou seja, prefiro [yellow]aquela[reset] a [yellow]este.[reset]
			[green]Ele prefere a 'pamonha' - o primeiro a ser mencionado, o mais distante da retomada. = 'aquele', 'aquela', 'aquilo'[reset]
		[blue]Do que 'pequi' - o segundo ou último termo mencionado - 'este','esta','isto'.[reset]

        Exemplo 02:

        A polícia soltou alguns integrantes da quadrilha._____________destruiram provas do crime a pedido de_________;
        A polícia soltou alguns integrantes da quadrilha. [bg_yellow]Esses[reset] destruiram provas do crime a pedido de... ( termo do meio 'esses' concordando com o verbo )
        '...destruiram provas do crime a pedido [bg_yellow]desta.[reset] [blue]( para referência ao último mencionado - este, [de + esta] , isto)[reset]

        O problema é que ________________dificultou o trabalho_________________.
        O problema é que [bg_yellow]isso[reset] dificultou.... [blue]( 'isso' -> referência ao termo entre o primeiro e o último: 'esse','essa','isso'. )[reset]

        ... dificultou o trabalho [bg_yellow]daquela.[reset] [blue][ Referente ao primeiro mencionado - do crime de destruir provas - ][reset]

Outro exemplo:
	
	A lenda é melhor, muito superior à história autêntica. Enquanto [bg_yellow]esta[reset] se limita ao fato sumário, verídico, [bg_yellow]aquela[reset] o engrandece, tornando-o poético,
belo, universal. Por isso, a [bg_yellow]esta[reset] prefiro [bg_yellow]aquela.[reset]

[yellow]'a lenda'[reset] - [blue]substantivo em que podemos colocar para substitui-lo o pronome demonstrativo 'aquela', o termo mais distante e o primeiro termo também...[reset]
[yellow]'...à história autêntica.'[reset] -> último termo, portanto é 'esta'- pronome demonstrativo para o último termo da frase.
[yellow]'aquela'[reset] - o engrandece, tornando-o poético. [blue] Pronome demonstrativo que se refere ao substantivo 'a lenda', o termo mais distante e o primeiro da frase.[reset]
'Por isso, a [yellow]'esta[reset]...' -> refere-se ao último termo - 'a história autêntica' -> último termo.


CRN-8/QUADRIX:
	Muitos recém-nascidos recebem uma injeção de vitamina K para evitar uma condição rara, mas grave, de sangramento excessivo. Isso ocorre porque os
bebês nascem com baixos níveis de vitamina K.

	O pronome 'isso' retoma a ideia de que recém-nascidos:

a. recebem injeção de vitamina K
b. não precisam de reforço de vitamina K.
c. Não tem vitaminas K no corpo.
d. sempre apresentam condição grave.
e. tem níveis baixos de vitamina K.

    O pronome demonstrativo 'isso' no contexto da frase retoma a ideia de que recebem uma injeção de vitamina K. Letra 'a'.

	O pronome demonstrativo 'isso' retoma o primeiro termo da frase, sendo que a finalidade é para evitar uma condição rara.

            
a. recebem injeção de vitamina K [bg_green][CORRETO][reset]
b. não precisam de reforço de vitamina K. [bg_red][ERRADO][reset]
c. Não tem vitaminas K no corpo.[bg_red][ERRADO][reset] <- a vitamina em baixo nível
d. sempre apresentam condição grave.[bg_red][bg_red][ERRADO][reset] <- quando apresentam condição grave
e. tem níveis baixos de vitamina K.[bg_red][ERRADO][reset] <- não é sempre.


[bg_red]ALERTA! [reset]

[red]Texto 1.[reset] Quem estuda vence. [yellow]Isto[reset] é um fato.

[blue]O correto seria 'isso' em regra resumindo o fato anterior.[reset]

Pergunta 1. No texto, 'isto' se referiu à frase anterior? SIM. É um pergunta somente interpretativa. Sem levar em conta a regra.

Pergunta 2. O texto respeitou a norma culta padrão de linguagem? NÃO! O correto seria 'isso', retomando a ideia anterior.

        Depende do que a banca perguntar:

    Quando a banca pergunta se o pronome demonstrativo 'isto' se refere a frase anterior, é o sentido no texto. SIM.

    Quando a banca pergunta se o pronome demonstrativo 'isto' respeitou o padrão culto da linguagem? Não.

Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura do Município de Valinhos - Professor II - Área Matemática - 2024 

O pronome demonstrativo que introduz o excerto “Esse é o principal indicador do interesse de um indivíduo por um cheiro.”
Atua, no contexto em que ocorre, como um elemento de coesão textual de referenciação. Isso porque é empregado para:

A. introduzir um novo elemento na sequência textual.
B. retomar um elemento já mencionado na sequência textual.
C. estabelecer uma relação de hiponímia com outro elemento da sequência textual.
D. estabelecer uma relação de hiperonímia com outro elemento da sequência textual.
E. estabelecer uma relação de sinonímia com outro elemento da sequência textual.

Gabarito letra 'B'.

O item A sugere a substituição de 'no qual' por 'em que' e 'que' por 'as quais'. 
A substituição está correta, pois 'em que' é uma forma válida de pronome relativo que retoma 'relatório' e 'as quais' retoma 'tragédias', mantendo a coesão e a concordância adequadas.

Pronome relativo retoma algo dito anteriormente.

Pronome demonstrativo também. Os pronomes demonstrativos dão ideia de espaço presente, passado ou passado distante.

Espaço presente: este (1° pessoa)

Espaço Passado: Esse (2° Pessoa)

Espaço Passado muito distante: Aquele "dia"(3° Pessoa)

40. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE /Prova: CESPE/CEBRASPE - MPU - Técnico do Ministério Público - Área Administração Área: Auditoria - Pós-Edital - 2024 - 1º Simulado 

Dada a tecnologia do século XX, seria ineficiente concentrar informação e poder demais num só lugar. 

Ninguém tinha capacidade para processar toda a informação com rapidez suficiente para tomar decisões corretas. 

[yellow]Essa[reset] é em parte a razão de a União Soviética ter tomado decisões muito piores que as dos Estados Unidos, e de a economia soviética ter ficado bem atrás da economia americana.

No primeiro parágrafo, o pronome “Essa” (último período) retoma “Dada a tecnologia do século XX, seria ineficiente concentrar informação e poder demais num só lugar” (terceiro período).

C.Certo
E.Errado

[red]ERRADO.[reset]

[yellow]O pronome “Essa” no último período do primeiro parágrafo refere-se à afirmação “Ninguém tinha capacidade para processar toda a informação com rapidez suficiente para tomar decisões corretas”.[reset]


'''                    
    def verbo(self):
        return '''Verbos:

É a palavra mais variável da língua portuguesa que expressa ação ( estudar ), posse ( ter, possuir ), fato ( ocorrer ), estado ( ser, estar )
			    fenômeno ( chover, ventar ) e situados no tempo: passado, presente e futuro.
				                Chove agora, choveu ontem, choverá amanhã.

Conjugação é a distribuição dos verbos em sistemas conforme a terminação do infinitivo:

[red]-ar[reset] -> cantar, estudar: 1º conjugação
[red]-er[reset] -> ver, crer: 2º conjugação
[red]-ir[reset] -> dirigir, sorrir: 3º conjugação

	As vogais antes da terminação do infinitivo -R são 'a', 'e', 'i' são chamadas de vogais temáticas.
	Somente 'pôr' e derivados ficam sem vogal temática no infinitivo, mas têm nas conjugações: põe, pusera.

Estrutura verbal:\n
[red]RADICAL:[reset] é a parte invariável do verbo no infinitivo, retirada a vogal temática e a desinência -r, por exemplo: cant-, dirig-\n
[red]TEMA:[reset] é a junção da vogal temática ao radical: canta-, cre-, dirigi-


[red]Forma rizotônica:[reset] é a forma verbal com vogal tônica no radical:[yellow] estUda, vIvo, vImos. Pronúncia e não escrita. Tudo que tem ligação com a raiz.[reset]
[red]Forma arrizotônica:[reset] é a forma verbal com vogal tônica fora do radical: [yellow]estud-Amos, viv-Eis, vir-Iam.[reset]

    	para que serve isso? lá na frente, os verbos irregulares, em alguns verbos, terão mudanças na forma rizotônica.
                    Onde terá mudança no radical

[red]Flexão verbal:[reset] Pode ser em número ( singular ou plural ) , de pessoa (primeira, segunda, terceira) ou de tempo e modo.
[red]Flexão de número:[reset] no singular, ele chega // No plural: nós aprendemos, eles chegam.
[red]Flexão de pessoa:[reset] 1º pessoa é o emissor da mensagem -> EU CANTO // 2º pessoa é o receptor da mensangem -> TU CANTAS, Vós cantais

	        [bg_red]obs: 'vós' se refere a uma só pessoa, indica singular apesar de tomar a flexão plural. É uma forma respeitosa.[reset]

[red]Flexão de tempo:[reset] situa o momento do fato: presente, pretérito e futuro ( basicamente )

[red]Flexão de modo:[reset] indica atitude do falante e condições de fato ou ação.

	[blue]Modo indicativo:[reset] traduz geralmente a segurança, certeza.[yellow] Eu estudei. Não agi mal. Amanhã chegarão os convites.[reset]\n
	[blue]Modo subjuntivo:[reset] traduz a incerteza, dúvida e possibilidade. Usada emm orações subordinadas.\n
		        Quero que ele venha logo.
		        Gostaria que ele viesse logo.
		        Será melhor que ele vier a pé.

[yellow]Modo imperativo:[reset] expressa ordem, conselho, convite, súplica, pedido. Se dirige ao ouvintes: tu, você, vós, vocês. Não se dirige a si próprio.


São três tempos primitivos: infinito impessoal ( terminação -R ), presente do indicativo, pretérito perfeito simples do indicativo.

Derivados do infinito impessoal surge:

	1. o pretérito imperfeito do indicativo
	2. futuro do presente do indicativo
	3. futuro do pretérito do indicativo
	4. infinitivo pessoal ( para eu chegar ), ( para tu chegares ), (para ele chegar), ( para nós chegarmos ), (para vós chegardes), (para eles chegarem)
	5. gerúndio
	6. particípio

Os tempos podem assumir duas formas:

[red]a.[reset] [blue]Simples:[reset]  um só verbo -> Estudo francês. Terminaoms o livro. Faremos revisão.
[red]b.[reset] [blue]Composto:[reset] [yellow]verbos 'ter' ou 'haver' + particípio[reset]: tenho estudado, tinhamos estudado, haveremos feito.

	locução verbal = verbo auxiliar + verbo principal
		O tempo composto é um forma especial de locução verbal.
			1º verbo 'haver' ou 'ter' + verbo principal no particípio com terminação -ADO/-IDO
	'Vou estudar' por exemplo é uma locução verbal simples
         Agora 'tenho estudado' é uma locução verbal de tempo composto

         [bg_red]Esquema DESINÊNCIAS DOS TEMPOS DO MODO DO INDICATIVO E DO SUBJUNTIVO:[reset]

	[red]- Futuro do pretérito indicativo[reset] : [yellow]-RIA para verbos de 1º,2º,3º conjugação[reset]
	[red]- Futuro do presente  indicativo[reset] : [yellow]-REI para verbos de 1º,2º,3º conjugação[reset]
	[red]- Futuro do subjuntivo[reset] : [yellow]Terminação '-R' ->  quando eu sonhar / se eu sonhar p/ verbos na 1º,2º,3º conjugação[reset]
	[red]- Presente do indicativo[reset] : [yellow]- Terminação 'O' para verbos de 1º,2º,3º conjugação[reset]
	[red]- Presente do subjuntivo[reset] : [yellow]- Terminação 'e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
	[red]- Pretérito imperfeito indicativo[reset] : [yellow]- Para verbos de 1º conjugação 'ava' / para verbos de 2º conjugação 'ia' / 3º 'ia'[reset]
	[red]- Pretérito perfeito do indicativo[reset] : [yellow]- 'ei' para verbos de 1º conjugação / 'i' para verbos de 2º conjugação / 'i' também para verbos de 3º conjugação[reset]
	[red]- Pretérito mais-que-perfeito do indicativo[reset] : [yellow]- 'ara' para verbos de 1º conjugação / 'era' - para verbos de 2º conjugação / 'ira' -> para verbos de 3º conjugação[reset]
	[red]- Pretérito imperfeito do subjuntivo[reset] : [yellow]- 'asse' para verbos de 1º conjugação / 'esse' para verbos de 2º conjugação / 'isse' -> para verbos de 3º conjugação[reset]

Verbo regular SONHAR : 1º conjugação => -AR

	- eu sonho    	   - Presente do indicativo -> [yellow]Terminação 'O' para verbos de 1º,2º,3º conjugação[reset]
	- eu sonharei 	   - Futuro do presente do indicativo -> [yellow]REI para verbos de 1º,2º,3º conjugação[reset]
	- eu sonharia 	   - Futuro do pretérito do indicativo -> [yellow]-RIA para verbos de 1º,2º,3º conjugação[reset]
	- eu sonhava  	   - Pretérito Imperfeito do indicativo -> [yellow]Para verbos de 1º conjugação 'ava' / para verbos de 2º conjugação 'ia' / 3º 'ia'[reset]
	- eu sonhei   	   - Pretérito Perfeito do indicativo - [yellow]'ei' para verbos de 1º conjugação / 'i' para verbos de 2º conjugação / 'i' também para verbos de 3º conjugação[reset]
	- eu sonhara  	   - Pretérito mais-que-perfeito do indicativo - [yellow]'ara' para verbos de 1º conjugação / 'era' - para verbos de 2º conjugação / 'ira' -> para verbos de 3º conjugação[reset]
	- se eu sonhasse   - Pretérito imperfeito do subjuntivo - [yellow]'asse' para verbos de 1º conjugação / 'esse' para verbos de 2º conjugação / 'isse' -> para verbos de 3º conjugação[reset]
	- que eu sonhe     - Presente do subjuntivo - [yellow]- e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
	- quando eu sonhar - Futuro do subjuntivo - [yellow]'-R' c/ preposição quando eu sonhar / se eu sonhar p/ verbos na 1º,2º,3º conjugação[reset]

Verbo regular VIVER : 2º conjugação -ER   

    - eu vivo    - Presente do indicativo -> [yellow]Terminação 'O' para verbos de 1º,2º,3º conjugação [reset]
	- eu viverei - Futuro do presente do indicativo -> [yellow] -REI para verbos de 1º,2º,3º conjugação[reset]
	- eu viveria - Futuro do pretérito do indicativo - [yellow] -RIA para verbos de 1º,2º,3º conjugação[reset]
	- eu vivia   - Pretérito imperfeito do indicativo -> [yellow] Para verbos de 1º conjugação 'ava' / para verbos de 2º conjugação 'ia' / 3º 'ia' [reset]
	- eu vivi    - Pretérito perfeito do indicativo -> [yellow] 'ei' para verbos de 1º conjugação / 'i' para verbos de 2º conjugação / 'i' também para verbos de 3º conjugação [reset]
	- eu vivera  - Pretérito mais-que-perfeito do indicativo - [yellow] 'ara' para verbos de 1º conjugação / 'era' - para verbos de 2º conjugação / 'ira' -> para verbos de 3º conjugação [reset]
	- se eu vivesse   - Pretérito imperfeito do subjuntivo - [yellow] 'asse' para verbos de 1º conjugação / 'esse' para verbos de 2º conjugação / 'isse' -> para verbos de 3º conjugação[reset]
	- que eu viva     - Presente do subjuntivo - [yellow] - 'e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
	- quando eu viver - Futuro do subjuntivo - [yellow] '-R' c/ preposição quando eu sonhar / se eu sonhar p/ verbos na 1º,2º,3º conjugação[reset]

Verbo regular SAIR - 3º Conjugação -IR

	- Eu saio   - Presente do indicativo -> [yellow] Terminação 'O' para verbos de 1º,2º,3º conjugação [reset]
	- Eu sairei - Futuro do presente do indicativo - [yellow] -REI para verbos de 1º,2º,3º conjugação [reset]
	- Eu sairia - Futuro do pretérito do indicativo - [yellow] -RIA para verbos de 1º,2º,3º conjugação[reset]
	- Eu saía  - Pretérito Imperfeito do indicativo - Para verbos de 1º conjugação 'ava' / para verbos de 2º conjugação 'ia' / 3º'ia'[reset]
	- Eu sai   - Pretérito Perfeito do indicativo - 'ei' para verbos de 1º conjugação / 'i' para verbos de 2º conjugação / 'i' também para verbos de 3º conjugação[reset]
	- Eu saíra - Pretérito mais-que-perfeito do indicativo - 'ara' para verbos de 1º conjugação / 'era' - para verbos de 2º conjugação / 'ira' -> para verbos de 3º conjugação[reset]
	- que eu saia - Presente do subjuntivo - [yellow] - 'e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
	- se eu / quando eu sair - Futuro do subjuntivo - [yellow] '-R' c/ preposição quando eu sonhar / se eu sonhar p/ verbos na 1º,2º,3º conjugação[reset]
	- se eu / que eu saísse  - Pretérito imperfeito do subjuntivo - [yellow] 'asse' para verbos de 1º conjugação / 'esse' para verbos de 2º conjugação / 'isse' -> para verbos de 3º conjugação[reset]

Questão 01 - IADES,CAU/RJ - Considerando o trecho 'criou uma planta única, inovadora que destoava de todos os palácios', assinale a alternativa que indica
respectivamente, tempo/modo em que cada verbo se encontra conjugado:

a. Presente do subjuntivo e pretérito imperfeito do indicativo.
b. Pretérito perfeito do indicativo e pretérito imperfeito do indicativo.
c. Pretérito imperfeito do subjuntivo e pretérito mais-que-perfeito do indicativo.
d. Pretérito perfeito do indicativo e pretérito imperfeito do subjuntivo.
e. Pretérito imperfeito do subjuntivo e pretérito perfeito do indicativo.
	
'criou' / 'destoava'
'destoava' -AVA - Pretérito imperfeito do indicativo
'criou' - Ideia que passou - Pretérito perfeito do indicativo 2º pessoa do discurso.

a. Presente do subjuntivo e pretérito imperfeito do indicativo.
b. Pretérito perfeito do indicativo e pretérito imperfeito do indicativo. [bg_green][CORRETO][reset]
c. Pretérito imperfeito do subjuntivo e pretérito mais-que-perfeito do indicativo.
d. Pretérito perfeito do indicativo e pretérito imperfeito do subjuntivo.
e. Pretérito imperfeito do subjuntivo e pretérito perfeito do indicativo.


[bg_red]O teste para saber se o verbo é regular ou irregular é na 1º pessoa do discurso: EU no tempo presente.[reset]
	
	A letra e som precisa mudar. Existem verbos que mudam somente a letra e continua sendo verbo regular.
		AGIR -> eu ajo.  Certo, mas possui o mesmo som. Portanto é um verbo regular.
		TRAZER -> eu trago. Som e letra diferente -> verbo irregular.

	VERBOS IRREGULARES: Muda letra e/ou som no radical e ou nas terminações.

    Verbo Irregular: TER - Derivados: 'obter','conter','deter','reter','entreter',...

Os derivadores terão o mesmo radical sempre.

	eu tenho - presente do indicativo -> Terminação 'O' para verbos de 1º,2º,3º conjugação
	eu terei - futuro do presente do indicativo -> -REI para verbos de 1º,2º,3º conjugação
	eu teria - futuro do pretérito do indicativo -> -RIA para verbos de 1º,2º,3º conjugação
	eu tinha - pretérito imperfeito do indicativo -> Irregularidade
	eu tive  - pretérito perfeito do indicativo  -> Irregularidade
	eu tivera - pretérito mais que perfeito do indicativo - 'ara' para verbos de 1º conjugação / 'era' - para verbos de 2º conjugação / 'ira' -> para verbos de 3º conjugação

	que eu tenha - presente do subjuntivo -  [yellow]'e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
	quando eu tiver / se eu tiver - futuro do subjuntivo - [yellow]Terminação '-R' c/ preposição : quando eu sonhar / se eu sonhar p/ verbos na 1º,2º,3º conjugação[reset]
	se eu tivesse/ que eu tivesse - pretérito imperfeito do subjuntivo - [yellow] 'asse' para verbos de 1º conjugação / 'esse' para verbos de 2º conjugação / 'isse' -> para verbos de 3º conjugação[reset]

Verbo Irregular: PÔR - Derivados: 'repor','dispor','compor','interpor','...' (POER)

Os derivadores terão o mesmo radical sempre

eu poria / eu interporia -   futuro do pretérito do indicativo - RIA para verbos de 1º,2º,3º conjugação
eu ponho / eu interponho -   presente do indicativo -> Terminação 'O' para verbos de 1º,2º,3º conjugação
eu porei / eu interporei -   futuro do indicativo -REI para verbos de 1º,2º,3º conjugação
eu punha / eu interpunha -   pretérito imperfeito do indicativo -  Irregularidade
eu pus 	 / eu interpus   -   pretérito perfeito do indicativo - Irregularidade
eu pusera / eu interpusera - pretérito mais-que-perfeito do indicativo - 'ara' para verbos de 1º conjugação / 'era' - para verbos de 2º conjugação / 'ira' -> para verbos de 3º conjugação

que eu ponha  - presente do subjuntivo - [yellow]'e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
quando eu puser   - futuro do subjuntivo - [yellow] Terminação'-R' c/ preposição quando eu sonhar / se eu sonhar p/ verbos na 1º,2º,3º conjugação[reset]
se/que eu pusesse / interpusesse - pretérito imperfeito do subjuntivo - [yellow] 'asse' para verbos de 1º conjugação / 'esse' para verbos de 2º conjugação / 'isse' -> para verbos de 3º conjugação[reset]

Verbo Irregular: VER - Derivados: REVER / ANTEVER / PREVER 

Os derivadores terão o mesmo radical sempre

eu veria - futuro do pretérito do indicativo - RIA para verbos de 1º,2º,3º conjugação
eu verei - futuro do presente indicativo -REI para verbos de 1º,2º,3º conjugação
eu vejo  - Presente do indicativo -> Terminação 'O' para verbos de 1º,2º,3º conjugação
eu via   - pretérito imperfeito do indicativo -> Para verbos de 1º conjugação 'ava' / para verbos de 2º conjugação 'ia' / 3º 'ia'
eu vi    - Pretérito perfeito do indicativo -> 'ei' para verbos de 1º conjugação / 'i' para verbos de 2º conjugação / 'i' também para verbos de 3º conjugação
eu vira  - Pretérito mais-que-perfeito do indicativo 'ara' para verbos de 1º conjugação / 'era' - para verbos de 2º conjugação / 'ira' -> para verbos de 3º conjugação

Subjuntivo:

	quando / se eu vir  - Futuro do subjuntivo - [yellow] Terminação'-R' c/ preposição quando eu sonhar / se eu sonhar p/ verbos na 1º,2º,3º conjugação[reset]
	que eu veja         - Presente do subjuntivo [yellow]'e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
	se / que eu visse   - Irregularidade
	
Verbo Irregular: VIR - Derivados: INTERVIR / SOBREVIR / ADVIR /  CONVIR

Os derivadores terão o mesmo radical sempre

EU VIRIA - Futuro do Pretérito do indicativo [yellow] RIA para verbos de 1º,2º,3º conjugação [reset]
eu virei - Futuro do indicativo -> [yellow]-REI para verbos de 1º,2º,3º conjugação[reset]
eu venho - Presente do indicativo -> [yellow]Terminação 'O' para verbos de 1º,2º,3º conjugação[reset]
eu vinha - Pretérito imperfeito do indicativo - Irregularidade
eu vim   - Pretérito perfeito do indicativo - Irregularidade
eu viera - Pretérito mais-que-perfeito do indicativo - Irregularidade

Futuro do subjuntivo - quando eu vier / se eu vier ( retira a vogal do preterito mais-que-perfeito do indicativo p/ usar no futuro do subjuntivo )
que eu venha - Presente do subjuntivo -[yellow]'e' para verbos da 1º conjugação./ 'a' para verbos de 2º conjugação / 'a' para verbos de 3º conjugação [reset]
se eu /  que eu viesse - Pretérito imperfeito do subjuntivo se/que eu pusesse / interpusesse - Irregularidade

Verbo irregular anômalos: SER / IR <- Verbos anômalos muda até o radical

[red]Presente do Indicativo[reset] -> [yellow]Eu sou / Tu és / Ele é / Nós somos / Vós sois / Eles são [reset]
[red]Pretérito Perfeito do indicativo[reset] -> [yellow]Eu fui / Tu foste / Ele foi / Nós fomos / Vós fostes / Eles foram[reset]
[red]Pretérito Imperfeito do indicativo[reset] -> [yellow]Eu era / Tu eras / Ele era / Nós éramos / Vós éreis / Eles eram[reset]
[red]Pretérito Mais-que-perfeito do indicativo[reset] ->[yellow] Eu fora / Tu foras / Ele fora / Nós fôramos / Vós foreis / Eles foram[reset]
[red]Futuro do presente do indicativo [reset]-> [yellow]Eu serei / Tu serás / Ele será / Nós seremos / Vós sereis / Eles serão[reset]
[red]Futuro do pretérito do indicativo [reset]->[yellow] Eu seria / Tu serias / Ele seria / Nós seriamos / Vós seríeis / Eles seriam[reset]
[red]Presente do subjuntivo[reset] -> [yellow]que eu seja /  que tu sejas / que ele seja / que nós sejamos / que vós sejais / que eles sejam[reset]
[red]Pretérito imperfeito do subjuntivo[reset] ->[yellow] se eu fosse / se tu fosses / se ele fosse / se nós fossemos / se vós fosseis / se eles fossem[reset]
[red]Futuro do subjuntivo[reset] -> [yellow]quando eu for / quando tu fores / quando ele for / quando nós formos / quando vós fordes / quando eles forem[reset]


Verbo irregular IR:
	
[red]Presente do indicativo[reset] -> [yellow]Eu vou / Tu vais / Ele vai / Nós vamos / Vós ides / Eles vão[reset]
[red]Pretérito Perfeito do indicativo [reset]-> [yellow]Eu fui / Tu foste / Ele foi / Nós fomos / Vós fostes / Eles foram[reset]
[red]Pretérito Imperfeito do indicativo[reset] -> [yellow]Eu ia / Tu ias / Ele ia / Nós íamos / Vós ieis / Ele iam [reset]
[red]Pretérito mais-que-perfeito do indicativo[reset] -> [yellow]Eu fora / Tu foras / Ele fora / Nós foramos / Vós foreis / Eles foram[reset]
[red]Futuro do pretérito do indicativo [reset]-> [yellow]Eu iria / Tu irias / ELe iria / Nós iríamos / Vós iríeis / Eles iriam[reset]
[red]Futuro do presente do indicativo [reset]->[yellow] Eu irei / Tu irás / Ele irá / Nós iremos / Vós ireis / Eles irão[reset]
[red]Presente do subjuntivo[reset] -> [yellow]que eu vá / que tu vás / que ele vá / que nós vamos / que vós vades / que eles vão[reset]
[red]Pretérito imperfeito do subjuntivo[reset] ->[yellow] se eu fosse /  se tu fosses /  se ele fosse /  se nós fossemos / se vós fosseis / se eles fossem[reset]

[bg_red] ATENÇÃO! [reset]
	Irá depender do contexto e o sentido na frase em relação ao verbo IR ou SER, porque ambos são iguais em sua conjugação.

Pretérito Perfeito do indicativo do verbo SER  -> Eu fui / Tu foste / Ele foi / Nós fomos / Vós fostes / Eles foram
Pretérito Perfeito do indicativo do verbo IR   -> Eu fui / Tu foste / Ele foi / Nós fomos / Vós fostes / Eles foram

	Eu fui ao colégio -> Verbo IR
	Eu fui vendedor   -> Verbo SER

Pretérito Mais-que-perfeito do indicativo do verbo SER -> Eu fora / Tu foras / Ele fora / Nós fôramos / Vós foreis / Eles foram
Pretérito mais-que-perfeito do indicativo do verbo IR  -> Eu fora / Tu foras / Ele fora / Nós foramos / Vós foreis / Eles foram

 O verbo foi não é do verbo ir? Depende do contexto:
	Vejamos:

		Eu fui a praia. ( É do verbo ir )
		Eu fui feliz.   ( É do verbo ser )

Futuro do subjuntivo do verbo SER -> quando eu for / quando tu fores / quando ele for / quando nós formos / quando vós fordes / quando eles forem
Futuro do subjuntivo do verbo IR  -> quando eu for / quando tu fores / quando ele for / quando nós formos / quando vós fordes / quando eles forem

Pretérito imperfeito do subjuntivo do modo subjuntivo do verbo IR  - se eu fosse / se tu fosses / se ele fosse / se nós fôssemos / se vós fôsseis / se eles fossem
Pretérito imperfeito do subjuntivo do modo subjuntivo do verbo SER - se eu fosse / se tu fosses / se ele fosse / se nós fôssemos / se vós fôsseis / se eles fossem

CESPE - SEDF - 
'O transporte é público. O corpo da mulher não. Se você for vítima ou vir alguém sendo assediado. Ligue 190 e denuncie.'

	No período 'for' e 'vir' são formas flexionadas no modo subjuntivo dos verbos do movimento 'ir' e 'vir', empregadas
em um jogo de palavras que aproximam o campo semântico do movimento com o campo semântico do transporte.

[bg_yellow]Se vc 'for' vítima, está sofrendo a ação, portanto está flexionada na primeira pessoa do discurso do verbo irregular SER do futuro do subjuntivo e não do verbo IR.[reset]
[bg_yellow]E o verbo se vc 'vir' alguém, no sentido de VER ALGUÉM. Portanto a o verbo está flexionado na primeira pessoa do discurso do verbo VER e não do verbo VIR.[reset]

[bg_red]Questão totalmente ERRADA. [reset]'''

    def modo_imperativo(self):
        return '''Modo imperativo:
            
            - Expressa ordem, conselho, convite, súplica, pedido. Dirige-se aos ouvintes: tu, você, vós, nós
            
            
            O imperativo pode ser Afirmativo:
	
	- Tu e vós vêm do presente do indicativo, retirando o '-s' final: deixa (tu), deixai (vós) [yellow][ O resto vem do presente do subjuntivo ][reset]

    O imperativo pode ser Negativo:

	- Copia exatamente o presente do subjuntivo: não deixes tu, não deixe você, não deixemos nós, não deixeis vós, não deixem vocês.
		No presente do subjuntivo é: que eu deixe, que tu deixes, que você deixe, que nós deixemos, que vós deixeis, que eles deixem. sem o 'não'

        Presente do indicativo     Imperativo Afirmativo      Presente do subjuntivo           Imperativo negativo
	        Eu   falo					                            Que eu fale			
	        Tu   falas		            Fala    (tu) -s		        Que tu fales			    Não fales   (tu)
	        Ele/você fala		        Fale    (você)		        Que ele/você fale		    Não fale    (você)	
	        Nós  falamos		        Falemos (nós)		        que nós falemos			    Não falemos (nós)
	        Vós  falais		            Falai   (vós) -s	        que vós faleis			    Não faleis  (vós)
	        Eles falam		            Falem   (vocês)		        que eles/vocês falem		Não falem   (vocês)

    Completa em conformidade com a gramática normativa, respeitando a uniformidade de tratamento:

a. Quando você chega, eu peço:  - Fal___-me como foi seu dia!  Pronome 'seu' combina com 'você'
b. Quando tu chegas, eu peço:   - Fal___-me como foi teu dia!  Pronome 'teu' combina com 'tu'
c. Quando vós chegais, eu peço: - Fal___-me como foi vosso dia! Pronome 'vosso' combina com 'vosso'

a. Quando você chega, eu peço:  - Fal___-me como foi seu dia!  [Fale-me como foi seu dia!] - 3º pes do sing do imperativo afirmativo e presente do subjuntivo
b. Quando tu chegas, eu peço:   - Fal___-me como foi teu dia!  [Fala-me como foi teu dia!] - 2º pes do sing do imperativo afirmativo e presente do subjuntivo.
c. Quando vós chegais, eu peço: - Fal___-me como foi vosso dia!  [Falai-me como foi vosso dia!]- 2º pes do plural do imper. afirm. e pres. do subjuntivo.

Presente do indicativo      Imperativo afirmativo  Presente do subjuntivo      Imperativo negativo
	Eu dou						Que eu dê			
	Tu dás			Dá (tu) -s		que tu dês			não dês (tu)
	Ele/você dá		dê (você)		que ele/você dê			não dê (você)
	Nós damos		Demos (nós)		que nós demos			não demos (nós)
	Vós dais		dai (vós) -s		que vós deis			não deis (vós)
	Eles dão		deem (vocês)		que eles/vocês deem		não deem (vocês)

    
    Complete:

	Pai nosso, que estais nos céus: Santificado seja o Vosso nome... O pão nosso de cada dia d___-nos hoje.

Perdo___ as nossas ofensas.. Não nos deix___ cair em tentação, mas livr___-nos do mal.

	Pai nosso que estás nos céus: Santificado seja o teu nome...  O pão nosso de cada dia d___ -nos hoje.

Pedo___ as nossas ofensas. Não nos deix___ cair em tentação, mas livr___-nos do mal. Amém.

	Pai nosso, que estais nos céus: Santificado seja o Vosso nome... O pão nosso de cada dia d___-nos hoje.

[bg_yellow][Se eu escrevo 'estais' estou considerando sujeito subintendido 'vós' - 'que o Senhor (vós), aquele que estais nos céus' - 'vosso nome...' - Uniformidade de tratamento][reset]\n
[bg_green]['dai-nos hoje...' hoje - 2º pessoa do plural do imperativo afirmativo em uniformidade com o 'estais' no início da frase][reset]

		[bg_yellow][Lembrando que modo imperativo afirmativo deve ser em modo ênclise - pronome depois do verbo][reset]
		[bg_yellow][Lembrando que no modo imperativo negativo o modo é próclise - pronome antes do verbo][reset]

Perdo___ as nossas ofensas.. Não nos deix___ cair em tentação, mas livr___-nos do mal.

[Vós perdoais - Presente do indicativo e para conjugar no modo imperativo afirmativo retirao final -s - perdoai (vós) as nossas ofensas]

'Não nos deix___ cair em tentação, mas livr___-nos do mal.' 

    [[No presente do subjuntivo é o mesmo do imperativo negativo: a 2º pessoa do plural é 'que vós deis/deixeis - Não deixeis (vós) cair em...]

    [O verbo 'livrar' no presente do indicativo da 2º pessoa do plural é - 'nós livrais' - lembrando que para afirmativo imperativo retira o -s final - livrai (vós)
	Portanto, '... mas livrai-nos do mal.'

    	Pai nosso que estás nos céus: Santificado seja o teu nome...  O pão nosso de cada dia d___ -nos hoje.\n

        [bg_red] ATENÇÃO! [Agora a segunda parte da oração é referente ao presente do indicativo na 2º pessoa do discurso 'tu' - tu estás][reset]\n
       	[Portanto, para uniformidade, para afirmativo imperativo retira o final -S do presente do indicativo - 'está (tu)'/ 'dá (tu)' / dá-nos hoje - pedido]
           
        Perdo___ as nossas ofensas.            

        [tu no presente do indicativo é 'tu perdoas', para o afirmativo imperativo retira o -s final - / perdoa (tu), ou seja, '... perdoa nossas ofensas...']

        Não nos deix___ cair em tentação, mas livr___-nos do mal. Amém.	

        [Para imperativo negativo é o mesmo que o presente do subjuntivo - Como se refere a 2º pessoa do discurso 'tu' é: que tu deixes / Não deixes (tu)]        

        Não nos deixes cair em tentação, mas livr__-nos do mal. Amém.

        tu livras - Presente do indicativo 2º pessoa do discurso, retirar o final -s para conjugar corretamente no imperativo afirmativo - 'livra (tu)'
            portanto... [yellow]mas livra-nos do mal. Amém.[reset]


QUADRIX-SEDF:

- Olha aí, 'soberba'. Se você falar 'soberba', ninguém vai saber o que é. Não fala 'soberba'. Nem 'todavia'. Nem 'outrossim'. E cuidado com os pronomes.
	Para que a oração 'não fala soberba' esteja em conformidade com a gramática normativa da língua portuguesa, é necessária a flexão da forma verbal
'fala' no modo imperativo negativo, a depender da pessoa verbal: NÃO FALES 'SOBERBA' OU 'NÃO FALE SOBERBA'.

	O subjuntivo do presente é: que eu fale /  que tu fales igual  / que vc fale /  que nós falemos / que vós faleis / que eles falem
    No imperativo negativo : não fales (tu) / não fale (você) / não falemos (nós) / não faleis (vós) / não falem (eles)

	[yellow]'Não fales 'soberba'[reset] na 2º pessoa do singular do discurso - [bg_green]CORRETO[reset]
	[yellow]'Não fale você 'soberba'[reset] na 3º pessoa do singular do discurso - [bg_green]CORRETO[reset]

        [bg_green]Afirmação da questão está correta.[reset]
            [bg_red]  O texto estava mesmo equivocado e a questão estava certa em corrigir o modo correto [reset]
'''

    def formas_nominais_verbo(self):
        return '''[bg_red]Formas nominais dos verbos:[reset]

	- [bg_yellow]Não exprimem nem tempo nem modo. São valores de substantivo ou adjetivo.[reset]
		- São formas: Infinitivo / gerúndio / particípio

	[bg_green]O infinito é a pura ideia de ação.[reset]

	Infinito impessoal: não se refere a uma pessoa, nenhum sujeito próprio. É A IDEIA DE AÇÃO.\n

		Ex: É agradável [yellow]viajar.[reset] <- [blue]ação de viajar sem se referir a uma pessoa.[reset]\n
			Posso [yellow]falar[reset] com João. <- [blue]'falar' não tem sujeito próprio. O verbo 'posso' tem o sujeito próprio que é "EU".[reset]

	O infinito impessoal pode funcionar como sujeito de outro verbo:
		Ex: [yellow]Navegar[reset] [bg_yellow]é[reset] preciso, [yellow]viver[reset] não é preciso. [blue][ Navegar se refere ao verbo SER=>'é'][reset]
			[blue][Verbo 'viver' se refere ao verbo SER flexionado 'é'][reset]

    O infinito impessoal pode exercer função de predicativo:
		Ex: Seu maior sonho [yellow]é cantar.[reset] <- [blue]'é' -> verbo de ligação + predicativo do sujeito representado pelo verbo 'cantar'[reset]

   	O infinito impessoal pode exercer função de objeto direto:
		Ex: Admiro [yellow]o cantar[reset] dos pássaros. [blue][Funcionando como substantivo devido ao artigo, derivação imprópria.'o cantar'][reset]
            
	O infinito impessoal pode exercer função de objeto indireto:
		Ex: Gosto [yellow]de viajar[reset] -> [blue]Objeto Indireto precede de preposição: 'de' antes do verbo 'viajar'[reset]

   	O infinito impessoal pode exercer função de adjunto adnominal:
		Ex: Comprei livros [yellow]de desenhar[reset] -> [blue]'de desenhar' está qualificando o substantivo 'livros', portanto, adjunto adnominal.[reset]

  	O infinito impessoal pode exercer função de complemento nominal:
		Ex: Este livro é [yellow]bom[reset] [green]de ler.[reset] => [blue]'bom' => adjetivo + complemento nominal 'de ler' [reset]

    O infinito impessoal pode vir no lugar do gerúndio:
		Ex: Estou a [yellow]pensar[reset] => [blue]gerúndio => ( estou pensando )[reset] <- Ambos corretos

   	O infinito impessoal pode ter valor passivo:
		Ex: O dano é fácil de [yellow]reparar.[reset] Frutas boas de [yellow]comer.[reset]

        	[blue]O dano é raparado - valor passivo. Frutas não comem, elas são comidas -> valor passivo[reset]

	O infinito impessoal pode ter tom imperativo:
		Ex: O que nos falta é [yellow]estudar.[reset] -> 'estudar' => [blue]um conselho[reset]

[bg_yellow]O infinito impessoal pode ser escrito de duas formas diferentes: Forma simples e forma composta.[reset]

    	[blue]Forma simples[reset]: valor de presente, atual momento que se prolonga no tempo. Possui somente um verbo.
Ações de aspecto não concluido:\n

	Ex: [yellow]Estudar[reset] Português ajuda em todas as provas.
		ideia de [blue]'estudar' é algo habitual, aspecto não concluido.[reset]

	Ex: [yellow]Perder[reset] o jogo irrita.
		[blue]ideia de 'perder' sempre irrita, algo/aspecto que não é concluido.[reset]

        
        [blue]Forma composta:[reset] 2 verbos e que indica passado, porém de ações de aspecto concluido no passado!!

		Ex: [yellow]Ter estudado[reset] Português ajuda nas provas. \n
			Os tempos compostos são locuções verbais com 2 verbos : 'ter estudado' \n
	[blue]Tendo o verbo 'haver' e 'ter' como verbos auxiliares são em forma nominal infinitivo.[reset]
	[green]O verbo 'estudado' está na forma nominal no particípio.[reset]

		Ex: [yellow]Ter perdido[reset] o jogo irrita. <- [blue]Aquilo que já passou. 'ter perdido' forma composto no infinito impessoal.[reset]

        
        [blue]INFINITO PESSOAL:[reset]
		Refere-se a um sujeito próprio.\n
Que podem vir marcadas com as desinências das pessoas no verbo: sermos, serem

		Ex: Não [yellow]estudou[reset] para [yellow]errar.[reset]

        [blue]	[Temos duas ações diferentes na mesma frase, com dois verbos diferentes.][reset]
		[blue]'estudar' é uma ação / 'errar' é outra ação [reset]<-[red] NÃO FORMA LOCUÇÃO VERBAL.[reset]
			[green]Portanto podemos considerar que ele/ela para 'estudar' e também ele/ela para 'errar'[reset]

	[blue]Agora um exemplo de locução verbal[reset] : [yellow]'vou acertar'[reset] <- [green]dois verbos juntos é uma locução verbal, e o sujeito é o do primeiro verbo -> EU 'VOU'[reset]
				[bg_yellow]Sendo também uma ação. Somente ação de acertar.[reset]
	Exemplos:
			Não estudamos para errarmos. <- Sujeito 'nós', mesmo sujeito para verbos diferentes. Ações diferentes. Nâo é locução verbal.

          	[bg_yellow]Infinitivo PESSOAL: refere-se a um sujeito próprio.[reset]

	Mesmo sujeito:
		
			Para nós [yellow]sermos[reset] pássaros, (nós) precisamos de imaginação. <- Mesmo sujeito para os dois verbos.\n
			[yellow]'sermos'[reset] <- infinito pessoal com desinência. 1º pessoa do plural
			'precisamos' <-

	Sujeito diferentes: ( Eu ) ouvi os pássaros cantarem. [blue] ( 'eu' sujeito & 'os pássaros' outro sujeito )[reset] <- Sujeitos diferentes.

	Preposicionados: Nós lhes dissemos isso [yellow]por[reset] sermos amigos. <- [blue]preposição : por[reset]

			 Nós lhes dissemos [yellow]por[reset] serem amigos. <- [blue]preposição : por[reset]

	Sujeito indeterminado: Sabe que existe mas não está escrito.
		
			       Ex: Naquela hora ouvi chegarem. [red][eles/elas??][reset]


[red]O infinito pessoal simples[reset] : refere-se ao presente momento e possui aspecto não concluido.
		
	Ex: Por [yellow]chegarmos[reset] cedo, estamos em dia. / Por [yellow]chegarmos[reset] cedo, obtivemos uma vaga.

		[yellow]'chegarmos'[reset] => [blue]Forma nominal infinitivo pessoal simples[reset]

[red]O infinito pessoal composto[reset] : [blue]refere-se ao passado com aspecto concluido + verbo no participio.[reset]

	Ex: 	    Por [yellow]termos chegado[reset] cedo, obtivemos uma vaga.		

		    Por [yellow]termos chegado[reset] cedo, estamos em dia.

		[yellow]'termos'[reset] ->  [blue]verbo em sua forma nominal no infinito pessoal[reset]
		[yellow]'chegado'[reset] -> [blue]verbo em sua forma nominal no particípio[reset]

GERÚNDIO:

Forma nominal do verbo que exprime ação está em processo, em desenvolvimento. Possui valor de adjetivo ou advérbio.

	Chegou com os olhos [yellow]lacrimejando.[reset]  
[yellow]'lacrimejando'[reset] -> [blue]valor de adjetivo para o substantivo 'olhos' sendo verbo no gerúndio[reset]

    [bg_yellow] Portanto é um verbo em sua forma nominal gerúndio em que apresenta valor de ajetivo. [reset]

    	Vi-o [yellow]cantando.[reset] <- [blue]'cantando' valor adverbial de tempo[reset]

        Verbo no gerúndio pode ser usado em início de frase como uma ação anterior encerrada:

        	[yellow]Jurando[reset] vingança, atacou o ladrão.

        Verbo no gerúndio pode ser usado em ação anterior e continuada.

	[yellow]Fechando[reset] os olhos, começou a imaginar a festa.

Após um verbo, para ação simultânea: 
	
	Saí [yellow]cantando.[reset] /  Morreu [yellow]jurando[reset] inocência.

[bg_red]Maneira informal: ação posterior : Os juros subiram, reduzindo o consumo.[reset]

[bg_green]	Correção da maneira informal: Os juros subiram e reduziram o consumo.[reset]

[bg_yellow]Formas gerúndio simples: Aspecto não concluido no presente.[reset]

	Ex: [yellow]Sorrindo[reset], olha para o pai.  <- [blue]ainda olha para o pai sorrindo, sem concluir.[reset]
	
	    [yellow]Ignorando[reset] os perigos, continuou na estrada. <- [blue]continua na estrada ignorando os perigos, sem concluir a ação.[reset]

		[bg_red] Atenção! Na forma gerúndio simples em que o aspecto de ideia de não concluido no presente é somente com 1 verbo eu sua forma simples! [reset]

[bg_yellow]Forma gerúndio composto: aspecto de ação concluido no passado + verbo no particípio. 2 verbos em formas nominais diferentes.[reset]

	Ex: [yellow]Tendo[reset] sorrido, olhou para o pai.

		[yellow]Tendo[reset] compreendido os perigos, abandonou a estrada.

	[bg_yellow] ATENÇÃO! [reset]

	'tendo sorrido' <- temos uma locução verbal sendo do mesmo sujeito. 'tendo' -> verbo em sua formal nominal no gerúndio + verbo em sua forma nominal no particípio
	'tendo compreendido' <- locução verbal para o mesmo sujeito. 'tendo'( gerúndio ) + 'compreendido' ( particípio )

	[bg_yellow] Atenção ao aspecto de conclusão no passado para gerúndio composto , somente pela locução verbal! 2 verbos![reset]

PARTICIPIO : Terminação -ADO/-IDO. [blue]importante para a voz passiva.[reset]

Como tempo composto com verbo auxiliar TER ou HAVER (não varia em gênero e número)

	A polícia [yellow]tem prendido[reset] mais traficantes.

	Já [yellow]havíamos chegado[reset] quando você veio.


Com verbo auxiliar SER ou ESTAR, locução verbal ( varia em gênero e número ):

	Muitos ladrões [yellow]foram presos[reset] pela milícia. <- 'preso' é o participio irregular do verb PRENDER

	Os corruptos [yellow]estão presos.[reset]

[bg_yellow]SEM VERBO AUXILIAR: Quando o verbo no participio não tem verbo auxiliar.[reset]

	[bg_green] O verbo é um estado resultante de ação encerrada.[reset]

		[yellow]Derrotados[reset], os soldados não ofereceram resistência.

[bg_yellow]Particípio também é Ação encerrada: cantar -> cantado / beber -> bebido [reset]

	Verbos terminados na 1º conjugação (-AR) terão (-ADO) -> AMAR / AMADO
	Verbos terminados na 2º conjugação (-ER) terão (-IDO) -> VENDER / VENDIDO
	Verbos terminados na 3º conjugação (-IR) terão (-IDO) -> SORRIR / SORRIDO

    [bg_red]ATENÇÃO!  Verbo VIR e derivados:[reset]

	[bg_yellow]O verbo VIR no gerúndio e particípio possuem e assumem a mesma forma.[reset]

	Ex:
		[yellow]Tenho vindo[reset] aqui todo dia. [blue]( Particípio )[reset] <- [green]Com verbo auxiliar 'TER' sempre terá participio[reset]\n
			'Tenho chegado' -> Particípio
			'Tenho vindo'   -> Particípio mesmo o verbo 'vindo' parecer gerúndio, [blue]o verbo auxiliar 'ter' flexionado o torna sempre no particípio.[reset]

		[yellow]Estou vindo[reset] aqui todo dia. [blue]( Gerúndio )[reset]   
        
             [bg_green]Com verbo auxiliar 'ESTAR' sempre será gerúndio.[reset]

    O verbo no particípio sem os verbos auxiliares, pode-se tratar de adjetivo:

    	Ex: A criança [yellow]assustada[reset] não dorme.

        O verbo no participio sem verbos auxiliares pode ser substantivado:

	Ex: A [yellow]morta[reset] era inocente.

		[yellow]'a morta'[reset] ->[blue] substantivo que é do verbo 'morrer'[reset]

	    Muitos [yellow]mortos[reset] são enterrados como indigentes.

		'mortos' -> substantivo

Verbos conforme função dentro da locução verbal:

	[bg_yellow]O verbo principal é sempre o último verbo de uma locução verbal e deve ser do mesmo sujeito.[reset]
		
		Devo [yellow]estudar[reset] // Comecei a [yellow]sorrir.[reset]

	[bg_yellow]Os verbos auxiliares são os verbos anteriores na locução.[reset]

Não forma locução verbal:

	 	[yellow]Ana mandou[reset] [green]vir o convidado.[reset]

	'Ana mandou' <- 1º sujeito / 'vir o convidado' -> 2º convidado
			Verbos separados

    Dois sujeitos na oração. De forma independentes e na verdade separados em duas orações diferentes. não forma locução verbal.
Lembrando que somente quando o verbo for do mesmo sujeito que poderá ser locução verbal.
		
[red]Verbo SER[reset]: como verbo auxiliar, ou seja, anterior ao verbo principal da locução, funciona como voz passiva de ação. Ou seja, ação que o sujeito RECEBE.

	Exemplo:
			O livro [yellow]será aberto[reset] pelo escolhido. [blue] O sujeito é 'o livro'  e ação é o verbo principal -> 'aberto'[reset]
				[green]Portanto o sujeito 'o livro' é passivo da ação de ser aberto.[reset]

[red]VERBO ESTAR:[reset] também usado em voz passiva mas de ESTADO:
			
			O livro [yellow]está aberto.[reset]  <- 'o livro' sujeito da oração está na condição de aberto, situação de estar aberto.

[red]Verbo ESTAR + gerúndio[reset] : [blue]ação duradoura num momento preciso:[reset] 
	
		[yellow]Estou escrevendo[reset] um livro.

[red]VERBO TER E HAVER:[reset] como tempo composto + participio de outro verbo = locução verbal.

	Já [yellow]tinham ( ou haviam ) aberto[reset] o livro.

	Se [yellow]tivesse ( ou houvesse ) ficado[reset], não perderia o trem.

[red]Verbo TER ou HAVER com preposição 'de' [reset]+ infinitivo: sentido de obrigação (ter) ou de promessa ( haver )

	[yellow]Tenho de estudar[reset] mais. [blue][ verbo auxiliar 'ter' + preposição + infinitivo = locução verbal = mesmo sujeito ][reset]

	[yellow]Hei de chegar[reset] cedo amanhã. [blue][ verbo auxiliar 'haver' + prep + infinitivo = loc verbal = mesmo sujeito ][reset]

Verbo IR - irregular: Como verbo auxiliar + gerúndio de verbo principal indicando:
		
	[blue]Ação duradoura:[reset] O professor [yellow]ia entrando[reset] devagar. [red][ idéia de ação demorada ][reset]

    O verbo IR no presente do indicativo 'VOU' + verbo principal no infinitivo indica intenção firme ou certeza de futuro próximo.

   	[yellow]Vou encerrar[reset] a reunião - Sentido é um futuro próximo, ok. Porém é uso impróprio, informal. Equivale ao futuro do presente. Não perde sentido.
       
   	[bg_yellow]O uso formal é : Encerrarei a reunião - O verbo no tempo futuro do presente do indicativo.[reset]
       
    Verbo irregular auxiliar VIR + gerúndio, indica: ação gradual -> Ex: [yellow]Venho estudando[reset] este fenômeno há tempo.\n
                	[blue]ideia gradual, aos poucos...[reset]

    Verbo irregular auxiliar VIR + gerúndio, duração rumo a nossa época ou lugar: 
    
            Ex: Os alunos [yellow]vinham chegando[reset] quando o sinal tocou.

    Verbo irregular auxiliar VIR + infinitivo: sentido de resultado final:
     
         [yellow]Viemos a descobrir[reset] o culpado mais tarde.

		    [blue]ideia de resultado mais tarde	[reset]


            [bg_yellow]Atenção! IMPORTANTE![reset]

	Possuem o mesmo sentido 'ele tem estudado' ou 'ele vem estudando.' <- [red]sentido de ação iniciada e prolongada[reset]

	Verbo auxiliar VIR flexionado + infinitivo = sentido de resultado final:
     
                [yellow]Viemos a descobrir[reset] o culpado mais tarde.

    		Ele [yellow]vem[reset] estudando.

        	Ele [yellow]tem[reset] estudado.

	Traduz o mesmo sentido utilizar 'vem' ou 'tem'. Qual seria o sentido? Um sentido de ação iniciada e prolongada.
                

                Verbo ANDAR flexionado + gerúndio : sentido de duração, continuidade: 
		
                		Ando estudando muito.

		                Ele anda escrevendo livros.'''

    def verbos_dois(self):
        return '''Verbos conforme a flexão: regular, irregular, defectivo e abundante.

[red]Regular[reset]: o radical e as terminações do padrão de cada conjugação não mudam letra e som. Pode até mudar a letra, mas o som permanece. agir=ajo, agirei.
		
	ficar=fico, fiquei, ficarei, tecer=teço, teci, tecerei.

[red]Irregular[reset]: radical e terminações como letra e som mudam. fazer / faço / fiz / farei

	Fazer é capaz de substituir outro verbo na sequência de frases. 
	
		Veja: Gostaríamos de [yellow]reverter[reset] o quadro do país como [yellow]fez[reset] o governo anterior.


        			[bg_green] O verb 'fez' é vicário. Pode substituir outro verbo na sequência. [reset]

        Prova ESA - Exército

São exemplos de verbos irregulares, exceto:

a. Nós pedimos uma pizza.
b. Restrinjo a passagem de alunos por aqui a partir de hoje.
c. Quando tinha três anos, já media um metro.
d. Todos os anos, ela me dava um presente.
e. Minha mãe faz bolos deliciosos.

[red]Lembrando que o verbo regular pode mudar a letra mas o som não.[reset]

[red]a.[reset] Nós [yellow]pedimos[reset] uma pizza.

[yellow]PEDIR[reset] ->	[blue]Eu peço - presente do indicativo[reset] -> [red]radical e som diferente.[reset]

    [bg_red]Portanto o verbo 'pedir' é irregular.[reset] A questão está pedindo a exceção.

b. [yellow]Restrinjo[reset] a passagem de alunos por aqui a partir de hoje.

[yellow]RESTRINGIR[reset] ->   [blue]Eu restrinjo - Presente do indicativo [reset]- [red] Muda a letra , porém o som é o mesmo.[reset]

                [bg_green] VERBO REGULAR [CORRETO] [reset]

                    [bg_yellow] Repare que mesmo mudando a letra 'G' para 'J' o verbo continua REGULAR, ATENÇÃO! [reset]

[red]c.[reset] Quando tinha três anos, já [yellow]media[reset] um metro.

[yellow]MEDIR[reset] -> [blue]Eu meço[reset] -[green] Presente do indicativo[reset] - [red]Muda a letra e som - Verbo Irregular[reset]

[red]d.[reset] Todos os anos, ela me [yellow]dava[reset] um presente.

[yellow]DAR[reset] ->[blue] Eu dou[reset] -[yellow] Presente do indicativo [reset]->[red] Desinência e som diferente -> Verbo irregular[reset]

[red]e.[reset] Minha mãe [yellow]faz[reset] bolos deliciosos.
	
[yellow]FAZER[reset] -> [blue]Eu faço[reset] -[green] Presente do indicativo[reset] -> [red]Desinência e som diferente -> Verbo irregular[reset]

[red]VERBO DEFECTIVO: [reset]

	[bg_red]não possui certas formas, em razão de eufonia ou homofonia.[reset]\n
Existem 3 grupos de verbos defectivos:

[red]Verbo defectivo impessoal e unipessoal [reset]-> [blue] conjugado somente na terceira pessoa do discurso. [reset]
	[bg_yellow]Indicam fenômenos da natureza, vozes de animais, ruídos e não admitem certas pessoas. Ex: Chover, zurrar, zunir[reset]

[green]Verbo é defectivo quando não se conjuga na primeira pessoa do singular no presente do indicativo: [reset] abolir, jungir, puir, soer, demolir, explodir, colorir

	puir = desgastar uma superfície física
	soer = ter o costume / tu sóis

[bg_red]Verbos defectivos = não existem algumas pessoas do discurso no presente.[reset]
			adequar -> só tem nós/vós ->
			doer -> não tem 1º pessoa <-

	[bg_red] ATENÇÃO! Os VERBOS DEFECTIVOS SEMPRE APRESENTAM PROBLEMA PARA CONJUGAR NA 1º PESSOA DO DISCURSO NO TEMPO PRESENTE [reset]

    [red]VERBO ABUNDANTE:[reset]

[red]Verbo abundante [reset] -> possuem mais de uma forma correta na sua conjugação:

	[yellow]ele diz ou ele dize [reset] / [green]ele faz ou ele faze[reset] / [blue]ele requer ou ele requere[reset] / 

	[yellow]tu destruis ou tu destróis[reset] / [green]tu construis ou tu constróis[reset]

	[blue]nós hemos ou nós havemos.[reset]

    [red]Verbos abundantes com duplo particípio: Forma regular X forma irregular[reset]

O particípio regular termina sempre com o final -ADO/-IDO

	[blue]\A regra para escrever no regular é colocar o verbo auxiliar TER ou HAVER/ <- Para combinar[reset]

			Eu [yellow]tenho[reset] imprimido livros.

Quando não usar os verbos auxiliares: forma irregular
			
			O livro foi impresso é correto e errado é: o livro foi imprimido.

           [bg_yellow] ATENÇÃO - SER / ESTAR pedem participio irregular.[reset]

[bg_red]RELAÇÕES PRINCIPAIS DOS TEMPOS VERBAIS: CORRELAÇÃO           [reset]

[red]Podemos combinar o verbo presente do indicativo com o presente do subjuntivo [reset]

            Ex: QUERO que você VENHA.

[green]verbo 'quero' no presente do indicativo [reset]/ [yellow]verbo 'venha' no presente do subjuntivo[reset]

[blue]O Futuro do presente do indicativo tem correlação com o presente do subjuntivo [reset]
[blue]O presente do subjuntivo é possível pois trata-se de uma possibilidade que pode se realizar hoje ou depois[reset]


[red]Futuro do presente do indicativo correlaciona com o presente do subjuntivo.[reset]

	Ex:  [yellow]Gabaritarei[reset], desde que [yellow]estude[reset] bem.

[blue]verbo 'gabaritarei' no futuro do presente do indicativo / 'estude' no presente do subjuntivo[reset]

[red]Futuro do presente do indicativo correlaciona com o futuro do subjuntivo.[reset]

	Ex: [yellow]Gabaritarei[reset], quando [yellow]estudar[reset] bem.

[blue]'gabaritarei' no futuro do presente do indicativo correlaciona com futuro do subjuntivo 'estudar'.[reset]

[bg_red]ATENÇÃO! 'quando' conjunção subordinativa pedi verbo no modo subjuntivo. Portanto temos um futuro no subjuntivo e não no infinitivo.[reset]

[red]Futuro do pretérito do indicativo correlaciona com pretérito imperfeito do subjuntivo:[reset]

São dois tempos e modos verbais hipotéticos:

	Gabaritaria, desde que estudasse bem.

[yellow]'gabaritaria'[reset] -> futuro do pretérito do indicativo
[yellow]'estudasse'[reset]   -> pretérito imperfeito do subjuntivo

[red]Pretérito imperfeito do indicativo correlaciona com o pretérito imperfeito do subjuntivo[reset]

	Queria que você viesse

'queria' -> Pretérito imperfeito do indicativo
'viesse' -> pretérito imperfeito do subjuntivo

[bg_red] ATENÇÃO![reset] Exemplo:	Se eu tivesse dinheiro, eu te pagava. ( informal, coloquial ) <-[bg_red] ERRADO[reset]
			
            'pagava'  -> Pretérito imperfeito do indicativo
			'tivesse' -> Pretérito imperfeito do subjuntivo

			[bg_green]Forma correta:[reset]

			Se eu tivesse dinheiro, eu te pagaria. ( formal, correta , culta ) <-[bg_green] CORRETA[reset]
			'tivesse' -> pretérito imperfeito do subjuntivo
			'pagaria' -> futuro do pretérito do indicativo

		[bg_yellow]'pagava' no seu pretérito imperfeito do indicativo teria que ser hipótese pelo contexto da frase.[reset]
					[bg_yellow]Portanto o correto seria 'pagaria' <- futuro do pretérito do indicativo.[reset]

                    
[red]O pretérito perfeito do indicativo correlaciona com o pretérito mais-que-perfeito do indicativo:[reset]


			Quando ENTREI no cinema, o filme já COMEÇARA.
			Quando ENTREI no cinema, o filme já TINHA COMEÇADO. / havia começado -> pretérito mais-que-perfeito do indicativo composto. Verbo Aux + verbo no particípio.

verbo 'entrei' -> pretérito perfeito do indicativo
verbo 'começara' -> pretérito mais-que-perfeito do indicativo simples
verbo auxiliar TER/HAVER flexionado + verbo principal no particípio -> tinha/havia começado

[bg_yellow]A ideia do pretérito mais-que-perfeito é de falar do passado antes/ anterior de outro dentro da frase.[reset]

VUNESP/SP

Assinale a alternativa em que a frase apresenta corretamente a correlação verbal.

a. Se Dolores tornar seus dias úteis, ela recebeu seu livro.
b. Se Dolores tornara seus dias úteis, ela receberia seu livro.
c. Se Dolores tornasse seus dias úteis, ela receberá seu livro.
d. Se Dolores tornou seus dias úteis, ela receberá seu livro.
e. Se Dolores tivesse tornado seus dias úteis, ela teria recebido seu livro.

a. Se Dolores [yellow]tornar[reset] seus dias úteis, ela [yellow]recebeu[reset] seu livro.

	[bg_yellow]'se' é conjunção subordinativa adverbial condicional e o verbo 'tornar' está no futuro do subjuntivo e não no infinitivo.[reset]
		[bg_red]Lembrando que o verbo no infinitivo não tem antecedente uma conjunção.[reset]
	[bg_red]'recebeu' está no passado, no pretérito. O futuro do subjuntivo correlaciona com o futuro do presente.[reset]

			Se Dolores [yellow]tornar[reset] seus dias úteis, ela [yellow]receberá[reset] seu livro.

			[blue]Combinação possível [reset]: [red]'tornar' -> futuro do subjuntivo / 'receberá' -> futuro do presente[reset]

b. Se Dolores tornara seus dias úteis, ela receberia seu livro.

	'tornara'    => pretérito mais-que-perfeito do indicativo: é um fato concreto no passado.
	'receberia'  -> futuro do pretérito (hipótese)

[red]Como 'tornara' é um fato concreto no passado e não hipótese, não há correlação verbal na frase. Precisa de algo hipotético.[reset]

[red]O correto seria [reset][yellow]'se Dolores tornasse...'[reset] <- [blue]pretérito imperfeito do subjuntivo.[reset]

	'tornasse'  -> pretérito imperfeito do subjuntivo
	'receberia' -> futuro do pretérito

c. Se Dolores tornasse seus dias úteis, ela receberá seu livro.

	'tornasse' <- Pretérito imperfeito do subjuntivo
	'receberá' <- Futuro do presente do indicativo

Estamos falando agora no sentido hipotético 'Se Dolores tornasse...', portanto 'receberá' está incorreto, por trazer ideia de certeza.
					O correto seria 'receberia' no passado.
    
	'tornasse'  <- pretérito imperfeito do subjuntivo
	'receberia' <- futuro do pretérito

d. Se Dolores tornou seus dias úteis, ela receberá seu livro.

	'tornou'     <- fato concreto no passado
	'receberá'   <- não traz sentido hipotético , e sim certeza. Portanto teria que ser algo hipotético.
	'receberia'  <- passado / futuro do pretérito

O correto seria 'tornasse' no passado hipotético para colocar 'receberia'

e. Se Dolores tivesse tornado seus dias úteis, ela teria recebido seu livro. [bg_green][CORRETO][reset]

	'tivesse' -> forma hipotética pretérito imperfeito do subjuntivo
	'teria'   -> futuro do pretérito

	[bg_yellow]Combinando as formas hipotéticas dos dois verbos de forma correta.[reset]

[Correlacionado as formas hipotéticos do tempo e modo verbal]


FCC- SEDUC-ES

É adequada a correlação entre os tempos e modos verbais na seguinte frase:

a. Caso algumas alunas do colégios se insurjam contra a pedagogia adotada, teriam sido advertidas ou expulsas.
b. Não fossem úteis para a vida das mulheres os ensinamentos da escola, as alunas haverão de se insurgir contra elas.
c. As moças de hoje haverão de achar risíveis os valores da pedagogia conservadora que se impunha às alunas daquela época.
d. A expectativa que as moças de hoje têm em relação ao seu futuro não teria sido a mesma das que estudavam antigamente.
e. É possível que, para um estudante de hoje, o termo 'educadora' não faz sentido, em função dos valores que regessem os hábitos atuais.


a. Caso algumas alunas do colégios se [yellow]insurjam[reset] contra a pedagogia adotada, [yellow]teriam[reset] sido advertidas ou expulsas.

	[yellow]'insurjam'[reset] -> Presente do subjuntivo -> [red]Projeta a possibilidade atual ou futura. Não pode usar o presente do subjuntivo para hipótese passada.[reset]
	[yellow]'teriam'[reset]   -> Futuro do pretérito -> [red]Hipótese no futuro [reset]

[blue]O correto seria 'terão' - futuro do presente do indicativo para correlação com o presente do subjuntivo.[reset]

	Quando nós [yellow]voltarmos[reset] ele já [yellow]terá[reset] feito a tarefa.

	'voltarmos' -> presente do subjuntivo
	'terá' -> futuro do presente do indicativo

b. Não [yellow]fossem[reset] úteis para a vida das mulheres os ensinamentos da escola, as alunas [yellow]haverão[reset] de se insurgir contra elas.

	[yellow]'fossem'[reset]  -> [blue]pretérito imperfeito do subjuntivo[reset]
	[yellow]'haverão'[reset] -> [blue]futuro do presente.[reset]

[red]O futuro do presente não há hipótese e sim certeza de um fato que irá ocorrer no futuro.[reset]

[bg_red]Não há correlação verbal. Não pode ter uma correlação do pret. imper. do sub com futuro do presente. [reset]

[blue]A associação deveria ser com 'haveriam' futuro do pretérito. Forma hipotética em relação ao passado.[reset]

	'... as alunas [yellow]haveriam[reset] de se insurgir contra elas.'

c. As moças de hoje [yellow]haverão[reset] de achar risíveis os valores da pedagogia conservadora que se [yellow]impunha[reset] às alunas daquela época.

	[yellow]'haverão'[reset] -> [blue]futuro do presente. [reset] Fato posterior que irá acontecer após o presente.
	[yellow]'impunha'[reset] -> [blue]pretérito imperfeito do indicativo [reset]-> hábito no passado.

[bg_green]Questão CORRETA.	[reset]

d. A expectativa que as moças de hoje têm em relação ao seu futuro não teria sido a mesma das que estudavam antigamente.

	'têm'   -> futuro do presente
	'teria' -> futuro do pretérito
	[yellow]'será'[reset]  -> [blue]futuro do presente do indicativo em correlação ao futuro do presente do indicativo 'têm'[reset]

[bg_yellow]Se é uma expectativa de hoje em relação ao futuro. O correto seria '...não será a mesma...'[reset]

[bg_red]ERRADO. O correto seria 'será'.[reset]


e. É possível [yellow]que[reset], para um estudante de hoje, o termo 'educadora' não [yellow]faz[reset] sentido, em função dos valores que [yellow]regessem[reset] os hábitos atuais.

	[blue]A conjunção subordinativa 'que' vai pedir presente do subjuntivo. [reset]

	O correto seria 'faça'. Presente do subjuntivo ' que eu faça '.

		[bg_yellow]'faz' é presente do indicativo.[reset]

	[green]É algo hipotético, um futuro hipotético, portanto é presente do subjuntivo e não um fato que ocorrerá no futuro, certeza.[reset]
	
	[yellow]'faça'[reset] -> [blue]Pela conjunção deverá ser por regra 'que eu faça'[reset] -> [red]Presente do subjuntivo.[reset]

	[yellow]'regessem'[reset] - [bg_red]ERRADO[reset] - Pretérito imperfeito do subjuntivo. Mesmo sendo um Passado hipotético. Esse tempo fica no passado.
                        [bg_yellow] é um hábito passado que vem ao futuro.[reset]

	[yellow]'regiam'[reset] - [blue]Hábito atuais no passado.[reset] -> [green]Futuro do pretérito [reset]<- [blue]com hipóteses de futuro[reset]
	[yellow]'regem'[reset]  - [blue]Hábitos anteriores que irão ocorrer atuais[reset] - [green]Futuro do presente - hábitos[reset]'''

    def vozes_verbais(self):
        return '''Vozes Verbais:

Verbos que indicam ação admitem voz ativa, voz passiva e voz reflexiva.
    Existem verbos que não indicam ação. Verbo ESTAR por exemplo.
        Verbo chover -> não indica ação. Não admitem vozes.

                    A voz verbal consiste em uma atitude do sujeito em relação à ação do verbo.
                        O sujeito não precisa ser o praticante da ação, é o assunto da oração.

    [red]A voz ativa[reset]: o sujeito só pratica a ação.
     
             Ex: O governo aumentou os juros.
	Para identificar o sujeito temos: o que ou quem é que aumentou? [blue]o governo[reset] <-[red] sujeito.[reset] Assunto da oração e atitude dele.

    [yellow]A voz passiva[reset]: [blue]o sujeito só recebe ação.[reset]
     
         Ex: Os juros foram aumentados pelo governo. 
         
            o que é que foi aumentado? [blue]os juros[reset] <- [red]Sujeito que recebe a ação, voz passiva.[reset]
	        'foram' do verbo flexionado SER.

[bg_yellow]O sujeito inicia sem PREPOSIÇÃO.[reset]

 [bg_red] ['... PELO GOVERNO.' pelo = preposição 'por' + artigo 'o', portanto não pode ser sujeito.][reset]
[bg_yellow]O sujeito que pratica ação não pode ser iniciado por preposição.[reset]

[bg_red]O sujeito inicia sem PREPOSIÇÃO. [reset] '... PELO GOVERNO.' -> pelo = preposição 'por' + artigo 'o', portanto não pode ser sujeito.

[bg_red]O sujeito que pratica ação não pode ser iniciado por preposição.[reset]

Existem duas formas de escrever na voz passiva...

[red]a.[reset] Passiva analítica: [green]com verbo SER ( passiva de ação ) ou ESTAR ( passiva de estado )[reset]

Exemplos:

	Os juros [yellow]foram (SER)[reset] aumentados pelo governo. 
	O ladrão [yellow]foi[reset] preso pelos guardas. ( SER )
	O ladrão está preso. ( ESTAR )

[bg_yellow]\ Verbo SER flexionado + verbo no particípio = voz passiva analítica /[reset]

[bg_red]      REPARE:[reset]
	O agente da voz passiva ( pelo governo, pelos guardas ) indica o ser que pratica a ação sofrida pelo sujeito sempre com preposição 'por' ou 'de'.  
		            
                        Ele é querido [yellow]de[reset] todos. ( Ele é querido [yellow]por[reset] todos )

                        'de todos' -> agente da voz passiva
                        'por todos' -> agente da voz passiva

A voz passiva analítica pode formar uma locução de 3 verbos: 

	Temos sido amados. <- 3 verbos <- Locução verbal <- verbo ser flexionado + verbo no particípio

	Tenho sido amado.  <- 3 verbos <- Locução verbal <- verbo ser flexionado + verbo no particípio

	Estou sendo amado. <- 3 verbos <- Locução verbal <- verbo ser flexionado + verbo no particípio

[bg_red]Deve ter o verbo SER flexionado + verbo no participio.[reset]

[bg_yellow]VOZ REFLEXIVA:[reset]

    Voz reflexiva: o sujeito pratica e recebe ação. Ocorre quando houver pronome pessoal obliquo reflexivo ( me, te, se, nos, vos)

	    Eu me lavei. 'me lavei' -> voz reflexiva - ação de lavar recai para o próprio sujeito, eu.
         
            O sujeito 'eu' agente/paciente pratica e recebe a ação. Pronome + verbo
		
	    Ele se feriu com facas. -> 'se feriu' -> voz reflexiva recaida para o sujeito do assunto.
         
             O sujeito 'ele' pratica e recebe a ação. Pronome + verbo 


A voz reflexiva pode ter dois sentidos:

	[blue]Voz reflexiva simples ( ação recai para si mesmo )[reset]
		
	João se penteou

	Eu me machuquei

	[blue]Voz reflexiva recíproca:[reset]  (um ao outro) necessariamente no plural para fazer a ação uma sobre a outra.
	
	Os filhos se abraçaram. ( um ao outro )

	Nós nos cumprimentamos. ( um ao outro )

Voz passiva sintética:

	* Verbo de ação não pede preposição. o 'se' da frase é uma particula apassivadora apresentada dentro da voz passiva sintética.
	
	'se' pronome pessoal obliquo apassivador

[bg_yellow]Tudo que é analítico é dividido. Terá divisão de 2 ou 3 verbos. / A sintética é uma forma de resumir.[reset]


        		O material orgânico [yellow]se decompõe[reset] no lixo.


                	    'o material orgânico' é o sujeito paciente - assunto -
                        Sujeito + se ( partícula apassivadora )
                        o material se 'decompoe' - 1 verbo - sintética
	                    O 'se' é partícula apassivadora própria da agente da passiva sintética.

                O material orgânico [yellow]é decomposto[reset] no lixo.

                    		[red]ele 'é decomposto' - 2 verbos ( 'SER' + 'DECOMPOR' )- Voz passiva analítica[reset]

[bg_yellow]TRANSFORMAÇÃO ENTRE VOZ ATIVA E VOZ PASSIVA ANALÍTICA.[reset]                            


[yellow]Quando o sujeito agente é encontrado da esquerda pra direita na frase, está na voz ativa.[reset]

		O Brasil [yellow]sediou[reset] a Copa.
 
	'O Brasil' -> sujeito agente, voz ativa
	'sediou'   -> verbo flexionado
	'complemento verbal': Objeto Direto, Objetoo Indireto ou Predicativo

   		A Copa [yellow]foi sediada[reset] pelo Brasil

'a copa' -> sujeito paciente , é o assunto. A copa foi, sofre a ação.
'foi sediada' -> ser + particípio
'pelo Brasil' -> agente da passiva

[yellow] Quando o sujeito PACIENTE é encontrado da esquerda pra direita na frase, está na voz passiva. [reset]

A transformação correta para voz passiva -> 1 verbo vira 2 verbos
2 verbos na voz ativa para a passiva 3 verbos.

        O Brasil sediaria a Copa

        'o brasil'  -> Sujeito agente, voz ativa.
        ' sediaria' -> verbo flexionado
        ' a copa'   -> Objeto direto 

        O verbo "sediar" é um verbo transitivo direto, o que significa que ele não requer preposição para completar seu sentido.

A expressão "a Copa" responde à pergunta "O Brasil sediaria o quê?" – o que indica que ela está recebendo diretamente a ação do verbo.

Para voz passiva:

        A copa seria sediada no Brasil.

        'seria'  -> verbo flexionada no mesmo tempo que a voz ativa + verbo no particípio
        'a copa' -> sujeito paciente e objeto direto
        'no Brasil' -> Adjunto Adverbial de lugar 

Voz ativa:

        O Brasil sediava a copa. ( 'o brasil' -> sujeito agente - voz ativa // 'sediava' -> pretérito imperfeito do sub // 'a copa' -> ob. dir.

Voz passiva:

Manter o modo e tempo verbal do verbo principal da frase para o verbo SER 'ERA' + participio do verbo principal

        A copa [yellow]era sediada[reset] no Brasil.

Voz ativa:

		O Brasil [yellow]sediara[reset] a Copa. 

        Para transformação correta de voz ativa para passiva analítica.

	        'O Brasil' <- sujeito paciente, voz ativa
	        'sediara' -> Pretérito mais-que-perfeito do indicativo
	        'a copa' -> agente da passiva. Objeto Direto

Acrescentar o verbo 'ser' no mesmo modo e tempo verbal da frase na voz ativa ( pret. mais-que-perf. ind. ) + particípio para voz passiva:

		A copa [yellow]fora sediada[reset] pelo Brasil -> [blue]Verbo SER flexionado para o pretérito imperfeito do indicativo - 'FORA' + particípio[reset]

	Outro exemplo:

		O Brasil [yellow]sediará[reset] a copa.

		'o Brasil' -> Sujeito paciente
		'sediará'  -> futuro do presente
		'a copa'   -> agente da passiva

Para transformar para voz passiva analítica temos:

		A Copa [yellow]será sediada[reset] no Brasil -> [blue]o verbo SER obrigatório e flexionado no mesmo tempo e moodo verbal da voz ativa: 'será' -> futuro do presente + part[reset]

A transformação correta da voz ativa para voz passsiva -> 1 verbo vira 2 verbos
Caso tenha 2 verbos na voz ativa para transformar para a voz passiva serão 3 verbos.

Outros tempos verbais:

        Voz ativa:

		Se o Brasil [yellow]sediasse[reset] a copa. 

		'sediasse' -> pretérito imperfeito do subjuntivo.
		Verbo SER flexionado no mesmo modo e tempo: pret. imperf. subj + verbo no participio para transformação da voz ativa para passiva analítica.
        'o Brasil' -> sujeito paciente

        Voz passiva:

		A copa [yellow]fosse sediada[reset] pelo Brasil. -> 

		'fosse sediada' = 'fosse' -> Pretérito imperfeito do subjuntivo + participio do verbo principal.

	Outro exemplo:

		Se o Brasil [yellow]sedie[reset] a copa. -> 

		'sedie' -> Presente do subjuntivo
		Colocar o verbo SER no subjuntivo do presente + verbo principal no particípio:
        'o Brasil' -> sujeito paciente

        Voz passiva:

		A copa [yellow]seja sediada[reset] pelo Brasil. -> 

		'seja sediada' => Verboo 'SER' no presente do subjuntivo + verbo principal no participio 'sediada'

        [bg_red]Se temos 1 verbo na voz ativa vira 2 na voz passiva. REGRA DE TRANSFORMAÇÃO![reset]
        [bg_red]Se temos 2 verbos na voz ativa vira 3 na voz passiva. REGRA DE TRANSFORMAÇÃO![reset]


   		O Brasil 'ia sediar' a copa. <- Voz ativa / A copa 'ia ser sediada' pelo Brasil <- Voz passiva analítica.

    	Exemplo de 3 verbos na voz ativa:

		O Brasil deve estar sediando a copa. [red]'deve estar sediando'[reset] - [bg_yellow]locução verbal na voz ativa[reset]

        Para voz passiva:

	    [green]Flexionar o verbo SER no mesmo tempo do verbo principal da voz ativa -> sediando.../...sendo + participio do verbo principal para voz passiva analítica.[reset]

		A copa [yellow]'deve estar sendo sediada'[reset] no Brasil.

            [bg_red]Se na voz ativa tinha 3 verbos, para transformar em voz passiva será verbos.  [reset]

        Outro exemplo:

            Voz ativa:

		O Brasil [yellow]está sediando[reset] a copa.
         
           [yellow]'está sediando'[reset] <- Locução verbal 2 verbos ( Haver ( verbo auxiliar ) + verbo principal no gerúndio )\n

           Para transformar em voz passiva:
	
		A copa [yellow]está sendo sediada[reset] no Brasil. <- [yellow]'está sendo sediada'[reset] - Colocar o VERBO SER flexionado no gerúndio do verbo principal + particípio do verbo principal.
		    3 verbos - Locução Verbal           

        '''
    def ortografia(self):
        return '''Ortografia - Marcio Wesley

Emprego das letras 


Emprego do S:

	Após ditongos: Sousa, maisena, mausoléu, faisão

s[yellow]ou[reset]sa -> identificado o ditongo, encontro de vogais: s[yellow]ou[reset] - za // [blue]emprego do S[reset]

mai-se-na -> identificado o ditongo, encontro de vogais na separação silábica : m[yellow]ai[reset]-se-na // [blue]emprego do S[reset]

Adjetivos terminados com sufixo '-OSO / -OSA': gost[yellow]oso[reset], prazer[yellow]oso[reset], ansi[yellow]oso[reset] <- [blue]emprego do S[reset]

	Palavras com sufixos '-ES/-ESA/-ISA':  ( quando estamos falando de origem, nacionalidade, títulos)
	
		Baron[yellow]esa[reset], [blue] Emprego do S[reset]\n

		Portugu[yellow]esa[reset], [blue] Emprego do S [reset]\n
 
		Sacerdot[yellow]isa[reset], [blue] Emprego do S [reset]\n

   	Palavras com prefixo TRANS: Utiliza-se a letra 'S'

		transatlântico
		intransigente
		transcendente

   	Em substantivo NÃO DERIVADO DE ADJETIVO:

		defesa ( do verbo defender )
		
	Os derivadores dos verbos 'pôr' e 'querer':

		eu não quis, 
		se ele quisesse,
		se eu puser

	Nos sufixos gregos, terminações '-ESE / -ISE / -OSE' : todos com o emprego da letra 'S'

		hemodiálise
		virose
		meiose
		mitose

	[bg_red] ATENÇÃO! [reset]

		[bg_yellow]Quando a palavra primitiva já tem 's' mantem o 'S':[reset]

			atrás - atrasado
			paralisia - paralisar


            	[bg_red] Exceções! [reset]

		[bg_yellow] catequese -> catequizar [reset]
		[bg_yellow] batismo   -> batizar[reset]
		[bg_yellow] síntese   -> sintetizar[reset]

            	[bg_red] Palavras terminadas com 'ismo' é utilizado a letra 'Z' [reset]


   	Sufixos diminutivos : 'inho' / 'inha' / 'ito' / 'ita' emprega-se a letra 'S':
	
    	luis = luisinho / inglês = inglesinho / pires = piresinho


[bg_yellow] Verbos com final 'dir'/'ender' formam substantivos com 's':[reset]
		
        Verbo -----  Subs           verbo --------- subs
		dividir -   divisão     //	colidir -     colisão
		aludir -    alusão      //	rescindir -   rescisão
		defender -  defesa      //	compreender - compreensão
		suspender - suspensão   // 	empreender -  empreensão

        
    Emprego da letra 'Z':

    	Sufixos '-EZ / -EZA' em substantivo formado a partir de adjetivo:

	        	belo - beleza

                'belo' - Substantivo // 'beleza' - escrito com 'Z' pois é um adjetivo derivado de um substantivo.

		        gentil - gentileza

                'gentil' - substantivo // 'gentileza' - escrito com 'z' pois é um adjetivo derivado do substantivo.

		        mesquinho - mesquinheza
	
                'mesquinho' - substantivo // 'mesquinheza' - escrito com 'z' pois é um adjetivo derivado do substantivo.

	Sufixo diminutivo '-INHA/-INHO' conserva a letra 'z' da palavra original:

		raiz - raizinha // cruz - cruzinha // juiz - juizinho

Se a palavra original não tiver 's' acrescentamos o diminutivo com 'z' = 'zinho'/'zinha':

		mãe - mãezinha // pé - pezinho // flor - florzinha

        Emprego da letra 'G':

	Terminações '-AGEM / -IGEM / -UGEM ': 

		margem, vertigem, fuligem, garagem, origem

		[bg_red] ALERTA! [reset]
	
		[bg_yellow] Palavras de origem indígena podem ser escritas com 'J'. = pajem, pajé, lambujem.[reset]

	Terminações 'ágio'/'égio'/'ígio'/'ógio'/'úgio'/'ege'/-oge':

			pedágio, relógio, egrégio, litígio, refúgio, herege, doge

			[bg_green] Todos com o emprego da letra 'G' [reset]

	Verbos terminados com '-GER'/-GIR': corrigir, viger, fingir, fugir

	[bg_red] ALERTA! [reset]

		[bg_red] Substantivo é 'a viagem', mas o verbo é 'que eles viajem' tem que ser com o 'J'. Em todas as conjugações do verbo [reset]

Emprego do 'J':

	Palavras com origem indígena: jenipapo, pajé, jerimum

		Exceção: Mogi-mirim // Mogi das Cruzes // Sergipe.

			São de origens indígenas mas permanecem com 'G'.

	Palavras de origem árabe: alforge, 

	Terminação '-AJE' sempre com 'J': ultraje, laje

	Conservar a letra 'j' quando a palavra é original:

		laranja - laranjada - laranjinha - laranjeira
		
		loja - lojinha - lojista
		
		granja - granjear 
		
		granjeiro - granjinha

Emprego do 'CH': após '-re-'

	Manter a palavra derivada de outra já com 'ch' 

			 charco - encharcar
		
                	chouriço - enchouriçar
		
			cheio - encher - enchimento

			enchova - enchovinha


Emprego do X:

	Som de 'z' em palavras com prefixo '-ex' seguido de vogal: 

		[yellow]exa[reset]me, [yellow]exu[reset]ltar, [yellow]exe[reset]cutar	// emprega-se o X

	Som de 'SS' entre vogais: 'trouxe', 'próximo', 'sintaxe' // emprega-se o X

	Som de 'CH' no início ou interior de palavras: xícara, xarope, luxo, ameixa // emprega-se o X

	Som de 'KS' no meio ou final: fixo, táxi, conexão, tórax...

	Palavras de origem árabe: xadrez, oxalá, enxaqueca...

	Palavras de formação popular, africana ou indígena:

		xepa, xereta, xingar, abacaxi, muxoxo, xodó, xiquexique ( ou xique-xique )

	Após a sílaba inicial 'EN-': 

		enxada, enxergar, enxaqueca, enxó, enxertar, enxurrada, enxofre, enxuto

	Após ditongo: encontro de vogais e semivogais na mesma sílaba

		ameixa, caixa, peixe, frouxo, feixe, deixar, baixa, rouxinol

	amei - xa // pei  - xe // frou - xo // fei  - xe // dei  - xar // bai  - xa // rou  - xi - nol

		Exceção: chutar - cauchutar - recauchutar ( palavra original 'chutar' )      '''  

    def porques (self):
        return '''POR QUE / POR QUÊ /  PORQUE / PORQUÊ
        
        	POR QUE:
			Usado para início de período em perguntas e afirmações.

            	[yellow]Por que[reset] você fez isso?

	[yellow] Por que [reset] construí Brasília.

	[yellow] Por que [reset] Adriana acha que é melhor do que Henrique.?

			Usado também para período composto ( pelo qual / pela qual / pelos quais / pelas quais )

			Ex: Este é o caminho [yellow]por que[reset] passaram.

			Esta é a resposta [yellow]por que[reset] aguardava

			[bg_yellow]Sentido de 'por qual motivo'?[reset]

			Não se sabe [yellow]por que[reset] chove tanto, naquela região do país.

			Mas [yellow]por que[reset] você não apareceu mais lá em casa?
	
			Ninguém sabia [yellow]por que[reset] ela foi embora.

			Deve existir uma razão [yellow]por que[reset] os juros caíram tanto.	

			Lembre-se bem dos fatos [yellow] por que[reset] você já passou.

            
            POR QUÊ:

		    Usado no final do período composto ou simples em perguntas e afirmações. Também no sentido de 'por qual motivo' usado no final da oração....


            			Você fez isso [yellow]por quê[reset]

			Susana agiu assim e não sabe [yellow]por quê[reset]
		
		[bg_yellow] O por quê separado e acentuado usa-se também antes de sinais de pontuação.[reset]

			Mas você não apareceu mais lá em casa [yellow]por quê?[reset]

			Ninguém sabia [yellow]por quê[reset] , mas o fato é que ela foi embora.
		
			[blue]Final de oração pode ser:[reset]

					[blue]Ponto e vírgula ( ; )[reset]
					[blue]vírgula ( , )[reset]
					[blue]dois pontos ( : )[reset]
					[blue]interrogação ( ? )[reset]
					[blue]ponto final ( . )[reset]

            PORQUE:

		    Sentido de explicação ou respostas, podendo ser substituido por 'pois'.

		        Por que parou? [yellow] Porque [reset] estou cansado . <- Resposta

		        Raquel não veio à faculdade, [yellow]porque[reset]está doente. <- Explicação

		        Eu canto [yellow] porque [reset] o istante existe e a minha vida está completa.

		        Ele não veio ontem [yellow] porque [reset] estava doente ou [yellow] porque [reset] teve alguma emergência?

			    [bg_red] ALERTA! [reset]

			        [red]Podemos substituir por 'pois' mesmo sendo uma oração composta com pergunta.[reset]

		            Ele não veio ontem [red] pois [reset] estava doente ou [red] porque [reset] teve alguma emergência?

            PORQUÊ:

    		O 'porquê' junto e com acento significa que exige diretamente antes dele um artigo, numeral, adjetivo ou pronomes masculinos.


	        	Nem sempre existe [blue]um[reset] [yellow]porquê[reset] para tudo. <- [green]'um' = numeral[reset]
	
		        Não sei [blue]o[reset] [yellow]porquê[reset] disto. <- [green]'o' <- artigo[reset]

		        Ela me deu um [blue]belo[reset] [yellow]porquê[reset] <- [green]'belo' -> adjetivo[reset]

		        Ofereceram [blue]três[reset] [yellow]porquês[reset] para o problema. <- [green]'três' = numeral[reset]

		        [blue]Este[reset] [yellow]porquê[reset] não serve. <- [green]'este' = pronome[reset]
		
		        Essa vida sem você não tem [yellow]porquê[reset] -> [blue]função sintática de objeto direto como substantivo nuclear[reset]

			        [bg_red]Obs: 'tem' é verbo transitivo direto que necessita de um objeto direto 'porquê'.[reset]'''        

    def estrutura (self):
        return '''Estrutura das palavras:

Partes que formam as palavras...

[red]Radical[reset] ->  'Barc' + vogal temática 'o' -> 'Barc + o' : [blue]Barco[reset]

[red]Vogal temática[reset] -> final da palavra. [red]Não indica gênero.[reset]\n
[blue]A desinência nominal que indica gênero da mesma espécie.[reset]

[red]Tema[reset] -> União do radical + vogal temática

Ex: 	Barc + vogal temática 'o'  = [blue]tema[reset] 'barco'
	    Port/ + vogal temática 'a' = [blue] tema [reset] 'porta'

        Em verbos?

            	Sonhar

                [red]Radical[reset]: [blue]sonh[reset]
                [red]Vogal temática[reset]: [blue]a[reset]
                [red]Desinência verbal do infinitivo[reset]: [blue]r[reset]

[red]Afixos[reset]: antes e depois do radical ou seja, prefixos e sufixos.\n
[bg_red]Infixos são vogais e consoantes de ligação dentro no meio da palavra.[reset]

Ex:
		gás + metro = gas[yellow]ô[reset]metro => [blue]vogal de ligação infixo[reset]

Outro exemplo de consoante de ligação:

		pau + ada = pau[yellow]l[reset]ada => [blue]consoante de ligação[reset]

DESINÊNCIAS:

	[red]Desinência verbal[reset]: SONHA [yellow]'-R'[reset]

	[red]Desinência nominal[reset]: CACHORR [yellow]'-O'[reset]


    [bg_red] ATENÇÃO! [reset]

    	Radical pode ser primário ou secundário. A raiz não pode ser decomposta. A origem mais antiga.


            		'gelar' => radical > 'gel' -> radical primário.

        	Agora:
		            'desgelar' => radical 'desgel' -> radical secundário.

               		[bg_yellow] Um radical secundário ainda pode ser decomposto porque podem conter afixos.[reset]
					[bg_red] Que no caso tem um prefixo 'des' [reset]

Palavras cognatas compartilham a mesma raiz:

            Cognatas são palavras de idiomas diferentes que têm a mesma origem, grafia semelhante e o mesmo significado. 
            Esse fenômeno idiomático acontece porque as palavras têm a mesma raiz e pertencem à mesma família etimológica.

	            pedra, pedregulho, apedrejar, pedrinha, pedreiro

	            flor, florescer, inflorescência, florido

            				VOGAL TEMÁTICA X DESINÊNCIA


        [red]Desinência[reset] = após o radical , indica gênero. (masculino/feminino)\n
        [red]Vogal temática[reset] = apenas se junta ao radical e forma a palavra.

        menin[yellow]o[reset] / menin[yellow]a[reset], cachorr[yellow]o[reset] / cachorr[yellow]a[reset] -> [blue]desinência de gênero:[reset] [red]o / a[reset]

        carr[yellow]o[reset] / pedr[yellow]a[reset] -> [blue]vogais temáticas:[reset] [red]o / a[reset]

        pent[yellow]e[reset] / urub[yellow]u[reset] / muric[yellow]i[reset] -> [blue]vogais temáticas:[reset] [red]e / u / i[reset]


        Tipos de desinências:

        	Desinência nominal => indica gênero (masculino/feminino) e número (singular/plural)\n
		            Ex: menin[yellow]o[reset] / menin[yellow]os[reset]

	    [red]Desinência verbal [reset] => [blue]indica a variação do verbo nos tempos e modos e nas pessoas.[reset]

            Veja:
		
	                    [yellow]Construíamos[reset]
		
	                        'constru' => [red]raiz do verbo 'construir'.[reset]
	                        'ia'  => [red]desinência verbal do pretérito imperfeito do indicativo.[reset]
	                        'mos' => [red]desinência verbal da 1º pessoal do plural.[reset] 'nós'


Vogal temática nos verbos:
	
	Logo após o radical no infinitivo:

    		Conversar => radical = convers-
			     vogal temática = a
			     desinência do infinitivo = r

	    	retroceder -> radical => retroced-
			      vogal temática => 'e'
		          desinência do infinitivo = r

Nem sempre aparece a vogal temática:

	conversei => radical = convers-
			desinência do pretérito perfeito na 1° pessoa singular: -EI

	retrocedia => radical = retroced-
			desinência do pretérito imperfeito: -IA

            Afixos -> prefixo e sufixo

	Prefixo => antes da raiz, agrega sentido.
	Sufixo  => após a raiz, agrega sentido.


Leal => Palavra original
[yellow]des[reset]leal => prefixo

Aéreo => Palavra original
[yellow]ANTI[reset]aéreo => 'anti' prefixo

Sacola => Palavra original
sacol[yellow]eiro[reset] => sufixo


INFIXOS: Vogal de ligação e consoante de ligação.

	gas[yellow]o[reset]metro => gas + 'o' + metro => vogal de ligação: 'o'

	chaleira => cha + 'L' + eira => consoante de ligação: letra 'L'

	cofeicultor => café + 'i' + cultor => vogal de ligação: 'i'

	cafeteira   => café + 't' + eira => consoante de ligação: 't'


COMPOSIÇÃO E DERIVAÇÃO NA FORMAÇÃO DE PALAVRAS:

COMPOSIÇÃO =>  dois ou mais radicais se juntam

	Veja: passatempo ( passa + tempo )

		'passa': do verbo passar
		'tempo': substantivo

		As três classes formam a Composição

		bem-te-vi

		'bem': advérbio
		'te': pronome
		'vi': verbo


A composição pode ocorrer de duas formas:


	[red]JUSTAPOSIÇÃO[reset] => Os radicais se juntam sem perder elementos.

	    Veja: passatempo, pontapé, bem-te-vi, meia-direita, espaçonave

	[red]AGLUTINAÇÃO[reset] => os radicais se juntam e perdem elementos.

	    Veja:
		    [yellow]água[reset] + ardente[reset] = [blue]aguardente[reset]  [red]( perdeu uma letra 'a' )[reset]

		    [yellow]plano + alto = [blue]planalto[reset] [red]( perdeu a letra 'o' )[reset]

		    [yellow]vossa mercê[reset]  = [red]você[reset]

		    [yellow]em + boa + hora[reset] = [blue]embora[reset] [red]( perde a letra 'a' e a letra 'h' )[reset]

		    [yellow]filho + de + algo[reset] = [blue]fidalgo[reset] [red]( perde 'lho', perdeu 'e' )[reset]


DERIVAÇÃO:

	Possui somente um radical ou perde elementos.

	[red]INesperado[reset] -> [green]prefixo[reset] -> derivação
	[red]pizzaRIA[reset]   -> [green]sufixo[reset] -> derivação
	[red]anti-inflamatório[reset] -> [green]prefixo[reset] -> derivação

DERIVAÇÃO PREFIXAL:

		-> REdefinir; TRANSatlântico; DESleal; ANTI-inflamatório.

DERIVAÇÃO SUFIXAL:
		
		-> portEIRO; suaveMENTE; lealDADE; capitalISMO

DERIVAÇÃO PREFIXAL E SUFIXAL:

		-> DESlealDADE; NEOcapitalISMO; REdefiniÇÃO.

DERIVAÇÃO PARASSINTÉTICA: ( parassíntese )=:> prefixos e sufixos obrigatórios. NÃO PODEMOS RETIRAR!

		-> SUBterraNEO; ApedreJAR; ENtardECER; AmanhECER; AcorrentAR; AterrISSAGEM.

		CUIDADO COM A DIFERENÇA ENTRE PARASSÍNTESE E DERIVAÇÃO PREFIXAL E SUFIXAL!

		DESlealDADE => prefixo e sufixo opcionais porque existe 'lealdade' e 'desleal'.

		SUBterraNEO => parassíntese:

			Não existe a palavra 'terraneo' nem 'subterra'. Então prefixo e sufixo são obrigatórios.		


[red]DERIVAÇÃO REGRESSIVA OU DEVERBAL[reset] => a partir de um verbo, forma-se o nome da ação (substantivo abstrato)
			
				[bg_yellow]Retira a vogal temático e a desinência para formar a derivação regressiva.[reset]

		[red]verbo primitivo 'CHORAR'[reset] - [yellow]'O CHORO'    <- Derivação regressiva <- SUBSTANTIVO ABSTRATO DERIVADO <- Nome da ação -> 'O choro'[reset]

		[red]verbo primitivo 'DEFENDER'[reset] - [yellow]'A DEFESA' <- Derivação regressiva <- Substantivo abstrato derivado <- Nome da ação -> 'defesa'[reset]

		[red]verbo primitivo 'COMBATER'[reset] - [yellow]'O COMBATE' <- Derivação regressiva <- Substantivo abs. derivado <- Nome da ação -> 'O combate'[reset]

		[red]verbo primitivo 'ATACAR'[reset] - [yellow]'O ataque' <- Derivação regressiva <- Substantivo abs. derivado <- Nome da ação -> 'O ataque'[reset]

	[bg_red] ATENÇÃO! [reset]

		Existe também o processo de formação de palavras tanto do substantivo primitivo como do verbo primitivo.
	Eis abaixo o processo do do substantivo primitivo para o verbo derivado:

	[red]Pedra[reset]    <- [blue]substantivo primitivo[reset]  <- [red]Apedrejar[reset]  <- [blue]verbo derivado ( parassíntese )[reset]
	[red]Corrente[reset] <- [blue]substantivo primitivo[reset]  <- [red]Acorrentar[reset] <- [blue]verbo derivado ( parassíntese )[reset]
	[red]Telefone[reset] <- [blue]substantivo primitivo[reset]  <- [red]Telefonar[reset]  <- [blue]verbo derivado ( parassíntese )[reset]

    	Eis abaixo o processo do verbo primitivo para o substantivo derivado ( abstrato, nome da ação )

	[red]Estudar[reset] <- [blue]verbo primitivo[reset] // O estudo <- [blue]susbtantivo derivado[reset] ( derivação regressiva )
	[red]Vender[reset]  <- [blue]verbo primitivo[reset] // A venda  <- [blue]substantivo derivado[reset] ( derivação regressiva )
	[red]Caçar[reset]   <- [blue]verbo primitivo[reset] // A caça   <- [blue]substantivo derivado[reset] ( derivação regressiva )


    DERIVAÇÃO IMPRÓPRIA:

	Só muda a classe da palavra sem mudar a estrutura. (escrita)

    	O livro [yellow]que[reset] ganhei foi um bom presente.

	        'que' => pronome relativo ( classe original )

	    Essa moça tem um [yelow]quê[reset] de mistério.
		
	        'quê' => substantivo ( derivação imprópria ) Palavra que possui acento monossílaba tônica, com sentido próprio. Substantivo é significativa.
	        'um'  => artigo que acompanha o substantivo.

	[yellow]Estudar[reset] e [yellow]trabalhar[reset] caminham juntos. [red]( classe original = verbos )[reset]

	[yellow]O estudar[reset] e [yellow]o trabalhar[reset] caminham juntos.  [red]( derivação imprópria = substantivos por terem o artigo acompanhando-os )[reset]

				 	DERIVAÇÃO IMPRÓPRIA x DERIVAÇÃO REGRESSIVA

        	Derivação imprópria não muda a forma da palavra. Muda somente a classe.
	        Derivação regressiva MUDA a forma da palavra.

OUTROS PROCESSOS DE FORMAÇÃO DAS PALAVRAS:

	ABREVIAÇÃO VOCABULAR É DIFERENTE DE ABREVIATURA.

    	ABREVIAÇÃO ou redução é uma redução da palavra longa para uma forma curta que passa a ser usada em seu lugar.

		MOTO  por MOTOCICLETA
		FOTO  por FOTOGRAFIA
		PNEU  por PNEUMÁTICO
		FONE  por TELEFONE
		CINE  por cinema
		REFRI por refrigerante
		QUILO por QUILOGRAMA
		REBU  por REBULIÇO

	[bg_yellow] Abreviação não tem ponto final. [reset]

	ABREVIATURA é diferente. Representa uma palavra com algumas letras:

	obs.   => observação
	ex.    => exemplo
	etc.   => et cetera ou etcétera
	Dr.    => Doutor
	V.Exa. => Vossa Excelência
	p.     => página
	i.e.   => isto é

		[bg_yellow] Abreviatura possui ponto final obrigatório [reset]	

	[bg_red] A SIGLA é abreviatura sem ponto final e sem ponto entre as letras.[reset]

	A sigla pode ser formada com iniciais e ou com partes de palavras que compõem o nome de uma instituição.
			
			ONU, OEA, BIRD, BNDES, Petrobras, FIAT, Anvisa, PCDF, Agepol

ACRÔNIMO:
		é SIGLA em forma de sílabas: ONU,

ORTOGRAFIA DAS SIGLAS:
		
		Escrever todas as letras maiúsculas quando:

		* a sigla contém até três letras;
		* quatro ou mais letras pronunciadas individualmente;
		* quando quatro ou mais letras formarem sílabas, somente a primeira letra será maiúscula;
				
				Anatel / Petrobras / Embratur / Agepol

	** Siglas com leitura mista ficam com todas maiúsculas: DNIT, HRAN

Plural de siglas e acrônimos:

	Apenas acrescente 's' minúsculo, sem apóstrofo.

Veja:

	PMs // PM's(ERRADO) // ONGs // ONG's(ERRADO)

ONOMATOPEIA => forma palavras que imitam sons.

	MIAU, TIQUE-TAQUE, PINGUE-PONGUE, TOC-TOC

Neologismo semântico e morfológico não é um processo. Esse é nome que se dá quando se cria palavra e aquele é o que cria sentido para uma palavra já existente.

	TUITAR, STALKEAR, PRINTAR, BOLSOMINION

Neologismo morfológico: cria a palavra e o sentido

	[yellow]INOBSTANTE[reset] o deferimento, os autos não foram concluidos ainda.

	'inobstante' : 'não obstante' 

	Sabe quem está [yellow]ficando[reset] com a Patrícia?

	'ficando' : 'neologismo semântico'

	Descobri uma [yellow]parada[reset] sinistra.


HIBRIDISMO: mistura elementos de línguas diferentes.

	televisão  => tele( do grego ) e visão ( do latim )

	sociologia => socio (latim) e logia (grego)

	burocracia => buro, de bureau (francês) e cracia (grego)

	sambódromo => samba (dialeto africano) e dromo (grego)
'''             

    def questoes_estrutura_porques(self):
        return '''Questões de formação de palavras:
            
            1. (IDESG-COREN-ES-Aux.Adm-2024) A palavra 'desajeitada' é formada pelo processo de:

            a. Derivação prefixal e sufixal
            b. Oneomínia
            c. Derivação regressiva
            d. Derivação imprópria
            
            A palavra 'desajeitada' é formada pelo processo de derivação tanto prefixal como sufixal.
            O prefixo : 'DES-'
            Radical : 'AJEIT-'
            O sufixo : '-ADA'
            
            Não pode ser derivação regressiva porque é um processo de redução da palavra, geralmente um verbo que se transforma
            em substantivo. E nem derivação imprópria quando ocorre uma palavra que muda de classe gramatical sem sofrer alteração
            em sua forma.
            A palavra 'desajeitada' se encaixa no processo de adição de prefixo e sufixo.

            2.2024 - Banca: LJ Assessoria e Planejamento Administrativo Limitada - LJ:
            Em português, existem dois processos principais de formação de palavras: derivação e composição. Numere as palavras de acordo com o seguinte código:

            1. Para derivação prefixal
            2. Para derivação sufixal

            () Impossível
            () Possivelmente
            () Cordialmente

            'Impossível' é formada pela adição do prefixo 'im- ao radical 'possível', caracterizando derivação prefixal.
            'Possivemente' é formada pela adição do sufixo '-MENTE' ao radical 'possível', caracterizado derivação sufixal.
            'Cordialmente' é formada pela adição do sufixo '-MENTE' ao radical 'cordial', caracterizado derivação sufixal.

            3. SELECON/ANALISTA/2024- A palavra PERMANÊNCIA deriva do verbo “permanecer” e é formada por derivação sufixal. 
            Esse mesmo processo é atestado na palavra:

            a.ciência
            b.essência
            c.anuência
            d.coerência

            a.ciência   <- Essa palavra deriva do latim e significa 'conhecimento'. Não se encaixa no processo de derivação.\n
            b.essência  <- Essa palavra deriva do latim e não segue o mesmo processo de derivação.\n
            c.anuência  <- [bg_green]O sufixo '-ência' é adicionado ao radical do verbo 'anuir' 'anu-', formando o substantivo abstrato por derivação sufixal.[reset]\n
            d.coerência <- A formação da palavra passa também pela derivação sufixal a partir do latim, onde '-CO' significa 'com'
            e 'haerere' significa 'aderir'. O sufixo '-ência' é adicionado para forma o substantivo abstrato que indica a qualidade
            de estar aderido ou logicamente conectado.

            4. FURB/2024/tradutor: A respeito dos processos de formação de palavras do texto, analise as afirmações a seguir:

            I.  As palavras "arrumando" e "avaliação" foram formadas por meio de derivação prefixal.
            II. A palavra "aprendizado" foi formada pelo processo de composição por justaposição.
            III.A palavra "pesquisadora" foi formada pela derivação sufixal.
            IV. A palavra "pesquisa" foi formada por uma derivação imprópria.

            a. III, apenas
            b. III e IV  apenas
            c. I e II  apenas
            d. I, II, III, IV
            e. I,II e IV apenas

            I. A palavra 'arrumando' não há prefixo, seu radical é 'arrum-' e possui derivação sufixal com desinência gerúndio '-ndo'.
            Vem do verbo primitivo 'arrumar' que possui a vogal temática 'a' e a desinência 'r' no infinitivo.
            A palavra 'avaliação' não há prefixo, seu radical é 'avali-' e possui derivação sufixal '-ção'.

            II. A palavra 'aprendizado' é formada por derivação sufixal somente com seu radical 'aprend-' e o sufixo '-izado'.
            Composição por justaposição são 2 ou mais radicais que se juntam sem perder elementos.

            III. Correto a afirmação. A palavra possui seu radical 'pesquis- e sufixo '-adora' caracterizando deverivação sufixal.

            IV. A palavra 'pesquisa' é formada por derivação regressiva ou deverbal na qual consiste na redução da palavra primitiva do verbo
            'pesquisar' para um substantivo abstrativo derivado 'pesquisa'.

            [bg_green] Somente a III está correta. Alternativa 'a' [reset]

            5.2024/AVANCA-SP/Serviços gerais/camara:
            As palavras ‘memorável’ e ‘clemente’ são formadas por processos derivacionais e apresentam sufixos formadores de adjetivos na língua portuguesa. 
                O mesmo ocorre em:

                a. metodicamente
                b. esfriar 
                c. funcional 
                d. escassez
                e. probabilidade

                a. A palavra 'metodicamente' apresenta sufixo '-mente' formador de advérbios.
                b. A palavra 'esfriar' apresenta sufixo '-AR' formador de verbos.\n
                c. [bg_green]A palavra 'funcional' apresente sufixo '-AL' formador de adjetivos.[reset]\n
                    O radical "funcion-" é um verbo, mas ao adicionar o sufixo "-al", transforma-se em um adjetivo.
                    [bg_red]O sufixo confere um novo significado ao radical, indicando a qualidade de algo que funciona.[reset]
                      [bg_red]Em resumo, o adjetivo "funcional" é um exemplo claro de como o processo de sufixação pode criar novas palavras a partir de radicais[reset]
                       [bg_red]existentes, alterando seu significado e classe gramatical.[reset]\n
                d. A palavra 'escassez' apreseta sufixo '-EZ' formador de substantivos abstratos.
                e. A palavra 'probabilidade' apresenta o sufixo '-DADE' formado de substantivos abstratos.

6. Instituto Access/2024/CREMEB/2024:A respeito dos processos de formação das palavras, assinale a alternativa correta.

a. Planalto – derivação.
b. Vaivém – derivação.
c. Livraria – composição.
d. Guarda-chuva – composição.
e. Felicidade – composição.

a. A palavra 'planalto' é uma união das palavras 'plano' + 'alto' a qual os radicais se juntam e perdem elementos. O processo é chamado
de COMPOSIÇÃO POR AGLUTINAÇÃO. Não é por derivação. Alternativa ERRADA.

b. A palavra 'vaivém' é o mesmo processo de composição por JUSTAPOSIÇÃO a qual NÃO perdem elementos na união. 'vai' + 'vem'

c. 'Livraria' é derivação sufixal da palavra 'livro' + sufixo 'ARIA e não uma composição de dois radicais.

[bg_green]d. 'Guarda-chuva' é uma palavra formada pela junção das palavras 'guarda' e 'chuva', caracterizando um processo de composição por justaposição.[reset]

e. 'Felicidade' é uma palavra formada a partir da palavra 'feliz' com o acréscimo do sufixo '-idade'. Caracterizando um processo de derivação sufixal
e não de composição.

7. Instituto Darwin/2024-Professor. - Analise os períodos abaixo retirados do Texto:

I. “Entrar o Ano-Novo de [yellow]gravata-borboleta¹[reset] pode comprometer [yellow]seriamente²[reset] as relações entre o Oriente e o Ocidente.”

II. “Mas a [yellow]]encosta³[reset] do vulcão é comprida...”

a.1. Composição por justaposição. 2. Derivação pré-sufixal. 3. Derivação regressiva.
b.1. Derivação prefixal. 2. Composição por justaposição. 3. Derivação imprópria.
c.1. Composição por aglutinação. 2. Derivação sufixal. 3. Derivação imprópria.
d.1. Composição por justaposição. 2. Derivação sufixal. 3. Derivação regressiva.

'Gravata-borboleta' é um exemplo de composição por justaposição, onde duas palavras se unem mantendo suas identidades sem perda de elementos.
A palavra 'seriamente' exemplifica a derivação sufixal, com a adição de um sufixo 'mente'
'encosta', substantivo abstrato em que seu verbo primitivo 'encostar' deriva por derivação regressiva.

8.FUNDATEC/Tecnologista/2024:

Assinale a alternativa que indica palavra que tenha sido formada pelo mesmo processo que o vocábulo “inovação”.


A.Guarda-chuva.
B.Chuvisco.
C.Planalto.
D.Debate.
E.Enraizar.

 O termo 'guarda-chuva' é formado por composição por justaposição, onde duas palavras se unem para formar uma nova, sem alteração morfológica.\n
  [bg_green]'Chuvisco' é formado pelo processo de derivação sufixal, semelhante a 'inovação'.[reset]\n
    A palavra base 'chuva' recebe o sufixo '-isco', resultando em uma nova palavra. Este processo é análogo ao da formação de 'inovação' a partir de 'inovar' + '-ção'.
'Planalto' é um exemplo de composição por justaposição, onde 'plano' e 'alto' se unem para formar uma nova palavra.\n
'Debate' é uma palavra que não resulta de um processo de derivação sufixal evidente como em 'inovação'.
 Ela vem do francês 'débat', indicando um empréstimo linguístico, e não a adição de um sufixo a uma base já existente na língua portuguesa.\n
 'Enraizar' é formado por derivação prefixal e sufixal, onde o prefixo 'en-' e o sufixo '-ar' são adicionados à base 'raiz'. 
 Embora envolva a adição de um sufixo, o processo também inclui um prefixo, diferindo do processo que formou 'inovação'.
 O processo é chamado de derivação parassintética

 9. FUNDATEC / Professor / 2024

 Cegalla nos diz que “Em nossa língua há dois processos gerais para a formação de palavras: a derivação e a composição”.
   Sobre tais processos, são feitas as seguintes afirmações:

I. Parassíntese consiste no acréscimo, ao mesmo tempo, de um prefixo e de um sufixo a um radical.
 A NGB não adotou a denominação “parassíntesse” nem alude explicitamente a esse processo.

II. A derivação regressiva consiste na substituição da terminação de um verbo por qualquer outra desinência.
 Nesse tipo de derivação, a língua cria verbos a partir de substantivos.

III. O processo de composição associa duas ou mais palavras ou dois ou mais radicais para formar uma palavra nova.
 Esse processo pode ser efetuado por justaposição ou por aglutinação; ao aglutinarem-se, os componentes subordinam-se a um só acento tônico, o do último componente.

[bg_green]Item I correto // [reset]
[bg_red]Item II INCORRETO //[reset]\n
O item II está incorreto. A derivação regressiva não consiste na substituição da terminação de um verbo por outra desinência,
 mas sim na formação de substantivos a partir de verbos, geralmente pela retirada de uma terminação verbal.\n
[bg_green]Item III -stá correto ao afirmar que a composição associa duas ou mais palavras ou radicais para formar uma nova palavra,[reset]
[bg_green]podendo ser por justaposição ou aglutinação. Na aglutinação, os componentes se subordinam a um só acento tônico.[reset]

10. Legalle/2024. A derivação regressiva é um dos processos de formação de palavras existentes. 
Contrariamente às outras formas de derivação, que ocorrem por acréscimo, na derivação regressiva ocorre a redução da palavra primitiva para a formação da palavra derivada.
 Qual dos seguintes vocábulos é formado por derivação regressiva?

A.português (l.4).
B.comerciante (l.10).
C.adocicado (l. 14).
D.involuntários (l.29).
E.boteco (l.33)


O termo 'português' não é formado por derivação regressiva. Ele é um adjetivo pátrio, derivado do latim 'portucalensis', 
referindo-se a algo ou alguém de Portugal. Portanto, não se encaixa no processo de derivação regressiva.\n
A palavra 'comerciante' é formada por derivação sufixal, a partir do verbo 'comerciar'.
O sufixo '-ante' é adicionado para formar um substantivo que designa a pessoa que realiza a ação de comerciar.
Não é um exemplo de derivação regressiva.\n
O vocábulo 'adocicado' é formado por derivação sufixal, com o acréscimo do sufixo '-ado' ao radical 'adocicar'.
Este processo não é regressivo, pois envolve a adição de um sufixo.
A palavra 'involuntários' é formada por derivação prefixal e sufixal, com o prefixo 'in-' e o sufixo '-ários' adicionados ao radical 'voluntário'. 
Este processo não é regressivo, pois envolve a adição de afixos.\n
[bg_green]O termo 'boteco' é um exemplo de derivação regressiva. Ele é derivado do verbo 'botecar', que significa frequentar botecos.[reset]
[bg_green]A formação de 'boteco' a partir de 'botecar' ocorre pela redução do verbo, caracterizando a derivação regressiva.[reset]

11. AOCP/2024 - A palavra 'revitalizar' passa pelo processo de formação que o vocábulo:

A.rebento.
B.rebocar.
C.socializar.
D.humanizar.
E.desconstrução.


A palavra 'revitalizar' é formada pelo acréscimo do sufixo '-izar' ao radical 'vital', indicando a ação de tornar vital ou dar vida novamente.
e do prefixo '-re'.\n
'Rebento' é um forma derivada do verbo 'rebentar', portanto é derivação deverbal ou regressiva.\n
'rebocar' é o verbo em sua desinência no infinitivo.\n
A palavra 'socializar' é formada pelo acréscimo do sufixo '-izar' ao radical 'social', indicando a ação de tornar social ou integrar socialmente.
Portanto é uma derivação sufixal, diferente da palavra em questão.\n
'humanizar'é formada pelo acréscimo do sufixo '-izar' ao radical 'humano', indicando a ação de tornar humano ou dar características humanas.\n
Portanto é uma derivação sufixal diferente da palavra em questão.\n
[bg_green] A palavra 'desconstrução' é formada pelo acréscimo do prefixo 'des-' ao radical 'construção', indicando a ação de desfazer ou desmontar algo construído.[reset]
 [bg_green]Embora o processo de formação envolva prefixação e sufixação, a lógica de transformação do significado é semelhante à de 'revitalizar', que também envolve uma mudança significativa no estado ou condição.[reset]
 [reset]Além disso temos um sufixo '-ção', derivação sufixal do verbo primitivo CONTRUIR.[reset]

 12. IDECAN/médico/2024:

 Assinale a alternativa em que esteja indicada corretamente uma palavra do texto que tenha sido formada, ao longo de seu processo, por composição.

A.interagências
B.economia
C.ultrapassam
D.Infelizmente
E.descapitalização

A palavra 'interagências' não é composição e sim uma derivação prefixal 'inter' + radical 'agências'.\n
[bg_green]A palavra 'economia' é formada por composição por justaposição. Resulta na união dos elementos 'eco-'( do grego casa) + 'nomia' ( do grego 'lei')[reset]\n
A palavra 'ultrapassam' é derivação prefixal e sufixal. Derivação do verbo 'passar' + prefixo 'ultra' + sufixo '-am'.\n
A palavra 'infelizmente' é formada por derivação prefixal e sufixal. Onde o prefixo 'in-' é adicionado ao adjetivo 'feliz' e o sufixo '-mente' para formar o advérbio.\n
A palavra 'descapitalização' é formada por derivação sufixal e prefixal. Onde o prefixo 'des-' é adicionado ao substantivo 'capital' e o sufixo '-ização ' forma o substantivo abstrato.\n

13.IDCAP/2024- Esses dados incluem desde incêndios até 'desmatamento' e mudanças do uso da terra, dentro e fora das áreas protegidas.
O vocábulo destacado é formado pelo processo de:

A.Parassíntese.
B.Derivação imprópria.
C.Prefixação e sufixação.
D.Sufixação.

Não pode ser parassíntese pois a retirada do sufixo 'mento' ainda resultaria em palavra existente 'desmatar'.
Ou retirando o prefixo 'des' resultaria em'matar'.\n
Derivação imprópria é quando ocorre quando uma palavra muda de classe gramatical sem sofrer alteração em sua forma..
Não houve mudança em sua classe, ocorreu um adição de sufixo e prefixo.\n
[bg_green] Ocorreu uma adição prefixal e sufixal na palavra portanto a alternativa correta é a letra 'C'.[reset]

14. IBADE/ANalista TI/2024:
Qual é o processo de formação de palavras que originou o vocábulo “sobrevivência”?

A.Derivação sufixal.
B.Derivação prefixal e sufixal.
C.Derivação prefixal.
D.Derivação parassintética.
E.Derivação imprópria.

A palavra 'sobrevivência' é formada a partir do verbo 'viver' com adição do sufixo e prefixo.
[bg_green]'Sobre' é prefixo, verbo primitivo 'viver' + -ência ( sufixo ) = 'sobrevivência'. Portanto a alternativa correta é a 'B'[reset]

A derivação sufixal ocorre quando um sufixo é adicionado a uma palavra base. No caso da palavra 'sobrevivência' não somente o sufixo é adicionado
mas também um prefixo 'sobre-'. [bg_red]Portanto não é a alternativa a.[reset]

A derivação prefixal ocorre quando um prefixo é adicioado a uma palavra base. No caso da palavra em questão não somente o prefixo é adicionado
mas também um sufixo '-ência'. [bg_red] Portanto não é a alternativa c.[reset]\n
A derivação parassintética ocorre quando um prefixo e um sufixo são adicionados simultaneamente a uma palavra base, 
e a retirada de qualquer um deles torna a palavra inexistente ou sem sentido.
 No caso de 'sobrevivência', a palavra 'viver' existe independentemente, o que não caracteriza a parassíntese.\n
A derivação imprópria ocorre quando uma palavra muda de classe gramatical sem sofrer alteração em sua forma.
No caso de 'sobrevivência', há a adição de prefixo e sufixo, não uma mudança de classe gramatical.

15. Instituto Legatus/Professor/2024:
Quanto ao processo de formação de vocábulos, marque a alternativa que contém as informações corretas.

A.[...] o mais antigo dos abomináveis [yellow]gracejos[reset] racistas. DERIVAÇÃO IMPRÓPRIA.
B.Não precisamos condená-lo ao [yellow]submundo[reset][...] – COMPOSIÇÃO POR JUSTAPOSIÇÃO.
C.[...] [yellow]empobrecendo[reset] ainda mais nosso paupérrimo debate público, apenas para alimentar o minotauro. PARASSÍNTESE.
D.Troca-se a difícil tarefa de confrontar [yellow]intelectualmente[reset] o "inimigo" [...]- PREFIXAÇÃO E SUFIXAÇÃO.
E.Os [yellow]hipócritas[reset] investem na decência dos decentes, em busca de uma finalidade indecente. DERIVAÇÃO DEVERBAL.

O termo 'gracejos' é um substativo abstrato derivado do verbo gracejar, com adição do sufixo 'os'. A palavra não muda de classe gramatical.
[bg_red]Portanto não é derivação imprópria.[reset]
O termo 'submundo' é uma adição prefixal 'sub' + substantivo 'mundo' = 'submundo'. Não é composição por justaposição. [bg_red][ERRADO][reset]\n
O termo 'empobrecendo' é uma parassíntese, processo que envolve adição simultânea de um prefixo e um sufixo ao radical da palavra.
A partir da palavra 'pobre' forma-se um novo verbo 'empobrecer' na desinência gerúndio 'empobrecendo'.
Prefixo 'em' + adjetivo + sufixo 'cendo'. [bg_green] Alternativa C a CORRETA [reset]\n
O termo intelectualmente é um processo de derivação sufixal somente, onde temos o sufico '-mente' adicionado ao adjetivo 'intelectual'
para forma o advérbio de modo.\n
O termo 'hipócritas' é derivado do substantivo abstrato 'hipocrisia' através do processo de derivação sufixal onde o sufixo '-TAS'
é adicionado para formar um adjetivo 'hipócritas', no plural. Não é derivação regressiva, pois não deriva diretamente de um verbo.\n

16. MAXIMA Auditoria / 2024 -
“Sentia o mundo [yellow]palpitar[reset] docemente em seu peito, doía-lhe o corpo como se nele suportasse a feminilidade de todas as mulheres."
Levando em consideração o processo de estrutura e formação de palavras, está INCORRETA a afirmação:

A.O radical é PALPIT.
B.O segundo “A” consiste numa vogal temática.
C.PALPITA é a união do radical com a vogal temática, denominada tema.
D.Há uma desinência de gerúndio representada pela letra “R”.

A.O radical é PALPIT. [CORRETA]
B.O segundo “A” consiste numa vogal temática. [CORRETA]
C.PALPITA é a união do radical com a vogal temática, denominada tema. [CORRETA]
D.Há uma desinência de gerúndio representada pela letra “R”. [bg_red] INCORRETA [reset]

[bg_green]A desinência correta é no infinitivo.[reset]
[blue]O radical de 'palpitar' é 'palpit'. O radical é a parte da palavra que contém o seu significado básico. Neste caso, 'palpit' é o radical que dá origem a palavras como 'palpitação' e 'palpitante'.[reset]\n
[blue]O segundo 'a' em 'palpitar' é uma vogal temática. A vogal temática é a vogal que se junta ao radical para formar o tema da palavra. Em 'palpitar', o 'a' é a vogal temática que se junta ao radical 'palpit.[reset]\n
[blue]'Palpita' é a união do radical 'palpit' com a vogal temática 'a', formando o tema 'palpita'. [reset]\n

17. ITAME/Artífice/2024.
Assinale a alternativa cujas palavras são formadas respectivamente pelo processo de derivação parassintética e prefixal.

A.Esquentar e realmente.
B.Martelada e coautor.
C.Esquentar e coautor.
D.Realmente e felizmente.

[bg_green]A palavra 'esquentar' é formada a partir do adjetivo 'quente' com adição simultânea do prefixo 'es-' e do sufixo '-ar'.[reset]
[bg_green]O verbo 'esquentar' não faria sentido sem a presença de ambos, prefixo e sufixo ao mesmo tempo. Ou seja, derivação parassintética.[reset]\n

[bg_green]A palavra 'coautor' é formado pelo processo de derivação prefixal a qual o prefixo 'co' adiciona a palavra substantivo 'autor'.[reset]

[yellow]A palavra 'realmente' é formada pelo processo de derivação sufixal a qual temos o adjetivo 'real' + sufixo '-MENTE'.[reset]\n
[yellow]A palavra 'felizmente' é formada pelo processo de derivação sufixal '-MENTE' adicionado ao radical do adjetivo 'feliz'[reset]\n
[yellow]O termo 'martelada' é formado pelo processo de derivação sufixal diretamente do verbo primitivo 'martelar' + sufixo '-ada'[reset]\n

18. FGV/Auditor/2024
Leonardo da Vinci, certa vez, definiu arte como aquilo que “diz o indizível, exprime o inexprimível e traduz o intraduzível”.
Sobre o processo de formação das palavras destacadas, assinale a alternativa incorreta.

A.Os prefixos atribuem ao radical um sentido de negação.
B.Os prefixos ligam-se ao radical por meio da vogal temática -i.
C.São adjetivos formados a partir de verbos.
D.São palavras formadas por derivação parassintética.
E.Todas podem ser transformadas em orações adjetivas.

[blue]Alternativa A - Realmente os prefixos 'in-' atribuem um sentido de negação.[reset] [bg_green] CORRETA [reset]

[red] Os prefixos não se ligam ao radical por meio da vogal temática '-i'. A vogal faz parte da derivação SUFIXAL que torna os verbos em adjetivos. 'ível'[reset] [bg_red] ERRADA [reset]\n
[red] A alternativa D também encontra-se errada. Não são formadas por derivação parassintética e sim por derivação prefixal.[reset]\n
[red] Mesmo com a retirada do prefixo 'in-' ainda deixam as palavras válidas e existentes ( dizível, exprimível, traduzível )[reset]\n
[blue] As palavras podem ser transformadas em orações adjetivas sim: 'que não pode ser dito','que não pode ser exprimido', 'que não pode ser traduzido'.[reset][bg_green] CORRETO [reset]

19. FUNDATEC/2024/Fiscal:
Qual das alternativas abaixo apresenta palavras formadas por derivação sufixal?

A.Antepassado – lugarzinho.
B.Queridíssima – subscrito.
C.Sobrescrito – incomum.
D.Assexuado – frutífero.
E.Farináceo – sanguíneo.

A palavra 'antepassado' é formada pelo processo de derivação prefixal 'ante' + verbo no particípio 'passado' do verbo primitivo 'passar'.
A palavra 'lugarzinho' é formada pelo processo de derivação sufixal '-zinho' + radical 'lugar' substantivo abstrativo.\n
[bg_red]Não é a alternativa A - Precisa ser derivação sufixal em ambas. [reset]\n

A palavra 'queridíssima' é formado pelo adjetivo 'querida' + derivação sufixal 'íssima'.
A palavra 'subscrito' é formada pela derivação prefixal 'subs' + radical 'crito' = 'subscrito'
[bg_red] Não é a alternativa B - Precisa ser derivação sufixal em ambas. [reset]

A palavra 'sobrescrito' é formado pela composição por justaposição onde duas palavras se unem sem perda na estrutura das palavras originais.
'sobre' é palavra própria, é preposição e 'escrito' é um substantivo abstrato derivado do verbo 'escrever'.
A palavra 'incomum' é formada pela derivação prefixal 'in-' + adjetivo 'comum'.
[bg_red] Não é a alternativa C - Precisa ser derivação sufixal nas duas. [reset]

A palavra 'assexuado' é formado tanto por derivação prefixal 'as-' como sufixal '-uado' e possui o radical 'sex', ou seja, algo que não é sexualizado.
A palavra 'frutífero' é formada por derivação sufixal '-fero' do verbo primitivo 'frutificar' do radical 'fruti'.
[bg_red] Portanto não é a alternativa 'D' - Ambas precisam ser derivação sufixal.[reset]

A palavra 'farináceo' é um adjetivo formado pelo substantivo 'farinha' e deriva-se sufixo '-áceo'.
A palavra sanguíneo é um adjetivo formado pelo substantivo 'sangue' + sufixo '-íneo'.
[bg_green] Portanto, a alternativa correta da questão é a 'E'. [reset]

20. UFES /médico/2024:
A palavra que apresenta o mesmo processo de formação da palavra 'infausta' é:

A.incapacidade.
B.indesafiável.
C.indesejável.
D.invenção.
E.irreal.

[blue]A palavra 'infausto' sigifica algo que traz má sorte. Seu processo de formação deriva-se por prefixo 'in-' que tem o sentido de negação, inverso.[reset]\n
[red] A palavra 'incapacidade' é formada por derivação sufixal '-cidade' e prefixal 'in-' a partir do adjetivo 'capaz'.[reset]
[bg_red]Portanto não é o mesmo processo de formação. Não é a alternativa A[reset]\n

[red] A palavra 'indesafiável' é um adjetivo formado por derivação prefixal 'in-' como por derivação sufixal '-ável' do verbo primitivo 'desafiar'.[reset]
[red] A palavra 'invenção' é formada por derivação prefixal 'in-' e sufixal '-nção'. Substantivo que significa algo diferente do visto.[reset]

[bg_green] A palavra 'irreal' é formada por derivação prefixal 'ir-' algo que é fora da realidade.[reset] [bg_green] CORRETA ALTERNATIVA [reset]

21. INSTITUTO SOCIAL UNIVIDA/2024/ASSISTENTE:
As palavras “alcoolismo” e “etilismo” são formadas por:

A.Derivação prefixal.
B.Derivação sufixal.
C.Derivação parassintética.
D.Composição por justaposição.
E.Derivação regressiva ou deverbal.

As palavras possuem o mesmo significado. São atos comportamentais de dependências de substâncias alcoólicas. O radical é 'álcool'
e o sufixo é '-ismo' usado em substantivos que indicam condição ou comportamento. \n
Assim como o radical 'etil' relacionado ao etanol e o sufixo '-ismo' que indica condição, estado, doutrina.
[bg_green] Portanto ambas as palavras se foram por derivação sufixal.[reset] [bg_green] Alternativa B [reset]

22. FUNDATEC/2024:
Sobre Estrutura e Formação de Palavras, à luz do que ensina Bechara, analise as assertivas a seguir:

I. Prefixos e sufixos recebem o nome de afixos; são prefixos os afixos que se pospõem ao radical, e sufixos os que se lhes antepõem.
II. Tema é o radical acrescido da vogal temática e que constitui a parte da palavra pronta para funcionar no discurso e para receber a desinência ou sufixo.
III. As desinências nos nomes e em certos pronomes marcam as flexões de gênero e número; nos verbos: número, pessoa, tempo e modo.

Quais estão corretas?
A.Apenas I.
B.Apenas II.
C.Apenas I e II.
D.Apenas II e III.
E.I, II e III.

[red]O item I está errado.[reset] Os prefixos antepõem ao radical e os sufixos pospõem.\n

[green]O item II está correto.[reset]
Tema é realmente o radical acrescido da vogal temática, pronto para funcionar no discurso e receber desinências ou sufixos. 

[bg_green] O item III também está correto, pois as desinências nos nomes e pronomes marcam flexões de gênero e número, e nos verbos marcam número, pessoa, tempo e modo.[reset]
 [bg_green]Desinências nominais indicam gênero e número, enquanto as desinências verbais indicam número, pessoa, tempo e modo.[reset]

23. Instituto Verbena/2024/analista:
Os vocábulos “perda”, “corte” e “apelo” são formados a partir do seguinte processo de formação de palavras

A.composição por justaposição.
B.composição por aglutinação.
C.derivação regressiva.
D.derivação parassintética.

[bg_green]'perda', 'corte', 'apelo' são substantivos abstratos derivados dos verbos primitivo'perder', 'cortar', 'apelar' por derivação regressiva a qual[reset]
[bg_green]retira-se a vogal temática e a desinência para formar o subsntativos.[reset]

24.Ano: 2024 Banca: Instituto Avança São Paulo - Avanca SP Prova: Avança SP - Câmara de Itapecerica da Serra - Técnico em Informática - 2024
Analise as palavras a seguir, que ocorrem no texto, e assinale a alternativa em que a palavra dada é formada pelo processo de composição por justaposição.

A.desconcertante.
B.polimorfo.
C.silicatos.
D.quimicamente.
E.subsequente.

O termo 'desconcertante' é formada pelo processo de derivação sufixal '-ante'- sufixo que forma adjetivos a partir de verbos indicando
algo que está acontecendo ou que causa uma ação e pelo prefixo 'des-' que indica negação, reversão ou oposição.\n
O radical 'concertar' significa ajustar, harmonizar ou organizar. [bg_red]Portanto não é composição por justaposição.[reset]

[bg_green]O termo 'polimorfo' é uma composição por justaposição em que ocorre a união de duas palavras próprias sem perdas de elementos.[reset]
[bg_green]A palavra 'poli' + a palavra 'morfo' = 'polimorfo' = várias formas.[reset]

A palavra 'silicatos' é formada por derivação sufixal. O radical 'silic' é derivado do substantivo 'silício', elemento químico. Seu sufixo é
'-atos' usado para formar nome de sais minerais.

[blue]A palavra 'quimicamente' é formada por derivação sufixal -'mente'. Formador de advérbios. Seu radical 'quimica' é substantivo abstrato derivado do latim.[reset]

25. Ano: 2024 / Banca: COSEAC / Prova: COSEAC - Prefeitura de Maricá - Docente - 2024
Os vocábulos “brigas” (linha 17), “coexistência” (linha 23) e “caixote” (linha 11) são formados, respectivamente, pelos processos de derivação:

A.imprópria, sufixal e prefixal.
B.sufixal, prefixal e sufixal, e regressiva.
C.parassintética, por amálgama e por conversão.
D.por conversão, parassintética e sufixal.
E.regressiva, prefixal e sufixal.

A palavra 'brigas' derivado do substantivo abstrato no plural do verbo primitivo 'brigar' formado por derivação regressiva.\n
A palavra 'coexistência' é formado por derivação prefixal '-co' + verbo primitivo 'existir' + sufixal '-ência',\n
A palavra 'caixote' é formado pelo substantivo 'caixa' + sufixo '-ote' por derivação sufixal.\n
[bg_green] Portanto a alternativa correta é a E [reset]

26. Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN
Prova: IDECAN - Prefeitura de Mossoró - Assistente Social - 2024
Na Língua Portuguesa, há diversos processos morfológicos relacionados à formação de palavras – 
os quais enriquecem o idioma ao possibilitarem a criação de novos termos, ampliam o léxico e refletem a evolução linguística.
 Nesse sentido, pode-se afirmar que a “atemporal” é fruto de um processo de derivação:

A.sufixal.
B.prefixal.
C.imprópria.
D.regressiva.
E.parassíntética.

[yellow]A derivação parassintética ocorre quando uma palavra é formada simultaneamente pela adição de um prefixo e um sufixo a um radical.[reset]
[yellow]No caso de 'atemporal', temos o prefixo 'a-' e o sufixo '-al' adicionados ao radical 'tempo'.[reset]

[red] A derivação regressiva ocorre quando uma palavra é formada pela redução de outra palavra, geralmente um verbo que se transforma em substantivo.[reset]
[red]'Atemporal' não é um caso de derivação regressiva, pois envolve a adição de prefixo e sufixo[reset]


27. Ano: 2024/Banca: Instituto Avalia/Prova: Instituto Avalia - IMASUL - Analista Ambiental - Área: Direito - 2024
Qual das palavras a seguir NÃO é formada pelo processo de derivação prefixal?

A.Desfavorável.
B.Contraproposta.
C.Imprescindível.
D.Inadiável.
E.Catalisador.

[red]A palavra 'Desfavorável' é formada pelo processo de derivação prefixal, onde o prefixo 'des-' é adicionado ao radical 'favorável'. [reset]

[red]A palavra 'Contraproposta' é formada pelo processo de derivação prefixal, onde o prefixo 'contra-' é adicionado ao radical 'proposta'. [reset]

[red]A palavra 'Imprescindível' é formada pelo processo de derivação prefixal, onde o prefixo 'im-' é adicionado ao radical 'prescindível'.[reset]

[red]A palavra 'Inadiável' é formada pelo processo de derivação prefixal, onde o prefixo 'in-' é adicionado ao radical 'adiável'. [reset]

[bg_green]A palavra 'Catalisador' não é formada por derivação prefixal. Ela é formada por derivação sufixal, onde o sufixo '-dor' é adicionado ao radical 'catalis-'.[reset]


28.Ano: 2024 / Banca: MS Concursos / Prova: MS Concursos - Prefeitura de Potim - Técnico de Enfermagem - 2024 
Referindo-se à estrutura e formação das palavras, assinale (V) verdadeiro ou (F) falso e marque a alternativa devida.

( ) Exemplo de derivação parassintética ou parassíntese: entristecer.

( ) Exemplo de derivação sufixal ou sufixação: reler.

( ) Exemplo de derivação prefixal ou prefixação: risonho.

( ) Exemplo de derivação regressiva: o portuga (de português).

( ) Exemplo de derivação imprópria: O olhar de Aurora era fascinante.

A.F – V – V – V – V.
B.V – F – F – V – V.
C.V – V – V – F – F.
D.V – V – V – V – V.
E.F – V – F – V – V.

[green]'Entristecer' é um exemplo de derivação parassintética, pois a palavra é formada pela adição simultânea do prefixo 'en-' e do sufixo '-ecer'.[reset]
[green]O adjetivo em questão é 'triste' em que não existem palavras com a remoção dos afixos.[reset]

[red]'Reler' não é um exemplo de derivação sufixal, mas sim de derivação prefixal, pois é formada pela adição do prefixo 're-'[reset]

[red] 'Risonho' é um adjetivo exemplo de formação por derivação sufixal '-sonho' proveniente do radical 'ri'.[reset]

[blue] 'o portuga' é exemplo de derivação regressiva em que ocorre uma redução da palavra, é uma forma reduzida de 'português'.[reset] [bg_green] CORRETO [reset]

[blue] 'o olhar' é derivação imprópria. O artigo 'o' define o verbo 'olhar' como substantivo no contexto.[reset] [bg_green] CORRETO [reset]


29.Ano: 2024 / Banca: Instituto AOCP / Prova: Instituto AOCP - MPE PR - Contador - 2024 
Considerando os processos de formação de palavras, analise as assertivas e assinale a alternativa que aponta as corretas.

I. No trecho “[...] nossos processos mentais são distintos dos nossos corpos físicos (dualismo mente-corpo) [...]”
“dualismo” formou-se por derivação sufixal, enquanto “mente-corpo”, por composição por justaposição.\n
II. Em “[...] estas explicações intuitivas dentro de uma estrutura 'materialista' consistente com as descobertas da 'neurociência'.”
Os termos destacados originaram-se mediante um mesmo processo de formação de palavras.\n
III. No trecho “Dessa forma, a arquitetura mental da mente deve estar fortemente adaptada [...]”
Os termos destacados apresentam sufixos nominais.\n
IV. Em “Apesar de ser contraintuitivo atribuir arbítrio e responsabilidade pessoal a um conjunto biológico de células nervosas [...]”
O termo destacado formou-se por composição por justaposição.\n
V. No trecho “Em vez de ajudar os indivíduos a sobreviver, ela evoluiu para nos ajudar [...]”, o verbo destacado formou-se por derivação prefixal.

A.Apenas I, II e III.
B.Apenas II, III e IV.
C.Apenas II e IV.
D.Apenas I e V.
E.Apenas I, IV e V.


[bg_green]I   - 'dualismo' -> derivação sufixal '-ismo', radical 'dual' // 'mente-corpo' -> composição por justaposição [reset]
[red]II  - materialista -> derivação sufixal '-ista', radical 'material' -> substantivo // neurociência -> composição por justaposição - [reset]
[red]III - mental -> radical 'mente' sufixo '-al' // fortemente -> radical 'forte' sufixo '-mente' -> derivações sufixais -[reset]
[bg-green]IV  - 'contraintuitivo' -> composição por justaposição 'contra' + 'intuitivo' // Bancas não consideram prefixos como palavras próprias[reset]
[yellow]Portanto, a palavra 'contraintuitivo' é formada por derivação prefixal 'contra-' + radical 'intuitivo'[reset]
[bg_green]V   - 'sobreviver' -> composição por justaposição. 'sobre' + 'viver'[reset] // Atenção! Bancdas não consideram prefixos como palavras próprias [reset]
[yellow]  Portanto, a palavra 'sobreviver' é formada por derivação prefixal 'sobre' + radical 'viver' [reset]

[bg_green] Gabarito: Alternativa E a correta [reset]

30.Ano: 2024 // Banca: LJ Assessoria e Planejamento Administrativo Limitada - LJ // Prova: LJ - Prefeitura de Turilândia - Professor de 1º ao 5º ano - 2024 :

Pratique o DEBOISMO: ficar de boa , ficar em paz, sem estresse, sem preocupações.
Sobre o processo de formação das palavras, podemos dizer que o termo DEBOISMO é exemplo de formação:

A.parassintética
B.prefixal
C.sufixal
D.regressiva
E.neológica

[bg_red] Atenção! [reset]
    [bg_green] 'deboismo' é uma palavra que não existe e foi criada para dar sentido a algo. Portanto a alternativa correta é a 'E' [reset]
            [blue] neologismo morfológico é o nome que dá quando se cria uma palavra e sentido para a palavra [reset]

31.Ano: 2024 // Banca: Instituto Legatus - Legatus // Prova: Legatus - Prefeitura de Parnaíba - Professor Classe A - Área Artes - 2024
Quanto ao processo de formação das palavras destacadas, está correto o que se afirma em:

A.esperança de que a 'embalagem' estrangeira [...]. Derivação por prefixação e sufixação.
B.possa 'envaidecer' os novos "students" e suas "families". Derivação por sufixação.
C.Pelo excesso ou pela falta, o resultado é o mesmo: a 'atrofia' do valor do passado. Derivação imprópria
D.[...] criando uma 'infindável' biblioteca pública [...] Composição por aglutinação.
E.[...] tudo o que 'envelhece', que enfeia e que, portanto, se humaniza, se transforma em trauma. Derivação por parassíntese.            

[red] A palavra 'embalagem' é formada pela derivação sufixal '-gem' + radical do verbo primitivo 'embalar' somente. Questão errada.[reset]
[red] A palavra 'envaidecer' é formado por derivação sufixal '-ecer' e prefixal 'en' do adjetivo 'vaidoso' que por sua vez vem do substantivo 'vaidade'.[reset]
 [red] Por parassíntese , portanto a alternativa está errada. [reset]
 [red]A palavra 'atrofia' é formada por derivação sufixal , onde o sufixo '-ia' é adicionado ao radical adjetivo 'atrófico'. Não é por derivação imprópria.[reset]
 [red] A palavra 'infindável' é formada pelo processo de derivação prefixal 'in- que indica negação ou ausência e sufixal '-ável' que forma adjetivos. [reset]
 [bg_green] A palavra 'envelhece' é formada por derivação parassintese a qual o prefixo 'en-' + radical adjetivo 'velho' + sufixo '-ece' são adicionados simultâneamente.[reset]
        [blue]Sendo que com a remoção de algum afixo, não existe palavra alguma.[reset]

32. Ano: 2024 / Banca: Instituto Brasileiro de Apoio e Desenvolvimento Executivo - IBADE 
Prova: IBADE - Prefeitura de Vila Velha - Agente Comunitário de Saúde - 2024
O processo de formação da palavra “Transformação” é classificado como:        

A.derivação prefixal.
B.derivação sufixal.
C.derivação parassintética.
D.derivação imprópria.
E.derivação regressiva.

[bg_green]A palavra 'transformação' é formada por parassíntese a qual adiciona afixos simultâneos. Prefixal 'trans' + radical 'forma' + sufixo '-ção'[reset]
[blue] Porém, ao retirar os afixos, existem palavras existentes, irá depender da banca. Ex: 'formação' ( somente sufixo ) // 'transformar' ( somente prefixo )[reset]

33. A palavra “encaminhado”, que aparece no primeiro parágrafo do texto, é formada pelo processo denominado:

A.composição por justaposição.
B.composição por aglutinação.
C.derivação imprópria.
D.derivação parassintética.

 [bg_green]A derivação parassintética é o processo correto para a formação da palavra 'encaminhado'. [reset]
 [bg_green]Neste caso, a base 'caminho' recebe simultaneamente o prefixo 'en-' e o sufixo '-ado', formando uma nova palavra[reset]
 [yellow] Porém, existem outras palavras que podem ser formadas com prefixo: 'en-' + radical 'caminho' = 'encaminha' [reset]

34. Ano: 2024 // Banca: Instituto de Consultoria e Concursos - ITAME // Prova: ITAME - Prefeitura de Nova Glória - Coveiro - 2024
A palavra “infeliz” é formada pelo processo de derivação prefixal. O mesmo ocorre em:

A.Desfazer.
B.Felizmente.
C.Anoitecer.
D.Folhagem. 

[bg_green]A palavra 'desfazer' é formada pelo processo de derivação prefixal, onde o prefixo 'des-' é adicionado ao radical 'fazer',[reset]
 [bg_green]alterando seu sentido para o oposto.[reset]

[red]A palavra 'felizmente' é formada por derivação sufixal, onde o sufixo '-mente' é adicionado ao adjetivo 'feliz' para formar um advérbio[reset]

[red]A palavra 'anoitecer' é formada por derivação sufixal, onde o sufixo '-ecer' é adicionado ao substantivo 'noite' para formar um verbo.[reset]

[red]A palavra 'folhagem' é formada por derivação sufixal, onde o sufixo '-agem' é adicionado ao substantivo 'folha' para formar outro substantivo.[reset]

35.Ano: 2024 // Banca: Instituto de Apoio à Gestão e Educação - IGEDUC // Prova: IGEDUC - Câmara de Vitória de Santo Antão - Auxiliar de Serviços Gerais - 2024 

No que se refere à grafia, “porque” (sem acento) é um substantivo e tem o mesmo sentido de o motivo, a causa, a razão;
 já “porquê” (com acento) deve ser utilizado em respostas e para dar ideia de causa, justificativa ou finalidade.

C.Certo
E.Errado

'Porque' é uma conjunção causal ou explicativa, usada para introduzir a causa ou a razão de algo,
enquanto 'porquê' é um substantivo que significa 'a razão' ou 'o motivo'.
A confusão entre essas duas palavras é comum, pois elas são homófonas, ou seja, têm a mesma pronúncia, mas grafia e significados diferentes.

Para evitar confusões, é importante lembrar que 'porque' é usado em respostas e 'porquê', quando é substantivo, vem geralmente acompanhado de artigo, pronome ou adjetivo.

[red]Por que[reset]: [yellow]utilizado em perguntas. Exemplo: Por que não veio falar comigo?[reset]

[red]Porque[reset]: [yellow]utilizado em respostas. Exemplo: Eu não fui trabalhar porque perdi o ônibus.[reset]

[red]Por quê[reset]: [yellow]utilizado no fim das frases. Exemplo: Você já saiu da escola? Por quê?[reset]

[red]Porquê[reset]: [yellow]possui o valor de substantivo e indica o motivo, a razão. Exemplo: Gostaria de saber o porquê de sua mudança de opinião.[reset]

[red]Porque[reset]: [blue]é uma conjunção (eu tento substituir por : pois/ visto que/já que)[reset]

[red]Por que[reset]: [blue]é um pronome relativo/ interrogativo ( eu tento substituir por : pela qual(ais), por qual/ por qual motivo, por qual razão)[reset]

[red]Por quê[reset]: [blue]sempre vem antes de pontuação (., ?, !, ; ...)[reset]

O Porquê: é um substantivo ( eu substituo por: o motivo ou a razão)

36.Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Mato Leitão - Professor de Língua Portuguesa - 2024

Na frase “Ela não pôde comparecer à cerimônia, pois teve um compromisso importante; o porquê dessa ausência ainda não foi revelado.”, o uso de “porquê” (junto e com acento) justifica-se:

A.Porque se refere a um substantivo, indicando uma razão.
B.Por apresentar uma função coordenativa, podendo ser substituído por “pois”.
C.Por se tratar de um substantivo na frase, podendo ser substituído por “o qual”.
D.Porque traz um caráter subordinativo, usado para indicar motivo.

[blue]A forma 'porquê' é utilizada como substantivo, significando 'motivo' ou 'razão', e é precedida de artigo ou outro determinante.[reset]

[green]O item A está correto.[reset]
[bg_green]A forma 'porquê' é usada como substantivo, indicando uma razão ou motivo. Na frase,[reset]
[bg_green]'o porquê dessa ausência' pode ser substituído por 'a razão dessa ausência', confirmando que 'porquê' está sendo usado como substantivo.[reset]

[red]O item B está incorreto.[reset] [bg_red]A forma 'porquê' não apresenta uma função coordenativa e não pode ser substituída por 'pois'.
[bg_red] 'Porquê' é um substantivo e, neste contexto, não tem a função de conjunção explicativa.[reset]

[red]O item C está incorreto.[reset] [bg_red]Embora 'porquê' seja um substantivo, ele não pode ser substituído por 'o qual'.[reset] 
[bg_red]A substituição correta seria por 'a razão' ou 'o motivo'.[reset]

[red]O item D está incorreto.[reset] [bg_red]Porquê' não traz um caráter subordinativo e não é usado para indicar motivo de forma subordinativa. Ele é um substantivo que indica razão ou motivo, mas não funciona como uma conjunção subordinativa.[reset]


37. Ano: 2024 // Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC // Prova: FUNDATEC - Prefeitura de Jari - Agente Administrativo Escolar - 2024

No fragmento adaptado “Porque sou menina”, assinale a alternativa que apresenta a correta grafia do termo sublinhado caso a frase fosse uma pergunta.

A.Por quê.
B.Por que.
C.Porque.
D.Porquê.
E.Nenhuma das alternativas anteriores está correta.

[red]A forma 'Por quê' é utilizada no final de frases interrogativas diretas ou indiretas. [reset]
[red]Como a frase proposta não está no final, esta opção não está de acordo.[reset]

[green]A forma 'Por que' é utilizada no início de perguntas diretas ou indiretas, ou quando se pode subentender a expressão 'por qual razão'.[reset]
[green] Neste caso, a frase 'Porque sou menina' transformada em pergunta ficaria 'Por que sou menina?', o que está de acordo com o gabarito da banca.[reset]

[red]A forma 'Porque' é utilizada em respostas ou explicações, não em perguntas.[reset] 
[red]Portanto, esta opção não está de acordo com o gabarito da banca.[reset]

[red]A forma 'Porquê' é utilizada como substantivo, geralmente precedido de artigo, e não se aplica a perguntas. [reset]
 
38.Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Mato Leitão - Fiscal em Vigilância Sanitária - 2024

A alternativa em que há ERRO quanto ao emprego do porquê é:

A.Quero saber por que não aceitaram a explicação.
B.Por que o projeto foi interrompido?
C.Explique porque você brigou com sua irmã.
D.Eles não se inscreveram. Por quê?

[blue]A forma 'por que' está correta neste contexto, pois é usada em perguntas diretas ou indiretas, significando 'por qual razão'.[reset]

				A.Quero saber [yellow]por que[reset] não aceitaram a explicação.

[blue]A forma 'por que' está correta neste contexto, pois é usada em perguntas diretas, significando 'por qual razão'.[reset]

				B.[yellow]Por que[reset] o projeto foi interrompido?

[red]A forma 'porque' está incorreta neste contexto. Deveria ser usada a forma 'por que', pois a frase é uma pergunta indireta, significando 'por qual razão'. [reset]
			
            	A frase correta seria 'Explique [yellow]por que[reset] você brigou com sua irmã

[blue]A forma 'por quê' está correta neste contexto, pois é usada no final de frases interrogativas, significando 'por qual razão'.[reset]

						D.Eles não se inscreveram. [yellow]Por quê?[reset]
                        
                        
39. Ano: 2024 // Banca: Fundação Getúlio Vargas - FGV // Prova: FGV - Prefeitura de Caraguatatuba - PEB II - Português - 2024
Assinale a frase em que a grafia do porquê está incorreta.

A.Se os homens escalam montanhas só porque estão ali, [yellow]por que[reset] não lavam a louça?
B.Meus antepassados vagaram 40 dias pelo deserto, porque mesmo em tempos bíblicos os homens tinham vergonha de perguntar o caminho.
C.O porquê de tanta gente não conhecer a letra de nosso hino é a sua extensão e o seu vocabulário erudito.
D.Por que tanta gente deixa de votar em eleições importantes?
E.Os russos atacaram a Ucrânia por que?            


[bg_green]a. 'por que' separado é usado em início de perguntas e afirmações. Mesmo depois de vírgula ou ponto final.\n[reset]

						A.Se os homens escalam montanhas só porque estão ali, [yellow]por que[reset] não lavam a louça?
                        
                       
[bg_green]b.  A forma 'porque' junto é usada corretamente para indicar uma explicação ou causa. Pode ser substituido por 'pois'[reset]

	B.Meus antepassados vagaram 40 dias pelo deserto, [yellow]porque[reset] mesmo em tempos bíblicos os homens tinham vergonha de perguntar o caminho.


[bg_green]c. O 'porquê' junto e com acento significa que exige diretamente antes dele um artigo, numeral, adjetivo ou pronomes masculinos.[reset]\n
[bg_green]A forma 'porquê' é usada corretamente como um substantivo, indicando a razão ou o motivo de algo.[reset]

			C.O [yellow]porquê[reset] de tanta gente não conhecer a letra de nosso hino é a sua extensão e o seu vocabulário erudito.
                
                
[bg_green]d. 'por que' separado é usado em início de perguntas e afirmações. Mesmo depois de vírgula ou ponto final.[reset]

						D.[yellow]Por que[reset] tanta gente deixa de votar em eleições importantes?

[bg_red]e. 'por que' usado errado. O 'por quê', separado e com acento é usado no final do período composto ou simples em perguntas e afirmações. Também no sentido de 'por qual motivo' usado no final da oração....[reset]


									E.Os russos atacaram a Ucrânia [red]por que?[reset]
                                    
40. Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de São Ludgero - Auxiliar - Área: Escola - 2024 

Em relação ao emprego dos porquês, assinalar a alternativa CORRETA:

A.Caminho todos os dias porquê quero ser mais saudável.
B.Não entendo o porquê de tanta confusão.
C.Porque os gatos ronronam?
D.O trânsito está parado naquela rua. Alguém sabe por que?                                    

[green]a. Uso correto: PORQUE ( junto )[reset] // [blue]Sentido de explicação ou respostas, podendo ser substituido por 'pois'.[reset]

			A.Caminho todos os dias [yellow]porque[reset] quero ser mais saudável.
            
            
[green]B.Uso correto: PORQUÊ ( JUNTO E COM ACENTO ) [reset] // [blue]usado corretamente como um substantivo, significando 'o motivo pelo qual' e está precedido do artigo 'o'.[reset]

				Não entendo [yellow]o porquê[reset] de tanta confusão.
                                    
[red]c. Uso INCORRETO[reset] PORQUE junto e sem acento é sentido de explicação ou respostas, podendo ser substituido por 'pois'. [reset]                                   

			[bg_green]O correto seria 'por que' sem acento e separado. Perguntas e afirmações no início da frase.[reset]
            
									[yellow]Por que[reset] os gatos ronronam?


[red]d. Uso INCORRETO do 'por que'.[reset] 
O uso correto seria o 'por quê' separado com acento usado no final do período composto ou simples em perguntas e afirmações.
Também no sentido de 'por qual motivo' usado no final da oração....

				D.O trânsito está parado naquela rua. Alguém sabe [yellow]por quê?[reset]        

41.Assinalar a alternativa em que há emprego CORRETO do porquê:

A.Nunca entendi por que ela foi embora e não voltou mais.
B.Por quê você não me conta o que ocorreu na festa de ontem?
C.Eu não falo sobre aquele assunto com Roberta, por que poderia despertar um gatilho nela.
D.Quando chove muito não tem aula, porquê a sala tem muitas goteiras.                                            

[bg_green]Alternativa A está correta o uso do 'por que'.[reset]
[blue]A forma 'por que' é empregada corretamente em contextos de perguntas indiretas, como na frase apresentada.[reset]
[blue]Aqui, 'por que' introduz uma pergunta implícita, buscando uma explicação ou motivo[reset]

			A.Nunca entendi [yellow]por que[reset] ela foi embora e não voltou mais.
            
[bg_red]A alternativa B está INCORRETA o uso do por quê.[reset]
[blue] O correto seria o 'por que' separado sem acento. Pois está no início de uma pergunta direta.[reset]
[blue] O uso de 'por quê' com acento circunflexo é reservado para o final de frases interrogativas.[reset]             

			[yellow]Por que[reset] você não me conta o que ocorreu na festa de ontem?
            
[red]A alternativa C está incorreta o uso do 'por que' separado e sem acento.[reset]
[blue]'porque' é o correto, junto e sem acento para indicar a causa ou a razão de não falar sobre o assunto. Podendo ser substituido por 'pois'.[reset]

		Eu não falo sobre aquele assunto com Roberta, [yellow]porque[reset] poderia despertar um gatilho nela.

[red]Alternativa D o 'porquê' está errado.[reset] [blue]Pelo mesmo motivo da alternativa anterior. O uso correto seria 'porque' junto e sem acento. [reset]
[blue]Por indicar causa ou razão. Podendo ser substituido por 'pois'.[reset]


42. Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de São Ludgero - Procurador Jurídico - 2024 
Em conformidade com o adequado emprego dos porquês, assinalar a alternativa que preenche as lacunas abaixo CORRETAMENTE:

_____________ você está triste?
Ele abandonou a faculdade no último semestre, _____________?
Ela não quis sair com ele __________ não quer um relacionamento agora.

A.Por quê | por quê | porque
B.Por que | por quê | porque
C.Por que | por que | porquê
D.Por quê | por que | porquê

[blue]Por que você está triste?[reset]  Uso do 'por que' separado e sem acento para início de pergunta ou afirmação.\n
	[bg_green]Lembrando também que ser serve para como uma pergunta indireta, implícita buscando explicação ou motivo.[reset]
    
[blue]Ele abandonou a faculdade no último semestre, por quê?[reset]  O uso do 'por quê' separado e com acento é no final de oração.   \n
		[bg_green]Com o sentido de 'por qual motivo?' no final de oração. Podendo ser utilizado antes de vírgula no meio da oração também.[reset]
        
[blue]Ela não quis sair com ele porque não quer um relacionamento agora.[reset] O uso do 'porque' junto e sem acento é correto em explicações.   
		[bg_green]Podendo assim sendo ser substituido por 'pois', para explicação de uma resposta a uma pergunta.[reset]
        
        [bg_green]Alternativa B a correta.[reset]
        
43.Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Travesseiro - Professor - Área: Educação Especial I - 2024

O ERRO no emprego do porquê está na alternativa:

A.Por que você chegou atrasado hoje?
B.Preciso descobrir o porquê desse sorriso radiante.
C.Você brigou com seu namorado, por quê?
D.Ele reclamou, porquê se preocupa com você.        

[bg_green]O uso do 'por que' separado e sem acento na afirmativa A está correto.[reset] [blue]Para início de pergunta ou afirmação de algo.[reset]\n
	[yellow]Lembrando também que serve como pergunta indireta, implícita buscando explicação ou motivo dentro do contexto.[reset]
    
[bg_green]O uso do 'porquê' junto e com acento na afirmativa B está correto.[reset] [blue]Está funcionando como um substantivo, acompanhado do artigo em questão.[reset]

[bg_green]O uso do 'por quê' separado e com acento está correto na afirmativa C.[reset] [blue]O 'por quê' separado e com acento usado em final de período em perguntas ou afirmações.[reset]\n
		[blue]Também pode ser substituido por 'por qual motivo'.[reset]
        
[red]O erro está na afirmativa D.[reset][bg_red] O uso do 'porquê' junto e com acento funciona como substantivo e precisa estar sendo acompanhado.[reset]
	[blue]O 'porque' correto seria sem acento e junto para uma explicação ou resposta e pode ser substituido por 'pois'.[reset]
    
    
44.Ano: 2024 / Banca: Fundação de Cultura e Apoio ao Ensino Pesquisa e Extensão - FUNCEPE / Prova: FUNCEPE - Câmara de Caucaia - Analista Legislativo - Área Direito - 2024 

É proibido grudar chiclete na juba do leão.
_____________ eu faria isso?
_____________ é proibido.
hmmmm

As formas que preenchem respectiva e adequadamente as lacunas do texto são:


A.Por quê | Por que
B.Por que | Porque
C.Por quê | Porquê
D.Porque  | Por que
E.Por que | Porquê

[blue]O 'por que' correto seria o separado sem acento. Para início de conversas. Além de perguntas indiretas, implícita, buscando uma explicação ou motivo.[reset]
[blue] Para a segunda lacuna o porque correto seria o junto e sem acento com o sentido de explicação ou respondendo algo na frase. [reset]

45.Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Senador Salgado Filho - Analista Ambiental - 2024 

Sobre o emprego dos porquês, assinalar a alternativa que preenche as lacunas abaixo CORRETAMENTE.

Não compreendo o _________ de ele ter ido embora tão cedo.
Ora, _________ você não gosta de maracujá?  A criança chorou _________ estava com dor.
O jornaleiro passou mais cedo _________?

A.porque  | por quê | por que | porquê
B.por que | porque  | porquê  | por quê
C.por quê | por que | porque  | porquê
D.porquê  | por que | porque  | por quê

Não compreendo o [yellow] porquê [reset] de ele ter ido embora tão cedo. ( 'porquê' junto e com acento funciona como substantivo na oração. Lembrando que tem um artigo preposto )

Ora, [yellow]por que[reset] você não gosta de maracujá? ( 'por que' separado e sem acento para perguntas iniciais buscando uma explicação ou motivo )

A criança chorou [yellow]porque[reset] estava com dor. ( 'porque' junto e sem acento para explicações ou respostas, podendo ser substituido por 'pois')

O jornaleiro passou mais cedo [yellow]por quê[reset]? ( 'por quê separado e com acento usado para final de frase com perguntas, podendo ser substituido 'por qual motivo' )


46. Complete a frase adequadamente:

“Resta ainda descobrir o __________ dessas declarações.

A.porque
B.por quê
C.por que
D.porquê

Existe um artigo que pode acompanhar o substantivo na oração. O único porquê que pode ser substantivado é o junto com acento. 
Alternativa D

47.Ano: 2024 // Banca: Objetiva Concursos // Prova: Objetiva Concursos - Prefeitura de Canguçu - Auxiliar em Saúde Bucal - 2024 
Observar a fala de alguns internautas nas redes sociais:

∙ Paulo: Se sou inteligente, não poderia entender este por quê?

∙ Pedro: Sem uma resposta satisfatória, jamais compreenderia porquê.

∙ Maria: Porque eu te acho bonito, serás recompensado?

Considerando o emprego dos “porquês”, houve ERRO na(s) fala(s) de:

A. Paulo.
B. Pedro.
C. Paulo e Pedro.
D. Paulo, Pedro e Maria

[blue]Na frase de Paulo temos o pronome 'este' acompanhando o substantivo 'porquê' só que junto.[reset] [bg_red]Na frase está separado. ERRADO[reset]
[green]Poderia estar correto com o 'por que' ( separado e sem acento ),[reset] logo após a vírgula temos uma pergunta indireta, buscando uma explicação.
							[bg_green]Podendo ser assim, nem sempre somente no início da frase.[reset]

Para que a frase de Pedro o correto seria estar acompanhado de um pronome, numeral ou artigo. [bg_red]ERRADO[reset]
	Poderia estar correto com o [yellow]'por que' (separado e sem acento)[reset], [blue]por uma razão ou motivo em uma frase não interrogativa.[reset]
Configurando uma oração subordinada substantiva objetiva direta. Segundo Bechara em Moderna Gramática Portuguesa, o uso de 'por que' é o correto neste contexto.

A única frase correta é de Maria. 'porque' junto e se acento para início de pergunta, explicando ou respondendo. Podendo ser substituido por 'pois'. [bg_green] CORRETO [reset]

[bg_green]Alternativa C [reset]

48.Ano: 2024 /  Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - Prefeitura de Santo André - Auxiliar Administrativo II - 2024 

No trecho “No dia seguinte, o administrador da fazenda perguntou para meu tio Paulo por que os americanos não tinham ido na lua cheia” (último parágrafo), a expressão destacada foi corretamente empregada assim como em:

A.Os americanos tiveram sucesso na missão [yellow]por que[reset] investiram uma quantia considerável no programa espacial.

B. Os Estados Unidos propagandearam o feito que haviam conquistado [yellow]por que[reset] estavam competindo com os soviéticos.

C. É difícil para muitos entender [yellow]por que[reset] era tão importante para os Estados Unidos levar um ser humano à Lua.

D. Animais eram enviados para o espaço [yellow]por que[reset] os cientistas deveriam fazer os devidos testes antes de enviar humanos.

E. [yellow]Por que[reset] havia uma necessidade de mostrar poder, a corrida espacial foi uma disputa acirrada e dura até os dias de hoje.

Na alternativa 'A' - A frase não é uma pergunta, portanto, a expressão correta seria 'porque', que é usada para responder perguntas ou explicar algo.\n
							Na mesma frase cabe uma conjunção explicativa ou causal logo usa-se "porque".
                            
Na alternativa 'B' - A frase não é uma pergunta, portanto, a expressão correta seria 'porque', que é usada para responder perguntas ou explicar algo.
							Na mesma frase cabe uma conjunção explicativa ou causal logo usa-se "porque".
                            
[bg_green]Na alternativa 'C'- expressão 'por que' é usada corretamente em uma pergunta indireta, cabendo uma razão ou motivo logo após o 'por que'.[reset]                            

Na alternativa 'D' - a expressão 'por que' é usada de forma incorreta. A frase não é uma pergunta, portanto, a expressão correta seria 'porque', que é usada para responder perguntas ou explicar algo.
							Na mesma frase cabe uma conjunção explicativa ou causal logo usa-se "porque".
                            
Na alternativa 'E' - A frase não é uma pergunta, portanto, a expressão correta seria 'porque', que é usada para responder perguntas ou explicar algo.
							Na mesma frase cabe uma conjunção explicativa ou causal logo usa-se "porque".
                            
49. Ano: 2024 / Banca: GUALIMP Assessoria e Consultoria Ltda - GUALIMP / Prova: GUALIMP - Prefeitura de Alfredo Chaves - Enfermeiro - 2024

Indique a alternativa em que o uso do porquê está correto, de acordo com as regras da norma padrão:

A.Está chateada porquê?
B.Acabei comprando um notebook porque era mais barato.
C.Não entendi o por quê de você não querer ir.
D.Porque você não pode me ajudar?                            

[red]Para que a alternativa 'A' estivesse correta teria que ser 'por quê' separado e com acento. Usa-se no final de frase, tendo o sentido de 'por qual motivo'...[reset]
                            
				Está chateada [yellow]por quê?[reset]  <- [bg_green] CORRETO [reset]

[bg_green]Alternativa 'B' CORRETA[reset] -> [blue]Sentido de explicação, resposta. Podendo ser substituido por 'pois'. É uma conjunção explicativa ou causal.[reset]                                

				Acabei comprando um notebook [yellow]porque[reset] era mais barato.

[red]Na alternativa 'C' o uso do 'porquê' deve ser junto, pois é um substantivo.[reset]

				Não intendi [yellow]o porquê[reset] de você não querer ir.
                
[red]Na alternativa 'D' o correto seria 'por que' separado e sem acento, para início de perguntas.[reset]

				[yellow]Por que[reset] você não pode me ajudar?

50. Ano: 2024 / Banca: MB Gestão Pública Ltda. EPP - MAXIMA Auditoria / Prova: MAXIMA Auditoria - Serviço Autônomo de Água e Esgoto de Baixo Guandu - Auxiliar Administrativo - 2024

"E se o piso não tem arranhão, é porque ali ninguém dança."
 Analisando a palavra destacada nesse trecho, sabe-se que ela possui mais de uma forma de escrita, de acordo com o contexto. 
 Das alternativas a seguir, aquela que utilizou da mesma forma da escrita, indevidamente, através de uma pergunta indireta, conforme o que rege, quanto a redação oficial, a ortografia é:

A.Tudo foi resolvido, porque não se tocam mais no assunto.
B.Farei o possível, porque pretendo deixar uma boa imagem.
C.Ela não disse porque ainda não informaram os relatórios referentes à produtividade.
D.Eles viajaram, porque estão todas as janelas trancadas.        


[bg_green]Alternativa 'A' uso CORRETO do 'porque' para uma explicação.[reset] Podendo ser substituido por 'pois', não mudaria o sentido.
						[blue]Além disso, esse 'porque' trata-se de uma conjunção explicativa.[reset]
                        
[bg_green]Alternativa B uso CORRETO do 'porque' para uma explicação/ resposta de algo após uma pergunta.[reset] Podendo ser susbtituido por 'pois', não mudaria o sentido.                      
						[blue]Além disso, esse 'porque' trata-se de uma conjunção explicativa.[reset]

[bg_red]Alternativa 'C' uso INCORRETO. Teria que ser separado, 'por que', pois se trata de uma pergunta indireta.[reset]  

[bg_green]Na alternativa 'D' o uso do 'porque' está CORRETO.[reset] Para uma explicação, podendo ser substituido por 'pois' sem alteração no sentido.
						[blue]Além disso, esse 'porque' trata-se de uma conjunção explicativa.[reset]
                        
51.Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura do Município de Valinhos - Professor I - 2024 

Analise as sentenças a seguir e assinale a alternativa em que a palavra “porquê” foi empregada corretamente.

A. A festa foi cancelada porquê a anfitriã está doente.
B. Porquê todas as coisas são belas é que temos motivos para sorrir.
C. A polícia conseguiu desvendar o crime. Resta apenas uma dúvida: porquê?
D. Não se sabe o porquê do sumiço da aluna.
E. Eu sei bem porquê você está mentindo.                        

[red]O uso do 'porquê' na alternativa 'A' está incorreto![reset]\n

[blue] O 'porque' correto seria junto e sem acento. Uma conjunção explicativa, podendo ser substituida por 'pois' que não mudaria o sentido.[reset]

[bg_red]'porquê' para início de frase com acento está ERRADO.[reset] [blue]O correto seria o 'porque' junto e sem acento para uma explicação ( conjunção explicativa ).[reset]
			[bg_red]Portanto, alterantiva 'B' ERRADA[reset]

[yellow]A alternativa C poderia estar correta com o uso do artigo para acompanhar o substantivo 'o porquê'.[reset]

		 [blue]Caso não, teria que ser separado.[reset] 'por quê' [red]( por qual motivo , usado também em final de frases interrogativas )[reset]

[bg_green]Alternativa D - Uso correto do substantivo 'porquê' com o artigo anteposto acompanhando-o.[reset]

[red]Alternativa 'E' - Faltaria o artigo ou pronome para acompanhar o substantivo 'porquê'.[reset]
	[blue]Caso não, o correto seria 'por que' junto e sem acento para justificar a frase em questão.[reset]
			[yellow]O correto seria ou 'o porquê' ou 'por que' como uma afirmação com sentido de explicação[reset]
            
52.Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Vila Boa - Controlador Interno - 2024 

Sobre o emprego dos porquês, assinalar a alternativa que preenche as lacunas CORRETAMENTE.

● Não fui à aula _______ estava chovendo muito.

● Procure saber _______ há tanto movimento nas ruas.

● Afinal, não se sabe bem o _______ das coisas.

● Eles vivem brigando, mas _______?

A.porque  | porque  | por quê | porquê
B.porque  | por que | porquê  | por quê
C.por quê | porquê  | por que | porque
D.porquê  | por quê | porque  | por que

	Não fui à aula [yellow]porque[reset estava chovendo muito.] [blue]Uso correto para uma explicação, trata-se de uma conjunção causal.[reset]
    
	Procure saber [yellow] por que [reset] há tanto movimento nas ruas. [blue]Uso correto buscando uma razão ou motivo em uma frase não interrogativa.[reset]

	Afinal, não se sabe bem [yellow]o porquê[reset] das coisas. [blue]Uso correto para substantivo.[reset]
    
    Eles vivem brigando, mas [yellow]por quê[reset]? Uso correto da palavra usado em final de frase. [blue]Podendo ser substituido por 'por qual motivo?'[reset]

[bg_green]alternativa correta 'B'[reset]

53.Ano: 2024 / Banca: MB Gestão Pública Ltda. EPP - MAXIMA Auditoria / Prova: MAXIMA Auditoria - Prefeitura de São João de Manteninha - Motorista de Educação Básica - 2024

“Por que alguns animais marinhos comem lixo?” Assinale a frase em que o emprego do “por que” deve ser o mesmo do destacado no trecho acima.

A.Não sei ________ eles não se reuniram no último final de semana.
B.Não trouxeram o material _________ não sabiam quais eram.
C.Você não quis participar da reunião _______?
D.Não sei o _________ de tanta reclamação.

								Não sei [yellow]por que[reset] eles não se reuniram no último final de semana.\n
			 		[blue]Oração em que o uso da palavra 'por que' está correto. Além de ser usado em início de frase.[reset]
							[blue]Também pode ser usado em frases em busca de uma razão ou motivo não interrogativo [reset]
                            	[yellow]Configurando uma oração subordinada substantiva objetiva direta[reset]
                                
						Não trouxeram o material [yellow]porque[reset] não sabia quais eram. z\n                               
							Uso correto junto e sem acento com o sentido de explicação, podendo ser substituido por 'pois'[reset]
                            			Além disso, é uma conjunção causal[reset]

                                        Você não quis participar da reunião [yellow]por quê[reset]?\n                                        
                                        [blue]Para uso no final de frase coloca-se separado e com acento[reset]
											[yellow]Podendo substituir por 'por qual motivo?'[reset]
                                            
                                            Não sei [yellow]o porquê[reset] de tanta reclamação.\n
                               	[blue]Usado como substantivo na oração indicando o motivo e ou a razão.[reset]
                                   
54.Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Guaraniaçu - Assistente Administrativo - 2024 
Em qual alternativa o uso do porquê está INCORRETO?

A.Levou um tapa e não entendeu por quê!
B.Reagimos mal porque fomos pegos de surpresa.
C.Terminei o relacionamento, e ele sabe por quê.
D.Corro por que é saudável e meu médico disse que é bom.                                   

[green]Na alternativa 'A' o uso está correto.[reset] 'por quê' para final de frase. Usa-se antes de sinais de pontuação.

[green]Na alternativa 'B' usado com sentido de explicação, pode-se usar 'pois'. 'porque' no caso é conjunção causal.[reset]

[green]Na alternativa 'C' uso correto da palavra. Final de frase.[reset]

[red]Na alternativa 'D' uso incorreto do 'por que' separado sem acento pelo sentido que a frase leva.[reset]
 			[blue]O correto seria junto 'porque' trazendo uma conjunção causal com sentido explicativo. [reset]
    [red]O 'por que' separado e sem acento tras outra ideia uma busca por explicação uma razão em uma frase não interrogativa.[reset]

55. Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Mato Leitão - Agente de Combate às Endemias - 2024

Qual alternativa apresenta o uso do porquê CORRETAMENTE?

A.Porque você não quis participar da pesquisa?
B.Gostaria de saber o porquê de você ter faltado à aula.
C.Eu não irei viajar por quê estou estudando.
D.Você fechou a loja mais cedo. Porque?    

[red]Na alternativa 'A' o uso está INCORRETO.[reset] [blue]O certo é 'por que' separado para inicio de pergunta.[reset]

[green]Na alternativa 'B' o uso está correto.[reset] [blue]'o porquê' junto com acento é substantivo com o artigo acompanhando.[reset]

[red]Na alternativa 'C' o uso da palavra está ERRADO.[reset] [blue]'por quê' separado e com acento é para final de frase ou após sinal de pontuação.[reset]

[red]Na alternativa 'D' o usdo da palavra está INCORRETO.[reset] [blue]O correto seria 'por quê' SEPARADO e COM ACENTO. Logo após sinal de pontuação e final de frase;[reset]

56.Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC / Prova: IBFC - TRF 5 - Analista Judiciário - Área: Administrativa - 2024 

Na passagem “Sim, por que não na Suíça?” (4º§), ocorre o emprego de uma das formas do “porquê”. Assinale a alternativa cuja lacuna deveria ser preenchida por essa mesma forma.

A.O motivo ______ trabalho é que desejo organizar minha vida.
B.Faltou o evento administrativo e não explicou ______.
C.Chegou atrasado ao compromisso ______ confundiu o horário.
D.Deve haver algum ______ para essa transferência ter ocorrido.    

[bg_green]Alternativa 'A' a CORRETA pelo gabarito.[reset] [blue]O uso do 'por que' em busca de uma explicação ou motivo em uma frase não interrogativa.[reset]
							[yellow]Assim também usado como uma pergunta direta inicial[reset]
                            
A alternativa 'B' usa-se 'o porquê' como substantivo na oração.\n
A alternativa 'C' usa-se o 'porque' junto para uma explicação, é uma conjunção causal.\n
[bg_green]A alternativa 'D' usa-se o mesmo do gabarito da alternativa 'A', buscando uma explicação ou motivo em uma frase não interrogativa.\n[reset]
	[bg_red] Mas a banca considerou a alternativa 'A'[reset]

56.Ano: 2024 / Banca: LJ Assessoria e Planejamento Administrativo Limitada - LJ / Prova: LJ - Câmara de Turilândia - Vigia - 2024 

O uso do “porque” está INCORRETO em:

A.Fiz isso porque precisava.
B.Porque você foi embora?
C.Porque ela estudou bastante, passou na prova.
D.Não responda sua mãe, porque ela está com a razão.
E.Não fui ao trabalho hoje, porque estou doente.    

Na alternativa 'A' o uso do 'porque' está correto. Uma explicação, funciona como uma conjunção explicativa/causal.\n
[bg_green]Na alternativa 'B' o uso está INCORRETO e é o gabarito da questão. O uso correto seria separado 'por que', para inicio de pergunta direta.\n[reset]
Na alternativa 'C' o uso está CORRETO. Conjunção explicativa. porque junto\n
Na alternativa 'D' o uso está CORRETO. Conjunção explicativa. porque junto\n
Na alternativa 'E' o uso está CORRETO. Conjunção explicativa. porque junto\n

57. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de São José dos Campos - Técnico Tributário - 2024

Assinale a frase em que a grafia do “porquê” está correta.

A.Você certamente sabe por que acreditar num deus.
B.Gostaria de saber porque as pessoas boas dormem melhor à noite do que as pessoas más.
C.Muita luz também é ruim por que não deixa ver.
D.Amaria saber por quê não acreditar em Deus.
E.Deus criou o homem porquê ficou desapontado com o macaco.    

Na alternativa 'A' é uma frase interrogativa indireta, indicando uma busca pelo motivo ou razão de que se deve acreditar em Deus.
		Uso correto do 'por que'

Na alternativa 'B' é uma frase interrogativa indireta bucando um motivo de saber pela qual as pessoas dormem melhor. 
		Portanto usdo INCORRETO da palavra, deveria ser separado 'por que'.
        
Na alternativa 'C' é uma explicação da causa ou motivo do contexto. é umma conjunção causal, portanto é 'porque' junto.        

Na alternativa 'D' a palavra está INCORRETA. A frase indica uma pergunta INDIRETA, portanto é 'por que', separado. Procurando uma razão...

Na alternativa 'E' o uso está incorreto. O correto seria uma conjunção explicativa 'porque' junto. Explicando a causa ou motivo.     

58. Ano: 2024 / Banca: Instituto de Desenvolvimento Social e Tecnologia - IDESG / Prova: IDESG - Prefeitura de Varre-Sai - Enfermeiro - 2024

Considere a seguinte hipótese de afirmação baseada no texto: Os cientistas estão interessados na descoberta ______ ela pode indicar a presença de água em Marte.

Qual alternativa preenche, corretamente, a lacuna?

A.por quê.
B.porquê.
C.por que.
D.porque.


		[yellow]A forma 'porque' junto é uma conjunção explicativa ou causal, utilizada para introduzir uma explicação ou causa.[reset]
[yellow]No contexto da frase, 'porque' é a forma correta, pois introduz a explicação de por que os cientistas estão interessados na descoberta.[reset]

59. Ano: 2024 / Banca: Universidade de Blumenau - FURB / Prova: FURB - Floram - Fiscal de Meio Ambiente - 2024

Analise as sentenças a seguir:

I.Por quê o biodiesel é considerado uma alternativa promissora aos combustíveis fósseis?

II.Você já se perguntou por quê o biodiesel é uma opção tão viável para reduzir as emissões de gases poluentes?

III.O porquê do crescimento do biodiesel como alternativa energética está relacionado à sua menor emissão de gases poluentes em comparação aos combustíveis fósseis.

IV.As políticas ambientais estão promovendo o uso de biodiesel por que ele é uma fonte de energia renovável e menos poluente que os combustíveis fósseis.

V.A produção do biodiesel está aumentando porque há uma crescente demanda por fontes de energia mais limpas e renováveis.

Está correto o emprego dos "porquês" em:

A.I, II e IV, apenas.
B.I e II, apenas.
C.III, IV e V, apenas.
D.I, II, III, IV e V.
E.III e V, apenas.

[red]O item I está incorreto no uso da palavra.[reset] [yellow]O correto seria 'por que' separado sem acento usado para inicio de perguntas.[reset]
[red]O item II está incorreta no uso da palavra.[reset] [yellow]O correto seria 'por que' separado e sem aceto também usado em perguntas indiretas buscando uma razão/motivo para uma explicação.[reset]
[green]O item III o uso da palavra está CORRETO.[reset] [blue]'porquê' junto e com acento acompanhado de um artigo.[reset]
[red]O item IV o uso está incorreto. [reset] [yellow]O correto seria 'porque' junto porque se trata de uma conjunção explicativa, afirmando o motivo da qual ocorreu.[reset]
[green]O item V o uso da palavra está correto.[reset] [blue]'porque' junto e sem acento é conjunção explicativa. Explicando o motivo da qual ocorreu o fato.[reset]

[bg_green]Gabarito então é: 'E' Item III e V, apenas.[reset]

60. Em relação ao uso correto dos porquês, relacionar as colunas e assinalar a alternativa correspondente.

(1) Por que.
(2) Porquê.
(3) Por quê.
(4) Porque.

( ) Tem valor de substantivo.

( ) Usado no final de sentenças. Pode ser substituído por “por qual razão”.

( ) Usado em perguntas. Pode ser substituído por “por qual motivo”.

( ) Usado em respostas.

A.4 - 1 - 2 - 3.
B.2 - 3 - 4 - 1.
C.3 - 4 - 1 - 2.
D.2 - 3 - 1 - 4.

O 'porquê' junto é usado como substantivo sempre que acompanhado de pronome, numeral, artigo. ( 2 )\n
'Por quê' separado e com acento é usado em final de sentenças e pode ser substituido por 'por qual razão' ( 3 )\n
'por que' separado e sem acento é usado em perguntas diretas e indiretas e pode ser substituido por 'por qual motivo' ( 1 )\n
'porque' junto e sem acento é usado em respostas para explicar motivos e razões afirmativas. ( 4 )
            '''

    def mas_mais (self):
        return '''MAS/MÁS/MAIS:

	Emprega-se MÁS como adjetivo oposto a 'boas':

		Existem pessoas boas e pessoas [yellow]más.[reset]

		Até que ele não tem [yellow]más[reset] qualidades.

		[yellow] 'más'[reset] -> [blue] adjetivo para o substantivo 'qualidades'.[reset]

		Eles tem atitudes [yellow]más.[reset] [red] Do contrário seria 'boas qualidades' [reset]

		[yellow] 'más'[reset] -> [blue] adjetivo que qualifica o substantivo 'atitudes'.[reset]


        Emprego do MAS::

	O 'mas' é uma conjunção adversativa que indica oposição, contraste. Pode ser substituida por outra conjunção adversativa.
			[blue]( porém, contudo, todavia, entretanto )[reset]

			Eu iria ao cinema, [yellow]mas[reset] choveu.

			[yellow]'mas'[reset] -> [blue]conjunção adversativa[reset]
		
[bg_red] 'MÁS' É MONOSSÍLABO TÔNICO, SENTIDO PRÓPRIO [reset]						

Emprego do MAIS:

	'mais' pode ser um advérbio de intensidade ou um pronome indefinido. [bg_red]é antônimo de 'menos'.[reset]

	Sem dúvida, é a garota [yellow]mais[reset] simpática da sala! <- [blue] Advérbio de intensidade [reset]

	Atualmente, tenho [yellow]mais[reset] sabedoria e [yellow] mais[reset] conhecimento. <- [blue] Advérbio de intensidade.[reset]
    '''
    def ha_a(self):
        return '''Emprego do HÁ / A 

	Há ( do verbo haver ) para indicar tempo passado ou para significar existência.

		[yellow]Há[reset] dois meses, ele não aparece.

		No mundo, [yellow]há[reset] muitos fãs de futebol.

    Emprego do 'A':

		Preposição que indica tempo futuro e distância;

		Ex:

			Daqui [yellow]a[reset] dois meses, ele aparecerá.

			A Terra fica [yellow]a[reset] milhões de quilômetros do Sol.
            '''           
    def afim_de(self):
        return '''AFIM DE / AFIM


                [red]'A fim de'[reset]; separado tem o sentido de finalidade, com objetivo.

	                Estudou [yellow]a fim de[reset] acertar mais questões na prova.			

                    [red]'Afim'[reset]; junto tem o sentido de semelhança, afinidade.

	                Fizemos redações parecidas: eram temas [yellow]afins.[reset] [blue]( temas semelhantes )[reset]


                    	[bg_red] ALERTA! [reset]

                		Uso informal no sentido de ter interesse ou vontade ( escrita separada )

			                Joaquim estava [yellow]a fim[reset] de Ana.

		                    Hoje estamos [yellow]a fim[reset] de um sorvete.
                            '''    

    def mal_mau(self):
        return '''MAL /  MAU

	Mal com 'l' é o oposto de 'bem'. Também é substantivo e advérbio de modo.

		A bebida pode fazer muitos [yellow]males.[reset] [blue]( no plural de substantivo )[reset]

		Evite seguie o caminho do [yellow]mal.[reset] [blue] O caminho do bem [reset] [red] Substantivo [reset]

		Por favor, não me entenda [yellow]mal[reset] [blue] entenda-me bem [reset] [red] Advérbio de modo [reset]

		Era um menino [yellow]mal[reset]-educado (bem-educado) advérbio de modo

		Ele não sabe o [yellow]mal[reset] que me faz. [blue] Substantivo [reset]

		Ele se comportou [yellow] mal.[reset] [blue] advérbio de modo [reset]

		[yellow]Mal[reset] o professor chegou, todos calaram. [blue] Conjunção temporal [reset]

[bg_yellow]Usa-se o MAU com 'u' para adjetivo, qualificação. Referindo-se ao substantivo.[reset]

        	Estamos de [yellow]mau[reset] [blue]humor[reset] hoje. 

	                [blue]'humor'[reset] -> substantivo
	                [yellow]'mau'[reset] -> adjetivo
		
	                Quando faço alguém chorar, isso é [yellow]mau.[reset] 	

	                    'mau' -> 'bom'

	                Escolheu um [yellow] mau [reset] momento.

	                [blue]'mau'  -> Adjetivo para o substantivo 'momento'[reset]

	                    Era um [yellow]mau[reset] aluno.

	                    [blue] 'mau' -> Adjetivo para o substantivo 'aluno'


                        		[bg_red] ALERTA! [reset]

            			Usar 'mau' como substantivo derivado do adjetivo 'mau':

			        	Não se importe com o sucesso [yellow]dos maus.[reset]

			        [yellow]'dos maus'[reset] -> [red]derivação imprópria do adjetivo por substantivo, lembrando que temos 'de' preposição + 'os' artigo.[reset]
'''
    def hifen(self):
        return '''Emprego do hífen - Marcio Wesley

	Usado na ênclise ( quando o pronome vem após o verbo ) e na mesóclise (pronome antes do verbo)

		diga-[yellow]me[reset] <- após o verbo ( ênclise )
		esqueci-[yellow]me[reset] <- após o verbo (ênclise)
		esquecer-te-ei <- após oo verbo 
		di-lo-ia <- após o verbo

	Usado em palavras compostas:

		-> Nas nacionalidades e gentílicos( adjetivos que indicam a origem ) em geral:
				
				- norte-americano ( duas palavras, composição, uso do hífen )
				- sul-africano ( duas palavras, composição, uso do hífen )
				- são-caetanense-do-sul ( três palavras, composição, uso do hífen ) <- gentílico -> 'do sul'
				- mato-grossense-do-sul ( três palavras, composição, uso do hífen ) <- gentílico -> 'do sul'

		-> Nos nomes de espécies minerais, animais e vegetais:

			pedra-sabão <- espécie mineral
			veado-galheiro <- espécie animal
			mão-de-vaca <- espécie animal (pata-de-vaca)
			pimenta-de-cheiro <- espécie vegetal
			elefante-marinho  <- espécie animal

		-> Compostos: dois substantivos sendo que o segundo identificando o primeiro. 'salário-família'
			
				verde-amarelo <- dois adjetivos combinados
		
				verde-claro <- dois adjetivos combinados
	
				garoto-propaganda -> substantivo 'propaganda' especificando o 'garoto' , outro substantivo.

				asa-delta -> segundo substantivo especificando o primeiro.
		
				cor-de-rosa -> manteve o hífen.

De acordo com a nova ortografia o hífen desaparece nos compostos com os termos unidos por preposição.

		Mão de obra // Faz de conta // Pé de moleque // Pé de cabra // Mão de vaca(o sovina) // Mão de ferro

Hífen com prefixos:

	Sempre com hífen entre vogais e consoantes iguais:

		micro-ondas <- repare que a letra 'o' de 'micro' e a outra letra 'o' de 'ondas' usa-se hífen para separá-las.
	
		anti-inflamatório <- repare a vogal 'i' do prefixo 'anti' e a mesma letra 'i' de 'inflamatório', deve-se separar com hífen.

		hiper-realidade <- repare a consoate 'r' do prefixo 'hiper' e a mesma letra 'i' de 'realidade', deve-se separar com hífen.

		contra-ataque <- repare que a vogal 'a' do prefixo 'contra' é a mesma letra 'a' da 'ataque', deve-se separar com hífen.

	Sempre com hífen antes de palavras iniciadas com a letra 'h' para prefixos:

		super-herói // sub-hepático // hiper-hidrose // bem-humorado

	Junto SEM hífen entre letras diferentes para prefixos:

		microestrutura // semiárido // supermercado // hipersensibilidade // subseção // subdiretor // suboficial // subtenente 


	[bg_red] Duplica a letra entre vogais as letras consoantes 'r' e 's' para prefixos:[reset]

			contrarregra // contrassenso


	[bg_red] Atenção! [reset]

		O elemento de composição 'geral' como sufixo sempre usa hífen:

		Procurador-geral // coordenação-geral // advogado-geral // controladoria-geral // diretor-geral

	O prefixo 'SUB' terá hífen sempre diante das letras 'b', 'h' e 'r':

		sub-base // sub-hepático // sub-rogar // sub-região

	Fica sem hífen:

		paraquedista // paraquedismo // paraquedas // parapeito // mandachuva // paramédico // paramilitar // paranormal // paraolimpíada

	Manteve o hífen de acordo com a nova regra ortografica:

			para-sol // para-raios // para-fogo // para-lama // para-luz // para-brisa

PRÉFIXOS QUE SEMPRE HAVERÃO HÍFEN:

	recém : recém-nascido // recém-casado
	além  : além-mar
	pré   : pré-requisito // pré-escola
	pós   : pós-graduação // pós-operatório
	grão  : grão-mestre
	aquém : aquém-mar
	ex    : ex-esposa // ex-prefeito
	vice  : vice-presidente // ex-vice-presidente
	bem   : bem-estar // bem-vindo // bem-sucedido

		[bg_yellow] Prefixos que tem acento sempre haverá hífen [reset]

[bg_red] Atenção REDOBRADA [reset]

	prefixos que não usam hífen:

	CO : cooperar // correlação // coabitar (habitar)// cosseno // coerdeiro (herdeiro)
			
			[red]Mesmo que a palavra original com 'h' usa-se hífen, mas o prefixo 'CO' não utiliza.[reset]

	RE : reedição // reexaminar // reorganizar

	[bg_green]O prefixo utiliza-se a regra normal de vogais e consoantes TELE:  teleconferência //  tele-entrega // teletrabalho // televendas [reset]

(SEE/AL) Na palavra 'artista-docente', para maior clareza gráfica, caso o hífen da translineação coincidisse, na partição da sílaba ao final da linha,
com o hífen da translineação coincidisse, na partição da sílaba ao final da linha, com o hífen integrante da palavra composta, seria gramaticalmente
correto repeti-lo, no início da linha subsequente, da forma a seguir: artista -/- docente.

	[bg_green] CORRETO [reset]

IFB - O autor usou o hífen com efeitos distintos nos seguintes casos: em 'conhecimentos-conteúdos-acumulados', foi criado um vocábulo por três palavras,
o que conota amontoado, acúmulo; já em 're-forma', o hífen atribui ênfase ao sentido do prefixo 're-' aposto à forma verbal 'forma'.

	[bg_green] CORRETO [reset]

	[bg_yellow] Sabemos que sempre tem hífen para o prefixo 'bem'. Porém para a palavra 'mal' é usada somente antes da letra 'h' e de vogais![reset]

		malmequer // malvisto // mal-estar (antes de vogal) // malsucedido // mal-humorado (antes de h) // malcasado // maldisposto


CRF/DF - Tendo coom referência apenas as regras de ortografia, acentuação gráfica e pontuação vigentes, assinale a alternativa correta.

Ao contrário do que se observa em 'automedicação', o uso do hífen seria obrigatório caso a autora decidisse acrescentar o prefixo 'auto' ao vocábulo
'intoxicação'.

		[bg_red]  ERRADO [reset]

	[bg_red] O prefixo 'auto' termina com vogal e a palavra 'intoxicação' começa com consoante 'i', portanto é junto sem hífen.[reset]

O trecho 'esse hábito da automedicação oferece muitos perigos à saúde e ao bem-estar das pessoas' poderia, sem acarretar qualquer tipo de transgressão gramatical
ser substituido pela redação 'muitos perigos à saúde e ao bem-estar das pessoas tem sido oferecido por esse hábito da automedicação'

	[bg_red] ERRADO [reset]

		[red] O erro está na acentuação no 'tem', 'têm' para o plural, devido a frase iniciar no plural -> 'muitos perigos...'[reset]


					Maiúscula e minúscula segundo o Novo Acordo Ortográfico

	A letra minúscula é usada:

		Usada em nomes dos dias, meses, estações do ano.  // Datas comemorativas as iniciais são Maiúsculas
		Substantivo comuns
		Bibliónimos/Bibliônimos : Nomes de obras, títulos de livros. As primeiras iniciais podem ser escritos com maiúsculas.
		Nos usos de fulano, sicrano e beltrano são minúsculos.
		Pontos cardeais: norte, sul, leste, oeste. As abreviaturas não são minúsculas.
		Axiônimos : Opcionais com letra maiúscula. Valores sociais, títulos: 'senhor doutor' ou 'Senhor Doutor' Joaquim da Silva
		Hagiônimos : Valores religiosos : o cardeal Bembo ou o Cardeal Bembo / santa ou Santa Filomena
		Nomes que designam domínios do saber, cursos e disciplinas: Opcional com letra maiúscula: Português ou português, matemática ou Matemática
			línguas e literaturas modernas ( Línguas e Literaturas Modernas )

	
	A letra maiúscula é usada:

		Antropônimos, reais ou fictícios: Pedro Marques; Branca de Neve; D.Quixote
		Topônimos, reais ou fictícios: Lisboa, Luanda, Rio de Janeiro, Terra Média
		Seres antropomorfizados/mitológicos: Adamastor, Neturno, Ades, Zeus
		Nomes que designam instituições: Instituto de Pensões e Aposentadorias da Previdência Social
		Nomes de festas/festividades: Natal, Páscoa, Ramadão, festas de Santos
		Títulos periódicos: Jornais e revistas: O Primeiro de Janeiro / O Estado de São Paulo
		Nos pontos cardeais empregados absolutamente: 'Nordeste' invés de 'nordeste do Brasil'; Norte invés de norte de Portugal
			Ocidente invés de ocidente europeu; Oriente invés de oriente asiático.
		Emprega-se maiúscula em siglas, símbolos ou abreviaturas.
		Opcionalmente emprega-se em 
			logradouro público: rua ou Rua da Liberdade / largo ou Largo dos Leões / 
			templos : igreja ou Igreja do Bonfim / templo ou Templo do Apostolado Positivista
			edifícios: palácios ou Palácio da Cultura, edifício ou Edifício Azevedo Cunha.
		

[bg_yellow] Uso do apóstrofo [reset]

		Para dar realce com o uso da letra maiúscula: '

		d'Ele <- Realçar a letra 'E' em maiúscula
		n'Ele <-  Realçar a letra 'E' em maiúscula
		d'Aquele <-  Realçar a letra 'A' em maiúscula
		n'Aquele <-  Realçar a letra 'A' em maiúscula

O novo acordo ortográfico torna opcional o uso de iniciais maiúsculas em palavras usadas reverencialmente, para cargos e títulos:
		Presidente francês / presidente francês

	Em palavras com hífen, após se optar pelo uso da maiúscula ou da minúscula, deve-se manter a escolha para a grafia de todos os elementos hifenizados:
		pode-se escrever 'Vice-Presidente' ou 'vice-presidente', mas não 'Vice-presidente'.

	Os artigos serão designados pela abreviatura 'Art.' com inicial maiúscula sem traço antes do início do texto e ao longo do texto, com 'a' minúsculo.	'''

    def exercicios_pronomes(self):
       return '''Exercicios de pronomes:

1.Ano: 2024 / Banca: Legalle Concursos / Prova: Legalle Concursos - Prefeitura de Cerro Largo - Fiscal de Tributos - 2024

Os pronomes são uma classe de palavras que substituem ou acompanham um substantivo, desempenhando funções específicas nas frases. 
Nesse sentido, analise as frases abaixo e assinale a alternativa que apresenta a classificação dos pronomes sublinhados.


I. São [yellow]poucos[reset] os que escrevem sobre nós (I.54).
II. agora [yellow]nos[reset] restou o melhor da vida (I.49).
III. tudo o que [yellow]isso[reset] inclui (I.11-12).

A.I - Indefinido; II - Relativo; III - Possessivo.
B.I - Pessoal; II - Pessoal; III - Relativo.
C.I - Relativo; II - Demonstrativo; III - Relativo.
D.I - Indefinido; II - Pessoal; III - Demonstrativo.

Gabarito letra 'D'
	
	Pronome substantivo / pronome adjetivo:

Quando um pronome é empregado junto de um substantivo, ele é chamado de pronome adjetivo.
Quando um pronome aparece isolado, sozinho na frase, ele é chamado de pronome substantivo.

Ex:

[yellow]Ninguém[reset] pode adivinhar [yellow]suas[reset] vontades?
	
	[yellow]Ninguém[reset] -> [blue]pronome substantivo (pois está sozinho)[reset]
	[yellow]suas[reset]    -> [blue]pronome adjetivo ( acompanha o substantivo 'vontades')[reset]

	Encontrei [yellow]minha[reset] caneta mas não [yellow]a[reset] apanhei.

	[yellow]minha[reset]   -> [blue]pronome adjetivo ( está acompanhando o substantivo 'caneta' )[reset]
	[yellow]a[reset]       -> [blue]pronome substantivo ( está sozinho e substituindo alguém no discurso dentro contexto )[reset]

				
						São [yellow]poucos[reset] os que escrevem sobre nós (I.54).

[yellow]A palavra 'poucos' é da classe dos pronomes indefinidos. Ou seja, apontar coisas ou objetos que tem sentido vago, sem definição, sem saber o que é.[reset]

Os pronomes indefinidos são:

algum, alguns - algumas, alguma - alguém

nenhum, nenhuns, nenhuma, nenhumas - ninguém

[blue]todo, todos, toda, todas - tudo[reset]

outro, outras, outra, outras - outrem

muito, muitos, muita, muitas - nada

[yellow]pouco, poucos, pouca, poucas, -- cada[reset]

certo, certos, certa, certas - algo

[blue]tanto, tantos, tanta, tantas[reset]

quanto, quantos, quanta, quantas

[bg_red] ATENÇÃO! [reset] 

    [yellow]QUANTO, QUANTOS, QUANTA, QUANTAS[reset] são pronomes relativos se estiverem precedidos dos pronomes indefinidos [yellow]TUDO, TANTO(s), TANTA(S), todos(s), toda(s)[reset]
mas eles são pronomes indefinidos.

	Sempre obteve [yellow]tudo quanto[reset] quis.

    [yellow]'tudo'[reset]   -> [blue]Pronome indefinido [reset]
    [yellow]'quanto'[reset] -> [blue]Pronome relativo,  mas precisa ser precedido de um pronome indefinido.[reset]


qualquer - quaisquer <- Pronome Indefinido



				'...agora [yellow]nos[reset] restou o melhor da vida.' (I.49).

A palavra 'nos' é da classe dos pronomes pessoais do caso oblíquo: não exercem função de sujeito na oração.
O Pronome 'nos' sem acento, é do caso oblíquo átono: Não é sujeito da oração.


				'...tudo o que [yellow]isso[reset] inclui (I.11-12).'

A palavra 'isso' é da classe do pronomes demonstrativos, ou seja, apontar ou indicar a posição ou lugar dos seres em relação às três pessoas gramaticais.

[yellow]Aquela[reset] casa é igual à nossa.\n
                O pronome demonstrativo 'aquela' refere-se a distância. 3º pessoa.

                Os pronomes demonstrativos:

                    este, esta, estes, estas -> isto
                    esse, essa, esses, essas -> [yellow]isso[reset]
                    aquele, aquela, aqueles, aquelas -> aquilo
                    o, a, os, as -> o

        [bg_red]Podem funcionar como pronomes demonstrativos: o, os, a, as, mesmo, mesma, semelhante, semelhantes, tal, tals[reset]

	Chegamos hoje, não [yellow]o[reset] sabias? [blue](o = isto)[reset]

    	Quem diz [yellow]o[reset] que quer, ouve [yellow]o[reset] que não quer [blue](o = aquilo)[reset]

	[blue]Podemos substituir por 'aquilo' pronome demonstrativo também:[reset]
	Quem diz [yellow]aquilo[reset] que quer, ouve [yellow]aquilo[reset] que não quer.

    	[yellow]Tais[reset] coisas não se dizem em público. [blue]( tais = estas )[reset]

        Outros exemplos:

	O livro que você trouxe não é [yellow]o[reset] que te pedi. [blue] Note que 'o' equivale ao pronome demonstrativo 'aquele'[reset]

	A revista que você trouxe não é [yellow]a[reset] que te pedi. [blue] Note que 'a' equivale ao pronome demonstrativo 'aquela'[reset]

	Pode fazer [yellow]o[reset] que você quiser. [blue] Note que 'o' equivale a 'aquilo'.[reset]

            Regra dos pronomes demonstrativos:

        Conceito básico: Servem para referêcia a objetos em relação as pessoas que participam de um diálogo ( pessoas do discurso )

REGRA:

            - Primeira pessoa: eu / nós .-> Deve-se empregar ESTE,ESTA,ISTO com referência a objeto próximo de quem fala.
            - Segunda pessoa: tu / vós / você. ->  Deve-se empregar ESSA,ESSA,ISSO com referência a objeto próximo de quem ouve.
          	- Terceira pessoa: ele, ela, eles, elas.->  Deve-se empregar AQUELE,AQUELA,AQUILO com referência a objeto distante tanto de quem fala, como de quem ouve.
            
- Primeira pessoa: eu / nós -> Deve-se empregar ESTE,ESTA,ISTO com referência a objeto próximo de quem fala.              

        Esta camisa que estou usando.

- Segunda pessoa: tu / vós / você. ->  Deve-se empregar ESSA,ESSA,ISSO com referência a objeto próximo de quem ouve.

        Esses óculos que estão no seu rosto.

- Terceira pessoa: ele, ela, eles, elas.->  Deve-se empregar AQUELE,AQUELA,AQUILO com referência a objeto distante tanto de quem fala, como de quem ouve.        

    

CRN-8/QUADRIX:
	Muitos recém-nascidos recebem uma injeção de vitamina K para evitar uma condição rara, mas grave, de sangramento excessivo. Isso ocorre porque os
bebês nascem com baixos níveis de vitamina K.

	O pronome 'isso' retoma a ideia de que recém-nascidos:

a. recebem injeção de vitamina K
b. não precisam de reforço de vitamina K.
c. Não tem vitaminas K no corpo.
d. sempre apresentam condição grave.
e. tem níveis baixos de vitamina K.

    O pronome demonstrativo 'isso' no contexto da frase retoma a ideia de que recebem uma injeção de vitamina K. Letra 'a'.

	O pronome demonstrativo 'isso' retoma o primeiro termo da frase, sendo que a finalidade é para evitar uma condição rara.

            
a. recebem injeção de vitamina K [bg_green][CORRETO][reset]
b. não precisam de reforço de vitamina K. [bg_red][ERRADO][reset]
c. Não tem vitaminas K no corpo.[bg_red][ERRADO][reset] <- a vitamina em baixo nível
d. sempre apresentam condição grave.[bg_red][bg_red][ERRADO][reset] <- quando apresentam condição grave
e. tem níveis baixos de vitamina K.[bg_red][ERRADO][reset] <- não é sempre.

[bg_red]ALERTA! [reset]

[red]Texto 1.[reset] Quem estuda vence. [yellow]Isto[reset] é um fato.

[blue]O correto seria 'isso' em regra resumindo o fato anterior.[reset]

Pergunta 1. No texto, 'isto' se referiu à frase anterior? SIM. É um pergunta somente interpretativa. Sem levar em conta a regra.

Pergunta 2. O texto respeitou a norma culta padrão de linguagem? NÃO! O correto seria 'isso', retomando a ideia anterior.

        Depende do que a banca perguntar:

    Quando a banca pergunta se o pronome demonstrativo 'isto' se refere a frase anterior, é o sentido no texto. SIM.

    Quando a banca pergunta se o pronome demonstrativo 'isto' respeitou o padrão culto da linguagem? Não.


2. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP / Prova: IDCAP - Prefeitura de Reduto - Auxiliar Odontológico - 2024

[yellow]Esse[reset] software de código aberto e [yellow]suas[reset] ferramentas de análise foram especialmente projetados para auxiliar os gerentes de conservação no [yellow]seu[reset] trabalho de vigilância.


Em relação aos pronomes, é correto afirmar que a frase apresenta:

A.Um possessivo, um indefinido e um pessoal oblíquo.
B.Um demonstrativo e dois possessivos.
C.Dois demonstrativos, um possessivo e um indefinido.
D.Um demonstrativo, um possessivo e dois indefinidos.

Gabarito letra 'B'.

Pronome substantivo / pronome adjetivo:

Quando um pronome é empregado junto de um substantivo, ele é chamado de pronome adjetivo.
Quando um pronome aparece isolado, sozinho na frase, ele é chamado de pronome substantivo.

Ex:

[yellow]Ninguém[reset] pode adivinhar [yellow]suas[reset] vontades?
	
	[yellow]Ninguém[reset] -> [blue]pronome substantivo (pois está sozinho)[reset]
	[yellow]suas[reset]    -> [blue]pronome adjetivo ( acompanha o substantivo 'vontades')[reset]

	Encontrei [yellow]minha[reset] caneta mas não [yellow]a[reset] apanhei.

	[yellow]minha[reset]   -> [blue]pronome adjetivo ( está acompanhando o substantivo 'caneta' )[reset]
	[yellow]a[reset]       -> [blue]pronome substantivo ( está sozinho e substituindo alguém no discurso dentro contexto )[reset]


A palavra 'esse' é da classe do pronomes demonstrativos, ou seja, apontar ou indicar a posição ou lugar dos seres em relação às três pessoas gramaticais.

[yellow]Aquela[reset] casa é igual à nossa.\n
                O pronome demonstrativo 'aquela' refere-se a distância. 3º pessoa.

                Os pronomes demonstrativos:

                    este, esta, estes, estas -> isto
                    [yellow]esse[reset], essa, esses, essas -> isso
                    aquele, aquela, aqueles, aquelas -> aquilo
                    o, a, os, as -> o

        [bg_red]Podem funcionar como pronomes demonstrativos:[reset] [bg_yellow]o, os, a, as, mesmo, mesma, semelhante, semelhantes, tal, tals[reset]

	Chegamos hoje, não [yellow]o[reset] sabias? [blue](o = isto)[reset]

    	Quem diz [yellow]o[reset] que quer, ouve [yellow]o[reset] que não quer [blue](o = aquilo)[reset]

	[blue]Podemos substituir por 'aquilo' pronome demonstrativo também:[reset]
	Quem diz [yellow]aquilo[reset] que quer, ouve [yellow]aquilo[reset] que não quer.

    	[yellow]Tais[reset] coisas não se dizem em público. [blue]( tais = estas )[reset]

        Outros exemplos:

	O livro que você trouxe não é [yellow]o[reset] que te pedi. [blue] Note que 'o' equivale ao pronome demonstrativo 'aquele'[reset]

	A revista que você trouxe não é [yellow]a[reset] que te pedi. [blue] Note que 'a' equivale ao pronome demonstrativo 'aquela'[reset]

	Pode fazer [yellow]o[reset] que você quiser. [blue] Note que 'o' equivale a 'aquilo'.[reset]

            Regra dos pronomes demonstrativos:

        Conceito básico: Servem para referêcia a objetos em relação as pessoas que participam de um diálogo ( pessoas do discurso )

[red]REGRA:[reset]

            - [blue]Primeira pessoa:[reset] eu / nós .-> Deve-se empregar [yellow]ESTE,ESTA,ISTO[reset] com referência a objeto próximo de quem fala.
            - [blue]Segunda pessoa:[reset]  tu / vós / você. ->  Deve-se empregar [yellow]ESSA,ESSA,ISSO[reset] com referência a objeto próximo de quem ouve.
            - [blue]Terceira pessoa:[reset] ele, ela, eles, elas.->  Deve-se empregar AQUELE,AQUELA,AQUILO com referência a objeto distante tanto de quem fala, como de quem ouve.
            
- [blue]Primeira pessoa: eu / nós [reset]-> [yellow]Deve-se empregar ESTE,ESTA,ISTO com referência a objeto próximo de quem fala.[reset]              

        [yellow]Esta[reset] camisa que estou usando.

- [blue]Segunda pessoa:[reset] tu / vós / você. ->  [yellow]Deve-se empregar ESSA,ESSA,ISSO com referência a objeto próximo de quem ouve.[reset]

        [yellow]Esses[reset] óculos que estão no seu rosto.

- [blue]Terceira pessoa:[reset] ele, ela, eles, elas. ->  [yellow]Deve-se empregar AQUELE,AQUELA,AQUILO com referência a objeto distante tanto de quem fala, como de quem ouve.[reset]        

        
Exemplo 1:
		
		Correspondência do Governador para o Presidente da Assembleia Legislativa.
	Senhor Presidente,

	Solicito a V.Exa que ESSA Casa Legislativa analise com urgência o projeto que destina verba para reforma do Ginásio Estadual Américo de Almeida.

		[blue]Note que o remetente é:[reset] [yellow]GOVERNADOR [reset]
		[blue]Note que o destino é:[reset] [yellow]Presidente da Assembleia Legislativa [reset]

		[blue] '...que ESSA Casa Legislativa...'[reset] : [yellow] PRONOME DEMONSTRATIVO 'ESSA' em referência ao objeto próximo de quem ouve.[reset]

	Resposta do Presidente da Assembleia Legislativa para o Governador.
Senhor Governador,
	
	Informo a V.Exa que [yellow]esta[reset] Casa colocará em pauta na quarta-feira próxima a análise do projeto que destina verba para reforma do Ginásio Américo de Almeida.
	[yellow]Essa[reset] Governadoria pode aguardar informativo na quinta-feira.

	[yellow] Agora o pronome demonstrativo 'ESTA' no contexto da frase é referido ao objeto próximo de quem está falando, que no caso é 'a casa'.[reset]
	[blue] '... ESSA Governadoria pode...' [reset] => [green] 'essa' pronome demonstrativo ao objeto próximo de quem ouve. [reset]



[bg_red]ALERTA! [reset]

[red]Texto 1.[reset] Quem estuda vence. [yellow]Isto[reset] é um fato.

[blue]O correto seria 'isso' em regra resumindo o fato anterior.[reset]

Pergunta 1. No texto, 'isto' se referiu à frase anterior? SIM. É um pergunta somente interpretativa. Sem levar em conta a regra.

Pergunta 2. O texto respeitou a norma culta padrão de linguagem? NÃO! O correto seria 'isso', retomando a ideia anterior.

        Depende do que a banca perguntar:

    Quando a banca pergunta se o pronome demonstrativo 'isto' se refere a frase anterior, é o sentido no texto. SIM.

    Quando a banca pergunta se o pronome demonstrativo 'isto' respeitou o padrão culto da linguagem? Não.

[yellow]Esse[reset] software de código aberto e [yellow]suas[reset] ferramentas de análise foram especialmente projetados para auxiliar os gerentes de conservação no [yellow]seu[reset] trabalho de vigilância.

As palavras 'suas' e 'seu' são pronomes da classe dos possessivos.

      [blue]O pronome possessivo deve concordar com o substantivo.[reset]

		Nós temos [yellow]nossa[reset] ideia - [yellow]O pronome 'nossa' é possessivo e concorda em gênero em 'ideia' - palavra feminina.[reset]
                                        
Os pronomes possessivos 'seu(s)' e 'sua(s)' podem se referir tanto à 2º pessoa (pessoa com quem se fala) como à 3º pessoa (pessoa de quem se fala)

        		Sua casa foi vendida [blue](sua = de você)[reset]    <- [green] 2º pessoa do discurso [reset]
        		Sua casa foi vendida [blue](sua = dele, dela)[reset] <- [green] 3º pessoa do discurso [reset]

Os pronomes 'seus' e 'suas' são usados tanto para 3º pessoa do singular quanto para 3º pessoa do plural:

		Ana recebeu [yellow]sua[reset] notícia. [blue]( 'notícia' = de outra pessoa ou da própria 'ana')[reset]
 
		Ana e João receberam [yellow]sua[reset] notícia. [blue]( 'notícia' = de outra pessoa ou deles <- podendo ser duas ou mais notícias)[reset]

[bg_green] Os pronomes possessivos podem em muitos casos ser substituidos por pronomes oblíquos equivalentes. [reset]

		A chuva molha-[yellow]me[reset] o rosto. [blue]( 'me' pronome oblíquo átono que pode significar 'meu' = molha 'meu' rosto, pronome possessivo)[reset]

   		A chuva molha-[yellow]lhe[reset] o rosto. [blue]( 'lhe' pronome oblíquo átono que pode significar 'seu' = molha seu rosto, pronome possessivo) [reset]


O pronome possessivo 'seu' refere-se gramaticalmente ao substantivo, podendo estar do lado do substantivo. 
Porém é a concordância que o pronome está fazendo é em relação ao possuidor da ideia.
A referência de pronome possessivo é o possuidor e não o substantivo que o acompanha.
           
           
Questão de concurso:

Quadrix/CRN-8:
	Uma dieta saudável e equilibrada é importante para apoiar o sistema imunológico do seu corpo e a má nutrição pode comprometê-lo.
    Procure comer uma grande variedade de frutas e legumes para garantir que você obtenha todos os nutrientes de que seu sistema imuno-
    lógico precisa.
O pronome possessivo 'seu' (linha 19) refere-se ao

a. sistema imunológico
b. leitor
c. corpo
d. termo 'dieta'
e. micronutriente.

Alternativa 'B'.  O pronome possessivo 'seu' refere-se gramaticalmente ao substantivo 'corpo', ao lado do substantivo. 
Porém a referência que o pronome está fazendo é em relação ao 'leitor' possuidor da ideia. '... que você obtenha todos...'
A referência de pronome possessivo é o possuidor e não a 'coisa possuida' o substantivo que o acompanha.

    'Corpo' é a coisa possuida, a concordância.
    Referência em pronomes possessivos em questões de concurso é o possuidor.

3. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de Caraguatatuba - PEB II - Português - 2024

As frases a seguir, mostram o mesmo problema na utilização de pronomes, à exceção de uma. Assinale-a.

A.[yellow]Nós[reset] temos todas as nossas malas já prontas. Por que [yellow]se[reset] apressar?
B.[yellow]Eu e meu irmão[reset] preparamos nosso material esportivo. É por isso que já estamos procurando um lugar para [yellow]se[reset] treinar.
C.Por causa do ruído das máquinas, [yellow]nosso guia[reset] nos propôs um lugar retirado para [yellow]se[reset] descansar.
D.[yellow]Por mim e por minha mulher[reset], nosso destino de viagem será o Alaska; poderemos assim [yellow]nos[reset] medirmos com a natureza selvagem.
E.Mesmo que o casamento esteja menos popular, [yellow]Sofia e eu[reset] decidimos, para alegria de nossos respectivos pais, de [yellow]se casar.[reset]


[bg_blue]A questão aborda o tema do emprego correto dos pronomes pessoais oblíquos em contextos específicos, focando na coesão referencial.[reset]

	A.[yellow]Nós[reset] temos todas as nossas malas já prontas. Por que [yellow]se[reset] apressar?

A frase utiliza incorretamente o pronome 'se' em 'se apressar', quando deveria empregar 'nos' para manter a coesão e a coerência com o sujeito 'nós'. 
Este erro é comum e demonstra a dificuldade em usar corretamente os pronomes pessoais oblíquos.

	B.[yellow]Eu e meu irmão[reset] preparamos nosso material esportivo. É por isso que já estamos procurando um lugar para [yellow]se[reset] treinar.

A frase utiliza incorretamente o pronome 'se' em 'se treinar', quando deveria empregar 'nos' para manter a coesão e a coerência com o sujeito 'Eu e meu irmão'. 
Este erro é comum e demonstra a dificuldade em usar corretamente os pronomes pessoais oblíquos.

	C.Por causa do ruído das máquinas, [yellow]nosso guia[reset] nos propôs um lugar retirado para [yellow]se[reset] descansar.

Similar ao item B, este também apresenta um erro no uso do pronome 'se' em 'se descansar', 
que deveria ser 'nos descansar' para referir corretamente ao sujeito 'nosso guia nos'. Este é outro exemplo do problema comum de coesão referencial.

	D.[yellow]Por mim e por minha mulher[reset], nosso destino de viagem será o Alaska; poderemos assim [yellow]nos[reset] medirmos com a natureza selvagem.

Este item está correto e de acordo com o gabarito da banca. O uso de 'nos medirmos' está adequado, pois o pronome 'nos' refere-se corretamente aos sujeitos da frase ('Por mim e por minha mulher'), 

	E.Mesmo que o casamento esteja menos popular, [yellow]Sofia e eu[reset] decidimos, para alegria de nossos respectivos pais, de [yellow]se casar.[reset]

 Aqui, o erro está novamente no uso do pronome 'se' em 'se casar', que deveria ser 'nos casar' para referir-se adequadamente aos sujeitos 'Sofia e eu'. 
Este item reforça a dificuldade em empregar corretamente os pronomes pessoais oblíquos, mantendo a coesão referencial.



4.Ano: 2024 / Banca: Instituto Social Univida / Prova: Instituto Social Univida - Prefeitura de Floraí - Educador Social - 2024 

“No ano 590 d.C., a Igreja Católica incorporou ao [yellow]seu[reset] calendário o Carnaval.” 1º§

A palavra sublinhada é corretamente classificada como pronome:

A.Pessoal reto.
B.Pessoal oblíquo.
C.Relativo.
D.Possessivo.
E.Demonstrativo.

A palavra em questão é 'seu', que se refere ao calendário da Igreja Católica, indicando posse.

5. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura de Tapiratiba - Motorista de Transporte Escolar - 2024

Considere o excerto: “‘É cerca de 200 a 150 anos mais velho do que os túmulos de passagem, tornando-o uma das câmaras mortuárias de pedra mais antigas da Suécia e de toda a Escandinávia’”. 
No contexto apresentado, o pronome pessoal oblíquo ‘o’ exerce o cargo de:

A.sujeito.
B.objeto indireto.
C.objeto direto.
D.complemento nominal.
E.adjunto adverbial.

A.Sujeito [bg_red] ERRADO [reset]
O pronome pessoal oblíquo 'o' não pode exercer a função de sujeito, pois o sujeito é o termo que pratica a ação do verbo. 
No caso da frase apresentada, 'o' é o termo que sofre a ação do verbo 'tornar'.\n
B.Objeto Indireto [bg_red] ERRADO [reset]
O pronome pessoal oblíquo 'o' não exerce a função de objeto indireto, pois o objeto indireto é introduzido por uma preposição. 
Na frase, 'o' não está precedido por preposição, logo, esta alternativa está incorreta.\n
C. Objeto Direto [bg_green] CORRETO [reset]
O pronome pessoal oblíquo 'o' exerce a função de objeto direto, pois é o termo que sofre diretamente a ação do verbo 'tornar'. 
A frase pode ser reescrita como: 'Tornando-o uma das câmaras mortuárias de pedra mais antigas da Suécia e de toda a Escandinávia'.\n
D.Complemento Nominal [bg_red] ERRADO [reset]
O pronome pessoal oblíquo 'o' não exerce a função de complemento nominal, pois o complemento nominal é um termo que completa o sentido de um nome (substantivo, adjetivo ou advérbio) 
e é sempre introduzido por uma preposição. Na frase, 'o' não está completando o sentido de um nome, mas sim de um verbo. Portanto, esta alternativa está incorreta.\n
E.adjunto adverbial [bg_red] ERRADO [reset]
O pronome pessoal oblíquo 'o' não exerce a função de adjunto adverbial, pois o adjunto adverbial é um termo que modifica o verbo, o adjetivo ou outro advérbio, 
indicando circunstâncias como tempo, modo, lugar, etc. Na frase, 'o' está sofrendo a ação do verbo 'tornar', logo, esta alternativa está incorreta.

Outras colocações:

“‘É cerca de 200 a 150 anos mais velho do que os [yellow]túmulos[reset] de passagem, tornando-[yellow]o[reset] uma das câmaras mortuárias de pedra mais antigas...' 

O pronome "o" refere-se a "ele", que neste contexto é o "excerto" ou o "túmulo".

Vamos agora analisar cada alternativa:

A. Sujeito:

O sujeito é aquele que pratica a ação ou de quem se fala na oração.

No caso, o sujeito da frase é "ele" (o túmulo). Portanto, o pronome "o" não é sujeito.

B. Objeto indireto:

O objeto indireto é aquele que completa o sentido do verbo por meio de uma preposição (geralmente "a", "para", "de"). Exemplo: "Ele falou ao amigo".

Na frase dada, não há preposição introduzindo "o", então "o" não é objeto indireto.

C. Objeto direto:

O objeto direto é o termo que completa o sentido do verbo sem necessidade de preposição. Exemplo: "Ele comeu a maçã".

Na frase “tornando-o uma das câmaras mortuárias de pedra mais antigas da Suécia e de toda a Escandinávia”, o pronome "o" está sendo diretamente afetado pelo verbo "tornar", sem preposição.

Logo, "o" é objeto direto.

Tornando o que?

Tornando quem?

D. Complemento nominal:

O complemento nominal completa o sentido de um nome (substantivo, adjetivo ou advérbio) e é sempre introduzido por uma preposição. Exemplo: "Ele tem medo de altura".

Na frase "Ele tem medo de altura", "altura" não é verbo e sim substantivo, "de" é preposição. Se altura, completa o sentido da frase e não é verbo, está precedido de preposição, é complemento nominal.

No nosso caso, o pronome "o" não está completando o sentido de um nome e não é introduzido por preposição, então não pode ser complemento nominal.


E. Adjunto adverbial:

O adjunto adverbial é o termo que indica uma circunstância (tempo, modo, lugar, etc.) e modifica o verbo, adjetivo ou advérbio. Exemplo: "Ele correu rapidamente". Na frase, "o" não está indicando nenhuma circunstância, então não é adjunto adverbial.

Portanto, a resposta correta é:

C. Objeto direto.

6.Ano: 2024 / Banca: COSEAC / Prova: COSEAC - FME - Professor - Área: Educação Física - 2024 

Em minha trajetória, pretendo ensinar [yellow]a[reset] leitura e [yellow]a[reset] escrita [yellow]a[reset] quantas crianças conseguir. Esse é um direito delas. 
Fico pensando como seria [yellow]a[reset] minha vida se eu não soubesse ler e escrever. Que perspectiva de vida têm aquelas pessoas que não são alfabetizadas? 
Foi por meio desse propósito que me encontrei ao começar [yellow]a[reset] trabalhar com [yellow]a[reset] educação infantil”.

A.artigo definido em todas as ocorrências.
B.artigo na primeira, quarta e quinta ocorrência, preposição na sexta e pronome pessoal na segunda e na terceira.
C.pronome pessoal na terceira e na sexta ocorrência, artigo definido na segunda e preposição nas demais.
D.preposição na terceira e na sexta ocorrência, pronome pessoal na primeira e artigo definido nas demais.
E.preposição na terceira e na quinta ocorrência, sendo artigo nas demais.

Gabarito letra 'E'.

O artigo seja indefinido ou definido sempre irá acompanhar e identificar um substantivo. 
'a leitura' -> 'leitura' <- substantivo ( 1º ocorrência )
'a escrita' -> 'escrita' <- substantivo ( 2º ocorrência )
'a minha vida' -> 'vida' <- substantivo ( 'minha' <- pronome adjetivo possessivo ) ( 4º ocorrência )
'a educação infantil' -> 'educação' <- substantivo ( infantil <- adjetivo <- qualificando o substantivo ) ( 6º ocorrência )

Por sua vez a preposição na ( 3º ocorrência ) 'a' que irá ligar orações criando relacionamentos: pretende ensinar a leitura e escrita pra quem? 
	- 'a' quantas crianças conseguir.

Na 4º ocorrência temos a preposição 'a' ligando uma oração a outra : Ela se encontrou a começar a fazer o que? 'a' trabalhar com educação infantil. 

7.Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN 
Prova: IDECAN - ALE PI - Analista Legislativo - Área: Redação e Revisão de Texto - 2024

Assinale a alternativa que contém pronome pessoal corretamente indicado.

A.Não há nada além de desprezo entre eu e ela.
B.Vim aqui ti fazer um convite para uma festa.
C.Meu pai me deu esse livro para me ler.
D.Se fores à festa, iremos então contigo.
E.Geraldo veio mim dar um recado.

Gabarito letra 'D'.

Os pronomes pessoais são palavras que substituem os nomes e indicam a quem se refere a enunciação. 
Eles podem ser retos (eu, tu, ele, nós, vós, eles) quando exercem a função de sujeito, 
u oblíquos (me, te, se, nos, vos, lhe, lhes, o, a, os, as) quando exercem a função de complemento. 

				'Não há nada além de desprezo [yellow]entre eu e ela.[reset]'

Neste caso, o uso dos pronomes pessoais 'eu' e 'ela' está incorreto. 
A preposição 'entre' exige o uso de pronomes oblíquos, portanto a frase correta seria 'Não há nada além de desprezo [blue]entre[reset] [yellow]mim e ela.[reset]'


				B.Vim aqui [yellow]ti[reset] fazer um convite para uma festa.

Neste caso, o uso do pronome pessoal 'ti' está incorreto. O pronome 'ti' não pode ser usado ante de verbos no infinitivo. Precisa de preposição.
A frase correta seria 'Vim aqui para [yellow]te[reset] fazer um convite para uma festa.'
													ou
						' Vim aqui para ti fazer um convite para uma festa.'														

				Meu pai me deu esse livro para [yellow]me[reset] ler.'						

O item C apresenta a frase 'Meu pai me deu esse livro para me ler.' Neste caso, o uso do pronome pessoal 'me' está incorreto. 
O pronome 'me' não pode ser usado como sujeito de um verbo no infinitivo. A frase correta seria 'Meu pai me deu esse livro para [yellow]eu[reset] ler.'

				'Se fores à festa, iremos então [yellow]contigo[reset]

O item D apresenta a frase 'Se fores à festa, iremos então contigo.' Neste caso, o uso do pronome pessoal 'contigo' está correto. 
O pronome 'contigo' é um pronome pessoal oblíquo átono que pode ser usado após verbos no infinitivo, também. OU precedido de preposição: 'até'

					'Geraldo veio [yellow]mim[reset] dar um recado.'

O item E apresenta a frase 'Geraldo veio mim dar um recado.' Neste caso, o uso do pronome pessoal 'mim' está incorreto. 
O pronome 'mim' não pode ser usado como objeto direto de um verbo. A frase correta seria 'Geraldo veio [yellow]me[reset] dar um recado.'

7.Ano: 2024 / Banca: Comissão permanente de Concursos - UFAM - COMPEC / Prova: COMPEC - UFAM - Fisioterapeuta - 2024 
Assinale a alternativa em que houve ERRO ao se substituir a expressão destacada em negrito pelo pronome pessoal oblíquo:

A.Deves [yellow]investir o teu dinheiro[reset] em bancos estatais = investi-lo.
B.Os atletas da NBA [yellow]fazem coisas fenomenais[reset] = fazem-nas.
C.E, enfim, [yellow]eis a bela paisagem de que te falei[reset] = ei-la.
D.Se [yellow]nos permitissem,[reset] degustaríamos o bolo com as mãos = no-lo.
E.A assistente social [yellow]visitou cada um dos idosos[reset] em sua casa = visitou-lhes.

Gabarito letra 'E'.

				A.Deves [yellow]investir o teu dinheiro[reset] em bancos estatais = investi-lo.

Verbos terminados em -r, -s ou -z, os pronomes o, a, os, as assumem as antigas formas lo, la, los, las, caindo aquelas consoantes". 
Observe que o verbo transitivo direto "investir" termina em "-r" e o termo a ser substituído está no masculino singular; logo, a forma pronominal correta é "lo" [investi-lo].
A substituição está correta, pois [yellow]'o teu dinheiro'[reset] é objeto direto e 'lo' é o pronome oblíquo átono adequado para substituir um objeto direto masculino singular. 

				B.Os atletas da NBA [yellow]fazem coisas fenomenais[reset] = fazem-nas.

Além disso, cabe inserir outra regra gramatical contida em Cegalla: Associados a verbos terminados em ditongo nasal, os ditos pronomes tomam as formas no, na, nos, nas. 
Veja que a forma verbal "fazem" termina em "-n" e o termo "coisas fenomenais" está no feminino plural. Nesse caso, usa-se a forma "-nas" [fazem-nas].

A expressão 'fazem coisas fenomenais' é substituída por 'fazem-nas'. A substituição está correta, pois 'coisas fenomenais' é objeto direto e 'nas' é o pronome oblíquo átono adequado para substituir um objeto direto feminino plural.

				C.E, enfim, [yellow]eis a bela paisagem de que te falei[reset] = ei-la.

Veja que a forma verbal "eis" termina em "-s" e o termo "a bela paisagem de que te falei" possui como núcleo a palavra "bela". 
Nesse caso, a forma pronominal correta é "-la" [ei-la].				
A expressão 'eis a bela paisagem de que te falei' é substituída por 'ei-la'. A substituição está correta, pois 'a bela paisagem' é objeto direto e 'la' é o pronome oblíquo átono adequado para substituir um objeto direto feminino singular

				D.Se [yellow]nos permitissem,[reset] degustaríamos o bolo com as mãos = no-lo.
Aqui temos uma regra de contração dos pronomes oblíquos. De acordo com Cegalla (idem, p. 561), os pronomes oblíquos "me", "te", "lhe", "nos", "vos", "lhes" contraem-se com os pronomes átonos "o", "a", "os", "as". 
No caso do pronome "nos", a contração com o átono "os", forma a expressão "no-lo".
A expressão 'nos permitissem' é substituída por 'no-lo'. A substituição está correta, pois 'nos' é objeto direto e 'lo' é o pronome oblíquo átono adequado para substituir um objeto direto masculino singular.

				E.A assistente social [yellow]visitou cada um dos idosos[reset] em sua casa = visitou-lhes.
 Aqui devemos analisar a transitividade do verbo "visitar". Esse verbo é transitivo direto (quem visita, visita alguém ou alguma coisa). 
Por ser transitivo direto, o pronome "lhe" foi usado inadequadamente, pois este pronome só é usado na função de objeto indireto. 
O certo seria: A assistente socia os visitou.
A expressão 'visitou cada um dos idosos' é substituída por 'visitou-lhes'. A substituição está incorreta, pois 'cada um dos idosos' é objeto direto e 'lhes' é um pronome oblíquo átono que substitui objetos indiretos. A forma correta seria 'visitou-os'.
			

8. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP /Prova: IDCAP - INOVA Capixaba - Enfermeiro - Área Terapia Intensiva - 2024

À medida que a indústria do esqui testava maneiras de conservar a neve para permitir a realização de eventos no outono ou início do inverno, os resorts empilhavam 'a neve', e depois cobriam as pilhas com um material orgânico.

Substituindo o termo destacado pelo pronome oblíquo adequado, tem-se:

A.os resorts empilhavam-lhe
b.os resorts lhe empilhavam
c.os resorts empilhavam-la
d.os resorts empilhavam-a
e.os resorts empilhavam-na


				os resorts empilhavam-lhe

O item 'os resorts empilhavam-lhe' está incorreto. O pronome 'lhe' é utilizado para substituir objetos indiretos, em que necessita-se de preposição no caso do 'lhe.
Enquanto 'a neve' é um objeto direto. Quem 'necessita' necessita de algo ou alguém.. Verbo Transitivo Direito,  portanto, Objeto Direto. Portanto, a substituição está ERRADA.


				os resorts lhe empilhavam

Próclise para o pronome 'lhe'. Além disso o pronome pessoal do caso oblíquo tônico 'lhe' é utilizado soente para objeto indireto, em que precisa de preposuição.
'a neve' é objeto indireto

				
				d.os resorts empilhavam-a

O item 'os resorts empilhavam-a' está incorreto. Embora o pronome 'a' seja correto para substituir 'a neve', a posição do pronome está incorreta. 
Em português, o pronome oblíquo átono deve ser colocado após o verbo em casos de ênclise, mas a frase original não justifica essa posição.

				e.os resorts empilhavam-na

 O item 'os resorts empilhavam-na' está correto. O pronome 'na' é a forma correta para substituir 'a neve' como objeto direto, 
e a posição do pronome está adequada. Este item está de acordo com o gabarito da banca.

9.Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Turuçu - Enfermeiro - 2024 
Em “________ orientou-a”, para que o pronome “a” tenha que ficar, obrigatoriamente, após o verbo, a lacuna deve ser preenchida por qual das opções a seguir?

A.Sempre
B.Ninguém
C.Não
D.Antes,

A questão aborda a colocação pronominal, especificamente a próclise, ênclise e mesóclise, que são regras de colocação dos pronomes átonos em relação ao verbo. 
No caso específico, a questão pede que o pronome 'a' seja colocado obrigatoriamente após o verbo, o que caracteriza a ênclise. 
A ênclise é obrigatória em início de oração, após pausas e após certas palavras que atraem o pronome para depois do verbo.

 O item 'Sempre' é uma palavra que atrai o pronome para antes do verbo, caracterizando a próclise. 'sempre' é advérbio portanto é próclise obrigatória.
Portanto, a frase ficaria 'Sempre a orientou', o que não atende à exigência da questão.

 O item 'ninguem' é pronome indefinido quee atrai para antes do verbo, caracterizando próclise.

 O item 'não' é uma palavra negativa que atrai o pronomme para antes do verbo, caracteriznado próclise obrigatória.

 O item 'Antes,' seguido de vírgula, cria uma pausa que obriga a colocação do pronome após o verbo, resultando em 'Antes, orientou-a'.


10.Ano: 2024 / Banca: MS Concursos / Prova: MS Concursos - SAAE Manhuaçu - Ajudante Administrativo - 2024

Considerando as normas de colocação pronominal, assinale a alternativa que contém a frase gramaticalmente correta.

A.Jamais esquecerei-me daqueles momentos que passamos juntos.
B.Não aceitaram-me naquele emprego.
C.“Se vai a primeira pomba despertada”.
D.Dar-me-iam água para lavar as mãos?

Gabarito 'D'.

A questão aborda as normas de colocação pronominal na língua portuguesa, um tópico fundamental da gramática que trata 
da posição dos pronomes oblíquos átonos (me, te, se, nos, vos) em relação aos verbos. 
A correta colocação pronominal é essencial para a construção de frases gramaticalmente corretas e compreensíveis. 
As normas de colocação pronominal incluem a próclise, a mesóclise e a ênclise.

O item 'A' está errado. A presença do advérbio 'jamais' no início da frase exige a próclise, ou seja, 
o pronome oblíquo átono deve ser colocado antes do verbo, resultando em 'Jamais me esquecerei daqueles momentos que passamos juntos.'
A próclise é usada quando há palavras ou expressões que atraem o pronome para antes do verbo, como negações (não, nunca, jamais), 
conjunções subordinativas (que, como, se), pronomes relativos (que, quem), pronomes indefinidos (algum, nenhum), advérbios, entre outros.

Item 'B' está errado. Pois a presença da negação 'não' exige a próclise, e o pronome oblíquo átono deve ser colocado antes do verbo, 
formando 'Não me aceitaram naquele emprego.'

O item 'C' está errado. A análise de colocação pronominal foca na posição dos pronomes oblíquos átonos em relação aos verbos. Frases que não contêm pronomes oblíquos átonos não são aplicáveis à regra de colocação pronominal.
Porém, é errado iniciar frases com a colocação de pronomes obliquos. Por regra.

O item 'D' é a única correta. A frase 'Dar-me-iam água para lavar as mãos?' está de acordo com o gabarito da banca, 
pois segue corretamente a regra de colocação pronominal. 
Neste caso, utiliza-se a mesóclise, que é a inserção do pronome no meio do verbo, aplicável a verbos no futuro do presente ou no futuro do pretérito, como em 'dar-me-iam'.
A mesóclise é utilizada quando o verbo está no futuro do presente ou no futuro do pretérito e não há nenhuma palavra que exija a próclise. 
A inserção do pronome no meio do verbo reflete a correta aplicação das regras de colocação pronominal em contextos futuros sem palavras atrativas.

11.Ano: 2024 / Banca: FUNDEP Gestão de Concursos - FUNDEP / Prova: FUNDEP - HRTN - Médico - Área Anestesiologia - 2024 

Releia este trecho:

[yellow]“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Se disfarça de preguiça ou distração [...].”[reset]


Respeitadas as regras de colocação pronominal, o trecho pode ser reescrito, sem alteração no seu sentido, como:

A.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarçar-se-ia de preguiça ou distração [...].”
B.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarça se de preguiça ou distração [...].”
C.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarça-se de preguiça ou distração [...].”
D.“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Se disfarça-se de preguiça ou distração [...].”


Gabarito alternativa 'C'.

O item 'A' apresenta a forma [yellow]'Disfarçar-se-ia'[reset], que é uma mesóclise, usada em orações com verbos no futuro do presente ou futuro do pretérito. 
No entanto, a frase original está no presente do indicativo, o que torna essa reescrita inadequada. Mudando o sentido.

O item 'B' os pronomes enclíticos são aqueles que se unem ao verbo, formando uma única palavra com ele. Em português, isso é mais comum com os pronomes pessoais oblíquos átonos. Quando usados encliticamente, eles aparecem depois do verbo.

Exemplos de Pronomes Enclíticos:

[blue]Encontrar-me-ão[reset] -> (Eles me encontrarão)

[blue]Dizer-te-ei[reset] -> (Eu te direi)

[blue]Ajudar-nos-á[reset] -> (Ela nos ajudará)

Regras de Uso:

- São usados em construções afirmativas.

- Não são usados após palavras negativas, advérbios, pronomes relativos ou conjunções subordinativas.

[yellow]Observações:[reset]

Na língua formal e escrita, o uso dos pronomes enclíticos é bastante comum, especialmente para manter a eufonia (som agradável) da frase.

Em contextos informais ou na fala cotidiana, é mais comum o uso da próclise (pronome antes do verbo) ou da ênclise (pronome entre a partícula negativa e o verbo).


O item 'C' é o correto. Apresenta a forma [yellow]'Disfarça-se'[rset], que está correta, pois o pronome 'se' está corretamente posicionado após o verbo, 
formando uma ênclise. Esta reescrita mantém o sentido original da frase e respeita as regras de colocação pronominal. 

[red]O item D apresenta a forma 'Se disfarça-se', que é incorreta, pois há uma duplicação desnecessária do pronome 'se'. A forma correta seria 'disfarça-se'. [reset]

12. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - Prefeitura de São Bernardo do Campo - Inspetor - 2024 

A colocação pronominal atende à norma-padrão em:

A. A casa devia já ser velha; os tetos baixos e o soalho carunchoso tremiam quando me movimentava, arrastando os chinelos.
B. Na rua estreita e tortuosa, todos se conheciam, e o mesmo padeiro servia as famílias, sempre demorando-se de palestra pelas escadas.
C. Tão logo mudei para a nova casa, a primeira coisa que pude notar na vizinhança foi que não encontrava-se uma cara bonita, por ali.
D. Pelos buracos do rodapé, apareciam as baratas, que espalhavam-se de noite aos rebanhos, em cata de alimento para sobreviverem.
E. Me mudei para uma casa que nada tinha de confortável e resguardada, era apenas alta e mais clara que o primeiro andar da rua do Sol.

[bg_green] O item 'A' é o gabarito da questão.[reset]

No item 'A', '... tremiam [yellow]quando[reset] [blue]me[reset] movimentada....'

O pronome [yellow]'me'[reset] está corretamente posicionado antes do verbo 'movimentava', seguindo a regra da próclise, que é comum após conjunções subordinativas e advérbios e entre outros.

[yellow]A palavra "quando" é uma conjunção subordinativa temporal. Ela é usada para introduzir orações subordinadas que indicam uma circunstância de tempo relativa à ação principal da oração. Em outras palavras, "quando" conecta uma ação a um momento específico.[reset]

Exemplos de Uso de "Quando":

[yellow]Quando[reset] eu cheguei, ele já tinha saído. <- 'quando' -> [blue]conjunção subordinativa temporal[reset]

Nós vamos à praia [yellow]quando[reset] o tempo estiver bom. <- 'quando' -> [blue]conjunção subordinativa temporal[reset]

[yellow]Quando[reset] eu era criança, adorava brincar no parque. <- 'quando' -> [blue]conjunção subordinativa temporal[reset]

[red]Função Gramatical:[reset]

[blue]Conjunção Subordinativa Temporal:[reset] Estabelece uma relação temporal entre a oração principal e a subordinada.

[red]Observações:[reset]

[blue]"Quando" pode também ser usado em perguntas diretas ou indiretas, mas nesse caso, ele funciona como um advérbio interrogativo:[reset]

[yellow]Quando[reset] você vai chegar?

Não sei [yellow]quando[reset] ele vem.

O item 'B' está errado. Na frase 'Na rua estreita e tortuosa, todos se conheciam, e o mesmo padeiro servia as famílias, [yellow]sempre demorando-se [reset]de palestra...'
O pronome 'se' deveria estar antes do verbo 'demorando', [blue]formando a próclise obrigatória'sempre se demorando'.[reset]
[yellow]O advérbio de tempo 'sempre' no início da oração puxa o pronome antes do verbo, tornando a próclise obrigatória.[reset]

O item 'C' está errado.

A frase '...foi que [red]não[reset] [yellow]encontrava-se[reset] uma cara bonita, por ali.' Apresenta um erro de colocação pronominal. \n
O correto seria 'não se encontrava', utilizando a próclise. [red]Por regra, palavra negativas puxam o pronome para si, deixando o caso de próclise obrigatória.[reset]

O item 'D' está errado.

Na frase 'Pelos buracos do rodapé, apareciam as baratas, [yellow]que espalhavam-se[reset] de noite...'
O pronome 'se' deveria estar antes do verbo 'espalhavam', formando a próclise obrigatória, por regra, o pronome relativo 'que' o puxa.  -> [yellow]'se espalhavam'.[reset]
[red]Início de oração com pronome relativo, por regra, torna a próclise obrigatória.[reset]

[yellow]Me mudei[reset] para uma casa que nada tinha de confortável e resguardada, era apenas alta e mais clara que o primeiro andar da rua do Sol.' 
apresenta um erro de colocação pronominal. O correto seria 'Mudei-me', utilizando a ênclise.

Os pronomes pessoais oblíquos átonos em português incluem: [blue]me, te, se, lhe, nos, vos, lhes, o, a, os, as.[reset]
[red]Não devem ser utilizados no início de uma oração ou frase. [reset]

Exemplos Correto e Incorreto:

[red]Incorreto:[reset] [yellow]Me ajude [reset]com isso. <- [green]Próclise equivocada pelo contexto.[reset]

[blue]Correto:[reeset] [yellow]Ajude-me[reset] com isso. <- [green]ênclise obrigatória[reset]

[red]Incorreto:[reset] [yellow]Te espero [reset]na entrada. <- [green]Próclise equivocada pelo contexto.[reset]

[blue]Correto:[reset] [yellow]Espero-te[reset] na entrada. <- [green]ênclise obrigatória[reset]

[bg_green]Alternativas:[reset]

[blue]Próclise:[reset] Uso do pronome antes do verbo, geralmente precedido por palavras que atraem a próclise (palavras negativas, advérbios, pronomes relativos, etc.)

[red]Exemplo:[reset] Não me diga isso.

[blue]Ênclise:[reeset] Uso do pronome após o verbo, normalmente no início de frases ou após pausas.

[red]Exemplo:[reset] Diga-me a verdade.

[blue]Mesóclise:[reset] Uso do pronome no meio do verbo, em formas verbais futuras (mais comum em linguagem formal e escrita).

[red]Exemplo:[reset] Dizer-te-ei amanhã.


13.Ano: 2024 // Banca: CRS - Polícia Militar de Minas Gerais - CRS PMMG / Prova: CRS - PMMG - PM MG - Soldado Pós-Edital - 2024 - 5º Simulado

Identifique a alternativa em que ocorreu a correta substituição da expressão em destaque em “que nomeasse professor de desenho na Bahia o cidadão argentino Hector Bernabó” (l. 20-21) por um pronome oblíquo átono.

A. que nomeasse-lhe professor de desenho na.
B. que lhe nomeasse professor de desenho na.
C. que nomeasse-o professor de desenho na.
D. que o nomeasse professor de desenho na.

Gabarito da questão é a alternativa 'D'.

O item 'A' a substituição '[yellow]que nomeasse-lhe[reset] professor de desenho na...' está [red]incorreta.[reset] 
O pronome 'lhe' é utilizado SOMENTE para substituir 'objetos indiretos', enquanto o verbo 'nomear' é transitivo direto. Quem 'nomea', nomea algo ou 'para' alguem, exige um objeto direto. 
Portanto, a substituição não está de acordo com a regência verbal correta.

	O uso do pronome 'lhe' é para verbos que Exigem Preposição: (objeto indireto )

Exemplo: [yellow]Darei[reset] uma resposta [yellow]a ele.[reset] => [yellow]lhe[reset] darei uma resposta.

			[yellow]'darei'[reset] = verbo flexionado em que equm da algo, da algo a alguem ( verto transitivo ) <- [blue] sujeito da oração[reset]
			[yellow]'a ele'[reset] = preposição + pronome pessoal do caso reto 'ele' / objeto indireto ( com preposição )

			[yellow]lhe[reset] darei uma resposta. <- [blue]pronome em que substitui o objeto indireto 'a ele'[reset]

Exemplo: Vou contar [yellow]para ela[reset] o que aconteceu. => Vou [yellow]lhe[reset] contar o que aconteceu.

		[yellow]'vou contar'[reset] -> locução verbal sujeito da oração / quem conta conta algo, para alguém -> [red]verbo transitivo[reset]
		[yellow]'para ela' [reset]  -> preposição + pronome pessoal do caso reto 'ela => [red]objeto indireto  [reset]

[bg_red]No item 'b' também está inadequado o uso do pronome 'lhe' em próclise.[reset] Pelo mesmo motivo de uso inadequado.

					B. que [yellow]lhe[reset] nomeasse professor de desenho na...

	O pronome pessoal oblíquo átono 'lhe' é usado para orações em que o verbo transitivo exige objeto indireto, ou seja, com preposição inclusa.

[red]O item 'C' está inadequado o uso em ênclise pela oração iniciar com pronome relativo 'que' em que atrai o pronome.[reset]
			[bg_green]	O uso correto é com próclise obrigatória. Antes do verbo [reset]

[bg_green]Afirmativa 'D' a correta.[reset]

A substituição 'que o nomeasse professor de desenho na...' está correta. O pronome 'o' é adequado para substituir o objeto direto 'cidadão argentino Hector Bernabó', 
e sua posição antes do verbo 'nomeasse' está de acordo com a norma culta da Língua Portuguesa. Este item está de acordo com o gabarito da banca.


14.Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - Autoridade Portuária de Santos - Técnico Eletricista - 2024 
Assinale a alternativa redigida em conformidade com a norma-padrão de emprego e colocação dos pronomes.

A.O professor de português conheceu a literatura angolana e decidiu que iria estudar-lhe com mais profundidade.
B.Nunca lhe tinham contado que, na China, havia uma região em que as pessoas falavam a língua portuguesa.
C.Não convidaram-o para o curso de história da língua portuguesa que era ministrado na faculdade.
D.Estavam contentes por aprender sobre os diferentes sotaques do português e escutar-los ao vivo.
E.Ainda que faltassem-no informações sobre Moçambique, o poeta decidiu embarcar para o país africano.


O gabarito é letra 'B'.

O item 'A' está incorreto. 'O professor de português conheceu a literatura angolana e decidiu [yellow]que iria estudar-lhe[reseet] com mais profundidade.'

"lhe" é um pronome pessoal oblíquo átono que funciona como complemento indireto, ou seja, substitui objetos indiretos introduzidos por preposições como "a" ou "para". 
No entanto, na frase fornecida, o verbo "estudar" pede um complemento direto, 'quem estuda estuda o quê?' Não é um complemento indireto.	

Verbo "estudar": É um verbo transitivo direto, ou seja, precisa de um complemento direto (algo que se estuda, 'a literatura'), e não de um complemento indireto.
[blue]Uso Correto de "lhe": Deve ser usado com verbos que exigem complemento indireto, como "dar", "enviar", "oferecer", etc.[reset]

[blue]Frase Correta:[reset] O professor de português conheceu a literatura angolana e decidiu que iria [yellow]estudá-la[reset] com mais profundidade.

[blue]Portanto, ao corrigir a frase, substituímos "lhe" por "a", concordando com "literatura", que é feminino singular: "estudá-la".[reset] 
[blue]Isso garante que a frase esteja gramaticalmente correta e clara.[reset]

	Quando o verbo exige um objeto direto, usamos "o, a, os, as" dependendo do gênero e número do complemento direto.
	Os pronomes "o", "a", "os" e "as" são pronomes pessoais oblíquos átonos. Eles são usados como complementos diretos

	Para o complemento indireto, usamos "lhe, lhes".

Sofrem alterações na grafia os pronomes com o verbo terminados em -R, -S, -Z diante dos pronomes o, a, os, as:
            
            	Veja: Vamos [yellow]cantar[reset] os hinos. -> [yellow]Final -R[reset]
                
Vamos cantá-los. ( o verbo cantar fica oxítona com final 'a' acentuada e o substantivo 'os hinos' pelo pronome pessoal oblíquo átono 'os' acrescentando a letra 'l' )

[yellow]Cantamos os hinos[reset] -> Final -S // 'os hinos' -> substantivo para qual usamos o pronome pessoal do caso oblíquo átono 'os' acrescentando o 'l'.
                     
[yellow]Cantamo-los[reset] <- Não acentua o verbo pois a sílaba tônica está no 'ta'- paroxítona e retira o S e acrescenta o pronome 'los'.

Fiz o relatório -> Terminação -Z retira e 'o relatório' substantivo a qual será substituido pelo pronome pessoal do caso oblíquo átono 'o' acrescentado de 'l'.

[yellow]Fi-lo.[reset] <- 'lo' pronome que substitui 'o relatório' <- substantivo

[blue]Portanto, ao corrigir a frase, substituímos "lhe" por "a", concordando com "literatura", que é feminino singular: "estudá-la". [reset]


[bg_green]Item correto.[reset] [yellow]Nunca lhe[reset] tinham contado que, na China, havia uma região em que as pessoas falavam a língua portuguesa.

Além da próclise ser obrigatória pelo fato do advérbio puxar o pronome. O pronome "lhe" está empregado corretamente como complemento indireto.

O verbo "contar" é transitivo direto e indireto, o que significa que ele pode exigir:

 um objeto direto ([blue]o que é contado?[reset]) e um objeto indireto (a quem se conta algo: [blue]ele ou ela[reset]).

[red]Complemento Direto:[reset] [yellow]que, na China, havia uma região em que as pessoas falavam a língua portuguesa.[reset]

[red]Complemento Indireto:[reset] O pronome "lhe" substitui o complemento indireto "a ele" ou "a ela".

Exemplo: Nunca contaram [yellow]a ele/ela[reset] que...  <- 'a' -> preposição / 'ele/ela' => pronome pessoal do caso reto

[blue]Com Pronome:[reset] Nunca [yellow]lhe[reset] contaram que...

[bg_red]O item C apresenta um erro de colocação pronominal. [reset]
		[red]Não convidaram-o[reset] para o curso de história da língua portuguesa que era ministrado na faculdade.

O correto seria [yellow]'Não o convidaram [reset]para o curso de história da língua portuguesa que era ministrado na faculdade'.

[blue]O pronome oblíquo átono 'o' deve vir antes do verbo em orações negativas. [reset]  [red] Por regra, é próclise obrigatória[reset]


[red]O item D apresenta um erro na colocação do pronome 'los'.[reset]

		Estavam contentes por aprender sobre os diferentes sotaques do português e [red]escutar-los[reset] ao vivo.

O correto seria [yellow]'e escutá-los ao vivo'[reset], [blue]pois o pronome oblíquo átono deve ser ligado ao verbo por hífen quando este está no infinitivo impessoal.[reset]


[red] O item 'E' está incorreto.[reset]

			Ainda que [yellow]faltassem-no[reset] informações sobre Moçambique, o poeta decidiu embarcar para o país africano.

	[red]Verbo "faltar": É um verbo transitivo indireto, que exige um complemento indireto (usualmente precedido pela preposição "a").[reset]
		[blue]Ele é indireto porque ele requer um complemento introduzido por uma preposição para completar seu sentido.[reset]

						[bg_red]Objeto Indireto: "Lhe" (a ele, ao poeta)[reset]

Exemplos:

Sem Complemento:

"Faltam informações." (A frase é compreensível, mas incompleta. Precisamos saber a quem ou a quê essas informações estão faltando.)

Com Complemento Indireto:

"Faltam informações ao professor." (Aqui, "ao professor" é o complemento indireto. [blue]'ao' -> preposição 'a' + artigo 'o' )[reset]

"Faltam dois dias para a viagem." (Aqui, "para a viagem" é o complemento indireto.) [blue]'para' -> preposição [reset]

"no": A combinação "no" não é apropriada porque "o" é um pronome oblíquo que substitui objetos diretos, e não é precedido por "a". O verbo "faltar" exige um objeto indireto.

"lhe": Este pronome é usado corretamente para objetos indiretos, substituindo "a ele" ou "a ela". [bg_red]Objeto Indireto: "Lhe" (a ele, ao poeta)[reset]


15. Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN / Prova: IDECAN - Agente da Mobilidade Urbana Pós-Edital - 2024 - 1º Simulado

Com base no trecho "Mas aí lhe tiraram a roça." do texto fornecido, avalie as alternativas a seguir quanto à colocação pronominal adequada e escolha a correta.

A. Mas aí tiraram-lhe a roça, refletindo a colocação pronominal mesoclítica, adequada ao contexto formal da escrita.
B. Tiraram-lhe a roça aí, demonstrando o uso correto da próclise, influenciado pela presença de uma palavra negativa.
C. Mas aí a roça lhe tiraram, ilustrando uma ênclise, que é inadequada pela presença de palavra atrativa anterior.
D. A colocação pronominal em "lhe tiraram" é um exemplo correto de próclise, influenciada pela conjunção subordinativa "Mas".

Gabarito 'D'

O item A sugere que a frase 'Mas aí tiraram-lhe a roça' é um exemplo de mesóclise. No entanto, isso é incorreto. A mesóclise ocorre quando o pronome é colocado no meio do verbo.

O item B sugere que a frase 'Tiraram-lhe a roça aí' é um exemplo de próclise, influenciada pela presença de uma palavra negativa. No entanto, isso é incorreto. A próclise ocorre quando o pronome é colocado antes do verbo.

O item C sugere que a frase 'Mas aí a roça lhe tiraram' é um exemplo de ênclise. No entanto, isso é incorreto. 
A ênclise ocorre quando o pronome é colocado após o verbo, mas a presença da palavra 'Mas' no início da frase atrai o pronome para antes do verbo (próclise).

O item D sugere que a colocação pronominal em 'lhe tiraram' é um exemplo correto de próclise, influenciada pela conjunção subordinativa 'Mas'. 
Isso está correto. A próclise ocorre quando o pronome é colocado antes do verbo, e a presença da conjunção 'Mas' no início da frase atrai o pronome para essa posição.

16. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP / Prova: IDCAP - Prefeitura de Vila Rica - Fonoaudiólogo - 2024

Ele acrescentou 'que' existem alguns métodos 'que' as pessoas podem usar para reprimir espirros sem fechar o nariz e a boca.

Os vocábulos destacados são, respectivamente:

A. Pronome relativo e pronome relativo.
B. Conjunção integrante e pronome relativo.
C. Pronome relativo e conjunção integrante
D. Conjunção integrante e conjunção integrante.

O item B está correto e de acordo com o gabarito da banca. Ele corretamente identifica que na primeira ocorrência, o 'que' funciona como uma conjunção integrante, introduzindo uma oração subordinada substantiva. 
Na segunda ocorrência, o 'que' funciona como um pronome relativo, introduzindo uma oração adjetiva e retomando o substantivo 'métodos'.


17. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP / Prova: IDCAP - Prefeitura de Vila Rica - Fonoaudiólogo - 2024

Isso' causa lesões, como ruptura de tímpanos, aneurismas e até costelas quebradas.
Morfologicamente, pelo contexto da frase, o vocábulo destacado trata-se de pronome:

A. Indefinido adjetivo
B. Demonstrativo adjetivo.
C. Demonstrativo substantivo.
D. Indefinido substantivo.

[red]'isso' é um substantivo demonstrativo. 'isso' está substituindo um termo ou ideia anterior expressa, funcionando como substantivo mesmo. Isolado, sem qualificação[reset]

18. Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - Câmara de Maria da Fé - Assessor - Área: Finanças, Contabilidade e Pessoal - 2024 

Analise o emprego do pronome “cuja”: “[...] em pensemos, por exemplo, em pessoas cuja situação as impede de realizar escolhas, [...]” (5º§). O pronome está adequadamente empregado. Assinale a alternativa que não cumpre com as regras de concordância em relação ao uso do pronome “cujo”.

A. Há situação cujo objetivo requer prioridade.
B. A casa cuja cores foram modificadas ficou mais estilosa.
C. O episódio novo da série cujas cenas foram bem produzidas me chamaram atenção.
D. O homem, cujos atributos foram mencionados, recebeu a promoção merecidamente.


Gabarito letra 'B'
B. A casa [yellow]cuja[reset] cores foram modificadas ficou mais estilosa.

O pronome 'cujo' deve concordar em gênero e número com o substantivo que o segue. 
A frase correta seria 'A casa [yellow]cujas[reset] cores foram modificadas ficou mais estilosa'.

19. Ano: 2024 / Banca: Fundação Mariana Resende Costa - FUMARC / Prova: FUMARC - Câmara de Lagoa da Prata - Controlador Interno - 2024 

O segredo está em ler [yellow]o que[reset] se acabou [yellow]de[reset] escrever ...

Assinale a alternativa em que se classificam, respectivamente, os termos sublinhados.

A. artigo – conjunção – preposição
B. artigo – pronome – conjunção
C. pronome – pronome – preposição
D. pronome – conjunção – conjunção
 

	Gabarito letra 'C'.
Esta classificação está correta: 'o' é um pronome demonstrativo, 'que' é um pronome relativo e 'de' é uma preposição.

20. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura do Município de Valinhos - Professor II - Área Matemática - 2024 

O pronome demonstrativo que introduz o excerto “Esse é o principal indicador do interesse de um indivíduo por um cheiro.” atua, no contexto em que ocorre, como um elemento de coesão textual de referenciação. Isso porque é empregado para:

A. introduzir um novo elemento na sequência textual.
B. retomar um elemento já mencionado na sequência textual.
C. estabelecer uma relação de hiponímia com outro elemento da sequência textual.
D. estabelecer uma relação de hiperonímia com outro elemento da sequência textual.
E. estabelecer uma relação de sinonímia com outro elemento da sequência textual.

Gabarito letra 'B'.

O item A sugere a substituição de 'no qual' por 'em que' e 'que' por 'as quais'. 
A substituição está correta, pois 'em que' é uma forma válida de pronome relativo que retoma 'relatório' e 'as quais' retoma 'tragédias', mantendo a coesão e a concordância adequadas.

Pronome relativo retoma algo dito anteriormente.

Pronome demonstrativo também. Os pronomes demonstrativos dão ideia de espaço presente, passado ou passado distante.

Espaço presente: este (1° pessoa)

Espaço Passado: Esse (2° Pessoa)

Espaço Passado muito distante: Aquele "dia"(3° Pessoa)

21. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRC RR - Técnico de Informática - 2024 

'Trata‑se da Regra do Número 72, que mostra em quanto...'

Seria mantida a correção gramatical do texto caso o pronome “se” (linha 14) fosse deslocado para o início do período, da seguinte forma: Se trata.

C.Certo
E.Errado

A colocação pronominal em português segue regras específicas. 
No caso do pronome 'se', a próclise (colocação do pronome antes do verbo) é obrigatória quando há palavras atrativas, como advérbios, pronomes relativos, pronomes indefinidos, conjunções subordinativas, entre outros. 
No trecho 'Trata-se da Regra do Número 72', o verbo 'tratar' está no início da oração, e não há palavra atrativa que justifique a próclise. 
Portanto, a forma correta é 'Trata-se' e não 'Se trata'. A próclise seria incorreta nesse contexto, pois não há elemento que a justifique.		

22. Ano: 2024 / Banca: Projetos para Municípios - PROMUN / Prova: PROMUN - Câmara de São José do Barreiro - Assistente Legislativo - 2024
Em relação às classes de palavras, observe as afirmativas abaixo com atenção, sobretudo para os termos destacados e assinale a alternativa cuja classificação indicada em parênteses está incorreta:

A. “...alcançariam o país VIZINHO...” (adjetivo)
B. “... as montanhas QUE circundavam a cidade.” (pronome relativo)
C. “Precisamos do SENHOR . (Pronome de tratamento)
D. “...no colo do seu neto de TREZE anos.” (numeral ordinal)

 O termo 'TREZE' é um numeral, mas é classificado como numeral cardinal, não ordinal. Numerais cardinais indicam quantidade (um, dois, três...), 
enquanto numerais ordinais indicam ordem (primeiro, segundo, terceiro...). 
Portanto, a classificação está incorreta e o item está de acordo com o gabarito da banca.

23.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - MPE AM - Agente de Apoio - Área: Administrativa Pós-Edital - 2024 - 1º Simulado

Assinale a alternativa em que, assim como no trecho “Há uma passividade no ressentimento, que não se confunde com uma imobilidade”, não há erro de colocação pronominal.

A. Se tratava de certa desconfiança.
B. Quando trata-se de desconfiança?
C. Todos sabiam disto: não se tratava de desconfiança.
D. Tratar-se-ou de incontestável desconfiança.
E. Afirmou que tratava-se de desconfiança.

Gabarito letra 'C'

No item 'A' por regra, não iniciar frases com pronoes pessoais oblíquos. O correto seria ' Tratava-se de...'

No item 'B' está errado a colocação devido a oração ser interrogativa direta. Sendo assim, é próclise obrigatória. Antes do verbo.

O item 'C' está correto. 'Não se tratava de desconfiança' segue a regra de próclise, onde o pronome 'se' é atraído para antes do verbo pela presença da negação 'não'.

O item 'D' está errado. O uso de mesóclise somente para os tempos verbais futuro do pretérito e futuro do presente. Ou seja, 'Tratar-se-ia'.

O item 'E' está errada. Devido a conjunção subordinativa 'que' a próclise é obrigatória. Ou seja, 'Afirmou que se tratava de desconfiança.'

24.Ano: 2024 / Banca: MS Concursos / Prova: MS Concursos - SAAE Manhuaçu - Ajudante Administrativo - 2024

Considerando as normas de colocação pronominal, assinale a alternativa que contém a frase gramaticalmente correta.

A. Jamais esquecerei-me daqueles momentos que passamos juntos.
B. Não aceitaram-me naquele emprego.
C. “Se vai a primeira pomba despertada”.
D. Dar-me-iam água para lavar as mãos?

Gabarito letra 'D'

No item 'A' estaa errado o emprego do pronome pessoal oblíquo átono 'me'. A próclise é obrigatória em frases iniciadas por advérbios, portanto o correto seria 'Jamais me esquecerei daqueles...'

No item 'B' está errado o emprego do pronome 'me'. A próclise é obrigatória em orações negativas. O correto seria 'Não me aceitaram naquele...'

No item 'C' está errado o emprego do pronome pessoal do caso oblíquo 'se'. Não pode iniciar frases com o pronome. por regra.

O item 'D' está correto. A frase 'Dar-me-iam água para lavar as mãos?' está de acordo com o gabarito da banca, pois segue corretamente a regra de colocação pronominal. 
Neste caso, utiliza-se a mesóclise, que é a inserção do pronome no meio do verbo, aplicável a verbos no futuro do presente ou no futuro do pretérito, como em 'dar-me-iam'.

A mesóclise é utilizada quando o verbo está no futuro do presente ou no futuro do pretérito e não há nenhuma palavra que exija a próclise. 
A inserção do pronome no meio do verbo reflete a correta aplicação das regras de colocação pronominal em contextos futuros sem palavras atrativas.

25. Ano: 2024 / Banca: FUNDEP Gestão de Concursos - FUNDEP / Prova: FUNDEP - HRTN - Médico - Área Anestesiologia - 2024 

Releia este trecho:

“Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Se disfarça de preguiça ou distração [...].”

Respeitadas as regras de colocação pronominal, o trecho pode ser reescrito, sem alteração no seu sentido, como:

A. “Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarçar-se-ia de preguiça ou distração [...].”
B. “Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarça se de preguiça ou distração [...].”
C. “Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Disfarça-se de preguiça ou distração [...].”
D. “Como uma ladra sorrateira, a procrastinação rouba tempo, energia e potencial. Se disfarça-se de preguiça ou distração [...].”

Gabarito letra 'C'.

O item 'A' está errado. Apesar de gramaticalmente esta correto, o sentido muda. O verbo está no futuro do pretérito 'Se disfarçaria', mudando o sentido da oração.
O item 'B' está errado. O pronome pessoal do caso oblíquo 'se' é pronome enclítico.
Os pronomes enclíticos são aqueles que são colocados após o verbo, formando com ele uma única palavra. 
Eles são comuns no português formal e escrito, e são particularmente usados com pronomes pessoais oblíquos átonos. Aqui estão alguns exemplos e regras de uso:

Regras de Uso de Pronomes Enclíticos:

Uso Após Verbo: O pronome é adicionado diretamente após o verbo, formando uma única palavra.

Exemplo: Ajude-me.

Verbos no Futuro do Presente ou Futuro do Pretérito: Aqui, é mais comum usar a mesóclise (pronome no meio do verbo), mas a ênfase eufônica ainda pode usar a ênclise.

Exemplo: Ajudar-me-á.

Imperativo Afirmativo: O pronome átono deve ser usado em ênclise.

Exemplo: Diga-me.

Exemplos de Uso:

Presente do Indicativo:

"Encontrei-o no parque."

Infinitivo Pessoal:

"Dizer-te o que penso."

Gerúndio:

"Estou ajudando-o."

Futuro do Presente:

"Dar-te-ei uma resposta amanhã."

A alternativa C é a correta e a última a 'D' está duplicado o pronome, totalmente errado.

26. Ano: 2024 / Banca: Instituto Mais - IMAIS / Prova: IMAIS - Câmara de Santo André - Agente Legislativo - 2024

Assinale a alternativa cujas palavras, entre parêntesis, substituam os termos destacados, em conformidade com a norma-padrão da Língua Portuguesa.

A. “... os seres humanos fizeram uma compensação”. (fizeram-na)
B. “... têm a mesma importância ou até maior”. (têm-la)
C. “... realmente geram profundas mudanças cognitivas”. (geram-lhes)
D. “... os seres humanos possuem cérebros maiores”. (lhes possuem)

O gabarito da questão é a alternativa 'A'. A única correta.

O item 'A', o pronome pessoal oblíquo átono 'a' se refere ao substantivo 'uma compensação', ou seja, '... os seres humanos [yellow]fizeram-na.[reset]

O  item 'A' está correto. Quem faz, faz algo. 'fazer' é transitivo direto e indireto, portanto o complemento do verbo pode ser objeto direto ( 'uma compensação' ) ou indireto ( 'os seres humanos' )
		Por isso a grafia está correta.

Sofrem alterações na grafia os pronomes com o verbo terminados em -R, -S, -Z diante dos pronomes o, a, os, as:
		- Para: [yellow]lo, la, los, las[reset] [blue]( mas somente para verbos terminados co -R, -S, -Z )[reset]

[red]Os Sons nasais com finais -M, -ÃO, -ÕE DIANTE DOS PRONOMES O, A, OS, AS:[reset]
		- Para: [yellow]no, na, nos, nas [reset]

	[bg_green]O verbo 'fizeram' termina com a consoante -M e o pronome deve concordar em número e gênero com o substantivo, portanto é fizeram-na.[reset]

[red]O item 'B' está incorreto.[reset] A alteração na grafia do pronome está errada. O verbo 'têm' termina com '-M', portanto o correto seria 'têm-na'.

[red]O item 'C' está incorreto.[reset ] Quem gera, gera algo, geram profundas mudanças... Portanto é um verbo transitivo direto em que exige-se um complemento direto.
	[red]O pronome 'lhes' é usado em complementos INDIRETOS. [reset]
		Sendo assim, a grafia correta para o pronome é 'na' em retomada/referência ao substantivo 'profundas'. 
O verbo 'geram' termina com -M, portanto ocorre mudança na grafia dos pronomes pessoais oblíquos átonos para no, na, nos,nas. A Depender do gênero e número do substantivo.

O item 'D' está incorreto. Quem possue, possue algo. Possui 'cérebros maiores', portanto é um verbo transitivo direto em que precisa de um complemento direto.
	[red]O pronome 'lhes' é usado em complementos indiretos.[reset]
		[blue]O correto seria [reset]: [yellow]'... os seres humanos possuem-nos ( concordando em gênero e número, no caso masculino e plural )[reset]

27.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de Caraguatatuba - Professor - Área: Educação Infantil - 2024 

Os pronomes possessivos são empregados basicamente para indicar a propriedade de algo, como ocorre no seguinte caso:

A. Aquela é a minha casa e meu castelo.
B. Um povo ignorante é instrumento cego de sua própria destruição.
C. Eu não tenho mensagem. Minha mensagem é minha vida.
D. Aqueles que eliminam os olhos das pessoas, as reprovam pela sua cegueira.
E. Todo homem tem seu preço.

Gabarito da questão é o item 'A'. Com sentido de algo tangível onde utiliza 'minha' e 'meu' para indicar a propriedade da casa e do castelo.

No item 'B' temos uma frase em que utiliza o pronome possessivo 'sua' para indicar que o povo ignorante é o própria instrumento para destruição. Algo abstrato.
Ou seja, para indicar uma consequência ou resultado e não um posse no sentido estrito.

No item 'C' o pronome possessivo 'minha' é utilizado para identificar uma equivalência e não posse no sentido estrito.

No item 'D' o pronome possessivoo 'sua' é utilizado para indicar uma condição ou estado e não uma posse no sentido estrito.

No item 'E' o pronoe possessivo 'seu' é utilizado para indicar uma condição atribuida e não uma posse no sentido estrito.

28.Ano: 2024 / Banca: Instituto AOCP / Prova: Instituto AOCP - Câmara de Nova Iguaçu - Analista Contábil - 2024

Qual frase apresenta o uso adequado da colocação do pronome obliquo “se”, de acordo com a norma culta da língua portuguesa?

A. “Promulgou-se em 1828 a lei que redefiniu as câmaras municipais.”
B. “Não esqueceram-se das antigas atribuições das câmaras municipais.”
C. “As câmaras municipais reorganizariam-se a partir da nova lei.”
D. Para reorganizarem-se as câmaras municipais, foi necessária a promulgação da lei.”
E. “Se adaptaram logo às regras estabelecidas pela nova lei.”

Gabarito letra 'A'. O pronome 'se' está corretamente colocado em ênclise, pois o verbo está no início da oração.

O item 'B' está INCORRETO. A frase é um oração subordinativa negativa, portanto, a próclise é obrigatória. O correto seria: 'Não se esqueceram das...'

O item 'C' está INCORRETO. Em orações afirmativas é correto o uso de ênclise, porém o verbo está no futuro do pretérito do subjuntivo daí a próclise é FACULTATIVA.
			[blue]o mais adequado seria o uso de mesóclise: 'reorganiza-se-iam' a partir da nova lei.[reset]

O item 'D' está INCORRETA. A frase '[yellow]Para reorganizarem-se[reset] as câmaras municipais, foi necessária a promulgação da lei.' está incorreta. 
A presença da preposição 'para' exige a próclise: [yellow]'Para se reorganizarem[reset] as câmaras municipais, foi necessária a promulgação da lei.'

O item 'E' está INCORRETO. Não utiliza pronomes pessoal do caso oblíquo em inicio de frases.

29. Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - Prefeitura de Nova Iguaçu - Auxiliar de Serviços Gerais - 2024

Assinale a alternativa em que há uma correlação INADEQUADA entre a expressão destacada e a sua classificação gramatical.

A. “É impossível ser feliz o tempo [yellow]todo[reset] ou em todo lugar.” (5º§) – pronome indefinido.
B. “[yellow]Ela[reset] se manifesta na cultura popular, em livros de autoajuda, terapias e palestras de motivação.” (1º§) – pronome pessoal.
C. “Muitas vezes, aliás, quanto mais as pessoas procuram a felicidade, menos parecem capazes de obtê-[yellow]la.[reset]”(4º§) – pronome reflexivo.
D. “Crianças altamente alegres estão associadas com o maior risco de mortalidade na idade adulta por [yellow]seu[reset] envolvimento em comportamentos arriscados.” (2º§) – pronome possessivo.

Gabarito letra 'C'.

O item 'A' está correto. [yellow]todo, todos, toda, todas - tudo[reset] são pronomes indefinidos
O item 'B' está correto. 'ela' é pronome pessoal do caso reto.
O item 'C' está ERRADO. O pronome pessoal do caso oblíquo 'a' não é reflexivo.

[bg_red] Os pronomes oblíquos átonos : me, nos, te, vos, se -> podem indicar ação praticada pelo próprio sujeito. Tais pronomes são chamados de pronomes reflexivos.[reset]

	Eu [yellow]me[reset] machuquei. 'me' - ( a mim mesmo ) => [yellow]pronome reflexivo[reset]

    Os pronomes oblíquos tônicos: SI e CONSIGO são sempre reflexivos.

    	Márcia só pensa em [yellow]si[reset] -> ( pensa nela mesma ) <- [yellow] Pronome substantivo reflexivo pessoal do caso oblíquo tônico [reset]

       	Ele trouxe [yellow]consigo[reset] o livro -> ( com ele mesmo ) <- [yellow] Pronome adjetivo reflexivo pessoal do caso oblíquo tônico [reset]
           
	Maneiras erradas:

    	Marcos, eu preciso falar consigo [bg_red](ERRADO)[reset]
        [red] Não como seria 'contigo', além de ser pronome reflexivo em que pratica a ação é o próprio sujeito. [reset]
            [red] 'consigo' => preposição 'com' + pronome 'ti' referindo a 2º pessoa do discurso. [reset]
                    [green] O correto seria '... eu preciso falar contigo [reset] -> [blue]preposição 'com' + pronome pessoal oblíquo tônico[reset]
                        [yellow] Além disso os pronomes pessoais tônicos precisam anteceder preposição [reset]\n

        	Eu gosto muito de SI, minha amiga. [bg_red](ERRADO)[reset]            
            [red] 'SI' é pronome reflexivo, quem pode praticar a ação é o próprio sujeito.[reset]\n
            [red] Precisa de um pronome que refira a 2º pessoa do discurso, 'ti', pronome oblíquo tônico da 2º pesssoa que não é reflectivo. [reset]

O item 'D' está correto. O pronome 'seu' é da classe dos pronomes possessivos.

Para cada pronome pessoal do caso reto temos pronomes possessivos específicos:

                - Para associar 1º pessoa do discurso, pronome pessoal EU temos: MEU, MINHA, MEUS, MINHAS
                        
                        Exemplos: Meu lápis, Minhas roupas, meu tênis.

                - Para associar a 2º pessoa do discurso do pronome pessoal TU temos: TEU, TUA, TEUS, TUAS

                        Exemplos: Teu lápis, tua casa, tuas ideias
                
                - Para associar a 3º pessoa do discurso a que se refere ao pronome pessoal ELE, temos: SEU, SUA, SEUS, SUAS

                        Exemplos: Seu lápis, sua ideia, seus livros, suas roupas

                - Para associar a 1º pessoa do discurso no plural a que se refere o pronome pessoal do caso reto:
                    temos: nosso, nossa, nossos, nossas

30. Ano: 2024 / Banca: Instituto Sagaz - IS / Prova: IS - Prefeitura de Carmo do Rio Claro - Secretário Escolar - 2024

Complete a frase: Senhores, __________ quando __________.

A. me avisem, telefonarem-vos
B. avisem-me, telefonarem-vos
C. avisem-me, vos telefonarem
D. me avisem, vos telefonarem
E. avisem, telefonarem

O gabarito da questão é a letra 'C'. A cojunção subordinativa temporal 'quando' atrai os pronomes para perto. Portanto é:

			Senhores, [yellow] avisem-me[reset] quando [yellow]vos telefonarem[reset]

31. Ano: 2024 / Banca: Fundação CESGRANRIO - CESGRANRIO / Prova: CESGRANRIO - Concurso Nacional Unificado - CNU - Bloco 8 - Nível Intermediário – Português - Pós-Edital - 2024 - 4º Simulado

Nas passagens abaixo, a palavra destacada corresponde corretamente à sua classificação gramatical em:

A. Está certo [yellow]que[reset] todos os adultos mantêm uma parcela de infância ... – pronome relativo.
B. Além disso, o julgamento do [yellow]outro[reset] não nos incomoda... – pronome demonstrativo.
C. [yellow]Pois[reset] parece que é dessa maneira que os adultos têm se comportado publicamente – conjunção coordenativa conclusiva.
D. "...[yellow]aliás[reset], parece que nos orgulhamos disso ... – palavra denotativa retificadora.
E. "..mostra uma criança com o dedo no nariz [yellow]enquanto[reset] o narrador diz “limpar o salão” – conjunção subordinativa adverbial de proporção.

Gabarito letra 'D'.

	A. Está certo [yellow]que[reset] todos os adultos mantêm uma parcela de infância ... – conjunção integrante

O termo 'que' neste contexto funciona como conjunção integrante, introduzindo uma oração subordinada substantiva. 
Ele não retoma um termo anterior nem estabelece uma relação de relativização, o que caracterizaria um pronome relativo.

	B. Além disso, o julgamento do [yellow]outro[reset] não nos incomoda... – pronome indefinido

O termo 'outro' é da classe dos pronomes indefinidos: [yellow]outro, outras, outra, outras - outrem[reset]

	C. [yellow]Pois[reset] parece que é dessa maneira que os adultos têm se comportado publicamente – conjunção coordenativa explicativa

'Pois' é empregado aqui como uma conjunção explicativa, e não conclusiva. 
Seu papel é introduzir uma explicação ou justificativa para a afirmação anterior, e não uma conclusão derivada das ideias anteriores. 


	D. "...[yellow]aliás[reset], parece que nos orgulhamos disso ... – palavra denotativa retificadora.

Aliás' é corretamente identificado como uma palavra denotativa retificadora. 
Ela é utilizada para introduzir uma retificação ou um esclarecimento em relação ao que foi dito anteriormente. 
Este uso está de acordo com o gabarito da banca, refletindo a função de 'aliás' de adicionar uma informação que corrige ou modifica o que foi mencionado antes.


	E. "..mostra uma criança com o dedo no nariz [yellow]enquanto[reset] o narrador diz “limpar o salão” – oração subordinada temporal

A conjunção 'enquanto' é classificada incorretamente como adverbial de proporção. 
Na verdade, 'enquanto' introduz uma oração subordinada adverbial temporal, indicando simultaneidade de ações. 
A função de proporção não se aplica a este contexto, pois a relação estabelecida é de tempo e não de proporção.

32.Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Câmara de Vinhedo - Controlador Interno - 2024 
Analise as sentenças a seguir quanto ao emprego do vocábulo “a” em destaque e assinale a alternativa em que sua função é a de pronome demonstrativo.

A. Meus pais e eu já estamos [yellow]a[reset] caminho do restaurante.
B. Os executivos começaram a discutir [yellow]a[reset] respeito do preço do dólar.
C. [yellow]A[reset] prateleira de livros já foi instalada e está pronta para uso.
D. Não compare sua forma de ver o mundo com [yellow]a[reset] de Cecília.
E. A garota gostaria que [yellow]a[reset] tratassem de outra forma.

Gabarito letra 'D'.

O pronome demonstrativo possui valor substantivo 'o','a','os','as'

        [yellow] o = aquele / aquilo <- pronome demonstrativo substantivo[reset]
        [blue]   a = aquela / <- pronome demonstrativo substantivo[reset]
        [green] os = aqueles  <- pronome demonstrativo substantivo[reset]
        [red]   as = aquelas  <- pronome demonstrativo substantivo[reset]

        Exemplo:

            Ele sempre consegue [yellow]o[reset] [blue]que[reset] deseja.

            'o'   = pronome demonstrativo -> 'aquele' / 'aquilo' <- pronome demonstrativo substantivo
            'que' = pronome relativo -> 'o qual' -> pronome relativo variável masculino

                Ele sempre consegue [yellow] aquilo [reset] [green] o qual [reset] deseja.

	[bg_red] MACETE! Substitua o pronome 'a' por 'aquela' na frase. [reset]

		A. Meus pais e eu já estamos [yellow]a[reset] caminho do restaurante.

		'a' é uma preposição que indica direção ou movimento. 

B. Os executivos começaram a discutir [yellow]a[reset] respeito do preço do dólar.

No item B, 'a' é uma preposição que introduz o complemento 'respeito'. 
A frase 'Os executivos começaram a discutir a respeito do preço do dólar' utiliza 'a' para ligar o verbo 'discutir' ao seu complemento. 
Portanto, não é um pronome demonstrativo.


			C. [yellow]A[reset] prateleira de livros já foi instalada e está pronta para uso.

			No item C, 'a' é um artigo definido que antecede o substantivo 'prateleira'.


			D. Não compare sua forma de ver o mundo com [yellow]a[reset] de Cecília.

No item D, 'a' é um pronome demonstrativo que substitui o substantivo 'forma de ver o mundo'. 
A frase 'Não compare sua forma de ver o mundo com a de Cecília' utiliza 'a' para retomar 'forma de ver o mundo'.
De qualquer forma, o pronome demonstrativo 'aquela' pode substituir o 'a' sendo assim:

			Não compare sua forma de ver o mundo com [yellow]aquela[reset] de Cecília

			E. A garota gostaria que [yellow]a[reset] tratassem de outra forma.

No item E, 'a' é um artigo definido que antecede o substantivo 'garota'. 
A frase 'A garota gostaria que a tratassem de outra forma' utiliza 'a' para definir o substantivo 'garota'. Portanto, não é um pronome demonstrativo.

33. Ano: 2024 / Banca: CRS - Polícia Militar de Minas Gerais - CRS PMMG / Prova: CRS - PMMG - PM MG - Soldado Admissão ao Curso de Formação de Soldados – CFSd QP-PM - Pós-Edital - 2024 - 2º Simulado

Assinale a alternativa em que é adequada a substituição do termo destacado por um pronome.

A. “Quando me lembro disso, lamento [yellow]a condição de Ofélia[reset] [...]” – Quando me lembro disso, lamento-lhe
B. “[...] e entre os meus antepassados não sei de algum que tenha levantado [yellow]a arma[reset] [...]” – e entre os meus antepassados não sei de algum que tenha levantado-a
C. “A Pedro, um velho marinheiro sardento, eles lembram apenas [yellow]as tabernas inglesas.[reset]” – A Pedro, um velho marinheiro sardento, eles lembram-nas apenas
D. “[...] a me sugerirem [yellow]longos cruzeiros por oceanos infestados de piratas malaios[reset] [...]” – a me sugerirem-lhes

O gabarito é letra 'C'.

			“Quando me lembro disso, lamento [yellow]a condição de Ofélia[reset] 

O termo “a condição de Ofélia” é objeto direto da forma verbal “lamento”. Quem lamenta, lamenta algo. Lamenta a condição de ofélia.
Portanto, somente pode ser substituído pelo pronome oblíquo átono “a”, uma vez que “lhe”, quando complemento verbal, funciona como objeto indireto. 
Veja-se a redação correta:
					Quando me lembro disso, lamento-[yellow]a.[reset]

		“[...] e entre os meus antepassados não sei de algum que tenha levantado [yellow]a arma[reset] [...]” – 

O termo “a arma” é objeto direto do tempo composto “tenha levantado”. Portanto, deve ser substituído pelo pronome oblíquo átono “a”. 
Entretanto, é ilícita a ênclise ao particípio de tempos verbais composto. 

Veja-se a redação correta:

				e entre os meus antepassados não sei de algum que [yellow]a[reset] tenha levantado



			C. “A Pedro, um velho marinheiro sardento, eles lembram apenas [yellow]as tabernas inglesas.[reset]” 

O termo “as tabernas inglesas” é objeto direto da forma verbal “lembram”. Quem lembra, lembra de algo. Das tabernas inglesas.
Portanto, é corretamente substituído pelo pronome oblíquo átono “as”. 
Em razão de este estar ligado a verbo terminado em som nasal, emprega-se a sua variante “nas”.
				
						'... eles lembram-nas...'


	
		D. “[...] a me sugerirem [yellow]longos cruzeiros por oceanos infestados de piratas malaios[reset] [...]” – 

O termo “longos cruzeiros por oceanos infestados de piratas malaios” é objeto direto da forma verbal “sugerirem”. Quem sugere, sugere algo. Sugere longos cruzeiros...
Portanto, o verbo sugerir é transitivo direto a qual precisa do complemento direto. 
Portanto, somente pode ser substituído pelo pronome oblíquo átono “os. /  “lhe”, quando complemento verbal, funciona como objeto indireto.

						'... a me sugerirem-os.'

34. Ano: 2024 / Banca: Associação dos Municípios do Extremo Oeste de Santa Catarina - AMEOSC / Prova: AMEOSC - Prefeitura de São Miguel do Oeste - Auxiliar de Creche - 2024

	"Ele nunca atende [yellow]ligações[reset] de números desconhecidos, pois "ou é golpe, ou é marketing."

Em relação à colocação pronominal no período acima, ao substituir a expressão destacada pelo pronome átono correspondente deverá ocorrer:

A. próclise, visto que os pronomes demonstrativos atraem os pronomes.
B. mesóclise, pois o pronome ficará intercalado com o verbo, ligando- o por meio de hífen.
C. ênclise, visto que depois de preposições o pronome deverá ficar posposto ao verbo.
D. próclise, visto que os advérbios atraem os pronomes.

Alternativa 'D' a correta. Próclise obrigatória pelo advérbio 'nunca' ao substituir a expressão destacada pelo pronome pessoal do caso oblíquo átono 'a'.

					'Ele nunca a atende...'


35. Ano: 2024 / Banca: Comissão Permanente de Concursos da Universidade Estadual da Paraíba - CPCON UEPB / Prova: CPCON UEPB - UEPB - Nutricionista - 2024 

Assinale a alternativa que contém uma frase, na qual ocorre o uso do pronome relativo:

A. “Desde o momento em que ouvi aquelas palavras do médico — tremor essencial —, fiquei ...”
B. “... Fiquei confiante em que poderia lidar com a situação.”
C. “... surgiram até boatos infundados de que seria Parkinson.”
D. “O médico recomendou um medicamento diário e mudança de hábitos, já que a condição, no meu caso, não é genética.”
E. “Hoje, reconheço que estou bem graças à minha obstinação em ficar saudável.”

Gabarito letra 'A'.

Pronomes relativos são aqueles que retomam um termo anterior, chamado de antecedente, e introduzem uma oração subordinada adjetiva. 
Eles têm a função de conectar duas orações, evitando a repetição de palavras e proporcionando coesão ao texto.

			A. “Desde o momento [yellow]em que[reset] ouvi aquelas palavras do médico — tremor essencial —, fiquei ...”		

O item 'A'. Contém o pronome relativo 'que', que retoma o substantivo 'momento'. 
O pronome 'que' introduz uma oração subordinada adjetiva explicativa, explicando o momento específico em que o sujeito ouviu as palavras do médico.


				B. “... Fiquei confiante [yellow]em que[reset] poderia lidar com a situação.”

		O 'que' nesta frase é uma conjunção integrante, que introduz uma oração subordinada substantiva objetiva direta.

				C. “... surgiram até boatos infundados [yellow]de que[reset] seria Parkinson.”

		O 'que' aqui é uma conjunção integrante, introduzindo uma oração subordinada substantiva completiva nominal.
	
				D. “O médico recomendou um medicamento diário e mudança de hábitos, [yellow]já que[reset] a condição, no meu caso, não é genética.”

		Contém a expressão 'já que', que é uma locução conjuntiva causal, e não um pronome relativo.

				 “Hoje, reconheço [yellow]que[reset] estou bem graças à minha obstinação em ficar saudável.”

		contém o 'que' como uma conjunção integrante, introduzindo uma oração subordinada substantiva objetiva direta.

36. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - Prefeitura de Taubaté - Agente Fiscal de Saúde - Área: Nutrição - 2024

Assinale a alternativa em que a alteração da colocação pronominal do trecho do texto preserva a correção gramatical:

A. Já não era-lhe mais permitido vagar livre depois da meia-noite.
B. A cidade devia apresentar-se em casa à uma no máximo…
C. Depois desse dia, quem atreve-se a circular por suas ruas…
D. Tão fácil assim a cidade insone não dorme, não resigna-se…
E. E é assim que podem-se frequentar vastos salões nobres…

Gabarito 'B'

No item 'A' temos uma oração negativa iniciado por advérbio, portanto, é mais do que obrigação a próclise. O correto seria: 'Já não lhe era mais permitido...'
No item 'B' está correta a colocação.
No item 'C' a próclise é obrigatória pelo conectivo 'quem' -> pronome relativo puxa próclise. O correto seria: 'quem se atreve a circular...'
No item 'D' após a vírgula temos uma palavra negativa em que atrai o pronome. O correto seria: '...não se resigna..'
No item 'E' temos um pronome relativo conectivo 'que' tornando a próclise obrigatória. O correto seria: 'E é assim que se podem frequentar...'

37. Ano: 2024 / Banca: Instituto Consulplan / prova: Instituto Consulplan - Câmara de Belo Horizonte - Técnico Legislativo - 2024

Assinale a afirmativa INCORRETA.

A. Em “[...] o mundo não se acabou, [yellow]talvez[reset] tenha ficado um pouco triste [...]” (4º§), o termo grifado exprime circunstância de “possibilidade”.
B. No excerto “[yellow]Se[reset] o fim do mundo não for em fevereiro, todos teremos fim, em qualquer mês...” (11º§), a expressão destacada denota ideia de “causa”.
C. “Enquanto isso, os planetas assumem os lugares que [yellow]lhes[reset] competem, na ordem do universo, [...]” (10º§) O pronome “lhes” refere-se “aos planetas”.
D. “Ninguém fala em cometa, e é pena, porque eu gostaria de tornar a ver um cometa, [yellow]para[reset] verificar se a lembrança que conservo dessa imagem do céu é verdadeira ou inventada pelo sono dos meus olhos naquela noite já muito antiga.” 
(6º§) A preposição “para” estabelece relação de “finalidade”

Gabarito da banca, alternatica 'B'.

O item 'A' realmente exprime uma possibilidade, uma dúvida também.
O item 'B' a expressão 'Se' denota ideia de condição, e não de causa.
O item 'C' quem assume, assume algo. Quem assume? os planetas. Portanto, assumir é verbo transitivo direto e indireto. O pronome 'lhes' é objeto indireto refere-se 'os planetas'.
O item 'D' a preposição 'para' estabelece relação de finalidade.

38. Ano: 2024 / Banca: SELECON Instituto Nacional de Seleções e Concursos - SELECON / Prova: SELECON - Prefeitura de Lucas do Rio Verde - Fonoaudiólogo - 2024 

Em relação à colocação pronominal, ocorre ênclise e próclise, respectivamente, em:

A. o apalpam/ Lembro-me
B. observam-no/ o apalpam
C. Lembro-me / observam-no
D. o chamam pelo nome/ o apalpam

Gabarito letra 'B'. Ênclise é o pronome DEPOIS do verbo e Próclise é o pronome ANTES do verbo.

39. Ano: 2024 / Banca: BRB Assessoria e Concursos / Prova: BRB Assessoria e Concursos - Prefeitura de Senhor do Bonfim - Monitor de Transporte Escolar - 2024 

Marque a alternativa cuja indicação de classe morfológica para a palavra destacada tenha sido feita corretamente segundo as regras da norma culta da Língua Portuguesa.

A. “O levantamento mostrou que 24% desses adultos disseram que começaram [yellow]a[reset] falar com as crianças sobre o tema quando elas tinham até 5 anos.” – [yellow]Artigo definido[reset]
B. “Estudos mostram [yellow]que[reset], quanto mais cedo as crianças aprendem sobre finanças pessoais, mais preparadas elas ficam para lidar bem com o dinheiro.” – [yellow]Pronome Relativo[reset]
C. “Existem contas infantis simples, [yellow]e[reset] essa é uma excelente forma de começar a educar a criança sobre a entrada e a saída de dinheiro...” – [yellow]Conjunção[reset]
D. “Em geral, com as contas de acesso instantâneo, você pode sacar [yellow]ou[reset] depositar dinheiro a qualquer momento...” – [yellow]Preposição[reset]
E. “O essencial é não se endividar, nem usar cartão de crédito [yellow]sem[reset] condições de pagar o boleto no mês seguinte.” – [yellow]Advérbio[reset]

[bg_green]Gabarito letra  'C' - a letra 'e' é uma conjunção coordenativa aditiva sintaticamente. Morfologicamente é um pronome relativo.[reset]

Na alternativa 'A' a letra 'a' é uma preposição que liga o verbo 'começaram' ao verbo 'falar'. '...que começaram [yellow]a[reset]falar com as crianças...'
Na alternativa 'B' é uma conjunção integrante, e não um pronome relativo. Ela introduz sintaticamente uma oração subordinada substantiva objetiva direta.
Na alternativa 'D' é uma conjunção coordenativa alternativa e não uma preposição. Ela liga duas ações alternativas ( sacar ou depositar )
Na alternativa 'E' a palavra 'sem' é preposição de ausência de condições. E não um advérbio.


40. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE /Prova: CESPE/CEBRASPE - MPU - Técnico do Ministério Público - Área Administração Área: Auditoria - Pós-Edital - 2024 - 1º Simulado 

Dada a tecnologia do século XX, seria ineficiente concentrar informação e poder demais num só lugar. 

Ninguém tinha capacidade para processar toda a informação com rapidez suficiente para tomar decisões corretas. 

[yellow]Essa[reset] é em parte a razão de a União Soviética ter tomado decisões muito piores que as dos Estados Unidos, e de a economia soviética ter ficado bem atrás da economia americana.

No primeiro parágrafo, o pronome “Essa” (último período) retoma “Dada a tecnologia do século XX, seria ineficiente concentrar informação e poder demais num só lugar” (terceiro período).

C.Certo
E.Errado

[red]ERRADO.[reset] O pronome “Essa” no último período do primeiro parágrafo refere-se à afirmação “Ninguém tinha capacidade para processar toda a informação com rapidez suficiente para tomar decisões corretas”.


41.Ano: 2024 / Banca: Associação dos Municípios do Extremo Oeste de Santa Catarina - AMEOSC / Prova: AMEOSC - Câmara de Guaraciaba - Controlador Interno - 2024

Em "As pesquisas trazem conclusões claras", o vocábulo destacado pode ser substituído pelo pronome átono : trazem-nas . Todas alternativas abaixo também apresentam o pronome oblíquo átono substituindo o termo destacado corretamente, EXCETO:

A. Os pais deram um beijo [yellow]na filha.[reset] - [blue](deram-lhe)[reset]
B. O soldado defende [yellow]a pátria.[reset] [blue](defende-a)[reset]
C. As nuvens encobrem [yellow]o sol.[reset][blue](encobrem-no)[reset]
D. Os guardas atiraram [yellow]no ladrão.[reset][blue](atiraram-no)[reset]


O gabarito da questão é a alternativa 'D' a INCORRETA. Todas as outras estão certas.

A alternativa 'A' está correta:

	que dá, dá algo: 'um beijo [yellow]na filha[reset] => 'na' -> 'em' preposição + artigo 'a' -> objeto indireto.
		[blue]Portanto, o emprego está certo:[reset] [yellow]'Os pais deram-lhe um beijo'[reset]


A alternativa 'B' está correta:

	O soldado defende [yellow]a pátria.[reset] [blue]( defende-a )[reset]

	quem defende, defende algo: 'a pátria.' <- objeto direto. Portanto o verbo defender é transitivo direto.
			O soldado defende-a  ( o pronome pessoal oblíquo átono 'a' deve concordar com o substantivo em número e gênero )

A alternativa 'C' está correta:

	As nuvens encobrem [yellow]o sol[reset] - (encobrem-no)
		Quem encobre, encobre algo: 'o sol' <- objeto direto / 'encobrir' -> transitivo direto
	verbo 'encobrir' possui terminação '-M' sofre alteração na grafia do pronome: 'o' por 'no'
				As nuvens encobrem-[yellow]no[reset]

A alternativa 'D' está correta:
	
		Os guardas atiraram [yellow]no ladrão.[reset] [blue](atiraram-no)[reset]

			quem atira, atira em algo, em alguém: 'no ladrão' -> preposição 'em' + artigo 'o' = 'no' -> objeto indireto
				Portanto o verbo 'atirar' exige objeto indireto, o é verbo transitivo indireto.
					Para objeto indireto utiliza-se o pronome 'lhe'

					Os guardas atiraram-lhe

42. Ano: 2024 / Banca: Funatec / Prova: Funatec - Prefeitura de Tucuruí - Professor - Área: Matemática - 2024 
Acerca da colocação pronominal, podemos afirmar corretamente, EXCETO:

A. A norma culta não aceita orações iniciadas com pronomes oblíquos átonos.
B. A colocação pronominal é a posição que os pronomes pessoais oblíquos átonos ocupam na frase em relação ao verbo a que se referem.
C. A mesóclise só acontece quando o verbo está flexionado no futuro do pretérito.
D. São pronomes oblíquos átonos: me, te, se, o, os, a, as, lhe, lhes, nos e vos.

A. A norma culta não aceita orações iniciadas com pronomes oblíquos átonos. [green] CORRETO [reset]
B. A colocação pronominal é a posição que os pronomes pessoais oblíquos átonos ocupam na frase em relação ao verbo a que se referem. [green] CORRETO [reset]
C. A mesóclise só acontece quando o verbo está flexionado no futuro do pretérito. [red] INCORRETO [reset] 
		[yellow] Também do futuro do presente [reset]
D. São pronomes oblíquos átonos: me, te, se, o, os, a, as, lhe, lhes, nos e vos.[green] CORRETO [reset]

43. Ano: 2024 / Banca: Fundação de Apoio à Cultura, à Pesquisa e ao Desenvolvimento Institucional, Científico e Tecnológico - CETREDE
Prova: CETREDE - - Prefeitura Caucaia - Enfermeiro - 2024 

Na frase “Informo a Vossa Senhoria que .............. seguem o ofício e o relatório para .............. conhecimento.”

Marque a alternativa que completa corretamente a frase.

A. incluso  – vosso.
B. incluso  – seu.
C. inclusos – vosso.
D. inclusos – seu.
E. inclusos – seus.

Os pronomes possessivos referidos a pronomes de tratamento são sempre os da terceira pessoa. Ex: VOSSA senhoria nomeará SEU substituto." 

	'inclusos' no plural deve concordar com 'ofício' e 'relatório'


44. Ano: 2024 / Banca: Instituto Brasileiro de Apoio e Desenvolvimento Executivo - IBADE / Prova: IBADE - CRMV ES - Agente Administrativo - 2024

Marque a alternativa que completa corretamente as lacunas da frase “Senhor Ministro, pedimos-____ a _____ interferência na condução dos projetos de sustentabilidade.
Se ____________, a população ficará muito grata.”

A. lhe, vossa, intervieres;
B. lhe, tua, intervieres;
C. lhe, sua, intervier;
D. vos, vossa, intervieres;
E. lhe, sua, intervirdes;

Alternativa 'C'

Os pronomes possessivos referidos a pronomes de tratamento são sempre os da terceira pessoa. Ex: VOSSA senhoria nomeará SEU substituto." 

“Senhor Ministro, pedimos-lhe a sua interferência na condução dos projetos de sustentabilidade. Se intervier, a população ficará muito grata.”

			futuro do subjuntivo -> se intervier ( ele ) - Sempre na terceira pessoa do singular
	[blue] VOSSA só se usa no vocativo. Vossa Majestade (de forma direta), Sua Majestade (de forma indireta)[reset]
[yellow]"Vossa" é um pronome de tratamento usado para se referir diretamente a uma pessoa de alta posição, como "Vossa Excelência" ou "Vossa Senhoria"[reset]


45. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura de Tapiratiba - Motorista de Transporte Escolar - 2024

Considere o excerto a seguir para responder às questões 4 e 5:

Outro diferencial do túmulo é a forma com que foi construído, segundo o arqueólogo. “Há uma pequena saliência em cada extremidade. 
Isso é algo único entre túmulos em Falbygden”, ele diz. 
Em Falbygden, uma área geográfica de Falköping, há mais de 250 túmulos de passagem que são construídos com blocos de pedra e datam de cerca de 3,3 mil a.C.

As palavras “outro”, “cada” e “algo”, que ocorrem no contexto apresentado, são classificadas gramaticalmente e respectivamente como:

[green]A.pronome indefinido, pronome indefinido, pronome indefinido.[reset]

[red]B.pronome indefinido, adjetivo, pronome indefinido.[reset]
[red]C.pronome indefinido, pronome indefinido, advérbio.[reset]
[red]D.advérbio, advérbio, advérbio.[reset]
[red]E.advérbio, adjetivo, advérbio.[reset]

46.Ano: 2024 / Banca: Universidade de Blumenau - FURB / Prova: FURB - Prefeitura de Florianópolis - Enfermeiro - 2024

Os excertos a seguir foram elaborados a partir dos Textos 01 e 02, assinale a alternativa que apresenta a correta colocação pronominal:

A. Não pode-se aceitar que as pesquisas sigam os padrões éticos distorcidos que bem entenderem.
B. Alguém explicou-lhes a razão para não participar desses experimentos.
C. Moreau quis colaborar com os grupos minoritários os defendendo na ciência.
D. Isso nos mostra a importância de discutirmos a ética em pesquisa durante a formação inicial.
E. Moreau e seus colegas fizeram sua parte. Os alertaram sobre mais de uma centena de artigos.

Gabarito letra 'D'.

O item 'A' a oração é coordenativa negativa, portanto é próclise obrigatória. O correto seria: 'Não se pode aceitar que as pesquisas...'
O item 'B'. Quem explica, explica algo: 'para' não participar desses experimentos...' Portanto, verbo transitivo indireto. O 'lhes' é para objetos indiretos, com preposição 'para.
		Porém, na regra de colocação pronominal determina que, após um verbo no início da frase, deve-se usar a ênclise. ( pronome ANTES do verbo )
					[blue]O correto seria:[reset] Alguém [yellow]lhe[reset] explicou a razão para...'

O item 'C' A forma correta seria: “Moreau quis colaborar com os grupos minoritários [yellow]defendendo-os[reset] na ciência.”
[bg_red]Isso ocorre porque, em locuções verbais (como “quis colaborar”), o pronome oblíquo átono deve ser colocado após o verbo principal no infinitivo ou no gerúndio, formando uma ênclise.[reset]

No item 'D'. A regra de colocação pronominal determina que, após um ponto final, deve-se usar a ênclise. 
	Portanto, a forma correta seria 'Moreau e seus colegas fizeram sua parte. Alertaram-nos sobre mais de uma centena de artigos.'


47.Ano: 2024 / Banca: Universidade de Blumenau - FURB / Prova: FURB - Floram - Oceanógrafo - 2024

Assinale a alternativa que apresenta a correta colocação pronominal, segundo a norma padrão brasileira:

A. A pesquisadora não informou-lhe que o biodiesel é um combustível renovável produzido a partir de fontes como óleos vegetais e gorduras animais.
B. Alguém disse-nos que países têm incentivado a mistura de biodiesel ao diesel convencional como uma estratégia para promover a sustentabilidade energética.
C. Todos os pesquisadores quiseram participar, lhes informando que a utilização de biodiesel pode contribuir para a redução das emissões de gases de efeito estufa quando comparado aos combustíveis fósseis.
D. A informação que passei-lhe foi que a produção de biodiesel envolve processos como a transesterificação, que transforma óleos vegetais em um combustível adequado para motores diesel.
E. Não nos haviam informado que o biodiesel pode ser utilizado inclusive na geração de energia, devido às suas propriedades ambientalmente amigáveis e renováveis.


Gabarito correto letra 'E' a única correta. as outras estão erradas.

O item 'A'. A oração é negativa, portanto, próclise obrigatória. O correto seria: 'A pesquisadora não lhe informou que o biodiesel...'
No item 'B' "Alguém nos disse" é a forma correta porque o pronome "nos" deve vir antes do verbo "disse" devido à ausência de uma palavra que justifique a ênclise.

Situações que Justificam Ênclise:

Início de Orações:

Quando o verbo inicia a frase, a ênclise é obrigatória.

Exemplo: Diga-me o que aconteceu.

Após Vírgulas:

Quando o verbo vem após uma vírgula que separa orações ou incisos.

Exemplo: Estou feliz, conte-me mais.

Formas Verbais Específicas:

Infinitivo Impessoal: Quando o verbo está no infinitivo impessoal.

Exemplo: Era necessário revisar tudo antes de entregá-lo.

Gerúndio: Quando o verbo está no gerúndio.

Exemplo: Estava explicando-lhe a situação.

Futuro do Presente e Futuro do Pretérito: A mesóclise é comum nesses casos, mas a ênclise também pode ser usada em contextos específicos.

Exemplo (Ênclise): Dir-se-á a verdade.

Exemplo (Mesóclise): Dir-se-lhe-á a verdade.

Proibição de Próclise:

Após Palavras Proibidas: Quando há palavras negativas, conjunções subordinativas, pronomes relativos, advérbios, etc., que não atraem a próclise.

Exemplo: Isso ajuda-nos a entender.

Exemplos com Ênclise:
Levante-se agora.

Encontraram-na na biblioteca.

Não sei se ele verá-me.

No item 'C' é um exemplo que justifica uma ênclise ( pronome após o verbo ) após a vírgula em uma frase.
Após a vírgula, que separa orações, a ênclise é a colocação correta, portanto, deveria ser 'informando-lhes'. 

O item 'D' A presença do pronome relativo 'que' exige próclise, portanto, o correto seria 'que lhe passei'.


48. Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN / Prova: IDECAN - Polícia Penal do Ceará - Agente Penitenciário Pós-Edital - 2024 - 2º Simulado

A fim de evitar uma repetição viciosa no texto, pode-se, por exemplo, substituir elementos de um texto por um pronome. Identifique a alternativa em que ocorreu a correta substituição da expressão em destaque em “que atormentam a existência” (l. 18) por um pronome.

A. que atormentam-na.
B. que lhe atormentam.
C. que atormentam ela.
D. que a atormentam.
E. que atormentam-a.

Gabarito letra 'D'. 'que a atormentam'

Em “que atormentam a existência”, a expressão destacada exerce a função sintática de objeto direto do verbo “atormentam”, podendo escrever no lugar desse objeto direto o pronome “a”. 
Como o vocábulo “que” é um pronome relativo, ele atua como fator de atração, exigindo o uso do pronome oblíquo átono “a” antes do verbo. 
Portanto, a forma correta será: que a atormentam. Lembre-se de que o vocábulo “que” sempre atua como fator de atração.

49. Ano: 2024 / Banca: FACET Concursos - FACET / Prova: FACET - Prefeitura de Queimadas - Técnico em Farmácia - 2024 
Assinale a opção que contém o uso inadequado do pronome de acordo com a norma culta:

A. Ninguém exigiu-me segredo.
B. Dar-te-ei todo o meu amor!
C. Por gentileza, entregue o computador para ela.
D. Hoje eu te chamei umas 30 vezes.
E. Não me ligue mais!

Gabarito letra 'A'. A única que está errada!

"Ninguém" é uma palavra negativa, e palavras negativas atraem a próclise. Portanto é, 'Ninguém me exigiu segredo.'

No item 'B'. 'Dar-te-ei todo o meu amor!' está correto segundo a norma culta. 
A mesóclise é utilizada em verbos no futuro do presente ou do pretérito, quando não há palavra atrativa antes do verbo.

O item 'C' colocação 'para ela' correta.
O item 'D' colocação correta. Nada demais também.
O item 'E' correto. Próclise para frase negativa.

50. Ano: 2024 / Banca: Comissão Permanente de Concursos da Universidade Estadual da Paraíba - CPCON UEPB / Prova: CPCON UEPB - Prefeitura de Matinhas - Motorista D - 2024 

No fragmento: 
“Sabe-se apenas que se comunicaram rapidamente, pois não havia tempo. Sabe-se também que sem falar eles se pediam. 
Pediam-se com urgência, com encabulamento, surpreendidos”. 
Observe o emprego dos pronomes oblíquos átonos no fragmento e assinale o emprego CORRETO, de acordo com as normas gramaticais referentes ao uso da colocação pronominal:

A. Por favor, me procure mais.
B. Cansei-me e vou seguir sem você.
C. Se vestiu de preto e saiu para matar.
D. Me alimentei do fruto da vida.
E. Se sinta uma grande mulher.

Alternativa 'B' é o gabarito. A única correta. Frase com inicio de um verbo é ênclise obrigatória.

Alternativa 'A', frase após uma pausa (vírgula), o pronome oblíquo átono deve ser colocado após o verbo, formando uma ênclise.
O correto seria:

				[yellow]A. Por favor, procure me mais.[reset]

Alternativa 'B', a frase está correta.

				B. [yellow]Cansei-me[reset] e vou seguir sem você.

O pronome oblíquo átono 'me' está corretamente posicionado após o verbo 'cansei', 
formando uma ênclise, que é a colocação pronominal adequada no início de uma oração ou após uma pausa.

 				C. [yellow]Se[reset] vestiu de preto e saiu para matar.
Na alternativa 'C', o pronome obliquo 'se' é iniciado na frase, incorreto. O correto é: Vestiu-se de preto e saiu para matar.' ênclise obrigatória.
	Frase iniciada com verbo flexionado é ênclise obrigatória ou após vírgula (pausa)

				[yellow]Vestiu-se[reset] de preto e saiu para matar.

Alternativa 'D' / O pronome obliquo 'me' é iniciado na frase, INCORRETO. [red]Me alimentei do fruto da vida.[reset]
				O correto é [yellow]'Alimentei-me[reset] do fruto da vida.


Assim como na alternativa 'E'. O pronome obliquo 'se' é iniciado na frase, INCORRETO. 'Se sinta uma grande mulher'.
				O correto seria: [yellow]Sinta-se[reset] uma grande mulher.
					ênclise obrigatória.


51. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TRF 1 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 2º Simulado
Em relação ao uso da colocação pronominal, assinale a alternativa adequada.

A. Te ajudou nas tarefas de casa.
B. Aquele obrigou-me a trabalhar.
C. Farei-te uma surpresa.
D. Tratar-me-ei como um objeto.
E. Depois que ajudou-nos, foi embora.

Gabarito letra 'D'. A única correta.

O item 'a' a frase não pode iniciar com pronome oblíquo átono. O correto seria: Ajudou-te nas tarefas de casa

No item 'B' o pronome demonstrativo 'aquele' puxa o pronome tornando-o próclise obrigatória. O correto seria: Aquele me obrigou a trabalhar.

No item 'C' o verbo no futuro do pretérito do subjuntivo jamais aceitará uso do ênclise. O correto é mesóclise: 'far-te-ei uma surpresa.'

No item 'D' Mesóclise utilizada corretamente. Verbo no futuro do pretérito do subjuntivo.

No item 'E'. O pronome relativo 'que' sempre será fator de atração do pronome obliquo, tornando próclise obrigatória ( pronome antes do verbo )
		O correto seria:

					Depois que nos ajudou, foi embora.'''


    def exercicios_verbos(self):
       return '''Exercicios de verbos:

1.Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC / Prova: FUNDATEC - Prefeitura de Bagé - Terapeuta Ocupacional - 2024 

Assinale a alternativa que indica a correta transposição do trecho a seguir da voz passiva sintética para a analítica.


[yellow]“Abrem-se condições para uma disputa mental”.[reset]

A. Condições é aberta para uma disputa mental.
B. Condições são abertas para uma disputa mental.
C. Condições foi aberta para uma disputa mental.
D. Condições foram abertas para uma disputa mental.
E. Condições serão abertas para uma disputa mental.

A questão aborda a transposição de uma frase da voz passiva sintética para a voz passiva analítica. 
A voz passiva sintética é caracterizada pelo uso do pronome 'se' junto ao verbo, 
enquanto a voz passiva analítica é formada pelo verbo ser seguido do particípio do verbo principal.

Alternativa 'B'. 
'Condições são abertas para uma disputa mental' está correto. 
A forma verbal 'são abertas' está no plural, concordando corretamente com o sujeito 'Condições'. Esta é a forma correta da voz passiva analítica para a frase dada,


2.Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP / Prova: IDCAP - Prefeitura de Vila Rica - Técnico em Radiologia - 2024

As regras também 'impactam' aqueles que já 'vivem' legalmente no país e 'pretendem', por exemplo, trazer cônjuges ou parentes para morar com eles.

Conjugando os verbos destacados no pretérito imperfeito do indicativo, tem-se:

A. As regras também impactaram aqueles que já viveram legalmente no país e pretenderam, por exemplo, trazer cônjuges ou parentes para morar com eles.
B. As regras também impactariam aqueles que já viveriam legalmente no país e pretenderiam, por exemplo, trazer cônjuges ou parentes para morar com eles.
C. As regras também impactassem aqueles que já vivessem legalmente no país e pretendessem, por exemplo, trazer cônjuges ou parentes para morar com eles.
D. As regras também impactavam aqueles que já viviam legalmente no país e pretendiam, por exemplo, trazer cônjuges ou parentes para morar com eles.


O pretérito imperfeito do indicativo é um tempo verbal que expressa um fato ocorrido no passado, 
mas que não foi completamente terminado ou que ocorria com certa frequência. 
As terminações para a conjugação no pretérito imperfeito do indicativo são: -ava, -avas, -ava, -ávamos, -avam para os verbos da 1ª conjugação (terminados em -ar) 
e -ia, -ias, -ia, -íamos, -iam para os verbos da 2ª e 3ª conjugações (terminados em -er e -ir).

Gabarito letra 'D'

3.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TRF 1 - Analista Judiciário - Área Judiciária - Especialidade: Oficial de Justiça Avaliador Federal Pós-Edital - 2024 - 3º Simulado

Considerando o uso dos tempos e modos verbais no trecho :
"Quando a academia sueca [yellow]anuncia[reset] os vencedores do Nobel de Física ou Química, telejornais do mundo inteiro [yellow]dedicam[reset] preciosos minutos 
a temas herméticos como entrelaçamento quântico ou química bio-ortogonal", é correto afirmar que:

A. o presente do indicativo é utilizado para indicar ações habituais e recorrentes.
B. o futuro do presente é utilizado para expressar ações que acontecerão posteriormente.
C. o pretérito perfeito é utilizado para narrar ações concluídas no passado.
D. o presente do subjuntivo é utilizado para expressar uma hipótese ou desejo.
E. o pretérito imperfeito é utilizado para descrever ações contínuas no passado.


Ao presente do indicativo utilizado para indicar ações habituais e recorrentes.


4. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura de Tapiratiba - Monitor - 2024
Analise as sentenças a seguir e assinale aquela em que a forma verbal empregada está conjugada na 3ª pessoa do singular.

A. Voltamos de viagem no domingo.
B. Todos os alunos fizeram o trabalho de artes com excelência.
C. Fui ao mercado hoje de manhã.
D. Felizmente, Marco não fez nada de ruim para Ana.
E. Sabes toda a fofoca!

A (Nós)  ->  Voltamos de viagem no domingo.
B (Eles) ->  Todos os alunos fizeram o trabalho de artes com excelência.
C (Eu)   ->  Fui ao mercado hoje de manhã.
D (Ele)  ->  Terceira do singular ( Felizmente, Marco não fez nada de ruim para Ana.)
E (Tu)   ->  Sabes toda a fofoca!

Gabarito letra 'D'.


5. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - TJ SP - Escrevente Técnico Judiciário Pós-Edital - 2024 - 7º Simulado

Em – 'A neutralidade da internet é outro pilar de sustentação da igualdade de oportunidades, 
cara a todo e qualquer coração que [yellow]bata[reset] pela causa da liberdade (parágrafo 2) –, a forma verbal destacada expressa:

A. uma ação habitual passada.
B. uma ação futura.
C. uma ação hipotética no presente.
D. um desejo passado.
E. um fato atemporal.

A forma verbal “bata” no presente do subjuntivo expressa uma ação hipotética no presente. 
Essa forma é frequentemente utilizada para indicar situações que são hipotéticas no tempo presente, mas que não são necessariamente reais ou confirmadas.

	Gabarito letra 'C'

6. Ano: 2024 / Banca: Instituto Brasileiro de Apoio e Desenvolvimento Executivo - IBADE / Prova: IBADE - SMTT MA - Agente de Trânsito Pós-Edital - 2024 - 1º Simulado

No trecho do último parágrafo “A confirmação do bronze veio depois do solo de Simone Biles”, a forma verbal destacada circunscreve a informação apresentada no tempo

A.passado, reiterando a confirmação da medalha de bronze.

A forma verbal “veio” está conjugada no pretérito perfeito do indicativo e indica uma ação concluída no passado.

	
Nesse sentido, a letra A está correta, por afirmar que o verbo está no passado e reforça os fatos ocorridos.

7. Ano: 2024 / Banca: Escola de Sargentos das Armas - ESA / Prova: ESA - ESA - Sargento - Área: Geral Pós-Edital - 2024 - 1º Simulado

Analise as formas verbais presentes nas frases abaixo e escolha a opção que corretamente identifica o tempo e modo verbais, levando em conta o contexto em que são empregados.

A. "A inteligência artificial é uma tecnologia revolucionária que [yellow]tem impactado[reset] significativamente diversas áreas da sociedade." – O verbo "tem impactado" está no pretérito mais-que-perfeito do indicativo, indicando uma ação que foi completada no passado, antes de outra ação também passada.


O verbo composto 'tem impactado' está no presente do indicativo + participio. Indicando uma ação que começou no passado e continua até o presente				
O pretérito-mais-que-perfeito do indicativo indica ação que foi completada no passado, antes de outra ação no passado.  que 'tivera impactado'
		
B. "Por meio de assistentes virtuais e chatbots, pessoas com diferentes níveis de habilidades tecnológicas podem acessar informações." – O verbo "podem acessar" está no futuro do presente do indicativo, expressando uma possibilidade ou capacidade futura.

Futuro do indicativo -> eu posso / tu pudes / ele pode / nos podemos / vos podeis / eles podem -expressa possibilidade/capacidade no momento atual e não futuro.			


C. "A aplicação na medicina proporciona diagnósticos mais precisos." – O verbo "proporciona" está no pretérito imperfeito do indicativo, sugerindo uma ação habitual que ocorria no passado.

eu proporcionava / tu proporcionavas / ele proporcionava -> pretério imperfeito do indicativo, 

porém o verbo 'proporciona' está no presente do indicativo -> eu proporciono / tu proporcionas / ele proporciona -> indicando uma ação que ocorre no momento atual de forma habitual.		

D. "A IA favorece a telemedicina e a assistência médica remota." – O verbo "favorece" está no presente do subjuntivo, expressando um desejo ou uma possibilidade em relação ao futuro.

		que eu favoreça / que tu favoreças / que ele favoreça -> presente do subjuntivo -> algo hipotético no presente momento
		eu favoreço / tu favoreces / ele favorece -> presente do indicativo -. ação que acontence no presente momento habitualmente
		
E. "Os algoritmos permitem que as pessoas descubram novos conteúdos baseados nos seus interesses." – O verbo "permitem" está no presente do indicativo, expressando uma ação que acontece no momento atual, de forma habitual, enquanto "descubram" está no presente do subjuntivo, indicando uma ação potencial ou desejada que depende de outra condição.

		eu permito / tu permites / ele permite / nós permitimos / vós permitireis / eles permitem - presente do indicativo -> ação habitual no presente momento

		que eu descobra / que tu descubras / que ele descubra / que nós descubremos / que vós descubireis / que eles descubram - presente do subjuntivo - algo hipotético

Gabarito letra 'E'

8. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - PM SP - Soldado PM de 2ª Classe Pós-Edital - 2024 - 1º Simulado

Observe o período a seguir:

“Se estudasse com afinco, hoje já [yellow]estaria[reset] aprovado.”

A forma verbal “estaria”

A. está conjugada no futuro do presente.  
B. transporta a uma época passada e descreve o que seria ação futura.
C. indica um passado contínuo.
D. traduz ações posteriores ao tempo da oração anterior.
E. exprime dúvida sobre fatos passados.


A. está conjugada no futuro do presente.  <- eu estarei / tu estarás / ele [yellow]estará[reset] <- [red]alternativa INCORRETA.[reset]
B. transporta a uma época passada e descreve o que seria ação futura. [bg_green]CORRETO[reset]

[blue]A forma verbal 'estaria' transporta a uma época passada e descreve o que seria uma ação futura em relação a esse passado. [reset]
[blue]Esta é a definição correta do futuro do pretérito, que é usado para expressar uma ação que seria realizada no futuro em relação a um momento passado.[reset]

C. indica um passado contínuo. <- [blue]O passado contínuo seria indicado pelo pretérito imperfeito do indicativo, como 'estava'.[reset]
D. traduz ações posteriores ao tempo da oração anterior.
E. exprime dúvida sobre fatos passados.  <- A expressão de dúvida sobre fatos passados seria feita com o uso do pretérito mais-que-perfeito.

9. Ano: 2024 / Banca: SELECON Instituto Nacional de Seleções e Concursos - SELECON /Prova: SELECON - Prefeitura de São Gonçalo - Auxiliar de Creche - 2024 

Em “Se [yellow]adiássemos[reset] a busca do conhecimento e a procura do belo até haver alguma paz, nem sequer as pinturas rupestres existiriam” (2º parágrafo), 
o verbo destacado está flexionado no:

A. pretérito perfeito do indicativo
B. futuro do pretérito do indicativo
C. pretérito imperfeito do indicativo
D. pretérito imperfeito do subjuntivo

Gabarito 'D'. A correta. Vamos as outras alternativas:

O item 'A' O pretérito perfeito do indicativo é utilizado para expressar uma ação concluída no passado, uma certeza concluida no passado.

		eu adiei <- aspecto concluido no passado

No item 'B' O futuro do pretérito do indicativo expressa uma ação que poderia ocorrer em um momento posterior ao passado.

		eu adiaria <- ação que poderia ocorrer em um momento posterior ao passado.

No item 'C' O pretérito imperfeito do indicativo é usado para descrever ações habituais ou não concluídas no passado.

		'eu adiava' <- ações habituais no passado. Ações não concluidas no passado.

O item D corretamente identifica o verbo 'adiássemos' como estando no pretérito imperfeito do subjuntivo, que está de acordo com o gabarito da banca. 
Este tempo verbal é apropriado para expressar situações hipotéticas, desejos ou condições que não necessariamente ocorreram.

10. Ano: 2024 / Banca: CRS - Polícia Militar de Minas Gerais - CRS PMMG / Prova: CRS - PMMG - PM MG - Soldado Pós-Edital - 2024 - 5º Simulado

A forma verbal “vivia”, em “Carybé vivia em Buenos Aires” (l. 14), indica:

A. uma situação hipotética.
B. uma ação concluída no passado.
C. uma ação habitual no passado.
D. uma ação anterior a outra no passado.

	'vivia' está no pretérito imperfeito do indicativo, ou seja, uma ação habitual ou repetitiva no passado. com aspecto não concluido. Item 'C'

		eu vivia / tu vivias / ele vivia

O verbo 'vivia' não indica situação hipotética como está no item 'A'

No item 'B' O verbo 'vivia' não indica ação no passado concluido. Uma ação concluida no passado seria o pretérito perfeito do indicativo. Eu vivi / tu viveu / ele vivi
	
						"Carybé viveu em Buenos Aires"

No item 'D' 'vivia' não é ação anterior a outra no passado. O pretérito mais-que-perfeito do indicativo 'eu vivera / tu viveras / ele vivera'

						"Carybé vivera em Buenos Aires"

11.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TRT 7 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 3º Simulado

Transpondo-se a frase [yellow]Ele também reforçou a necessidade[reset] (3º parágrafo) para a voz passiva analítica, a forma verbal resultante será:

A. foi reforçada.
B. era reforçada.
C. é reforçada.
D. seria reforçada.
E. será reforçada.

		O correto seria: A necessidade [yellow]foi reforçada[reset] por ele.
Na voz passiva, precisamos acrescentar o verbo “ser” no mesmo tempo e modo do verbo na voz ativa. E depois devemos escrever o verbo principal no particípio.

12. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - TJ SP - Escrevente Técnico Judiciário Pós-Edital - 2024 - 1º Simulado

No trecho “[yellow]era[reset] preciso passar por um corredor imenso, onde [yellow]ficavam[reset] troços e destroços de cenários semidestruídos daqueles programas populares” (2º parágrafo), as palavras em destaque indicam ações que

A. iniciaram anteriormente e ainda estão ocorrendo no agora.
B. ocorreram mais de uma vez no passado.
C. já estão acontecendo e vão se repetir.
D. aconteceram anteriormente a outra situação.
E. ainda vão acontecer, em um futuro próximo.

Os verbos 'era' e 'ficavam' estão conjugados no pretérito imperfeito do indicativo o que indica ação que é habitual, repetida no passado.

						Terminações: 1º(-AVA)/2º(IA)/2º(IA)
	Pretérito Imperfeito do indicativo verbo SER   -> [yellow]Eu era[reset] /  Tu eras / Ele era / Nós éramos / Vós éreis / Eles eram
	Pretérito Imperfeito do indicativo verbo FICAR -> Eu ficava / Tu ficavas /  Ele ficava / Nós ficávamos / Vós ficareis / [yellow]Eles ficavam[reset]


13. Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - DPE PR - Técnico da Defensoria Pública - Área: Técnico Administrativo - 2024

“Se [yellow]abríssemos[reset], ele – [yellow]fosse[reset] quem [yellow]fosse[reset] – nos [yellow]lançaria[reset] um olhar, [yellow]diria[reset] alguma coisa – e então o nosso mundo [yellow]seria[reset] invadido.” (3º§) 
Tendo em vista que os tempos verbais assumem diversos valores semânticos, na passagem anterior, as expressões destacadas exprimem ações

A.incertas e improváveis.
B.totalmente concluídas.
C.habituais, rotineiras e durativas.
D.momentâneas e determinadas no tempo.

					Terminações: 1º -ASSE / 2º -ESSE / 3º -ISSE

A frase inicia-se com hipóteses ou incertezas 'se abríssemos..' <- verbo no pretérito imperfeito do subjuntivo -> se eu abrisse / se tu abrisses / se ele abrisse / 
														  [yellow]se nós abrissemos[reset] / se vós abrisseis / se eles abrissem
'fosse' quem 'fosse' Verbo 'SER' no pretérito imperfeito do subjuntivo -> se eu fosse <- 1º pessoa do singular


'lançaria' / 'diria'/ 'seria' estão no futuro do pretérito do indicativo que exprime um futuro que poderia ter acontecido sob certas condições do passado. Terminação: -RIA

			A questão está bem correlacionada. Mas no modo geral é uma frase subjuntiva, hipotética, incerta.

14. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP / Prova: IDCAP - Prefeitura de Reduto - Secretário Escolar - 2024

O professor Ezzati, que 'analisa' dados globais há anos, 'diz' estar surpreso com a velocidade com que o quadro mudou.

Conjugando os verbos destacados no pretérito imperfeito do indicativo e no pretérito mais que perfeito do indicativo, respectivamente, tem-se:

A. O professor Ezzati, que analisou dados globais há anos, dizendo estar surpreso com a velocidade com que o quadro mudou.
B. O professor Ezzati, que analisara dados globais há anos, dizia estar surpreso com a velocidade com que o quadro mudou.
C. O professor Ezzati, que analisaria dados globais há anos, disse estar surpreso com a velocidade com que o quadro mudou.
D. O professor Ezzati, que analisava dados globais há anos, dissera estar surpreso com a velocidade com que o quadro mudou.

Não é a alternativa 'A'. 'Analisou' está no pretérito perfeito do indicativo -> eu analisei / tu analisaste / [yellow]ele analisou[reset] / 'dizendo' -> forma nominal gerúndio
Não é a alternativa 'B'. 'analisara' está no pretérito mais-que-perfeito do indicativo -> eu analisara / 'dizia' -> pretérito imperfeito do indicativo -> eu dizia
Não é a alternativa 'C'. 'analisaria' está no futuro do pretérito do indicativo -> eu analisaria / 'disse' -> pretérito imperfeito do subjuntivo
Correta a alternativa 'D' conforme pediu o enunciado:
	terminação -AVA para o pretérito imperfeito do indicativo 'analisava' / 'dissera' -terminação -ERA para pretérito mais-que-perfeito do indicativo


15. Ano: 2024 / Banca: Desenvolvimento Institucional e de Carreiras - LTDA - EMBRASIL / Prova: EMBRASIL - Câmara de Itapetininga - Controlador Interno - 2024

Identifique o tempo verbal e a pessoa gramatical na expressão "eu mudei".

A. Presente do indicativo, primeira pessoa do singular.
B. Pretérito perfeito do indicativo, primeira pessoa do singular.
C. Futuro do subjuntivo, segunda pessoa do singular.
D. Pretérito imperfeito do indicativo, terceira pessoa do singular.


Terminação '-EI' é pretérito perfeito do indicativo -> Eu mudei - Alternativa 'B'

	No item 'A' seria: Presente do indicativo 1º pessoa : Eu mudo   ( terminação 'O')
	No item 'C' para o futuro do subjuntivo seria: quando eu mudar / se eu mudar  ( terminação -R' )
	No item 'D' para o pretérito imperfeito do indicativo seria: eu mudava ( terminação -AVA )

16. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - CFC - Contador Exame CFC - 2024.1 - Pós-Edital - 2024 - 3º Simulado

Releia o trecho:


A Inteligência Artificial na contabilidade [yellow]tem se tornado[reset] mais pertinente do que nunca.


Assinale a alternativa que indica corretamente o tempo da forma verbal destacada.

A. Presente do indicativo.
B. Pretérito perfeito do indicativo.
C. Pretérito imperfeito do indicativo.
D. Pretérito mais-que-perfeito do indicativo.

A forma verbal “tem se tornado” está conjugada no pretérito perfeito composto do indicativo. 
Sempre que tivermos o verbo 'ter'ou 'haver' seguido de um verbo no particípio, teremos um tempo composto. 
Nesse caso, quanto houver o verbo 'ter' ou 'haver' no presente do indicativo seguido de um verbo no particípio, teremos o pretérito perfeito composto do indicativo.


17.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TRT 7 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 1º Simulado

Transpondo-se a frase “[yellow]Fui levado[reset] para um lugar conhecido como Usina Pequena” (6º parágrafo) para a voz ativa, a forma verbal resultante será:

A. Tinham me levado
B. Levavam-me
C. Haviam me levado
D. Levaram-me
E. Levou-me

A forma verbal “Fui levado” está na voz passiva analítica e indica uma ideia de passividade.
Para transpor para a voz ativa é necessário conjugar o verbo 'levar' no mesmo tempo do verbo 'SER' da voz passiva.
O verbo 'SER' está conjugado no pretérito perfeito do indicativo 'EU FUI'.
O sujeito na frase é indeterminado, não sabe quem levou, ou se levaram. 
Portanto devemos usar o verbo na 3º pessoa do plural do pretérito perfeito do indicativo: levaram-me

	eu levei / tu levaste / ele levou / nós levamos / vós levastes / [yellow]eles levaram[reset]


18. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - PM SP - Soldado PM de 2ª Classe Pós-Edital - 2024 - 1º Simulado
Assinale a opção que apresenta a frase cuja forma verbal está correta.

A. Estados Unidos detem grande poder
B. Requiseram o emprego de regras mais rígidas.
C. Advinhamos os números da loteria.
D. O retirante proviu do interior do Nordeste.
E. Proveem a casa do necessário.

No item 'A' a palavra 'detem' deve ser acentuada. 'Os estados unidos detém'.

No item 'B' deve estar no pretérito perfeito do indicativo -> eu requeri / tu requereste / ele requeriu / nós requerimos / vós requerestes / [yellow]eles requereram[reset]

No item 'C' adivinhamos deve ter a letra 'i' e não a letra 'd' muda.

No item 'D' temo o presente do indicativo 'Eu provejo / tu provês / ele provê / nós provemos / vós provedes / [yellow]eles proveêm[reset]

19. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - ALE TO - Analista Legislativo - Área Revisão - 2024

O verbo fazer é muitas vezes empregado como substituto de toda uma oração anterior, como ocorre na seguinte opção:


A. Enquanto uns trabalham, outros evitam [yellow]fazer[reset] o mesmo.
B. As abelhas trabalham muito, mas também [yellow]fazem[reset] cera.
C. Alguns trabalham enquanto outros [yellow]fazem[reset] greve.
D. Enquanto alguns trabalham outros [yellow]fazem[reset] a sesta.
E. Alguns fazem, outros prometem [yellow]fazer.[reset]

NO item 'A' O verbo 'fazer' é empregado para evitar a repetição da ação expressa anteriormente ('trabalham'), 
substituindo efetivamente toda a oração 'uns trabalham' pela palavra 'fazer'.

No item 'B' o verbo 'fazer' é utilizado com um sentido específico ('fazem cera'), 
não servindo como substituto de uma oração anterior, mas indicando uma ação própria das abelhas.

No item 'C' emprega o verbo 'fazer' para indicar uma ação específica ('fazem greve'), que não retoma diretamente uma ação expressa anteriormente, mas introduz uma nova informação.

No item 'D' 'fazer' é usado para indicar uma nova ação ('fazem a sesta'), sem a função de retomar uma oração anterior por meio de elipse.

no item 'E' O item E utiliza o verbo 'fazer' em duas instâncias, ambas indicando ações gerais ('Alguns fazem, outros prometem fazer'), sem, contudo, substituir uma oração anterior.

20. Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Catuípe - Odontólogo - 2024 

Assinalar a alternativa que preenche CORRETAMENTE as lacunas abaixo, respeitando-se a correta flexão verbal:

_____ anos que a loja de doces fechou as portas. Lá ______ muitas opções de guloseimas para comprar.

A. Faz — havia.
B. Fazem — havia.
C. Faz — haviam.
D. Fazem — haviam.

A frase 'Faz anos que a loja de doces fechou as portas' está correta, pois o verbo 'fazer' está sendo usado para indicar tempo decorrido, portanto, é impessoal e fica no singular. 
A frase 'Lá havia muitas opções de guloseimas para comprar' também está correta, pois o verbo 'haver' está sendo usado com o sentido de existir, portanto, é impessoal e fica no singular.
Gabarito letra 'A'.

21. Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - Prefeitura de Santa Maria de Jetibá - Cuidador Social - 2024 

Em todos os fragmentos a seguir, transcritos do texto, as formas verbais estão flexionadas no mesmo tempo, EXCETO:

A. “A corte, claro, tinha sua justificativa.” (3º§)
B. “Durante o namoro, ele mandava poemas, [...]” (1º§)
C. “Na geração seguinte, o homem pedia a mulher em namoro, [...]” (1º§)
D. “[...] todo o ritual de aproximação que chegou a exageros de regras e restrições, [...]” (2º§)

[blue]'tinha'   -> eu tinha   -> 1º pessoa do singular do pretérito imperfeito do indicativo[reset]
[blue]'mandava' -> eu mandava -> 1º pessoa do singular do pretérito imperfeito do indicativo[reset]
[blue]'pedia'   -> eu pedia   -> 1º pessoa do singular do pretérito imperfeito do indicativo[reset]
[red]'chegou'  -> ele chegou -> 3º pessoa do singular do pretérito perfeito do indicativo[reset]


22. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ SC - Técnico Judiciário Auxiliar Pós-Edital - 2024 - 1º Simulado 
Leia as palavras de Leonardo da Vinci

“As mais lindas palavras de amor são ditas no silêncio de um olhar”.

A forma verbal “são” significa

A. uma situação hipotética.
B. uma ação concluída.
C. uma ação que ocorrerá.
D. um tempo atual.
E. uma ação anterior a outra.

A forma verbal “são” está conjugada no presente do indicativo e indica um tempo atual.

Presente do indicativo do verbo SER:

Eu   sou
Tu   és
Ele  é 
Nós  somos
Vós  sois
[yellow]Eles são[reset]

23. Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC / Prova: IGEDUC - Câmara de Abreu e Lima - Técnico em Informática - 2024

Em narrativas que descrevem cenários ou hábitos passados, o uso do pretérito imperfeito do indicativo é 
apropriado para expressar a continuidade ou regularidade das ações, 
como em "Ele [yellow]caminhava[reset] pela praia todas as manhãs".

Correto. As terminações para o pretérito imperfeito do indicativo são: 1ºAR (-AVA)/ 2ºER(-IA)/3ºIR(-ia)

24. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC / Prova: FUNDATEC - Prefeitura de Cruzaltense - Auxiliar de Saúde Bucal - 2024

Assinale a alternativa que indica a correta reescrita do trecho a seguir no pretérito perfeito do indicativo:

“E também há casos que envolvem sacrifícios”.

A. “E também haverá casos que envolverão sacrifícios”.
B. “E também havia casos que envolviam sacrifícios”.
C. “E também haviam casos que envolviam sacrifícios”.
D. “E também houveram casos que envolveram sacrifícios”.
E. “E também houve casos que envolveram sacrifícios”.

Na frase o verbo flexionado está na 3º pessoa do singular do presente do indicativo 'Ele há'
Na mesma frase o verbo 'envolver' está no presente do indicativo 'Eles envolvem'
eu envolvo / tu envolves / ele envolve / nós envolvemos / vós envolveis / [yellow]eles envolvem[reset]

O Verbo haver na frase está com sentido de "existir", logo é impessoal e fica no singular.

[yellow]eu houve[reset] / tu houveste / ele houve / nós houviamos / vós houvestes / [yellow]eles houveram[reset] -> [blue]pretérito perfeito do indicativo do verbo irregular 'HAVER'[reset]

25. Ano: 2024 / Banca: Legalle Concursos / Prova: Legalle Concursos - Prefeitura de General Câmara - Auditor Público Interno - 2024 

Na frase [yellow]"Toda escultura nasceu de uma matéria bruta [reset]"(l.12-13), o verbo está conjugado em qual tempo do modo indicativo?

A. Presente.
B. Pretérito imperfeito.
C. Pretérito perfeito.
D. Futuro do presente.

O pretérito perfeito é utilizado para expressar ações concluídas no passado.

nascer : eu nasci / tu naceste / [yellow]ele nasceu[reset] / nós nascemos / vós nascestes / eles nasceram -> Pretérito perfeito do indicativo

26. Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - Prefeitura de Miracema - Auxiliar de Laboratório - 2024 

Observe: [yellow]“E, cada vez mais, as pessoas reclamam da solidão.” [reset](4º§)
 Nas frases a seguir, as formas verbais destacadas estão flexionadas em tempos verbais diferentes da frase anterior, EXCETO:

A. “Nossos avós viviam altos e baixos.” (1º§)
B. “O amor tornou-se um produto descartável.” (1º§)
C. “A recompensa, porém, é um vínculo intenso e duradouro.” (2º§)
D. “Um dos sociólogos mais respeitados da atualidade, o polonês Zygmunt Bauman, escreveu o livro ‘Amor líquido’, [...]” (1º§)

'reclamam' -> presente do indicativo -> eu reclamo / tu reclamas / ele reclama / nós reclamamos / vós reclameis / [yellow]eles reclamam[reset]

[red]item 'A'[reset] -> 'viviam' -> futuro hipotético -> futuro do pretérito do indicativo -> terminação -RIA -> eu vivia / tu vivias / ele vivia / nós vivíamos / vós vivíeis / [yellow]eles viviam[reset]
[red]Item 'B'[reset] -> 'tornou' -> pretérito perfeito do indicativo -> eu tornei / tu tornaste / [yellow]ele tornou[reset]
[green]Item 'C'[reset] -> 'recompensa' -> presente do indicativo -> eu recompenso / tu recompensas / [yellow]ele recompensa[reset] <- Gabarito letra 'C'
[red]Item 'D'[reset] -> 'escreveu' -> pretérito perfeito do indicativo -> eu escrevo / tu escreveste / [yellow]ele escreveu[reset][reset]


27. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE / Prova: CESPE/CEBRASPE - DPF - Agente Administrativo Pré-Edital - 2024 - 9º Simulado

No primeiro período do terceiro parágrafo, a forma verbal “tem feito” veicula a ideia de uma ação passada que repercute no presente.

"Do que pouco ou nenhum caso [yellow]tem feito[reset] essa sociologia."

A forma verbal “tem feito” está no tempo composto pretérito perfeito do indicativo, que é usado para indicar uma ação que começou no passado e continua até o presente.

	O tempo composto pretérito perfeito do indicativo: presente do indicativo (ter ou haver) + verbo no particípio.

		'tem' -> presente do indicativo -> eu tenho / tu tens / [yellow]ele tem[reset] / nós temos / vós tendes / eles têm + feito ( forma nominal particípio do verbo FAZER )


28. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC / Prova: FUNDATEC - Prefeitura de Criciúma - Fiscal de Tributos - 2024 

Caso o tempo verbal da forma “recebiam” fosse alterado para o futuro do presente do indicativo na frase 
“Mais de 25 mil inscritos que recebiam, de forma gratuita, correspondências criadas por Fabrício”, 
ela seria corretamente escrita da seguinte forma: 
“Mais de 25 mil inscritos que ___________, de forma gratuita, correspondências criadas por Fabrício”.

Assinale a alternativa que preenche corretamente a lacuna do trecho acima.

A. receberá
B. recebem
C. receberam
D. receberão
E. receberiam

RECEBER -> futuro do presente -> (-REI) -> eu receberei / tu receberás / ele receberá / nós receberemos / vós recebereis / [yellow]eles receberão[reset]
	[bg_blue]O verbo deve concordar com o sujeito: 'mais de 25 mil inscritos'.[reset]


29. Ano: 2024 / Banca: Instituto Americano de Desenvolvimento - IADES / Prova: IADES - CFM - Assistente Administrativo Pós-Edital - 2024 - 1º Simulado

Em “o meu espírito nunca [yellow]pôde[reset] compreender grandes complicações”, a palavra sublinhada no texto está classificada, de acordo com o tempo e o modo verbal, no

A. pretérito perfeito do indicativo.
B. pretérito imperfeito do indicativo.
C. presente do indicativo.
D. futuro do presente do indicativo.
E. futuro do pretérito do indicativo.


[green]'poder' -> pretérito perfeito do indicativo -> Eu pude / Tu pudeste / Ele pôde / Nós pudemos / Vós pudestes / eles puderam[reset]
'poder' -> presente do indicativo -> eu posso / tu podes / ele pode / nos podemos / vós pudeis / eles podem
'poder' -> pretérito imperfeito do indicativo -> eu podia / tu podias / ele podia / nós podíamos / vós podíeis / eles podiam
'poder' -> futuro do presente  -> eu poderei / tu poderás / ele poderá / nós poderemos / vós podereis / eles poderam
'poder' -> futuro do pretérito -> eu poderia / tu poderias / ele poderia / nós poderiamos / vós poderieis / eles poderiam

30.  Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC / Prova: IBFC - IMBEL - Ajudante Geral - 2024

Observe oração em voz passiva e indique a voz ativa correta: “Daiane criou dois movimentos que foram eternizados pela Federação Internacional de Ginástica (FIG).”

A. Daiane criou dois movimentos que a Federação Internacional de Ginástica eternizou.
B. Daiane havia criado dois movimentos que foram eternos para a Federação Internacional de Ginástica.
C. Daiane criou dois movimentos, eternos para a Federação Internacional de Ginástica.
D. Daiane criou dois movimentos que a Federação Internacional de Ginástica eternizaram.
E. A Federação Internacional de Ginástica criou dois movimentos eternizados por Daiane.

'foram eternizados' -> 'foram' -> pretérito perfeito do indicativo 3º pessoa do plural - eles foram + participio -> voz passiva analítica
agente da voz passiva - > pela FIG
'eternizar' -> pretérito perfeito do indicativo -> eu eternizei / tu eternizaste / [yellow]ele eternizou[reset]
'daiane criou dois movimentos' -> sujeito paciente

	Daiane criou dois movimmentos que a FIG eternizou. <- CORRETO

O item 'B' não transforma para voz ativa corretamente, simplesmente colocou um tempo composto para confundir o candidato.
O item 'C' não transforma corretamente para voz ativa, devendo colocar o mesmo modo e tempo verbal da voz passiva, no pretérito perfeito do indicativo
No item 'D' a mesma coisa. Para transformar para a voz ativa corretamente, deverá transformar o verbo principal da voz ativa no mesmo tempo e modo verbal do verbo auxiliar 'SER'
No item 'E' o sentido da frase é alterado, dizendo que foi eternizados por Daiane. Sendo que quem eternizou foi a FIG.

31. Ano: 2024 / Banca: Universidade do Extremo Sul Catarinense - UNESC / Prova: UNESC - Prefeitura de Balneário Rincão - Assistente Social - 2024

"Isso [yellow]poderia[reset] elevar a média da temperatura para a época e pode tornar este um dos meses de setembro mais quentes já registrados no país."

Identifique a alternativa que apresenta um verbo no mesmo tempo e modo do destacado no texto.

A. "Caso queira alterar a agência bancária para receber o pagamento, o aposentado pode solicitar a mudança pelo aplicativo ou site Meu INSS."
B. "A crise das queimadas no Brasil chamou a atenção do país há duas semanas, quando a fumaça gerada por incêndios cobriu o céu de boa parte do país."
C. "O instituto alerta para o aumento das chances de ocorrerem incêndios florestais."
D. "O responsável pela obra informou que seriam necessários mais planejamentos, o que requereria uma contratação maior de engenheiros civis."
E. "O ocupante do ônibus intermediara a negociação entre os bandidos e policiais nesta sexta."


	A oração é hipotética. 'poderia' -> futuro do pretérito do indicativo -> 'eu poderia' <- 1º pessoa do singular

No item 'A' o verbo 'queira' está no presente do subjuntivo -> que eu queira. Porém não está no mesmo tempo.
No item 'B' o verbo 'chamou' está no pretérito perfeito do indicativo -> eu chamei / tu chamaste / ele chamou <- 3º pessoa do singular Não está no mesmo tempo e modo verbal
No item 'C o verbo 'ocorrerem' está no futuro do subjuntivo -> Também não está no mesmo tempo e modo verbal.
-> quando eu ocorrer / quando tu ocorreres / quando ele ocorrer / quando nós ocorrermos / quando vós ocorreis / [yellow]quando eles ocorrerem[reset]
[bg_green]No item 'D' o verbo 'seriam' está no futuro do pretérito do indicativo -> eu seria / tu serias / ele seria / nós seriamos / vos serieis / [reset]eles seriam[reset][reset]
No item 'E' o verbo 'intermediara' está no pretérito mais-que-perfeito do indicativo 1º pessoa do singular. Não corresponde ao mesmo tempo.


32.Ano: 2024 / Banca: Fênix Instituto Ltda / Prova: Fênix Instituto Ltda - Prefeitura de Rodeio - Auxiliar Administrativo - 2024 

No trecho "Dados do Banco Central mostram que movimentações do Pix somaram R$ 17,2 trilhões", a palavra "somaram" está em qual tempo e modo verbal?

A. Presente do indicativo.
B. Pretérito perfeito do indicativo.
C. Futuro do presente do indicativo.
D. Pretérito imperfeito do subjuntivo.

Presente do indicativo ( terminação -O ) : eu somo / tu somas / ele soma / nós somamos / vós somais / eles somam
[bg_green]pretérito perfeito do indicativo (-EI / I / I ) : eu somei / tu somaste / ele somou / nós somamos / vós somastes / eles somaram[reset]
Futuro do presente do indicativo ( -REI ): eu somarei / tu somarás / ele somará / nós somaremos / vós somareis / eles somarão
Pretérito imperfeito do subjuntivo ( -ASSE/-ESSE/-ISSE ): se eu somasse / se tu somasses / se ele somasse / se nós somassemos / se vós somasseis / se eles somassem

33.Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP / Prova: VUNESP - UNICAMP - Profissional da Arte, Cultura e Comunicação - Área: Revisor - 2024

Camarada, por estes calores do Estio que embotam a ponta da sagacidade, [yellow]repousemos[reset] do áspero estudo da Realidade humana... 
[yellow]Partamos[reset] para os campos do Sonho, vaguear por essas azuladas colinas românticas onde se ergue a torre abandonada do Sobrenatural, 
e musgos frescos recobrem as ruínas do Idealismo...
(Prólogo. Eça de Queirós. O Mandarim)

Mantendo-se a flexão no mesmo modo e pessoa em que estão conjugados os verbos “repousar” e “partir”, o prólogo é concluído corretamente com a frase:

A. Façamos fantasia!!!
B. Faríamos fantasia!!!
C. Faremos fantasia!!!
D. Fazemos fantasia!!!
E. Fizemos fantasia!!!

	[bg_red]O prólogo está no imperativo afirmativo.[reset]

[red]'repousemos'[reset] -> que eu repouse / que tu repouses / que ele repouse / [yellow]que nós repousemos[reset] / que vós repouseis / que eles repousem 
[red]'partamos'[reset]   -> que eu parta / que tu partas / que ele parta / [yellow]que nós partamos[reset] / que vós parteis / que eles partam

Do futuro do subjuntivo temos o imperativo afirmativo:

[red]'repousemos'[reset] -> repouses (tu) / repouse (você) / [yellow]repousemos (nós)[reset] / repouseis (vós) / repousem (vocês)
[red]'partamos'[reset]   -> partas (tu) / parta (você) / [yellow]partamos (nós)[reset] / parteis (vós) / partam (vocês)

[red]fazer[reset] -> futuro do subjuntivo -> que eu faça / que tu faças / que ele faça / que nós façamos / que vós faceis / que eles façam

	[bg_green]Portanto o gabarito é a letra 'A'[reset]

[red]'faríamos'[reset] -> [bg_bluefuturo do pretérito do indicativo (-RIA)[reset] -> eu faria / tu farias / ele faria / [yellow]nós faríamos[reset] / vós faríeis / ele fariam
[red]'faremos'[reset]  -> [bg_bluefuturo do presente (-REI)[reset] : eu farei / tu farás / ele fará / [yellow]nós faremos[reset] / vós fareis / ele farão
[red]'fazemos'[reset]  -> [bg_bluepresente do indicativo (-O)[reset] : eu faço / tu fazes / ele faz / [yellow]nós fazemos[reset] / vós fazeis / ele fazem 
[red]'fizemos'[reset]  -> [bg_blue]pretérito perfeito do indicativo (EI/I/I)[reset] : eu fiz / tu fezeste / ele fez / [yellow]nós fizemos[reset] / vós fizestes / eles fizeram

34.Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN
Prova: IDECAN - Prefeitura de Teresina - Auxiliar Educacional - 2024

- Escreva na louça a palavra ética!
- roubaram o giz, professora!

Assinale a alternativa em que a fala da professora tenha sido corretamente transposta para a forma “vós”.

A. Escrevai na lousa a palavra ética.
B. Escrevais na lousa a palavra ética.
C. Escrevei na lousa a palavra ética.
D. Escrevas na lousa a palavra ética.
E. Escreveis na lousa a palavra ética.

[bg_green]A fala da professora está no modo imperativo afirmativo. [reset]

'escreva' está no modo presente do subjuntivo. Para transformar para o imperativo afirmativo é necessário conjugar no presente do subjuntivo
E No presente do indicativo retirar os 'S' da 2º pessoa do singular/plural

[red]Presente do subjuntivo (e/a/a):[reset] que eu escreva / que tu escrevas / que ele escreva / que nós escrevamos / que vós escrevais / que eles escrevam
[red]Presente do indicativo (-O) :[reset] eu escrevo / tu escreve / ele escreveu / nós escrevemos / vós escreveis/ eles escrevem

[red]Imperativo afirmativo :[reset] escrevas (tu) / escreva (você) / escrevamos (nós) / [yellow]escrevei (vós)[reset] / escrevam (vocês)

			[bg_green]Alternativa 'C' a correta.[reset]

35. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Câmara de Fortaleza - Analista - Área Redação - 2024

Assinale a frase em que a forma verbal está correta.

A. O deputado [yellow]reveu[reset] todo o texto do projeto.
B. Os seguranças se [yellow]enterteram[reset] com as crianças.
C. O chefe da casa [yellow]reouve[reset] todo o tempo perdido.
D. Os policiais [yellow]interviram[reset] na discussão em plenário.
E. Serão nomeados os que a chefia [yellow]propor.[reset]

No item 'A' o correto seria: O deputado REVIU todo o texto do projeto.

	Pretérito perfeito do indicativo (EI/I/I) -> eu revi / tu revieste / [yellow]ele reviu[reset] / nós revimos / vós reviestes / ele revieram

						Utilizado para expressar ações concluidas no passado.

No item 'B' o correto seria 'ENTRETERAM' e não enterteram.

No item 'C' conjuga-se no verbo haver, no pretérito perfeito do indicativo: eu houve / tu houveste / [yellow]ele houve ( ele reouve )[reset]

No item 'D' o correto é 'intervieram' : eu intervim / tu intervieste / ele interveio / nós interviemos / vós interviestes / [yellow]eles intervieram[reset]

No item 'E' o correto seria 'propuser' : futuro do subjuntivo : se eu propuser / se tu propuseres / se ele propuser / se nós propusermos / se vós propuserdes / se eles propuserem

O futuro do subjuntivo é um tempo verbal que se utiliza para indicar uma ação futura que é incerta ou depende de uma condição. 
É comum em orações subordinadas introduzidas por conjunções como "quando", "se", "assim que", entre outras.

36. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV /Prova: FGV - DATAPREV - Analista de Tecnologia da Informação - Área Desenvolvimento de Software - Pós-Edital - 2024 - 1º Simulado

Observe a frase para responder à questão:

O aluno [yellow]tem estudado[reset] para as provas finais.

A forma verbal “tem estudado” expressa uma ação

A. iniciada no passado e com impacto no presente.
B. habitual e recorrente no passado.
C. realizada em um momento específico no presente.
D. interrompida antes de ser concluída.
E. concluída antes de outra ação no passado.

Item 'A' o gabarito, a forma composta do pretérito perfeito do indicativo 'tem estudado' é iniciada no passado e tem impacto até o presente momento.

Verbo Auxiliar "ter" no Presente do Indicativo + Particípio do Verbo Principal

Conjugação do Verbo "Estudar" no Pretérito Perfeito Composto do Indicativo:

Eu tenho estudado

Tu tens estudado

Ele/Ela/Você tem estudado

Nós temos estudado

Vós tendes estudado

Eles/Elas/Vocês têm estudado

37. Ano: 2024 / Banca: Instituto Verbena / Prova: Instituto Verbena - Câmara de Santo Antônio do Descoberto - Jardineiro - 2024 

Ao analisar os tempos verbais em destaque no trecho: “Não [yellow]é[reset] a primeira vez que o premiado livro de Jeferson Tenório, Avesso da Pele, é objeto de censura.
 Antes, [yellow]foi[reset] uma escola privada em Salvador, agora em Santa Cruz do Sul, no estado do Rio Grande do Sul.”, tem-se, respectivamente:

A. presente do indicativo e presente do subjuntivo.
B. pretérito imperfeito do indicativo e presente do indicativo.
C. pretérito imperfeito do indicativo e pretérito mais-que-perfeito do indicativo.
D. presente do indicativo e pretérito perfeito do indicativo.

A primeira oração nos indica um fato atual, presente. De que o livro foi premiado novamente.
Presente do indicativo do verbo SER: eu sou / tu és / [yellow]ele é[reset]/ nós somos / vós sois / eles são
O verbo 'foi' está no pretérito, dizendo que teve outra escola que censurou o livro. Poderia estar correto com um 'fora' pretérito mais-que-perfeito do indicativo.
Pretérito perfeito do indicativo SER: eu fui / tu foste / [yellow]ele foi[reset] / nós fomos / vós fostes / eles foram

	Portanto alternativa 'D' a correta.

38.Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura do Município de Araçariguama - Engenheiro Ambiental Sanitarista - 2024 
Analise as sentenças a seguir e assinale a alternativa em que o verbo empregado é irregular.

A. O incenso queimava por horas.
B. Ele pôs seu nome na lista de doadores de mantimentos.
C. Nós almoçamos em um restaurante italiano.
D. Sabrina adora livros de romance.
E. Não conheço este lugar.

'queimava' -> queimar -> regular -> pretérito imperfeito do indicativo -> eu queimava / tu queimava / ele queimava <- 1º pessoa do singular
'por' -> IRREGULAR -> pôs -> presente do indicativo -> eu ponho / tu pões / ele põe / nós pomos / vós pondes / eles põem
'almoçamos -> presente do indicativo -> eu almoço / tu almoça / ele almoçou / nós almoçamos / vós almoceis / eles almoçam
'adora' -> presente do indicativo -> eu adoro / tu adora / ele adorou / nós adoramos / vós adoreis / ele adoram
'conheço' -> presente do indicativo -> eu conheço / tu conhece / ele conheceu / nós conhecemos / vós conheceis / ele conhecem

39. Ano: 2024 / Banca: Instituto de Desenvolvimento Institucional Brasileiro - IDIB / Prova: IDIB - Prefeitura de Serra do Mel - Professor de Português - 2024

Analisando as transposições de voz ativa para passiva, assinale a única opção que preza pela correção gramatical e sintática e preserva o mesmo sentido do trecho original.

A."Os arqueólogos encontraram o corpo do suposto líder religioso enterrado de bruços." − 
O corpo do suposto líder religioso enterrado foi encontrado pelos arqueólogos de bruços.

B."Os antigos chefes da América Latina muitas vezes estabeleciam relações políticas e econômicas com líderes de comunidades próximas.” − 
Relações políticas e econômicas, muitas vezes, eram estabelecidas pelos líderes de comunidades próximas com os antigos chefes da América Latina.

C."A equipe de pesquisa acredita que a pessoa encontrada deitada no centro da sepultura tinha um status mais elevado." 
O − status mais elevado da pessoa encontrada deitada no centro da sepultura foi acreditado pela equipe de pesquisa.

D."A civilização da região ao redor de El Caño na época tratava o local como sagrado e adorava seus 'ancestrais'." 
Na época, o − local era tratado como sagrado pela civilização ao redor de El Caño e seus "ancestrais" eram adorados por ela.

A."Os arqueólogos encontraram o corpo do suposto líder religioso enterrado de bruços." 

'os arqueólogos' -> voz ativa (sujeito que realiza a ação)
'encontraram' -> verbo
'objeto direto' -> o corpo do suposto líder...

Para converter a frase "Os arqueólogos encontraram o corpo do suposto líder religioso enterrado de bruços." para a voz passiva, 
precisamos fazer com que o objeto direto (o corpo do suposto líder religioso) se torne o sujeito da nova frase, e o sujeito original (os arqueólogos) se torne o agente da passiva.

Voz Ativa:
Os arqueólogos encontraram o corpo do suposto líder religioso enterrado de bruços.

Voz Passiva:
O corpo do suposto líder religioso foi encontrado enterrado de bruços pelos arqueólogos.

Sujeito da Passiva: O corpo do suposto líder religioso

Verbo Auxiliar: foi

Particípio do Verbo Principal: encontrado

Complemento: enterrado de bruços

Agente da Passiva: pelos arqueólogos

[red]O corpo do suposto líder religioso enterrado foi encontrado pelos arqueólogos de bruços.[reset]
		[bg_red]Os arqueólogos não estavam de bruços e sim o líder religioso.[reset]

B."Os antigos chefes da América Latina muitas vezes estabeleciam relações políticas e econômicas com líderes de comunidades próximas.” 


O sujeito (quem faz a ação) é "Os antigos chefes da América Latina".

O verbo na voz ativa é "estabeleciam".

O objeto direto (o que recebe a ação) é "relações políticas e econômicas".

O complemento especifica com quem essas relações foram estabelecidas: "com líderes de comunidades próximas".

'estabeleciam' está na 3º pessoa do plural do pretérito imperfeito do indicativo (AVA/IA/IA)

Para transformar da voz ativa na passiva devemos:

1. Transformar o objeto direto (paciente) no sujeito da voz passiva: 'relações políticas e econômicas'
2. Utilizar o verbo auxiliar SER no mesmo tempo do verbo da voz ativa: pretérito imperfeito do indicativo : ERAM
3. Adicionar o verbo principal no participio: estabelecidas
4. Incluir o complemento após o tempo composto : verbo auxiliar flexionado + particípio do verbo principal
5. Incluir o agente da passiva: pelos antigos chefes da America Latina.

	Relações políticas e econômicas muitas vezes eram estabelecidas com líderes de comunidades próximas pelos antigos chefes da américa latina.


[red]Relações políticas e econômicas, muitas vezes, eram estabelecidas pelos líderes de comunidades próximas com os antigos chefes da América Latina.[reset]
[bg_red]Não foi feita corretamente a transformação da voz ativa para a voz passiva. O agente da passiva não ficou claro se foi os líderes de comunidades ou os antigos chefes.[reset]


A equipe de pesquisa acredita que a pessoa encontrada deitada no centro da sepultura tinha um status mais elevado."

agente ativo : a equipe de pesquisa (sujeito)
verbo : tinha
objeto direto: um status mais elevado
complemento: a pessoa encontrada no centro da sepultura

Voz passiva:

Sujeito da passiva: Um status mais elevado
Verbo auxiliar: (pretérito imperperfeito do verbo SER: eu era
Participio do verbo principal: atribuido
complemento: a pessoa encontrada no centro da sepultura
agente da passiva: pela equipe de pesquisa

		Um status mais elevado era atribuido a pessoa encontrada no centro da sepultura pela equipe de pesquisa.

Pretérito imperfeito do indicativo SER : Eu era / tu eras / ele era / nós éramos / vós éreis / eles eram

	D."A civilização da região ao redor de El Caño na época tratava o local como sagrado e adorava seus 'ancestrais'." 

sujeito : a civilização da região 
complemento: ao redor de El caño
verbo : tratava / adorava
objeto direto: o local como sagrado e adorava seus 'ancestrais.
complemento: na epoca

Na epoca, o local era tratado como sagrado e adorado pela civilização e seus ancestrais da região ao redor de El caño

Voz passiva:

complemento: na epoca
sujeito da passiva: o local como sagrado e adorava seus ancestrais
verbo auxiliar + particio: era tratado
complemento: ao redor de el cano

40. Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - TJ MA - Técnico Judiciário - Apoio Técnico Administrativo Pós-Edital - 2024 - 1º Simulado

No trecho “[...] essa história [yellow]tem apresentado[reset] novíssimas armas de uma ubiquidade e de um poder de penetração sem precedentes [...]” 
(2º §), a forma verbal destacada expressa a ideia de

A. conclusão imediata de uma ação.
B. continuidade de uma ação no passado que se estende até o presente.
C. ação futura prevista ou planejada.
D. repetição habitual de uma ação no passado.


alternativa 'b'
A forma verbal “tem apresentado” é a forma composta do pretérito perfeito do indicativo, usada para indicar uma ação que começou no passado e continua até o presente. 
	

41. Ano: 2024 / Banca: Centro de Extensão, Treinamento e Aperfeiçoamento Profissional Ltda - CETAP / Prova: CETAP - Prefeitura de Castanhal - Agente Administrativo - 2024

A conjugação do verbo prever, presente em: "prevê aumento" está grafada incorretamente em:

A. Eles prevêem.
B. Vós prevedes.
C. Eu prevejo.
D. Tu prevês.	

A forma correta é 'Eles preveem', sem acento circunflexo. Alternativa 'A'
A reforma ortográfica de 2009 eliminou o acento circunflexo em verbos terminados em '-eem' na terceira pessoa do plural do presente do indicativo.


42. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura de Juquitiba - Agente de limpeza urbana - 2024

	Talvez eu [yellow]consiga[reset] um ponto por origininalidade

O verbo “conseguir”, que ocorre no último quadrinho, está conjugado no modo subjuntivo, e exprime uma ação:

A. hipotética e futura.
B. concreta e presente.
C. concreta e passada.
D. em curso no presente.
E. hipotética e passada.	


conseguir -> presente do subjuntivo (e/a/a) -> 	que eu consiga <- 1º pessoa do singular -> exprime uma ideia hipotética e futura.
	
43. Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN
Prova: IDECAN - Prefeitura de Salvador - Enfermeiro PSF Pós-Edital - 2024 - 1º Simulado
 
A forma verbal destacada em “A diretriz vem causando polêmica entre educadores” tem valor de uma ação que

A. começou no passado e continua no presente.
B. mostra uma ação anterior a outra ação passada.
C. ocorre, provavelmente, no presente e no futuro.
D. começa e termina no presente.
E. se repete no passado.

A forma verbal “vem causando” apresenta a forma no gerúndio que significa um tempo que inicia no passado e se arrasta até o presente. 
Sendo assim, a letra “a” está correta.

44 .Ano: 2024 / Banca: ADVISE / Prova: ADVISE - Prefeitura de Serra da Raiz - Auxiliar de Serviços Gerais - 2024

 “Talvez discurse bem esta noite”.

Na frase acima o modo do verbo é:

A. Indicativo.
B. Imperativo.
C. Subjuntivo.
D. Adjunto.

		A frase é hipotética. O verbo 'discurse' está flexionado no presente do subjuntivo (e/a/a)
		que eu discurse <- 1º pessoa do singular do presente do subjuntivo - alternativa 'C'


45.Ano: 2024 / Banca: Instituto de Desenvolvimento Educacional, Cultural e Assistencial Nacional - IDECAN
Prova: IDECAN - IFAP - Professor de Educação Física - 2024

Na sentença “Vandirene (1) [yellow]precisava comprar[reset] sua comida e o dinheiro não (2) [yellow]chegava[reset]” os termos em destaque, respectivamente, são/estão:

A.1) locução verbal: verbo auxiliar na 3º pessoa do singular no pretérito mais-que-perfeito do indicativo + verbo principal no infinitivo; 2) verbo: 1º pessoa do singular do pretérito imperfeito do modo subjuntivo.
B.1) tempo composto verbal: 1º pessoa do singular do pretérito perfeito do indicativo; 2) verbo: 32 pessoa do singular do pretérito perfeito do modo indicativo.
C.1) tempo composto verbal: 3º pessoa do singular do pretérito imperfeito do indicativo; 2) verbo: 3º pessoa do singular do pretérito imperfeito do modo indicativo.
D.1) tempo composto verbal: 1º pessoa do singular do pretérito imperfeito do indicativo; 2) verbo: 1º pessoa do singular do pretérito perfeito do modo subjuntivo.
E.1) locução verbal: verbo auxiliar na 3º pessoa do singular no pretérito imperfeito do indicativo + verbo principal no infinitivo; 2) verbo: 3º pessoa do singular do pretérito imperfeito do modo indicativo.

'chegava' está na 3º pessoa do singular 'ele chegava' do pretérito imperfeito do indicativo
'precisava comprar' é uma locução verbal e não um tempo composto pelo verbo auxiliar 'precisava' na 3º pessoa do singular do pretérito imperfeito do indicativo
e o verbo principal 'comprar' no infinitivo.

46. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TRF 1 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 2º Simulado
Leia a frase de Albert Einstein:

“A condição dos homens [yellow]seria[reset] lastimável se tivessem de ser domados pelo medo do castigo ou pela esperança de uma recompensa depois da morte.”

A forma verbal destacada está conjugada no:

A. pretérito perfeito do indicativo.
B. pretérito imperfeito do indicativo.
C. pretérito imperfeito do subjuntivo.
D. futuro do subjuntivo.
E. futuro do pretérito do indicativo.


'seria' está no futuro do pretérito do indicativo, terminação '-RIA' -> eu seria / tu serias / ele seria / nós seriamos / vós serieis / eles seriam
			alternativa 'E' gabarito da questão


47. Ano: 2024 / Banca: Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas Gerais – IFSULDEMINAS - IFSULDEMINAS
Prova: IFSULDEMINAS - IFSULDEMINAS - Professor de Letras - 2024

Sobre o emprego e o sentido de tempos verbais do modo indicativo, conforme Abaurre e Pontara, 
analise as assertivas a seguir, assinalando V, se verdadeiras, ou F, se falsas.


( ) Quando se usa o presente do indicativo (o momento do evento corresponde ao momento da enunciação da fala), se dá a entender que a ação nomeada pelo verbo ocorre exatamente no momento em que é expressa. Por exemplo: “Maria escreve”.

( ) Pode-se usar o presente do indicativo para expressar ação habitual. Por exemplo: “Maria come, dorme, reclama”.

( ) O pretérito imperfeito refere-se a um ato inconcluso, que se prolonga por algum tempo no passado. Por exemplo: “Maria nadava na piscina nas férias”.

( ) O futuro do presente refere-se a um fato futuro, que pode ocorrer ou não, relacionado a um fato passado. Por exemplo: “Eu tinha certeza de que compraria um carro no ano passado, mas não consegui”.


Item 1 Verdadeiro
Item 2 Verdadeiro - Pode-se usar o presente do indicativo para expressar ação habitual no presente.
Item 3 Verdadeiro - O pretérito imperfeito refere-se a um ato inconcluso no passado e que se prolonga no passado também
Item 4 Falso -  O futuro do presente refere-se a um fato que ocorrerá no futuro em relação ao momento da fala, e não a um fato passado. 
Diferente do futuro do pretérito do indicativo. em que indica uma ação futura em relação a um momento passado.
A frase 'Eu tinha certeza de que compraria um carro no ano passado, mas não consegui' está no futuro do pretérito.

48. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura de Pedreira - Auxiliar de Oficina - 2024 
Assinale a alternativa que apresenta um verbo impessoal.

A. Os rapazes foram mais corajosos que as garotas.
B. Meus pais dizem que adoram churrasco.
C. Essas ideias, que não funcionam na prática, serão descartadas.
D. Os funcionários argumentaram que precisavam de férias imediatamente.
E. Nevou muito fortemente ontem de manhã.

Verbos que indicam fenômenos da natureza sempre serão impessoais. 'nevou' é um verbo impessoal.
O verbo 'nevou' é impessoal, pois descreve um fenômeno da natureza e não possui sujeito. Está de acordo com o gabarito da banca.

49. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Prefeitura de Águas de Lindóia - Cirurgião Dentista - 2024 

No excerto “Os falantes monolíngues [yellow]tendem[reset] a descrever essas cores englobando-as em muitos tons além do que um falante de espanhol ou inglês incluiria.”, 
a ação expressa pelo verbo ‘tendem’, em termos de aspecto, é:

A. incoativa.
B. finalizada.
C. descontínua.
D. pontual.
E. durativa.

"Os falantes monolíngues tendem a descrever essas cores..."

	Incoativa se refere a uma ação que está começando. Sendo que é algo contínuo, duradouro. [bg_red]Item 'A' ERRADO[reset]
	finalizada se refere a uma ação que já foi concluida. O verbo 'tendem' no contexto é uma ação habitual, sem indicar conclusão. [bg_red]Item 'B' ERRADO[reset]
	descontínuo se refere a uma ação que ocorre de forma intermitente, com interrupções, que parou no tempo. Portanto o [bg_red]item 'C' ERRADO[reset]
	O pontual se refere a uma ação que ocorre em um ponto específico no tempo, sem duração. No caso do verbo 'tendem', a ação é contínua, com duração. [bg_red]Item D ERRADO[reset]
	O aspecto durativo se refere a uma ação que se prolonga no tempo, sem indicação de início ou fim. 
	No caso do verbo 'tendem', a ação é contínua, o que é característico do aspecto durativo. [bg_green]ITEM 'E' CORRETO[reset]

50.Ano: 2024 / Banca: COSEAC / Prova: COSEAC - FME - Professor - Área: Língua Portuguesa - 2024

Com relação à análise mórfica da forma verbal “tomavam”, é correto afirmar que

A. o primeiro –a– é a vogal temática.
B. esse vocábulo é composto por três morfemas.
C. o segmento –vam é a desinência modo-temporal.
D. o segmento toma– é o radical.esse vocábulo pertence a um verbo irregular de primeira conjugação.
E. esse vocábulo pertence a um verbo irregular de primeira conjugação.

Item 'A' está correto.
Item 'B' Mais de 3 morfemas: Tom: radical / a: vogal temática / va: modo- temporal pretérito imperfeito / m: número -pessoal terceira pessoa do plural
Item 'C' correto. Não é o gabarito mas está correto.
Item 'D' INCORRETO; não é verbo irregular
Item 'E' INCORRETo não é verbo irregular

51.Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE / Prova: CESPE/CEBRASPE - TSE-UNIF - Analista Judiciário - Área Arquivologia Pós-Edital - 2024 - 1º Simulado

No trecho “A Justiça Eleitoral [yellow]possui[reset] diversos mecanismos para garantir à eleitora e ao eleitor o acesso ao local de votação”, 
O verbo “possuir” está conjugado no pretérito perfeito do indicativo, indicando uma ação concluída.

C. Certo
E. Errado

Presente do indicativo:		   eu possuo / tu possuis   / [yellow]ele possui[reset]  / nós possuimos / vós possuis    / eles possuem
Pretérito perfeito do indicativo : [red]eu possuí[reset] / tu possuiste / ele possuiu / nós possuimos / vós possuístes / eles possuíram

No pretérito perfeito do indicativo 1º pessoa do singular eu possuí ( a vogal i é tônica). Além de exprimir passado concluido.
A frase completa está no indicativo no tempo presente, no tempo atual, referindo-se a Justiça eleitoral . 
Portanto é: ela possui <- 3º pessoa do singular do presente do indicativo

	questão ERRADA. Não está no pretérito perfeito do indicativo e sim no presente do indicativo.

52. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC
Prova: FUNDATEC - Prefeitura de Ibirapuitã - Professor de Educação Física - 2024 

Assinale a alternativa que apresenta, correta e respectivamente, 
a classe morfológica das palavras sublinhadas no trecho a seguir: 

	“Lídia nasceu [yellow]no[reset] Distrito Federal, mas seus pais [yellow]são[reset] cearenses [yellow]da[reset] região da Ibiapaba”.

A. Preposição (contração)  – verbo – adjetivo – preposição (contração)
B. Preposição (combinação) – verbo – adjetivo – preposição (combinação).
C. Preposição (contração)  – adjetivo – substantivo – conjunção (combinação).
D. Conjunção  (contração)  – adjetivo – verbo – preposição (contração).
E. Conjunção  (combinação) – adjetivo – substantivo – preposição (combinação).

A resposta é a alternativa 'A'.

Na contração há uma espécie de aglutinação ( perdem elementos na união )
 enquanto que na combinação há justaposição. ( não perdem elementos )

53. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC / Prova: FUNDATEC - Prefeitura de Bagé - Terapeuta Ocupacional - 2024 

Assinale a alternativa que indica a correta transposição do trecho a seguir da voz passiva sintética para a analítica.

			“Abrem-se condições para uma disputa mental”.

A. Condições é aberta para uma disputa mental.
B. Condições são abertas para uma disputa mental.
C. Condições foi aberta para uma disputa mental.
D. Condições foram abertas para uma disputa mental.
E. Condições serão abertas para uma disputa mental.

A voz passiva sintética é caracterizada pelo uso do pronome 'se' junto ao verbo.
enquanto a voz passiva analítica é formada pelo verbo auxiliar 'SER' flexionado + seguido do particípio do verbo principal. 

	Flexiona o verbo auxiliar no mesmo tempo e modo que o verbo principal na voz passiva sintética: 'abrem' para 'aberta'

Presente do indicativo: eu abro / tu abris / ele abri / nós abrimos / vós abrireis / [yellow]eles abrem[reset]
Presente do indicativo SER: eu sou / tu és / ele é / nós somos / vós sois / [yellow]eles são[reset]

A forma verbal 'são abertas' está no plural, concordando corretamente com o sujeito 'Condições'. Alternativa 'B'

54. Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TRT 7 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 3º Simulado

Transpondo-se a frase Ele também reforçou a necessidade (3º parágrafo) para a voz passiva analítica, a forma verbal resultante será:

A. foi reforçada.
B. era reforçada.
C. é reforçada.
D. seria reforçada.
E. será reforçada.

'reforçou' : Pretérito perfeito do indicativo : eu reforçei / tu reforçaste / [yellow]ele reforçou[reset] / nós reforçamos / vós reforceis / eles reforçaram
verbo SER: pretérito perfeito do indicativo : eu fui / tu foste / [yellow]ele foi[reset] / nós fomos / vós fostes / ele foram

Portanto alternativa 'A' - Foi reforçada

55. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - SPTRANS - Analista de Comunicação - 2024
Assinale a alternativa cuja frase apresenta correlação verbal correta.

A. Se as mudanças tecnológicas avançarão muito, resolveriam o problema…
B. Se as mudanças tecnológicas avançassem muito, resolverão o problema…
C. Se as mudanças tecnológicas avançarem muito, resolveram o problema…
D. Se as mudanças tecnológicas avançam muito, resolvessem o problema…
E. Se as mudanças tecnológicas avançarem muito, resolverão o problema…


Na afirmativa 'A' a frase inicia como uma hipótese 'se as mudanças' e o verbo 'avançarão' exprime certeza, algo pontual no tempo.  Além disso 'resolveriam'
não correlaciona com 'resolverão'. futuro do presente não correlaciona com futuro do pretérito que é algo no futuro hipotético.

Na afirmativa 'B' 'avançassem' está no pretérito imperfeito do subjuntivo a qual não correlaciona com o futuro do presente.
O pretérito imperfeito do subjuntivo correlaciona com o futuro do pretérito (-RIA) ou com o pretérito imperfeito do indicativo (-AVA/-IA-IA)

Ex: Se as mudanças tecnológicas avançassem muito, [yellow]resolveriam[reset] o problema / Se as mudanças tecnológicas avançassem muito, [yellow]resolviam[reset] o problema.

Na afirmativa 'C' está no futuro do subjuntivo 'avançarem' e 'resolveram' está no pretérito imperfeito do subjuntivo a qual NÃO se correlacionam.
O futuro do subjuntivo correlaciona com o futuro do presente. O correto seria:

		Se as mudanças tecnológicas [yellow]avançarem[reset] muito, [yellow]resolverão[reset] o problema.

Na afirmativa 'D', o 'avançam' presente do indicativo e 'resolvessem' pretérito imperfeito do subjuntivo não se correlacionam.
O presente do indicativo correlaciona somente com o presente do subjuntivo (e/a/a) ou com o proprio presente do indicativo

		Se as mudanças tecnológicas [yellow]avançam[reset] muito, [yellow]resolvem[reset] o problema.

O item 'E' é a correção do item 'C'. O emprego da correlação está correto.

		[blue]'avançarem' está no futuro do subjuntivo[reset] [bg_yellow]+[reset] [blue]'resolverão' futuro do presente[reset]


56. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Câmara de São Paulo - Procurador Legislativo - 2024

Assinale a frase em que houve erro na conversão da voz passiva pronominal para a voz ativa.

A. Aqui se empregam mulheres? / Aqui empregam mulheres?
B. Encontrou-se o relógio roubado? / Encontraram o relógio roubado?
C. Há de fazer-se o trabalho. / Há de fazerem o trabalho.
D. Devolveu-se-lhe o livro. / Devolveram-lhe o livro.
E. Aqui estão as caixas que se haviam perdido / Aqui estão as caixas que haviam perdido.

A questão nos pede a alternativa incorreta em relação a transposição da voz passiva sintética (com o pronome "se), também chamada de voz passiva pronominal, para a voz ativa.

Para haver voz passiva, o verbo deve ser obrigatoriamente transitivo direto. Ou seja, deve existir um objeto direto na voz ativa, pois ele se transformará no sujeito passivo na voz passiva.

Voz Ativa: Sujeito - Objeto Direito
Voz Passiva: Agente da Passiva - Sujeto

Vamos ver um exemplo?

• Voz ativa: Os políticos não reconhecem a importância da educação. (Reconhecer é verbo transitivo direto e a importância da educação é o objeto direto)
• Voz passiva analítica: A importância da educação não é reconhecida pelos políticos (O objeto direto da voz ativa virou o sujeito passivo na voz passiva)
• Voz passiva sintética: Não se reconhece a importância da educação.

Portanto, o primeiro passo para saber se é voz passiva é identificar se há verbo transitivo direto. Além disso, você notou que, na voz passiva sintética, não aparece o agente da passiva? 
Se o agente da passiva não está expresso, quando a gente transpor a oração para a voz ativa, o sujeito não ficará expresso. A gente sabe que alguém praticou a ação, mas não sabemos quem. 
Portanto, na passagem da voz passiva pronominal para a voz ativa, teremos um sujeito indeterminado.


Você se lembra do que é um sujeito indeterminado e quais as situações em que geralmente temos esse tipo de sujeito?

O sujeito indeterminado existe, só que nós não conseguimos identificá-lo. Geralmente, os casos de sujeito indeterminado acontecem nas seguintes situações:

Verbo na terceira pessoa do plural sem um sujeito expresso → Roubaram minha bicicleta.

Verbo transitivo indireto na terceira pessoa do singular + partícula "se" → Precisa-se de professores de Língua Portuguesa.

Verbo no infinitivo impessoal → Ler é bom ("Ler" é o sujeito de "é", mas o sujeito de "ler" é indeterminado).

Pronto. Com essa teoria, ficará "mais fácil" resolver a questão. Vamos lá?

a) Aqui se empregam mulheres? / Aqui empregam mulheres? - CERTO

Antes de transformar em voz ativa, vamos fazer a comparação com a voz passiva analítica:


• Aqui se empregam mulheres? → Aqui mulheres são empregadas?

O sujeito da voz passiva é "mulheres". Logo, na voz ativa, essa expressão será o objeto direto. Lembre-se:

Voz Ativa: Sujeito - Objeto Direito

Voz Passiva: Agente da Passiva - Sujeito

Na voz passiva, não sabemos quem emprega as mulheres, não sabemos quem é o agente da passiva.

Logo, na voz ativa, não saberemos quem será o sujeito. Ele é sujeito indeterminado. Uma das formas de indeterminar o sujeito, como vimos, é colocá-lo na terceira pessoa do plural:

• Aqui empregam mulheres?



b) Encontrou-se o relógio roubado? / Encontraram o relógio roubado? - CERTO

Transformando para a voz passiva analítica: o relógio roubado foi encontrado?


O sujeito é "o relógio roubado". Na voz ativa, ele será o objeto direto. Não há agente da passiva.

Então, na voz ativa, o sujeito será indeterminado (verbo na terceira pessoa do plural SEM a partícula "se")

• Encontraram o relógio roubado?


c) Há de fazer-se o trabalho. / Há de fazerem o trabalho. - ERRADO *************************************

Aqui, temos uma locução verbal: "há de fazer". O verbo haver só é impessoal quando ele tem o sentido de existir.

A locução haver de + infinitivo, com o sentido de futuro, é formada pelo verbo no infinitivo + presente do indicativo do verbo haver. Equivale ao futuro do presente do modo indicativo:


Eu provar + hei ⇔ Eu hei de provar ⇔ Eu provarei
Tu provar + hás ⇔ Tu hás de provar ⇔ Tu provarás
Ele provar + há ⇔ Ele há de provar ⇔ Ele provará
Nós provar + havemos ⇔ Nós havemos de provar ⇔ Nós provaremos
Vós provar haveis ⇔ Vós haveis de provar ⇔ Vós provareis
Eles provar hão ⇔ Eles hão de provar ⇔ Eles provarão

Vamos transformar para a voz passiva analítica:


• Há de fazer-se o trabalho → O trabalha há de ser feito (= o trabalho será feito)


Note que não há sentido de existir. O verbo haver é o verbo auxiliar da locução verbal.

Logo, ele pode ser flexionado no plural normalmente. Na voz ativa, temos que usar o verbo na terceira pessoa do plural para indeterminar o sujeito, lembra?


• Hão de fazer o trabalho.


d) Devolveu-se-lhe o livro. / Devolveram-lhe o livro. - CERTO

Vamos transformar para a voz passiva analítica primeiro:


• Devolveu-se-lhe o livro → O livro lhe foi devolvido (ou O livro foi-lhe devolvido)


O sujeito da voz passiva (o livro) será o objeto direto na voz ativa. E o sujeito na voz ativa será indeterminado, na terceira pessoa do plural e sem a partícula "se", já que não temos agente da passiva.


• Devolveram-lhe o livro.



e) Aqui estão as caixas que se haviam perdido / Aqui estão as caixas que haviam perdido. - CERTO

Passando para a voz passiva analítica:


• Aqui estão as caixas que se haviam perdido → Aqui estão as caixas que se haviam sido perdidas


Você já sabe que "as caixas" será o objeto direto e o verbo ficará na terceira pessoa do plural sem a partícula "se". A oração que está na voz passiva é a segunda, a negritada: Aqui estão as caixas que se haviam perdido. Dessa forma, é só nela que vamos mexer:


• Aqui estão as caixas que haviam perdido.

57. Ano: 2024 / banca: Instituto Brasileiro de Formação e Capacitação - IBFC / Prova: IBFC - FAGIFOR - Fisioterapeuta - Área: Intensivista - 2024 

Assinale a alternativa correta em relação à passagem de voz passiva para voz ativa na oração: Um raro adereço indígena foi encontrado pelo Iphan.

A. O Iphan encontrara um raro adereço indígena.
B. Um raro adereço indígena tinha sido encontrado pelo Iphan.
C. O Iphan encontra um raro adereço indígena.
D. Um raro adereço indígena teria sido encontrado pelo Iphan.
E. O Iphan encontrou um raro adereço indígena.

Voz passiva:
'um raro adereço indígena' -> agente passivo <- 
'foi encontrado' -> SER + participio
'pelo Iphan' -> sujeito agente

Voz ativa:
'O Iphan' -> agente ativo
verbo 'encontrar' no pretérito perfeito 'encontrou'
Objeto direto: 'um raro adereço indígena'

	O iphan encontrou um raro adereço indígena

58. Ano: 2024 / Banca: Centro de Extensão, Treinamento e Aperfeiçoamento Profissional Ltda - CETAP / Prova: CETAP - SEOP - Técnico em Gestão Pública - Área: Ciências Econômicas - 2024

A transposição para voz passiva analítica de: "As alunas [yellow]escolheriam[reset] um dos títulos." está adequada em:

A. Um dos títulos foram escolhidos pelas alunas.
B. Escolher-se-á um dos títulos.
C. Um dos títulos serão escolhidos pelas alunas.
D. Escolher-se-ão pelas alunas.
E. Um dos títulos seria escolhido pelas alunas.

No item 'A' o verbo 'foram' está no pretérito perfeito do indicativo, tempo e modo verbal errado.
No item 'B' a transposição está errada. E a mesóclise também
No item 'C' o verbo 'serão' está no futuro do presente, tempo e modo verbal diferente do verbo principal 'escolheriam'
No item 'D' a transposição está errada.
No item 'E' o verbo 'seria' está no mesmo modo e tempo verbal do verbo principal 'escolheriam' -> futuro do pretérito do indicativo


59 .Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - Prefeitura de Jaboatão dos Guararapes - Auditor Fiscal Tributário - 2024
 
Seria razoável supor que, quanto mais sabemos sobre o mundo, mais perto estaríamos de um destino final

Mantém-se a adequada correlação entre os tempos e modos das formas verbais sublinhadas na frase acima caso elas sejam substituídas, na ordem dada, por:

A. Teria sido - sabermos - estávamos
B. Será - soubermos - estivéssemos
C. Será - soubéssemos - estivemos
D. Será - soubermos - estaremos
E. Teria sido - sabíamos - estamos

Item 'a'.'teria sido' está no futuro do pretérito composto. 'sabermos' esta no infinitivo pessoal e 'estávamos' está pretérito imperfeito do indicativo.
				Não há nenhuma correlação verbal entre os tempos.

Item 'b'.'será' está no futuro do prente. 'soubermos' está no futuro do subjuntivo <- Há relação verbal, porém 'estivéssemos' está no pretérito imperfeito do subjuntivo.
				Não há correlação com os outros tempo e modos verbais.
[blue]O pretérito imperfeito do subjuntivo tem correlação com o futuro do pretérito simples e com o pretérito imperfeito do indicativo[reset]

Item 'c' o verbo 'será' está no futuro do presente e 'soubéssemos' está no pretérito imperfeito do subjuntivo <- Não há correlação verbal entre eles
		O futudo do presente tem correlação verbal com o futuro do subjuntivo (-R) ou com presente do subjuntivo (e/a/a)
O verbo 'estivemos' está no pretérito perfeito do indicativo que por sua vez correlaciona somente com o pretérito mais-que-perfeito do indicativo. (-ara/-era/-ira)

Item 'D' 'será' estpa no futuro do presente e 'soubermos' está no futuro do subjuntivo <- HÁ CORRELAÇÃO VERBAL SIM.
			Por sua vez 'estaremos' está no futuro do presente a qual se relacionam.

Item 'E' 'teria sido' está no futuro do pretérito composto. 'sabíamos' está no pretérito imperfeito do indicativo e 'estamos' está no presente do indicativo
		 			o qual não há correlação nenhuma!



60 .Ano: 2024 / Banca: Instituto Mais - IMAIS / Prova: IMAIS - Câmara de Santo André - Agente Legislativo - 2024

“Esta conclusão indica que os seres humanos fizeram uma compensação evolutiva”.

Assinale a alternativa que transpôs a frase acima para a voz passiva, em conformidade com a norma-padrão da Língua Portuguesa.

A. “Esta conclusão indica que uma compensação evolutiva foi feita pelos seres humanos”.
B. “Esta conclusão indica que uma compensação evolutiva havia sido feita pelos seres humanos”.
C. “Esta conclusão indica que uma compensação evolutiva tinha sido feita pelos seres humanos”.
D. “Esta conclusão indica que uma compensação evolutiva está sendo feita pelos seres humanos”.	


'fizeram' está no pretérito perfeito do indicativo - eu fiz / tu fizeste / ele fez / nós fizemos / vós fizestes / [yellow]eles fizeram[reset]

'foi' é pretérito perfeito do indicativo do verbo SER - eu fui / tu foste / [yellow]ele foi[reset] / nós fomos / vós fostes / eles foram
	
+ participio do verbo principal FAZER -> [yellow]feito[reset]


61. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC
Prova: FUNDATEC - Prefeitura de Carlos Barbosa - Médico Ginecologista e Obstetra - 2024 

Ao converter o fragmento “Os cinéfilos apreciam os filmes hollywoodianos” para a voz passiva, a reescrita será:

A. Os filmes hollywoodianos estão sendo apreciados pelos cinéfilos.
B. Filmes hollywoodianos serão apreciados pelos cinéfilos.
C. Os cinéfilos vão apreciar os filmes hollywoodianos.
D. Os filmes hollywoodianos são apreciados pelos cinéfilos.
E. Cinéfilos apreciam filmes hollywoodianos.


'apreciam' está no presente do indicativo, portanto o verbo auxiliar 'SER' deve ser flexionado para o mesmo tempo e modo verbal:

	eu sou / tu és / ele é / nós somos / vós sois / eles são + participio do verbo principal : 'apreciados'


Alternativa 'D'.

62. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - PM SP - Soldado PM de 2ª Classe Pós-Edital - 2024 - 1º Simulado
Observe o período abaixo:

Na literatura carioca, [yellow]era registrado[reset] o termo samba.

Há um exemplo de voz passiva com o verbo ser. Assina-le a alternativa que transforma essa frase corretamente para a voz ativa.

A. Na literatura carioca, registravam-se o termo samba.
b. Na literatura carioca, registrou-se o termo samba.
C. Na literatura carioca, registrava-se o termo samba.
D. Na literatura carioca, o termo samba era registrado.
E. Na literatura carioca, registravam o termo samba.

'era' está no pretérito imperfeito do indicativo do verbo SER

	'eu era / tu eras / ele era / nós eramos / vós éreis / eles eram'

'registrar' - Pretérito imperfeito do indicativo -> eu registrava / tu registravas / ele registrava / nós registravamos / vós regestraveis / [yellow]eles registravam[reset]

tem um sujeito indeterminado (pode-se entender que alguém ou eles faziam o registro). Portanto o gabarito é letra 'E'.

63 .

A frase O diretor [yellow]alterou[reset] o horário de funcionamento da empresa está na voz ativa. 

Qual forma verbal teríamos se essa mesma frase fosse convertida para a voz passiva analítica?

A. Alterou-se.
B. Será alterado
C. Se alterou.
D. Alterar-se-á.
E. Foi alterado.

'alterou' está no pretérito perfeito do indicativo -> eu alterei / tu alteraste / [yellow]ele alterou[reset] / nós alteramos / vós alterastes / eles alteraram

verbo SER no pretérito perfeito do indicativo -> eu fui / tu foste / [yellow]ele foi[reset] / nós fomos / vós fostes / eles foram + participio do verbo principal

Alternativa 'E'.

64. Ano: 2024 / Banca: Centro de Extensão, Treinamento e Aperfeiçoamento Profissional Ltda - CETAP
Prova: CETAP - Prefeitura de Castanhal - Agente Administrativo - 2024

No excerto "Essa sensação de Apocalipse, segundo o psiquiatra, é alimentada pelo medo (...)", a estrutura, ao passar à voz ativa, está correta em:

A. O medo alimentará, segundo o psiquiatra, a sensação de Apocalipse.
B. Alimenta-se o medo da sensação de Apocalipse.
C. Alimentou-se o medo pela sensação de Apocalipse.
D. O medo alimenta essa sensação de Apocalipse, segundo o psiquiatra.


'é' do verbo SER está no presente do indicativo + participio do verbo principal 'alimentada'.
'pelo medo': agente da passiva <- realiza a ação de voz passiva
'segundo o psiquiatra' : complemento
'essa sensação de apocalipse': sujeito <- sofre a ação

voz ativa:

'o medo' : sujeito
verbo: alimenta; ( alimenta o que? ) transitivo direto
objeto direto: essa sensação de Apocalipse
Complemento: segundo o psiquiatra

O medo alimenta essa sensação de Apocalipse, segundo o psiquiatra. Alternativa 'D'

65. Ano: 2024 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Mato Leitão - Professor - Área: Educação Física - 2024 
Transpondo a oração: “Pedro amava a cidade grande.” para a voz passiva analítica, obteremos a forma verbal:

A. Foi amada.
B. Era amada.
C. É amada.
D. Fora amada.

'amava' está no pretérito imperfeito do indicativo, exprimindo um passado habitual.
Para a voz passiva analítica temos:

A cidade grande [yellow]era amada[reset] por Pedro <- mesmo sentido textual, um passado habitual.

	eu amava / tu amavas / ele amava

Na alternativa 'A' 'foi' está em um passado que ficou no passado. Pretérito Perfeito do indicativo

	eu fui / tu foste / ele foi

Na alternativa 'C' o verbo 'é' está no presente do indicativo, exprimindo uma ação no presente momento, atual.

	eu sou / tu és / ele é

Na alternativa 'D' 'fora' está no pretérito mais-que-perfeito do indicativo (ara/era/ira)

	eu fora / tu foras / ele fora / nós fôramos / vós fôreis / eles foram

	Seria correto se a frase estivesse escrita da seguinte forma:

			Pedro amara a cidade grande. < voz ativa
			A cidade grande fora amada por Pedro <- voz passiva analítica

66.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TRT 7 - Técnico Judiciário - Área: Administrativa - 2024

É adequada a articulação entre os tempos e modos verbais na seguinte frase:

A. Ficamos sem saber por que [yellow]vem[reset] ela se dedicado a atos virtuosos que sua doença lhe [yellow]impedisse[reset] de haver praticado.
B. Quando [yellow]perdesse[reset] a voz, em função da distrofia que lhe [yellow]acometeria[reset], ela [yellow]passará[reset] a ensinar surdos e mudos.
C. Fora uma mulher em paz consigo mesma, apesar dos sofrimentos que a vida lhe reserve, ao desafiar seus limites.
D. Quando me confessou que se mataria, não me surpreendi e disse que muita gente poderia vir a tomar igual decisão.
E. Segundo meu amigo, a dor maior comparece quando nos convencêssemos de que não sejamos os únicos a sofrer.


Na alternativa 'A' está errada a colocação no presente do indicativo "'vem' ela" com o pretérito imperfeito do subjuntivo 'impedisse'
O texto nos traz uma incerteza, uma dúvida.
Portanto o correto seria a correlação entre pretérito imperfeito do indicativo 'VINHA' com o pretérito imperfeito do subjuntivo. 'IMPEDIA'

	Ficamos sem saber por que 'vinha' ela se dedicado a atos virtuosos que sua doença lhe 'impedia' de haver praticado.

O pretérito imperfeito do indicativo é usado para expressar ações habituais, contínuas ou repetitivas no passado. 
Ele também é utilizado para descrever situações, estados ou condições que duraram um certo período no passado.

O pretérito imperfeito do subjuntivo é usado para expressar situações hipotéticas, desejos, incertezas, ou ações não realizadas no passado, 
geralmente dependendo de uma condição ou de outra ação que não ocorreu. 
Ele é frequentemente empregado em orações subordinadas introduzidas por "se", "quando", "caso", "embora", entre outras.


No item 'b': Quando [yellow]perdesse[reset] a voz, em função da distrofia que lhe [yellow]acometeria[reset], ela [yellow]passará[reset] a ensinar surdos e mudos.

	'perdesse' exprime dentro do contexto, incerteza algo duvidoso sem fim, deveria estar no futuro do subjuntivo, algo no futuro que exprime incerteza.
	'perder' a voz seria o mais adequado. -> futuro do subjuntivo
	'acometeria' está no futuro do pretérito , dentro do contexto o mais adequado um passado que fica no passado, o pretérito perfeito do indicativo -> 'acometeu'
	'passará' está no futuro do presente afirmando que irá ensinar surdos e mudos.

O correto seria:

		Quando [yellow]perder[reset] a voz, em função da distrofia que lhe [yellow]acometeu[reset], ela [yellow]passará[reset] a ensinar surdos e mudos.

							ou

		Quando [yellow]perdesse[reset] a voz, em função da distrofia que lhe [yellow]acometeu[reset], ela [yellow]passaria[reset] a ensinar surdos e mudos.

'perdesse' -> pretérito imperfeito do subjuntivo correlaciona com futuro do pretérito (-RIA) 'passaria'
'acometeu' -> pretérito perfeito do indicativo

No item 'c':

		[yellow]Fora[reset] uma mulher em paz consigo mesma, apesar dos sofrimentos que a vida lhe [yellow]reserve[reset], ao desafiar seus limites.

'fora' está no pretérito mais-que-perfeito do subjuntivo, algo que exprime um passado anterior ao outro. o mais adequado seria o pretérito perfeito do indicativo 'foi'
'reserve' está no presente do subjuntivo ( que eu reserve) modo no presente que indica incerteza, hipotese atual, uma possibilidade, portanto sem correlação nenhuma.
O mais adequado seria o pretérito mais-que-perfeito do indicativo exprimindo um passado anterior ao outro dentro do contexto da frase.

		O correto seria:

			[yellow]Foi[reset] uma mulher em paz consigo mesma, apesar dos sofrimentos que a vida lhe [yellow]reservara[reset], ao desafiar seus limites.

Item 'D': 

		Quando me [yellow]confessou[reset] que se [yellow]mataria[reset], não me [yellow]surpreendi[reset] e disse que muita gente [yellow]poderia[reset] vir a tomar igual decisão.

	'confessou' -> pretérito perfeito do indicativo
O pretérito perfeito do indicativo é usado para expressar ações que foram concluídas no passado. 
Este tempo verbal indica que a ação começou e terminou em um momento passado, sem se prolongar até o presente.

	'mataria' -> futuro do pretérito - Algo no passado que se prolonga no futuro
	'surpreendi' -> presente do indicativo -> Traz uma ação atual com certeza.
	'poderia' -> futuro do pretérito -> Ação do passado que se prolonga no futuro

Item 'E':

		Segundo meu amigo, a dor maior [yellow]comparece[reset] quando nos [yellow]convencêssemos[reset] de que não [yellow]sejamos[reset] os únicos a sofrer.

		
		'comparece' -> presente do indicativo -> momento atual, com certeza.
		'convencêssemos' -> algo incerto no passado -> pretérito imperfeito do subjuntivo, o mais adequado seria um passado que ficou, pretérito perfeito do indicativo -> 
					eu convenci / tu convenceste / ele convenceu / [yellow]nós convencemos[reset] / vós convencestes / eles convenceram
		'sejamos' -> presente do subjuntivo -> que eu seja / que tu sejas / que ele seja / [yellow]que nós sejamos[reset] e o mais adequado seria:
		'somos' -> no presente do indicativo -> eu sou / tu és / ele é / nós somos / vós sois / eles são

		
			Segundo meu amigo, a dor maior [yellow]comparece[reset] quando nos [yellow]convencemos[reset] de que não [yellow]somos[reset] os únicos a sofrer.

'comparece' -> presente do indicativo
'convencemos -> pretérito perfeito do indicativo
'somos' -> presente do indicativo

'''		
    def exercicios_orto(self):
        return '''
		 Exercícios de ortografia - 

1. Ano: 2024 / Banca: Instituto Social Univida / Prova: Instituto Social Univida - Câmara de Piraí do Sul - Controlador Interno - 2024 

Relativamente à última reforma ortográfica da língua portuguesa, ocorrida no ano de 2009, observe as afirmações abaixo e assinale a alternativa correta.


I- Na expressão “União Europeia”, a segunda palavra perdeu o acento agudo, como também ocorre com os vocábulos assembleia e ideia.
II- Se no texto o autor utilizasse a expressão “comércio intra-bloco”, a uso do hífen seria obrigatório.
III- No primeiro parágrafo, o uso de aspas pode ser corretamente substituído pelo uso de travessões, por possuírem a função de dar destaque às palavras envolvidas.

A. Está correto apenas o item III.
B. Estão corretos os itens I e III.
C. Todos os itens estão corretos.
D. Todos os itens estão incorretos.
E. Está correto apenas o item I.

Item I  - CORRETO
Item II - ERRADO

[bg_red]1ª regra - Não se emprega o hífen nos vocábulos em que o prefixo ou falso prefixo termina em vogal e o segundo elemento começa por vogal diferente.[reset]

autoafirmação, autoajuda, autoaprendizagem, autoescola, autoestrada, autoinstrução, contraexemplo, contraindicação, contraordem, extraescolar, extraoficial, 
infraestrutura, intraocular, intrauterino, neoexpressionista, neoimperialista, semiaberto, 
semiárido, semiautomático, semiembriagado, semiobscuridade, supraocular, ultraelevado

[bg_blue]Exceção: Nos vocábulos com prefixo em que o segundo elemento começa por –h, o uso do hífen permanece:[reset] 

ante-hipófise, anti-herói, anti-higiênico, 
anti-hemorrágico, extra-humano, neo-helênico, semi-herbáceo, super-homem, supra-hepático etc.


[bg_red]2ª regra - Emprega-se o hífen nos vocábulos em que o prefixo ou falso prefixo termina em vogal e o segundo elemento começa por vogal igual.[reset]

[yellow]Anti-ibérico, anti-inflamatório, anti-inflacionário, anti-imperialista, arqui-inimigo, arqui-irmandade, micro-ondas, micro-ônibus, micro-orgânico[reset]

[bg_blue]Exceção: Nos prefixos átonos (não possuem acento) co-, pre-, re– e pro-, não se usa o hífen: coordenar, reescrever, propor, preestabelecer.[reset]


[bg_red]3ª regra - Não se emprega o hífen em certos compostos em que se perdeu, em certa medida, a noção de composição.[reset]

[yellow]mandachuva, paraquedas, paraquedista[reset]

[bg_blue]Exceção: O uso do hífen permanece nas palavras compostas que não contêm um elemento de ligação e constituem uma unidade sintagmática e semântica, [reset]
[bg_blue]mantendo acento próprio, bem como naquelas que designam espécies botânicas e zoológicas: [reset]
ano-luz, azul-escuro, médico-cirurgião, conta-gotas, guarda-chuva, 
segunda-feira, tenente-coronel, beija-flor, couve-flor, erva- doce, bem-te-vi, formiga-branca etc.

Item III - ERRADO. Os travessões são mais frequentemente utilizados para introduzir informações adicionais, fazer interrupções na frase ou destacar uma mudança de pensamento. 
Eles não têm a mesma função de destacar palavras ou expressões específicas como as aspas fazem. 


2. Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC / Prova: IGEDUC - Câmara de Vitória de Santo Antão - Analista Legislativo - 2024 

Quando um elemento termina com vogal e o segundo começa pelas letras “r” ou “s”, as consoantes são duplicadas, como ocorre nas seguintes palavras: 
“antissocial”, contrarreforma”, “macrorregião”, “microssegundo”. 
Portanto, não se utiliza hífen nesses casos.

[bg_green] CORRETO [reset]

3. Ano: 2024 / Banca: Projetos para Municípios - PROMUN / Prova: PROMUN - Prefeitura de Campos do Jordão - Professor Fundamental II - Área Português - 2024
Em relação às mudanças implementadas pelo Novo Acordo Ortográfico vigente, analise os itens abaixo e assinale a alternativa correta:

I - O alfabeto da língua portuguesa passa a ter 29 letras, com a incorporação das letras K, W e Y, que se empregam na grafia de nomes próprios, palavras deles derivadas e em abreviações.

II - Cai o acento circunflexo do hiato EE dos verbos LER, DAR, CRER, VER e derivados.

III – Cai o acento diferencial, apesar de permanecer nas palavras PÔDE e PÔR e, facultativamente, poder-se acentuar o substantivo FÔRMA.

Item I  - [red]ERRADO[reset] - O alfabeto com as letras K,W,Y passa a ter 26 letras.
Item II - [red]ERRADO[reset] - O Novo Acordo Ortográfico eliminou o acento circunflexo nos hiatos EE e OO, mas isso não se aplica aos verbos LER, DAR, CRER, VER e seus derivados. Esses verbos não possuem hiatos EE que seriam afetados por essa regra.
Item II - [green]CORRETO[reset] - O Novo Acordo Ortográfico eliminou o acento diferencial em várias palavras, mas manteve o acento diferencial em 'pôde' (pretérito perfeito do verbo poder) e 'pôr' (verbo) para diferenciá-los de 'pode' (presente do indicativo do verbo poder) e 'por' (preposição). 
[bg_green]No entanto, o acento diferencial em 'fôrma' (substantivo) é facultativo, o que está correto.[reset]

3. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC
Prova: FUNDATEC - Prefeitura de Cidreira - Professor de 5ª ao 8ª Série - Área Português - 2024
Sobre o sistema ortográfico oficial vigente, analise as seguintes assertivas:

I. O uso do acento circunflexo na terceira pessoa do plural do presente do indicativo dos verbos “ter” e “vir” (eles têm, elas vêm) é obrigatório.

II. Vocábulos oxítonos terminados em “e(s)”, “o(s)” – vogais tônicas e fechadas – devem receber o acento circunflexo na última sílaba, como em “bebê, bebês, avô, avôs” etc.

III. O uso do acento circunflexo na terceira pessoa do plural do presente do indicativo de verbos como “dar”, “crer”, “ler”, “ver”, “rever” é obrigatório.

Item I - CORRETO
Item II - CORRETO
Item III - [red]INCORRETO[reset] - O uso do acento circunflexo na terceira pessoa do plural do presente do indicativo de verbos como 'dar', 'crer', 'ler', 'ver', 'rever' não é obrigatório.

	eu dou / tu dás / ele dá / nós damos / vós dais / eles dão
	eu creio / tu crês / ele crê / nós cremos / vós credes / eles creem
'	eu leio / tu lês / ele lê / nós lemos / vós leis / eles leem
	eu vejo / tu vês / ele vê / nós vemos / vós veis / ele veem
	eu revejo / tu revês / ele revê / nós revêmos / vós reveis / eles reveem

	[green]De acordo com a nova regra ortográfica as vogais redobradas , em hiato, perderam o acento.[reset]

4.Ano: 2024 / Banca: Fundação de Apoio à Educação e Desenvolvimento Tecnológico de Minas Gerais - Fundacao CEFETMINAS
Prova: Fundação CEFETMINAS - Prefeitura de Timóteo - Cargos de Nível Fundamental - 2024
O Acordo Ortográfico da Língua Portuguesa foi assinado em Lisboa, em 16 de dezembro de 1990, por Portugal, Brasil, Angola, São Tomé e Príncipe, Cabo Verde, Guiné-Bissau, Moçambique e, posteriormente, por Timor Leste. 
No Brasil, o Acordo foi aprovado pelo Decreto Legislativo nº 54, de 18 de abril de 1995. 
Esse Acordo é meramente ortográfico; portanto, restringe-se à língua escrita, não afetando nenhum aspecto da língua falada.

Informe se é verdadeiro (V) ou falso (F) o que se afirma sobre o novo acordo ortográfico.

( ) As letras k, w e y, que haviam desaparecido da maioria dos dicionários da nossa língua, deverão continuar proibidas.

( ) Não se usa mais o trema (¨), sinal colocado sobre a letra u para indicar que ela deve ser pronunciada nos grupos gue, gui, que, qui.

( ) Não se usa mais o acento dos ditongos abertos éi e ói das palavras paroxítonas (palavras que têm acento tônico na penúltima sílaba). 
Como era: idéia, jóia. Como fica: ideia, joia.

( ) Não se usa mais o acento das palavras terminadas em êem e ôo(s). Como era: enjôo, lêem. Como fica: enjoo, leem.

De acordo com as afirmações, a sequência correta é:

A. F, F, V, V.
B. F, V, F, F.
C. F, V, V, V.
D. V, V, V, F.

Primeira afirmativa - Falsa - as letras k,w e y voltaram para o alfabeto em que compõem 26 letras.
Segunda afirmativa  - Verdadeiro - não se usa mais trema colocado sobre a letra 'u' bis grupos 'gue','gui','que','qui'
Terceiro afirmativa - Verdadeira - Em palavras na posição 'paroxítona' os ditongos abertos EI,OI,EU retira o acento.
Quarta afirmativa - Verdadeira - vogais redobradas retiram o acento

Alterntiva C - CORRETA

5. Ano: 2024 / Banca: Fundação de Estudos e Pesquisas Socioeconômicos - FEPESE / Prova: FEPESE - CINCATARINA - Técnico em Edificações - 2024 

Assinale a única alternativa em que o hífen foi empregado de acordo com a Nova Ortografia da Língua Portuguesa.

A. anti-racista
B. olho-de-lince
C. norma-padrão
D. co-proprietário
E. extra-salarial

[red]O termo 'anti-racista' está incorreto segundo a Nova Ortografia. [reset]
De acordo com as novas regras, o prefixo 'anti' deve ser unido diretamente ao radical, sem hífen, exceto quando o radical começa com 'h'. 
Portanto, a forma correta é 'antirracista'.

[red]O termo 'olho-de-lince' está incorreto. [reset]
Segundo a Nova Ortografia, o hífen é utilizado em compostos que designam espécies botânicas e zoológicas, mas 'olho de lince' não se enquadra nessa categoria. 
A forma correta é 'olho de lince', sem hífen.

O termo 'norma-padrão' está correto de acordo com a Nova Ortografia. O hífen é utilizado em compostos que formam uma unidade semântica.

[red]O termo 'co-proprietário' está incorreto. [reset]
Segundo a Nova Ortografia, o prefixo 'co' deve ser unido diretamente ao radical, sem hífen, independentemente da letra que inicia o radical. 
A forma correta é 'coproprietário'.

[red]O termo 'extra-salarial' está incorreto.[reset] De acordo com a Nova Ortografia, o prefixo 'extra' deve ser unido diretamente ao radical, sem hífen, 
exceto quando o radical começa com 'h' ou 'a'. A forma correta é 'extrasalarial'.

6.Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC / Prova: IGEDUC - Câmara de São José do Egito - Agente Administrativo - 2024

De acordo com o Novo Acordo Ortográfico, o uso do trema em palavras como "lingüiça" e "seqüestro" foi mantido para indicar a pronúncia correta.

[bg_red]ERRADO[reset]

7. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP / Prova: IDCAP - Prefeitura de Ibirataia - Técnico Ambiental - 2024

" Se os funcionários forem [yellow]microgerenciados[reset]"

De acordo com o Novo Acordo Ortográfico, assim como "microgerenciados", as palavras abaixo não devem levar hífen , EXCETO:

A. Extraescolar.
B. Coeducação.
C. Aeroespacial.
D. Microondas.

A palavra 'extraescolar' é formada pelo prefixo 'extra-' e não leva hífen, conforme as regras do Novo Acordo Ortográfico, 
que estipulam que o hífen não é utilizado quando o prefixo termina em vogal e o segundo elemento começa com uma consoante diferente de 'r' ou 's'.

A palavra 'coeducação' é formada pelo prefixo 'co-' e não leva hífen, de acordo com o Novo Acordo Ortográfico, 
que determina que o hífen não é usado quando o prefixo termina em vogal e o segundo elemento começa com uma vogal diferente.

A palavra 'aeroespacial' é formada pelo prefixo 'aero-' e não leva hífen, conforme as regras do Novo Acordo Ortográfico, 
que indicam que o hífen não é utilizado quando o prefixo termina em vogal e o segundo elemento começa com uma vogal diferente.

A palavra 'microondas' deveria ser escrita com hífen, 'micro-ondas', pois o Novo Acordo Ortográfico estabelece :
o hífen é utilizado quando o prefixo termina em vogal e o segundo elemento começa com a mesma vogal.

8.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / 
Prova: FGV - STN - Auditor Federal de Finanças e Controle Econômico-Financeira (Contratações) - Conhecimentos Gerais - Pós-Edital - 2024 - 1º Simulado

A frase inteiramente redigida segundo o sistema ortográfico vigente é:

A. Após passar pelo [yellow]lava a jato[reset], o carro parecia novo, mas, ao toque, a pintura tinha a textura suave como um creme de [yellow]maizena.[reset]
B. As teorias sobre a origem dos [yellow]hieróglifos[reset] egípcios levantam a possibilidade de uma visita [yellow]extra-terrestre[reset] nos tempos antigos.
C. A pesquisa revelou que condições [yellow]socioeconômicas[reset] precárias estão associadas a maiores taxas de [yellow]malformação[reset] em bebês.
D. O creme [yellow]antirruga[reset] vem numa embalagem inusitada que lembra um [yellow]mini-revólver[reset], facilitando o transporte no dia a dia.
E. Tentar fazer uma lei viger sem consulta pública é como fazer uma brincadeira de [yellow]mal gosto[reset] em um momento sério, gerando desconforto e resistência.

[red]Erro No item 'A'[reset]: [blue]'lava-jato' é uma palavra composta ( dois substantivos ) portanto utiliza-se hífen.[reset]
 'lava a jato' indica o modo como a lavagem é feita. [bg_red]Além disso a grafia correta para 'maizena' é 'maisena' o composto e não a marca.[reset]

[red] Erro No item 'B'[reset] : 'hieróglifos' ou 'hieroglifos' estão corretas. 
Em 'extra-terreste' emprega-se hífen somente se for iniciado por 'h' ou por ela mesma 'a'. 
[green]O correto é: 'extraterrestre'[reset]

[green]No item 'C'[reset]: malformação ou máformação estão corretas. 'sócio' é adjetivo de social <- substantivo, grafa-se sem acento e sem hífen. CORRETO

No item 'D': 'antirruga' está correto. Inicial 'r' ou 's' duplica a letra e não usa hífen. Agora 'mini-revólver' está ERRADO. O correto seria: 'minirrevolver'.
Emprega-se hífen com 'mini' somente antes de 'i' no segundo elemento, ou a letra 'h', obrigatório o hífen em letras iniciais 'h'.

[red]No item 'E': ERRADO. a grafia correta na frase seria 'mau gosto'. 'mau' é o oposto de 'bom'.  'mal' é o oposto de 'bem'.[reset]

9. Ano: 2024 / Banca: EDUCA Assessoria Educacional - EDUCA / Prova: EDUCA - Câmara de Piancó - Assistente Legislativo - 2024

“O secretário-geral da ONU, António Guterres, voltou, esta quinta-feira, a alertar que o planeta está "à beira do abismo"...”, 
analise as assertivas abaixo e coloque (V) para VERDADEIRO e (F) para FALSO.

( )“secretário-geral” pode ser também grafado sem hífen, segundo o Novo Acordo Ortográfico.

( )Na escrita de “secretário-geral” e “quinta-feira”, há uso de hífen indevido, segundo o Novo Acordo Ortográfico.

( )“quinta-feira”, por ser dia da semana, continua sendo escrito com hífen mesmo depois do Novo Acordo Ortográfico.


A sequência CORRETA é:

A. V, F, F.
B. F, V, V.
C. V, F, V.
D. F, F, V.
E. F, V, F.


1. **“secretário-geral” pode ser também grafado sem hífen, segundo o Novo Acordo Ortográfico.**

**Falso (F)**. O termo “secretário-geral” deve **manter o hífen** de acordo com o Novo Acordo Ortográfico, pois se trata de um substantivo composto por justaposição
que contém um elemento que especifica uma função ou cargo da mais alta patente.


2. **Na escrita de “secretário-geral” e “quinta-feira”, há uso de hífen indevido, segundo o Novo Acordo Ortográfico.**

**Falso (F)**. Ambos os termos **mantêm o hífen** conforme as regras do Novo Acordo Ortográfico. 
No caso de “quinta-feira”, os dias da semana continuam a ser grafados com hífen, e “secretário-geral” segue sendo um substantivo composto que requer hífen.


3. **“quinta-feira”, por ser dia da semana, continua sendo escrito com hífen mesmo depois do Novo Acordo Ortográfico.**

**Verdadeiro (V)**. Todos os dias da semana continuam sendo grafados com hífen após o Novo Acordo Ortográfico.


Por que em "secretário-geral" o hífen é obrigatório?

Como já mencionamos, o adjetivo "geral" nesse contexto indica a mais alta posição dentro de uma hierarquia. O hífen reforça essa ideia de superioridade e singularidade do cargo.


E em "secretário-adjunto"?

"Adjunto" como adjetivo: O termo "adjunto" significa "aquele que está junto", "auxiliar". Ele funciona como um adjetivo que qualifica o substantivo "secretário".

Hífen opcional: Diferentemente de "geral", "adjunto" não indica necessariamente a mais alta posição, mas sim uma função auxiliar. 
Por isso, o uso do hífen não é tão obrigatório.

Escrevem-se com hífen os cargos:

* Formados pelo adjetivo geral: diretor-geral, relator-geral, ouvidor-geral, procurador-geral, secretário-geral;

*Postos e gradações da diplomacia: primeiro-secretário, segundo-secretário;

*Postos da hierarquia militar: tenente-coronel, capitão-tenente.

10. Ano: 2024 / Banca: FUNDEP Gestão de Concursos - FUNDEP / Prova: FUNDEP - Câmara de Pará de Minas - Analista de Controle Interno - 2024 

Considere as afirmativas a seguir, a respeito de termos e expressões da escrita em português, e assinale a incorreta.

A.As palavras [yellow]reboliço[reset] e [yellow]rebuliço[reset] significam, respectivamente, “confusão ou desordem” e “aquele que rebola muito”, na norma-padrão da Língua Portuguesa.
B.A dúvida comum entre a grafia de [yellow]cabeçalho[reset] ou [yellow]cabeçário[reset] não procede, porque a segunda palavra não existe na grafia da norma-padrão da Língua Portuguesa.
C.As expressões [yellow]por hora[reset] e [yellow]por ora[reset] têm diferentes referências temporais: a primeira remete a um intervalo de tempo, e a segunda significa “neste momento”.
D.Verbos podem terminar com as formas [yellow]-isar[reset] ou [yellow]-izar[reset], mas entre as formas [yellow]paralisar[reset] ou [yellow]paralizar[reset], a grafia correta do infinitivo desse verbo é a primeira.

O item 'A': está INCORRETO. Estas duas palavras existem na língua portuguesa e estão corretas. 
São palavras com significados diferentes. A palavra rebuliço se refere a uma grande confusão, desordem, agitação, desentendimento. 
Pode significar também um conjunto de pessoas agitadas. 
A palavra reboliço se refere a alguma coisa que rebola, tendo a forma de um rebolo, ou seja, de uma pedra redonda
O item 'B': realmente 'cabeçário' não existe.
[bg_blue]O item 'C': 'por hora' refere-se a um intervalo de tempo / 'por ora' significa 'neste momento'[reset]
O item 'D': 'paralizar' está incorreto. O correto é 'paralisar'.

11. Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP
Prova: IDCAP - Prefeitura de Ibirataia - Analista de Sistemas - 2024

Em "No primeiro dia, senti um hiperfoco e bem-estar incríveis." De acordo com o novo acordo ortográfico, analise as afirmativas relacionadas aos vocábulos destacados no trecho.

I.  "Bem-estar" Segundo o atual acordo ortográfico, o hífen é utilizado em palavras compostas com os advérbios bem e mal quando a segunda palavra começa por vogal ou h, por isso a palavra foi grafada corretamente.
II. "Hiperfoco" está grafado corretamente, uma vez que a palavra "hiper" exige hífen quando precede palavras iniciadas pelas consoantes H e R.
III."Hiperfoco" Segundo a atual acordo ortográfico, o hífen é utilizado em prefixos como "hiper" e "sub" quando a segunda palavra começa com F e H, sendo correto a grafia hiper-foco.

A alternativa que apresenta a(s) afirmativa(s) correta(s) é:

A. Apenas II.
B. Apenas I, II.
C. Apenas I, III.
D. Todas estão incorretas.

Somente a afirmativa I a correta.
I.  "Bem-estar" Segundo o atual acordo ortográfico: 

[yellow]o hífen é utilizado em palavras compostas com os advérbios 'bem' e 'mal' quando a segunda palavra começa por vogal ou h, por isso a palavra foi grafada corretamente.[reset]


12. Ano: 2024 / Banca: Funatec / Prova: Funatec - Câmara de Itapecuru Mirim - Auxiliar Jurídico - 2024 

Assinale a alternativa correta do ponto de vista ortográfico:

A. Agora você pode fruir suas férias.
B. As crianças estavam ansiosas para se divertirem no horário da recriação.
C. Gostei do seu novo namorado: é um sujeito descente.
D. A loja fica na intercessão da Rua 40 com a Avenida 10.

A) Agora você pode fruir suas férias.

A palavra "fruir" está corretamente grafada e significa "aproveitar" ou "desfrutar". A frase está correta do ponto de vista ortográfico.


B) As crianças estavam ansiosas para se divertirem no horário da recriação.

A palavra "recriação" está incorreta. A forma correta é "recreação". A frase está incorreta do ponto de vista ortográfico.


C) Gostei do seu novo namorado: é um sujeito descente.

A palavra "descente" está incorreta. A forma correta é "decente". A frase está incorreta do ponto de vista ortográfico.


D) A loja fica na intercessão da Rua 40 com a Avenida 10.

A palavra "intercessão" está incorreta. A forma correta é "interseção". A frase está incorreta do ponto de vista ortográfico.

O substantivo intercessão é sinônimo de intervenção e o substantivo interseção é sinônimo de cruzamento.

13. Ano: 2024 // Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Câmara de São José do Egito - Auxiliar de Serviços Gerais - 2024

De acordo com o Acordo Ortográfico, o uso do hífen é obrigatório em palavras compostas que indicam espécies botânicas e zoológicas, como em "bem-te-vi" e "erva-doce".

C.Certo

14. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP
Prova: Avança SP - Prefeitura de Lorena - Analista - Área: Procuradoria - 2024 
Analise as sentenças a seguir e assinale aquela em que não ocorre desvio ortográfico.

A. Comprei cravos da índia para enfeitar os docinhos da festa.
B. As pessoas que conheci neste ano são verdadeiras bençãos para mim.
C. Os professores não têm tempo para esses garotos mal-educados.
D. As máquinas continham engrenagens espiróides.
E. Poucas são as pessoas que entendem à respeito das cripto-moedas.

No item 'A' - 'cravos-da-india' usa-se hífen para espécies botânicas
No item 'B' - 'bençãos' usa-se acento 'bênçãos'
No item 'C' -  CORRETA
No item 'D' - 'espiroides' <- Para mim, correto. Ditongo aberto, retira o acento em posição paroxítona.
No item 'E' -  O correto é 'a respeito', sem acento grave, pois não há crase antes de palavras masculinas. e 'criptomoedas' sem hífen

15. Ano: 2024 / Banca: SELECON Instituto Nacional de Seleções e Concursos - SELECON
Prova: SELECON - CEFET RJ - Pedagogo - 2024 

A palavra LATINO-AMERICANO é um adjetivo composto, formado por duas partes ligadas por hífen. De acordo com a ortografia oficial, também é ligada por hífen a palavra:

A. afro-descendente
B. micro-bactéria
C. afro-brasileiro
D. micro-análise

Com as formas adjetivas afro, anglo, euro, franco, indo, luso, sino e assemelhadas, mais de uma nacionalidade, etnia ou região de origem: 
afro-brasileiro, use hífen quando o segundo elemento é outro adjetivo pátrio, e a palavra, dessa forma, envolve anglo-saxão, ibero-americano, 
euro-asiático, luso-brasileiro, afro-brasileiro.

Nos demais casos (quando só há uma nacionalidade ou etnia), use sem hífen: afrodescendente, eurocêntrico, lusofonia.

Adjetivos gentílicos compostos são grafados sempre com hífen: porto-alegrense, mato-grossense, norte-rio-grandense.

Portanto 'afro-brasileiro' - mais de uma nacionalidade, etnia ou região de origem usa-se hífen. Alternativa 'C'.

Resumo

[red]Hífen:[reset] quando tem duas nacionalidades ou etnias diferentes (afro-brasileiro) ou em adjetivos gentílicos compostos (mato-grossense).

[red]Sem hífen:[reset] quando é uma única nacionalidade ou etnia (afrodescendente).

16. Ano: 2024 / Banca: Instituto Legatus - Legatus // Prova: Legatus - Prefeitura de Luís Domingues - Professor - Área: Língua Portuguesa - 2024

Quanto às regras de acentuação gráfica, “herói”, conforme o último Acordo Ortográfico (1990, em vigor até os dias atuais), está corretamente acentuado; 
das palavras abaixo NÃO obedecem à regra de acentuação:

A. Heroína
B. Heróico
C. Dói
D. Anéis
E. Heroísmo


"Herói" é oxítona terminada em ditongo aberto "ói"; mantem acento

"Heroína", apesar de paroxítona terminada em "a", é acentuada pela regra dos hiatos ("i" tônico); he-ro-í-na <- hiato

"Heroico" é paroxítona (e quando há os ditongos "ei" ou "oi" (como tônicas) em posição paroxítonas, não acentuamos);

"Heroísmo", acentua-se pela regra dos hiatos (assim com "heroína"). he-r[yellow]o-í[reset]s-mo <- hiato

"dói" - monossílabo tônico - mas são acentuadas por serem ditongos abertos em posição oxítona.

"anéis" - oxítona de ditongo aberto - recebe acento

17.Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - Prefeitura de Miracema - Cuidador Social - 2024

Falecido em 2011, Moacyr Scliar não chegou a viver a obrigatoriedade do último acordo ortográfico da língua portuguesa, a qual passou a vigorar em 2016. 
O termo “mal-traçadas” (3º§), por exemplo, grafado com hífen na reprodução do texto anterior:

A. Obedece ao acordo ortográfico, pois o prefixo “mal” sempre exige hífen.
B. Obedece ao acordo ortográfico, pois o prefixo “mal” exige hífen quando sucedido por consoante.
C. Vai de encontro ao acordo ortográfico, pois o prefixo “mal” exige hífen apenas quando sucedido por vogais.
D. Vai de encontro ao acordo ortográfico, pois o prefixo “mal” não exige hífen quando sucedido pela consoante “t”.

Atenção! O prefixo 'mal' exige hífen em vogais, h e na letra 'l'.

O prefixo mal exige hífen antes de vogal, h e l: mal-acabado, mal-agradecido, mal-humorado, mal-intencionado, mal-lavado, mal-estar, mal-entendido. 
Nos demais casos, escreve-se sem hífen, com aglutinação: malcriado, malfeito, malsucedido.

18. Ano: 2024 / Banca: Creative Group / Prova: Creative Group - Prefeitura Buritizal - Psicólogo - 2024 

Assinale a alternativa que apresenta a palavra que teve sua grafia alterada a partir do Novo Acordo Ortográfico.

A. apóiam
B. constituída
C. latino-americana
D. perdê-lo

'a-pói-am' : paroxítona com ditongo aberto retira-se o acento.
'cons-ti-tu-í-da' : hiato, mantem o acento.
'latino-americana' : Com as formas adjetivas afro, anglo, euro, franco, indo, luso, sino e assemelhadas, mais de uma nacionalidade, etnia ou região de origem: 
afro-brasileiro, use hífen quando o segundo elemento é outro adjetivo pátrio, e a palavra, dessa forma, envolve anglo-saxão, ibero-americano, 
euro-asiático, luso-brasileiro, afro-brasileiro.

Nos demais casos (quando só há uma nacionalidade ou etnia), use sem hífen: afrodescendente, eurocêntrico, lusofonia.

Adjetivos gentílicos compostos são grafados sempre com hífen: porto-alegrense, mato-grossense, norte-rio-grandense.

19.Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC / Prova: IGEDUC - Prefeitura de Tuparetama - Auxiliar Administrativo - 2024

De acordo com o novo Acordo Ortográfico, são acentuadas as palavras oxítonas com os ditongos abertos grafados -éi, éu ou ói, 
podendo estes dois últimos ser seguidos ou não de -s, como em: 
anéis, batéis, fiéis, papéis; céu(s), chapéu(s), ilhéu(s), véu(s); corrói (de corroer), herói(s), remói (de remoer) e sóis.

20. Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Prefeitura de Garanhuns - Auditor Fiscal da Receita Municipal - 2024

Considerando o novo Acordo ortográfico da Língua Portuguesa, emprega-se o apóstrofo para assinalar, no interior de certos compostos, 
a supressão do E da preposição DE, em combinação com substantivos, como ocorre em: borda-d’água, cobra-d’água, copo-d’água, estrela-d’alva, pau-d’água, pau-d’arco.

[bg_green] CORRETO [reset]

21. Ano: 2024 / Banca: Instituto Consulplan 
Prova: Instituto Consulplan - TJ MA - Técnico Judiciário - Apoio Técnico Administrativo Pós-Edital - 2024 - 2º Simulado

Dentre os vocábulos destacados, o único que segue as normas ortográficas vigentes na língua portuguesa é:

A. “Tensões insolúveis e forças opostas agitam o [yellow]micro-cosmo[reset] da nossa vida subjetiva [...]” (1º §)
B. “Pior: o véu do [yellow]autoengano[reset] com frequência oculta da visão que temos de nós mesmos traços e falhas [...]” (1º §)
C. “Se discursos [yellow]bem intencionados[reset], saltos milenaristas ou rupturas violentas com o passado pudessem produzir o milagre duvidoso [...]” (2º §)
D. “[...] acordos [yellow]inter-subjetivos[reset] que se mostraram perfeitamente compatíveis com o substrato rígido [...]” (4º §)

[red]'micro-cosmo'[reset] -> [blue]emprega-se hífen com o prefixo 'micro' apenas quando o segundo elemento é iniciado por 'h' ou 'o'.[reset] [bg_red]Portanto, a grafia correta é 'microcosmo'.[reset]
[red]'autoengano'[reset]  -> [blue]emprega-se hífen com o prefixo 'auto' apenas quando o segundo elemento é iniciado por 'h' ou 'o'. [reset] [green]Portanto, a grafia está CORRETA.[reset]
[red]'bem intencionados' [reset]-> [blue]emprega-se o hífen com o prefixo 'bem' apenas quando o segundo elemento possuir autonomia na língua. [bg_red]Portanto, grafia correta é 'bem-intencionado'.[reset]
'intenciado' é um verbo, portanto emprega-se hífen.
[red]'inter-subjetivos'[reset]  -> [blue]Emprega-se hífen com o prefixo 'inter' apenas quando o segundo elemento for iniciado por 'h' ou 'r'. A grafia correta é 'intersubjetivos'[reset]

22. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP
Prova: Avança SP - FSPSS - Técnico em Prótese Dentária - 2024 

Analise as palavras a seguir e assinale a alternativa em que o emprego do hífen é dispensado, de acordo com o acordo ortográfico vigente.

A. gota-d"água.
B. aquém-mar.
C. co-habitação.
D. mesa-redonda.
E. corre-corre.

'co-habitação' é dispensado o hífen. As outras afirmativas são palavras que possuem autonomina própria e se juntam formando um substantivo composto com uso do hífen obrigatório.

23. Ano: 2024 / Banca: Associação dos Municípios do Extremo Oeste de Santa Catarina - AMEOSC
Prova: AMEOSC - Prefeitura - Auxiliar Administrativo - 2024

Em relação às regras de ortografia e às de acentuação analise as afirmativas:

I.'bem-estar' é hifenizada, assim como afro-descendente.

II.'micro-organismos' é hifenizada, pois emprega-se o hífen nas formações com prefixo quando o 1º elemento termina por vogal igual à que inicia o 2º elemento.

III.'vírus' é uma paroxítona assim como 'caracteres'.

IV.'saúde' é acentuada pela mesma regra de 'faísca'.

Estão corretas:

A. Apenas II, III e IV.
B. Apenas II e IV.
C. Apenas I, II e III.
D. Apenas I, III e IV.

Afirmativa I - ERRADA - a palavra 'bem-estar' é hifenizada. 
Afirmativa II - CORRETO
Afirmativa III - ví - rus / ca - rac - te - res -> paroxítonas
Afirmativa IV - Ambas as palavras são acentuadas pela mesma regra do hiato com a segunda vogal 'i' ou 'u' tônica.

Portanto, afirmativa 'A' gabarito da questão.

24. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TJ AP - Técnico Judiciário - Área Apoio Especializado - Especialidade: Informática - 2024 
A opção em que as duas palavras nela apresentadas recebem acento gráfico corretamente, é:

A. dócil / maquinária;
B. autóctone / rúbrica;
C. hífen / táctil;
D. barbária / têxtil;
E. éter / cíclope.

[red]a) Dócil - Maquinária (errado) Maquinaria (correto)[reset]

Regra de acentuação das paroxítonas:

Acentuam-se as paroxítonas terminadas em ditongo crescente ou decrescente (seguido ou não de s) e -ãs, tritongo e 
qualquer outra terminação (L, que é o caso de dócil, n, um, r, ns, x, i, is, us, ps), 
[bg_red]exceto as terminadas em -a(s) (que é o caso de Maquinaria), -e(s), -o(s), -em(-ens).[reset]

[red]b) Autóctone é uma proparoxítona, acentuam-se todas. [red]Rúbrica (errado)[reset] [green]Rubrica (correto)[reset]

[blue] Rubrica é uma paroxítona termina em A, por isso NÃO é acentuada.[reset]

[red]c) Hífen - Táctil[reset]

[blue]Hífen é uma paroxítona terminada em N, por isso é acentuada.[reset]
[blue]Táctil é uma paroxítona terminada em L, por isso é acentuada.[reset]

[red]d) Barbária (errado)[reset] [blue]Barbaria (correto) - Têxtil[reset]

Barbaria é uma paroxítona terminada em A, por esse motivo não recebe acento.
Têxtil é uma paroxítona terminada em L, por esse motivo recebe acento.

[red]e) Éter - Cíclope (errado) Ciclope (correto)[reset]

[yellow]Éter é uma paroxítona terminada em 'r', por esse motivo é acentuada.[reset]
[yellow]Ciclope é uma paroxítona terminada em E, por esse motivo NÃO é acentua[reset]

[bg_red] Atenção! Não acentua palavras paroxítonas terminadas em -a(s),-e(s),-o(s),-em(-ens)[reset]


25. Ano: 2024
Banca: Instituto Access - Instituto de Acesso à Educação, Capacitação Profissional e Desenvolvimento Humano
Prova: Instituto Access - Instituto de Acesso à Educação, Capacitação Profissional e Desenvolvimento Humano - CREMEB - Técnico de Atividades de Suporte I - 2024

Na frase: “O trabalho dos médicos acarretou em novas pesquisas para a área da saúde” ocorre um erro de:

A. Ortografia.
B. Acentuação.
C. Concordância verbal.
D. Concordância nominal.
E. Regência verbal.

Regência verbal trata da relação entre o verbo e seus complementos, incluindo a preposição correta. 
O verbo 'acarretar' é transitivo direto e não exige preposição. A forma correta seria 'acarretou novas pesquisas'. 
Portanto, este item está de acordo com o gabarito da banca.


26.Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Câmara de Araripina - Agente Administrativo - 2024
 
Segundo o Novo Acordo Ortográfico, as palavras compostas que têm os prefixos tônicos acentuados (pós-, pré-, pró-) 
devem ser grafadas com hífen quando o segundo elemento é entendido separadamente, como em "pré-história" e "pós-graduação".

Certo 

Quando o prefixo é tônico acentuado (pós, pré, pró) e o segundo elemento é entendido separadamente, usa-se hífen: pós-graduação, pré-datado, pré-escolar, pré-história, pré-natal, pró-africano, pré-sal.

Já as correspondentes formas átonas (pos, pre, pro), co e re não levam hífen, unem-se ao segundo elemento mesmo se este for iniciado por o ou e: pospor, prever, preestabelecer, predeterminado, promover, 
coorganizar, coordenar, cooperação, coirmão, coorganizador, reedição, reeleição, reempossar.


27. Ano: 2024 / Banca: MS Concursos / Prova: MS Concursos - SAAE Manhuaçu - Ajudante Administrativo - 2024
De acordo com o emprego do hífen, assinale a alternativa que apresenta a série em que todas as palavras estão grafadas dentro da norma padrão da Língua Portuguesa.

A. Mal-feito, pós-escolar, próalfabetização, circum-polar.
B. Água-marinha, tenente-coronel, rodapé, bioquímico.
C. Decreto-lei, panamericano, prénupcial, mal-criado.
D. Aero-moça, termo-elétrico, antiibérico, autobservação.

Afirmativa 'A':

[bg_red]'mal-feito' está errado. Usa-se hífen após a palavra 'mal' somente quando a palavra começar com vogal, um 'h' ou 'l'.[reset]
O uso do hífen com os prefixos tônicos acentuados "pós", "pré" e "pró" é feito quando o segundo elemento é entendido separadamente. 
As formas átonas (pos, pre, pro) não usam hífen e ligam-se ao segundo elemento sem hífen. Por exemplo: Pospor, Prever, Promover.
'pós-escolar' portanto está correto. 
'próalfabetização' está errado. O correto é: 'pró-alfabetização'.
'circum-polar' não leva hífen quando o segundo elemento começa por vogal, 'h', 'm' ou 'n'.

Afirmativa 'B':

'água-marinha' e 'tenente-coronel' são palavras compostas que usam hífen obrigatoriamente.
'rodapé' união por justaposição (não perdem elementos) roda + pé
'bioquimico' união prefixal. O hífen não é necessário quando o prefixo "bio-" se junta a um elemento que começa com consoante, exceto quando a consoante é "h".

Afirmativa 'C':

'decreto-lei' palavras compostas, uso do hífen.
'panamericano' tem hífen porque o prefixo "pan-" pede hífen quando a palavra seguinte começa por vogal, 'h', 'm' ou 'n.'
'prénupcial' está errado. Tem hífen. O uso do hífen com os prefixos tônicos acentuados "pós", "pré" e "pró" é feito quando o segundo elemento é entendido separadamente. 
As formas átonas (pos, pre, pro) não usam hífen e ligam-se ao segundo elemento sem hífen. Por exemplo: Pospor, Prever, Promover. Por derivação prefixal.
'mal-criado' -> está incorreto. Usa-se hífen quando a segunda palavra começar com vogal, um 'h' ou 'l'. na palavra 'mal'
Por exemplo:
Mal-acabado, Mal-agradecido, Mal-humorado, Mal-intencionado, Mal-lavado, Mal-estar, Mal-entendido. 
Nos demais casos, escreve-se sem hífen, com aglutinação: Malcriado, Malfeito, Malsucedido. 

Afirmativa 'D':

'aero-moça' -> ERRADO. O correto é: 'aeromoça'.
'termo-elétrico -> ERRADO. O correto é: 'termoelétrico'.
'antiibérico -> ERRADO. O correto é: anti-ibérico.
'autobservação' -> ERRADO. O correto é: auto-observação.

28. Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Prefeitura de Tuparetama - Professor de Educação Infantil - 2024

De acordo com o novo Acordo Ortográfico, usa-se hífen em compostos formados com o advérbio NÃO: organização não-governamental, pacto de não-proliferação de armas nucleares, não-indígena.

ERRADO.

Antes do novo acordo ortográfico, recomendava a norma usar o hífen sempre que o "não" viesse antes de substantivo:

- Não-agressão / não-fumante / não-combatente / não-intervenção.

• E associado a um adjetivo ou particípio (terminações -ado e -ido); e, quando o "não" formasse uma palavra de sentido completo:


- Não-alinhado, não-beligerante, não-combatente, não-conformista, não-engajado, não-esperado, não-essencial, não-existente, não-ferroso, não-fumante, não-iluminado, não-intervencionista, não-participante, não-positivo, não-saturado, não-verbal, não-viciado.

• Pois bem, de acordo com o novo vocabulário ortográfico, não se emprega mais o hífen nos casos citados acima.

29.Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Prefeitura de Tuparetama - Auxiliar Administrativo - 2024
 
Considerando a redação dada pelo novo Acordo Ortográfico, o acento é opcional na palavra FÔRMA, com o sentido de modelo, molde. Assim, pode-se escrever fôrma ou forma.

C.Certo

30. Ano: 2024 / Banca: Instituto Social Univida
Prova: Instituto Social Univida - Prefeitura Nossa Senhora das Graças - Psicólogo - 2024 

Assinale em qual das alternativas abaixo a lacuna deve ser obrigatoriamente preenchida com a primeira das opções apresentadas entre parênteses.

A. A manipulação religiosa leva a torturas e massacres de forma completamente ________ com a desculpa de respeitar a fé, sendo que tal atitude é a principal prova de desrespeito. (des-humana / desumana)

B. Devem-se respeitar uns aos outros, _________ de que não haja tantos desentendimentos e guerras por conta dessa questão. (a fim / afim)

C. Para atenuar a questão de intolerância, é necessário mudar a visão das pessoas _________ crenças desconhecidas por elas, suprimindo assim o preconceito. (sob / sobre)

D. É preciso que exista a educação sobre religião, seja ela em _________ escolar ou doméstico. (hambiente / ambiente)


Alternativa 'A' - a primeira palavra não existe a grafia portugues. 'desumana' existe
Alternativa 'B' - 'a fim' separado com a ideia de alguma explicação, justificativa.  'Devem-se respeitar uns aos outros, [yellow]a fim[reset] de que não haja...'
			'afim' junto refere-se a algo semelhante, afinidade.
Alternativa 'C' - 'sobre' indica uma relação de assunto ao tema. ex: '...é necessário mudar a visão das pessoas [yellow]sobre[reset] crenças desconhecidas...'
			'sobre' é preposição onde liga ideias uma a outra.
Alternativa 'D' -  'hambiente' não existe na grafia portuguesa.


31 . Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Prefeitura de Garanhuns - Auditor Fiscal da Receita Municipal - 2024

Segundo o novo Acordo ortográfico da Língua Portuguesa, o H inicial deve ser suprimido quando, por via de composição, 
passa ao interior da palavra e o elemento em que figura se aglutina ao precedente, como em: 
BIEBDOMADÁRIO, DESARMONIA, DESUMANO, EXAURIR, INÁBIL, LOBISOMEM, REABILITAR, REAVER.

C.Certo

32. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC
Prova: FUNDATEC - Prefeitura de Cidreira - Técnico em Enfermagem - 2024 

Considerando as regras do Acordo Ortográfico vigente, analise as seguintes assertivas sobre palavras retiradas do texto:

I. “Pan-Americana” (l. 01) está escrita incorretamente, pois está com hífen.

II. O vocábulo “custo-efetivas” (l. 16) está escrito corretamente, pois está grafado com hífen e com as duas palavras unidas.

III. A palavra “bem-estar" (l. 25) deveria estar grafada sem hífen e com espaço.

'pan-amarericana' está ERRADO. não leva hífen se o segundo elemento começar com vogal, 'm' ou 'n'

A palavra "bem-estar" é escrita com hífen, pois o prefixo "bem" exige hífen antes de palavras que possuem vida autônoma ou quando a pronúncia o exige. 
O hífen é utilizado quando:
A palavra que segue tem vida autônoma na língua 
A pronúncia exige o hífen 
O segundo elemento começa por vogal ou h 
Os compostos formam com o elemento que se lhes segue, compostos contíguos na cadeia da fala e não podem se substituir mutuamente 
Exemplos de palavras escritas com hífen:
Bem-acabado, Bem-amado, Bem-casado, Bem-criado, Bem-humorado, Bem-nascido, Bem-vindo, Bem-aventurado. 
Por outro lado, existem compostos em que "bem" aglutina-se com o segundo elemento, como: Benfeito, Benfazer, Benfeitor, Benquerer, Benquisto


33. Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Câmara de São José do Egito - Vigilante - 2024

De acordo com o Novo Acordo Ortográfico, os adjetivos gentílicos derivados de topônimos compostos, como "porto-alegrense" e "belo-horizontino",
 mantêm o hífen para preservar a clareza da formação das palavras.

C.Certo

34. Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Prefeitura de Tuparetama - Professor de Educação Infantil - 2024

Segundo o novo Acordo Ortográfico, é facultativo assinalar com acento agudo as formas verbais de pretérito perfeito do indicativo, do tipo AMÁMOS, LOUVÁMOS, 
para as distinguir das correspondentes formas do presente do indicativo AMAMOS e LOUVAMOS.

C.Certo

implementado nos países de língua portuguesa a partir de 2009, realmente é facultativo o uso do acento agudo nas formas verbais de pretérito perfeito do indicativo 
para distingui-las das formas do presente do indicativo.

35. Ano: 2024 / Banca: Instituto de Apoio à Gestão e Educação - IGEDUC
Prova: IGEDUC - Prefeitura de Tuparetama - Psicólogo - 2024

De acordo com o Novo Acordo Ortográfico, é necessário usar acento gráfico em PÁRA, flexão do verbo parar, para haver distinção da preposição PARA.

C.ERRADO

O uso do acento diferencial em 'PÁRA' (verbo parar) foi abolido. Portanto, tanto a forma verbal quanto a preposição são escritas como 'PARA'. 
A questão está correta ao afirmar que não é mais necessário usar o acento gráfico para distinguir entre as duas palavras


36. Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - Correios - Conhecimentos Básicos Comuns para todos os Cargos - Pós-Edital - 2024 - 1º Simulado 

No texto, aparecem palavras que seguem diferentes regras de acentuação gráfica conforme o Novo Acordo Ortográfico. Considerando essas regras, assinale a alternativa incorreta sobre a acentuação das palavras do texto.

A. A palavra "mágica" recebe acento por ser proparoxítona, assim como "pântano" e "cálculo". CORRETO
B. "Difícil" e "tórax" são acentuadas pela mesma regra, pois ambas são paroxítonas terminadas em "l" e "x", respectivamente. CORRETO
C. A acentuação de "pôde" e "pôr" segue a mesma regra, pois ambas são formas verbais que recebem acento para distinguir seu significado. CORRETO
D. A palavra "só" e a palavra "têm" são acentuadas pela mesma razão, sendo ambos monossílabos tônicos. ERRADO

A palavra 'só' é acentuada por ser um monossílabo tônico, enquanto 'têm' é acentuada por ser uma forma verbal do verbo 'ter' na terceira pessoa do plural do presente do indicativo.
"Só" é um monossílabo tônico, porém o “têm” é acentuado por causa da regra do acento diferencial, ou seja, para diferenciar singular de plural.

37. Ano: 2024 / Banca: Funatec
Prova: Funatec - Prefeitura de Abadiânia - Técnico de Enfermagem - 2024 
Destaque a alternativa que não contém um caso de uso de acento diferencial, nos termos do Novo Acordo Ortográfico:

A. pôde (verbo no passado) e pode (verbo no presente)
B. pôr (verbo) e por (preposição)
C. pára (verbo) e para (preposição)
D. de (preposição) e dê (verbo)

A. pôde (verbo no passado) e pode (verbo no presente) - Uso de acento diferencial correto. 
B. pôr (verbo) e por (preposição) - Uso de acento diferencial correto. 
C. pára (verbo) e para (preposição) - A forma verbal "pára" perdeu o acento diferencial com o Novo Acordo Ortográfico, sendo escrita como "para". 
D. de (preposição) e dê (verbo) - Uso de acento diferencial correto.

Portanto, a alternativa que não contém um caso de uso de acento diferencial, de acordo com o Novo Acordo Ortográfico, é a alternativa C.
38. Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - Petrobras Biocombustível - Ênfase 16: Suprimento de Bens e Serviços - Especialidade: Administração - Pós-Edital - 2024 - 1º Simulado

Segundo as regras oficiais de ortografia, a expressão “além-mar” (terceiro período do segundo parágrafo) poderia ser grafada alternativamente como “além mar”.

Errado.

De acordo com as regras ortográficas vigentes na Língua Portuguesa, é obrigatório o emprego de hífen nos compostos com o elemento além.

39. Ano: 2024 / Banca: Fundação CESGRANRIO - CESGRANRIO
Prova: CESGRANRIO - Concurso Nacional Unificado - CNU - Bloco 8 - Intermediário – Português - Pós-Edital - 2024 - 3º Simulado

A frase em que as palavras destacadas respeitam as regras ortográficas da norma padrão é:

A. Após [yellow]deferir[reset] o pedido, o juiz notou a falta de [yellow]censo[reset] na argumentação apresentada.
B. A [yellow]dispensa[reset] estava organizada, o que facilitou apreender[reset] os alimentos proibidos.
C. O advogado conseguiu [yellow]aferir[reset] benefícios significativos do [yellow]mandado[reset] judicial.
D. A [yellow]câmera[reset] municipal exigiu uma [yellow]calção[reset] significativa para a construção da escola.
E. Durante a densa [yellow]cerração[reset], as tropas [yellow]infligiram[reset] duras derrotas ao inimigo.

[red](A) Errada.[reset] São os seguintes os significados dos parônimos:

[red]Deferir:[reset] Conceder, aceitar um pedido ou proposta.

[red]Diferir:[reset] Ser diferente, discordar.

[red]Censo:[reset] Levantamento estatístico de uma população, incluindo dados demográficos, econômicos, entre outros.

[red]Senso:[reset] Capacidade de julgar corretamente, discernimento ou bom senso.

Veja-se a redação correta:

[yellow]Após deferir o pedido, o juiz notou a falta de senso na argumentação apresentada.[reset]


[red](B) Errada[reset]. São os seguintes os significados dos parônimos:

[red]Despensa:[reset] Cômodo ou armário em que se armazenam alimentos e mantimentos.

[red]Dispensa: Ato de liberar alguém de uma obrigação ou serviço; ato de demitir.

[red]Aprender[reset]: Adquirir conhecimento, habilidade ou informação por meio de estudo ou experiência.

[red]Apreender:[reset] Capturar, pegar ou assimilar mentalmente algo.

Veja-se a redação correta:

[yellow]A despensa estava organizada, o que facilitou apreender os alimentos proibidos.[reset]


[red](C) Errada.[reset] São os seguintes os significados dos parônimos:

[red]Aferir:[reset] Medir, avaliar ou verificar a exatidão de algo.

[red]Auferir:[reset] Obter, ganhar, especialmente lucros ou vantagens.

[red]Mandado:[reset] Ordem escrita emitida por uma autoridade competente, como um juiz.

[red]Mandato: [reset]Período de tempo em que um cargo ou função é exercido; autorização para agir em nome de outrem.

Veja-se a redação correta:

[yellow]O advogado conseguiu auferir benefícios significativos do mandado judicial.[reset]

[red](D) Errada. [reset]São os seguintes os significados dos parônimos:

[red]Câmara:[reset] Órgão legislativo ou espaço fechado.

[red]Câmera:[reset] Dispositivo utilizado para capturar imagens ou vídeos.

[red]Calção:[reset] Peça de vestuário, geralmente curta e usada para a prática de esportes.

[red]Caução: [reset]Garantia em dinheiro ou bens, dada para assegurar o cumprimento de uma obrigação.

Veja-se a redação correta:

[yellow]A câmara municipal exigiu uma caução significativa para a construção da escola.[reset]


[red](E) Certa.[reset] São os seguintes os significados dos parônimos:

[red]Cerração:[reset] Neblina densa, especialmente em regiões costeiras ou fluviais.

[red]Serração:[reset] Ação ou efeito de serrar, cortar madeira ou outros materiais.

[red]Infligir:[reset] Aplicar um castigo ou pena.

[red]Infringir:[reset] Desrespeitar uma regra, lei ou ordem.

40.Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - UNICAMP - Profissional da Arte, Cultura e Comunicação - Área: Revisor - 2024
 
De acordo com o Novo Acordo Ortográfico, são acentuadas as proparoxítonas aparentes, devidamente exemplificadas com os seguintes termos do texto:

A. revolucionário, dúvida.
B. últimas, astúcias.
C. Colégio, História.
D. tecnocrática, necessário.
E. responsável e privilégio.

'colégio'  -> co-lé-gio ou proparoxítona aparente : co - lé - gi - o
'história' -> his - tó - ria ou proparoxítona aparente : his - tó - ri -a

Nas palavras paroxítonas terminadas em ditongo oral,
 acentua-se a vogal da sílaba tônica: ágeis, imundície, lírio, túneis, tênue, jóquei, nódoa, cerimônia, história.

 'revolucionário' é paroxítona terminada em ditongo, acentua-se e pode ser eventual proparoxítona.
 ' dúvida' é proparoxítona

 Na b: 'últimas': é proparoxítona / 'astúcias' : paroxítona terminada em ditongo, acentua-se

 A alterntiva C a correta.

 Na alternativa 'd' : tec - no - crá - ti - ca -> proparoxítona / ne - ces - sá - rio : eventual proparoxítona ( aparente )

 Na alternativa 'e': res - pon - sá - vel - paroxítona terminanda em 'L' - acentua-se / pri - vi - lé - gio -> paroxítona terminada em ditongo - acentua-se sendo eventual proparoxítona.

41. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - BACEN - Analista de Economia e Finanças Pós-Edital - 2024 - 4º Simulado

No texto, as expressões “não-naturalidade” e “recém-chegado” seguem as normas ortográficas atualmente vigentes na língua portuguesa.

ERRAOD. As expressões compostas pelo elemento “não” não levam hífen. Já o prefixo “recém” sempre demanda o emprego de hífen.

42. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - Prefeitura de Cachoeiro de Itapemirim - Arquiteto - 2024 

Tanto a forma “assobiava”, empregada no último parágrafo do texto, quanto a forma assoviava são admitidas pela ortografia oficial em vigor, tendo ambas o mesmo significado.

C.Certo

42.Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - BACEN - Analista de Economia e Finanças Pós-Edital - 2024 - 3º Simulado 
 
Segundo as regras oficiais de grafia, a expressão “pré-moderna” (terceiro período) poderia ser grafada como pré moderna.

E.Errado / Sempre exigirá hífen em prefixos tônicos.

43. Ano: 2023 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - SEC - Professor da Educação Básica - Área Língua Portuguesa - 2023

A infração gravíssima aumenta o risco de acidentes em até 400%, atrapalha o tráfego e ______ (tem - têm) crescido anualmente.

'tem' A primeira lacuna deve ser preenchida com "tem", forma verbal no singular, pois concorda com o sujeito simples "A infração gravíssima", 
cujo único núcleo, "infração", é um substantivo singular. 
É um acento diferencial que distingue a forma plural (têm) da forma singular (tem) do verbo "ter" conjugado na terceira pessoa do presente do indicativo.

é ver outra pessoa ao telefone enquanto ______ (dirige - dirije).
A segunda lacuna deve ser preenchida com "dirige", forma verbal do verbo "dirigir", também escrito com "g". 
A letra "j" vai ser usada apenas com as vogais "a", "o" ou "u", como em "dirija" e "dirijo".

Se incomoda ver o outro ao celular, ______ (porque - por que) grande parte da população não deixa de cometer essa infração gravíssima? 

A terceira lacuna deve ser preenchida com "por que", aparecendo em uma frase interrogativa direta, ou seja, uma pergunta terminada com ponto de interrogação.

44. Ano: 2023 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - EBSERH - Enfermeiro Pós-Edital - 2023 - 1º Simulado

Assinale a alternativa que, respeitando o Novo Acordo Ortográfico, mantém a correção verificada quanto ao emprego de hífen conforme o termo destacado em 
“Eu sei por que motivo o meio-termo não é seguido: o homem inteligente ultrapassa-o, o imbecil fica aquém”.

A. Recém-divulgado.
B. Semi-aberto.
C. Não-autorizado.
D. bem-querer.
E. Mal-feito.


Letra a.

Assunto abordado: Ortografia oficial

a) Certa. O prefixo “recém” exige hífen em qualquer situação: recém-divulgado.

b) Errada. O prefixo “semi” só exige hífen quando a palavra seguinte começar com “h” ou com vogal “i”. Nos demais caso, escreve-se junto, em aglutinação: semiaberto.

c) Errada. O uso de hífen é dispensado na formação de palavras com “não”: não autorizado.

d) Errada. O prefixo “bem” exige hífen sempre, porém existem aglutinações que dispensam o uso, quando o “m” final é suplantado pelo “n”, como na exceção da alternativa: benquerer.

e) Errada. O prefixo “mal” exige hífen antes das vogais, de “h” e de “l”. Nos demais casos, grafa-se sem hífen, com aglutinação: malfeito.

45. Ano: 2022 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC / Prova: IBFC - MGS - Administrador - 2022 

Com o Novo Acordo Ortográfico, algumas palavras sofreram alteração quanto ao emprego do hífen. O vocábulo “Super-herói”, que se encontra no texto, manteve esse sinal. Dentre os vocábulos abaixo, assinale o único que está grafado ERRONEAMENTE:

A. interrelação.
B. micro-ondas.
C. anti-higiênico.
D. autoestrada.

Vejamos as demais palavras:

A) INCORRETA (GABARITO). Quando o prefixo termina por consoante (inter),

usa-se o hífen se o segundo elemento começar pela mesma consoante (relação). O certo é: inter-relação.

46. Ano: 2022 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TRT 4 - Técnico Judiciário - Área: Administrativa - 2022 - 1º Simulado 
Assinale a alternativa que NÃO apresenta problemas de grafia.

A. O excludente de ilicitude poderia ter sido implantado a pelo menos trinta anos.
B. Se o excludente de ilicitude for implantado agora, os resultados aparecerão daqui há trinta anos.
C. Ainda hoje, há vários grupos que resistem à implantação do excludente de ilicitude.
D. A violência policial, problema que persiste a muito tempo, agrava a convivência nos centros urbanos.
E. Há posição do Código Penal frente ao excludente de ilicitude mudou.

A. O excludente de ilicitude poderia ter sido implantado a pelo menos trinta anos.
[](A) Errada. O excludente de ilicitude poderia ter sido implantado há (tempo passado) pelo menos trinta anos.

B. Se o excludente de ilicitude for implantado agora, os resultados aparecerão daqui há trinta anos.
(B) Errada. Se o excludente de ilicitude for implantado agora, os resultados aparecerão daqui a (tempo futuro) trinta anos.

C. Ainda hoje, há vários grupos que resistem à implantação do excludente de ilicitude.
Certa. Ainda hoje, há (= existem) vários grupos que resistem (exige a preposição “a”) à implantação (exige o artigo “a”) do excludente de ilicitude.

D. A violência policial, problema que persiste a muito tempo, agrava a convivência nos centros urbanos.
Errada. A violência policial, problema que persiste há muito tempo (tempo passado), agrava a convivência nos centros urbanos.

E. Há posição do Código Penal frente ao excludente de ilicitude mudou.
(E) Errada. A posição do Código Penal frente ao excludente de ilicitude mudou.

48. Ano: 2022 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - PC BA - Investigador Pós Edital - 2022 - 1º Simulado 

Das expressões seguintes, apenas uma foi grafada incorretamente segundo o Novo Acordo Ortográfico da Língua Portuguesa. Assinale-a:

A. “chicles” (l. 3)
B. “sairmos” (l. 10)
C. “histórias” (l. 17)
D.  cor de rosa (l. 18-19)
E. “puxa-puxa” (l. 44)

'cor de rosa' -> ERRADO. A forma correta é “cor-de-rosa”. Trata-se de uma exceção à regra do emprego de hífen nos compostos de três elementos com preposição.

49.Ano: 2022 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - ALE RN - Analista Legislativo Pré Edital - 2022 - 2º Simulado 
 
Assinale a alternativa correta em relação ao emprego do acento gráfico nos vocábulos do texto.

A. A palavra “vitória” (l. 1) é acentuada em razão de ser paroxítona terminada em a.
B. O vocábulo “pelo” (l. 28) (contração entre a preposição por e o artigo o) não é acentuado para que seja diferenciado da forma “pêlo” (substantivo).
C. Os acentos gráficos empregados em “contínuo” (l. 7) e “experiências” (l. 11) são explicados pela mesma regra.
D. Em “paixão” (l. 13) e “noção” (l. 18), o acento gráfico indica nasalizada da vogal a.
E. Os vocábulos “prevê” (l. 13) e “até” (l. 22) seguem regras distintas de acentuação gráfica.

Letra c.

(A) Errado. A palavra “vitória” é acentuada em razão de ser paroxítona terminada em ditongo oral.

(B) Errado. Antes do Novo Acordo Ortográfico, havia acento diferencial em “pêlo” (substantivo), para que fosse distinguido de “pelo” (contração de preposição e artigo). Com a entrada em vigor do Novo Acordo Ortográfico, o acento foi extinto. Agora, os dois vocábulos são diferenciados pelo contexto de seu uso.

(C) Certo. De fato, “contínuo” e “experiências” são acentuados por serem paroxítonas terminadas em ditongo oral, seguido ou não de s.

(D) Errado. Em “paixão” e “noção”, o sinal acima da vogal a, denominado til, é indicador de pronúncia nasalizada dessa vogal, não constituindo um acento gráfico.

(E) Errado. Os vocábulos “prevê” e “até” são acentuados por serem oxítonas terminadas em e.


50. Ano: 2023 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - SEC - Professor Área: Educação Profissional - 2023

Ao final daquela noite, Eric Clapton chamou os garçons ______ e lhes deu ______ quantia como ______.

Assinale a alternativa que preencha correta e respectivamente as lacunas.

A. as pressas / vultuosa / gorjeta.
B. às pressas / vultosa / gorjeta.
C. às pressas / vultósa / gôrjeta.
D. às pressas / vultosa / gorgeta.
E. as pressas / vultuosa / gorgeta.

A primeira lacuna deve ser preenchida com "às pressas". Trata-se de uma locução adverbial de modo inicia pela preposição "a", a qual se junta ao artigo definido "as" que precede o substantivo feminino plural "pressas" e ocasiona a crase: a + as pressas = às pressas.

A segunda lacuna deve ser preenchida com "vultosa", que significa "de grande importância". É diferente de "vultuoso", que significa "congestionado" ou "inchado".

A terceira lacuna deve ser preenchida com "gorjeta", palavra escrita com "g" e "j", assim como seu termo de origem, o substantivo "gorja".

A opção correta, portanto, é a letra B.

51. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TSE - Técnico Judiciário - Área: Administrativa Pré-Edital - 2023 - 9º Simulado 
Analise a oração a seguir:

“Combinei com o funcionário da empresa que continuaria ajudando as pessoas.”

Na frase, há um problema textual, que é:

A. erro de ortografia.
B. ausência de uma vírgula antes do termo “que”.
C. ambiguidade.
D. falha na concordância.
E. erro de regência.

Quando uma palavra tem mais do que um sentido impreciso, temos AMBIGUIDADE.
Exemplo: Ninguém conseguia se aproximar do porco do tio, tão mal ele cheirava.
Nessa frase, a palavra porco pode ter o sentido de animal (o porco que pertence ao tio) ou pode ter o sentido de pessoa suja (comparação do tio a um porco).
se não dá pra identificar o sujeito da ação é ambíguo

Nessa frase, fica a dúvida se quem continuaria ajudando seria “eu”, ou a “empresa” ou o “funcionário”.

Uma forma correta de escrita para acabar com a ambiguidade seria:

Combinei com o funcionário da empresa que eu continuaria ajudando as pessoas.

52. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPE SC - Promotor de Justiça Substituto - Tarde - 2023

No último período do primeiro parágrafo, a substituição de “antidireito” por anti-direito faria o texto ficar em desacordo com a ortografia oficial vigente no Brasil.

C.Certo

Usa-se o hífen depois do prefixo anti- quando o segundo elemento iniciar por 'h' ou 'i'.

53. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SME - Professor Ensino Fundamental e Médio - Área Educação Física - 2023 
As questões notacionais da Língua Portuguesa se referem, entre outras coisas, a palavras e expressões que frequentemente provocam dúvidas em relação à sua ortografia.

A esse respeito, assinale a opção ortograficamente correta.

A. A cerca de vinte carros enguiçados na avenida.
B. Os livros foram vendidos há cerca de dez semanas.
C. Os clientes esperaram o médico a cerca de duas horas.
D. O padre falou por horas há cerca do pecado original.
E. Os policiais estavam acerca de cem metros do assaltante.

A cerca de vinte carros enguiçados na avenida. ' a cerca de' indica distância aproximada.
 Exemplo: Ele mora a cerca de 10 km daqui. Portanto, utilizada de maneira errada.

'Há cerca de': Com o verbo 'HAVER' Indica tempo decorrido, no passado. Também com aproximadamente. Exemplo: Ele chegou há cerca de duas horas.
	Os livros foram vendidos há cerca de dez semanas.

'Acerca de': equivale a respeito de algo. Portanto a 'C' está incorreta.
O correto seria: O padre falou por horas acerca do pecado original.

Na alternativa 'E' está errado o 'acerca de' junto. A frase exprime distância aproximada, portanto é separado ' a cerca de'.

54. Ano: 2021 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE. - DPF - Papiloscopista - 5º Simulado Pós Edital - 2021 

Em razão do Novo Acordo Ortográfico, a oração “Do meu olho que vê”, última estrofe, deve ser reescrita sem o acento tônico no verbo “ver”, 
a fim de manter correta a gramática do texto conforme as novas regras.

ERRADO - O acento deve ser mantido para diferenciar o singular (3ª pessoa) do plural (3ª pessoa – veem).

54. Ano: 2022 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - SF - Analista Legislativo - Área Apoio Técnico ao Processo Legislativo - Especialidade: Processo Legislativo - 2022 - 11º Simulado

Preservando-se a correção gramatical, a frase “Quero ensinar às crianças.” (l.24) pode corretamente ser reescrita da seguinte forma: Quero ensinar as crianças.

C.Certo

O verbo “ensinar” na acepção de “instruir”, é transitivo direto e indireto: ensinar alguma coisa a alguém (primeira possibilidade) ou 
ensinar alguém a fazer alguma coisa (segunda possibilidade). 
Por isso, a supressão do sinal indicativo de crase é gramaticalmente correta, uma vez que, nessa situação, 
a segunda possibilidade de regência do verbo é que será construída..

55. Ano: 2022 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - INSS - Técnico do Seguro Social (Pós-Edital) - 2022 - 19º Simulado

O vocábulo “pré-história” (l.13) é grafado, segundo o Novo Acordo Ortográfico da Língua Portuguesa, da seguinte forma: pré história.


Errado - prefixo tônico sempre uso de hífen.

56. Ano: 2022 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - SES DF - Enfermeiro Pós Edital - 2022 - 1º Simulado
Quanto às normas ortográficas, assinale a alternativa que apresenta escrita incorreta do termo destacado.

A. O comportamento dele era anti-higiênico.
B. Marquei as aulas na auto-escola.
C. O vice-representante da turma está ausente.
D. Luíza foi super-racista agora.
E. Conquistei um garoto hiperativo.

a. Certo. Com prefixos, usa-se o hífen diante de palavra iniciada por “h”.

b. Errado. Não se usa hífen quando o prefixo termina em vogal diferente da vogal com que se inicia o segundo elemento, ou seja, a grafia correta é “autoescola”.

c. Certo. Com o prefixo “vice”, usa-se hífen.

d. Certo. Usa-se hífen quando o prefixo terminar com consoante e o segundo elemento iniciar pela mesma consoante.

e. Certo. Quando o prefixo termina por consoante, não se usa hífen se o segundo elemento começar por vogal.


 '''
    def exercicios_conjuncoes(self):
        return '''Exercícios de conjunções:

1.Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CREF 19 - Assistente Administrativo - 2024

-Não sei se faço natação ou se entro na academia
- Escolha fazer o que te dá mais prazer
- [yellow]Então [reset]só vou comer e domir


No terceiro quadrinho, “então” apresenta valor conclusivo.

C.Certo

A palavra destacada faz parte do conjunto das conjunções coordenativas conclusivas;

logo; pois (posposto ao verbo); portanto; assim; então; por isso; por conseguinte; por consequência; consequentemente;
de modo que; desse modo; dessarte; destarte;

2. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - IPREM Mogi das Cruzes - Auxiliar de Apoio Administrativo - 2024

Ando devagar porque já tive pressa
E levo esse sorriso

O vocábulo “porque” (linha 1) tem valor explicativo.

C.Certo

'porque' => Conjunções e locuções conjuntivas coordenativas explicativas: que, porque, porquanto, pois(anteposto ao verbo)

3. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - Conselho Regional de Biologia da 9ª Região (CRBio 9ª Região) - Agente Fiscal - 2024 

A lista vermelha também destaca as espécies marinhas

A palavra “também” (linha 25) classifica‑se morfologicamente como conjunção.

ERRADO 
Os advérbios de inclusão são os advérbios usados em frases que expressam a ação de incluir algo ou alguém em determinado lugar ou situação. 
Exemplos desse tipo de advérbio são: também, até, mesmo, inclusive, ademais, ainda etc.

4. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - COREN PR - Analista de Tecnologia da Informação - 2024 

No trecho “não só do enfermo, mas também de seus familiares em período de luto” (linhas 26 e 27), a expressão “não só... mas também” expressa uma adição.

CERTO

É uma conjunção coordenativa aditiva que tem a função de adicionar informações.
É importante lembrar que conjunções coordenativas aditivas, como 'não só... mas também', 'e', 'nem', 'bem como',
Sempre têm a função de adicionar informações ou elementos em uma frase.

5. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Prefeitura de Aparecida - Professor de Anos Iniciais do Ensino Fundamental - 2024 

Observe as relações de sentido estabelecidas pelas conjunções nas passagens destacadas:

Mudam os modismos, mudam os costumes, [yellow]mas certas coisas nunca mudam.[reset]

A ideia de que o que está à nossa frente é um buraco negro de incerteza pode ser tão intimidante [yellow]que é mais fácil acreditar no oposto…[reset]

Item: A) 
A primeira conjunção 'mas' estabelece uma relação de oposição, e não de restrição. 
A segunda conjunção 'que' estabelece uma relação de consequência, e não de explicação. 

Item: B) 
A primeira conjunção 'mas' estabelece uma relação de oposição, contrastando a mudança dos modismos e costumes com a imutabilidade de certas características humanas. 
A segunda conjunção 'que' estabelece uma relação de consequência, indicando que a ideia de incerteza é tão intimidante que leva a acreditar no oposto. 
Portanto, o item está de acordo com o gabarito da banca.

Item: C) 
A primeira conjunção 'mas' não estabelece uma relação de explicação, mas sim de oposição. 
A segunda conjunção 'que' não estabelece uma relação de comparação, mas sim de consequência. 

Item: D) 

A primeira conjunção 'mas' não estabelece uma relação de conclusão, mas sim de oposição. 
A segunda conjunção 'que' não estabelece uma relação de causa, mas sim de consequência. 

Item: E) 

A primeira conjunção 'mas' não estabelece uma relação de tempo, mas sim de oposição. 
A segunda conjunção 'que' não estabelece uma relação de modo, mas sim de consequência. 



6. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Instituto de Previdência de São Bernardo do Campo (SBCPREV) - Agente Previdenciário - 2024

Leia as passagens:

[yellow]À medida que[reset] avança a utilização da tecnologia da inteligência artificial (IA)... (1⁠º parágrafo)
[yellow]No entanto[reset], ao mesmo tempo em que novas tecnologias extinguiram profissões... (2⁠º parágrafo)
[yellow]Embora[reset] experimente fortes recuos nos índices de desemprego... (6⁠º parágrafo)


As expressões em destaque introduzem, correta e respectivamente, os sentidos de:

A. proporcionalidade; oposição; concessão.
B. conformidade; conclusão; explicação.
C. conclusão; explicação; conclusão.
D. conformidade; oposição; causa.
E. proporcionalidade; conclusão; oposição.

Na primeira frase temos uma conjunção subordinada proporcional: indica simultaneidade de ocorrência de fatos.

à medida que, à fim de que, de sorte que, de modo que, porque, à proporção que, quanto mais(menos, melhor, pior, maior, menor)...mais(menos, melhor,pior, maior), 
ao passo que

Na segunda frase temos uma conjunção coordenativas adversativas:
Indicação de uma ideia que contraria a anterior, uma oposição, uma divergência, um contraste, uma quebra de expectativa:
mas, porém, contudo, entretanto, no entanto, todavia, não obstante, senão(= mas sim), só que, ainda assim, e

Na terceira frase temos uma conjunção subordinada concessiva: 
concedem ou admitem uma condição contrária ao fato expresso pela oração principal, uma oposição fraca:
embora, conquanto, malgrado, ainda que, mesmo que, posto que, apesar de que, se bem que, não obstante, por mais que, por pior que, 
a despeito de,malgrado, em que pese

7. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - IBICT - Tecnologista - Área: Biblioteca - 2024 

[yellow]Se[reset] você espetar seu dedo, pode simplesmente ignorar a dor. [yellow]Mas[reset] tente ignorar uma coceira voraz. Impossível!


No segundo parágrafo, as conjunções “se” e “mas” são da mesma categoria, ou seja, são subordinativas.

E.Errado - Somente a conjunção 'se' é das subordinadas. A conjunção 'mas' é das coordenativas adversativas.
A conjunção 'se' é das subordinadas condicionais.

Mneumônico para ajudar:
Conjunções coordenativas -> ECAAA : Explicativas, conclusivas, aditivas, adversativas e alternativas
Conjunções subordinativas -> 6Cs + FTP: Causal, concessivas, consecutivas, conformidade, condicional, comparativa, final (finalidade), temporal e proporcional. 
(Entra também as integrantes - Que e Se)


8. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRO RR - Agente de contratação - 2024 

O vocábulo que inicia os segmentos “como qualquer outra infecção” (linhas 39 e 40) e “Como se pode observar” (linha 43) indica circunstância de conformidade em ambas as ocorrências.

Na primeira ocorrência, 'como qualquer outra infecção', o termo 'como' está sendo utilizado para estabelecer uma comparação, 
indicando que a doença periodontal pode dificultar o controle do diabetes da mesma forma que qualquer outra infecção.

Portanto, a conjunção 'como' no primeiro vocábulo é uma conjunção subordinada comparativa.

No segundo termo: 'Como se pode observar', o termo 'como' está introduzindo uma oração de valor conformativo,
indicando uma inferência conforme a partir do que foi apresentado anteriormente no texto.
Sendo assim, a conjunção 'como' no segundo termo é uma conjunção subordinativa conformativa:
Exemplos: conforme, segundo, consoante, como

9. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / 
Prova: Quadrix - Conselho Regional de Biologia da 9ª Região (CRBio 9ª Região) - Fiscal Biólogo - 2024

Imagens fortes mostram o animal em meio a uma mancha de sangue [yellow]enquanto[reset] tenta se soltar da gaiola.

A conjunção “enquanto” (linha 14) indica anterioridade.
 ERRADO - A conjunção 'enquanto' indica ideia temporal, é uma conjunção subordinativa temporal

10. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - CAGEPA - Advogado - 2024 

"No entanto, o país mantém com seus rios uma relação ambígua:..."

No início do segundo parágrafo do texto CG1A7-I, a expressão “No entanto” introduz uma ideia de

A.adição.
B.concessão.
C.oposição.
D.conclusão.
E.explicação

A expressão "no entanto", dá o mesmo sentido que "mas, porém, contudo, entretanto, todavia, não obstante, sendo assim, expressa adversidade, 
apesar disso, ao passo que, em todo caso, ou seja, oposição a um fato citado anteriormente.

'No entanto' é uma conjunção coordenativa adversativa, que introduz uma ideia de oposição﻿.

11. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRP 15 - Psicólogo - 2024

O desenho e a pintura eram usados como base para um possível diagnóstico, não havendo, entretanto, 
registros de seu uso como recursos em um processo terapêutico.

A conjunção “entretanto” (linha 25) expressa, no texto, uma oposição entre as ideias apresentadas.

C. Certo

A conjunção "entretanto" expressa uma oposição entre o uso do desenho e da pintura para diagnóstico e a falta de registros de seu uso como recursos terapêuticos.
'entretanto' uma conjunção coordenativa adversativa, que introduz uma ideia de oposição﻿.

12. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE / Prova: CESPE/CEBRASPE - CAU - Jornalista - 2024 

" [yellow]Não[reset] se trata apenas do levantamento de dados brutos, [yellow]mas[reset] da proficiente manipulação..."
" Dito de outra forma, [yellow]não[reset] basta somente a confecção de mapas digitais coloridos ilustrando, por exemplo, 
a exclusão social de uma determinada cidade por quantis, [yellow]mas[reset] é fundamental que,"
" Ou ainda, [yellow]não[reset] é suficiente apenas mapear a ocorrência de crimes em um sistema georreferenciado, [yellow]mas[reset] sim estudá-los de forma dinâmica"

Em todas as suas ocorrências nos 3º, 4º e 5º períodos do primeiro parágrafo, a conjunção “mas” introduz no texto uma ideia de contraste

Nas 3 situaçes, a conjunção foi utilizada com valor aditivo (e não de contraste / adversativo).


Justifica-se não apenas pela substituição da conjunção por 'mas também', 'bem como', 'além disso', etc, 
como também pela presença dos advérbios de exclusão ("não apenas", "não somente").


"[yellow]Não (apenas) [reset]se trata apenas do levantamento de dados brutos, [yellow]mas (também)[reset] da proficiente manipulação..."


"...[yellow]não (apenas) [reset]basta somente a confecção de mapas... [yellow]mas (também)[reset] é fundamental que,..."


"...[yellow]não (somente) [reset]é suficiente apenas mapear a ocorrência ..., [yellow]mas (também)[reset]sim estudá-los..."


Errado - Portanto a questão está errada em afirmar que a conjunção 'mas' introduz no texto uma ideia de contraste.
Mas sim uma conjunção coordenativa aditiva , realçando uma ideia de adição 'mas (também)'.

13. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - ALE TO - Analista Legislativo - Área Revisão - 2024
Assinale a frase em que não está presente uma expressão ou termo indicativo de causa.

A. O paisagista pinta tranquilo porque a paisagem defronte não se pode aproximar do quadro para ver se está parecida.
B. A História é como um estilingue. Quanto mais fundo você puxa, mais longe você alcança.
C. Algumas pessoas são o centro das atenções numa festa por terem ótimo senso se humor.
D. Em função de algumas declarações falsas, a repórter foi obrigada a desmenti-las.
E. Em vista do aumento de impostos, houve grande reclamação dos empresários.

O conceito central envolve a compreensão de elementos linguísticos que estabelecem uma relação de causalidade entre as ideias apresentadas nas frases. 
Na língua portuguesa, essa relação pode ser explicitada por meio de conjunções, locuções conjuntivas e outros termos que funcionam como indicativos de causa, 
tais como 'porque', 'em função de', 'em vista de', entre outros. 

Item: A) 
A frase apresenta a conjunção 'porque', que introduz uma oração subordinada adverbial causal, explicando o motivo pelo qual o paisagista pinta tranquilo. 
Portanto, o item não está de acordo com o gabarito da banca, pois contém um termo indicativo de causa.

Item: B) 
Esta frase utiliza uma comparação metafórica para estabelecer uma relação entre a profundidade do estudo da História e o alcance do conhecimento. 
Não há, explicitamente, um termo ou expressão que indique causa, estando de acordo com o gabarito da banca.

Item: C) 
A expressão 'por terem ótimo senso de humor' funciona como um indicativo de causa, explicando o motivo pelo qual algumas pessoas são o centro das atenções numa festa. 
Assim, o item não está de acordo com o gabarito da banca, pois contém um termo indicativo de causa.

Item: D) 
A expressão 'Em função de algumas declarações falsas' estabelece claramente uma relação de causa, indicando o motivo pelo qual a repórter foi obrigada a desmenti-las. 
Portanto, o item não está de acordo com o gabarito da banca, pois contém um termo indicativo de causa.

Item: E) 

A expressão 'Em vista do aumento de impostos' introduz uma causa para a grande reclamação dos empresários, estabelecendo uma relação de causalidade entre o aumento de impostos e as reclamações. 
Logo, o item não está de acordo com o gabarito da banca, pois contém um termo indicativo de causa.

14. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - PM SP - Soldado PM de 2ª Classe - 2024

Nas frases abaixo está presente a conjunção E. Assinale a frase em que o significado dessa conjunção está indicado corretamente.

A. Em muitos terrenos de cidades pequenas há simultaneamente plantas frutíferas e plantas ornamentais / oposição.
B. Algo só é impossível até que alguém duvide e acabe provando o contrário / consequência.
C. Ambiente limpo não é o que mais se limpa, e sim o que menos se suja / adição.
D. Há gente que fala e fala, mas nada diz / causa.
E. Os policiais chegam a suas casas e tiram o uniforme / conclusão.

Item A
A conjunção 'e' está sendo usada para adicionar informações, indicando a presença de ambos os tipos de plantas. 
Portanto, o significado correto seria adição, e não oposição.

Item B
A conjunção 'e' está sendo usada para indicar uma consequência, pois a ação de duvidar leva à ação de provar o contrário. 
Este item está de acordo com o gabarito da banca.

Item C

A conjunção 'e' está sendo usada para fazer uma oposição entre duas ideias. Portanto, o significado correto seria oposição, e não adição.

Item D
A conjunção 'e' está sendo usada para adicionar a repetição da ação de falar. Portanto, o significado correto seria adição, e não causa. 

Item E
A conjunção 'e' está sendo usada para adicionar duas ações sequenciais. Portanto, o significado correto seria adição, e não conclusão.

15. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de Macaé - Fonoaudiólogo - 2024 

Assinale a opção que apresenta o valor semântico do conector corretamente indicado.

A. [yellow]Afinal[reset], trata-se de uma bola profissional, uma número cinco, cheia de carimbos ilustres: / conclusão.
B. [yellow]No entanto[reset], aí está ela, correndo para cima e para baixo, na maior farra do mundo / justificativa.
C. ...disputada, maltratada até, [yellow]pois[reset], de quando em quando, acertam-lhe um bico, ela sai zarolha, vendo estrelas, coitadinha / explicação.
D. Racha é assim mesmo: tem bico, [yellow]mas[reset] tem também sem-pulo de craque como aquele do Tona, que empatou a pelada / adição.
E. O espantalho-gente pega a bola, viva, ainda, tira do bolso um canivete e dá-lhe a primeira espetada / tempo.

item A
O conector 'Afinal' é utilizado para introduzir uma explicação ou justificativa, e não uma conclusão.
Portanto, a função semântica correta seria de explicação, não de conclusão.

Item B
O conector 'No entanto' é utilizado para introduzir uma ideia de oposição ou contraste, e não de justificativa

Item C
O conector 'pois' é utilizado para introduzir uma explicação, justificando por que a bola é maltratada. 

Item D
O conector 'mas' é utilizado para introduzir uma ideia de contraste, e não de adição. No texto, ele contrapõe a ideia de que o racha tem bico com a ideia de que também tem jogadas bonitas. 

Item E
O trecho não apresenta um conector de tempo. A ação descrita é uma sequência narrativa, mas não há um conector específico que indique tempo


16. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Prefeitura de Osasco - Agente Comunitária de Saúde - 2024

Observe os períodos:

• ... morava em um estúdio e trabalhava na linha de frente da pandemia em Boston, [yellow]“mas[reset] nunca parecia bagunçado”. (1o parágrafo)

• “As diferentes propriedades das plantas, [yellow]como[reset] a aparência, o cheiro e a sensação ao toque...” (2o parágrafo)

• [yellow]Como[reset] passamos bom tempo em casa, talvez esteja na hora de incluirmos algumas plantas... (4o parágrafo)


Os termos em destaque estabelecem relações entre as orações, mantendo, correta e respectivamente, sentido de:

A. consequência, conformidade e explicação.
B. adição, explicação e comparação.
C. oposição, comparação e causa.
D. adição, conformidade e explicação.
E. oposição, explicação e causa.

A conjunção 'mas' na primeira fase nos indica uma ideia que contraria a anterior , uma oposição, divergência, um constraste, oposição
Portanto é uma conjunção de coordenativa adversativa

A conjunção 'como' presente na segunda oração nos mostra uma ideia de adequação, conforme o esperado ao fato.
Portanto é uma conjunção subordinativa conformativa: conforme, segundo, consoante, como

A conjunção 'como' presente na terceira oração nos mostra uma ideia de causa.
Sendo assim, uma conjunção subordinativa causal. Geralmente usado em início de frases:
	
	[yellow]Como[reset] estava doente, não pôde sair.

17. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CREFITO 8 - Assistente Administrativo - 2024 

No trecho “para prevenir e tratar dificuldades físicas e(ou) psicossociais” (linhas 12 e 13), 
uma conjunção coordena duas formas verbais no infinitivo que estão subordinadas a uma oração e que estão introduzidas por outra conjunção.

Errado - A oração não está introduzida por outra conjunção, e sim por uma PREPOSIÇAO. O restante está correto.

18. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRT 1 - Agente de Fiscalização - 2024 


[yellow]Caso[reset] sejam identificadas irregularidades, serão 16 fornecidas orientações e recomendações para que as empresas possam corrigir todas as questões.

O termo “Caso” (linha 15) é uma conjunção subordinativa adverbial concessiva.

ERRADO - O termo 'caso' é uma conjunção subordinativa condicional, indicam uma condição sob a qual se realiza o fato expresso pela oração principal:
se, caso, desde que, contanto que, salvo se, exceto se, sem que(=se não), a não ser que.

        Comprarei o livro, [yellow]desde que[reset] seja barato.
        [yellow]Se[reset] chover, não iremos.
        [yellow]Caso[reset] chova, não iremos.
        [yellow]Se[reset] você demorar, eu não vou te procurar.
        A vaga está disponível, [yellow]caso[reset] você mude de ideia.


19. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - ALE TO - Analista Legislativo - Área Revisão - 2024
Assinale a frase que mostra oposição entre seus segmentos básicos.

A. Uma coisa é ser dono do dinheiro; outra é ter o direito de usá-lo como quiser.
B. Lembre-se de que os vencedores fazem aquilo que os perdedores não querem fazer.
C. Não é a qualidade do dinheiro que você ganha, é a quantidade de dinheiro que você guarda.
D. Toda empresa precisa ter gente que erra, que não tem medo de errar e que aprende com o erro.
E. O resumo da sabedoria é este: nunca é perdido o tempo que se consagra ao trabalho.


Item A
Não há oposição. A frase apenas se refere ao dinheiro.

Item B
As palavras "VENCEDORES" e "PERDEDORES" sao claramente opostas, ou você ganha ou você perde.
há uma antítese (oposição) de termos (segmentos básicos de uma oração).

Item C
Não há oposição. A frase apenas se refere a dinheiro novamente. O contrário de qualidade não é quantidade (afinal, dá para ter os dois).

Item D
Não há oposição. Errar não é o contrário de medo que também não é o contrário de aprender.

Item E
Não há oposição. Não há nenhuma palavra oposta a sabedoria, nunca, perdido, etc


20. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de Caraguatatuba - Professor - Área: Educação Infantil - 2024 
Assinale a frase em que a expressão de tempo sublinhada tem seu valor corretamente identificado.

A. Tempo imediatamente anterior: A felicidade é [yellow]logo[reset] ou nunca.
B. Tempo distante: [yellow]Até[reset] 13 anos eu pensava que meu nome era “cale-se”.
C. Tempo correlato: [yellow]Enquanto[reset] se sonha, não se vive.
D. Tempo posterior imediato: Sinto-me muito melhor [yellow]agora[reset] que eu desisti de esperar.
E. Simultaneidade de tempo: A felicidade é uma bola atrás da qual corremos [yellow]enquanto[reset] rola e a chutamos logo que para.

Item A
A expressão 'logo' é usada para indicar um tempo imediatamente posterior, e não anterior como o item sugere. 

Item B
A expressão 'até' é usada para indicar um limite de tempo, e não necessariamente um tempo distante.

Item C
A expressão 'enquanto' é usada para indicar simultaneidade de tempo, e não um tempo correlato como o item sugere. 

Item D
A expressão 'agora' é usada para indicar o tempo presente, e não um tempo posterior imediato como o item sugere.

Item E
A expressão 'enquanto' é usada para indicar simultaneidade de tempo, que é o que o item E sugere.
está de acordo com o gabarito da banca.

Conjunções Subordinativas Temporais: indicam em que tempo ocorreu o fato expresso na oração principal:
quando, mal, logo que, assim que, sempre que, depois que, desde que, enquanto, apenas, até que, mal, antes que, sempre que

[yellow]Enquanto[reset] os políticos descansam, os brasileiros trabalham arduarmente.
Ela está parada [yellow]desde que[reset] chegou.
[yellow]Quando[reset] digo que deixei de te amar, é porque eu te amo.
[yellow]Logo que [reset]saíram, a festa acabou.
[yellow]Quando[reset] eu disse isso, ninguém acreditou.


21. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRQ 15 - Fiscal - 2024 

Entre muitas outras aplicações práticas, o trabalho do trio permitiu [yellow]que[reset] tratamentos contra o câncer possam ser mais direcionados, 
afirmou o comitê do Nobel.

Na linha 17, a palavra “que” após “permitiu” é uma conjunção integrante.

CORRETISSIMO - 

Um macete para saber se é conjunção integrante:

o "que" pode ser substituida por [yellow]"isso"[reset], logo é uma conjunção integrante.
"o trabalho do trio permitiu isso" 

Isso ocorre porque a oração 'que tratamentos contra o câncer possam ser mais direcionados' funciona como objeto direto do verbo 'permitiu'. 
Portanto, 'que' é uma conjunção integrante, pois integra a oração subordinada substantiva ao verbo principal da oração. 

22. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRF BA - Farmacêutico Fiscal - 2024

"De forma semelhante, no Brasil cerca de 82% da população utiliza produtos à base de plantas medicinais nos seus cuidados com a saúde, 
seja pelo conhecimento tradicional na medicina indígena, quilombola, entre outros povos e comunidades tradicionais, 
seja pelo uso 28 na medicina popular,..."


No último período do texto, o vocábulo “seja” é empregado, em suas duas ocorrências, como conjunção alternativa.

C- Certo

Conjunções e locuções conjuntivas coordenativas alternativas: indicação de alternância, exclusão, alternativa:
ou, ou...ou, ora...ora, quer...quer,já...já, seja...seja

Ou mude seu comportamento, ou mude-se daqui!
Muda de vida ou vai me perder.
Orachovia ora fazia sol. (alternância)
Ou você vem agora ou perde o lugar. Exclusão
Você quer suco ou deseja beber cerveja? (alternativa)

23.Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - EsFCEx - Oficial - Área Ciências Contábeis - 2024

Nas passagens – Aquilo era esquisito, [yellow]mas se tornava muito gostoso.[reset] – e – Prendia tudo na corda [yellow]e suspendia o bambu.[reset] –,
 as orações destacadas expressam, correta e respectivamente, sentidos de

A. conclusão e alternância.
B. oposição e alternância.
C. adição e conclusão.
D. conclusão e adição.
E. oposição e adição.

A primeira oração realmente expressa oposição, utilizando a conjunção 'mas', e a segunda expressa adição, utilizando a conjunção 'e'. 
Este item está de acordo com o gabarito da banca.

Conjunções e locuções conjuntivas coordenativas adversativas:
Indicação de uma ideia que contraria a anterior, uma oposição, uma divergência, um contraste, uma quebra de expectativa:
[yellow]mas, porém, contudo, entretanto, no entanto, todavia, não obstante, senão(= mas sim), só que, ainda assim, e[reset]

Tenho ódio,[yellow]e[reset] morro de amor por ela.
Ela sofria,[yellow] mas[reset] não se queixava.
Os alunos estudaram, [yellow]no entanto[reset], não conseguiram aprovação.
Não queria atrapalhar, [yellow]senão (mas sim)[reset] ajudar.
Esforçou-se para ser agradável,[yellow] não obstante[reset] o futuro sogro não simpatizou com ele.
Este é um bom livro, [yellow]todavia[reset] custa caro.
Estudo bastante, [yellow]só que[reset] não faço exercícios.

24.Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - TJ SP - Psicólogo Judiciário - 2024

Na passagem do 4o parágrafo – Uma desertificação da região não será desastrosa só para pequenos mamíferos da caatinga, [yellow]como[reset] prediz a pesquisa. –, 
a conjunção que substitui corretamente a destacada e a justificativa para o emprego da vírgula são, respectivamente:

A. segundo; separar expressão corretiva.
B. pois; separar expressão resumidora.
C. todavia; separar expressão explicativa.
D. conforme; separar oração subordinada.
E. assim; separar oração coordenada.


O vocábulo "como" é multifuncional; ou seja, pode aparecer basicamente em duas classes gramaticais: conjunção e advérbio.
Quando funciona como conjunção, o conectivo "como" pode estabelecer relação de:

comparação. Exemplo: O residente tratou o paciente como se fosse um médico muito experiente.
causa. Parece óbvio, mas, para estabelecer uma relação lógico-semântica de causa, a oração deve exprimir causa (ou motivo, razão). 
Vale destacar que nesse tipo de oração, a conjunção normalmente vem no início do período e tem valor equivalente a "Já que".
conformação, como no trecho no enunciado da questão. Veja que a informação sobre uma desertificação da região não será desastrosa 
só para pequenos mamíferos da caatinga está conforme prediz a pesquisa.

Conjunções Subordinativas Conformativas: indicam relação de adequação ou conformidade com o fato expresso pela oração principal:
conforme, segundo, consoante, como

Portanto, alternativa 'D'

25.Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Câmara de Itapeva - Analista de Recursos Humanos - 2024 

No trecho “... embora as disparidades tenham aumentado na maioria dos lugares, os últimos anos haviam assistido à redução das desigualdades entre os países...”
(3º parágrafo), o vocábulo destacado estabelece relação de sentido de __________ entre as orações e poderia ser corretamente substituído por __________.

Assinale a alternativa que completa, correta e respectivamente, as lacunas do texto.

A. concessão … uma vez que
B. causa … já que
C. concessão … ainda que
D. condição … ainda que
E. condição … se

Conjunções Subordinadas Concessivas: concedem ou admitem uma condição contrária ao fato expresso pela oração principal, uma oposição fraca:
embora, conquanto, malgrado, ainda que, mesmo que, posto que, apesar de que, se bem que, não obstante, por mais que, por pior que, a despeito de,malgrado, em que pese

Alternativa 'C' -> 'concessão... ainda que'

	[yellow]Embora [reset]você tenha boas intenções, é impossível acreditar em suas palavras.
        [yellow]Por mais que[reset] eu me esforce, não consigo seguir uma dieta.
        [yellow]Mesmo[reset] sendo falso o ar, sinto que respiro.
        Todos saíram, [yellow]embora[reset] estivesse chovendo.
        [yellow]Por mais que[reset] gritasse, ninguém o socorreu.
        Vim trabalhar [yellow]posto que[reset] estivesse doente.


26. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Câmara de Jaboticabal - Assistente - 2024

No trecho “Sem contar com políticas públicas específicas [yellow]para[reset] reduzir as taxas de jovens entre 15 e 29 anos que não estudam [yellow]nem[reset] trabalham…” (1o parágrafo), 
os vocábulos destacados estabelecem, respectivamente, relações de sentido de:

A. direção e negação.
B. direção e adição.
C. condição e negação.
D. finalidade e dúvida.
E. finalidade e adição.

'Para'com o verbo no infinito é conjunção de finalidade..e o 'nem' associado com o não antecedente dá sentido de adição.
Portanto, alternativa 'E'.

27. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - Conselho Regional de Serviço Social da 15ª Região (CRESS AM) - Agente Fiscal - 2024


Tecer algumas considerações sobre este processo é buscar compreender diferentes posicionamentos,lógicas e estratégias que permearam o pensamento e
a ação profissional do serviço social em sua trajetória [yellow]e[reset] [blue]que persistem[reset] até os dias atuais com novas articulações, expressões e redefinições.

No segundo parágrafo, a conjunção “e” antes de “que persistem” liga a oração que se inicia nesse ponto ao trecho “a ação profissional do serviço social em sua trajetória”.

ERRADO - o "que" depois da conjunção 'e' é pronome relativo que se refere a "estratégias", então concluímos que o "e" mencionado na assertiva liga duas orações subordinadas "que permearam..." e "que persistem..."

28. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ITAIPU Binacional - Administrador - 2024 

Fenômenos atmosféricos têm se tornado cada vez mais extremos e mais frequentes [yellow]desde que[reset] entramos no novo milênio. 

No quarto período do primeiro parágrafo do texto CB1A1-II, a oração iniciada pela locução “desde que” estabelece, com a oração que a antecede, uma relação de:

A.causa.
B.condição.
C.tempo.
D.concessão.
E.consequência.

Conjunções Subordinativas Temporais: indicam em que tempo ocorreu o fato expresso na oração principal:
[yellow]quando, mal, logo que, assim que, sempre que, depois que, desde que, enquanto, apenas, até que,mal, antes que, sempre que[reset]

Essas expressões, geralmente, quando vêm perto de datas, será especificando tempo.

Mas também podem ser conjunções subordinadas condicionais «desde que»

«[yellow]Desde que[reset] ela queira.»

«Ela já sabe que pode teclar com quem quiser [yellow]desde que[reset] não me traia.»


29. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - CBM PA - Oficial - 2024

Essas características são o que os cientistas cognitivos denominam vieses, e não verdades constantes. 
Ou seja: os cachorros também conseguem navegar o mundo em termos de objetos, e não de direções. 
[yellow]Contudo[reset], nesse caso, o aprendizado é mais lento e menos intuitivo.

A conjunção “Contudo” (terceiro período do segundo parágrafo do texto 1A1-II) introduz, no período em que se insere, ideia de

A. adição.
B. condição.
C. conclusão.
D. oposição.
E. explicação.

Conjunções e locuções conjuntivas coordenativas adversativas:
Indicação de uma ideia que contraria a anterior, uma oposição, uma divergência, um contraste, uma quebra de expectativa:
mas, porém, contudo, entretanto, no entanto, todavia, não obstante, senão(= mas sim), só que, ainda assim, e


30. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CAU RN - Assistente Administrativo - 2024 


É sério, tá bom? Então não...”,

Na linha 9, emprega‑se “Então” como um conector de valor explicativo.

E - Errado

No texto temos a utilização de "então" como conector de valor conclusivo.

Conjunções e locuções conjuntivas coordenativas Conclusivas: expressam ideia de conclusão:
portanto, por conseguinte, por isso, logo, assim, então, pois(posposto ao verbo), destarte, dessarte

31. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de São José dos Campos - Assistente de Gestão Municipal - 2024 
Nas opções abaixo, há comparações entre dois elementos; assinale a opção em que há um conector que estabelece essa comparação.

A. Na sala, a única peça que ainda resistia ao tempo era uma mesa que, tal qual um caixote estava cheio de marcas de ferramentas que o haviam aberto.
B. As raízes são plantas que crescem para baixo ao passo que os galhos são plantas que crescem para cima.
C. Os livros são folhas das árvores que se sacrificaram em benefício do homem.
D. A solidão é a mãe das reflexões filosóficas.
E. As questões dos concursos públicos são barreiras que precisamos superar para chegarmos bem ao final da corrida.

Item A
Na frase "uma mesa que, tal qual um caixote", o conector "tal qual" é usado para estabelecer uma comparação entre a mesa e um caixote, indicando semelhança entre os dois elementos.
Conjunções Subordinativas Comparativas: indicam uma relação de comparação - igualdade, inferioridade ou superioridade - entre os fatos expressos:
tão...como/quanto, mais...(do)que,menos...(do)que, assim como, tal qual, tal como, assim como,como,tanto...quanto

No item B
O conector não estabelece grau de comparação e sim de PROPORÇÃO
Conjunções subordinadas proporcionais: indicam simultaneidade de ocorrência de fatos:
à medida que, à fim de que, de sorte que, de modo que, porque, à proporção que, quanto mais(menos, melhor, pior, maior, menor)...mais(menos, melhor,pior, maior), 
ao passo que

Os outros itens não possuem conectores de comparação.


32. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ AP - Técnico Judiciário - Área: Administrativa - 2024 
Entre as frases abaixo, aquela que identifica corretamente a relação lógica entre os segmentos destacados, é:

A. Quanto menos tempo se tem, / mais tempo se encontra. ̶ correlação;
B. Nós matamos o tempo, / mas ele nos enterra. ̶ comparação;
C. Enquanto falo, / as horas passam. ̶ condição;
D. Recomendo-te que tenhas cuidado com os minutos, / de vez que as horas cuidarão de si mesmas. ̶ causa e consequência;
E. Como diz um amigo meu, / antes tarde do que mais tarde. ̶ modo.

As conjunções têm o seguinte sentido:


A- Correlação;
[yellow]Quanto menos[reset] tempo se tem, / [yellow]mais[reset] tempo se encontra.
Conjunções subordinadas proporcionais: indicam simultaneidade de ocorrência de fatos.

B- Oposição;
Nós matamos o tempo, / [yellow]mas[reset] ele nos enterra. Não traz ideia de comparação, mas sim de oposição.
Conjunção coordenativa adversativa: ideia contraria a anterior, uma oposição.

C- Temporal;
[yellow]Enquanto[reset] falo, / as horas passam. Não traz ideia de condição e sim temporal, algo : quando, desde que, enquanto

D- Explicação;
Recomendo-te que tenhas cuidado com os minutos, / [yellow]de vez que[reset] as horas cuidarão de si mesmas.
Traz uma ideia de explicação e não causa e consequência. E sim de condição.

E- Conformidade
[yellow]Como[reset] diz um amigo meu, / antes tarde do que mais tarde. Não traz ideia de modo e sim de conformidade.
Conjunção subordinada de conformidade, ideia de adequação ou conformidade.

Gabarito letra A

33. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Câmara de São Paulo - Consultor Técnico Legislativo - Área Registro - 2024
Assinale a frase abaixo – retirada do romance A Mão e a Luva, de Machado de Assis, em que a palavra ainda mostra valor concessivo (=embora).

A. Uma mulher jovem deve usar maquiagem. Uma velha, mais maquiagem ainda.
B. O microscópio serve somente para confundir-nos ainda mais.
C. Os dois amigos demoraram-se ainda algum tempo no corredor, um a insistir com o outro para que subisse, o outro a teimar que queria ir morrer...
D. Mas o certo é que a tempestade serenara; o que havia era uma ressaca, ainda forte, mas que diminuiria com o tempo.
E. - Vieste lavar a alma da poeira do caminho, disse Estêvão que, ainda falando em prosa, cultivava as suas metáforas poéticas.

O vocábulo "ainda" pode assumir várias conotações. É preciso interpretar o contexto, para identificar o sentido da palavra. 

a)  Uma mulher jovem deve usar maquiagem. Uma velha, mais maquiagem ainda.

Errada: valor de intensificação.

Nesta alternativa, não basta apenas "mais maquiagem", é preciso "ainda mais maquiagem". 

O vocábulo "ainda" se liga ao pronome "mais", intensificando-o, sinalizando que é preciso ir além de um ponto.

b)  O microscópio serve somente para confundir-nos ainda mais.
Errada: valor de intensificação.

O microscópio não se limitava a nos confundir mais... ele nos confundia "ainda mais". 

O vocábulo "ainda" se liga ao pronome "mais", intensificando-o, sinalizando que se vai além.

c)  Os dois amigos demoraram-se ainda algum tempo no corredor, um a insistir com o outro para que subisse, o outro a teimar que queria ir morrer...
Errada: valor de adição.

Na frase dada, o vocábulo "ainda" assume o sentido de "Mais", indicando a adição de "algum tempo" à duração da ação de "demoraram-se". 

Os dois amigos demoraram-se mais algum tempo no corredor

d)  Mas o certo é que a tempestade serenara; o que havia era uma ressaca, ainda forte, mas que diminuiria com o tempo.

Errada: valor de tempo.
No trecho "ainda forte", o vocábulo "ainda" indica que até aquele momento, a ressaca estava forte. Portanto, o sentido da palavra é de temporalidade:

o que havia era uma ressaca, até então/até aquele momento forte,

e)  - Vieste lavar a alma da poeira do caminho, disse Estêvão que, ainda falando em prosa, cultivava as suas metáforas poéticas.

Correta: valor concessivo.

A concessão é a oposição a uma ideia sem invalidá-la. 

Perceba que, se Estêvão cultivava metáforas poéticas, então ele deveria falar em versos. Afinal o que caracteriza a construção da poesia são os versos. 

A prosa não é a forma da poesia. Chama-se "prosa" a escrita corrida, em parágrafos, utilizada nos textos não poéticos.

Portanto, "falar em prosa" opõe-se a "cultivar metáforas poéticas" = opõe-se, mas não invalida. Há aqui uma concessão. Note como podemos trocar o "ainda" por locuções de sentido concessivo (com a adaptação do verbo para o modo subjuntivo):

disse Estêvão que, ainda falando em prosa, cultivava as suas metáforas poéticas.
disse Estêvão que, embora falasse em prosa, cultivava as suas metáforas poéticas.
disse Estêvão que, ainda que falasse em prosa, cultivava as suas metáforas poéticas.
disse Estêvão que, não obstante falasse em prosa, cultivava as suas metáforas poéticas.

34. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CREF 19 - Assistente Administrativo - 2024

Em “A precariedade de materiais e infraestrutura esportiva nas escolas” (linhas 1 e 2), a conjunção “e” coordena “precariedade” e “infraestrutura”.

ERRADO - 

"E" coordena "materiais" e "infraestrutura esportiva", que por sua vez estão subordinados ao núcleo "precariedade".

Não coordena "precariedade" e "infraestrutura", pois "infraestrutura" é parte do complemento de "precariedade".


35. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CREF 9 - Assistente Administrativo - 2024 

Em “Paris 1924 foi o marco inicial das vilas olímpicas, [yellow]mas[reset] elas só se tornaram permanentes em Helsinque, Finlândia, em 1952” (linhas de 16 a 18), a conjunção “mas” indica

A.causa.
B.concessão.
C.comparação.
D.tempo.
E.adversidade.

Indica uma Conjunção coordenativa adversativa: mas, porém, contudo, todavia, não obstante.

Alternativa 'E'

35.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TRT 11 - Analista Judiciário - Área: Administrativa - 2024

Na frase [yellow]Embora privado[reset], no estado social, de muitas vantagens da natureza, ele soube adquirir outras, o elemento sublinhado pode ser adequadamente substituído por:

A. A menos que destituído
B. Porquanto encarecido
C. Para se prover
D. Conquanto desprovido
E. Uma vez assoberbado


O conectivo "embora" é essencialmente uma conjunção concessiva. De acordo com Celso Cunha e Cintra (2017, p. 600), as concessivas "iniciam uma oração subordinada em que se admite um fato contrário à ação principal, mas incapaz de impedi-la". Também funcionam como conectivos que indicam ideia de concessão as conjunções "Não obstante", "Apesar de", "Conquanto" e "Posto que".

Além disso, a expressão "desprovido" significa "privar ou desprover algo de alguma coisa".

GABARITO: ALTERNATIVA D.
Nas demais opções, temos conjunções:

A) A locução "a menos que" é usada em orações com ideia de condição.

B) "Porquanto" é conjunção explicativa.

C) A preposição "para", seguida de verbo no infinitivo, indica ideia de finalidade.

E) A expressão "uma vez", em oração reduzida, indica ideia de causa.

36. Ano: 2024 / Banca: Instituto Americano de Desenvolvimento - IADES / Prova: IADES - EMATER DF - Administração - 2024 


[yellow]Quando se pensa no Brasil[reset], costuma-se pensar em Carnaval, futebol e belas paisagens naturais. 
[yellow]De fato, todos esses elementos compõem a cultura brasileira[reset] — e [yellow]são motivo[reset] de orgulho nacional. 
Mas o País vai muito além: com uma das maiores produções agrícolas do mundo, tem o papel de ser a reserva global de alimentos. 
É [yellow]líder inconteste na inovação[reset] entre os 33 países da América Latina, região da qual é de longe a maior economia com um produto interno bruto (PIB) 
de 1,6 trilhão de dólares.


Disponível em: <https://exame.com/revista-exame/>.
Acesso em: 2 fev. 2024, com adaptações.

Considerando os sentidos e os aspectos linguísticos do texto, assinale a alternativa correta.

A. O adjetivo “inconteste” tem função sintática de adjunto adnominal de “líder” e de “inovação”.
B. O sujeito do verbo “compor”, em “compõem a cultura brasileira”, é “todos”.
C. A substituição de “são motivo” por são motivos alteraria os sentidos e afetaria a correção gramatical do texto.
D. A conjunção “Mas”, em “Mas o País vai muito além”, tem valor concessivo no texto.
E. Em “Quando se pensa no Brasil”, o sujeito é indeterminado.

No item A
O adjetivo 'incosteste' tem função sintática de adjunto adnominal do substantivo concreto 'líder' somente.

No item B
O sujeito é 'todos esses elementos' e não somente 'todos' -> todos seria o núcleo.

No item C
Afetaria na correção gramatical, sendo que 'motivo' se refere 'a cultura brasileira' que está no singular

No item D
A conjunção 'Mas' é utilizada para introduzir uma ideia de contraste ou oposição em relação ao que foi mencionado anteriormente. 
Embora possa parecer ter um valor concessivo, seu uso neste contexto visa destacar que, além dos aspectos culturais mencionados, 
o Brasil possui outras qualidades notáveis. Portanto, seu valor é mais adequadamente interpretado como adversativo, não concessivo.

No item E
“Quando se pensa no Brasil”
o verbo "pensar" é VTI

VTI + SE = o "se" será índice de indeterminação do sujeito.

O trecho "Quando se pensa no Brasil" possui sujeito indeterminado que é aquele utilizado todas as vezes que não se pode ou não se quer explicitar o agente da ação verbal.
Quando = Conjunção Subordinativa Temporal (É válido lembrar que Conjunção não exercem função sintática)
Pensa = Verbo conjugado na 3ª pessoa do singular + SE (Este exerce a função de Índice de Indeterminação do Sujeito - IIS)
No Brasil (Objeto Indireto)
Agora vejam o exemplo:
Ex.: Quando como o bolo. Neste caso, EU = sujeito, COMO = Verbo e O BOLO = Obj. Direto.
Se eu quero sumir com o agente da ação verbal, basta apassivar o OD. O termo fica assim: Come-se o bolo.
Percebam que conjuguei o verbo na 3ª do Singular + SE. Daí concluímos que se quero sumir com AGENTE DA AÇÃO verbal quando tenho um VTD, eu apassivo Objeto direto e quando tenho um VTI, eu Indetermino o Sujeito.

37. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ MS - Técnico de Nível Superior - Área Jornalista - 2024 

A conjunção “e” apresenta, primariamente, valor aditivo. Dentre as alternativas abaixo, o único caso em que ela exibe, adicionalmente, valor conclusivo é:

A. “Trata-se de uma planta robusta [yellow]e[reset] viçosa [...]” (2º parágrafo);
B. “[yellow]E[reset] já existe um: o Fusarium oxysporum.” (6º parágrafo);
C. “[...] o agricultor simplesmente corta um pedaço dela [yellow]e[reset] enterra em outro lugar.” (4º parágrafo);
D. “Após a infecção, o solo fica contaminado por mais de 30 anos, [yellow]e[reset] não há nada a fazer [...]” (7º parágrafo);
E. “As tropas de Castillo invadiram o país em 18 de junho de 1954, o Exército não reagiu – [yellow]e,[reset] nove dias depois, o presidente Guzmán acabou forçado a renunciar” (16º parágrafo).

Item: A) 
Análise: A conjunção 'e' neste contexto une adjetivos que descrevem a bananeira, mantendo seu valor aditivo básico, sem indicar uma conclusão. 

Item: B) 
Análise: Aqui, a conjunção 'e' introduz uma informação adicional, mantendo seu valor aditivo e não conclusivo. 

Item: C) 
Análise: Neste caso, a conjunção 'e' conecta duas ações realizadas pelo agricultor no processo de reprodução da bananeira, sem implicar uma conclusão. 

Item: D) 
Análise: A conjunção 'e' neste contexto liga duas informações sobre as consequências da infecção por Fusarium oxysporum, mantendo-se aditiva. 

Item: E) 
Análise: A conjunção 'e' neste contexto, além de adicionar uma informação, introduz uma conclusão ao evento anterior (a invasão e a falta de reação do Exército), 
levando à renúncia do presidente Guzmán. Este uso demonstra a flexibilidade semântica da conjunção 'e', estando de acordo com o gabarito da banca.

38.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Câmara de São Paulo - Técnico Legislativo - Área: Enfermagem - 2024 

Assinale a frase em que a conjunção E tem valor adversativo.

A. O conselho da mulher é pouco [yellow]e[reset] quem não o aceita é louco.
B. Mulheres [yellow]e[reset] elefantes nunca esquecem.
C. A mulher é volúvel como uma pena ao vento, muda de palavra [yellow]e[reset] de pensamento.
D. Homens são como computadores: difíceis de se configurar [yellow]e[reset] nunca têm memória suficiente.
E. O homem é um ser prodigiosamente ondulante [yellow]e[reset] variável.

Item: A) 
Análise: Nesta frase, a conjunção 'E' está ligando duas orações que expressam ideias opostas. 
Na primeira oração, é dito que o conselho da mulher é pouco, ou seja, é algo limitado ou insuficiente. 
Na segunda oração, é dito que quem não aceita esse conselho é louco, ou seja, está cometendo um erro. 
Portanto, a conjunção 'E' está sendo usada para contrastar essas duas ideias, o que indica que ela tem um valor adversativo neste contexto. 
Portanto, este item está de acordo com o gabarito da banca.

Item: B) 
Análise: Nesta frase, a conjunção 'E' está sendo usada para ligar duas ideias que são semelhantes, não opostas. 
Portanto, ela não tem um valor adversativo neste contexto. Portanto, este item não está de acordo com o gabarito da banca.

Item: C) 
Análise: Nesta frase, a conjunção 'E' está sendo usada para ligar duas ideias que são semelhantes, não opostas. 
Portanto, ela não tem um valor adversativo neste contexto. Portanto, este item não está de acordo com o gabarito da banca.

Item: D) 
Análise: Nesta frase, a conjunção 'E' está sendo usada para ligar duas ideias que são semelhantes, não opostas. 
Portanto, ela não tem um valor adversativo neste contexto. Portanto, este item não está de acordo com o gabarito da banca.

Item: E) 
Análise: Nesta frase, não há a presença da conjunção 'E', portanto, não é possível analisar seu valor. 
Portanto, este item não está de acordo com o gabarito da banca.

39.Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - Conselho Regional de Biologia da 9ª Região (CRBio 9ª Região) - Fiscal Biólogo - 2024

Isso é terrível. Espero [yellow]que[reset] arrumem as gaiolas para que outros não fiquem presos desse jeito”, escreveu outro internauta.

O vocábulo “que” (linha 23) é uma conjunção integrante, que encabeça uma oração subordinada substantiva subjetiva.

ERRADO
(Eu) espero ISSO.
Portanto, a oração iniciada pela conjunção que expressa função sintática de objeto direto, sendo classificada como oração subordinada substantiva objetiva direta, 
não como substantiva subjetiva.

40.Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - IRBr - Terceiro Secretário da Carreira de Diplomata - 2024

"Mas, [yellow]se[reset] a visão idílica de Rousseau [yellow]foi[reset] a mais fecunda, [yellow]é[reset] impossível deixar de falar..."

No primeiro período do quinto parágrafo, a conjunção subordinativa “se” introduz uma condição real, o que é evidenciado pelo modo verbal empregado na oração em que ocorre.

CORRETO GABARITO: C


Nesse caso, o "se" tem valor de conjunção causal e, como tal, não expressa dúvida, incerteza e tampouco concessão.

Por isso temos a conjugação verbal no presente do indicativo (condição real) e não no subjuntivo (condição hipotética).

Substituindo o "se" pela conjunção causal "visto que", temos o seguinte:

"Mas, visto que a visão idílica de Rousseau foi a mais fecunda, é impossível deixar de falar..."

Outra explicação:
"Mas, se a visão idílica de Rousseau foi a mais fecunda, é impossível deixar de falar das vertentes mais negativas de interpretação."

Como a conjunção subordinativa "se" é condicional, o verbo "ser" (foi) deveria estar no modo subjuntivo para passar a ideia de condição, de hipótese (fosse), 
e o outro verbo "ser" (é) deveria estar no futuro do pretérito do modo indicativo, que traz a ideia de algo que poderia ter acontecido no futuro em relação ao passado 
(seria), porém no texto eles estão no modo indicativo, no tempo pretérito (foi) e presente (é).

41. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - PC PE - Agente de Polícia - 2024

Vale ressaltar, [yellow]no entanto[reset], que essa não é uma tendência exclusivamente brasileira.

Sem prejuízo da correção gramatical e do sentido original do texto 1A1-I, a expressão “no entanto” (primeiro período do segundo parágrafo) 
poderia ser substituída por:

A. conquanto.
B. sobretudo.
C. portanto.
D. todavia.
E. dessa forma.

Alternativa correta a 'D'
Conjunção coordenativa adversativa, que traz a ideia de Oposição/adversativa/contraste.: 
Mas, porém, contudo, todavia, entretanto ,no entanto, não obstante

No item A
A expressão 'conquanto' é uma conjunção concessiva, usada para indicar uma concessão, ou seja, uma situação em que, apesar de algo, outra coisa acontece.

No item B
A expressão 'sobretudo' é um advérbio que indica principalmente, em especial, acima de tudo. Não estabelece uma relação adversativa

No item C
A expressão 'portanto' é uma conjunção conclusiva, usada para indicar uma conclusão ou consequência. Não estabelece uma relação adversativa

Item D é o gabarito

No item E
A expressão 'dessa forma' é usada para indicar uma consequência ou resultado, não estabelecendo uma relação adversativa.

42.Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - Câmara de Maceio - Apoio Legislativo - 2024 

"Portanto, a discriminação tem como requisito fundamental o poder..." 

O vocábulo “Portanto” (segundo período do segundo parágrafo) introduz uma explicação, por isso substituí-lo por "Pois" manteria a coerência das ideias do texto.

ERRADO - A conjunção "PORTANTO" não é explicativa, é conclusiva. ( Conjunção coordenativa conclusiva )
[yellow] portanto, por conseguinte, por isso, logo, assim, então, pois(posposto ao verbo), destarte, dessarte[reset]

"POIS" - CONCLUSÃO = DEPOIS DO VERBO (ENTRE VIRGULA).
"POIS" - No inicio da oração = Explicativo

43. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRC RR - Contador - 2024

Considerando a estrutura linguística e o vocabulário empregados no texto, julgue os itens a seguir.

",embora estivessem ainda muito comprometidas com os processos de apenas registrar e informar."

A conjunção “embora” (linha 23) expressa circunstância de adversidade no contexto em que ocorre.

ERRADO - A conjunção 'embora' é utilizada para introduzir uma oração subordinada concessiva, admitindo ou concedendo uma ideia contrária ao fato:
[yellow] embora, conquanto, malgrado, ainda que, mesmo que, posto que, apesar de que, se bem que, não obstante, 
por mais que, por pior que, a despeito de,malgrado, em que pese[reset]

44. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de São Lourenço da Mata - Professor de Anos Iniciais - 2024
Leia o texto apresentado e as afirmações sobre os termos nele destacados.

Neste ano, o Festival de Inverno de Garanhuns (FIG) é realizado pela Prefeitura de Garanhuns, com patrocínios do Governo de Pernambuco, 
por meio da Empetur, e do Ministério do Turismo. As ações de literatura acontecem em novo endereço: no Parque Luiz Carlos de Oliveira, 
[yellow]que[reset] receberá o “Espaço da Palavra”, antes chamado de “Praça da Palavra”, [yellow]pois[reset] ficava na praça da fonte luminosa. 
[yellow]Também[reset] muda de endereço a Casa Galeria Galpão, com exposições fotográficas, artes visuais e ações de gastronomia, 
agora instaladas na Escola Municipal Padre Agobar Valença.

Folha de Pernambuco. Agreste: começa hoje o 32º FIG. Folha de Pernambuco. Caderno Cultura, p. 13, 11 jul. 2024. Adaptado.

Analisando o uso dos elementos destacados, conclui-se que:

I. o termo “que” funciona como pronome relativo, referindo-se a “Parque Luiz Carlos de Oliveira”.
II. o termo “pois” tem função adversativa, uma vez que marca uma relação de oposição e contraste entre as informações que ele articula.
III. o termo “Também” tem função aditiva, já que adiciona uma informação semelhante a outra apresentada anteriormente.

É verdadeiro o que se afirma em

A. I e II, apenas.
B. II, apenas.
C. I e III, apenas.
D. II e III, apenas.
E. III, apenas.

Item I - CORRETO
O termo 'que' funciona como pronome relativo, referindo-se a 'Parque Luiz Carlos de Oliveira'. 
Ele introduz uma oração adjetiva que caracteriza o parque, o que está de acordo com a função de pronomes relativos.

Item II - ERRADO

O termo 'pois' introduz, antes do verbo, uma explicação.

Item III - CORRETO

O termo 'Também' tem função aditiva, pois adiciona uma informação sobre outra mudança de endereço, semelhante à mudança anterior mencionada no texto.

45.Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - Conselho Regional de Biologia da 9ª Região (CRBio 9ª Região) - Agente Fiscal - 2024 

[yellow]Além disso[reset], a pesca excessiva ameaça quase dois em cada cinco tubarões de extinção.

O termo “Além disso” (linha 28), que está isolado por vírgula, funciona como um conector de adição.

O "além disso" tem a função de conector de adição. Ele está acrescentando um dado a mais, ligando uma sequência de dados apresentados.
Outros conectores de adição: e, também, em seguida, adicionalmente, não apenas, bem como...
Assertiva correta.

46.Ano: 2024 / Banca: Instituto Quadrix - Quadrix
Prova: Quadrix - Conselho Regional de Biologia da 9ª Região (CRBio 9ª Região) - Agente Fiscal - 2024 

[yellow]Além disso[reset], a pesca excessiva ameaça quase dois em cada cinco tubarões de extinção.

O termo “Além disso” (linha 28), que está isolado por vírgula, funciona como um conector de adição.

O "além disso" tem a função de conector de adição. Ele está acrescentando um dado a mais, ligando uma sequência de dados apresentados.
Outros conectores de adição: e, também, em seguida, adicionalmente, não apenas, bem como...

CORRETO

47. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TCE GO - Analista de Controle Externo - Área: Engenharia - 2024 
Todas as frases a seguir mostram termos ligados pela conjunção

OU.

Assinale a opção em que essa conjunção mantém o valor de alternativa (e não de adição).:

A. João ou Pedro devem ser eleitos presidente da empresa.
B. A alegria ou a tristeza fazem parte da vida.
C. Inglês ou francês são idiomas falados pelos turistas.
D. Os clientes leem livros ou revistas enquanto esperam.
E. Vasco ou Flamengo são times de longa tradição

Item: A) 
Análise: A frase 'João ou Pedro devem ser eleitos presidente da empresa.' utiliza a conjunção 'ou' para apresentar duas opções excludentes, ou seja, 
apenas um dos dois será eleito presidente. Portanto, a conjunção 'ou' mantém o valor de alternativa. Este item está de acordo com o gabarito da banca.
Não existe a possibilidade de João e Pedro serem eleitos presidentes ao mesmo tempo. Será um ou outro

Item: B) 
Análise: A frase 'A alegria ou a tristeza fazem parte da vida.' utiliza a conjunção 'ou' para indicar que ambos os sentimentos fazem parte da vida, 
não sendo excludentes. Aqui, 'ou' tem um valor de adição. 

Item: C) 
Análise: A frase 'Inglês ou francês são idiomas falados pelos turistas.' sugere que ambos os idiomas podem ser falados pelos turistas, não sendo excludentes. 
A conjunção 'ou' tem um valor de adição. 

Item: D) 
Análise: A frase 'Os clientes leem livros ou revistas enquanto esperam.' indica que os clientes podem ler tanto livros quanto revistas, não sendo excludentes. 
A conjunção 'ou' tem um valor de adição. 

Item: E) 
Análise: A frase 'Vasco ou Flamengo são times de longa tradição.' sugere que ambos os times têm longa tradição, não sendo excludentes. 
A conjunção 'ou' tem um valor de adição. 

48. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Prefeitura de Lins - Guarda Civil Municipal - 2024

Leia os versos:

Dói, [yellow]mas[reset] no dia seguinte

Aperto meu pé outra vez

[…]

[yellow]Pois[reset] eu já escolhi meu sapato

Que não vai mais me apertar

Os termos em destaque expressam, correta e respectivamente, sentido de:

A. explicação e causa.
B. conformidade e conclusão.
C. conclusão e concessão.
D. oposição e explicação.


'mas' é conjunção coordenativa adversativa: ideia contraria, uma oposição.

'pois' antes do verbo = explicação / pois depois do verbo = conclusão

CONJUNÇÃO coordenativa EXPLICATIVA. = POIS,PORQUE,ASSIM, QUE.

49. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ITAIPU Binacional - Relações Públicas - 2024 

[yellow]"Embora[reset] seja uma energia limpa e renovável, a eólica causa impactos ambientais e sociais:.."

No texto CB2A1, a conjunção “Embora”, empregada no início do último parágrafo, poderia, sem prejuízo dos sentidos originais do texto ou de sua correção gramatical, 
ser substituída por:

A. Para que.
B. Ainda que.
C. Apesar de.
D. Porque.
E. Desde que.


'embora' é conjunção subordinada concessiva: concedendo ou admitindo uma condição contrária :
podendo ser substituida por 'apesar de'

Item A:
A conjunção 'Para que' é uma conjunção subordinativa final, que indica finalidade, objetivo. Não é adequada para substituir 'Embora' que é uma conjunção concessiva.

Item B:
A conjunção 'Ainda que' é uma conjunção subordinativa concessiva, assim como 'Embora', e também indica uma ideia de contraste ou oposição. Portanto, pode substituir 'Embora' sem alterar o sentido original do texto ou sua correção gramatical.

Item C:
"Apesar de" também é uma conjunção concessiva, porém, sua substituição poderia ocasionar prejuízo gramatical. 

Item D:
A conjunção 'Porque' é uma conjunção subordinativa causal, que indica causa ou motivo

Item E:
A conjunção 'Desde que' é uma conjunção subordinativa condicional, que indica uma condição. Não é adequada para substituir 'Embora' que é uma conjunção concessiva.

50. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - UNESP - Assistente de Suporte Acadêmico - Área: Biblioteca - 2024

Considere a frase.


[yellow]Ainda que[reset] esse gênero tenha tido como uma das principais expoentes a pianista, maestrina e compositora Chiquinha Gonzaga (1847-1935), 
as mulheres tiveram que se esforçar [yellow]para[reset] conquistar respeito e espaço como instrumentistas e compositoras. (2o parágrafo)


As expressões destacadas introduzem, correta e respectivamente, os sentidos de:

A. concessão e modo.
B. concessão e finalidade.
C. condição e finalidade.
D. condição e causa.
E. causa e modo.

A expressão 'ainda que' introduz uma ideia de concessão, e 'para' indica finalidade. 

51. Ano: 2024 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - SPTRANS - Analista de Comunicação - 2024

Considere os trechos:

• … e que se escolha apenas um desses adjetivos [yellow]para[reset] dizer o que se deseja. (1⁠º parágrafo)

• O que deve ler um bom escritor, [yellow]segundo[reset] os economistas? (3⁠º parágrafo)

As palavras destacadas estabelecem, respectivamente, relações de

A. finalidade e conformidade.
B. finalidade e consequência.
C. direção e comparação.
D. direção e modo.
E. causa e modo.

Conjunções Subordinativas Conformativas: indicam relação de adequação ou conformidade com o fato expresso pela oração principal:
conforme, segundo, consoante, como

52. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ITAIPU Binacional - Jornalista - 2024 

Uma expansão em curso, [yellow]ainda[reset] sem data para entrar em operação, elevará a atual capacidade de geração para 5 TWh por ano.

No quinto período do primeiro parágrafo do texto CB2A1, a palavra “ainda” expressa uma ideia de:

A.tempo.
B.adição.
C.contraste.
D.conclusão.
E.condição.

A palavra 'ainda' expressa uma ideia de tempo, indicando que algo está em processo ou continuidade, mas que ainda não foi concluído. 
No contexto do texto, a palavra 'ainda' é usada para indicar que a expansão do complexo eólico está em curso, mas ainda não tem data para entrar em operação. 
Portanto, o item A está de acordo com o gabarito da banca.

53. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - PC PE - Agente de Polícia - 2024

[yellow]Porém[reset], em uma segunda e mais panorâmica leitura do cenário sobre crime e violência no Brasil.

No terceiro período do primeiro parágrafo do texto 1A1-I, a conjunção “Porém” introduz ideia de:

A. explicação.
B. oposição.
C. condição.
D. comparação.
E. exemplificação.

Principais conjunções adversativas: Porém, Todavia, Entretanto, Mas, Contudo, No entanto.
Introduzem uma ideia de oposição.
Vale destacar que o "e" também pode ter a ideia de adversidade com a mesma função do "mas".

Exemplo:

Estudei muito, e não passei.

Estudei muito, mas não passei.

Corrobora mencionar que nesse caso deve-se utilizar a virgula antes do "e".


54. Ano: 2024 / Banca: Instituto Quadrix - Quadrix
Prova: Quadrix - COREN PR - Auxiliar Administrativo - 2024

[yellow]Uma vez que[reset] esses materiais entram em contato com o solo ou a água, 

A locução “Uma vez que” (linha 11) expressa, no texto, uma circunstância temporal.

ERRADO -
A locução 'Uma vez que' no contexto do texto não expressa uma circunstância temporal, mas sim uma relação de causa. 
No trecho 'Uma vez que esses materiais entram em contato com o solo ou a água, podem causar sérias contaminações no ambiente e danos à vegetação', 
a locução 'Uma vez que' pode ser substituída por 'visto que' ou 'porque', indicando uma causa para a contaminação.

54. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ RN - Analista Judiciário - Área Judiciária - Especialidade: Direito - 2023 

Todas as frases abaixo foram iniciadas com o vocábulo “Segundo”, com noção de conformidade; se eliminarmos das frases esse vocábulo, mantendo-se o sentido original, a única forma adequada é:

A.Segundo a Fifa, o jogador do Grêmio deve ser suspenso por três anos / A Fifa manda que o jogador do Grêmio seja suspenso por três anos;
B.Segundo o regulamento do prédio, o morador que deixou lixo no corredor deve ser multado / O regulamento do prédio comenta que o morador que deixou lixo no corredor devesse ser multado;
C.Segundo o Denatran, ninguém pode dirigir sem carteira de habilitação / O Denatran instrui como obter-se a carteira de habilitação, que é obrigatória;
D.Segundo o edital do concurso, a prova tem a duração de quatro horas / O edital do concurso ordena que a prova tenha a duração de quatro horas;
E.Segundo o Serviço de Meteorologia, as chuvas não vão cair neste final de semana / O Serviço de Meteorologia preceitua que as chuvas não vão cair nesse final de semana.

RESOLUÇÃO DA QUESTÃO

A) CERTO
A Fifa é a autoridade máxima para tratar de assuntos relacionados ao futebol, essa instituição pode determinar algo para o jogador, algo que deve ser cumprido conforme orientações da própria Fifa

B) Segundo o regulamento do prédio, o morador que deixou lixo no corredor deve ser multado / O regulamento do prédio comenta que o morador que deixou lixo no corredor devesse ser multado; ERRADO
O regulamento é um instrumento que possui regras; que determina deveres, obrigações e direitos. Portanto o regulamento não "comenta".

C) Segundo o Denatran, ninguém pode dirigir sem carteira de habilitação / O Denatran instrui como obter-se a carteira de habilitação, que é obrigatória; ERRADO
O Denatran não instrui ninguém, ele possui normas que devem ser seguidas, normas que determinam. Instruir tem o mesmo significado de comunicar, informar etc, o que é totalmente diferente de determinar.

D) Segundo o edital do concurso, a prova tem a duração de quatro horas / O edital do concurso ordena que a prova tenha a duração de quatro horas; ERRADO
Aqui já temos um extrapolamento, pois não é possível deduzir que o edital ordenou; o que pode existir é uma determinação, uma regra específica quando a duração da prova.

E) Segundo o Serviço de Meteorologia, as chuvas não vão cair neste final de semana / O Serviço de Meteorologia preceitua que as chuvas não vão cair nesse final de semana. ERRADO
Preceituar é o mesmo que estabelecer uma regra, uma norma, um preceito. Portanto o Serviço de Meteorologia não estabelece uma regra, uma norma ou algum preceito, apenas informa/possibilidade.

55. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Prefeitura - Almoxarife - 2023

Assinale a alternativa em que o vocábulo destacado estabelece, no contexto em que se encontra, relação de sentido de conclusão.

A. Descobri ali que o barato era vitória sofrida, de preferência com gol nos últimos minutos, [yellow]porque[reset] as reações eram melhores. (2o parágrafo)
B. … já que no impeachment do Collor eu não sabia [yellow]bem[reset] do que se tratava e a TV ainda era em preto e branco. (3o parágrafo)
C. … eu nem sabia bem para que servia, mas se o Brasil tinha ganhado era, [yellow]portanto[reset], uma grande coisa. (5o parágrafo)
D. Eu não queria que aquilo acabasse, não podia durar uma semana a mais? Mas no dia seguinte [yellow]já[reset] não era Copa. (6o parágrafo)
E. Era preciso evitar a bagunça, [yellow]logo[reset] mais desfazer os enfeites, se despir da fantasia e retomar a normalidade… (6o parágrafo)


A alternativa em que o vocábulo destacado estabelece, no contexto em que se encontra, relação de sentido de conclusão é a letra C.

Conjunções e locuções conjuntivas coordenativas Conclusivas: expressam ideia de conclusão:
[yellow]portanto, por conseguinte, por isso, logo, assim, então, pois(posposto ao verbo), destarte, dessarte[reset]

Observe que portanto pode ser substituído 'por assim', 'então', 'por conseguinte' etc.

A alternativa A estabelece uma relação de sentido de explicação. Além de porque, os conectivos pois ou visto que estabelecem a mesma relação.

Na alternativa B, o conectivo em destaque estabelece uma relação de certeza, de afirmação. Outras alternativas com o mesmo valor semântico são seguramente, certamente, efetivamente, de certo.

Observe os exemplos:

… já que no impeachment do Collor eu não sabia [yellow]bem[reset] do que se tratava e a TV ainda era em preto e branco. (3o parágrafo)

… já que no impeachment do Collor eu não sabia [yellow]seguramente[reset] do que se tratava e a TV ainda era em preto e branco. (3o parágrafo)

… já que no impeachment do Collor eu não sabia [yellow]de certo[reset] do que se tratava e a TV ainda era em preto e branco. (3o parágrafo)

A alternativa E estabelece uma relação de sentido de sequência e continuidade. Além de logo, os conectivos em seguida, então ou na sequência estabelecem a mesma relação.

Observe os exemplos:

Era preciso evitar a bagunça, logo mais desfazer os enfeites, se despir da fantasia e retomar a normalidade… (6o parágrafo)

Era preciso evitar a bagunça, na sequência desfazer os enfeites, se despir da fantasia e retomar a normalidade… (6o parágrafo)


56. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura do Rio de Janeiro - Fiscal de Rendas - 2023

A frase abaixo em que o termo sublinhado indica simultaneidade temporal, é:

A. [yellow]Enquanto[reset] houver vida, há esperança;
B. [yellow]Assim que[reset] chegou a banda, a música começou;
C. [yellow]Após[reset] a pandemia, alguns hábitos de higiene mudaram;
D. As encomendas para a festa chegaram [yellow]em seguida;[reset]
E. Iniciada a confusão, a polícia chegou [yellow]de imediato.[reset]

A - Enquanto houver vida, há esperança; — ocorrem duas ações ao mesmo tempo. -> Gabarito letra 'A'
B - Assim que chegou a banda, a música começou; — a banda chegou primeiro, depois a música começou.
C - Após a pandemia, alguns hábitos de higiene mudaram; — depois da pandemia (já ocorreu), alguns hábitos de higiene mudaram.
D - As encomendas para a festa chegaram em seguida; — ocorreu alguma coisa antes de as encomendas chegarem.
E - Iniciada a confusão, a polícia chegou de imediato. — a confusão aconteceu primeiro, depois a polícia chegou.

57. Ano: 2023 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRT 10 - Técnico - Área: Industrial - 2023 

No texto, o conectivo “assim como” (linha 23) classifica‑se como conjunção coordenativa conclusiva.

de emitir laudo técnico e de ministrar disciplinas em sua especialidade, [yellow]assim como[reset] de realizar medições e calibrações em equipamentos e de projetar
cabeamentos de rede lógica.

ERRADO -  
A conjunção 'assim como' é classificada como conjunção coordenativa aditiva, pois expressa uma ideia de adição, soma ou continuação de pensamento.


58. Ano: 2023 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRA PE - Contador - 2023 

que viveram em um trecho de oceano, [yellow]mesmo se[reset] você não conseguir observar os animais individualmente.

“mesmo se” (linha 25) por ainda que

A afirmação está certa. Os conectivos "mesmo se" e "ainda que" expressam o mesmo valor semântico, o de concessão, 
indicando algo que poderia impedir ou afetar o que se expressa na oração principal, mas que não impede ou afeta.

59. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Câmara de Monte Alto - Contador - 2023 

Considere os trechos.

• … ficamos tão fora do sério com a falta de perspectiva política, [yellow]que[reset] não conseguimos nos erguer e respirar… (4o parágrafo)

• Precisamos ser críticos a essa ideia plasmada de humanidade homogênea (…), [yellow]pois[reset] essa ideia dispensa a experiência de viver numa terra cheia de sentido (5o parágrafo)

É correto afirmar que os termos destacados estabelecem nas frases, respectivamente, as ideias de:

A.consequência e concessão.
B.causa e explicação.
C.proporção e causa.
D.consequência e explicação.
E.proporção e concessão.

O item D sugere que os termos destacados estabelecem nas frases as ideias de consequência e explicação, o que está correto. 
No primeiro trecho, a conjunção 'que' estabelece uma relação de consequência. No segundo trecho, a conjunção 'pois' estabelece uma relação de explicação.

60. Ano: 2023 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - SEPLAG DF - Analista de Políticas Públicas - Área Gestão Governamental - 2023

Em “[yellow]Assim[reset], na Europa, a área de política pública vai surgir como um desdobramento dos trabalhos baseados em teorias explicativas sobre o papel do Estado e de uma das mais importantes instituições do Estado – o governo –, produtor, por excelência, de políticas públicas.” (linhas de 9 a 14), a palavra sublinhada apresenta valor

A. concessivo.
B. temporal.
C. conclusivo.
D. adversativo.
E. alternativo.

"Assim" é uma conjunção coordenada conclusiva.

conjunções coordenadas conclusivas:

-logo;
-pois (posposto ao verbo);
-portanto;
-assim;
-então;
-por isso;
-por conseguinte;
-por consequência;
-consequentemente;
-de modo que;
-desse modo;
-destarte;

61. Ano: 2023 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - SEPLAG DF - Analista de Políticas Públicas - Área Gestão Governamental - 2023

Em “No entanto, o desenho das políticas públicas e as regras que regem suas decisões, elaboração e implementação também influenciam os resultados dos conflitos 
inerentes às decisões sobre política pública.” (linhas de 30 a 33), as expressões sublinhadas apresentam, respectivamente, valor:

A. aditivo e adversativo.
B. adversativo e aditivo.
C. consecutivo e aditivo.
D. explicativo e aditivo.
E. alternativo e adversativo.


Vejamos cada conectivo:

-> "No entanto" é essencialmente uma conjunção adversativa (ver Cegalla, 2009, p. 290). Com isso, fica fácil identificar a alternativa B como o gabarito.

-> "Também" é um conectivo usado para indicar uma ideia de adição. Principalmente, quando vem antecedida da conjunção "e".

GABARITO: ALTERNATIVA B.

62. Ano: 2023 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - DPE AM - Assistente Técnico de Defensoria - Assistente Técnico Administrativo - 2023

Talvez pense que ensaio uma reconciliação, [yellow]embora[reset] esteja cansada de saber que sou adepto de caminhadas peripatéticas No contexto em que se encontra, o elemento sublinhado expressa ideia de

A. concessão.
B. causa.
C. consequência.
D. condição.
E. comparação.

A conjunção 'embora' é uma conjunção subordinativa concessiva, que indica uma circunstância contrária ao que seria esperado, mas que não impede a realização do fato expresso na oração principal. 

63. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEE MG - Especialista em Educação Básica - Área: Orientação Educacional/Supervisão Pedagógica - 2023 
Assinale a opção em que a conjunção E mostra um valor diferente do de adição.

A. Há duas palavras que abrem muitas portas: Puxe e Empurre.
B. É preciso sermos ponte, cobrir os abismos e nunca aprofundá-los.
C. Boa comunicação é tão estimulante quanto café preto e tão difícil quanto dormir depois.
D. Há tanta suavidade em nada dizer e tudo se entender...

Oposição de ideias ou termos contrastantes: e (com significado de mas adversativo)

Nada dizer, e (mas) tudo se entender [...]

64. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - EsFCEx - Oficial - Área: Capelão Evangélico - 2023

Considere os seguintes enunciados:

Nesse outro mundo eu me liberto da pequenez e das picuinhas do meu cotidiano e experimento, (I) ainda que momentaneamente, uma felicidade divina.


Protestei. Senti-me mal, (II) como se fosse um ladrão. (III) Mas não adiantou.


Assinale a alternativa que expressa corretamente as relações coesivas providas pelos conectivos nos enunciados e a respectiva reescrita.

A. restrição: apesar de momentaneamente; (II): comparação: sendo um ladrão; (III) oposição: Portanto não adiantou.
B. contraste: mesmo que momentaneamente; (II): condição: caso fosse um ladrão; (III) ressalva: Nem adiantou.
C. tempo: sempre momentaneamente; (II) modo: mesmo não sendo ladrão; (III) contraste: Contudo não adiantou.
D. condição: desde que momentaneamente; (II) conformidade: de modo que eu fosse um ladrão; (III) Porém não adiantou.
E. concessão: embora momentaneamente; (II) comparação: tal qual um ladrão; (III) restrição: Todavia não adiantou.


'ainda que' é conjunção subordinada concessiva presente no texto original, podendo ser substituida por 'embora', também uma conjunção subordinada concessiva
'como' se fosse um ladrão é conjunção subordinada comparativa presente no texto original, podendo ser substituida por 'tal qual' também uma conjunção subordinada comparativa
'mas' é conjunção coordenativa adversativa presente no texto original podendo ser substituida por 'todavia' que também é uma conjunção coordenativa adversativa.

	Portanto, gabarito letra 'E'.

65.Ano: 2023 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - IPREV DF - Analista Previdenciário – Perfil de Investimentos - 2023 


"...suas previsões de 25 crescimento para 2023 a níveis próximos dos de recessão em muitos países, [yellow]à medida que[reset] o impacto dos aumentos das taxas de juros se intensifica,"

Na quarta linha do quinto parágrafo, é correto substituir “à medida que” por "conforme", uma vez que essa substituição não altera o sentido do parágrafo.

ERRADO -

A locução "à medida que" introduz oração com valor de proporcionalidade. Essa locução poderia ser substituído por "à proporção que". 
Entretanto, a conjunção "conforme" é usada para introduzir oração conformativa.

GABARITO: ITEM ERRADO.

66. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPE SC - Promotor de Justiça Substituto - Tarde - 2023

O justo é um saber que se vai constituindo [yellow]à medida que[reset] nossa consciência da história se aguça. 

No segundo período do primeiro parágrafo, a locução conjuntiva “à medida que” denota proporcionalidade entre duas situações.

CORRETO - A conjunção conecta duas situações que ocorrem simultaneamente com sentido de proporcionalidade entre uma e a anterior.

67. Ano: 2023 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - SEPLAG DF - Analista – Área: Tecnologia da Informação e Comunicação - 2023

Em “As últimas décadas registraram o ressurgimento da importância do campo de conhecimento denominado políticas públicas, [yellow]assim como[reset] das instituições, 
regras e modelos que regem sua decisão, elaboração, implementação e avaliação.” (linhas de 1 a 5), a expressão sublinhada pode ser substituída, 
sem que haja alteração do sentido original do período, por:

A. em particular.
B. especialmente.
C. bem como.
D. principalmente.
E. exclusivamente.

A opção correta é a letra C.

A expressão "bem como" é classificada como uma conjunção subordinada comparativa, oferecendo um paralelo em relação à oração.

Possui o mesmo valor de comparação da expressão "assim como", que também é classificada como uma conjunção subordinativa comparativa, 
ligando ambas as orações com sentido comparativo.

As expressões apresentadas nas letras A, B, D e E: em particular; especialmente; principalmente e exclusivamente; 
são expressões com valor adverbial de modo, que introduz a oração com valor de circunstância de modo à informação que está sendo apresentada. 
Não possuem o mesmo sentido da expressão em destaque.

68.Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TJ ES - Analista Judiciário - Área Apoio Especializado - Especialidade: Letras - 2023
 
No primeiro período do último parágrafo, a expressão “além de” constitui um elemento de coesão que estabelece noção de esclarecimento.

"Trata-se de uma ferramenta de avaliação da administração pública, de diagnóstico e auxílio na escolha das prioridades e de promoção de boas práticas organizacionais, 
que, [yellow]além de[reset] ajudar políticos a priorizarem ações com base em uma inteligência de dados bem robusta..."

A locução "Além de" é usada para indicar ideia de adição, acréscimo, inclusão.

GABARITO: ITEM ERRADO.

69.Ano: 2023 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 15 - Analista Judiciário - Área Apoio Especializado - Especialidade: Tecnologia da Informação - 2023
 
Otermo sublinhado indica ideia de adição no seguinte segmento:

A. Para lá a família leiri emigrou [yellow]para[reset] prosperar. (2º parágrafo)
B. E seus passos eram alegres [yellow]quando[reset] a sirene tocou. (3º parágrafo)
C. leiri-san inspecionava as conversas dos navios [yellow]que[reset] nasciam no estaleiro que dirigia com disciplina. (2º parágrafo)
D. Não importava a ela que seu otosan estivesse em um leito de hospital [yellow]nem[reset] que o medo rondasse cada esquina. (3º parágrafo)
E. [yellow]Talvez[reset] elas não contenham toda a verdade. (1º parágrafo)


Item: A) 
Análise: No segmento 'Para lá a família leiri emigrou para prosperar.', o termo 'para' é uma preposição que indica finalidade, 
e não uma conjunção coordenativa aditiva que expressa ideia de adição. 

Item: B) 
Análise: No segmento 'E seus passos eram alegres quando a sirene tocou.', o termo 'quando' é uma conjunção subordinativa temporal, 
e não uma conjunção coordenativa aditiva que expressa ideia de adição. 

Item: C) 
Análise: No segmento 'leiri-san inspecionava as conversas dos navios que nasciam no estaleiro que dirigia com disciplina.', 
o termo 'que' é um pronome relativo, e não uma conjunção coordenativa aditiva que expressa ideia de adição. 

Item: D) 
Análise: No segmento 'Não importava a ela que seu otosan estivesse em um leito de hospital nem que o medo rondasse cada esquina.', 
o termo 'nem' é uma conjunção coordenativa aditiva que expressa ideia de adição, estando de acordo com o gabarito da banca.

Item: E) 
Análise: No segmento 'Talvez elas não contenham toda a verdade.', o termo 'talvez' é um advérbio de dúvida, 
e não uma conjunção coordenativa aditiva que expressa ideia de adição. 

70.Ano: 2023 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRA PE - Advogado - 2023 

[yellow]Mas[reset] o material genético extraído de amostras do solo revelou uma rica variedade de plantas e animais.

O “Mas” (linha 2) introduz uma oração coordenada adversativa e pode ser substituído por porém, sem alteração de sentido do texto.

Conjunções e locuções conjuntivas coordenativas adversativas:
Indicação de uma ideia que contraria a anterior, uma oposição, uma divergência, um contraste, uma quebra de expectativa:
mas, porém, contudo, entretanto, no entanto, todavia, não obstante, senão(= mas sim), só que, ainda assim, e

71. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Prefeitura de Sertãozinho - Cuidador Social - 2023

No trecho “[yellow]Apesar do[reset] seu pequeno tamanho (que varia de 7,6 a 33 cm), o rato-toupeira-pelado vive, em média, 30 anos” (2o parágrafo), a expressão destacada estabelece entre as ideias relação de

A. adição, pois o tamanho do animal e seu tempo de vida são duas de suas características.
B. explicação, pois o tamanho do rato-toupeira-pelado é definido por seu tempo de vida.
C. conclusão, pois só é possível saber o tamanho do rato-toupeira-pelado determinando-se sua idade.
D. concessão, pois o tamanho do animal não condiz com o tempo relativamente longo que vive.
E. exemplificação, pois o tamanho do animal é um exemplo da sua capacidade de viver 30 anos.

A opção correta é a letra D. O conectivo "apesar de" aponta para ideia de concessão porque introduz uma informação que poderia impedir ou 
afetar o que se afirma na oração principal, mas que não impede nem afeta. No caso em questão, o tamanho do rato-toupeira-pelado poderia 
indicar que ele tem pouco tempo de vida, porém isso não acontece, já que esse animal vive por bastante tempo.

72.Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - EPC PB - Repórter Fotógrafo - 2023 

Naturalmente, a gentileza precisa ser uma via de mão dupla, é difícil ser gentil com aqueles que são abertamente desdenhosos conosco, 
[yellow]ainda que[reset] talvez isso seja possível para os santos. A santidade, [yellow]entretanto[reset], não é uma qualidade que se costuma encontrar na vida política, e, 
[yellow]dessa forma[reset], não se pode contar com ela para a promoção de um comportamento decente. Apenas a cultura da tolerância pode fazer isso.
 
Assinale a alternativa que identifica, correta e respectivamente, as relações de sentido estabelecidas pelos elementos de sequenciação textual 
destacados no terceiro parágrafo.

A. concessão, restrição e conclusão.
B. restrição, contraste e modo.
C. tempo, condição e comparação.
D. condição, oposição e modo.
E. conclusão, contradição e comparação.

O enunciado se refere ao seguintes conectivos:

-> "ainda que" é usado para iniciar oração concessiva, pois exprime um fato que se concede ou se admite em relação a outro. 
Tal conectivo é equivalente às conjunções "embora, mesmo que, ainda que, não obstante, por mais que etc".

-> "entretanto" é essencialmente uma conjunção coordenativa adversativa, tal como "mas, porém, no entanto, contudo, todavia,  etc". 
As orações adversativas exprimem contraste, oposição, ressalva (ver Cegalla, 2009, p. 373).

-> "dessa forma" é usada para indicar ideia de conclusão. Assim como: 'portanto, por isso, assim, então, pois(posposto ao verbo), destarte, dessarte
Equivalente ao conectivo "portanto". São conjunções coordenativas conclusivas.

GABARITO: ALTERNATIVA A.

73. Ano: 2023 / Banca: Instituto Quadrix - Quadrix
Prova: Quadrix - Prefeitura de Alto Paraíso de Goiás - Fiscal de Tributos Municipais - 2023 
Assinale a alternativa que apresenta uma frase na qual o uso das preposições está correto e as conjunções correspondem ao sentido indicado entre parênteses.

A. Por mais que (concessão) eu não esteja convencido da perspectiva de que você defendeu, acredito que tivemos uma boa discussão.
B. Os documentos que você mostrou são suficientes, por isso (finalidade) podemos seguir adiante.
C. Caso (condição) haja algum item do qual você discorde, estou disposto a discutir.
D. A obra que mais gosto é uma ótima referência para (finalidade) aprofundar este assunto.
E. Os autores a cujos trabalhos nos referimos são sempre elogiados, já que (adversidade) fizeram contribuições relevantes para a cultura.

Item A:
A conjunção 'por mais que' é usada corretamente para indicar concessão, no entanto, a preposição 'de' não é apropriada no contexto. 
A forma correta seria 'da perspectiva que você defendeu'.

Item B:
A conjunção 'por isso' é usada para indicar causa ou consequência, e não finalidade. 
A frase estaria correta se a conjunção fosse 'para que', que indica finalidade.

Item C:
CORRETA

Item D:
A conjunção 'caso' é usada corretamente para indicar condição, e a preposição 'do qual' também está correta, estabelecendo uma relação de posse com o substantivo 'item'.

Item E:
A conjunção 'já que' é usada para indicar causa ou explicação, e não adversidade.

74.Ano: 2023 / Banca: Instituto Americano de Desenvolvimento - IADES / Prova: IADES - IRBr - Terceiro Secretário da Carreira de Diplomata - 2023

O contrário também é possível, [yellow]pois[reset], ao excluir escritores,acaba silenciando uma produção que gradualmente vai sendo esquecida, 
como foi o caso das escritoras oitocentistas.

O conectivo “pois” (linha 8) tem valor conclusivo acerca do silenciamento de escritores que acabam sendo esquecidos, uma vez que a referida conjunção se apresenta após a forma verbal “é”.

ERRADO -  Analisando o contexto do texto, percebemos que a conjunção 'pois' está sendo utilizada para indicar uma causa ou motivo, 
e não uma conclusão. Isso porque ela está introduzindo uma explicação para a afirmação anterior.

75.Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - TJM SP - Técnico em Comunicação e Processamento de Dados Judiciário - 2023
 
No trecho – Em razão da existência de casais que decidiram morar juntos, [yellow]porém[reset] mantendo uma relação de namoro … (3o parágrafo) —, 
o termo destacado estabelece entre as ideias relação:

A. adversativa, como em: Segundo o Código Civil, para que uma relação seja considerada união estável…
B. adversativa, como em: … não haverá conversão do namoro em união estável, todavia os direitos da criança serão resguardados.
C. causal, como em: … reformulando leis, pois é essencial trazer segurança jurídica para os indivíduos.
D. conclusiva, como em: Assim, visando estancar as obrigações jurídicas derivadas do término do relacionamento…
E. conclusiva, como em: … e apresentar tanto cláusulas comuns como outras adicionadas pelo casal.


'porém' é conjunção coordenativa adversativa assim como: mas, porém, contudo, todavia, no entanto, entretanto, só que, ainda sim
Portanto, a alternativa B é a correta.

76. Ano: 2023 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRM TO - Administrador - 2023 

Se eles puderem viver como as próprias entidades plenas, então devemos perguntar [yellow]se[reset] é moralmente permissível criar seres vivos apenas para fins de pesquisa”, defende.

No trecho “se é moralmente permissível” (linhas 21 e 22), o vocábulo “se” indica que o sujeito da oração é indeterminado.

O 'se' é uma conjunção subordinativa integrante, e não um índice de indeterminação do sujeito. 
Um erro comum é confundir as várias funções do 'se' na língua portuguesa. 
Para evitar esse tipo de confusão, é importante analisar cuidadosamente o contexto em que o 'se' está inserido e a função que ele está desempenhando na frase.

“então devemos perguntar se é…
“então devemos perguntar isto.
Quando o “se” ou “que” puder ser trocada por “isto” é porque é uma conjunção integrante e inicia uma oração subordinada substantiva. 
O sujeito do verbo é oculto “nós devemos perguntar..”

77. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - TRF 3 - Analista Judiciário - Àrea Apoio Especializado: Arquitetura - 2023

No trecho do primeiro parágrafo – A dengue é uma doença periódica e cíclica: os casos crescem no verão e há picos epidêmicos a cada 4 ou 5 anos. 
Trata-se, portanto, de enfermidade de atuação previsível. –, 
os dois-pontos e as vírgulas são empregados, correta e respectivamente, para sinalizar

A. a inclusão de um contra-argumento; separar conjunção condicional.
B. o detalhamento de uma informação; separar conjunção conclusiva.
C. o resumo das informações precedentes; separar expressão adverbial.
D. a retificação de uma informação; separar aposto explicativo.
E. a inclusão de informação nova; separar oração intercalada.

'portanto' que está entre vírgulas no texto é conjunção coordenativa conclusiva assim como: por conseguinte, por isso, logo, assim, então, pois(posposto ao verbo)

78. Ano: 2023 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - SMS SP - Residência em Nutrição - Área: Práticas Integrativas e Complementares em Saúde - 2023 

Apesar dos entraves, principalmente nos momentos

iniciais da pandemia, a Atenção Básica permaneceu como a

porta de entrada do Sistema Único de Saúde (SUS), uma vez

que se encontra capilarizada pelos territórios e conta com

atuação multiprofissional para a assistência, 

No texto, a locução “uma vez que” (linhas 3 e 4) estabelece uma relação de:

A.comparação.
B.causalidade.
C.condição.
D.finalidade.
E.concessão.

Causalidade - ITEM B

Conjunções Subordinativas Causais: indicam a causa de fato expresso pela oração principal :
porque, porquanto, visto que, pois que, como, já que, dado que, uma vez que, na medida em que, sendo que, uma vez que, haja vista que

79.Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Câmara de Várzea Paulista - Auxiliar - Área: Serviços Técnicos - 2023
 
Observe as passagens:

[yellow]Segundo[reset] Fran Winandy, a reflexão sobre o etarismo... (2o parágrafo)
Agora as pessoas estão começando a refletir, [yellow]mas[reset] ainda é um tema desconhecido por muitos. (4o parágrafo)
A conscientização é o primeiro ponto, [yellow]porque[reset] ela leva à reflexão. (8o parágrafo)

As palavras em destaque expressam, correta e respectivamente, relações de sentido de:

A. conformidade; explicação; causa.
B. explicação, conclusão; explicação.
C. conclusão; concessão; causa.
D. conformidade; oposição; explicação.
E. explicação; causa; oposição.

80.Ano: 2023 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - SAEB - Analista - Área: Engenheiro Agrimensor - 2023 

Assinale a alternativa que preencha correta e respectivamente as lacunas:

Prefiro trem ______ ônibus. Informe ______ passageiros que os preços aumentaram.

Lembrei ______ todos que o voo estaria lotado.

Sempre acabo concordando ______ eles.

A. do que / os / de / por.
B. a / aos / em / por.
C. a / aos / a / com.
D. aos / os / de / com.

O verbo 'informar' é transitivo indireto. Quem informa, informa a alguém: aos passageiros.(preposição + artigo) Eliminando assim as alternativas A e D
O verbo 'lembrar' é transitivo direto e indireto. Quem lembra, lembra de algo: que o voo estaria lotado. A alguem: à todos. Eliminando a alternativa B
Sobrando assim a C.

81.Ano: 2023 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRB 9º Região - Agente de Orientação e Fiscalização - 2023

Esse conceito se aplica a um tipo de parágrafo considerado como padrão, e padrão não apenas no sentido de modelo, de protótipo, que
se deva ou que convenha imitar, dada a sua eficácia, [yellow]mas também[reset] no sentido de ser frequente, ou predominante, na obra de escritores — sobretudo modernos — de
reconhecido mérito.

"Isso, todavia, não nos impede de apontar e(ou) comentar exemplos tanto dos que..."


As expressões “mas também” (linhas 17 e 18) e “todavia” (linha 25) possuem exatamente o mesmo valor de oposição.

ERRADA - A expressão "mas também" é uma expressão que indica a adição de informações, 
sendo classificada na gramática do Domingos Paschoal Cegalla como uma das conjunções aditivas, 
o referido gramático afirma que essas conjunções aditivas "Dão ideia de adição, acrescentamento: 
e, nem, mas também, mas ainda, senão também, como também, bem como". 

A conjunção "todavia" é uma conjunção coordenativa adversativa, um tipo de conjunção que indica adversidade, oposição entre informações, 
Cegalla classifica dessa forma as conjunções adversativas: 
"Exprimem oposição, contraste, ressalva, compensação: mas, porém, todavia, contudo, entretanto, senão, ao passo que, antes (= pelo contrário), no entanto, não obstante, apesar disso, em todo caso".

82.Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - Secretaria de Educação e Esportes de Pernambuco - Professor - Área: Intérprete de Língua Brasileira de Sinais - 2023 
 
No segundo período do quinto parágrafo, a conjunção ‘pois’ introduz uma conclusão.

De acordo com ela, a situação de alunos negros requer ainda mais atenção. 
“É preciso prestar atenção nessa condição: a pessoa já estava vulnerável socialmente, sem a possibilidade de realizar um isolamento dentro de casa, 
[yellow]pois[reset] vive em uma casa pequena ou onde não há cômodos suficientes”, contextualiza Suelaine.

O pois, quando não deslocado, possui o papel de explicação. = Conjunção explicativa.
O trecho 'pois vive em uma casa pequena ou onde não há cômodos suficientes' está explicando a situação de vulnerabilidade social mencionada anteriormente. 
Portanto, a conjunção 'pois' está sendo utilizada como uma conjunção coordenativa explicativa, e não conclusiva.


83. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Prefeitura de Piracicaba - Auxiliar de Saúde Bucal - 2023

A palavra ou expressão em destaque expressa relação de sentido de condição na alternativa:

A. [yellow]Logo,[reset] muita gente acaba dedicando horas preciosas… (2o parágrafo)
B. … acaba dedicando horas preciosas do seu dia [yellow]a fim de[reset] emitir críticas… (2o parágrafo)
C. [yellow]Porém,[reset] não dávamos bola para isso. (3o parágrafo)
D. [yellow]Se[reset] tivéssemos nos distraído com o blá-blá-blá… (4o parágrafo)
E. Você pode ser o indivíduo mais legal que existe, [yellow]mas[reset], se estiver progredindo… (4o parágrafo)

A opção correta é a letra D. 
A conjunção "se" é subordinativa condicional e expressa sentido de condição, introduzindo uma oração que expressa uma condição para que alguém maior e 
com mais recursos engolir os donos das empresas em questão. 
Podemos trocar essa conjunção por outra com mesmo sentido, como "caso" (realizando algumas adaptações verbais): 
Caso tivéssemos nos distraído com o blá-blá-blá dos outros, alguém maior e com bem mais recursos poderia ter nos engolido.

As demais opções estão incorretas porque apresentam em destaque conectivos que não expressam ideia de condição, mas, sim, 
de conclusão ("logo", na opção A), finalidade ("a fim de", na opção B) e oposição ("porém", na opção C, e "mas", na opção E).

84. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - Prefeitura de Pindamonhangaba - Professor de Educação Básica - Área: Educação Infantil e Ensino Fundamental - 2023

[yellow]Assim[reset], o sítio não é apenas o cenário onde a ação pode transcorrer. 
Ele representa igualmente uma concepção do mundo, da sociedade e do Brasil, [yellow]bem como[reset] uma tomada de posição a propósito da criação de obras para a infância, 
como se vê no trecho de O irmão de Pinóquio:


No terceiro parágrafo do texto, Assim e bem como estabelecem entre as ideias, correta e respectivamente, as relações de

A.causa e simultaneidade.
B.conclusão e adição.
C.consequência e finalidade.
D.concessão e comparação.
E.tempo e condição.

Vejamos cada conectivo destacado:

-> "Assim": veja que esse conectivo traz uma conclusão sobre o que foi dito antes no parágrafo anterior. Nesse caso, tal conectivo é equivalente às conjunções "portanto", "dessa forma" etc.;

-> A locução "bem como" é usada para indicar uma ideia de adição em relação à oração anterior (ver Cegalla, 2009, p. 289).

85. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - TRF 3 - Técnico - Área Apoio Especializado - Especialidade: Edificações - 2023

A conjunção “embora” substitui corretamente a expressão destacada em:

A. No teatro grego antigo, [yellow]quando[reset] não havia solução para um impasse...
B. Segundo especialistas, [yellow]porém,[reset] o perigo não está na criatura...
C. A inteligência artificial faz parte da rotina, [yellow]ainda[reset] que não se perceba.
D. ... resolvia o problema e, [yellow]assim,[reset] acabava a peça.
E. [yellow]Então,[reset] as máquinas começaram a gerar imagens perfeitas de pessoas...

Item: A) 
Análise: A expressão 'quando' indica uma relação temporal, enquanto 'embora' é uma conjunção concessiva que introduz uma ideia de contraste ou oposição. 
Portanto, a substituição não é adequada e não mantém o sentido original da frase.

Item: B) 
Análise: A expressão 'porém' é uma conjunção adversativa que indica oposição, mas não é uma concessiva. 
A substituição por 'embora' não é correta, pois altera o sentido da frase, que é de contraste e não de concessão.

Item: C) 
Análise: A expressão 'ainda que' é uma conjunção concessiva, assim como 'embora'. 
Ambas introduzem uma ideia de concessão, ou seja, algo que ocorre apesar de uma condição contrária. 
A substituição é adequada e mantém o sentido original da frase. Este item está de acordo com o gabarito da banca.

Item: D) 
Análise: A expressão 'assim' indica uma consequência ou conclusão, enquanto 'embora' é uma conjunção concessiva. 
A substituição não é adequada, pois altera o sentido da frase, que é de conclusão e não de concessão.

Item: E) 
Análise: A expressão 'então' indica uma sequência temporal ou causal, enquanto 'embora' é uma conjunção concessiva. 
A substituição não é adequada, pois altera o sentido da frase, que é de sequência ou causa e não de concessão.

86. Ano: 2023 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - SEAGRI - DF - Analista - Área: Contador - 2023 

No trecho “A efetivação do projeto de mudança, no entanto, só se concretizou na presidência de Juscelino Kubitschek, que assumiu o Governo em 1956, com o início das obras ocorrendo em novembro do mesmo ano.” (linhas de 5 a 8), a relação lógica apresentada pela conjunção adversativa é a de

A. acrescentar a ideia de que somente no governo de Juscelino Kubitscheck houve a mudança da capital para o interior do País.
B. negar o fato de que, desde a colonização dos portugueses, já se pretendia expandir o País para o interior.
C. explicar a transferência da capital do País para o interior a partir de 1956, com o objetivo de desenvolver outras regiões para poder povoá-las.
D. concluir os ideários europeus em relação à expansão de seus domínios portugueses e a sua subsistência por meio da agricultura.
E. demonstrar oposição quanto à informação apresentada no primeiro período do texto, o qual trata do projeto de transferência da capital do País para o interior do Brasil desde a época da colonização portuguesa.


A resposta está no enunciado que traz a palavra "oposição". A regra é clara: as orações adversativas exprimem oposição (ver Cegalla, 2009, p. 374). 
Essa é a ideia expressa pelo conectivo "no entanto" que demonstra oposição entre o primeiro período e a oração em que tal conectivo aparece.

GABARITO: ALTERNATIVA E.


87. Ano: 2023
Banca: Instituto Quadrix - Quadrix
Prova: Quadrix - CAU TO - Assistente Administrativo - 2023
Texto associado 
A expressão “conforme” (linha 18) possui o mesmo valor semântico de conquanto.

A cerimônia de premiação será [yellow]conforme[reset] a seguir.

O termo "conforme" se refere a uma conjunção conformativa, por sua vez, o termo "conquanto" diz respeito a uma conjunção concessiva.

Conjunções mais traiçoeiras que aparecem nas provas (de acordo com a tabela de conectivos do professor Elias Santana

Conclusivos --> por conseguinte

Explicativos/Causais --> porquanto

Concessivo--> Conquanto

Condocionais--> Conquanto

88. Ano: 2023 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - SEPLAG DF - Gestor Governamental - Área: Estatística - 2023 

Os termos sublinhados em “A crítica à judicialização da saúde, [yellow]embora[reset] tenha se tornado a regra, não é uniforme em seus argumentos. 
[yellow]Ademais[reset], é raro encontrar quem rejeite peremptoriamente a importância do acesso à justiça como forma de demandar concretização de direitos.” (linhas de 39 a 43), sem que haja alteração de sentido e nem incorreção gramatical no texto, podem ser substituídos, respectivamente, por

A. conquanto; Além disso.
B. ainda que; Además.
C. contanto que; Além do mais.
D. porquanto; Demais.
E. salvo se; Além disso.


O primeiro termo em destaque, "embora", expressa valor concessivo e pode ser substituído por outros de mesmo sentido, como "conquanto" ou "ainda que". 
No caso em questão, essa conjunção indica que o fato de a crítica à judicialização ter se tornado regra poderia indicar que ela é uniforme, padronizada, sem variações, 
entretanto não indica isso, pois essa crítica "[...] não é uniforme em seus argumentos".
O segundo termo em destaque, "ademais", é um advérbio de inclusão, assim como os termos "além disso" e "além do mais". 
Esse termo adiciona mais uma característica à crítica dada à judicialização da saúde, indicando que ela não chega a ponto de rejeitar 
o uso da justiça para se conseguir acesso a determinados direitos, como direto à saúde.
A opção correta, portanto, é a letra A.
As demais opções estão incorretas porque apresentam termos com outros valores semânticos, como "contanto que", com ideia de condição; 
"porquanto", com ideia de explicação; "salvo se", com valor adversativo; e "demais", com ideia de intensidade.

89. Ano: 2023 / Banca: Fundação para o Vestibular da Universidade Estadual Paulista - VUNESP
Prova: VUNESP - PM SP - Soldado PM de 2ª Classe - 2023

Em “Eu estaria mentindo [yellow]se[reset] dissesse que o reino era perto, [yellow]pois[reset] o reino era realmente distante mesmo!” (3o quadro), os termos destacados expressam, 
correta e respectivamente, as ideias de:

A. consequência e causa.
B. causa e conclusão.
C. explicação e consequência.
D. conclusão e condição.
E. condição e explicação.

Alternativa (e). Essa é a nossa alternativa correta. 
Em “Eu estaria mentindo se dissesse que o reino era perto, pois o reino era realmente distante mesmo!” (3º quadro), 
o elemento "se" transmite a ideia de condição, porque indica uma condição necessária para que algo ocorra, 
é uma partícula que pode ser classificada como uma conjunção subordinativa condicional, sobre as conjunções condicionais, 
Cegalla nos ensina que elas "Iniciam orações que exprimem condição ou hipótese: se, caso, contanto que, desde que, salvo se, sem que (= se não), 
a não ser que, a menos que, dado que". 
Na mesma passagem vemos que a partícula "pois" indica o sentido de explicação em relação ao que foi dito antes dessa conjunção, 
pois funciona como uma conjunção coordenativa explicativa, sobre esse tipo de conjunção, 
Cegalla nos ensina que elas "Precedem uma explicação, um motivo: que, porque, porquanto, pois (anteposto ao verbo)".

Gabarito: letra E

90.Ano: 2023 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - SEC - Professor da Educação Básica - Área Língua Portuguesa - 2023
 
Observe no parágrafo 6º: “é proibido não apenas segurar o celular, [yellow]mas também[reset] mexer no aparelho (...)”,
 o termo em destaque tem a função de conjunção e pode ser substituído por uma das alternativas sem perda de sentido.

A. [yellow]é proibido[reset] segurar o celular, [yellow]contudo[reset] mexer no aparelho é ilícito.
B. [yellow]é proibido[reset] segurar o celular, [yellow]entretanto[reset] mexer no aparelho é correto.
C. [yellow]é proibido tanto[reset] segurar o celular [yellow]quanto[reset] mexer no aparelho.
D. [yellow]é proibido[reset] não apenas segurar o celular, [yellow]todavia[reset] mexer no aparelho é possível.
E. [yellow]é proibido[reset] não apenas segurar o celular, [yellow]conforme[reset] mexer no aparelho é lícito.

91. Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - Prefeitura de Jaboatão dos Guararapes - Guarda Civil Municipal Pós-Edital - 2024 - 2º Simulado

Assinale a alternativa que corretamente apresenta o sentido do conector destacado no trecho “Em um esforço dedicado para enriquecer as vidas das crianças e dos adolescentes, a cidade de Jaboatão dos Guararapes está firmemente comprometida em promover cultura e lazer como ferramentas essenciais para o desenvolvimento saudável e equilibrado da juventude”.

A. Consecutivo.
B. Concessivo.
C. Comparativo.
D. Proporcional.
E. Conformativo.

Letra c.

Assunto abordado: Conectivos.

(A) Errada. Trata-se de conjunção subordinativa de valor comparativo. Conjunções consecutivas apresentam uma condição para a realização ou não do fato a que se refere a oração principal.
(B) Errada. Trata-se de conjunção subordinativa de valor comparativo. Conjunções concessivas apresentam uma contrariedade em relação ao fato exposto na oração principal.
(C) Certa. Conjunções comparativas apresentam uma comparação em relação ao fato a que se refere a oração principal.
(D) Errada. Trata-se de conjunção subordinativa de valor comparativo. Conjunções proporcionais apresentam uma noção de proporção em relação ao fato a que se refere a oração principal.
(E) Errada. Trata-se de conjunção subordinativa de valor comparativo. Conjunções conformativas apresentam um acordo, uma conformidade com o fato a que se refere a oração principal.

92. Ano: 2024 /Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPU - Técnico do Ministério Público - Área Administração Área: Auditoria - Pós-Edital - 2024 - 1º Simulado 
 
No penúltimo período do segundo parágrafo, o vocábulo “que” retoma “consciência”.

 É a consciência da necessidade de estabelecer e de viver essas relações [yellow]que[reset] constitui a razão de base da não-violência.

Termo expletivo "é que". Nesse caso, fica mais difícil enxergar porque o termo "é" está distante do termo "que".
Quando estiver inserido os termos: é...que ou foi...que, juntos ou separados, liguem o alerta para partícula expletiva

92. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - CODEVASF - Analista em Desenvolvimento Regional - Área: Administração Pós-Edital - 2024 - 1º Simulado

No período "É um nada a um tempo vazio e rico.", a conjunção "e" está conectando duas ideias contraditórias.

A conjunção "e" não está conectando duas ideias contraditórias, mas sim duas ideias que complementam a descrição da sensação de "nada". 
A conjunção "e" é utilizada para adicionar informações sobre a natureza do "nada", que é descrito simultaneamente como vazio e rico, 
sem que haja contradição entre essas características. 

93. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Analista Judiciário - Área Judiciária Pós-Edital - 2024 - 4º Simulado

Em “Enquanto os homens saíam para caçar e desenvolviam o sentido de orientação que hoje lhes permite lidar com mapas e estradas, 
as mulheres ficavam na caverna, organizando as coisas”, a conjunção “enquanto” traduz a ideia de tempo, com valor de simultaneidade, concomitância.

No quinto período do segundo parágrafo, a conjunção “enquanto” indica uma ideia de proporcionalidade.

ERRADO -a conjunção “enquanto” traduz a ideia de tempo, com valor de simultaneidade, concomitância.

94 - Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Analista Judiciário - Área Judiciária Pós-Edital - 2024 - 1º Simulado

Pôs a água a ferver e abriu a porta de serviço para apanhar o pão. Como estivesse completamente nu, olhou com cautela para um lado e para outro antes
de arriscar-se a dar dois passos até o embrulhinho deixado pelo padeiro sobre o mármore do parapeito. 

A conjunção “como” (l. 14) introduz uma oração com valor de causa.

a conjunção “como” introduz oração subordinada adverbial causal, já que é possível identificar no texto a ideia de causa e consequência.

95. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE

Considerando os sentidos do texto precedente e seus aspectos linguísticos, julgue os itens que se seguem.

Talvez, então, ele devesse apenas desfrutar aquela imagem particular [yellow]enquanto[reset] ela durasse. Ele ficou ali olhando, sem saber se ria ou chorava.

A conjunção “enquanto” em “enquanto ela durasse” (sexto período do quarto parágrafo) indica uma ideia de proporcionalidade.

E-Errado - a conjunção “enquanto” traduz a ideia de tempo, com valor de simultaneidade, concomitância.

96.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - ALE TO - Analista Legislativo - Área Revisão - 2024
Assinale a frase em que não está presente uma expressão ou termo indicativo de causa.

A. O paisagista pinta tranquilo porque a paisagem defronte não se pode aproximar do quadro para ver se está parecida.
B. A História é como um estilingue. Quanto mais fundo você puxa, mais longe você alcança.
C. Algumas pessoas são o centro das atenções numa festa por terem ótimo senso se humor.
D. Em função de algumas declarações falsas, a repórter foi obrigada a desmenti-las.
E. Em vista do aumento de impostos, houve grande reclamação dos empresários.

O "Quanto mais... mais" indica proporcionalidade - Alternativa 'B'

97.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TJ MS - Técnico de Nível Superior - Área Biblioteconomia - 2024 

Dentre as alternativas abaixo, o único caso em que o significado do elemento sublinhado foi identificado INCORRETAMENTE é:

A. “[yellow]Mas[reset] a prática teve uma consequência terrível: [...]” (3º parágrafo) – oposição;
B. “E também significa que a planta se reproduz de [yellow]forma assexuada” [reset](4º parágrafo) – modo;
C. “Ela não tem, [yellow]como[reset] Carlos II não teve, um pai e uma mãe com genes bem diferentes [...]” (5º parágrafo) – comparação;
D. “As bananeiras são clones – [yellow]por isso[reset], um único patógeno pode exterminá-las todas.” (5º parágrafo) – conclusão;
E.  “Os séculos se passaram, e, [yellow]à medida que[reset] as rotas comerciais foram se espalhando pelo mundo, o mesmo aconteceu com a banana.” (10º parágrafo) – finalidade.

Os itens estão de acordo com o elemento sublinhado, exceto o item E:

'À medida que' é uma conjunção que indica proporcionalidade, não finalidade.

98. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - CNJ - Analista Judiciário - Área Judiciária Pós-Edital - 2024 - 2º Simulado

O conectivo “como” (l. 25) indica um valor causal dentro do contexto em que se insere.

Ele acabará tirando da Saúde o sr. Miguel, como tirou do IBGE o general Poly”

a conjunção “como” estabelece, contextualmente, uma ideia comparativa. Por esse motivo, o item está incorreto.

99. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Analista Judiciário - Área Judiciária Pós-Edital - 2024 - 5º Simulado

A conjunção “Entretanto” (segundo período do segundo parágrafo) introduz uma oração com valor concessivo.

Já no século III a.C., há a clássica história do Princípio de Arquimedes. Conta Vitrúvio que o rei Hierão de Siracusa mandou fazer uma coroa de ouro. 
[yellow]Entretanto[reset], quando a coroa foi entregue, o rei suspeitou que o ouro fora trocado por prata.

A conjunção “Entretanto” indica valor adversativo, assim como “mas, porém, contudo, todavia”.

100.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - STN - Auditor Federal de Finanças e Controle Econômico-financeira - Pós-Edital - 2024 - 1º Simulado

Assinale a alternativa que corretamente apresenta o sentido do conector destacado no trecho :
“A ferramenta vem sendo atualizada com novas tecnologias [yellow]como[reset], por exemplo, a versão web do módulo gerencial do sistema.”.

A. Consecutivo.
B. Conformativo.
C. Comparativo.
D. Proporcional.
E. Temporal.

Alternativa C -  Conjunções comparativas apresentam uma comparação em relação ao fato a que se refere a oração principal.

101. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TCDF - Auditor de Controle Externo - Área: Psicologia Pós-Edital - 2024 - 1º Simulado 

No trecho “Não sei se você realmente se importa com o que aconteceu”, a palavra “se” desempenha a função de conjunção integrante, 
sendo responsável por introduzir uma oração subordinada substantiva. A ausência dessa conjunção não alteraria significativamente o sentido da frase.

Errado.
O “se” no trecho apresentado é uma conjunção integrante que introduz a oração subordinada substantiva objetiva direta 
“se você realmente se importa com o que aconteceu”, funcionando como complemento do verbo “sei”. 
A retirada da conjunção “se” comprometeria a estrutura sintática e o sentido da frase, tornando-a incompleta. 
Portanto, a conjunção “se” é essencial para a coesão e o sentido da oração, desempenhando uma função indispensável na estrutura do período.

102. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 7º Simulado

No trecho “O estudo da Nasa serve como um alerta urgente para a necessidade de ações imediatas contra as mudanças climáticas” (último parágrafo), 
a palavra “como” funciona morfologicamente como uma conjunção subordinativa comparativa, estabelecendo uma relação de comparação.

CORRETO
 
103. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Técnico Judiciário - Área: Agente da Polícia Judicial Pós-Edital - 2024 - 4º Simulado 

Não é, pois, um símbolo morto; é uma entidade viva, consagrada a funções gloriosas.

No sétimo período do primeiro parágrafo, o vocábulo “pois” estabelece relação explicativa entre orações.

E- Errado

POIS/ ENTRE VÍRGULA (,pois,) É CONCLUSÃO.

POIS/ SÓ UMA VÍRGULA ANTES (,pois) É EXPLICAÇÃO

"Pois" Antes do verbo  = explicativo.
"Pois" Depois do verbo = conclusivo.

104.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TCE GO - Conhecimentos Gerais - Pós-Edital - 2024 - 1º Simulado
Assinale a alternativa em que o termo destacado indica ideia de simultaneidade temporal.

A. [yellow]Enquanto[reset] eu viver, vou tentar apagar toda dor.
B. [yellow]Assim que[reset] a orquestra iniciou, todos se emocionaram.
C. [yellow]Mal[reset] as provas chegaram, os alunos se agitavam.
D. [yellow]Depois[reset] que ele operou a visão, a vida mudou completamente.
E. Ele sabia que a maré ia subir [yellow]logo[reset].

Letra a.

Assunto abordado: Domínio dos mecanismos de coesão textual

Os conectores “assim que, mal, depois que e logo” indicarão valor tempo. Mas apenas o termo “enquanto” é que trará uma ideia de simultaneidade, concomitância.


105.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - Prefeitura de Jaboatão dos Guararapes - Guarda Civil Municipal Área: Judiciária - Pós-Edital - 2024 - 1º Simulado

Assinale a alternativa que corretamente apresenta o sentido do conector destacado no trecho “[yellow]Uma vez que[reset] foi palco de duas grandes batalhas dos Guararapes, em 1648 e 1649, considera-se que os verdadeiros sentimentos de nacionalismo e patriotismo que impulsionaram o nascimento do Brasil como nação íntegra e soberana surgiram também ali.”.

A. Consecutivo.
B. Conformativo.
C. Causal.
D. Comparativo.
E. Temporal.

Conjunções causais apresentam uma razão para o acontecimento apontado na oração principal. Alternativa C


Conjunções Subordinativas Causais: indicam a causa de fato expresso pela oração principal :
[yellow]porque, porquanto, visto que, pois que, como, já que, dado que, uma vez que, na medida em que, sendo que, uma vez que, haja vista que[reset]

106. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de Niterói - Analista de Políticas Públicas - Área Gestão Governamental Pós-Edital - 2024 - 2º Simulado
Assinale a alternativa em que a conjunção “se” não apresenta valor de condição.

A. Se soubéssemos as consequências de cada decisão tomada, evitaríamos muitos erros ao longo da vida.
B. Se a verdade fosse subjetiva, os conceitos de certo e errado perderiam significado absoluto.
C. Se o silêncio fosse a melhor resposta, então as palavras seriam nossa pior ferramenta de comunicação.
D. Se as normas fossem respeitadas em sua totalidade, a convivência social se aproximaria da harmonia.
E. Se você comprou este carro recentemente, não acha exagero caminhar a pé até o trabalho todos os dias?

(A) Errada. A conjunção “Se” introduz uma hipótese: “Se soubéssemos as consequências de cada decisão tomada”. A segunda parte da frase apresenta o resultado dessa hipótese: “evitaríamos muitos erros ao longo da vida”. Nesse caso, “Se” tem valor condicional, pois estabelece uma relação de dependência entre a condição e a consequência.

(B) Errada. Na frase, a conjunção “Se” indica uma situação hipotética: “Se a verdade fosse subjetiva”. A continuação mostra a consequência dessas hipóteses: “os conceitos de certo e errado perderiam significado absoluto”. Nesse caso, “Se” tem valor condicional, conectando uma condição a um resultado possível.

(C) Errada. A frase começa com uma hipótese induzida por “Se”: “Se o silêncio fosse a melhor resposta”. A sequência apresenta a consequência dessa hipótese: “então as palavras seriam nossa pior ferramenta de comunicação”. Nesse caso, “Se” tem valor condicional ao estabelecer a relação entre a condição e seu efeito.

(D) Errada. A frase utiliza a conjunção “Se” para introduzir uma condição: “Se as normas forem respeitadas em sua totalidade”. A consequência dessa condição é exposta a seguir: “a convivência social se aproxima da harmonia”. Nesse caso, “Se” possui valor condicional, ligando uma hipótese a um resultado possível.

(E) Certa. Na frase, a conjunção “Se” possui valor causal, equivalendo a “Como” ou “Já que”. A frase utiliza “Se” para introduzir uma razão ou causa para a pergunta feita. Não há relação de condição, mas sim de causalidade, em que uma compra recente do carro é o motivo pelo qual caminhar a pé até o trabalho pode ser considerado um exagero.

107. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - PC MG - Perito Criminal Pós-Edital - 2024 - 1º Simulado

"A arma utilizada no crime estava carregada, entretanto, o suspeito alegou que não tinha intenção de atirar, portanto, solicitou-se a análise do mecanismo de segurança da arma para comprovar sua eficiência." Sobre o uso dos conectores neste trecho, é correto afirmar que:

A. O conector "entretanto" está inadequadamente utilizado, pois indica uma ideia de consequência, quando deveria ser substituído por "assim".
B. O uso de "portanto" indica corretamente uma relação de conclusão, que está de acordo com a lógica do argumento apresentado no laudo.
C. O conector "entretanto" está inadequado, pois deveria ser substituído por "além disso", para indicar adição de informações.
D. O uso dos conectores "entretanto" e "portanto" está correto, ambos estabelecendo uma boa relação entre as orações, garantindo a coesão textual.
E. O conector "portanto" está incorreto, pois não introduz uma conclusão válida, devendo ser substituído por "contudo".

A) Errada, pois "entretanto" expressa corretamente uma ideia de oposição e não de consequência.

(B) Certa, pois o conector "portanto" expressa de forma adequada a conclusão com base nos fatos apresentados.

(C) Errada, pois "entretanto" está correto no contexto de oposição entre as orações, e "além disso" indicaria uma ideia de adição que não cabe no contexto.

(D) Errada, pois "portanto" está correto, mas "entretanto" não deveria ser substituído.

(E) Errada, "portanto" é o conector correto para uma conclusão, e "contudo" não caberia nesse contexto.

108. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Câmara de Fortaleza - Analista - Área Redação - 2024
Assinale a frase, retirada de literatos brasileiros, em que a classe gramatical da palavra “mais” está corretamente indicada.

A. “E nada existe [yellow]mais[reset] abstrato do que o poema concreto” / pronome indefinido.
B. “Entrou a das Dores. Nenen, [yellow]mais[reset] uma amiga sua, que fora passar o dia com ela, rodavam de mãos nas cadeiras, rebolando em meio de uma volta de palmas cadenciadas, no acompanhamento do ritmo requebrado da música.” / advérbio.
C. “O Botelho não faltou ao prometido: dias depois do contrato selado e assinado, João Romão recebeu uma carta do vizinho, solicitando-lhe a fineza de ir jantar com ele [yellow]mais[reset] a família;” / preposição.
D. “Agora está livre. Doravante o que você fizer é só seu e [yellow]mais[reset] de seus filhos, se os tiver. Acabou-se o cativeiro de pagar os vinte mil-réis à peste do cego!” / advérbio.
E. “Ninguém melhor do que ele sabia lisonjear o amor-próprio feminino; ninguém prestava com [yellow]mais[reset] alma esses leves serviços de sociedade, que constituem muita vez toda a reputação de um homem.” / conjunção.


O MAIS pode ser PRONOME INDEFINIDO, ADVÉRBIO ou PREPOSIÇÃO

Quando é que ele será um Pronome Indefinido? Quando ele se referir a um substantivo, nesse caso ele terá valor de QUANTIDADE
Quando ele será Advérbio? Quando ele se referir a um verbo, adjetivo ou outro advérbio, e nesse caso ele estará intensificando o valor do termo ao qual ele se refere;
E também pode indicar ideia de tempo (advérbio de tempo), e nesse caso virá acompanhado da palavra não ou nunca, por exemplo: Nunca mais vi a Lua/ Não vou mais falar com você,
Em certos contextos, a palavra "mais" pode ser usada como sinônimo da preposição "com", indicando companhia.
"Eu mais três amigos fomos ao cinema ontem."


LETRA A) Mais se refere ao substantivo abstrato, portanto é advérbio
LETRA B) Mais é utilizada como sinônimo da preposição "com", portanto é preposição
LETRA C) Mais é utilizada como sinônimo da preposição "com", portanto é preposição
LETRA D) Emprego impopular da palavra mais, substituindo a preposição "de", portanto é preposição
LETRA E) Mais se refere ao substantivo alma, portanto é pronome indefinido.

109. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - BACEN - Analista - Área: Tecnologia da Informação - 2024

No entanto, a força de trabalho torna-se mais vulnerável, [yellow]pois[reset] as leis trabalhistas ainda se baseiam em um antigo sistema “binário”

No primeiro período do terceiro parágrafo, a oração introduzida pelo vocábulo “pois” consiste em uma explicação para o que se afirma na oração imediatamente antecedente.

C - Certo

'pois' isolado é explicativo e verificar o contexto da frase.

110. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de São José dos Campos - Técnico Tributário - 2024

Assinale a opção em que a conjunção E mostra valor de adição e não se oposição.

A. A rosa vive uma hora, e o cipreste, cem anos.
B. Conheço um pouco sobre a natureza, e nada sobre o homem.
C. Meu principal objetivo na vida é fazer as pessoas, felizes, e isso é quase impossível.
D. Deus fez a vida para ser praticada e não para ser conhecida.
E. A vida se vive e se escreve.

Item A: 
Análise do Item: Neste item, a conjunção 'e' é utilizada para contrastar a duração da vida de uma rosa com a de um cipreste, 
indicando uma oposição entre a brevidade e a longevidade. Portanto, o valor semântico aqui é de contraste, não de adição.

Item B: 
Análise do Item: Aqui, a conjunção 'e' conecta duas ideias que expressam uma oposição entre o conhecimento sobre a natureza e a falta de conhecimento sobre o homem. 
Esse uso sugere um contraste entre os dois tipos de conhecimento, não uma adição.

Item C: 
Análise do Item: O item apresenta uma conjunção 'e' que parece adicionar duas ideias, mas na verdade estabelece um contraste entre o objetivo de fazer as 
pessoas felizes e a dificuldade de alcançá-lo. 
A ideia de impossibilidade introduzida após a conjunção sugere um contraponto ao objetivo mencionado, caracterizando um valor de oposição.

Item D: 
Análise do Item: Neste caso, a conjunção 'e' liga duas ideias que, embora relacionadas ao propósito da vida, introduzem uma oposição entre 'ser praticada' e 
'ser conhecida'. Esse uso implica uma preferência ou priorização de uma ação sobre a outra, não uma simples adição.

Item E: 
Análise do Item: Este item é o único em que a conjunção 'e' claramente adiciona duas formas de experienciar a vida: vivendo-a e escrevendo-a. 
Não há contraste ou oposição entre as ideias, mas sim uma complementaridade, o que está de acordo com o valor aditivo da conjunção 'e' conforme solicitado na questão.

111. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de São Lourenço da Mata - Professor de Língua Portuguesa - 2024

De acordo com o art. 5º do Estatuto da Criança e do Adolescente, 
“nenhuma criança ou adolescente será objeto de qualquer forma de negligência, discriminação, exploração, violência, crueldade e opressão, 
punido na forma da lei qualquer atentado, por ação ou omissão, aos seus direitos fundamentais”. Portanto, a violação dos direitos infantojuvenis, 
seja por ação ou por omissão dos seus direitos, pode levar à responsabilidade civil e administrativa do agente.

Direitos da Criança e do Adolescente. Disponível em: https://servicosocialca.paginas.ufsc.br/. Acesso em: 19 jul. 2024.

Avalie se as afirmativas a seguir são verdadeiras (V) ou falsas (F):

( ) A expressão “de acordo com” é um conectivo que expressa a ideia de conclusão.
( ) A palavra “infantojuvenil” é formada por um processo de derivação sufixal.
( ) A vírgula em “violação dos direitos infantojuvenis, seja por ação ou por omissão” é considerada opcional e pode ser eliminada, mantendo-se as demais vírgulas do trecho, sem prejuízo da norma-padrão.

As afirmativas são, respectivamente,

A.F – F – F.
B.V – F – F.
C.F – V – V.
D.V – F – V.
E.V – V – F.

"A expressão 'de acordo com' é um conectivo que expressa a ideia de conclusão."
Análise: A expressão "de acordo com" é um conectivo que introduz a ideia de conformidade ou acordo, e não de conclusão. 
Ela é usada para citar fontes ou referências, indicando que algo está em conformidade com o que foi mencionado.
Resultado: Falsa (F)
"A palavra 'infantojuvenil' é formada por um processo de derivação sufixal."
Análise: A palavra "infantojuvenil" é composta pela junção de dois radicais: "infanto" (referente a criança) e "juvenil" (referente a jovem). 
Trata-se, portanto, de uma palavra formada por composição por justaposição e não por derivação sufixal.
Resultado: Falsa (F)
"A vírgula em 'violação dos direitos infantojuvenis, seja por ação ou por omissão' é considerada opcional e pode ser eliminada, 
mantendo-se as demais vírgulas do trecho, sem prejuízo da norma-padrão."
Análise: A vírgula antes da oração iniciada por "seja" marca uma oração subordinada adverbial reduzida de subjuntivo, que é explicativa. 
Essa vírgula é necessária para separar a oração principal da explicação ou adição feita pela oração subordinada. Portanto, a vírgula não é opcional.
Resultado: Falsa (F)

112. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Analista Judiciário - Área: Serviço Social Pós-Edital - 2024 - 1º Simulado

No trecho "A quantidade de notificações cresce a cada ano, à medida que mais pessoas se conscientizam sobre esse crime e os canais de denúncia são difundidos", 
as palavras "que" e "e" são, respectivamente, pronome relativo e conjunção coordenativa aditiva.

o termo "à medida que" é uma locução conjuntiva proporcional. O "que" não está retomando antecedentes.
O termo que integra a conjunção proporcional no contexto, ou seja, não exerce a função de pronome relativo
o conectivo 'e'  é sim uma conjunção coordenativa aditiva.

113. Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - MPE AM - Agente de Apoio - Área: Administrativa - 2024

Entretanto, no melo daquele quase nada apareceu um bicho estranho: uma tartaruga do mar. (1º parágrafo)

O termo sublinhado pode ser substituído, sem prejuízo para o sentido do texto, por:

A. Afinal
B. Portanto
C. Então
D. Assim
E. Contudo

A Afinal- creio que seja uma conjunção conclusiva 
B Portanto - conjunção conclusiva
C Então- conjunção conclusiva
D Assim- conjunção conclusiva

'entretanto' ou 'contudo' são coordenativas adversativas mas, porém, contudo, todavia, no entanto, entretanto, e , não obstante, só que, ainda assim etc
Gabarito letra 'E'

114. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Analista Judiciário - Área Judiciária Pós-Edital - 2024 - 1º Simulado

Enquanto esperava, resolveu fazer um café.

Na linha 13, a conjunção “enquanto” indica uma ideia de proporcionalidade.
ERRADO
Em “Enquanto esperava”, a conjunção “enquanto” traduz a ideia de tempo, com valor de simultaneidade. 

115. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - STN - Auditor Federal de Finanças e Controle Contábil (Conhecimentos Gerais) - Pós-Edital - 2024 - 1º Simulado

Assinale a alternativa que corretamente apresenta o sentido do conector destacado no trecho 
[yellow]“De acordo [reset]com o Tesouro, 75% dos investidores que adquiram os ‘títulos verdes’ são da Europa e da América do Norte, e 25% da América Latina, incluindo o Brasil.”.

A. Conformativo.
B. Consecutivo.
C. Comparativo.
D. Proporcional.
E. Temporal.

Trata-se de conjunção subordinativa de valor conformativo. Alternativa A

116.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - Prefeitura de Jaboatão dos Guararapes - Guarda Civil Municipal Pós-Edital - 2024 - 2º Simulado

Assinale a alternativa que corretamente apresenta o sentido do conector destacado no trecho “Uma vez que traz alegria e conforto por meio da interação com cães treinados, essa iniciativa destaca o poder transformador dos animais e reforça a importância do cuidado holístico em nossa comunidade”.

A. Consecutivo.
B. Conformativo.
C. Causal.
D. Comparativo.
E. Temporal.

'uma vez que' Trata-se de conjunção subordinativa de valor causal.

117 - Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Analista Judiciário - Área: Serviço Social Pós-Edital - 2024 - 1º Simulado

No trecho "Nada repara a dignidade nem devolve o tempo perdido por uma vítima que teve a liberdade cerceada", a palavra "nem" funciona como uma conjunção coordenativa aditiva.

O item está certo, pois no trecho mencionado, a palavra "nem" é uma conjunção coordenativa aditiva que liga as orações 
"Nada repara a dignidade" e "devolve o tempo perdido por uma vítima que teve a liberdade cerceada", apresentando uma ideia de adição.

118 - Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TCE PA - Auxiliar de Controle Externo Pós-Edital - 2024 - 2º Simulado
Apenas uma opção abaixo não apresenta termo ou expressão indicadora de causa:

A. O jogo foi suspenso pelo juiz, porquanto o acirramento dos ânimos da torcida ameaçava a segurança.
B. Em virtude das manifestações confusas e violentas, o Exército tomou frente da situação para controlar os excessos dos manifestantes.
C. Algumas opiniões são como terremotos. Abalam até as estruturas mais fixas da sociedade.
D. Os eventos começaram todos atrasados, haja vista as chuvas fortes repentinas.
E. O rio teve de ser desviado de seu curso natural devido ao garimpo intenso realizado na região.

(A) Errada. A conjunção “porquanto” indica causa. Não podemos confundir com a conjunção de escrita semelhante “portanto”, que indica conclusão. 
(B) Errada. A locução prepositiva “em virtude de” carrega sentido de causa. 
(C) Certa. A palavra “como” até pode ocorrer com sentido de causa, mas este não foi o caso aqui. 
Quando indica sentido de causa, a conjunção “como” aparece em oração subordinada adverbial escrita antes da oração principal, 
e não no meio da frase da maneira empregada aqui. Trata-se aqui de conjunção comparativa: algumas opiniões são como terremotos. 
(D) Errada. A locução “haja vista” é empregada em articulações de causa e consequência. 
(E) Errada. A locução prepositiva “devido a” indica causa

119. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TSE-UNIF - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 7º Simulado

No trecho “O estudo não considera apenas a temperatura, mas também a umidade”, a conjunção “mas” estabelece uma relação de oposição entre as ideias apresentadas.

Na verdade, o que se tem é a construção “mas também”, o que se classifica como uma conjunção aditiva, por isso o gabarito está errado.

119. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEAP - BA - Policial Penal Pós-Edital - 2024 - 2º Simulado
O conectivo destacado nas frases a seguir que tem seu valor semântico corretamente indicado é:

A.O padre realizou um bom trabalho, [yellow]porém [reset]foi excomungado. / conclusão
B.Aprendemos muito, [yellow]enquanto [reset]lemos livros. / proporção
C.O projeto não foi aprovado, [yellow]ainda que [reset]tivesse apresentado nobres objetivos. / concessão
D.Estude muito, [yellow]se[reset] quiser ser aprovado. / causa
E.O sanador agiu mais rápido [yellow]do que[reset] o deputado: escondeu tudo na cueca. / tempo

Item A:
A conjunção 'porém' exprime adversidade e esta na classe das conjuções coordenativas adversativas,assim como:
[yellow]mas, porém, contudo, entretanto, no entanto, todavia, não obstante, senão(= mas sim), só que, ainda assim, e[reset]

Item B:
A conjunção 'enquanto' é conjução subordinada temporal:
[yellow]quando, mal, logo que, assim que, sempre que, depois que, desde que, enquanto, apenas, até que,mal, antes que, sempre que[reset]

Item C:
'ainda que' expressa concessão, alternativa C a correta. Conjunções subordinada concessiva:
[yellow]embora, conquanto, malgrado, ainda que, mesmo que, posto que, apesar de que, se bem que, não obstante, por mais que, por pior que, [reset]
a despeito de,malgrado, em que pese[reset]

Item D:
A conjunção 'se' exprime condição. é subordinada condicional:
[yellow]se, caso, desde que, contanto que, salvo se, exceto se, sem que(=se não), a não ser que.[reset]

Item E:
A conjunção 'mais...(do que)'é subordinada comparativa:
[yellow]tão...como/quanto, mais...(do)que,menos...(do)que, assim como, tal qual, tal como, assim como,como,tanto...quanto[reset]


120. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TCE PA - Auditor de Controle Externo - Área Fiscalização - Especialidade: Ciências Atuariais - 2024 
Assinale a opção em que a frase inicial, introduzida pela conjunção “se”, não apresenta valor de condição.

A. Se a voz do povo é a voz de Deus, começo a pressupor que Deus é um sujeito muito calado.
B. Se os homens são tão maus com o auxílio da religião, como seriam sem ela?
C. Se os homens tivessem verdadeiramente convicção de sua fé, seriam todos santos.
D. Se quiserdes saber o que Deus pensa do dinheiro, é só olhar a quem Ele o dá.
E. Se existe Deus, por que há coisas como a fome e os horários políticos na televisão?

Item: A) 
Análise: No item A, a frase 'Se a voz do povo é a voz de Deus, começo a pressupor que Deus é um sujeito muito calado.' apresenta uma condição hipotética. 
A conjunção 'se' introduz uma condição para a conclusão que se segue. Portanto, este item está de acordo com o valor condicional da conjunção 'se'.

Item: B) 
Análise: No item B, a frase 'Se os homens são tão maus com o auxílio da religião, como seriam sem ela?' 
utiliza a conjunção 'se' para introduzir uma condição hipotética. 
No entanto, a frase está mais próxima de uma reflexão ou questionamento retórico sobre a natureza humana, não estabelecendo uma condição real. 
Portanto, este item está de acordo com o gabarito da banca, pois 'se' não apresenta valor de condição.

Item: C) 
Análise: No item C, a frase 'Se os homens tivessem verdadeiramente convicção de sua fé, seriam todos santos.' apresenta uma condição hipotética. 
A conjunção 'se' introduz uma condição para a conclusão que se segue. Portanto, este item está de acordo com o valor condicional da conjunção 'se'.

Item: D) 
Análise: No item D, a frase 'Se quiserdes saber o que Deus pensa do dinheiro, é só olhar a quem Ele o dá.' apresenta uma condição hipotética. 
A conjunção 'se' introduz uma condição para a conclusão que se segue. Portanto, este item está de acordo com o valor condicional da conjunção 'se'.

Item: E) 
Análise: No item E, a frase 'Se existe Deus, por que há coisas como a fome e os horários políticos na televisão?' 
apresenta uma condição hipotética. A conjunção 'se' introduz uma condição para a reflexão que se segue. 
Portanto, este item está de acordo com o valor condicional da conjunção 'se'.

121. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - SEFAZ AC - Auditor da Receita Estadual Pós-Edital - 2024 - 1º Simulado

“As organizações estão presentes não somente no território nacional, [yellow]mas também[reset] fora do país.

No último parágrafo do texto, a conjunção “mas também” expressa valor semântico de:

A. finalidade.
B. oposição.
C. proporcionalidade.
D. adição.
E. causa.

122. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPE TO - Técnico Ministerial - Área: Técnico de Contabilidade - 2024 

Julgue os itens que se seguem, relativos a aspectos linguísticos do texto CG2A1.

Ainda assim, nem tudo é um mar de rosas. [yellow]Conforme[reset] as mulheres vão progredindo na carreira acadêmica, por exemplo, esse cenário muda. 

O vocábulo “Conforme” introduz, no segundo período do quinto parágrafo, uma oração que expressa, em relação à oração subsequente, circunstância de conformidade.

ERRADO - Cuidado com a pegadinha da banca, expressa proporcao. Poderia ser substituida por " À proporção que, ao passo que, à medida que, à proporção que.''
Indicando simultaneidade na ocorrência dos fatos. São as conjunções subordinadas proporcionais.

123. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ANATEL - Cargo 2 – Ciência de Dados - Pós-Edital - 2024 - 1º Simulado

Implicam sempre com a Light, mas creio que essa poderosa companhia é simplesmente pseudônimo de uma outra que tem um nome alemão

Na linha 3, a conjunção “mas” poderá ser alterada por qualquer uma das seguintes: porém, contudo, todavia e conquanto.

ERRADO - CUIDADO COM A PEGADINHA
A conjunção “mas” indica uma adversidade, assim como “porém”, “contudo” e “todavia”. 
Já a conjunção “conquanto” se trata de um valor concessivo. Por isso, o item está errado.

124. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de Macaé - Assistente Técnico de Informática - 2024 

Entre os segmentos de cada opção abaixo há um conector. Assinale a frase em que o sentido desse conector é corretamente expresso.

A. Ande com um caderninho na bolsa / e anote tudo – oposição.
B. Anote tudo o que gasta / para saber para onde está indo seu dinheiro – finalidade.
C. Deixe em casa cartões de crédito / e cheques – alternância.
D. Só compre pela internet ou por telefone / se for algo necessário – modo.
E. Estabeleça um limite em dinheiro / para carregar na carteira – lugar.

O sentido nas questões é o seguinte:

A- aditivo;  conjunção 'e'
B- finalidade (para+ verbo no infinitivo);
C- aditivo; 'cojunção 'e'
D- condicional; conjunção 'se'
E- finalidade. 'para'

125.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TJ AL - Técnico Judiciário - Área Judiciária Pós-Edital - 2024 - 2º Simulado

Releia o trecho do texto:

Mas ela morrerá um dia sem jamais ter ouvido essa extraordinária declaração, [yellow]pois[reset] entrou no ônibus e se foi, sem olhar para trás.

No contexto em que se encontra, o elemento sublinhado expressa ideia de:

A. concessão.
B. causa.
C. consequência.
D. condição.
E. comparação.

Contextualmente, o vocábulo “pois” indica um valor causal, já que podemos identificar uma ideia causa e consequência. Letra 'B'

126. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - BACEN - Analista - Área: Tecnologia da Informação - 2024

"A Conferência considera que as tecnologias de IA podem ser de grande utilidade para a humanidade e podem beneficiar todos os países, 
mas também suscitam questões éticas fundamentais,..."

No primeiro período do segundo parágrafo, a expressão “mas também” caracteriza-se como elemento de conexão entre orações no qual a conjunção “mas” expressa sentido aditivo.

ERRADO -A expressão "mas também" no texto funciona como um elemento de conexão, mas a conjunção "mas" não expressa sentido aditivo. 
Na verdade, a conjunção "mas" expressa sentido adversativo, indicando uma oposição ou contraste.
No caso do texto, a adversidade está no fato de que, apesar de as tecnologias de IA serem úteis e benéficas, 
elas também levantam questões éticas importantes. A parte "também" adiciona uma ideia nova, 
mas o "mas" continua com a função de introduzir uma ideia que contrasta com a anterior.
Portanto, a conjunção "mas" não expressa sentido aditivo, e sim adversativo.

Para que o "mas" fosse aditivo, necessário seria que houvesse na oração anterior a expressão "não apenas" ou alguma expressão correlata. 
Por exemplo: ele não apenas joga bola pela manhã, mas também se dedica aos estudos.

127. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de São Lourenço da Mata - Professor de Anos Iniciais - 2024
Leia o texto apresentado e as afirmações sobre os termos nele destacados.

Neste ano, o Festival de Inverno de Garanhuns (FIG) é realizado pela Prefeitura de Garanhuns, com patrocínios do Governo de Pernambuco, por meio da Empetur, 
e do Ministério do Turismo. As ações de literatura acontecem em novo endereço: no Parque Luiz Carlos de Oliveira, [yellow]que[reset] receberá o “Espaço da Palavra”, 
antes chamado de “Praça da Palavra”, [yellow]pois[reset] ficava na praça da fonte luminosa. [yellow]Também[reset] muda de endereço a Casa Galeria Galpão, com exposições fotográficas, 
artes visuais e ações de gastronomia, agora instaladas na Escola Municipal Padre Agobar Valença.

Folha de Pernambuco. Agreste: começa hoje o 32º FIG. Folha de Pernambuco. Caderno Cultura, p. 13, 11 jul. 2024. Adaptado.

Analisando o uso dos elementos destacados, conclui-se que

I. o termo “que” funciona como pronome relativo, referindo-se a “Parque Luiz Carlos de Oliveira”.
II. o termo “pois” tem função adversativa, uma vez que marca uma relação de oposição e contraste entre as informações que ele articula.
III. o termo “Também” tem função aditiva, já que adiciona uma informação semelhante a outra apresentada anteriormente.

É verdadeiro o que se afirma em

A. I e II, apenas.
B. II, apenas.
C. I e III, apenas.
D. II e III, apenas.
E. III, apenas.

Somente o Item II está errado, a conjunção 'pois' é explicativa, muitas das vezes podendo ser causal.
Portanto, gabarito letra 'C'.

128. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TCE PA - Auxiliar de Controle Externo Pós-Edital - 2024 - 1º Simulado
Os marcadores textuais possuem função de indicar relações significativas entre trechos de um texto.


Um marcador textual possui função corretamente indicada em:

A. [yellow]Acerca dos casos de violência doméstica,[reset] os aspectos culturais exercem forte influência. / iniciar um novo tópico
B. [yellow]Inicialmente[reset], cabe destacar o papel disruptivo da IA. / marcar distinções entre elementos de um texto
C. [yellow]Para ser mais claro[reset], é preciso escolher palavras de significado trivial. / retificar um erro
D. [yellow]Outrossim[reset], faz-se mister também incluir práticas de auditoria preliminar. / colocar ideias em oposição
E. [yellow]Porquanto[reset] seja ainda incipiente, o funcionário pode cometer falhas. / inserir conclusão

A) Errada. O marcador sublinhado apenas situa um referente para a frase que lemos após a vírgula. Não marca início de um novo tópico. 
Esse marcador sublinhado tende a funcionar como retomada de ideia já mencionada, para agora trazer mais explicações e detalhes no desenvolvimento de um mesmo tópico.

(B) Certa. A palavra “inicialmente” pressupõe que vai aparecer depois algum outro tópico do texto que precisou ser separado possivelmente para marcar 
distinção entre os pontos abordados.

(C) Errada. O marcador sublinhado anuncia uma finalidade do que lemos na frase a seguir: a finalidade de “escolher palavras de significado trivial” 
é “para ser mais claro”. Não se trata de retificar (corrigir) um erro.

(D) Errada. A palavra “outrossim” significa “igualmente, do mesmo modo”. Serve para marcar continuação de pensamento em analogia com ideia anterior. 
Não significa ideias em oposição.

(E) Errada. A palavra “porquanto” é uma conjunção que podemos empregar com sentido de causa ou de explicação. 
Não se trata de inserir conclusão. Para inserir conclusão, existe uma palavra semelhante na escrita: portanto. Atenção!


129. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TCE PA - Auxiliar de Controle Externo Pós-Edital - 2024 - 1º Simulado

Um cartaz fixado no estacionamento de um shopping alertava:

Não nos responsabilizamos pelos veículos estacionados neste local, nem por furtos, colisões ou objetos deixados nos mesmos.

Assinale o comentário adequado sobre esse cartaz.

A. A administração do shopping se responsabiliza pelos veículos estacionados em outros shoppings.
B. A responsabilidade pelos veículos estacionados nesse shopping é exclusiva dos clientes.
C. Para ficar adequado à norma culta, seria preciso trocar “neste” por “nesse”.
D. O pronome demonstrativo “mesmos” ocorreu com emprego considerado vicioso, segundo a norma culta.
E. A conjunção “nem” estabeleceu oposição entre os trechos que conectou.

(A) Errada. O aviso contido no cartaz se limita a informar que naquele local, naquela parte do estacionamento onde está o cartaz, 
o shopping não se responsabiliza pelos veículos ali deixados. Isso não significa que o shopping vai se responsabilizar por veículos deixados em outros shoppings. 
Temos aqui uma extrapolação.

(B) Errada. Não se pode afirmar nem deduzir que a responsabilidade é exclusiva dos clientes. 
Outros responsáveis podem existir: a seguradora do veículo, por exemplo. 
Além disso, nem todo cliente possui veículo próprio. Então não podemos deduzir que os clientes em geral são responsáveis pelos veículos deixados no estacionamento do shopping.

(C) Errada. O emprego de “neste” está correto. Não deve ser trocado por “nesse”. O aviso contido no cartaz se referia ao mesmo local (estacionamento) 
onde estava fixado o cartaz. Segundo a norma gramatical, devemos empregar pronome demonstrativo “este, esta” para fazer referência ao próprio local onde já estamos. 
Já o pronome demonstrativo “esse, essa” será empregado para referência ao local onde está alguém distante para quem estamos dizendo algo.

(D) Certa. Conforme o rigor da norma gramatical, o pronome demonstrativo “mesmo” deve ser empregado apenas para acompanhar substantivos 
(o mesmo banco, a mesma praça...). Não deve ser empregado para substituir palavra: Leu o livro e resumiu o mesmo (errado); 
Leu o livro e resumiu-o (certo). Na frase do cartaz em questão, a palavra “veículos” foi substituída por “os mesmos” ao final da frase. 
Correção: ...ou objetos deixados neles.

(E) Errada. A conjunção “nem” é aditiva. Serve para adicionar uma negação para outra negação já feita antes. 
A frase do cartaz já começa negativa: Não nos responsabilizamos... Então a conjunção “nem” somou outra negação: nem por furtos...

130. Ano: 2024 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TJ AL - Técnico Judiciário - Área Judiciária Pós-Edital - 2024 - 1º Simulado

Em “enquanto dormia em um posto de gasolina” (l. 4-5), a conjunção destacada veicula a relação de:

A. causa.
B. concessão.
C. proporção.
D. conformidade.
E. tempo.

Letra e.

Assunto abordado: Processos de coordenação e subordinação.

A expressão “enquanto” significa uma ideia de tempo simultâneo.

d. Conjunções Subordinativas Temporais: indicam em que tempo ocorreu o fato expresso na oração principal:
[yellow]quando, mal, logo que, assim que, sempre que, depois que, desde que, enquanto, apenas, até que,mal, antes que, sempre que[reset]

131. Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 20 - Técnico Administrativo - Área Administrativa - 2024

Considerando o período em que ocorre no texto, o termo “que” é utilizado como conjunção em:

A. que as recordações começam a falhar.
B. que aconteceu comigo até o dia de minha partida.
C. em que vivo há mais de cinquenta anos.
D. que povoaram minha infância e adolescência.
E. que presenciei ou ouvi.

Item A:
"Há algum tempo venho percebendo que as recordações começam a falhar " 
DICA para achar a Conjunção Integrante > Troca o Trecho em negrito por ISSO.
ha algum tempo venho percebendo ISSO

"que": Conjunção integrante, introduzindo a oração subordinada. uma vez que se relaciona com o VERBO (percebendo isso).

Item B:

Paripiranga, decidi escrever [yellow]o que[reset] aconteceu comigo até o dia de minha partida.
o": Pronome demonstrativo (ou artigo em algumas gramáticas), usado para antecipar e substantivar o termo "que".
"que": Pronome relativo, que retoma e introduz a oração subordinada adjetiva restritiva.

Item C:
"Aqui, na cidade de Paris, em que vivo há mais de cinquenta anos"

"em que vivo há mais de cinquenta anos": Oração subordinada adjetiva explicativa.
"em que": Pronome relativo, função de adjunto adverbial de lugar.

Item D:
"tomei coragem para reviver as histórias que povoaram minha infância e adolescência. "
"que": Pronome relativo, sujeito da oração subordinada, retomando "histórias".

Item E:
"cansei de esperar o surto de genialidade e resolvi simplesmente contar alguns fatos que presenciei ou ouvi."
"que": Pronome relativo, sujeito da oração subordinada, retomando "fatos".

132. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPE TO - Analista Ministerial - Área Letras - 2024

Não negueis jamais ao erário, à administração, à União os seus direitos. São tão invioláveis, como quaisquer outros. 
O direito dos mais miseráveis dos homens, o direito do mendigo, do escravo,...

Estaria mantida a coerência de sentido do primeiro parágrafo caso o seu terceiro período fosse introduzido por elemento coesivo de contraste, 
como contudo, por exemplo — Contudo o direito (...).

CERTO, estaria mantida a coerêcia. O sentido mudaria, o texto antes da conjunção adversativa nos traz ideias que não são contrárias.

133. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TRF 1 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 6º Simulado

Assinale a alternativa que aponta para a classe das palavras destacadas no trecho
 “Ao todo, serão onze disciplinas [yellow]e[reset] o trabalho de conclusão de curso, [yellow]que[reset] juntos somarão 360 horas/aula.”.

A. Conjunção.
B. Pronome.
C. Advérbio.
D. Substantivo.
E. Adjetivo.

Conjunção é o termo que serve de ligação entre orações ou palavras de mesma função sintática, estabelecendo relação de coordenação ou de subordinação entre elas.

134. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de São Lourenço da Mata - Professor de Anos Iniciais - 2024

(1) “E como, [yellow]à medida que[reset] ele faz isso, ao longo da nossa história enquanto espécie, o cérebro humano criou abstrações mentais que se transformaram literalmente na infraestrutura, 
na base mental da civilização humana”.

(2) “Esse é o primeiro campus do planeta [yellow]onde[reset] todas as atividades foram planejadas, centradas na mente humana, há uma escola de educação científica, clínica.”

As expressões em destaque exprimem ideias relacionadas, respectivamente, a:

A. concessão e lugar.
B. comparação e explicação.
C. causalidade e tempo.
D. explicação e lugar.
E. proporção e lugar.

'onde' é lugar. Eliminando a alternativa 'B' e 'C'.

'à medida que'= Proporção
'Na medida que' = Causa

Alternativa 'E'

135. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ITAIPU Binacional - Relações Públicas - 2024 

No texto CB2A1, a conjunção “Embora”, empregada no início do último parágrafo, poderia, sem prejuízo dos sentidos originais do texto ou de sua correção gramatical, 
ser substituída por:

A. Para que.
B. Ainda que.
C. Apesar de.
D. Porque.
E. Desde que.

"Embora seja uma energia limpa e renovável..."

A) 'para que' -> final

B) 'ainda que' -> Concessiva

C) Consecutiva -> 'apesar de'

D) Explicativa ou Causal - 'porque'

E) Condicional - 'desde que'

1. CONCESSIVAS → ideia contrária que não impede a realização da outra oração. Traz o verbo sempre no subjuntivo. (concessão é uma exceção) 2. embora;

3. conquanto;

4. ainda que;

5. mesmo que;

6. se bem que;

7. posto que.

"Apesar de" também é uma conjunção concessiva, porém, sua substituição poderia ocasionar prejuízo gramatical. Ficaria assim: "Apesar de seja uma energia limpa...".

136. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ITAIPU Binacional - Jornalista - 2024 

No quinto período do primeiro parágrafo do texto CB2A1, a palavra “ainda” expressa uma ideia de

A. tempo.
B. adição.
C. contraste.
D. conclusão.
E. condição.

"Uma expansão em curso, ainda sem data para entrar em operação, ..."

'ainda' traz ideia de tempo.

Exemplos de como a palavra "ainda" pode ser usada para expressar tempo:


A obra ainda não foi concluída.

Ele ainda não chegou.

Eu ainda não terminei o meu trabalho.

137. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEDUC TO - Conhecimentos Básicos para Todos os Cargos - Pós-Edital - 2023 - 1º Simulado

Assinale a alternativa que corretamente apresenta o significado do conector indicado.

A. porquanto / explicativo.
B. conquanto / conformativo.
C. contanto que / concessivo.
D. conforme / comparativo.
E. portanto / consecutivo.

(A) Certa. O conectivo “porquanto” tem valor explicativo.

(B) Errada. O conectivo “conquanto” tem valor concessivo.

(C) Errada. O conectivo “contanto que” tem valor condicional.

(D) Errada. O conectivo “conforme” tem valor conformativo.

(E) Errada. O conectivo “portanto” tem valor conclusivo.

138. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - ALE MA - Técnico de Gestão Administrativa - Área: Enfermeiro Pós-Edital - 2023 - 1º Simulado 
A delegacia de polícia de uma cidade promoveu a seguinte campanha publicitária:

“Não se cale. Você pode salvar uma vida”.

Se reescrevêssemos esta frase substituindo o ponto entre os períodos por uma conjunção, a opção adequada seria

A. posto que.
B. porquanto.
C. conquanto.
D. apesar de que.
E. enquanto.

Há um nexo explicativo entre as orações. Sempre que houver um verbo no imperativo, a oração seguinte apresentará uma ideia explicativa. 
Como a conjunção “porquanto” indica explicação, a resposta correta é a letra B.

Recomendo que tenha acesso a uma tabela de conjunções para você internalizar todas.

139. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TJ AP - Técnico Judiciário - Área Judiciária e Administrativa Pós-Edital - 2023 - 1º Simulado
Nas frases a seguir, empregou-se a conjunção porque. A opção que, suprimindo-se esse conectivo, mantém necessariamente o sentido original é:

A. Manuel não visitou a amiga porque estava gripado. / Manuel não visitou a amiga por sua gripe.
B. Coralina acelerou o passo porque a rua estava escura. / Coralina acelerou o passo pela escuridão da rua.
C. Eles adiaram a viagem porque a previsão era de tempestade. / Eles adiaram a viagem pela previsão de tempestade.
D. A construção foi adiantada porque havia muitos ajudantes. / A construção foi adiantada por muitos ajudantes.
E. Os filhos fizeram muitas preces porque seus pais estavam bem. / Os filhos fizeram muitas preces pelo bem de seus pais.

Assunto abordado: Organização sintática das frases

(A) Errada. Na frase original, a razão para Manuel não visitar a amiga é explicitamente seu estado de gripe. 
Na reescrita, o pronome “sua” provoca ambiguidade, sendo possível entender que Manuel não visitou a amiga porque ela estava gripada.

(B) Errada. Na frase original, a ação de Coralina é uma reação direta à escuridão da rua. 
A reescrita permite entender que Coralina atravessou a rua escura correndo.

(C) Certa. A frase original e a reescrita indicam que a razão pela qual eles adiaram a viagem é a previsão de tempestade.

(D) Errada. Na frase original, a construção foi adiantada porque havia muitos ajudantes. Na reescrita, entende-se que são os ajudantes que adiantam a construção.

(E) Errada. Na frase original, os filhos fizeram muitas preces porque seus pais já estavam bem. 
Na reescrita, eles fizeram muitas preces para alcançar o bem de seus pais.

140. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEDUC TO - Conhecimentos Básicos para todos os Cargos - Pós-Edital - 2023 - 1º Simulado

Assinale a opção que apresenta o conector que tem seu significado corretamente indicado.

A. mesmo que / concessão.
B. e / finalidade.
C. mas / conclusão.
D. como / proporção.
E. para / conformação.

(A) Certa. O conector “mesmo” indica concessão, em seu uso associado ao “que”, conforme o contexto em análise.

(B) Errada. O conector “e” indica adição, em seu uso padrão.

(C) Errada. O conector “mas” indica adversidade.

(D) Errada. O conector “como” indica conformidade.

(E) Errada. O conector “para” indica finalidade.

141. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - POLC AL - Perito Criminal - Área Biomedicina - 2023

A obrigatoriedade do fornecimento do DNA e a submissão daqueles ainda não condenados e em liberdade condicional à entrega de seu material 
genético foram assuntos bastante discutidos no cenário estadunidense. A grande abrangência dos crimes que autorizam a extração do DNA assim 
como a permanência da informação por tempo indeterminado no índice também são questões controversas. O foco é a privacidade e a intimidade do indivíduo.

A coerência do primeiro parágrafo do texto seria mantida caso o segundo e o terceiro períodos fossem unidos em um só, 
empregando-se, entre eles, a conjunção portanto, da seguinte forma: 
A grande abrangência dos crimes que autorizam a extração do DNA assim como a permanência da informação por tempo indeterminado no índice 
também são questões controversas, [yellow]portanto[reset] o foco é a privacidade e a intimidade do indivíduo.

Portanto é uma conjunção conclusiva, não sendo coerente o seu emprego no período acima.
Resumindo, o terceiro período contradiz o segundo. Então não cabe o uso dessa conjunção.
porQUANTO que é uma conjunção explicativa. PorTANTO é conclusiva.

142. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPE SC - Promotor de Justiça Substituto - Tarde - 2023

"O justo é um saber que se vai constituindo à medida que nossa consciência da história se aguça."

No segundo período do primeiro parágrafo, a locução conjuntiva “à medida que” denota proporcionalidade entre duas situações.

A conjunção proporcional "À medida que" é equivalente a "à proporção que", "ao passo que", "quanto mais...menos"



"À MEDIDA QUE" NÃO É EQUIVALENTE A "CONFORME".

"À MEDIDA QUE" NÃO É EQUIVALENTE A "NA MEDIDA EM QUE"



À medida que = conjunção proporcional ("à proporção que", "ao passo que", "quanto mais...menos")

Conforme = conjunção conformativa ("de acordo com", "segundo", "consoante")

Na medida em que = conjunção causal ("visto que", "já que", "porquanto", "desde que")

143.Ano: 2023 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TSE - Técnico Judiciário - Área: Administrativa Pós-Edital - 2023 - 2º Simulado 

Em um texto, existem vários mecanismos de coesão: pronomes, conjunções, elipses, sinônimos. Alguns desses conectores são anafóricos – retomam um termo ou passagem anterior –, outros são catafóricos – antecipam termo ou passagem. Assim sendo, leia atentamente os fragmentos abaixo retirados do texto de Saramago. Marque a alternativa em que o termo destacado tem a classificação e o elemento do texto a que se refere corretos.

A. “Quando esta guerra acabar, e não tarda, que já [yellow]a[reset] estamos vendo em seus derradeiros e fatais estertores...” (l.1 ) – pronome oblíquo que se refere ao termo “esta guerra” (l.1).
B. “...a contagem final dos que nela perderam a vida, [yellow]uns[reset] tantos aqui, [yellow]uns[reset] tantos além, [yellow]uns[reset] mais perto, outros mais longe...” (ls.1 e 2) – numerais que retomam “dos” (daqueles que perderam a vida).
C. “...o país que há-de chamar-se Portugal, [yellow]cuja[reset] dimensão, na sua periferia, anda mais ou menos por aí” (ls.10 e 11) – pronome indefinido que antecipa o vocábulo “periferia” (ls.11 e 12)
D. “...se sobre os cabelos, [yellow]que[reset] antes eram arrancados” (ls.9 e 11) – conjunção integrante que apenas conecta orações.

(A) Certa. Nessa passagem, o elemento em destaque é um pronome pessoal do caso oblíquo com valor substantivo, isto é, substitui um termo ou expressão já mencionados. Tem caráter anafórico e substitui o termo “esta guerra”.


(B) Errada. Os termos destacados são pronomes indefinidos e se referem ao vocábulo “dos” (l.2).


(C) Errada. O termo em destaque é pronome relativo, sempre de caráter anafórico, e retoma o vocábulo “Portugal”.


(D) Errada. Na passagem, o conectivo QUE é um pronome relativo e retoma o antecedente “cabelos”.

144. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Câmara dos Deputados - Analista Legislativo - Atribuição - Técnica Legislativa Conhecimentos Gerais - Pós-edital - 2023 - 2º Simulado
Com fortes dores de cabeça, João Cabral de Melo Neto recebeu do médico a recomendação de praticar atividades físicas. Escolheu a prensa manual como exercício para publicar livros. Foi assim que vieram a público autores como Manuel Bandeira, Cecília Meireles, Vinícius de Moraes. Cabral não ficou curado da dor de cabeça, mas valeu. (Texto autoral produzido para este simulado.) A conjunção “mas” foi empregada na última frase do texto. Seu valor contextual ocorre igualmente, de modo mais adequado, em:

A. Cabral não chegou tão cedo às Índias, mas no caminho descobriu o Brasil.
B. Cabral sabia navegar bem, mas desviou-se da rota por algum motivo.
C. João Cabral enxergava pouco na velhice, mas continuava produtivo.
D. A história registra que os gregos derrotaram os persas, mas sucumbiram ao domínio de Alexandre.
E. Projetos podem ser aprovados por maioria absoluta na Câmara, mas ser reprovados no Senado.


Assunto abordado: Marcas de textualidade. Interpretação e compreensão.

No texto dado, o poeta João Cabral seguiu um conselho médico de exercitar-se, e fez uma escolha pouco comum: decidiu prensar manualmente seus livros como 
forma de atividade física. O objetivo era aplacar uma dor de cabeça. A dor de cabeça não ficou curada com essa atividade física. 
Em compensação, no lugar da cura pretendida, nós fomos presenteados com obras poéticas. 
Então, esse texto, a conjunção “mas” teve valor contextual de compensação. Não existe oposição entre “não ficou curado”, de um lado, e, de outro lado, “mas valeu”.

(A) Certa. Aqui também não existe oposição entre “Cabral não chegou tão cedo às índias”, de um lado, e, de outro lado, 
“no caminho descobriu o Brasil”. O que existe aqui é uma compensação: algo que se pretendia não foi alcançado, e outra coisa foi obtida no lugar (compensação). 
Atenção: compensação ocorre após situação negativa (não chegou tão cedo).

(B) Errada. Não é compensação. Trata-se de uma quebra da expectativa após uma frase de teor positivo (sabia navegar bem). 
A expectativa era boa a partir da informação de que Cabral sabia navegar bem. O desvio da rota quebra a expectativa inicial de algo positivo na segunda parte da frase.

(C) Errada. Não é compensação. Existe um contraste (diferença) entre a expectativa gerada por “enxergava pouco na velhice” e o fato de que “continuava produtivo”. 
Cuidado: não era algo pretendido de início que não foi alcançado, e depois se obteve algo que compensasse.

(D) Errada. Não é compensação. Existe mesmo oposição entre “derrotaram” e “sucumbiram”. São sentidos opostos.

(E) Errada. Não é compensação. Existe mesmo oposição entre “aprovados” e “reprovados”. São sentidos opostos.

145. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - ALE MA - Técnico de Gestão Administrativa - Área: Enfermeiro Pós-Edital - 2023 - 2º Simulado 
Observe a frase

“O padre foi excomungado, [yellow]conquanto[reset] tivesse realizado um bom trabalho”.

A oração grifada traz uma ideia de:

A. Causa.
B. Consequência.
C. Condição.
D. Conformidade.
E. Concessão.

A conjunção “conquanto” indica uma ideia concessiva, assim como as conectores: 
embora, mesmo que, ainda que, por mais que, se bem que, posto que, malgrado, apesar de que.

146. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TSE - Técnico Judiciário - Área: Administrativa Pré-Edital - 2023 - 10º Simulado
Assinale a frase em que o vocábulo quando apresenta mais de um valor semântico.

A. Estarei pronto quando você chegar esta tarde à minha bela cidade.
B. Agia como se soubesse de tudo, quando na verdade estava desinformado.
C. Só acredita em fogo quando vê fumaça saindo bem perto de onde está.
D. Perguntaram quando chegariam os tão prometidos investimentos em educação.
E. Perguntavam todos os detalhes do incidente, quando chegou o delegado.

(A) Errada. Na frase, “quando” tem valor temporal, referindo-se ao momento em que uma pessoa chegará.

(B) Errada. Na frase, “quando” tem valor de contraste, marcando a oposição entre agir como se soubesse de tudo e estar desinformado.

(C) Certa. Na frase, “quando” tem valor condicional, estabelece a condição sob a qual a pessoa acredita em fogo. 
Mas também tem um valor temporal, referindo- -se ao momento específico em que a pessoa acredita em fumaça.

(D) Errada. Na frase, “quando” tem valor temporal, referindo-se ao tempo em que os investimentos chegarão.

(E) Errada. Na frase, “quando” tem valor temporal, referindo-se ao tempo em que o delegado chegou.

147. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEDUC TO - Professor da Educação Básica - Área: Letras Português - Redação - 2023
Assinale a opção em que a conjunção e está empregada com valor aditivo.

A. Seu horóscopo: você é facilmente influenciado pelo que lê e tem a capacidade de relacionar sentenças vagas à sua existência.
B. Eu tinha seis teorias sobre o modo de educar crianças. Agora tenho seis filhos e nenhuma teoria.
C. Criatividade é se permitir cometer erros e arte é saber quais deles manter.
D. Aplauso é um recibo e não uma conta.
E. Livros trazem a vantagem de podermos estar sós e acompanhados.

A. Correta. De acordo com o posicionamento desta professora, no caso analisado, a conjunção coordenativa ''e'' tem valor aditivo, 
pois introduz segmento que possui ideia de acréscimo/adição em relação ao anterior.

B. Incorreta. De acordo com o posicionamento desta professora, no caso analisado, a conjunção coordenativa ''e'' tem valor adversativo, 
pois introduz segmento que possui ideia de oposição em relação ao anterior.

C. Incorreta. De acordo com o posicionamento desta professora, no caso analisado, a conjunção coordenativa ''e'' tem valor adversativo, 
pois introduz segmento que possui ideia de oposição em relação ao anterior.

D. Incorreta. De acordo com o posicionamento desta professora, no caso analisado, a conjunção coordenativa ''e'' tem valor adversativo, 
pois introduz segmento que possui ideia de oposição em relação ao anterior.

E. Incorreta. De acordo com o posicionamento desta professora, no caso analisado, a conjunção coordenativa ''e'' tem valor adversativo, 
pois introduz segmento que possui ideia de oposição em relação ao anterior.


148. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Câmara de São Paulo - Técnico Legislativo Pós-Edital - 2023 - 1º Simulado

Se reescrevêssemos a frase “Cuide de sua casa, juntos somos mais fortes”, acrescentando uma conjunção, a opção adequada seria:

A. portanto.
B. conquanto.
C. porquanto.
D. contanto que.
E. entretanto.

Há um nexo explicativo entre as orações. Sempre que houver um verbo no imperativo, a oração seguinte apresentará uma ideia explicativa. 

Como a conjunção “porquanto” indica explicação, a resposta correta é a letra C

149. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE / Prova: CESPE/CEBRASPE - FNDE - Especialista em Financiamento - 2023

Segundo dados da Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua, 2022), 18,3% dos jovens de 14 a 29 anos não concluíram alguma 
das etapas da educação básica seja por abandono, seja por nunca terem frequentado a escola.

No primeiro período do texto, a expressão “seja...seja” é empregada para coordenar, com sentido alternativo, duas causas atribuídas ao fato de jovens de 14 a 29 anos 
não concluírem alguma das etapas da educação básica.

CERTO

Conjunções coordernativas alternativas: ou, ou...ou, ora...ora, já...já, quer...quer, seja...seja 
Ex: ou mude seu comportamento, ou mude-se daqui. Ora ele estuda para a Polícia Civil de Pernambuco, ora ele se prepara para a polícia penal do Ceará.

150. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TCDF - Analista Administrativo - Área Controle Externo - Pós-Edital - 2023 - 3º Simulado 

Basta lembrar que as guerras religiosas foram guerras de ideias, assim como todas as revoluções, para sentir [yellow]como[reset] as ideias adquiriram poder desde a época dos gregos

No terceiro período do texto, o vocábulo “como” (segunda ocorrência) é morfologicamente uma conjunção subordinativa, porquanto introduz oração subordinada.

E - Errado

 o vocábulo “como” é um advérbio interrogativo de modo, empregado em uma interrogação indireta. 
Inicia a oração subordinada substantiva objetiva direta “como as ideias adquiriram poder desde a época dos gregos”. 
Note-se que as orações subordinadas substantivas podem ser introduzidas tanto por conjunções subordinativas integrantes quanto por pronomes ou advérbios interrogativos.

151.Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - PM SC - Soldado Pós-Edital - 2023 - 1º Simulado

Observe os trechos a seguir.

“...[yellow]cuja[reset] tarefa é sempre abrigar e proteger alguma coisa, – a criança [yellow]contra[reset] o mundo, o mundo contra a criança, o novo contra o [yellow]velho...[reset]” (l.3-5)

“...aceitando o mundo [yellow]como[reset] ele é, procurando somente preservar o status quo...” (l.11-12)

“...são mais ou menos verídicas para [yellow]cada[reset] nova geração...” (l.19-20)

“...porém, é [yellow]que[reset] tudo destruímos...” (l.36)

No texto, as palavras sublinhadas pertencem, respectivamente, às classes de palavras:

A. pronome pessoal, preposição, adjetivo, conjunção, pronome indefinido, pronome relativo.
B. pronome demonstrativo, advérbio, pronome, advérbio, pronome relativo, pronome relativo.
C. pronome possessivo, pronome demonstrativo, adjetivo, conjunção, pronome demonstrativo, pronome relativo.
D. pronome indefinido, conjunção, adjetivo, preposição, pronome indefinido, pronome relativo.
E. pronome relativo, preposição, substantivo, advérbio, pronome indefinido, partícula de realce.

Alternativa 'E'

152. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - CNMP - Técnico Área: Apoio Técnico Administrativo - Especialidade: Administração - Pós-Edital - 2023 - 1º Simulado 

A conjunção “quando” (l.20) expressa oposição de ideias no período em que é empregada.

"...representam o Oriente atual, quando, na realidade, a sua ação não é muito extensa nem profunda."

CORRETO - Nesse caso 'quando' assume papel adversativo. 

153.Ano: 2023 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TSE - Analista Judiciário - Área: Administrativa Pré-Edital - 2023 - 8º Simulado 

“O copo destina-se a beber, e flor não é para ser bebida”. A conjunção “e”, nesse trecho, apresenta ideia de:

A. adição.
B. concessão.
C. consequência.
D. adversidade.
E. condição.

O conectivo “e”, em regra, é classificado como aditivo. Entretanto, pode ser, em alguns casos, usado com valor de adversidade ou de consequência.
 No trecho “e flor não é para ser bebida”, o conectivo foi empregado com sentido adversativo (equivalente a “mas”). 
Perceba que há uma oposição entre “beber” e “não é para ser bebida”.

Logo, a resposta correta é a letra D.

154.Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TJ RN - Técnico Judiciário - Área Judiciária Pós-Edital - 2023 - 2º Simulado
Assinale a opção em que o vocábulo “logo” não apresenta valor semântico temporal.

A. As crianças devem fazer os deveres de casa logo, para ficarem livres no fim de semana.
B. Ninguém acreditava que logo o diretor da empresa se envolvera em corrupção.
C. Viajar logo que as férias começam significa aproveitá-las ao máximo.
D. Chegaram à conclusão de que logo estariam atravessando a fronteira entre os dois países.
E. Logo começarão a chover cartas de agradecimento à equipe que salvou a tripulação do navio naufragado.

(A) Errado. O vocábulo “logo” é advérbio de tempo, equivale a “imediatamente”.

(B) Certo. O vocábulo “logo” significa “justamente”, não possui valor semântico temporal.

(C) Errado. O vocábulo “logo” é advérbio de tempo, equivale a “imediatamente”.

(D) Errado. O vocábulo “logo” é advérbio de tempo, equivale a “sem demora”.

(E) Errado. O vocábulo “logo” é advérbio de tempo, equivale a “sem demora”.

155. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TSE - Técnico Judiciário - Área: Administrativa Pós-Edital - 2023 - 4º Simulado 
Em São Paulo, certa vez uma campanha publicitária de prevenção à dengue dizia:

“Cuide de sua casa. Juntos somos mais fortes”.

Uma nova redação para esse trecho, unindo os dois períodos e substituindo o ponto-final entre os períodos por uma conjunção, será a seguinte:

A. Cuide de sua casa, posto que juntos somos mais fortes.
B. Cuide de sua casa, porquanto juntos somos mais fortes.
C. Cuide de sua casa, conquanto juntos somos mais fortes.
D. Cuide de sua casa, apesar de que juntos somos mais fortes.
E. Cuide de sua casa, enquanto juntos somos mais fortes.

Letra b.

Há um nexo explicativo entre as orações. Sempre que houver um verbo no imperativo, a oração seguinte apresentará uma ideia explicativa. 
A forma verbal “cuide” está empregada no imperativo; por isso, a oração seguinte apresenta um valor explicativo. 
Como a conjunção “porquanto” indica a explicação, a resposta correta é a letra (B). 
Recomendo que tenha acesso a uma tabela de conjunções para você internalizar todas.

156. Ano: 2023 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TSE - Analista Judiciário - Área Judiciária Pré-Edital - 2023 - 8º Simulado
Fulano foi a um restaurante da cidade, na medida em que estava com fome.

O termo sublinhado acima introduz uma oração que expressa ideia de:

A. condição.
B. consequência.
C. causa.
D. finalidade.
E. proporção.

A locução conjuntiva “na medida em que” expressa a ideia de causa. Não confunda com “à medida que”, que expressa proporção.

Portanto, o gabarito correto é a letra C.

157. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEFAZ MG - Auditor Fiscal da Receita Estadual - Área Tecnologia da Informação - 2023 
Em todas as opções a seguir há um período composto por dois segmentos separados por um ponto.

Assinale a opção em que o conectivo substitui adequadamente esse ponto.

A. Em época de paz, os filhos enterram os pais. Em épocas de guerra são os pais que enterram os filhos. / quando.
B. Tenho medo de borboletas. Elas têm algo de esquisito, assustador. / conquanto.
C. Às vezes vejo um vulto lá fora, que é a velhice. Ela vê que estou trabalhando tanto que resolve procurar outra pessoa. / portanto.
D. Não é preciso muito para ser um produtor de coelhos. Você coloca um casal numa gaiola e é tudo./ enquanto.
E. No universo tudo procede por vias indiretas. Não existem linhas retas./ pois.

Alternativa (a). Essa não é a nossa alternativa correta, entre os períodos da sentença "Em época de paz, os filhos enterram os pais. 
Em épocas de guerra são os pais que enterram os filhos" podemos identificar um sentido de adversidade, portanto, ficaria inadequado o emprego da conjunção "quando", 
pois essa conjunção indica o sentido de tempo.

Alternativa (b). Essa não é a nossa alternativa correta, entre os períodos da sentença "Tenho medo de borboletas. Elas têm algo de esquisito, assustador" 
não podemos empregar a conjunção "conquanto", porque essa conjunção é uma conjunção subordinativa concessiva, 
Cegalla nos informa que essas conjunções "Iniciam orações que exprimem um fato que se concede, que se admite, em oposição a outro: 
embora, conquanto, que, ainda que, mesmo que, ainda quando, mesmo quando, posto que, por mais que, por muito que, por menos que, se bem que, em que (pese), 
nem que, dado que, sem que (= embora não)". Na sentença em análise vemos uma relação de causa e efeito, o que nos demonstra que seria mais adequada a conjunção "porque".

Alternativa (c). Essa não é a nossa alternativa correta, entre os períodos da sentença "Às vezes vejo um vulto lá fora, que é a velhice. 
Ela vê que estou trabalhando tanto que resolve procurar outra pessoa" vemos que há um sentido de oposição, um sentido que não pode ser iniciado pela conjunção 
"portanto", porque essa conjunção "portanto" está entre as conjunções coordenativas conclusivas.

Alternativa (d). Essa não é a nossa alternativa correta, entre os períodos da sentença "Não é preciso muito para ser um produtor de coelhos. 
Você coloca um casal numa gaiola e é tudo" vemos uma relação de explicação, um sentido que não é indicado pela conjunção "enquanto", 
pois essa conjunção "enquanto" indica o sentido de tempo.

Alternativa (e). Essa é a nossa alternativa correta, entre os períodos da sentença "No universo tudo procede por vias indiretas. 
Não existem linhas retas" vemos que a segunda frase funciona como uma explicação para a informação da primeira frase, esse sentido de explicação pode ser 
iniciado pela conjunção "pois", conjunção que pode ser explicativa. 
Cegalla nos ensina que as conjunções explicativas "Precedem uma explicação, um motivo: que, porque, porquanto, pois (anteposto ao verbo)".

158. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEE MG - Professor de Educação Básica - Área: Língua Portuguesa - 2023
Assinale a frase cujo conectivo sublinhado está corretamente classificado.

A. Não vivemos na plenitude democrática, mas não existe aqui uma ditadura e sim uma situação autoritária. / aditivo.
B. É proibido se apresentar com barba crescida ou por fazer, com cabelos compridos ou despenteados. /conclusivo.
C. Política não é só o bônus, mas também os ônus. / adversativo.
D. Brincar vai ser a ocupação principal do próximo século, pois não haverá trabalho para os homens. / explicativo.

Item: A) 
Análise: O conectivo 'e sim' na frase não é aditivo, mas sim alternativo. Ele é usado para contrapor uma ideia anteriormente expressa, 
apresentando uma alternativa a ela. Portanto, o item A não está de acordo com o gabarito da banca.

Item: B) 
Análise: O conectivo 'ou' na frase não é conclusivo, mas sim alternativo. Ele é usado para apresentar uma alternativa ou opção entre duas ou mais possibilidades. 
Portanto, o item B não está de acordo com o gabarito da banca.

Item: C) 
Análise: O conectivo 'mas também' na frase não é adversativo, mas sim aditivo. Ele é usado para adicionar uma informação à ideia anteriormente expressa. 
Portanto, o item C não está de acordo com o gabarito da banca.

Item: D) 
Análise: O conectivo 'pois' na frase é corretamente classificado como explicativo. Ele é usado para introduzir uma explicação ou causa para a ideia 
anteriormente expressa. Portanto, o item D está de acordo com o gabarito da banca.

159. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - ALE MA - Assistente Legislativo Administrativo - Área: Agente Legislativo - 2023 
Em todas as frases abaixo aparece a conjunção e sublinhada. Assinale a frase em que ela é empregada com valor adversativo.

A. Vida: um espaço de tempo cuja primeira metade é arruinada por nossos pais e a segunda metade, por nossos filhos.
B. Uma casa é feita de tijolo e pedra. Um lar é feito apenas de amor.
C. Esculpir: eu escolho um bloco de mármore e retiro tudo o que não preciso.
D. Arte é fazer alguma coisa do nada e vendê-la.
E. Nada tenho a dizer e estou dizendo-o. Tal é a poesia.

O conectivo "e" tem valor adversativo quando usado como equivalente à conjunção "mas". Nesse caso, vamos notar uma relação de oposição de ideias. 
Veja que há uma oposição entre não ter nada a dizer e dizer. Ou seja, a frase foi usada com o sentido de:

-> Nada tenho a dizer, mas estou dizendo-o.
GABARITO: ALTERNATIVA E.

160.Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - CD - Conhecimentos Gerais para Analista Legislativo - Consultoria - Pós-Edital - 2023 - 1º Simulado
Na frase “O sol saiu de manhã e todo frio da noite se dissipou”, a conjunção “E” mostra o mesmo valor em:

A. O professor se aproximou da sala e não entrou.
B. Os juros subiram muito e o consumo ainda se manteve.
C. Novidades e casos espúrios são assuntos para o jornal.
D. Os jovens foram recebidos e encaminhados para o pátio.
E. A guerra começou na fronteira e os moradores evacuaram a área.

Letra e.

Assunto abordado: Emprego de conectores e elementos de sequenciação textual.

Na frase dada, existe relação de causa e efeito na sucessão temporal de “o sol saiu de manhã” para “e todo frio da noite se dissipou”.

(A) Errada. O valor de “e” foi oposição, equivalente a escrever “mas”.

(B) Errada. O valor de “e” foi oposição, equivalente a escrever “mas”.

(C) Errada. O valor foi apenas a soma.

(D) Errada. O valor foi apenas a sucessão temporal, um fato seguido de outro.

(E) Certa. Além de sucessão temporal de fatos, aqui temos um fato gerador (causa: a guerra começou na fronteira) e uma consequência (os moradores evacuaram a área).

161.Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de São José dos Campos - Agente de Combate às Endemias - 2023 
Assinale a frase que não possui um termo indicativo de tempo.

A. Os jovens não percebem as amarguras da vida.
B. Sofre mais aquele que sempre espera do que aquele que nunca esperou nada.
C. Sonhos são como deuses: quando não se acredita neles, deixam de existir.
D. Enquanto uns cantam, outros dormem.
E. Ao perceber a verdade, desmaiou.

A) Os jovens não percebem as amarguras da vida.=> Não há nenhum termo indicativo de tempo.


B) Sofre mais aquele que sempre espera do que aquele que nunca esperou nada.  'sempre', 'nunca' -> tempo


C) Sonhos são como deuses: quando não se acredita neles, deixam de existir. 'quando' -. tempo


D) Enquanto uns cantam, outros dormem. -> 'enquanto' -> temporal


E) Ao perceber a verdade, desmaiou.=> "Ao" aqui equivale a "no momento em que" -> tempo


A    + INFINITO = Condição

AO   + INFINITIVO = Tempo

POR  + INFINITIVO = Causa

PARA + INFINITIVO = Finalidade

162. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEE MG - Professor de Educação Básica - Área: Língua Portuguesa - 2023
Nas frases a seguir há um conector sublinhado. Assinale a opção que mostra um outro conector de mesmo sentido.

A. Se um homem não faz novas amizades [yellow]à medida que[reset] avança na vida, ficará logo sozinho. / logo que.
B. Indicamos para o cargo um amigo. O absurdo seria [yellow]se [reset]indicássemos um inimigo. / caso.
C. É provavelmente verdadeiro, [yellow]como[reset] diz Gore Vidal, que a literatura não carece de escritores, mas talvez de leitores. / sempre que.
D. [yellow]Mesmo que[reset] eu fosse o Lloyd’s inglês, eu não faria o seguro da democracia brasileira. / Assim que.

'a medida que' - indica proporção e 'logo que' - indica tempo

'se' e 'caso' ( que é a nossa alternativa correta) indica condição

'como' conformidade - 'sempre que' - tempo

'mesmo que' - concessão 'assim que' - condição

163. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - FHEMIG - Técnico em Informática - 2023 
Assinale a opção em que a conjunção e mostra valor de consequência.

A. A liberdade não é nada senão a distância entre a caça e o caçador.
B. Nós todos apoiamos a liberdade, mas usamos a mesma palavra e não queremos dizer todos a mesma coisa.
C. A liberdade leva ao humor e o humor conduz à liberdade.
D. Ria e o mundo rirá com você.
E. O sorriso custa menos que a eletricidade e dá mais luz.

Item: A) 
Análise: Neste item, a conjunção 'e' está sendo usada para indicar uma relação de oposição entre 'a caça' e 'o caçador'. 
Não há uma relação de consequência entre as duas partes da frase, portanto, o item não está de acordo com o gabarito da banca.

Item: B) 
Análise: Aqui, a conjunção 'e' está sendo usada para conectar duas ideias que estão sendo contrastadas. 
Não há uma relação de consequência, portanto, o item não está de acordo com o gabarito da banca.

Item: C) 
Análise: Neste item, a conjunção 'e' está sendo usada para indicar uma relação de causa e efeito entre 'a liberdade' e 'o humor'. 
No entanto, a relação não é de consequência, mas sim de reciprocidade, portanto, o item não está de acordo com o gabarito da banca.

Item: D) 
Análise: Neste item, a conjunção 'e' está sendo usada para indicar uma relação de consequência. 
A frase sugere que se você rir ('Ria'), então o mundo rirá com você como resultado. 
Portanto, este item está de acordo com o gabarito da banca.

Item: E) 
Análise: Neste item, a conjunção 'e' está sendo usada para conectar duas ideias que estão sendo comparadas. 
Não há uma relação de consequência, portanto, o item não está de acordo com o gabarito da banca.

164. Ano: 2023 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 21 - Técnico Judiciário - Área: Agente da Polícia Judicial - 2023

Estabelece relação de condição o termo sublinhado em:

A. E, realmente, no dia seguinte não foram poucos os que se declararam perplexos com a questão.
B. Tirar a camisa no escritório, onde já se vira?
C. Curiosamente, fora o seu Justinho e o Simas, ninguém se lembrava como abotoava a camisa.
D. E não consigo decidir se começo a abotoar por baixo ou por cima!
E. Era como se não se conhecessem.

O termo "se" aparece na frase como (ver Cegalla, 2009, p. 562):

-> Pronome reflexivo, com função de objeto direto de verbos reflexivos. Nesse caso, o "se" é equivalente à expressão "a si mesmo", 
como em "poucos os que declararam a sim mesmos perplexos" (alternativa A); "ninguém lembrava a si mesmo como abotoava a camisa" (alternativa C); 
e "era como se não conhecessem a si mesmo" (alternativa E).

-> pronome apassivador. Forma a voz passiva pronominal, juntando-se a verbos transitivos, como na expressão "onde já se vira" (Alternativa B).

-> Conjunção subordinativa: nesse caso o "se" introduz uma oração condicional e é equivalente à conjunção "caso", como no trecho da alternativa D. 
Veja que a frase nos coloca uma condição de começar ou não a abotoar por baixo ou por cima.

165. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MRE - Oficial de Chancelaria - 2023

Ministro de quê? De qualquer coisa: [yellow]contanto que[reset] o meu nome figure, importa pouco a designação.

No terceiro parágrafo do texto 1A1-II, a oração introduzida pela expressão “contanto que” veicula ideia de

A. condição em relação à oração imediatamente subsequente.
B. consequência em relação ao segmento finalizado com dois-pontos.
C. concessão em relação à oração imediatamente subsequente.
D. causa em relação à oração imediatamente subsequente.
E. conclusão em relação ao segmento finalizado pelos dois-pontos.

"Contanto que" - sentido condicional. Sinônimo: desde que. Ministro de quê? De qualquer coisa: contanto que (desde que) o meu nome figure, importa pouco a designação.
Letra "A" a correta.

166. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - RFB - Auditor Fiscal Pós-Edital - 2023 - 4º Simulado 

Em seu romance Cinco Minutos, José de Alencar escreveu: “As almas [yellow]como [reset]as nossas [yellow]quando [reset]se encontram, se reconhecem e se compreendem. [yellow]Mas[reset] ainda é tempo;
não julgas que [yellow]mais [reset]vale conservar uma doce recordação [yellow]do que [reset]entregar-se a um amor [yellow]sem [reset]esperança e sem futuro?”.

Nesse trecho, há uma série de conectivos. O valor semântico de um deles é corretamente apontado em:

A. “As almas como as nossas” – conformidade
B. “quando se encontram” – adversidade
C. “Mas ainda é tempo” – concessão
D. “mais vale conservar uma doce recordação do que entregar-se” – consequência
E. “a um amor sem esperança” – ausência

(A) Errada. O vocábulo sublinhado denota comparação.

(B) Errada. O vocábulo sublinhado denota tempo.

(C) Errada. O vocábulo sublinhado denota adversidade.

(D) Errada. A expressão sublinhada (“mais do que”) denota comparação.

(E) Certa. O vocábulo sublinhado denota, efetivamente, ausência.

167. Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SME - Professor Ensino Fundamental e Médio - Área Língua Portuguesa - 2023 
Leia o fragmento a seguir.

O carro pegou fogo no meio do trânsito. O motorista não conseguiu sair do veículo. Um guarda de trânsito tentou ajudá-lo.

Se reescrevêssemos esse texto, substituindo a pontuação entre os períodos por conectores adequados, fazendo as modificações necessárias, a forma correta seria:

A. O carro pegou fogo no meio do trânsito, então o motorista não consegui sair do veículo embora um guarda de trânsito tenha tentado ajudá-lo.
B. O carro pegou fogo no meio do trânsito, mas o motorista não consegui sair do veículo quando um guarda de trânsito tentou ajudá-lo.
C. O carro pegou fogo no meio do trânsito; o motorista, porém, não consegui sair do veículo quando um guarda de trânsito tentou ajudá-lo.
D. O carro pegou fogo no meio do trânsito, enquanto o motorista não consegui sair do veículo, mas um guarda de trânsito tentou ajudá-lo.
E. O carro pegou fogo no meio do trânsito, mas o motorista não consegui sair do veículo embora um guarda de trânsito tenha tentado ajudá-lo.

O trecho do enunciado apresenta três períodos assindéticos; ou seja, sem a conexão por meio de conjunções. 
Veja que há três ações: o carro pegar fogo; o motorista não conseguir sair do veículo; um guarda de trânsito tentando ajudar.

O enunciado busca a reescrita, retirando o ponto final e incluindo um conectivo adequado, o que torna os três períodos um só. 
O que devemos fazer? Analisar a relação de sentido entre as orações.

Veja que a segunda oração apresenta uma ação contrária ao que se esperaria da primeira. 
Isso porque houve uma adversidade (não conseguir sair do veículo apesar do carro pegar fogo). 
Essa adversidade entre as orações pode ser estabelecida por meio de um conectivo adversativo, tal como "mas, porém" (como sugerem as alternativas B, C e E). 
Nesse caso, já vamos descartar as alternativas A e D, pois os conectivos "então" e "enquanto" indicam ideia de conclusão e tempo, respectivamente.

A última oração traz uma informação que se subordina ao que foi dito antes. 
Nesse caso, a oração é do tipo subordinativa. Veja que essa última oração também indica uma informação que se opõe ao que foi dito na segunda oração. 
Por ser uma oração subordinativa que indica ideia de oposição, devemos incluir um conectivo concessivo, tal como a conjunção "embora". 
Nesse caso, as alternativas B e C também podem ser descartadas, pois apresenta o conectivo temporal "quando".

Portanto, só sobra a alternativa E com a conjunção "embora".

168. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TJ ES - Analista Judiciário - Área Apoio Especializado - Especialidade: Taquigrafia - 2023

No período "Duas ditaduras e muitas incompreensões cercaram a sua atuação inconformista, pois escapava à sua posição na sociedade e ao controle das 
elites para servir às causas da justiça social, dos jovens e dos oprimidos."

No último período do primeiro parágrafo, a conjunção “pois” coordena duas orações que mantêm entre si uma relação de causa e consequência.

E - Errado

não vemos a conjunção "pois" indicando uma relação de causa e consequência, vemos que essa conjunção indica um sentido de explicação em relação à atuação de 
Antônio Cândido, algo que identificamos pelo sentido do texto, vemos também que a conjunção "pois" está antes de uma forma verbal, 
o que nos indica o sentido explicativo, pois Cegalla nos ensina que as conjunções coordenativas explicativas 
"Precedem uma explicação, um motivo: que, porque, porquanto, pois (anteposto ao verbo)".

169. Ano: 2023 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TJ ES - Analista Judiciário - Área Apoio Especializado - Especialidade: Taquigrafia - 2023

No entanto, à maneira de uma radiografia que nos revela, na sua nitidez, detalhes imperceptíveis ao olho nu, mas que, sendo estática, não retém a vida, 
o palpitar do coração, o fluir constante do sangue nas artérias, enfim, os fenômenos fisiológicos que se produzem no interior do nosso corpo, 
os esquemas da sociedade também não nos fazem suspeitar a luta surda e subterrânea dos grupos, a ininterrupta substituição dos indivíduos num arcabouço 
mais ou menos fixo.

Pois a separação de classes não é rígida como a que existe entre as castas. A classe é aberta e percorrida por um movimento contínuo de ascensão e descida, 
o qual afeta constantemente a sua estrutura, colocando os indivíduos de maneira diversa, uns em relação aos outros. 

No quarto parágrafo, o emprego da conjunção “Pois” explicita o caráter de vinculação explicativa entre o teor do primeiro período e as informações que o precedem.

C-Certo

A afirmação está certa. A conjunção "pois" foi usada para introduzir uma explicação para o que foi afirmado no terceiro parágrafo 
(sobre a incapacidade de uma radiografia não captar os sinais de vida que fluem em um ser).
	
		'''


    def menu(self):
        self.print_slow('Bem Vindo aos estudos da Morfologia para concursos com o professor Márcio Wesley...')
        
        while True:
            try:
                indice = int(input('''
                Estudos da Morfologia II:

                [0] - Preposições
                [1] - Adjetivo
                [2] - Locução Adjetiva
				[3] - Artigo
				[4] - Pronomes
				[5] - Pronomes Pessoais
				[6] - Colocações Pronominais  
				[7] - Pronome Possessivo
				[8] - Pronome Indefinido
				[9] - Pronome Interrogativo
				[10]- Pronome Relativo
				[11]- Pronome Demonstrativo
				[12]- Verbo
				[13]- Modo Imperativo (do verbo)
				[14]- Formas nominais do verbo
                [15]- Verbo II
				[16]- Vozes Verbais
				[17]- Ortografia
				[18]- Porque/Porquê/Por que/Por quê
				[19]- Estruturação das palavras ( Formação )
				[20]- Questões ( formação de palavras e emprego dos 'porques' )
				[21]- Mas/Mais
				[22]- Há/a
				[23]- 'afim de...'
				[24]- Mal/Mau
				[25]- Emprego do hífen - Marcio Wesley
				[26]- 51 exercícios de Pronomes
				[27]- 66 exercícios de verbos
				[28]- 56 exercícios de ortografia
				[29]- 170 exercícios de conjunções
                [30]- SAIR

                Escolha: '''))
                if indice == 0:
                    self.print_slow_2(self.preposicoes())
                    self.dots()
                elif indice == 1:
                    self.print_slow_2(self.adjetivo())
                    self.dots()    
                elif indice == 2:
                    self.print_slow_2(self.locucao_adjetiva())
                    self.dots()
                elif indice == 3:
                    self.print_slow_2(self.artigo())
                    self.dots()   
                elif indice == 4:
                    self.print_slow_2(self.pronomes())
                    self.dots()  
                elif indice == 5:
                    self.print_slow_2(self.pronome_pessoal())
                    self.dots()
                elif indice == 6:
                    self.print_slow_2(self.colocacao_pronominal())
                    self.dots()             
                elif indice == 7:
                    self.print_slow_2(self.pronome_possessivo())
                    self.dots()      
                elif indice == 8:
                    self.print_slow_2(self.pronome_indefinido())
                    self.dots()                 
                elif indice == 9:
                    self.print_slow_2(self.pronome_interrogativo())
                    self.dots()         
                elif indice == 10:
                    self.print_slow_2(self.pronome_relativo())
                    self.dots() 
                elif indice == 11:
                    self.print_slow_2(self.pronome_demonstrativo())
                    self.dots()    
                elif indice == 12:
                    self.print_slow_2(self.verbo())
                    self.dots()     
                elif indice == 13:
                    self.print_slow_2(self.modo_imperativo())
                    self.dots()   
                elif indice == 14:
                    self.print_slow_2(self.formas_nominais_verbo())
                    self.dots() 
                elif indice == 15:
                    self.print_slow_2(self.verbos_dois())
                    self.dots()         
                elif indice == 16:
                    self.print_slow_2(self.vozes_verbais())
                    self.dots()    
                elif indice == 17:
                    self.print_slow_2(self.ortografia())
                    self.dots()           
                elif indice == 18:
                    self.print_slow_2(self.porques())
                    self.dots()      
                elif indice == 19:
                    self.print_slow_2(self.estrutura())
                    self.dots()     
                elif indice == 20:
                    self.print_slow_2(self.questoes_estrutura_porques())
                    self.dots()
                elif indice == 21:
                    self.print_slow_2(self.mas_mais())
                    self.dots()
                elif indice == 22:
                    self.print_slow_2(self.ha_a())
                    self.dots()              
                elif indice == 23:
                    self.print_slow_2(self.afim_de())
                    self.dots()    
                elif indice == 24:
                    self.print_slow_2(self.mal_mau())
                    self.dots() 
                elif indice == 25:
                    self.print_slow_2(self.hifen())
                    self.dots()      
                elif indice == 26:
                    self.print_slow_2(self.exercicios_pronomes())
                    self.dots()	
                elif indice == 27:
                    self.print_slow_2(self.exercicios_verbos())
                    self.dots()	
                elif indice == 28:
                    self.print_slow_2(self.exercicios_orto())													                                                                           
                    self.dots()
                elif indice == 29:
                    self.print_slow_2(self.exercicios_conjuncoes())
                    self.dots()
                elif indice == 30:					
                    self.print_slow('Saindo...')
                    break
                else:
                    self.print_slow('Escolha inválida.')
                    self.dots()
            except ValueError:
                self.print_slow('Somente valores inteiros...')

if __name__ == '__main__':
    Morfologia = Morfologia()
    Morfologia.menu()