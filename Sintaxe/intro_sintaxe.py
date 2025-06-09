from colorama import Fore, Style, Back, init
from time import sleep
import sys
import keyboard

class Sintaxe:     
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

        #def toggle_pause():
        #    nonlocal paused
        #    paused = not paused

        #keyboard.on_press_key("space", lambda _: toggle_pause())

        #while i < len(text):
        #    char = text[i]
        #    if char == '[':  # Verifica se encontrou um possível código de cor
         #       end_index = text.find(']', i + 1)
          #      if end_index != -1:
           #         color_code = text[i + 1:end_index]
            #        if color_code in color_codes:
             #           current_color = color_codes[color_code]
               #         i = end_index + 1
              #          continue
            #if current_color:
             #   sys.stdout.write(current_color + char)
              #  sys.stdout.flush()
            #else:
                #sys.stdout.write(char)
                #sys.stdout.flush()
            #sleep(0.06)
            #while paused:
             #   sleep(0.1)
            #i += 1
        #print(Style.RESET_ALL)

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

        while i < len(text):
                char = text[i]
                if char == '[':  # Verifica se encontrou um código de cor
                    end_index = text.find(']', i + 1)
                    if end_index != -1:
                        color_code = text[i + 1:end_index]
                        if color_code in color_codes:
                            current_color = color_codes[color_code]
                            i = end_index + 1
                            continue

                if current_color:
                    sys.stdout.write(current_color + char)
                else:
                    sys.stdout.write(char)
                    
                sys.stdout.flush()
                output_text.append(char)
                sleep(0.06)

                while paused:
                    sleep(0.1)

                i += 1
                
        print(Style.RESET_ALL)                           

    def sujeito(self):
        return '''
        Sintaxe:

Termos relacionados ao verbo:

- Objeto direto
- Objeto indireto
- Adjunto adverbial
- Agente da passiva

Termos que se referem aos nomes: (substantivos)

- Adjunto adnominal
- Complemento nominal
- Aposto
- Predicativo

Termos essenciais:

    Sujeito e predicado

Termos integrantes:

    Complemento Verbal (objeto direto, indireto)
    Complemento Nominal 
    Agente da Passiva

Termos acessórios:

    Adjunto Adnominal
    Adjunto adverbial
    Aposto

Sujeito: é o termo a respeito do qual se declara alguma coisa.
Predicado: é aquilo que se declara a respeito do sujeito    


Frase - Sentença organizada em língua portuguesa

Coerência nominal

Oração : Frase + verbo

Período : com 1 oração  = simples (oração absoluta)
	      com 2 orações = COMPOSTO

A lingua portuguesa prefere por uma ordem direta da oração -> Ordem preferencial

Sujeito + verbo + complementos + adjunto adverbial

** Tudo aquilo que não é sujeito é o predicado. **

Identificação do sujeito : ordem direta da oração -> S + V + C + A.adv
	Conceito do sujeito:

		- [red]NÃO É QUEM PRATICA A AÇÃO VERBAL.[reset] Muitos sujeitos praticam ação verbal sim, é verdade. -

	[blue]O conceito é[reset]: [yellow]Termo com o qual o verbo estabelece concordância.[reset] ( a chamada concordância verbal )

	[green]O sujeito não pode ser preposicionado no início da frase. Nada impedi de existir termos preposicionados dentro do sujeito.[reset]

Na prática, para encontrar o sujeito de uma oração, é aconselhável localizar o verbo da oração
         e com ele construir uma interrogação do tipo “quem ou o que + verbo?”

    Milhares de abelhas invadiram a cidade.

    [red]“Quem invadiu?”[reset] -> [yellow]“Milhares de abelhas.”[reset] -> [blue]Sujeito da oração 'milhares de abelhas'[reset]
    
    Naquela noite, frisou muito a necessidade de mais empenho de nossa parte o palestrante, em sua colocação.

    [red]“Quem frisou?”[reset] -> [yellow]“O palestrante.”[reset] -> [blue]Logo, o sujeito é 'o palestrante'.[reset]

    Existe dentro do sujeito o chamado núcleo:

		O aumento dos preços dos combustíveis assustou os brasileiros

quem é que assustou os brasileiros? [red]'o aumento dos preços dos combustíveis'[reset] -> [bg_red]sujeito[reset]
Os elementos se subordinam, 'os preços' estão subordinados ao aumento, e 'os combustíveis' estão subordinados 'aos preços'.
Núcleo do sujeito: substantivo sem preposição 'aumento' - só pode ser núcleo do sujeito o substantivo que não estiver preposicionado.

Além disso, o verbo 'assustou' concorda com sujeito ou com o núcleo do sujeito ( sabendo o núcleo do sujeito ), se por acaso a banca perguntar:

	- o verbo 'assustou' está no singular porque deve concordar com o núcleo do sujeito: 'o aumento dos preços' - [bg_red]ERRADO[reset]
	- núcleo da frase é somente 'aumento' no caso de um sujeito simples. Portanto, o verbo deve concordar com o núcleo do sujeito.
[red]O substantivo 'aumento' não está preposicionado. [reset]
[bg_red]Por isso ele é núcleo do sujeito, os outros substantivos não podem ser núcleo por serem preposicionados.[reset]
	- Sendo assim, por concordar com o núcleo do sujeito o verbo não pode estar no plural, seria errado. O núcleo está no singular.

        Nas cidades do interior, vivem em paz os homens e as mulheres de bem.

        'vivem' -> verbo
	    'nas cidades do interior' -> nunca poderá ser sujeito pois inicia com preposição
	    após o verbo 'vivem' -> 'em paz' -> inicia com preposição, também não pode ser sujeito
	    quem é que vive em paz? 'os homens e as mulheres de bem' <- Sujeito posposto
		Dentro do sujeito temos o substantivo 'homens' e substantivo 'mulheres' <- dois núcleos

        Cabe às autoridades a aprovação dos projetos.

	    'cabe'-> verbo
	    'as autoridades' -> não pode ser sujeito 'a' preposição + artigo 'as', só pode ser predicado.
            Pergunte então ao verbo, o que cabe as autoridades? 'a aprovação dos projetos' <- sujeito posposto
	        O núcleo do sujeito portanto é a 'aprovação' <- substantivo
	    ' a aprovação dos projetos ' -> sujeito posposto
	    'dos projetos' é subordinação de 'aprovação.'


sujeito simples : 1 núcleo
sujeito composto: 2 núcleos
Eles são sujeitos expressos

Para melhor compreensão sobre como o sujeito pode exercer suas funções na oração, considera-se a seguinte classificação:

1. Sujeito Simples – possui de um só núcleo.

Nós // saímos cedo. 'nós' -> núcleo

As lindas e brancas flores do inverno europeu // desabrocharam. -> 'flores' -> núcleo

O núcleo do sujeito costuma ser um substantivo, mas pode ser também um pronome ou um numeral de valor substantivo,
 ou seja, um pronome ou um numeral que figure no lugar do substantivo.

Os outros dois [yellow]meninos[reset] dançam melhor. [blue](sujeito simples; núcleo: meninos)[reset]
Os [yellow]outros[reset] dançam melhor. [blue](sujeito simples; núcleo: outros = pronome substantivo)[reset]
[yellow]Dois[reset] dançam melhor.[blue] (Sujeito simples; núcleo: dois = numeral substantivo)[reset]

Nota: No primeiro exemplo, perceba que “outros” e “dois” acompanham o nome-núcleo “meninos”, 
por essa razão, são, respectivamente um pronome adjetivo e um numeral adjetivo.

2. Sujeito Composto – possui mais de um núcleo.

[yellow]Samara[reset] e [yellow]Kátia[reset] tinham uma amizade de longes dias.
[yellow]Dia[reset], [yellow]hora[reset] e [yellow]lugar[reset] devem ser ajustados com antecedência para a garantia de inocorrência
de atropelos de última hora.
Naquele momento da sua vida, [yellow]dinheiro[reset], [yellow]fama[reset], [yellow]poder[reset], nada mais importava ante a iminência da morte.

[bg_blue]vale destacar que o núcleo do sujeito não pode ser preposicionado.[reset]

A [yellow]iniciativa[reset] da equipe, [yellow]a inovação[reset] da ideia e a [yellow]propriedade[reset] da proposta foram responsáveis pelo
sucesso do projeto. (sujeito composto; núcleos = iniciativa, inovação, propriedade)

Os sujeitos não expressos podem ser chamados de elíptico ou desinencial ou oculto ou implícito

- Sempre estará na 1ª e 2ª pessoa do singular ou plural.

	Mentes tão bem.

Não está verbalmente expresso mas é [yellow](TU) MENTES TÃO BEM.[reset] <- [blue]O sujeito não apareceu, ele está elíptico. 2º pessoa do singular.[reset]

Sujeito Oculto (Elíptico ou Desinencial) – é aquele que, não estando escrito na frase,
pode ser identificado pela desinência verbal ou pela ausência dela.

Quase sempre verbos no imperativo apresentam sujeito oculto, ainda que se apresentem na 3.ª pessoa do plural.

Permanece calmo. (sujeito oculto: tu.)
Fique quieto, menino! (sujeito oculto: você.)
Venhamos e convenhamos: já tivemos dias melhores. (sujeito oculto: nós.)
Parem já com a bagunça! (Sujeito oculto: vocês.)

Quase sempre verbos no imperativo apresentam sujeito oculto, ainda que se apresentem na 3.ª pessoa do plural.

Permanece calmo. (sujeito oculto: tu.)
Fique quieto, menino! (sujeito oculto: você.)
Venhamos e convenhamos: já tivemos dias melhores. (sujeito oculto: nós.)
Parem já com a bagunça! (Sujeito oculto: vocês.)

Chegaremos a casa logo. (Sujeito oculto – nós.)

Pedro não veio, mas avisou. (Suj. oculto – Pedro.)

Perceba-se que “veio” tem sujeito simples (Pedro); contudo “avisou”, apesar de referir-se ao mesmo sujeito, não o apresenta
expresso, daí ser considerado oculto.

O sujeito indeterminado é 'eles/elas' 3º pessoa do plural:

	Disseram palavras de amor. ( quem disse? 'eles?elas?' )

4. Sujeito Oculto (Elíptico ou Desinencial) – é aquele que, não estando escrito na frase,
pode ser identificado pela desinência verbal ou pela ausência dela.

Quase sempre verbos no imperativo apresentam sujeito oculto, ainda que se apresentem na 3.ª pessoa do plural.

Permanece calmo. (sujeito oculto: tu.)
Fique quieto, menino! (sujeito oculto: você.)
Venhamos e convenhamos: já tivemos dias melhores. (sujeito oculto: nós.)
Parem já com a bagunça! (Sujeito oculto: vocês.)

5. Sujeito Indeterminado – ocorre quando não queremos ou não podemos identificar o sujeito da oração. Apresenta-se nos casos seguintes:

a) Verbos na 3.ª pessoa do plural que permitem subentender um “eles/elas” que não pode ser identificado no contexto.

[yellow]Roubaram[reset] meu carro ontem. -> 'eles/elas' -> sujeito indeterminado

[yellow]Falam[reset] muito mal dele por aqui -> 'eles/elas' -> sujeito indeterminado

[bg_blue]Conforme comentado anteriormente, verbos no imperativo têm sujeito oculto, ainda que se apresentem na 3.ª pessoa do plural.[reset]

[yellow]Escutem[reset], por favor! (Sujeito oculto: vocês.) -> Portanto, não é sujeito indeterminado.

Caso o sujeito do verbo na terceira pessoa do plural seja identificável, naturalmente não se terá sujeito indeterminado.

O governo se faz de bonzinho, mas [yellow]eles[reset] só querem saber de si. Não [yellow]ligam[reset] para a gente! 

[red](O sujeito de “querem” é simples – eles –, e o sujeito de “ligam” é oculto: eles.)[reset]

b) Verbos transitivos indiretos, verbos intransitivos e verbos de ligação a partícula SE (= índice de indeterminação de sujeito – ÍIS)
    será IIS, são considerados sujeitos indeterminados:

    Precisa-[yellow]se[reset] de empregados.

        Verbo 'precisar' é Verbo transitivo indireto, com preposição. 'de empregados' -> [blue]Objeto Indireto[reset]
                        [red]Portanto, o 'se' é índice de indeterminação do sujeito, indicando que o sujeito é indeterminado.[reset]

    Trata-[yellow]se[reset] de problemas graves.

            O verbo 'tratar' é verbo transitivo indireto que precisa de um complemento indireto: 'de problemas graves'
                        [red]Portanto, o 'se' é índice de indeterminação do sujeito.[reset]

    Obedece-[yellow]se[reset] às leis nesta cidade.

            O verbo 'obedecer' é transitivo indireto com o complemento indireto preposicionado 'às leis'.
            'nesta cidade' por sua vez é adjunto adverbial
            [red]Portanto, o 'se' é indice de indeterminação do sujeito, indicando que o sujeito é indeterminado.[reset]

    Vive-[yellow]se[reset] bem por aqui.

            O verbo 'vive' é intransitivo, não há complementos para o verbo na frase.
            'bem' por sua vez é adjunto adverbial de modo ao passo que 'por aqui' é adjunto adverbial de lugar.
            [red]Portanto, a partícula 'se' é indice de indeterminação do sujeito, indicando que o sujeito é indeterminado.[reset]

    Bebeu-[yellow]se[reset] muito ontem na festa.

            O verbo 'beber' é intransitivo, não há complementos.
            'muito' é adjunto adverbial de intensidade
            'ontem' é adjunto adverbial de tempo
            'na festa' é adjunto adverbial de lugar     
                [blue]Portanto, a partícula 'se' é indice de indeterminação do sujeito, indicando que o sujeito é indeterminado.[reset]

    Naquele tempo, era-se feliz e não se sabia.

            [blue]'era' é verbo de estado, de ligação.[reset] [red]Portanto 'se' é índice de indeterminação do sujeito[reset]
            [blue]'sabia' é verbo intransitivo[reset],[red] portanto, o 'se' é indice de indeterminação do sujeito[reset]

            Discutiu-se o fato

            [red]quem discute, discute algo:[reset] o fato -> [red]objeto direto[reset]
            [red]'discutir' é um verbo transitivo direto[reset], portanto o pronome 'se' é particula apassivadora
                [blue]A particula apassivadora serve para transformar o objeto direto em sujeito paciente 'o fato'[reset]

            [green]Sendo assim, se o sujeito for por plural: 'os fatos'[reset] .
             O verbo irá concordar com o sujeito paciente: 'discutiram-se os fatos'                

            Desconfiou-se do fato

            quem desconfia, desconfia de algo: 'do fato' O complemeto da frase se liga ao verbo pela preposição, portanto é objeto indireto.
                [red]E o verbo 'desconfiar' é transitivo indireto e o pronome 'se' é índice de indeterminação do sujeito.[reset]

            Não se acreditou, mesmo com todas as testemunhas de defesa, na sua versão.

            quem acredita, acredita em algo: [red]'na sua versão'[reset] -> [blue]objeto indireto ( preposição )[reset]
            [red]O verbo 'acreditar' é transitivo indireto, portanto, o pronome SE é indice de indeterminação do sujeito.[reset]

            Entregou-se para o professor, ao final da aula, a relação dos alunos matriculados.

            [red]quem entrega, entrega para alguém:[reset] [blue]objeto indireto ( preposição 'para') 'para o professor'[reset]
            [red]quem entrega, entrega algo:[reset] [blue]'a relação dos alunos matriculados'[reset]
            [green]O verbo 'entregar' portanto é VTDI.[reset]
            O pronome 'SE' então é partícula apassivadora em busca de um complemento direto do verbo para transformar em sujeito
                                Convertido em SUJEITO: 'a relação dos alunos matriculados'

            Ampliam-se os dados

            eles se ampliam? NÃO. [red]Não tem como identificar o agente da ação, quem pratica a ação.[reset] 
                Ficamos entre partícula apassivadora e índice de indeterminação do sujeito                                                        
            [yellow]quem amplia, amplia algo[reset]: [red]'os dados'[reset] -> [green]objeto direto, sem preposição.[reset]
                [red]O verbo 'ampliar' é transitivo direto e portanto o 'SE' é partícula apassivadora.[reset]
                                'os dados' é voz passiva sintética ou pronominal
                [green]Toda voz passiva há VTD mas não objeto direto, porque a voz passiva está na qualidade de sujeito.[reset]

                 Colocando na voz passiva analítica:

                    Os dados são ampliados

                    'os dados' -> Sujeito passivo

        Lembrando que as orações que possuem PA ou IIS não apresentam agente da ação verbal.

            A Particula Apassivadora: transformar o Objeto Direto em sujeito paciente
                    Somente verbos transitivos indiretos e diretos
                       Sujeito estabelece concordância com o verbo

            Deseja-se a verdadeira mudança

            [red]quem deseja?[reset] - não tem o praticante da ação             
            mas o verbo 'desejar' possui um complemento direto [blue]' a verdadeira mudança'[reset]
            [bg_red]A PA transforma OD em sujeito paciente, portanto o sujeito paciente: 'a verdadeira mudança'[reset]

            Acredita-se em qualquer notícia

            [red]quem acredita, acredita em algo:[reset] [blue]'em qualquer notícia'[reset] -> [red]objeto indireto[reset]
            [red]Verbo transitivo indireto com complemento indireto:[reset] [blue]'em qualquer notícia' [reset]       
                [blue]Portanto, o pronome 'se' é indice de indeterminação do sujeito.[reset]

            Foi-se muito feliz no passado

              verbo de ligação : foi
             'muito feliz' : predicativo do sujeito
             'no passado'  : adjunto adverbial
             'se' -> IIS

Considere as orações abaixo:

I. Prescreveu-se vários medicamentos.
II. Trata-se de doenças graves.

A concordância está correta em:

a) somente I b) Somente II  C) I e II  d) nenhuma

[red]quem prescreve, prescreve algo:[reset] [blue]'vários medicamentos'[reset]
     [red]Objeto direto que é o sujeito paciente pela partícula apassivadora 'SE'[reset]

[red]quem trata, trata de algo:[reset] [blue]'de doenças graves'[reset] -> [red]objeto indireto ( c/ preposição )[reset] -> 
            [blue]Portanto, verbos VTI, o pronome 'se' é IIS[reset]

Portanto, a correta concordância seria:

        [yellow]Prescreveram-se[reset] vários medicamentos. [blue]( O verbo concorda com o sujeito 'varios medicamentos')[reset]

        [bg_blue]Quando se é Indice de indeterminação do sujeito o verbo só pode ficar no singular[reset]
                        [bg_blue]portanto o Item II só pode ficar no singular.[reset]

[bg_blue]A alternativa 'b'.[reset]

Considere as orações abaixo:

I.  Não se tratam de questões relevantes.
II. Não se devem considerar problemas pessoais no trabalho.

De acordo com a norma culta:

a. somente I está correta.
b. somente II está correta.
c. I e II estão corretas
d. nenhuma está correta.

        Item I. Quem é que trata? 
                [yellow]quem trata, trata de algo:[reset] [yellow]'de questões relevantes'[reset] -> [blue]objeto indireto[reset]
                [red]Quando é IIS, o verbo só pode ficar no singular, portanto a frase está ERRADA.[reset]
                O correto seria:

                Não se [yellow]trata[reset] de questões relevantes
        
        Item II. 
        [red]'devem considerar'[reset] -> [blue]locução verbal.[reset] 
        [red] A transitividade buscamos no verbo principal 'considerar'.[reset]
        [bg_red]A concordância é feita no verbo auxiliar 'devem'[reset]
        [yellow]quem considera, considera algo[reset]: [blue]'problema pessoais'[reset] -> [red]sujeito paciente ( sem preposição )[reset]
            [red]O verbo auxiliar 'devem' está no plural para concordar com o sujeito 'problemas pessoais'[reset]

Considere as orações abaixo:

I.  Devem-se citar todas as vantagens do produto.
II. Pode-se precisar de mais pessoas no projeto.

A concordância está correta em:

a. Somente I
b. Somente II
c. I e II
d. Nenhuma

[yellow]'devem-se citar' -> locução verbal[reset] // transitividade no verbo principal: quem cita, cita algo: 'todas as vantagens do produto'
    [yellow]'todas as vantagens do produto'[reset] -> [green]Objeto Direto que por sua vez é sujeito paciente pela particula apassivadora 'SE'[reset]
                    [bg_blue]A concordância está correta: verbo auxiliar concordando com o sujeito[reset]

[yellow]'pode-se precisar'[reset] -> locução verbal // transitividade do verbo principal: quem precisa, precisa de algo: 'de mais pessoas'
    [yellow]'de mais pessoas'[reset] -> [blue]Objeto Indireto[reset] , portanto o pronome 'SE' é indice de indeterminação do sujeito, somente no singular.
                    [bg_blue]A concordância está correta: verbo auxiliar somente no singular.[reset]


Considere as orações abaixo:

I.  Devem-se pensar em todos os aspectos do problema.
II. Devem-se analisar todos os aspectos do problema.

A concordância está correta em:

a. somente I
b. Somente II
c. I e II
d. nenhuma

[blue]'devem-se pensar'[reset] -> locução verbal // [yellow]transitividade ocorre no verbo principal[reset]: quem pensa, pensa em algo: 'em todos os aspectos do problema'
    [bg_blue]Portanto, objeto indireto por ter preposição, sendo assim, somente o verbo pode ficar no singular: 'deve-se pensar' por ser IIS[reset]

[blue]'devem-se analisar'[reset] -> locução verbal // [yellow]transitividade ocorre no verbo principal[reset]: quem analisa, analisa algo: 'todos os aspectos do problema'
        [red]verbo transitivo direto, sem preposição, portanto, objeto direto é o sujeito paciente: pronome 'se' como particula apassivadora'[reset]
                [bg_red]Concordância correta no plural concordando com o sujeito.[reset]

Alternativa 'b', somente a II.

Outra questão:

    Nas formas de vida coletiva [yellow]podem assinalar-se[reset] dois princípios que se combatem e regulam diversamente as atividades dos homens.

    Embora elimine do texto a idéia de possibilidade, a supressão do auxiliar, na locução 'podem assinalar-se', mantém a coerência 
    textual e a correção gramatical, desde que seja feita a flexão no verbo principal: assinalam-se.

        [yellow]quem assinala, assinala algo[reset]: [blue]'dois principios'[reset] -> [red]objeto direto, sujeito paciente[reset]
            [red]'assinar'[reset] -> [blue]verbo transitivo direto com particula apassivadora.[reset]
            [bg_red]Com a supressão do auxiliar, a concordância irá para o verbo principal devendo ficar no plural,[reset]
                    [bg_red]concordando com o sujeto no plural 'dois principios' - Questão correta.[reset]

Outra questão:

    Além disso, espera-se que os genéricos sejam bem mais baratos.

    A oração 'que os genéricos sejam bem mais baratos' funciona como complemento da forma verbal 'espera-se', na qual o sujeito é
                        indeterminado pela partícula 'se'.

    quem espera, espera algo: 'que os genéricos sejam bem mais baratos' -> objeto direto ( oração subordinada )
                Portanto é partícula apassivadora serve para transformar em sujeito paciente

            Portanto a questão está errada, o sujeito não é indeterminado, o sujeito é oracional.

A partícula 'SE' em ' a grandeza que se mede em minutos, horas, dias, meses ou anos', classifica-se como:

a. parte integrante de verbo
b. pronome reflexivo recíproco
c. pronome apassivador
d. palavra expletiva
e. índice de indeterminação do sujeito

Temos quem pratica a ação de medir? NÃO -> Pode ser PA ou IIS

    quem mede, mede algo: 'a grandeza' -> objeto direto , portanto o 'se' é partícula apassivadora.

Outra questão:

    Muitas vezes, não se persegue o encarceramento do agressor.

        Em 'não se persegue' (l.31), a partícula 'se' está empregada como um recurso para indeterminar o sujeito.

            quem não persegue, persegue algo: 'o encarceramento do agressor' -> objeto direto sem preposição a qual o pronome 'se' 
                    é particula apassivadora transforma em sujeito paciente 'o encarceramento do agressor'
                        Portanto, a questão está errada. É uma particula apassivadora. 
                                    Está empregado para apassivar a frase.

    Veja esta questão:

        Ao mesmo tempo em que se improvisavam escadas de madeira para efetuar salvamentos, retirando-se os moradores, antes que eles
        se atirassem das janelas dos sobrados.

            Nas linhas 9 e 10, a partícula 'se' exerce a mesma função sintática em ambas as ocorrências.

            retirando-se os moradores, o sujeito é indeterminado. Não sabemos quem retirou os moradores
                'se' portanto, PA ou IIS.
            eles = os moradores / quem pratica a ação de retirar são os moradores, sabemos quem pratica a ação verbal.
                    Portanto o outro 'se' -> Não pode ser PA e nem IIS.
                        Logo as partículas exercem funções distintas.
            O primeiro 'se' é particula apassivadora, temos um verbo transitivo direto: 'retirar' -> 'os moradores' -> objeto direto
                    com o pronome 'se' apassivador, portanto, o sujeito paciente é 'os moradores'.                        
            No segundo 'se' temos um pronome reflexivo, 'eles' refere-se aos moradores - sujeito.

Veja esta questão:

    Uma delas é a impossibilidade de se registrar e deixar para a posteridade a vida de personagens importantes na formação do país,
        em qualquer ramo de atividade.

        O termo se, em 'se registrar' é utilizado para indicar reflexividade.

        quem registra, registra algo: 'a vida de personagens importantes' -> objeto direto
                Portanto, sem preposição, sujeito paciente, sendo assim, partícula apassivadora.
                                Não é reflexivo.


Veja esse exemplo interessante:

    Com efeito, cuida-se de associação que congrega categoria econômica diferenciada.

        'com efeito' -> não pode ser sujeito, com preposição.
        'de associação que congrega categoria econômica diferenciada' -> não pode ser sujeito, com preposição.

        Portanto, o 'se' não pode ser partícula apassivadora, precisa de um sujeito paciente.
                        Só pode ser índice de indeterminação do sujeito

        Às prorrogações do trabalho noturno aplica-se o disposto neste capítulo.

        quem aplica algo: 'o disposto neste capítulo' - objeto direto
        quem aplica a alguem: 'às prorrogações do trabalho noturno' -> Objeto Indireto
        Portanto, o verbo aplicar é VTDI, sendo assim, o 'se' tranforma o objeto direto em sujeito paciente
            'sujeito paciente' -> 'o disposto neste capítulo'
                NO VTD QUEM SOFRE A AÇÃO É O SUJEITO PASSIVO, COM A PARTICULA APASSIVADORA NÃO HÁ OBJETO DIRETO


CESPE/CGE/RJ/AUDITOR/2024

Quando se trata da construção da imagem de uma organização, ressalta-se o papel dos veículos de imprensa.
Esses veículos, ao publicarem uma notícia, atuam na associação e formação das crenças, das ideias, dos sentimentos e das impressões
que uma pessoa ou um grupo tem ou passa a ter sobre aquela organização.

A particula 'se' em ambas as suas ocorrências, indica que é indeterminado o sujeito sintático de cada uma das orações que formam o período.

    quem se trata, se trata de quem? 'da construção da imagem de uma organização' -> objeto indireto, não pode ser sujeito.
            portanto 'tratar' é verbo transitivo indireto -> a particula 'se' é IIS

    quem ressalta, ressalta algo: 'o papel dos veículos de imprensa' -> Objeto direto que por sua vez é o sujeito paciente
        A particula 'se' é apassivadora, ja que possui o sujeito paciente, mesmo o verbo sendo VTD, temos a PA 'se'

                    Portanto, ERRADA. A questão trata-se de partículas diferentes.

CESPE/TELEBRAS/2022

    A telecomunicação militar apoiada em satélites e a eletrônica determinarão as guerras do futuro imediato. Fala-se já de bombas
    eletrônicas que podem paralisar estabelecimentos neurais da sociedade moderna, como hospitais, centrais elétricas, oleodutos, etc.

    No último parágrafo do texto, a partícula 'se' em 'fala-se já de bombas eletrônicas', indica que o sujeito é indeterminado.

        quem fala, fala de algo: 'de bombas eletrônicas' -> termo com preposição, portanto, objeto indireto
            o verbo 'falar' é portanto, VTI sendo assim, a particula 'se' é índice de indeterminação do sujeito
                                        'já' -> adjunto adverbial

O SUJEITO É INDETERMINADO EM VERBOS NO INFINITIVO IMPESSOAL ( SEM FLEXÃO E SEM ASSOCIAÇÃO COM O SUJEITO)

Exemplos:

        Amar é quando não dá mais para disfarçar

        quem ama? Sujeito indeterminado

        Navegar é preciso, viver não é preciso.

        quem navega? quem vive? Sujeito indeterminado

        Outro exemplo:

            Em meus tempos de escola, não se via mal em provocar os colegas por suas peculiaridades ou manias.

                quem provoca? Sujeito indeterminado

            É preciso confiar em Deus 

'é' -> verbo
'confiar' -> verbo no infinitivo impessoal portanto é um sujeito indeterminado

O que é preciso? 'confiar em Deus' - Portanto 'confiar em Deus' é o sujeito do verbo 'é'
'confiar' por sua vez é infinitivo impessoal com sujeito indeterminado


		Choveu durante a cerimônia 

'choveu' -> fenômenos da natureza -> verbo impessoal -> fenômenos da natureza -> somente no singular

	O verbo impessoal não consegue identificar o referente, mas ele pode deixar de ser impessoal.
	Oração sem sujeito ou sujeito inexistente
	Portanto, seria incorreta colocar: Choveram durante a cerimônia

	Choveu granizo durante a cerimônia

	Agora choveu 'granizo' -> granizo -> sujeito simples

    Se o infinitivo se apresentar flexionado ou tiver sujeito identificável, naturalmente não se terá sujeito indeterminado.

Ele achou melhor refazer os exercícios desde o início.
(O sujeito de “refazer” é determinado: ele.)

5. Sujeito Inexistente (oração sem sujeito) – certas orações são construídas com verbos
que não possuem sujeito a que se possa atribuir o que é declarado; tais verbos são denominados impessoais. Sempre que utilizados, a oração terá sujeito inexistente. Tal ocorrerá nos
casos que se apresentam a seguir.

a) Verbos que expressam fenômeno meteorológico (chover, nevar, relampejar, ventar, escurecer, amanhecer etc.)

[yellow]Choverá[reset] muito à noite.

[yellow]Amanheceu[reset] lentamente.

Por aquelas bandas [yellow]escurece[reset] rápido.

Atente-se ao contexto! Veja exemplos:

[yellow]Choveu[reset] durante a reunião.

(O verbo se apresenta em seu sentido próprio, com expressão de fenômeno meteorológico; logo, trata-se de oração sem sujeito.)

[yellow]Choveu[reset] [blue]canivete[reset] durante a reunião.

(Tem-se aí sentido figurado; assim, “canivete” atua como núcleo do sujeito simples.)

Nossa! [yellow]Esfriou[reset] depressa.

[green](O verbo se apresenta em seu sentido próprio, com expressão de fenômeno meteorológico; logo, trata-se de oração sem sujeito.)[reset]

Nossa, meu [yellow]café[reset] [blue]esfriou[reset] depressa!

[green](Tem-se aí sentido próprio; contudo, “café” atua como núcleo do sujeito simples.)[reset]

O verbo HAVER não admite sujeito, é indeterminado.

 Quando empregado no sentido de existir, ocorrer ou quando empregado para indicar tempo decorrido.

  Portanto, não concorda com o sujeito.

  [yellow]Havia[reset] plantas na varanda. [blue]<- Portanto, 'havia' só pode ficar no singular.[reset]

	[red]O verbo haver no sentido existir é impessoal portanto, não admite sujeito.[reset]

	[yellow]Existiam[reset] plantas na varanda.

	'existiam' -> verbo existir
	'plantas'  -> sujeito <- agora admite sujeito

	[bg_red]PORTANTO SE COLOCAR 'HAVIAM PLANTAS NA VARANDA' no plural, é errado! Por ser impessoal, no sentido de existir.[reset]
	
		[bg_red]Atenção! O verbo 'existir' é pessoal.[reset]

Outro exemplo:

    [yellow]Houve[reset] acidentes durante o feriado.

        'houve' -> é verbo impessoal, mesmo flexionado. Somente fica no singular
            Portanto, 'houveram acidentes durante o feriado' é ERRADO, não concorda com o sujeito.

        Agora, se empregar o verbo ocorrer ou acontecer, são pessoais. Devem concordar com o sujeito.

            Ocorreram/aconteceram acidentes durante o feriado. -> corretos por concordar com o sujeito

            [red]Agora vejamos[reset]: locução verbal

            [yellow]Deve haver[reset] plantas na varanda. / [yellow]Pode haver[reset] plantar na varanda

            'deve' verbo auxiliar + 'haver' verbo principal

	        A locução verbal 'deve haver' é impessoal, no sentido de existir, a oração não tem sujeito.  


            Verbo auxiliar   -> concordância verbal     -> Principais: SER, ESTAR, TER, HAVER, IR, DEVER, PODER
            Verbo principal  -> significado da locução  -> Formas nominais do verbo: Infinitivo AR/ER/IR / participio -ADO / gerúndio -NDO          

            [yellow]Pode haver[reset] acidentes durante o feriado.

	'Pode haver' no sentido de ocorrer, acontecer, a frase não tem sujeito, a locução é impessoal.

	Se empregar Podem haver acidentes durante o feriado esta ERRADO, pois a locução toda é impessoal e o auxiliar no singular.

    Agora quando tem sujeito na frase:

            [yellow]As crianças[reset] haviam brincado no parque.

            'as crianças' -> sujeito
            'haviam brincado' -> esta correto             

            [bg_red] NEM TODO VERBO HAVER É IMPESSOAL, TENDO O SUJEITO NO PLURAL PARA FAZER A CONCORDÂNCIA [reset]

            [yellow]Há[reset] oito meses, eles esperam a criança.

            'há' -> [blue]tempo transcorrido, também impessoal, sem sujeito. Só pode ficar no singular[reset]

[yellow]Havia[reset] pessoas presas no elevador. (Verbo haver com sentido de existir: sujeito inexistente,oração sem sujeito.)

[yellow]Houve[reset] muitas abstenções na votação. (Verbo haver com sentido de ocorrer: sujeito inexistente, oração sem sujeito.)

[yellow]Estou[reset] aqui há horas. (Verbo haver com indicação de tempo decorrido: sujeito inexistente, oração sem sujeito.)

Se o verbo haver não for empregado para indicar existência, ocorrência ou tempo decorrido,
ele aceitará sujeito. Nessa situação, é comum que ele atue com verbo auxiliar de outro.

Quando eles chegaram, [yellow]nós[reset] já [blue]havíamos[reset] terminado os testes. (Sujeito simples; núcleo = nós.)

Foi uma confusão: [yellow]haviam[reset] incendiando pneus e até um carro. (Sujeito indeterminado)



Outro verbo impessoal:

[bg_red]- Fazer -> [reset]            

Tempo transcorrido - será impessoal
Referência climática - será impessoal

    [yellow]Faz[reset] oito meses que eles esperam a criança

    'faz' -> [red]não admite sujeito, só pode ficar no singular.[reset]
         [bg_red]Portanto, a troca por 'fazem' está errado.[reset]

         	[yellow]Faz[reset] frio na Holanda

            'frio' -> clima
            'faz' -> verbo impessoal que não admite sujeito, somente no singular.

d) Verbo SER
O verbo ser será impessoal (oração sem sujeito) quando empregado para indicar distância, hora ou data.            

Daqui à cidade, [yellow]são[reset] mais de quinze quilômetros.

[yellow]Eram[reset] seis horas quando ele chegou.

Hoje [yellow]é[reset] 22 de outubro

Hoje [yellow]são[reset] 22 de outubro.


CONCORDÂNCIA VERBAL:

	Uma parte dos candidatos [yellow]reclamou/reclamaram[reset] da estrutura das salas.

quem reclamou? 'uma parte dos candidatos' <- sujeito
'parte' <- núcleo do sujeito no singular concorda com o verbo 'reclamou'
'dos candidatos' -> termo que especificador o núcleo no plural, portanto é correto afirmar 'reclamaram'    

    A maioria da sociedade [yellow]torce/tocem[reset] por nosso altletas.

quem torce? 'a maioria da sociedade' -> sujeito / 'maioria' -> núcleo do sujeito -> singular
'da sociedade' -> especificante do núcleo no singular, portanto o verbo só pode ficar no singular 'torce'.

    Um bando de loucos [yellow]viajou/viajaram[reset] para o Japão.

[bg_red]Podemos fazer a concordância com o núcleo ou com o especificante do núcleo do sujeito.[reset]

 sujeito: Um bando de loucos
	núcleo do sujeito : bando
		[bg_blue] especificante do núcleo: 'de loucos' ( está no plural )[reset] -> podendo concordar com o especificante <-

        Um milhão de pesquisas já mostrou/mostraram essa verdade.

quem mostrou? sujeito: um milhão de pesquisas
	núcleo do sujeito: milhão
		termo especificador do núcleo: de pesquisas ( está no plural ) -> podendo concordar com o especicante <-

        [bg_green]Portanto, está sendo em mostrou ou mostraram essa verdade. As duas concordâncias são válidas.[reset]

[red]Sujeito com numerais percentuais e fracionários.        [reset]

        20% de todo o montante serão [yellow]doados/será[reset] doado aquela creche.

        quem será/serão doados? sujeito: 20% de todo o montante
        núcleo do sujeito: 20%

        O núcleo do sujeito 20% é plural
'de todo o montante' -> especificante do núcleo que o verbo pode concorda com ele, portanto, 
'de todo o montante' pode ser 'será' também. -> SINGULAR

	    Os 20% de todo o montante serão doados aquela creche.

        'os' -> artigo determinante do núcleo do sujeito 'os 20%'. O verbo 'serão' deve estar no plural para concordar com o núcleo sujeito.

        	1/4 dos médicos está/estão em greve.

            '1/4' -> na gramática somente importa o numerador '1' - 

            '1/4' -> núcleo do sujeito -> SINGULAR
            'dos médicos' -> especificante do núcleo que está no plural podendo ser 'estão em greve'

         	2/3 do povo brasileiro reclamam/reclama da política monetária

            núcleo do sujeito: numerador da fração é 2, plural.
            'do povo brasileiro' -> especificante do núcleo -> singular

            	[bg_blue]Portanto 'reclamam'/ 'reclama' : as duas formas estão corretas[reset]

	Mais de um milhão de crianças [yellow]vive/vivem[reset] em situação precária.

	'milhão' -> núcleo do sujeito -> SINGULAR
	'de crianças' -> plural - especificador do núcleo no plural

	    Portanto, as duas formas estão corretas. Tanto 'vive' como 'vivem'.

   	[yellow]Os[reset] Estados Unidos pautam a economia mundial.

	'os' determinantes - artigo - 'os Estados Unidos', portanto 'pautam' no plural

	Minas Gerais integra a região sudeste.

	Não há determinante, portanto o verbo 'integra' somente no singular.

    SUJEITO COMPOSTO:

    	O homem e a mulher batalham por melhorias.

    'o homem e a mulher' -> sujeito composto anteposto o verbo só pode ficar no plural 'batalham' unido por conjunção aditiva 'e'.

    	Batalham/batalha por melhorias o homem e a mulher. <- Sujeito Composto posposto

        quem batalha por melhorias? 'o homem e a mulher' <- Sujeito

Sendo assim, podendo o verbo 'batalha' no singular, concordando com o sujeito mais próximo 'o homem' mas somente se o suj. estiver posposto

	O medo e o temor não [yellow]pode/podem[reset] vencer.

  	'o medo e o temor' -> sinônimos/sujeito composto

    	Verbo SER:

	Nós somos o futuro.

	O verbo 'somos' concorda com a 1º pessoa do plural.

	Eu sou Elias Santana.
	
	O verbo 'sou' concorda com a 1º pessoa do singular.

	Tudo na vida é/são flores

	'tudo' não é pessoa / 'flores' não é pessoa
	'é' e 'são' podem concordar tanto com 'tudo' como com 'flores'

	O problema era/eram as brigas frequentes.

	'problema' -> não é pessoa
	
	'as brigas frequentes' -> não é pessoa

	Sendo assim, 'era/eram' podem concordar com 'problema' ou 'as brigas frequentes'.

    Verbo SER é impessoal quando indicar tempo/clima

	São cinco horas da tarde.

	O verbo 'SER' flexionado 'são' no presente do indicativo concorda em número com : 'cinco horas'

	É meio-dia e meia. 

	O verbo 'SER' flexionado 'é' no presente do indicativo concorda com o 'dia' , no singular com o sujeito

	São 12 horas.  * A abreviação é 12h. * 'São' no plural 

	Hoje é/são (dia) quatorze de maio.  <- dia está implicita

	Agora se o dia estiver escrito:

	Hoje é dia quatorze de maio <- Agora o verbo ser concorda somente no singular o sujeito
	
		É frio durante o inverno

	É impessoal por ser tempo e clima.
		'é' verbo ser concorda com o sujeito 'frio'

Questão 01:

	Na casa das palavras, sonhou Helena Villagra, chegavam os poetas.

Considerando ainda o fragmento, o termo destacado 'os poetas' exerce a mesma função sintática do elemento sublinhado:

a. As palavras, guardadas em velhos frascos de cristal, esperavam [yellow]pelos poetas[reset] (linhas 2-4)

b. ... elas rogavam [yellow]aos poetas[reset] que as olhassem 

c. ... e então lambiam [yellow]os lábios[reset]

d. Na casa das palavras havia [yellow]uma mesa das cores[reset] (linhas 13-14)

e. Em grandes travessas [yellow]as cores[reset] eram oferecidas (linhas 14-15)

    'os poetas' na frase é: sujeito

a. As palavras, guardadas em velhos frascos de cristal, esperavam [yellow]pelos poetas[reset] (linhas 2-4)

	[red]Não pode ser sujeito, preposição iniciada 'por' + artigo 'os[reset]

b. ... elas rogavam [yellow]aos poetas[reset] que as olhassem. 

	Sujeito não pode ser preposicionado:

	preposição 'a' + artigo 'os'    

c. ... e então lambiam [yellow]os lábios[reset] [linha 8-9]

	Os poetas abriam os frascos, provavam palavras com o dedo e então lambiam os lábios ou fechavam a cara.

    'os poetas' -> sujeito simples do verbo abriam
	'provavam' -> quem provavam palavras? 'eles' sujeito elíptico, oculto ou desinencial se referindo aos poetas
	'lambiam' -> quem lambiam os dedos? 'eles', os poetas, sujeito elíptico, oculto ou desinencial
	'fechavam' -> quem fechava a cara? 'eles' , sujeito oculto, elíptico ou desinencial

	O sujeito dos quatro verbos é 'os poetas'? NÃO! 
	O SUJEITO simples 'os poetas' é somente do verbo abriam, não pode ser sujeito simples de mais ninguém.     

d. Na casa das palavras havia [yellow]uma mesa das cores[reset] (linhas 13-14)

O verbo 'havia' no contexto de existia uma mesa das cores, se esta empregado no sentido de existir , é impessoal.
			Portanto não admite sujeito, só pode ficar no singular.

e. Em grandes travessas [yellow]as cores[reset] eram oferecidas (linhas 14-15)

	quem eram oferecidas? 'as cores' -> sujeito

            	Gabarito 'E'	

Questão 02:
A expressão 'há aspectos' manteria a correção gramatical de acordo com a norma padrão da língua caso fosse reescrita da seguinte forma:

a. 'existe aspectos'
b. 'existem aspectos'	
c. 'haveriam aspectos'
d. 'existirão aspectos'

[bg_blue]'há aspectos' - tempo presente[reset]

O verbo existir é pessoal, admitindo sujeito. Portanto, o verbo deve concordar com o sujeito 'aspectos' que está no plural.

[red]existe esta no singular[reset]
[red]haveriam está no futuro do pretérito[reset]
[red]existirão está no futuro do presente[reset]

	[blue]Gabarito portanto letra 'b' 'existem aspectos' <- tempo presente do verbo existir pessoal que admite sunjeito e concorda com ele[reset]

[red]questão 03:[reset]

	No trecho 'diferente é o que: fica doente onde a alegria impera. [yellow]Aceita empregos que ninguém supõe.[reset]
	O sujeito da oração destacada é:

a. implícito
b. oracional
c. impessoal
d. indeterminado

Diferente é o que: (ele) [yellow]fica[reset] doente onde a alegria impera. (ele) [yellow]aceita[reset] empregos que ninguém supõe. 

Sujeito oracional é aquele cujo núcleo é um verbo. ( não é o caso )
Sujeito nominal é aquele cujo núcleo é um substantivo. ( 'difererente' é o núcleo )

	Gabarito letra 'A'

questão 04:

Você é feliz? E agora, neste exato momento, você está feliz? Esperamos que sim.

O sujeito da oração 'esperamos que sim' é indeterminado.

[red]ERRADO.[reset] (nós) esperamos que sim - Sujeito desinencial, oculto, elíptico - 1º pessoa do plural - 'nós'

questão 05:

	No que diz respeito aos desafios da transição energética, a PETROBRAS contribui para a mitigação da mudança climática
por meio do investimento de recursos e tecnologias na produção de petróleo de baixo carbono no Brasil, gerando energia, divisas e riquezas
relavantes para o financiamento de uma transição energética responsável, bem como para a capacidade de ofertar gás e energia despachável para 
viabilizar a elevada participação de energias renováveis na matriz elétrica brasileira. Além disso, [yellow]investe[reset] em novas possibilidades de produtos
a negócios de menor intensidade de carbono, [yellow]promove[reset] pesquisa e desenvolvimento de novas tecnologias e soluções de baixo carbono e investe em 
projetos socioambientais para a recuperação e conservação de florestas.

	No último período do segundo parágrafo, as formas verbais 'investe' e 'promove', flexionadas na 3º pessoa do singular, 
		concordam com o termo 'matriz elétrica brasileira', que encerra o período imediatamente anterior.

	[bg_red]ERRADO.[reset]
			O sujeito está elíptico, 'ela' investe porque concordam com PETROBRAS.
			O sujeito está elíptico, 'ela' promove porque concordam com PETROBRAS.

Questão 07:

Em março do ano seguinte, quando o imperador outorgou a primeira Constituição brasileira, ela se afastava pouco do projeto elaborado em 1823, mas
[yellow]continha[reset] uma diferença crucial: os poderes eram quatro e incluíam um Moderador.

	A forma verbal 'continha' estabelece concordância com o mesmo referente da forma pronominal 'ela' - 'a primeira constituição brasileira'

quem que outorgou? 'o imperador' - Sujeito simples
 Portanto, 'a primeira constituição brasileira' não pode ser sujeito do verbo outorgou, porque o sujeito já é 'o imperador'.
	 	Mas 'a primeira constituição brasileira' funciona como sujeito elíptico de outro verbo, de 'continha', quem continha? 'ela' Sujeito elíptico
'ela' - (sujeito simples explícito) se afastava pouco do projeto elaborado em 1823 mas 'continha' uma diferença crucial 'ela' continha - Sujeito Elíptico - 
					' a primeira constituição brasileira '

				ERRADO - são referentes diferentes, um o sujeito é simples e o outro é OCULTO.

Questão 08: 

	Há evidências de que a oferta de medicação domiciliar pelas operadoras de planos de saúde [yellow]traz[reset] efeito positivo aos beneficiários.

	A forma verbal 'traz' está no singular porque concorda com o núcleo do sujeito: 'a oferta.'

		'a oferta de medicação domiciliar pelas operadoras de planos de saúde' -> sujeito
		'oferta' -> núcleo do sujeito somente palavra isolado / artigo não conta ERRADA A QUESTÃO

Questão 09:

	A universitária Amanda, de 20 anos de idade, é a primeira negra eleita miss DF. A modelo, que representou o Núcleo Bandeirante,
quase desistiu do mundo da moda, pois exigiram que ela alisasse o cabelo, afinasse o nariz e mudasse os traços.

	No trecho 'exigiram que ela alisasse o cabelo, afinasse o nariz e mudasse os traços', o sujeito da forma verbal 'exigiram' é indeterminado.

'a universitária Amanda' -> Sujeito
	[blue]Sintaticamente o verbo 'exigiram' refere-se ao sujeito 'eles/elas' 3º pessoa do plural, sem referente textual, logo é sujeito indeterminado.[reset]


questão 11:

	De acordo com a norma-padrão, a frase que não precisa ser corrigida pelo Professor Carlos Góis, mencionado pelo texto II, é:

a. Houveram muitos acertos naquela prova.
b. Existia poucos alunos com dúvidas na sala.
c. Ocorreram poucas dúvidas sobre a matéria.
d. Devem haver muitos aprovados este ano.
e. Vão fazer dois anos que estudei a matéria.


a. Houveram muitos acertos naquela prova.

	O verbo HAVER no frase está empregado no sentido de existir, portanto é impessoal que não admite sujeito e somente fica no singular. 
		
	O correto seria:  [blue]Houve muitos acertos naquela prova.[reset]

b. Existia poucos alunos com dúvidas na sala.

	'poucos alunos com dúvidas' -> sujeito
	'poucos' -> intensificador do núcleo no plural
	'alunos' -> núcleo do sujeito, plural 
	
	O verbo existir é PESSOAL, precisa concordar em número com o sujeito, no plural também.
	Portanto o correto é: [blue]Existiam poucos alunos com dúvidas na sala.[reset]

c. Ocorreram poucas dúvidas sobre a matéria.

	'poucas dúvidas sobre a matéria' -> Sujeito
	'dúvidas' -> núcleo do sujeito

d. Devem haver muitos aprovados este ano.

	'devem haver' -> locução verbal
	'muitos aprovados este ano' -> sujeito
	'aprovados' -> núcleo

	O verbo haver no sentido de existir muitos aprovados é impessoal a qual não admite sujeito, portanto a locução deve ser IMPESSOAL.
	Logo 'devem haver' esta ERRADO. O correto é: 'deve haver muitos aprovados este ano

e. Vão fazer dois anos que estudei a matéria.

	'vão fazer' -> locução verbal
	O verbo fazer que indica tempo transcorrido é IMPESSOAl, não admite sujeito. Fica somente no singular
	O correto seria: vai fazer dois anos que estudei a matéria.

12. Em muitas das quais nunca [yellow]haviam lidado[reset] com migrações desse porte anteriormente.
	O verbo 'haver' tem a concordância estabelecida corretamente com o sujeito da oração a que se refere.
A mesma correção NÃO ocorre em uma das alternativas a seguir por se tratar de caso em que o verbo 'haver' pode ser classificado como impessoal:

a. haveriam reuniões no auditório hoje, mas surgiram alguns imprevistos.
b. Se eles houvessem chegado mais cedo, saberiam do que se trata a convocação.
c. Haveremos de chegar ao destino ainda hoje, conforme traçado em nosso planejamento.
d. Haveriam de ganhar o prêmio caso estivessem devidamente preparados para a apresentação.

[bg_blue]'haviam lidado' -> locução verbal. O 'haviam' está com verbo auxiliar deverá concordar com o referente 'muitas'[reset]

[red]Na alternativa a.[reset]
 'HAVERIAM' está como verbo principal e no sentido de existir funciona como IMPESSOAL, portanto não admite sujeito, só pode ficar no singular
	[blue]O correto seria: Haveria reuniões no auditório hoje...[reset]
[red]Na alternativa b.[reset] 'houvessem chegado' o verbo 'haver' é auxiliar concorda com o sujeito simples 'eles'
[red]Na alternativa c.[reset] 'haveremos de chegar' o verbo 'haver' é auxiliar concorda com o sujeito elíptico 'nós'
[red]Na alternativa d.[reset] 'haveriam de ganhar' o verbo 'haveriam' é auxiliar concorda com o sujeito elíptico 'eles'    

13. Há um toque de filosofia

	A única variação estrutural correta para a expressão destacada na oração em evidência é:

a. haverão uns toques de filosofia
b. existirão uns toques de filosofia
c. terão uns toques de filosofia
d. existirá uns toques de filosofia


a. haverão uns toques de filosofia   -> [blue]o verbo 'haver' é impessoal, não admite sujeito, no singular ->[reset] 
                O correto seria: 'haverá uns toques de filosofia'
b. existirão uns toques de filosofia -> [blue]'existirão' no plural, verbo pessoal, concordando com o sujeito no plural -> 'uns toques'[reset]
c. terão uns toques de filosofia     -> [red]'ter' no sentido de existir é INCORRETO. É usado somente para posse ou locução verbal[reset]
d. existirá uns toques de filosofia  -> [red]'uns toques' sujeito no plural -> Portanto verbo no plural existir, pessoal, deve concordar com o sujeito.[reset]
                                                [red]'existirá' não está no plural para concordar com 'uns toques', questão ERRADA.[reset]

TER: no sentido de existir, ocorrer, acontecer, tempo transcorrido -> TUDO ERRADO

	[red]O verbo TER nao pode ser usado nesses sentidos.[reset]

		Tem uma pessoa parada em frente ao meu portão. <- [red]ERRADO[reset]
		Há uma pessoa parado em frente ao meu portão    <- [green]CORRETO[reset]

		Tem gente no banheiro <- ERRADO
		Há gente no banheiro <- CORRETO

		Moça, tem pão? <- ERRADO
		Moça, há pão?  <- CORRETO

O verbo TER serve para indicar POSSE e para locução verbal.

	Ela tinha estudado bastante. <- ERRADO

	Ela havia estudado bastante. CORRETO       

Esporadicamente, outros verbos podem ser usados como impessoais, tais como ESTAR e FICAR (indicando tempo meteorológico), 
PASSAR e PARECER (indicando tempo cronológico) e BASTAR E CHEGAR (indicando interrupção).

Como está frio aqui!

Ficou escuro de repente.

Passa das dezessete horas.

Parece sábado!

Basta de brigas!

Chega de contendas!                                             

Os verbos impessoais ficam sempre na 3.ª pessoa do singular.

Tem havido muitos incidentes durante a viagem.

Deve fazer muito frio à noite.

Está fazendo dez anos que não o vejo.

Costumam ser 21h 30min quando ele chega.

SUJEITO ORACIONAL:

Ocorre quando uma oração subordinada substantiva faz o papel de sujeito.

    O jogo é bom.

    'é' => verbo ser de ligação
    'bom' -> predicativo do sujeito
    'o jogo' -> sujeito simples ( núcleo do sujeito - 'jogo')

    É bom o jogo.

    'é' -> verbo de ligação
    'bom' -> predicativo do sujeito
    'o jogo' -> sujeito simples

    É bom que você jogue.

    'é' -> verbo SER, de ligação
    'bom' -> Predicativo do sujeito
    'que você jogue' <- sujeito oracional ( uma oração )
            'que' -> conjunção subornativa integrante // 'você' -> Pronome // 'jogue' -> verbo
        Se existe um verbo, existe uma oração.
        Dentro do sujeito oracional pode haver outro sujeito.

    Convém que Pedro vença a luta.

        'convém' -> verbo intranstivo ( não precisa de complemento )
        'que Pedro vença a luta' -> Sujeito Oracional ( por causa do verbo 'vencer' )
        Repare que dentro do sujeito oracional, 'Pedro' é o sujeito simples de 'vença'

    Praticar exercícios frequentemente é bom para a saúde.

    verbo é -> verbo de estado, verbo de ligação
    'bom para a saúde' -> predicativo do sujeito
    quem é bom para a saúde? 'praticar exercícios frequentemente' é o sujeito oracional
    Núcleo do sujeito é um verbo: 'praticar' <- núcleo do sujeito oracional

        O pronome 'isso': pronome demonstrativo para substituir pelo sujeito

    Viver bem é fundamental

    quem é fundamental? 'viver bem' <- Sujeito oracional , verbo no infinitivo

        1.Iniciado pela conjunção integrante 'que':

        Seria importante que você parasse de fumar.

        quem será importante? 'que você parasse de fumar' <- sujeito oracional

        2.Iniciado por advérbios interrogativos: QUANDO, ONDE, COMO, POR QUE

        Já está previsto onde o jogo acontecerá.        

        Substituir pelo pronome 'isso': Já está previsto ISSO

        3.Iniciado pelos pronomes interrogativos 'que', 'qual' e 'quanto':

        Está combinado qual horário vamos nos encontrar?

        está combinado isso?

        'qual horário vamos nos encontrar' <- Sujeito oracional

        Não se sabe QUANTO será necessário para chegarmos lá.

        Não se sabe, isso.



14. No maranhão, 60,5% dos trabalhadores ocupados eram informais.

	Assinale a alternativa em que, alterando-se o período acima, independentemente da alteração de sentido, se tenha mantido correção gramatical.

a. No Maranhão, 60,5% da população estava na informalidade.
b. No Maranhão, dois terços dos trabalhadores estava na informalidade.
c. No Maranhão, 1,98% da população estavam na informalidade.
d. No Maranhão, mais de um trabalhador estavam na informalidade.


a. No Maranhão, 60,5% da população estava na informalidade.

	[red]Quem estava no informalidade?[reset] [blue]'60,5% da população'[reset] <- [red]Sujeito da oração[reset]
		[red]Núcleo[reset]: 60,5% <- [red]Plural[reset]
		[red]'da população'[reset] -> [blue]especificador do núcleo[reset] -> [red]singular[reset]

	[green]estavam/estava estão corretos. Concordância facultativa[reset]

b. No Maranhão, dois terços dos trabalhadores estava na informalidade.

	[blue]'dois terços dos trabalhadores'[reset] -> [red]sujeito[reset]
	[blue]'estava'[reset] -> [red]verbo no singular[reset]
	 [red]núcleo[reset] -> [blue]'dois terços'[reset] -> [red]plural[reset]
	 [red]especificador do sujeito[reset] -> [blue]'dos trabalhadores'[reset] ->[blue]	plural[reset]


	[bg_blue]Portanto, o verbo 'estar' não existe concordância facultativa, somente concordar no plural, [reset]
                    [bg_blue]pelo sujeito e núcleo e especificador no plural.[reset]

c. No Maranhão, 1,98% da população estavam na informalidade.

	[red]núcleo[reset] -> [yellow]1,98%[reset] -> [blue]SINGULAR[reset]
	[blue]especificador do núcleo[reset] -> [red]'população '[reset]-> [green]que está também no singular. Não existe concordância facultativa, somente no SINGULAR.[reset]

	            [blue]O correto seria: estava na informalidade[reset]                    

d. No Maranhão, mais de um trabalhador estavam na informalidade.

	[red]'mais de um trabalhador'[reset] -> [yellow]sujeito no singular[reset]
	[red]'estavam' portanto está errado, concordar com o sujeito no SINGULAR[reset]

		[blue]'mais de um trabalhador estava na informalidade.'[reset]

15. De acordo com a norma culta, existe outra possibilidade de concordância verbal em:

a. O governo federal já deixou bem claro que a prioridade da educação será o ensino básico.

b. De acordo com o artigo 206 da Constituição, as univerdades públicas são gratuitas, não podem cobrar mensalidades.

c. A maioria dos estudantes dessas universidades vem de escolas particulares, poderia pagar a mensalidade. 

d. Em diferentes países, universidades cobram mensalidades de estudantes.

e. Há excelentes defensores de ideias em cada lado da polêmica.

a. O governo federal já deixou bem claro que a prioridade da educação será o ensino básico.

	[red]quem é que deixou bem claro?[reset] [yellow] [blue]'o governo federal'[reset] ->[red] Sujeito Simples / núcleo [reset]-. [blue]governo[reset]
		[blue]'deixou'[reset] -> [red]verbo que deve concordar com o sujeito, singular[reset]

	[red]o ensino básico será o que?[reset] [yellow] [blue]'a prioridade da educação' [reset]-> [yellow]Sujeito / núcleo [reset]-> [green]prioridade, no singular[reset]
	[yellow] verbo 'será' no singular[reset] /[blue] especificador do núcleo também no singular[reset]

	[red]Não há outra possibilidade de concordância verbal na alterantiva A[reset]

b. De acordo com o artigo 206 da Constituição, as univerdades públicas são gratuitas, não podem cobrar mensalidades.

	[red]quem são gratuitas?[reset] [yellow] [blue]'as universidades públicas'[reset] -> sujeito[reset]
	[red]'são' verbo no plural concordando com o sujeito no plural[reset]

	[red]quem não podem cobrar mensalidades?[reset] [yellow] 'elas' sujeito elíptico referindo as universidades públicas, no plural.[reset]
		[red]somente no plural concordando com o sujeito[reset]

c. A maioria dos estudantes dessas universidades vem de escolas particulares, poderia pagar a mensalidade. 	

	[red]quem que vem de escolas particulares? 'a maioria dos estudantes dessas universidades' ->[yellow]  sujeito[reset]
		[red]núcleo[reset] -> maioria -[reset]>[red] singular[reset] // [yellow] 'dos estudantes'[reset] ->[red] especificador do núcleo no plural, podendo ter outra possibilidade[reset]
	de concordância
		[red]Acento diferencial : vem / vêm [reset]<- [yellow]Mais de um possibilidade de concordância[reset]

d. Em diferentes países, universidades cobram mensalidades de estudantes.

	[red]quem é que cobram mensalidades?[reset] 'universidades' <-[yellow]  núcleo do sujeito[reset]
		[red]'cobram' deve concordar com o sujeito no plural, nenhum possibilidade de concordância verbal facultativa[reset]


e. Há excelentes defensores de ideias em cada lado da polêmica.

	[red]'há'[reset] -> Verbo haver não admite sujeito por ser IMPESSOAl, podendo só ficar no singular.[reset]
		[red]Portanto não há outra possibilidade de concordância verbal.        [reset]
        '''        

    def exercicios_fixacao_sujeito(self):

        return'''
            Exercícios de fixação:

1. Ano: 2024 / Banca: Instituto Legatus - Legatus / Prova: Legatus - Prefeitura de Castelo do Piauí - Profissional de Educação Física - 2024

Assinale a alternativa em que o termo marcado apresente a função sintática de sujeito simples.

A.Até 1990, inexistiam [yellow]instituições mercantis[reset]; atualmente, em conjunto com as demais privadas [...].
B.Numa geração, houve [yellow]um extraordinário avanço global[reset] do nível superior[...].
C.[yellow]Contextos diversos de articulações entre redes de universidades públicas[reset], faculdades privadas mercantis e instituições sem fins de lucro, por meio das modalidades presencial e a distância (EAD), configuram resultados diferentes.
D.[...] faculdades privadas mercantis e instituições sem fins de lucro, por meio das modalidades presencial e a distância (EAD), configuram [yellow]resultados diferentes.[reset]
E.[...] o processo de expansão da educação superior brasileira está produzindo e reproduzindo [yellow]as desigualdades existentes na sociedade.	[reset]

A.Até 1990, inexistiam [yellow]instituições mercantis[reset]; atualmente, em conjunto com as demais privadas [...].

	[red]quem inexistiam?[reset] [blue]'instituições mercantis'[reset] -> sujeito simples

 [bg_blue]O verbo 'inexistiam' está no plural, concordando com o sujeito 'instituições mercantis'. [reset]


B.Numa geração, houve [yellow]um extraordinário avanço global[reset] do nível superior[...].

[bg_red]o termo 'um extraordinário avanço global' é o objeto direto do verbo 'houve', e não o sujeito da oração.[reset]


C.[yellow]Contextos diversos de articulações entre redes de universidades públicas[reset], 
faculdades privadas mercantis e instituições sem fins de lucro, por meio das modalidades presencial e a distância (EAD), configuram resultados diferentes.

[red]quem configura resultados diferentes?[reset] [blue]'contextos diversos de articulações entre redes de universidades públicas'[reset] <- [bg_red]sujeito composto[reset]
	[bg_blue]Portanto, não é sujeito simples e sim composto, dois núcleos.[reset]


D.[...] faculdades privadas mercantis e instituições sem fins de lucro, por meio das modalidades presencial e a distância (EAD), 
configuram [yellow]resultados diferentes.[reset]

	[red]quem configuram?[reset] [blue]'faculdades privadas mercantis e instituições sem fins de lucro'[reset] <-[green] Sujeito[reset]
		[bg_red]'resultados diferentes' é objeto direto do verbo configuram[reset]

2. 17. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC
Prova: FUNDATEC - Prefeitura de Cruz Alta - Dentista ESF - 2024

Assinale a alternativa que indica a correta classificação do sujeito da forma verbal “clama” no trecho “O estresse diário clama por esse ‘prêmio’ hormonal”.

A. Simples.
B. Composto.
C. Oculto.
D. Indeterminado.
E. Inexistente.


O sujeito da forma verbal 'clama' é 'O estresse diário', que é um sujeito simples, pois é constituído por um núcleo (estresse) e seus determinantes (o, diário). 
Alternativa 'A'

No item 'B'  O sujeito composto é aquele que possui mais de um núcleo. 
No caso da frase 'O estresse diário clama por esse ‘prêmio’ hormonal', o sujeito é 'O estresse diário', que possui apenas um núcleo (estresse).

No item 'C'. O sujeito oculto é aquele que não está explícito na oração, mas pode ser identificado pelo contexto ou pela desinência verbal. 
o trecho 'O estresse diário clama por esse ‘prêmio’ hormonal', o sujeito 'O estresse diário' está explícito.

No item 'D'.  O sujeito indeterminado ocorre quando não se pode ou não se quer identificar o sujeito da ação. 
No trecho 'O estresse diário clama por esse ‘prêmio’ hormonal', o sujeito 'O estresse diário' está claramente identificado.

No item  'E'.  O sujeito inexistente ocorre em orações com verbos impessoais, como os que indicam fenômenos da natureza ou os verbos 'haver' e 'fazer' no 
sentido de tempo decorrido. No trecho 'O estresse diário clama por esse ‘prêmio’ hormonal', o verbo 'clama' tem um sujeito explícito ('O estresse diário').

3. Ano: 2024  /  Banca: Associação dos Municípios do Extremo Oeste de Santa Catarina - AMEOSC
Prova: AMEOSC - Prefeitura de Palma Sola - Psicólogo - 2024
Leia com atenção a afirmativa abaixo:

Este é o enfermeiro [yellow]por quem[reset] fui muito bem acompanhado.

Qual é a função sintática dos termos destacados?

A. Objeto direto.
B. Objeto indireto.
C. Sujeito.
D. Agente da passiva.


O termo 'por quem' não pode ser classificado como objeto direto, pois o objeto direto é o complemento de um verbo transitivo direto, sem preposição. 
No caso, 'por quem' está introduzido por uma preposição, o que já elimina essa possibilidade.

O termo 'por quem' também não pode ser classificado como objeto indireto, pois o objeto indireto é o complemento de um verbo transitivo indireto, 
introduzido por uma preposição. 
No entanto, 'por quem' está relacionado ao verbo 'acompanhar' na voz passiva, e não como complemento de um verbo transitivo indireto.

O termo 'por quem' não pode ser classificado como sujeito, pois o sujeito é o termo da oração que concorda com o verbo em número e pessoa. 
No caso, 'por quem' está introduzido por uma preposição e não exerce a função de sujeito na oração.

O termo 'por quem' está de acordo com o gabarito da banca. Ele exerce a função de agente da passiva, pois na frase :
'Este é o enfermeiro por quem fui muito bem acompanhado', 'por quem' indica o agente da ação na voz passiva, ou seja, a pessoa que realizou a ação de acompanhar.        

4. Ano: 2024  /  Banca: Instituto de Desenvolvimento Humano e Tecnológico - IDHTEC
Prova: IDHTEC - Câmara de Cortês - Auxiliar de Serviços Gerais - 2024
 
No trecho: “Após algumas tentativas frustradas, desistiu da Medicina, cursou Ciência Política e seguiu carreira artística”, 
os verbos estão sem sujeito explícito, mas é possível determinar a que termo do texto eles se referem. 
Esse termo é:

A.  tentativas
B. a artista
C. sobreviver
D.  -la
E.  carreira

O item 'tentativas' não pode ser o sujeito dos verbos 'desistiu', 'cursou' e 'seguiu' estão no pretérito perfeito do indicativo.
Pois 'tentativas' é um substantivo feminino plural e os verbos estão conjugados na terceira pessoa do singular.

O item 'a artista' é o sujeito oculto dos verbos 'desistiu', 'cursou' e 'seguiu'. A artista é a pessoa que realizou as ações descritas. 

O item 'sobreviver' é um verbo e não pode ser o sujeito dos verbos 'desistiu', 'cursou' e 'seguiu'. 

O item '-la' é um pronome oblíquo átono e não pode ser o sujeito dos verbos 'desistiu', 'cursou' e 'seguiu'.

O item 'carreira' é um substantivo feminino singular e não pode ser o sujeito dos verbos 'desistiu', 'cursou' e 'seguiu', 
pois o sujeito deve ser uma pessoa que realiza as ações.

5. Ano: 2024 /  Banca: Fênix Instituto Ltda / 
Prova: Fênix Instituto Ltda - Prefeitura de Major Vieira - Professor - Área: Língua Portuguesa - 2024 
 
Identifique a função sintática da expressão "Uma resolução publicada pelo Banco Central" no início do texto.

A. Objeto direto.
B. Sujeito da oração.
C. Complemento nominal.
D. Adjunto adverbial.

A expressão 'Uma resolução publicada pelo Banco Central' não pode ser classificada como objeto direto, 
pois o objeto direto é o termo que completa o sentido de um verbo transitivo direto, sem a presença de preposição.

A expressão 'Uma resolução publicada pelo Banco Central' é o sujeito da oração. 
O sujeito é o termo da oração que concorda com o verbo e sobre o qual se faz uma declaração. 
Neste caso, a declaração é que a resolução determina que as instituições financeiras promovam ações de educação financeira.

'Uma resolução' -> Sujeito simples
'publicada pelo Banco Central': -> 'locução adjetiva' que qualifica o substantivo "resolução": Adjunto Adnominal
Agente da Passiva: 'Pelo Banco Central': indicando quem realizou a ação de publicar.

Na frase "Uma resolução publicada pelo Banco Central",  não há verbo principal que permita a formação de sujeito e predicado.
  Portanto, não podemos classificar "publicada pelo Banco Central" como predicativo do sujeito,
   porque a frase é um fragmento nominal (não é uma oração completa).

Predicativo do sujeito ocorre apenas em orações que possuem um verbo de ligação, como em: "A resolução foi publicada pelo Banco Central."
Nesse caso, "publicada pelo Banco Central" seria predicativo do sujeito,
pois complementa o sujeito ("a resolução") por meio do verbo de ligação "foi".

Frase Ativa:

"O Banco Central publicou uma resolução."

Sujeito: O Banco Central: Sujeito agente.

Publicou: Verbo transitivo direto.

Objeto Direto: Uma resolução: Objeto direto, recebendo a ação do verbo.

	Gabarito  letra 'B'	

A expressão 'Uma resolução publicada pelo Banco Central' não pode ser classificada como complemento nominal, 
pois o complemento nominal é o termo que completa o sentido de um nome (substantivo, adjetivo ou advérbio) e geralmente vem precedido de preposição. 

O núcleo da frase é "resolução", que é um substantivo concreto.
A expressão "publicada pelo Banco Central" desempenha o papel de caracterizar ou qualificar a "resolução", explicando quem realizou a ação de publicar.
Isso a torna um adjunto adnominal, porque está diretamente ligada ao substantivo CONCRETO, indicando o autor da ação.

Para que fosse um complemento nominal, o substantivo "resolução" precisaria ser abstrato e sofrer a ação indicada pelo termo "pelo Banco Central".
No entanto, na frase, "resolução" não é abstrato e não sofre a ação de publicar; pelo contrário, a locução "publicada pelo Banco Central" apenas qualifica o substantivo.

A expressão 'Uma resolução publicada pelo Banco Central' não pode ser classificada como adjunto adverbial, 
pois o adjunto adverbial é o termo que modifica o verbo, o adjetivo ou outro advérbio, indicando circunstâncias como tempo, lugar, modo, etc. 

6. 21. Ano: 2024 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRQ 15 - Fiscal - 2024 

Na linha 3, o sujeito de “anunciou” está posposto ao verbo.

anunciou a Academia Real das Ciências dia 4 da Suécia.

CORRETO

A frase 'anunciou a Academia Real das Ciências da Suécia' apresenta o verbo 'anunciou' seguido pelo sujeito 'a Academia Real das Ciências da Suécia'. 
Isso confirma que o sujeito está posposto ao verbo, ou seja, aparece depois do verbo na estrutura da frase. 
Essa construção é gramaticalmente correta e comum em português, especialmente em contextos formais ou jornalísticos, 
onde a ênfase pode ser dada ao verbo ou à ação antes de mencionar o sujeito. 

6. 22. Ano: 2024 / Banca: Instituto Brasileiro de Apoio e Desenvolvimento Executivo - IBADE
Prova: IBADE - Prefeitura de Joinville - Agente de Combate às Endemias - 2024

Como se classificam os sujeitos dos verbos em destaque no período 
“Diversos cientistas [yellow]estudam[reset] como a fala é produzida e [yellow]tentam[reset] entender por que algumas pessoas não [yelloww]conseguem[reset] falar com facilidade.” (3º parágrafo)?

A. Composto | Composto | Simples.
B. Indeterminado | Indeterminado | Composto.
C. Simples | Inexistente | Composto.
D. Simples | Oculto | Simples.
E. Simples | Simples | Indeterminado.

[red]quem estudam?[reset]  [yelllow]'diversos cientistas'[reset] -> sujeito simples / 'estudam' eles concordando em número com o sujeito
[red]quem tentam?[reset] [yelllow]'eles'[reset] ->  sujeito elíptico, oculto ou desinencial
[red]quem não conseguem?[reset] [yelllow]'pessoas'[reset] ->  sujeito simples

    Alternativa 'D'

7. Ano: 2024 / Banca: Fundação Universidade Empresa de Tecnologia e Ciências - FUNDATEC
Prova: FUNDATEC - Câmara de Piracicaba - Controlador Interno - 2024 

Tendo em vista o fragmento adaptado do texto “Os nomes das pessoas mais antigas são compridos”, assinale a alternativa que apresenta a correta classificação do sujeito.

A. Simples.
B. Composto.
C. Indeterminado.
D. Oculto.
E. Inexistente.

'os nomes das pessoas mais antigas' -> sujeito
'nomes' -> núcleo do sujeito
'das pessoas' -> não faz parte do núcleo, pois está preposicionado pela preposição 'de' + 'as'.   

8. Língua Portuguesa  Sujeito / Ano: 2024
Banca: FUNDEP Gestão de Concursos - FUNDEP / Prova: FUNDEP - CIESP - Assistente Operacional - 2024

COLUNA I

1. Sujeito
2. Objeto direto
3. Predicado nominal
4. Oração subordinada

COLUNA II

( ) “[...] e continuou exibindo [yellow]o seu fenômeno[reset] [...].”

( ) “A partir daí, [yellow]Hans[reset] passou por vários donos [...].”

( ) “[...] [yellow]quando[reset], acredita-se, [yellow]foi morto em combate.[reset]”

( ) “Von Osten [yellow]não ficou convencido com as conclusões de Pfungst [reset][...].”


'o seu fenômeno' é o objeto direto do verbo 'exibindo'; 
'Hans' é o sujeito da oração 'Hans passou por vários donos'; 
'quando, acredita-se, foi morto em combate' é uma oração subordinada adverbial temporal; 
'não ficou convencido com as conclusões de Pfungst' é um predicado nominal, pois o verbo 'ficar' é de ligação e 'convencido' é o predicativo do sujeito 'Von Osten'.

9. Língua Portuguesa  Sujeito / Ano: 2024 / Banca: Instituto de Avaliação Nacional - IAN - IAN
Prova: IAN - Prefeitura de Três Rios - Auditor de Controle Interno - 2024

Três Rios

Três Rios é conhecido por sua natureza e prédios históricos. 
As atividades ao ar livre e os esportes radicais são as atrações mais procuradas, como a prática de rafting no rio Paraibuna. 
Lá, os turistas têm a oportunidade de descer 22 km, entre seis corredeiras. 
O ponto final de descida é no encontro dos rios Paraibuna, Paraíba do Sul e Piabanha, formando o único delta triplo fluvial da América Latina. 
Na região, ainda é possível realizar rapel, tirolesa e escalada.
Além do rafting, o município oferece diversos atrativos, tanto na sede quanto no seu entorno, 
e ainda promove uma das melhores festas de carnaval do interior do Estado. Vale a pena visitar a produção de cachaça local e experimentar as cervejas artesanais. 
Há, ainda, gastronomia diversificada e rica produção de artesanato.
A Cidade também possui importantes patrimônios históricos, como a Ponte das Graças, o coreto da Praça da Autonomia e o Teatro Celso Peçanha. 
Igrejas históricas, como a Capela Nossa Senhora da Piedade e a Igreja de São Sebastião, construídas no século XIX e XX, respectivamente, são opções de passeios.

Assinale a alternativa que apresenta um sujeito diferente do presente nos demais trechos.


A. ‘‘Três Rios é conhecido por sua natureza e prédios históricos’’.
B. ‘‘As atividades ao ar livre e os esportes radicais são as atrações mais procuradas, como a prática de rafting no rio Paraibuna’’.
C. ‘‘Além do rafting, o município oferece diversos atrativos, tanto na sede quanto no seu entorno’’.
D. ‘‘A Cidade também possui importantes patrimônios históricos, como a Ponte das Graças, o coreto da Praça da Autonomia e o Teatro Celso Peçanha’’.

No item 'A'  
Neste item, o sujeito da oração é 'Três Rios', que é mencionado explicitamente. 
A oração declara algo sobre 'Três Rios', fazendo dele o sujeito da sentença. Este item não apresenta um sujeito diferente dos demais trechos.

B. ‘‘As atividades ao ar livre e os esportes radicais são as atrações mais procuradas, como a prática de rafting no rio Paraibuna’’.

Aqui, o sujeito da oração são 'As atividades ao ar livre e os esportes radicais', que diferem dos sujeitos apresentados nas outras alternativas, que se referem diretamente a 'Três Rios' ou a aspectos relacionados à cidade

    [red]quem são as atrações mais procuradas?[reset] [blue]'as atividades ao ar livre e os esportes radicais'[reset] <- sujeito

C. ‘‘Além do rafting, o município oferece diversos atrativos, tanto na sede quanto no seu entorno’’.

Neste item, o sujeito é 'o município', referindo-se novamente a 'Três Rios'. A oração fala sobre o que o município oferece, mantendo o foco na cidade como sujeito da sentença. Este item não apresenta um sujeito diferente dos demais trechos, 

        [red]quem que oferece diversos atrativos?[reset] [blue]'o município'[reset] <- Sujeito

D. ‘‘A Cidade também possui importantes patrimônios históricos, como a Ponte das Graças, o coreto da Praça da Autonomia e o Teatro Celso Peçanha’’.

O sujeito deste item é 'A Cidade', uma referência direta a 'Três Rios'. A oração destaca os patrimônios históricos que a cidade possui, fazendo de 'Três Rios' o sujeito da sentença. Este item não apresenta um sujeito diferente dos demais trechos.

                [red]quem que possui importantes patrimônicos históricos?[reset] [blue]'a cidade'[reset] ->[red] Sujeito[reset]

10. Ano: 2024 / Banca: Instituto Avança São Paulo - Avanca SP / Prova: Avança SP - Câmara de Itapecerica da Serra - Contador - 2024

Analise as sentenças a seguir e assinale a alternativa em que se verifica um sujeito composto.

A. As fantasias de palhaço feitas à mão pelas costureiras locais eram doadas a instituições de arte e cultura popular.
B. Os funcionários recém-contratados da empresa foram convidados para um coquetel.
C. Todos já sabiam que os garotos do quinto ano ganhariam o prêmio da feira de ciências.
D. Quando se é criança, tem-se a percepção de um mundo perfeito.
E. Jovens e adultos moradores da Região Metropolitana de São Paulo poderão se consultar gratuitamente nesta clínica.

[red]No item 'A'[reset]: possui um sujeito simples, que é 'As fantasias de palhaço feitas à mão pelas costureiras locais'.

    [yellow]Lembrando que sujeito não pode iniciar com preposição, sendo assim:[reset] [red]'de palhaço', 'à mão', 'pelas constureiras locais'[reset] não podem ser.
    [red] Quem eram doadas a instituições de arte e cultura popular? [reset] 'As fantasias de palhaço feitas à mão pelas costureiras locais'
    [yellow] Adjunto Adnominal[reset]:  'As' -> Artigo determinante do núcleo 'fantasias'
    [yellow] Adjunto Adnominal [reset]: 'de palhaço' -> [blue]locução adjetiva que especifica o núcleo 'fantasias'[reset]
    [yellow] Adjunto Adnominal [reset]: 'feitas à mão pelas constureiras locais' (oração subordinada adjetiva reduzida)

    Predicado:

    [yellow]"Eram doadas a instituições de arte e cultura popular"[reset]

    [red]Verbo principal[reset]: 'eram' ( verbo de ligação, de estado )
    [red]Predicativo do sujeito[reset]: 'doadas a instituições de arte e cultura popular'
    [yellow]'doadas'[reset]: particípio usado como adjetivo, caracterizando o sujeito 'as fantasias'
    ' a instituições de arte e cultura popular' -> complemento verbal da forma 'doadas'
    ' de arte e cultura popular ' -> complemento nominal, especificando o tipo de instituições.

        Tipo de predicado: Verbo-nominal

[red]No item 'B'[reset]: possui um sujeito simples, que é 'Os funcionários recém-contratados da empresa'.

        Os funcionários recém-contratados da empresa foram convidados para um coquetel.

        [reset]quem que foram convidados para um coquetel?[reset] -> [yellow] Os funcionários recém-contratados da empresa[reset] -> SUJEITO

        A frase é composta por um sujeito e um predicado verbal com a voz passiva.

        [red] Núcleo do sujeito:[reset] -> 'funcionários' (substantivo)
        [red]Adjunto Adnominal[reset] -> 'os' -> Artigo determinante para o núcleo
        [red]Adjunto Adnominal[reset] -> 'recém-contratados' (locução adjetiva que caracteriza o nucleo)
        [red]Adjunto Adnominal[reset] -> 'da empresa' (locução adjetiva que especifica )
                [bg_blue] Lembrando que Adjunto Adverbial de lugar especifica ação do 'verbo' [reset]

        PREDICADO:

        [yellow]'foram convidados para um coquetel'[reset]

        [red]verbo principal:[reset] [blue] foram convidados ( locução verbal na voz passiva )[reset]
        [red]'foram'[reset] -> [blue] verbo auxiliar [reset]
        [red]'convidados'[reset] -> [blue] participio que indica ação sofrida pelo sujeito [reset]
        [red]'para um coquetel'[reset] -> [blue] Agora sim temos um Adjunto Adverbial de finalidade [reset]

[red]No item 'C'[reset]: possui um sujeito simples, 'todos'.

A frase completa: Todos já sabiam que os garotos do quinto ano ganhariam o prêmio da feira de ciências.

[red]Análise sintática:[reset]

    1° Oração:
    
    Todos já sabiam que os garotos do quinto ano ganhariam o prêmio da feira de ciências.

[red]'todos já sabiam' [reset]-> [yellow]Oração principal[reset] -> SUJEITO -> [blue]'todos'[reset]
[red]'já sabiam'[reset] -> [yellow]Predicado Verbal[reset]
[red]'já' [reset]->[yellow] adjunto adverbial de tempo[reset]
[red]'sabiam' [reset]->[yellow] verbo transitivo direto[reset]

    [yellow]2° Oração:[reset]

[red]Oração subordinada do verbo 'sabiam':[reset] [blue]'que os garotos do quinto ano ganhariam o prêmio da feira de ciências' [reset]->[blue] Oração subordinada substantiva objetiva direta[reset]

    [red]'que'[reset] ->[blue] conjunção subordinada integrante [reset]
    [red]Sujeito da oração subordinada[reset] -> [yellow]'Os garotos do quinto ano'[reset]
    [red]núcleo[reset] -> [yellow]'garotos'[reset]
    [red]Adjunto Adnominal [reset]-> [blue]'Os'[reset] ->[yellow] artigo que determina o sujeito[reset]
    [red]Adjunto Adnominal [reset]-> [yellow]'do quinto ano' (locução adjetiva)[reset]

    [blue]Predicação:[reset]

    [red]Predicado verbal da 2º oração subordinada:[reset] [yellow]'ganhariam o prêmio da feira de ciências'[reset]
    [red]Núcleo verbal:[reset] [yellow] 'ganhariam' ( verbo transitivo direto )[reset]
    [red]quem ganha, ganha o que? [reset] - [yellow]'o prêmio da feira de ciências'[reset] -> [red] objeto direto[reset]
    [red]Repare que o núcleo é nominal[reset]: [yellow]'prêmio' (substantivo)[reset]
        [red]Adjunto adnominal [reset]: [yellow]artigo 'o' determinante para o núcleo do objeto direto[reset]
        [red]Adjunto adnominal [reset]: [yellow]'da feira de ciências' [reset]-> [red]locução adjetiva[reset]


[red]No item 'D'[reset]: possui um sujeito indeterminado, indicado pelo uso do pronome 'se'.

        Repare que são dois pronomes 'se' na oração.

        Quando [yellow]se[reset] é criança, tem-[yellow]se[reset] a percepção de um mundo perfeito.

        1º oração: 'quando se é criança'
        Oração subordinada adverbial temporal, utilizada pela conjunção subordinativa adverbial de tempo, 'QUANDO'
        introduzindo a oração subordinada.

        'é' -> verbo SER de estado, serve como verbo de ligação com o sujeito indeterminado SE, chamado de IIS.
        Portanto 'criança' é uma característica do sujeito indeterminado, sendo assim, é Predicativo do Sujeito. Está qualificando o sujeito.

        2° Oração:

        tem-[yellow]se[reset] a percepção de um mundo perfeito.

        quem tem, tem algo: 'a percepção de um mundo perfeito' <- objeto direto
        'de um mundo perfeito' -> Complemento nominal -> 

        o "se" não faz o sujeito da oração sofrer a ação do verbo,
        mas indica que o sujeito é indeterminado. O sujeito da oração é indeterminado,
        Não há uma voz passiva aqui, pois a percepção não está sofrendo a ação de "ter",
        mas sendo simplesmente o objeto de "ter" no contexto de uma percepção genérica.




[red]No item 'E'[reset]: possui um sujeito composto, que é 'Jovens e adultos (núcleos) moradores da Região Metropolitana de São Paulo'  

11. Ano: 2024 / Banca: Instituto Consulplan / Prova: Instituto Consulplan - Câmara de Itajubá - Controlador Interno - 2024 

“A escrita já dava nervosismo, da oral muitos nunca se recuperaram inteiramente, pela vida afora.” (3º§). 
Assinale a afirmativa que contém a justificativa correta sobre a organização sintática dos elementos no fragmento anterior.

A. É um período simples formado por duas orações.
B. O sujeito da segunda oração é “prova oral” e concorda com o verbo “dava”.
C. O sujeito da segunda oração é “muitos” e concorda com o verbo “recuperaram”.
D. O sujeito da primeira oração é oculto e está marcado por uma desinência verbal.

[red]O item 'A'[reset]  -> afirma que o período é simples e formado por duas orações. 
No entanto, um período simples é composto por apenas uma oração. 
O fragmento apresentado é um período composto, pois possui duas orações: 'A escrita já dava nervosismo' e 'da oral muitos nunca se recuperaram inteiramente, pela vida afora'. 

[red]No item 'B'[reset] -> No entanto, o sujeito da segunda oração é 'muitos', que concorda com o verbo 'recuperaram'. 
'Prova oral' é parte do complemento da primeira oração.

[green]O item 'C'[reset]  -> Afirma corretamente que o sujeito da segunda oração é 'muitos' e que concorda com o verbo 'recuperaram'. 
A análise está correta, pois 'muitos' é o sujeito da oração 'muitos nunca se recuperaram inteiramente, pela vida afora'.

[red]No item 'D'[reset] -> [red]INCORRETO.[reset] O sujeito da primeira oração é 'A escrita', que é um sujeito simples e explícito. 

12. Ano: 2024 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - CENSIPAM - Analista - Área: Tecnologia da Informação - 2024 
[yellow]O Ministério do Meio Ambiente e o Banco do Brasil[reset] firmaram um acordo de cooperação técnica para estimular o desenvolvimento socioeconômico sustentável de comunidades da região amazônica.

No primeiro período do texto, o termo sublinhado classifica-se em sujeito:

A. composto.
B. simples.
C. inexistente.
D. indeterminado.
E. desinencial.

O sujeito da oração é 'O Ministério do Meio Ambiente e o Banco do Brasil', 
que é composto por dois núcleos: 'Ministério do Meio Ambiente' e 'Banco do Brasil'. Portanto, o sujeito é classificado como composto.

12. Ano: 2024 / Banca: Instituto de Apoio à Universidade de Pernambuco - UPENET IAUPE
Prova: UPENET/IAUPE - Cãmara de Tabira - Técnico em Controle Interno - 2024

Em “O que existe são pessoas que lutam PELOS SEUS SONHOS ou desistem DELES.”, 
os termos destacados em maiúsculo (pelos seus sonhos/deles) exercem sintaticamente a função de:

A. sujeitos.
B. complementos verbais.
C. complementos nominais.
D. adjuntos adverbiais.
E. predicativos.

Os termos 'pelos seus sonhos' e 'deles' não exercem a função de sujeitos. 
O sujeito é o termo sobre o qual se faz uma declaração, e neste caso, os termos destacados são complementos verbais, não sujeitos.

Os termos 'pelos seus sonhos' e 'deles' são complementos verbais. 
'Lutar' é um verbo transitivo indireto que exige complemento introduzido por preposição ('pelos seus sonhos'), e 
'desistir' é um verbo transitivo indireto que também exige complemento introduzido por preposição ('deles').

Os termos 'pelos seus sonhos' e 'deles' não são complementos nominais. 
Complementos nominais completam o sentido de um nome (substantivo, adjetivo ou advérbio) e não de um verbo.

Os termos 'pelos seus sonhos' e 'deles' não são adjuntos adverbiais. 
Adjuntos adverbiais são termos que modificam o verbo, indicando circunstâncias como tempo, lugar, modo, etc. 
Aqui, os termos destacados completam o sentido dos verbos 'lutar' e 'desistir'.

Os termos 'pelos seus sonhos' e 'deles' não são predicativos. 
Predicativos são termos que atribuem uma característica ao sujeito ou ao objeto, geralmente ligados por um verbo de ligação.

13. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - DATAPREV - Auxiliar Técnico de Enfermagem - 2024 

Das opções a seguir, assinale aquela que apresenta sujeito expresso na oração.

A. Não havia remédio senão corresponder a brindes tão obrigativos.
B. Encontrando Leopoldo, disseram duas palavras sobre ela.
C. Estabeleceu-se um cordão sanitário entre a velhice e a mocidade.
D. Certamente... não se chegará sempre cedo demais onde se corre algum risco?
E. Ao terceiro dia amanheceu.

[red]No item 'A'[reset]. O sujeito é indeterminado. O verbo 'havia' é impessoal, e não há um sujeito expresso na oração.
[red]No item 'B'[reset]. O sujeito é indeterminado. O verbo 'disseram' está na terceira pessoa do plural, mas não há um sujeito expresso que identifique quem realizou a ação.
[red]No item 'C'[reset]. 'Estabeleceu-se um cordão sanitário entre a velhice e a mocidade.', o sujeito é 'um cordão sanitário', que está expresso e é o núcleo do sujeito.

    quem estabelece, estabele algo: transitivo direto
    'se' é particula apassivadora, indicando que o sujeito sofre a ação ( voz passiva sintética )
    Portanto, 'um cordão sanitário' é o sujeito paciente que sofre a ação de estabelecer
    'entre a velhice e a mocidade' -> é adjunto adverbial de lugar indicando o espaço onde o cordão sanitário foi estabelecido.

[red]No item 'D'[reset].

        'ao terceiro dia' -> não pode ser sujeito por iniciar com preposição
        'amanheceu' -> verbo intransitivo

14. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - STN - Auditor Federal de Finanças e Controle Econômico-financeira - Pós-Edital - 2024 - 1º Simulado

Assinale a alternativa que corresponde à correta análise sintática do trecho 
“Desse modo, a STN desenvolveu o Siafi em conjunto com o Serpro.”

A.O sujeito da oração é composto.
B.O predicado da oração é verbal.
C.O sintagma “Desse modo” corresponde ao complemento verbal da oração.
D.O sintagma “Siafi” corresponde ao predicativo do sujeito.
E.O sintagma “em conjunto com o Serpro” corresponde ao sujeito da oração.

Análise da Frase:[reset]

[red]Sujeito[reset]: [yellow]"a STN"[reset]
[red]Verbo[reset]: [yellow]"desenvolveu"[reset]
[red]Complemento Verbal (Objeto Direto)[reset]:[yellow] "o Siafi"[reset]
[red]Complemento Verbal Indireto[reset]: [yellow]"em conjunto com o Serpro"[reset]
[red]Adjunto Adverbial de Modo[reset]: [blue]"Desse modo"[reset]

A) [red]FALSO.[reset] [blue]O sujeito é simples, por possuir apenas um núcleo (STN).[reset]
B) [green]CORRETO.[reset] Após encontrar o sujeito, tudo que resta na oração é o predicado: 
Sujeito "A STN", [yellow]Predicado "desenvolveu o Siafi em conjunto com o Serpro"[reset]
O predicado verbal pressupõe um verbo não de ligação (que é o caso de "desenvolver" - VTDI) 
e a inexistência de predicativo [predicativo é uma parte do predicado que informa estado (permanente ou passageiro) ou situação sobre algum ser, o que não acontece no predicado]
C) [red]FALSO.[reset] O sintagma “Desse modo” não é complemento verbal; ele funciona como um adjunto adverbial de modo, indicando a maneira como a ação foi realizada.
D) [red]FALSO.[reset] O sintagma “Siafi” não é predicativo do sujeito; ele funciona como objeto direto (desenvolveu o quê?), indicando o objeto da ação.
E) [red]FALSO.[reset] O sintagma “em conjunto com o Serpro” não é o sujeito da oração; ele funciona como adjunto adverbial, indicando a maneira como a ação foi realizada

O objeto direto "o siafi", não remete ao sujeito (STN), mas remete-se ao verbo "desenvolveu", por isso ele um predicado verbal.

Letra 'b'

15. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TRF 1 - Analista Judiciário - Área Judiciária - Oficial de Justiça Avaliador Federal Pós-Edital - 2024 - 2º Simulado
Observe as palavras de Sun Tzu:

“Triunfam [yellow]aqueles[reset] que sabem quando lutar e quando esperar.”

Assinale a alternativa que indica a função sintática da expressão destacada.

A. Complemento direto.
B. Sujeito.
C. Aposto explicativo.
D. Complemento indireto.
E. Adjunto adnominal.

O verbo “triunfam” é intransitivo, a expressão “aqueles que sabem quando lutar e quando esperar” exerce função sintática de sujeito 
em que a palavra “aqueles” atua como núcleo; portanto, a letra “b” está correta. 
Aconteceu que a frase está em ordem invertida.

16.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TRF 1 - Analista Judiciário - Área Judiciária - Oficial de Justiça Avaliador Federal Pós-Edital - 2024 - 2º Simulado
Observe o período a seguir para responder à questão:

“O Brasil, o maior produtor e exportador de café do mundo, representa cerca de 38% da produção global.”

Assinale a alternativa que indica corretamente a função sintática da expressão “o maior produtor e exportador de café do mundo”

A.Adjunto adverbial.
B.Sujeito.
C.Objeto direto.
D.Vocativo.
E.Aposto.

O tema central é a análise sintática, especificamente a função do aposto, 
que é um termo acessório da oração que explica, especifica ou resume um substantivo ou pronome. 
A expressão 'o maior produtor e exportador de café do mundo' está entre vírgulas e se refere ao substantivo 'Brasil', 
caracterizando-se como um aposto explicativo.


Adjunto adverbial é um termo que modifica o verbo, o adjetivo ou outro advérbio, indicando circunstâncias como tempo, modo, lugar, causa, etc. 
No caso da expressão 'o maior produtor e exportador de café do mundo', ela não está modificando o verbo, mas sim explicando o substantivo 'Brasil'.

Sujeito é o termo da oração que concorda com o verbo em número e pessoa, geralmente indicando quem pratica ou sofre a ação. 
A expressão 'o maior produtor e exportador de café do mundo' não exerce essa função, pois o sujeito da oração é 'O Brasil'.

Objeto direto é o termo que completa o sentido do verbo transitivo direto, sem preposição. 
A expressão 'o maior produtor e exportador de café do mundo' não está completando o sentido de um verbo, mas sim explicando o substantivo 'Brasil'. 
Portanto, não é um objeto direto.

Vocativo é o termo que serve para chamar ou invocar o interlocutor, geralmente isolado por vírgulas. 
A expressão 'o maior produtor e exportador de café do mundo' não está chamando ou invocando ninguém, mas sim explicando o substantivo 'Brasil'. 
Portanto, não é um vocativo.

Aposto é o termo que explica, especifica ou resume um substantivo ou pronome, geralmente isolado por vírgulas. 
A expressão 'o maior produtor e exportador de café do mundo' está explicando o substantivo 'Brasil', caracterizando-se como um aposto explicativo.

17. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - DATAPREV - Analista - Área: Desenvolvimento de Software Pós-Edital - 2024 - 2º Simulado
Os vocábulos destacados em “Basta uma palavra” desempenham função sintática de:

A.complemento nominal.
B.sujeito.
C.predicativo do sujeito.
D.adjunto adnominal.
E.complemento direto.

Na frase “Basta uma palavra”, o verbo “bastar” é intransitivo, ou seja, não exige complemento direto. 
Assim, “uma palavra” exerce a função de sujeito, indicando aquilo que é suficiente.

    Alternativa 'B' - Sujeito

18.Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TJ AL - Técnico Judiciário - Área Judiciária Pós-Edital - 2024 - 1º Simulado
 
Em “disse Josenaldo” (l.4), a palavra destacada exerce função sintática de:

A.objeto indireto.
B.objeto direto.
C.sujeito.
D.predicativo do sujeito.
E.vocativo.    

O sujeito é o termo da oração que indica quem ou o que realiza a ação expressa pelo verbo. 
Na frase 'disse Josenaldo', 'Josenaldo' é o sujeito que realiza a ação de 'dizer'. 
Portanto, a palavra 'disse' é o verbo intransitivo e 'Josenaldo' é o sujeito da oração.

19. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - PM SP - Soldado PM de 2ª Classe Pós-Edital - 2024 - 2º Simulado
Analise o período a seguir:

Lucas, um professor adepto do princípio da educação, jamais supôs que encontraria seus alunos na balada.

Identifique a função sintática da expressão “um professor adepto do princípio da educação”.

A.Adjunto adverbial.
B.Sujeito.
C.Objeto direto.
D.Vocativo.
E.Aposto.

VOCATIVO (INTERPELATIVA) → é um chamamento, uma invocação de alguém ou algo. Sempre vem separado por vírgula.
APOSTO por sua vez, é um termo ligado a outro elemento da oração e serve para explicar, determinar ou especificar o elemento ao qual está ligado.

20. Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - TRF 5 - Analista Judiciário - Área Contabilidade Pós-Edital - 2024 - 2º Simulado 

No trecho “Há, portanto, que se fazer esforço redobrado” (primeiro parágrafo), o sujeito da forma verbal destacada é classificado como:

A.elíptico.
B.inexistente.
C.simples.
D.indeterminado.

[bg_blue]Há, portanto, que se fazer esforço redobrado”, o verbo haver indica uma ideia de tempo decorrido.[reset]
[bg_blue]Nesse caso, trata-se de um verbo impessoal e o sujeito é classificado como inexistente. Não admite sujeito.[reset]

21. Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - Prefeitura de Manaus - Guarda Municipal - 2024

Observe a oração abaixo:

“Respeito é essencial”

Assinale a alternativa que descreva, corretamente, a oração, sintaticamente e/ou a seus termos essenciais.

A.oração subordinada substantiva predicativa do sujeito
B.oração formada por sujeito simples e predicado nominal
C.oração coordenada assindética aditiva
D.oração formada por sujeito oculto e predicado nominal
E.oração formada por sujeito composto e não há predicado

Predicado nominal ocorre quando temos o verbo de ligação.
Predicado verbal ocorre quando temos somente a transitividade verbal direta.
Predicado verbo nominal ocorre quando; nós temos a transitividade verbal + verbo de ligação, indireto e intransitivo.

O predicado é a parte da oração que contém o verbo e informa algo sobre o sujeito. 
Ele é responsável por descrever ações, estados ou características do sujeito. 
Por exemplo, na frase "O gato dorme", "dorme" é o predicado, que nos diz o que o gato está fazendo. 
O predicado pode ser verbal (quando contém um verbo) ou nominal (quando apresenta uma característica do sujeito, geralmente com um verbo de ligação).

Alternativa 'B'

22. Ano: 2024 / Banca: Instituto Americano de Desenvolvimento - IADES / 
Prova: IADES - ECT - Enfermeiro do Trabalho Júnior Pós-Edital - 2024 - 1º Simulado

No trecho “Os cortes no investimento em ciência nos últimos anos podem ter gerado esse declínio na produção científica”, 
a função sintática do termo “esse declínio” é:

A. predicativo do sujeito.
B. complemento nominal.
C. objeto direto preposicionado.
D. sujeito da oração.
E. objeto direto.

[red]No item A.[reset] 
O termo 'esse declínio' não funciona como predicativo do sujeito, pois não está atribuindo uma característica ou estado ao sujeito da oração. 
O predicativo do sujeito geralmente aparece em orações com verbos de ligação, o que não é o caso aqui.

[red]No item B.[reset]
O termo 'esse declínio' não é um complemento nominal, pois não está completando o sentido de um nome (substantivo, adjetivo ou advérbio) com preposição. 
Complementos nominais geralmente são introduzidos por preposições, o que não ocorre neste caso.

[red]No item C.[reset]
O termo 'esse declínio' não é um objeto direto preposicionado, pois não está precedido por preposição. 
Objetos diretos preposicionados são raros e ocorrem em contextos específicos, geralmente para evitar ambiguidade ou por questões estilísticas.

[red]No item D.[reset]

O termo 'esse declínio' não é o sujeito da oração. O sujeito da oração é 'Os cortes no investimento em ciência nos últimos anos', que é quem realiza a ação de 'ter gerado'.

[green]No item E.[reset]

O termo 'esse declínio' é o objeto direto da oração, pois é o complemento verbal que sofre a ação do verbo 'ter gerado'. 
O objeto direto é o termo que completa o sentido do verbo transitivo direto sem o uso de preposição. Esta análise está de acordo com o gabarito da banca.


23. Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - SEAD GO - Policial Penal Pós-Edital - 2024 - 4º Simulado

No trecho "O problema da segurança pública no Brasil passa, sobretudo, pelo déficit de nossas polícias", 
a expressão "pelo déficit de nossas polícias" exerce a função de:

A. sujeito.
B. predicativo do sujeito.
C. objeto indireto.
D. objeto direto.
E. adjunto adverbial.

Assunto abordado: Sintaxe do período simples.

a) Errada. O sujeito da oração é "O problema da segurança pública no Brasil".

b) Errada. O predicativo do sujeito é uma expressão que atribui uma característica ao sujeito, o que não é o caso aqui.

[bg_blue]c) Certa. "Pelo déficit de nossas polícias" é um complemento do verbo "passa", sendo introduzido pela preposição "por", caracterizando-o como objeto indireto.[reset]

d) Errada. O objeto direto complementa verbos transitivos diretos e não é precedido de preposição, o que não se aplica aqui.

e) Errada. O adjunto adverbial modifica o verbo, adjetivo ou advérbio, indicando circunstâncias como tempo, lugar, modo etc., o que não é o caso desta expressão.

24.Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - TJ SC - Técnico Judiciário Auxiliar Pós-Edital - 2024 - 1º Simulado 
Observe as palavras de Confúcio:

“Não corrigir nossas falhas é o mesmo que cometer novos erros”.

Assinale a alternativa que indica a função sintática da expressão “nossas falhas”.

A.Complemento direto.
B.Sujeito.
C.Aposto explicativo.
D.Complemento indireto.
E.Adjunto adnominal.


A expressão 'nossas falhas' funciona como complemento direto do verbo 'corrigir'. 
Neste contexto, 'corrigir' é um verbo transitivo direto que exige um objeto (neste caso, 'nossas falhas') para completar seu sentido. 
A expressão não introduz uma nova oração nem modifica diretamente o verbo, mas sim completa seu significado, caracterizando-se, portanto, como complemento direto

No item B.
 A expressão 'nossas falhas' não exerce a função de sujeito na oração. O sujeito da oração é implícito, relacionado ao verbo 'corrigir'.

No item C.

A expressão 'nossas falhas' não atua como aposto explicativo. Aposto explicativo é um termo que explica, esclarece ou resume um termo anterior a ele,

No item D.

A expressão 'nossas falhas' não funciona como complemento indireto na oração analisada. Complemento indireto é o termo da oração que completa o sentido de um verbo transitivo indireto, exigindo uma preposição para sua ligação, o que não se aplica aqui.

No item E.

A expressão 'nossas falhas' não desempenha a função de adjunto adnominal. Adjunto adnominal é um termo que modifica um substantivo, atribuindo-lhe uma característica ou especificação. Neste caso, 'nossas falhas' é o objeto direto do verbo 'corrigir', e não um modificador de um substantivo.


25. Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 7 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2024 - 1º Simulado

A expressão sublinhada em “E então aconteceu [yellow]a coisa mais surpreendente”[reset] (l. 19º parágrafo) exerce função sintática de:

A. objeto direto.
B. objeto indireto.
C. sujeito.
D. aposto.
E. adjunto adverbial.


“E então aconteceu a coisa mais surpreendente”, devemos primeiro analisar o verbo “acontecer” e procurar o seu sujeito. 
Note que o sujeito está posposto ao verbo. Ao escrever o texto em ordem direta, teremos: E então a coisa mais surpreendente aconteceu. 
Ou seja, a expressão “a coisa mais surpreendente” exerce a função de sujeito do verbo; por isso, a alternativa “c” está correta.


26. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SEAP - BA - Policial Penal Pós-Edital - 2024 - 2º Simulado

Existem duas possibilidades reais para a solução do caso. Identifique a função sintática da expressão “duas possibilidades reais”.

A.complemento direto.
B.sujeito.
C.aposto explicativo.
D.complemento indireto.
E.adjunto adnominal.

O verbo “existir” é intransitivo, já que não exige um complemento direto; portanto, a expressão “duas possibilidades reais” exercerá a função de sujeito. 
Por isso, a letra "b" está correta. Em ordem direta, teremos: Duas possibilidades reais para a solução do caso existem.

27. Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - IMBEL - Cargos de Nível Médio - 2024

“Seja consciente do espaço pessoal e das decisões de cada um.” Assinale a alternativa correta em relação à sintaxe da oração:

A. oração: modo imperativo.
B. oração: modo subjuntivo.
C. sujeito simples: “do espaço pessoal”.
D. sujeito composto: “do espaço pessoal e das decisões de cada um”.
E. predicado: verbo-nominal.

Item A.

Análise: A oração 'Seja consciente do espaço pessoal e das decisões de cada um.' está no modo imperativo, que é utilizado para expressar ordens, conselhos ou solicitações. 
Neste caso, o verbo 'Seja' é uma forma de expressar um conselho ou uma orientação, característica do modo imperativo.

Item B.

O item que sugere que a oração está no modo subjuntivo não está de acordo com o gabarito da banca. 
O modo subjuntivo é utilizado para expressar dúvida, desejo, possibilidade, entre outros aspectos que não se aplicam à oração em análise, que claramente expressa uma orientação ou conselho, característicos do modo imperativo.

Item C.

Análise: A análise de que o sujeito da oração é simples e representado pela expressão 'do espaço pessoal' não está correta. 
Na verdade, a oração não especifica um sujeito explícito, focando-se na ação de ser consciente, o que caracteriza o sujeito como indeterminado. 
Além disso, a expressão 'do espaço pessoal e das decisões de cada um' funciona como complemento da ação, não como sujeito.

Item D.

Análise: Este item sugere que o sujeito da oração é composto por 'do espaço pessoal e das decisões de cada um', o que não está correto. 
A oração em questão não apresenta um sujeito explícito, sendo o foco a ação de 'ser consciente'. 
Portanto, a identificação de um sujeito composto é inadequada para a análise desta oração.

No item E.

Análise: A classificação do predicado como verbo-nominal também não se aplica à oração em análise. 
Um predicado verbo-nominal contém um verbo que indica ação e um nome que desempenha a função de predicativo, atribuindo uma característica ao sujeito. 
No entanto, a oração 'Seja consciente do espaço pessoal e das decisões de cada um.' não apresenta essa estrutura, 
sendo mais apropriado identificá-la como uma expressão de comando ou conselho, típica do modo imperativo.

28. Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - MGS - Analista de Sistemas - 2024 
 
Leia o fragmento de texto que segue e assinale a alternativa correta: 
“O pessoal delirou. [yellow]O mais categorizado dos marqueteiros[reset], considerado o gênio da classe, exultou: 
‘Isso, Moisés! Isso, sim, [yellow]é[reset] uma solução criativa! 
Vai ser um estouro! Se você faz o seu pessoal atravessar [yellow]a pé enxuto[reset] o mar Vermelho, eu lhe garanto [yellow]duas páginas[reset] na Bíblia’!” - 
A palavras grifadas podem ser sequencialmente classificadas em:

A. sujeito / verbo de ligação / adjunto adverbial modo / objeto direto.
B. sujeito / verbo de ligação / adjetivo / objeto indireto.
C. substantivo / verbo de ligação / adjetivo / objeto direto.
D. substantivo / verbo de ligação / pronome / objeto indireto.

Aqui temos "O mais categorizado", que se refere a um substantivo (sujeito), que é "marqueteiro". Então, a palavra grifada "O" é o sujeito.

O verbo "é" é um clássico exemplo de verbo de ligação, porque liga o sujeito a uma característica, sem expressar ação.

'a pé enxuto:'

Esse termo indica modo de como o pessoal atravessou o mar Vermelho, caracterizando-se como um adjunto adverbial de modo.

'duas páginas:'

É o que Moisés receberia em troca, funcionando aqui como objeto direto da frase, pois é o complemento direto do verbo.

[bg_red]A. sujeito / verbo de ligação / adjunto adverbial modo / objeto direto.[reset]

29. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de Nova Iguaçu - Auditor Fiscal do Tesouro Municipal - 2024
Assinale a opção em que é possível identificar sujeito expresso no enunciado.

A.Observa-se o uso excessivo de telas pelas crianças.
B.Fala-se muito em defesa da democracia.
C.Acredita-se que a inteligência artificial traz ameaça à criatividade.
D.Disseram que as colheitas serão melhores.
E.Houve muito tumulto na última sessão.

[green]Item A.[reset]

    [red]A FRASE ESTÁ NA VOZ PASSIVA SINTÉTICA:[reset]
    [red]quem observa, observa algo:[reset] o uso excessivo de telas [reset]<- Objeto direto [reset]/ verbo 'observar' é: VTD[reset]
    'se' -> [red]partícula apassivadora[reset]
    [red]'o uso excessivo'[reset] ->[blue] sujeito paciente, sofre a ação do verbo 'observar'[reset]
    [red]'pelas crianças' [reset]-> voz passiva sintética, agente da ação passiva. [blue]( adjunto adverbial de agente )[reset]
     [red]Adjunto adnominal[reset]: 'excessivo'[blue] (adjetivo que qualifica o núcleo)[reset]
     [red]Adjunto adnominal[reset]: 'de telas' [blue]( locução adjetiva )[reset]

Item B.

    quem fala? Sujeito indeterminado na oração.
    o verbo "falar" está sendo usado de forma intransitiva, pois não exige complemento essencial para completar o sentido da oração.
    "Em defesa da democracia" não é um complemento do verbo, mas sim um adjunto adverbial de modo, 
    que indica o contexto em que a ação de "falar" ocorre.
    Portanto, o pronome 'se' é indice de indeterminação do sujeito.

Item C.

    Não há sujeito expresso ou definido para o verbo 'acreditar' e o foco está em acreditar no oração subordinada.
    Na oração subordinada completa a transitividade direta: 'que a inteligência artificial traz ameaça à criatividade.'
        Porém o sujeito irá concordar com o verbo 'trazer', realizando a ação de trazer a inteligência artificial
                Sendo assim, 'traz' é verbo transitivo direto, indicando a ação realizada pelo sujeito.
                Seu complemento direto é: 'ameaça à criatividade' -> objeto direto.
                    Que por sua vez o núcleo do objeto é: 'ameaça' e seu complemento nominal 'à criatividade'.
                    Portanto, O "se" na principal é partícula apassivadora, e a oração subordinada é o objeto direto do verbo "acreditar".

Item D. 'disseram' está na 3º pessoa do plural, portanto, sujeito indeterminado.    

Item E. Verbo 'haver' é impessoal, não admite sujeito.

30. Ano: 2024 / Banca: Instituto Americano de Desenvolvimento - IADES
Prova: IADES - CENSIPAM - Técnico - Área: Recursos Naturais e Análise Ambiental - 2024 

A Amazônia desempenha um papel crucial no combate às mudanças climáticas em razão de sua vasta reserva de carbono florestal. 
Suas árvores armazenam carbono, evitando que se acumule na atmosfera e promova o aquecimento global. 
E os principais responsáveis por esses estoques robustos são [yellow]os povos indígenas, guardiões ancestrais das florestas.[reset]

A alternativa correta é a C: Sujeito.

Sujeito: É quem realiza a ação ou de quem se fala na frase.
Predicado: É tudo o que se diz sobre o sujeito.
Objeto direto: Completa o sentido do verbo sem precisar de preposição.
Objeto indireto: Completa o sentido do verbo com o auxílio de uma preposição.
Complemento nominal: Completa o sentido de um nome (substantivo, adjetivo ou advérbio).
No caso da frase em questão:

"Os povos indígenas" é o sujeito.
"são os principais responsáveis por esses estoques robustos" é o predicado.
Portanto, a alternativa C é a que melhor classifica o termo sublinhado.

31. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ RR - Técnico Judiciário Pós-Edital - 2024 - 2º Simulado
O vocábulo destacado em “Aconteceu nada” desempenha função sintática de:

A.complemento direto.
B.sujeito.
C.aposto explicativo.
D.complemento indireto.
E.adjunto adnominal.

[bg_blue]O verbo “acontecer” é intransitivo, já que não exige um complemento objeto; portanto, a palavra “nada” exercerá, sintaticamente, a função de sujeito.[reset]

31. Ano: 2024 / Banca: Instituto Brasileiro de Formação e Capacitação - IBFC
Prova: IBFC - SEAD GO - Policial Penal Pós-Edital - 2024 - 1º Simulado

“Tive várias vidas. Em outra de minhas vidas, o meu livro sagrado foi emprestado porque era muito caro: Reinações de Narizinho. 
Já contei o sacrifício de humilhações e perseveranças pelo qual passei, pois, já pronta para ler Monteiro Lobato, 
o livro grosso pertencia a uma menina cujo pai tinha uma livraria.”

 Sobre os termos da oração no trecho acima, assinale a alternativa correta:

A. Em “o meu livro sagrado foi emprestado”, “o meu livro sagrado” é o sujeito da oração.
B. Em “porque era muito caro”, “muito caro” é o objeto direto da oração.
C. Em “pois, já pronta para ler Monteiro Lobato, o livro grosso pertencia a uma menina”, “a uma menina” é o sujeito da oração.
D. Em “já contei o sacrifício de humilhações e perseveranças pelo qual passei”, “pelo qual passei” é o complemento nominal da oração.
E. Em "pois, já pronta para ler Monteiro Lobato, o livro grosso pertencia a uma menina cujo pai tinha uma livraria" é objeto indireto da oração.

Item A - CORRETO
Em 'o meu livro sagrado foi emprestado', 'o meu livro sagrado' é o sujeito da oração. 
O sujeito é o termo da oração que concorda com o verbo em número e pessoa, e neste caso, 'o meu livro sagrado' é o termo que realiza a ação de ser emprestado.
Além disso, podemos perguntar ao verbo: quem foi emprestado? 'o meu livro sagrado' <- Sujeito

Item B - ERRADO
Em 'porque era muito caro', 'muito caro' não é o objeto direto da oração. 
Na verdade, 'muito caro' é um predicativo do sujeito 'ele' (subentendido), que se refere a 'o meu livro sagrado'. 
O verbo 'era' é um verbo de ligação, e 'muito caro' é o predicativo que atribui uma característica ao sujeito. (ele) - o livro

Item C - ERRADO
Em 'pois, já pronta para ler Monteiro Lobato, o livro grosso pertencia a uma menina', 'a uma menina' não é o sujeito da oração. 
'A uma menina' é o complemento indireto do verbo 'pertencia', introduzido pela preposição 'a'. 
Indicando a quem o livro grosso pertencia. O sujeito da oração é 'o livro grosso'.

Item D - ERRADO
Em 'já contei o sacrifício de humilhações e perseveranças pelo qual passei', 'pelo qual passei' não é o complemento nominal da oração. 
'Pelo qual passei' é uma oração adjetiva relativa que se refere a 'o sacrifício de humilhações e perseveranças', funcionando como adjunto adnominal

Item E - ERRADO

Em 'pois, já pronta para ler Monteiro Lobato, o livro grosso pertencia a uma menina cujo pai tinha uma livraria', 'cujo pai' não é o objeto indireto da oração. 
'Cujo pai' é um pronome relativo que introduz uma oração adjetiva, indicando posse e se referindo a 'uma menina'.  exercendo função de adjunto adnominal.
        '''


    def predicacao_verbal_nominal(self):

        return''' 
        
        Predicação Verbal do Prefessor Elias Santana - GranCursos

        Predicado:

        A estrutura do predicado gira em torno do verbo que ali se apresenta. Em vista disso, é
        natural que nossa análise do predicado comece com a identificação do verbo e do termo que o acompanha.

        [yellow] O estudo do comportamento do verbo na estrutura do predicado pode ser chamado de predicação verbal[reset]

            A professora ensinou importante lições.

            [red]quem ensinou importante lições? [reset]'a professora' ->[yellow] Portanto Sujeito da oração[reset]
            'ensinou importante lições'[reset] -> [yellow]Predicado[reset]
            [red]quem ensina, ensina algo: [reset]'importante lições' <- [yellow]Objeto Direto[reset]
            [red]Para dizer que o verbo é VTD eu preciso de um OD.[reset]

            A professora ensinou às crianças.

            [red]quem ensinou às crianças?[reset] 'a professora' -> [yellow]Sujeito[reset]
            [red]'ensinou' [reset]-> [yellow]verbo com ação de ensinar, ensinar a alguém ?[reset] 'as crianças' [blue]( verbo transitivo indireto )[reset]
            [red]'as crianças'[reset] -> [yellow]complemento verbal ( preposicionado 'a' + artigo 'as'[reset] = [red]Objeto indireto )[reset]

            A professora ensinou importantes lições às crianças.

            [red]quem ensinou importantes lições às crianças?[reset] ' a professora' <-[yellow] Sujeito simples[reset]
            [red]quem ensina, ensino algo: [reset]'importantes lições' -> [yellow]objeto direto[reset]
            [red]quem ensina, ensina a alguém[reset]: 'às crianças' ->[yellow] Objeto indireto (artigo + preposição = preposição)[reset]

          	[bg_red]obs: quem define a transitividade verbal é a presença do complemento. ( com exceções de verbos notáveis [reset])

            A professora ensinou importantes lições às crianças nesta manhã

            [red]quem ensinou importantes lições ás crianças nesta manhã? [reset]'a professora' -> [yellow]sujeito simples[reset]
            [red]'ensinou' [reset]-> [yellow]quem ensina, ensinou a quem?[reset] 'as crianças' /[yellow] ensinou o que?[reset] 'importante lições' // [blue]Portanto, verbo transitivo indireto e indireto[reset]
            [red]'as crianças'[reset][yellow] complemento indireto do verbo [reset]
            [red]'importante lições' [reset]-> [yellow]complemento direto do verbo [reset]
            [red]'nesta manhã' [reset]-> oferece uma circunstância ao verbo ->[yellow] adjunto adverbial de tempo[reset]

            A professora ensinou nesta manhã

            [red]quem ensinou nesta manhã? [reset]' a professora' ->[yellow] sujeito simples[reset]
            [red]'ensinou' [reset]-> quem ensina, ensina algo:[yellow] verbo intransitivo por não haver complementos verbais[reset]
            [red]'nesta manhã' [reset]-> [yellow]adjunto adverbial de tempo[reset]

            Eu li uma história

	            [red]quem leu uma historia?[reset] 'eu' <- [yellow]Sujeito simples[reset]
	            [red]Temos a ação de ler? SIM. [reset]'li' transitivo para algo lido -> VTD, portanto, 'uma história' -> [yellow]Objeto direto[reset]

            Eu li para meus filhos

            [red]Quem é que leu? [reset]'eu' <- [yellow]Sujeito simples[reset]
	        [red]Existe ação de ler? SIM Aquilo que é lido não, mas temos para quem? 'para meus filhos' ->[yellow] Objeto Indireto 'para' ( preposição )[reset]
        	[red]Portanto 'li' é um verbo transitivo indireto.[reset]

            Eu li na praia
	
	        [red]quem é que le?[reset] Eu ->[yellow] Sujeito simples[reset]
            [red]ação de ler, sim. Para quem? NÃO. [reset]
	        [yellow]O verbo não transita. Verbo intransitivo[reset]
	    	[red]'na praia' [reset]-> [yellow]Adjunto adverbial de lugar[reset]

            [bg_blue]ADJUNTO ADVERBIAL não é complemento. É UMA circunstância para o verbo.[reset]

            Exemplos:

            Os diretores permaneceram calados durante a reunião.

            [red]quem permaneceram calados durante a reunião?[reset] 'os diretores' -> [yellow]sujeito[reset]
		    [red]'permaneceram' [reset]- verbo de estado ( não pode ser transitivo ) - [yellow] Verbo de ligação entre o sujeito e o predicativo[reset]
		    [red]'calados' [reset]-> adjetivo / característica dos diretores ->[yellow] predicativo do sujeito[reset]
		    [red]'durante a reunião' [reset]-> [yellow]adjunto adverbial de tempo[reset]

Observações:

            [red]Predicativo do sujeito não é complemento.[reset]
	        [red]Para que o verbo seja de ligação precisa ser necessariamente um verbo de estado[reset]

            [red]Verbos de fenômenos da natureza[reset]: [yellow]chover, nevar, amanhecer, anoitecer[reset] [bg_red]( não podem ser transitivos )[reset]
            [red]Verbos de estados: [reset] [yellow] ser, estar, parecer, ficar, continuar, permanecer, andar, tornar-se, virar[reset] [bg_red]( não podem ser transitivos )[reset]
            Verbos de ação: o restante

            Os diretores permaneceram na sala durante a reunião.

            [red]'os diretores' [reset]->[yellow] sujeito simples[reset]
            [red]'permaneceram' [reset]-> [yellow]verbo de estado[reset] ( transitivo não pode ser e não liga para o predicativo do sujeito então é verbo intransitivo )[reset]
            [red]'na sala'[reset] -> [yellow]adjunto adverbial de lugar[reset]
            [red]'durante a reunião'[reset] -> [yellow]adjunto adverbial de tempo[reset]

Observações:

            [bg_red]O verbo pode ser estado, de ação ou de fenômenos da natureza. Mesmo assim terá predicativo do sujeito.[reset]

            A verdade é a nossa arma de combate.

            [red]'a verdade'[reset] ->[blue] sujeito simples[reset]
            [red]'é' [reset]-> [yellow]verbo SER, de estado ( não pode ser transitivo )[reset]
            [red]'nossa arma de combate'[reset] -> [yellow]predicativo do sujeito ( característica da verdade )[reset]

            Eles são 11 jogadores

            [red]'eles' [reset]->[yellow] sujeito simples[reset]
            [red]'11 jogadores' [reset]-> [yellow]características deles ( predicativo do sujeito )[reset]
            [red]'são' [reset]- [yellow]verbo de ligação[reset] - [blue]verbo de estado e a frase possui predicativo do sujeito, portanto, é verbo de ligação.[reset]

            [bg_yellow]O predicativo do sujeito não depende do verbo de ligação.[reset]

            O povo manifestava calado em suas casas

            [red]'o povo' [reset]-> [yellow]sujeito simples[reset]
            [red]'manifestava'[reset] -> [yellow]verbo de ação ( se for verbo de ação pode ser VTD ou VTI, ou VI ) não tem algo ou alguem, não tem complemento na frase.[reset]
            [bg_red]Portanto é um verbo INTRANSITIVO[reset]
            [red]'calado' [reset]-> variável / adjetivo / característica do sujeito -[yellow] Predicativo do sujeito[reset]
            [red]'em suas casas'[reset] -> [yellow]Adjunto adverbial de lugar[reset]

            O povo manifestava silenciosamente em suas casas

            [red]'o povo' [reset]-> [yellow]sujeito simples[reset]
            [red]'manifestava' [reset]-> [yellow]Intranstivo[reset]
            [red]'em suas casas'[reset] -> [yellow]Adjunto adverbial[reset]
            [red]'silenciosamente'[reset] -> [yellow] Adjunto adverbial -> [reset]advérbio[reset]

            As crianças entregaram os celulares muito contrariadas

            [red]'as crianças'[reset] -> [blue]sujeito simples[reset]
            [red]'entregaram' [reset] -> [yellow]verbo de ação ( VI ou VTDI ) entrega algo?[reset] os celulares <- [red]objeto direto[reset]
            [red]'muito contrariadas' ->[blue] flexão de gênero, não é adjunto adverbial.[reset] E sim uma característica do sujeito ->[bg_blue] Predicativo do sujeito[reset]  [red]'muito contrariadas'[reset]

TIPOS DE PREDICADO:

Predicado verbal:
	Verbo de significado:

		-VTD
		-VTI
		-VTDI
		-VI

Predicado nominal:

	Verbo de ligação + predicativo do sujeito

Predicado verbo-nominal: ( deve possuir 2 núcleos )

	Verbo de significado + predicativo do sujeito ou do objeto ( se tiver complementos verbais )

            A professora ensinou importantes lições

        [red]'ensinou' [reset]-> VTD -> 'importante lições' ->[yellow] Objeto Direto[reset]
        [red]Predicado verbal [reset]-> [yellow]aquele predicado que possui o verbo de significado VTD[reset]

        Os diretores permaneceram calados durante a reunião.

        [red]'calados' [reset]-> [yellow] predicativo do sujeito + Predicado Nominal[reset]
        [red]'permaneceram' [reset]-> verbo de ligação + predicativo do sujeito 'calados' =[yellow] Predicado Nominal[reset]

            Os povo manifestava calado em suas casas.

        [red]'manifestava'[reset] -> [yellow]verbo intransitivo[reset]
        [red]'calado' [reset]-> [yellow]predicativo do sujeito[reset]
         [red]Verbo Intransitivo + predicativo do sujeito[reset] = Predicado Verbo Nominal[reset]

            As crianças encontraram os celulares muito contrariadas

            [red]'entregaram'[reset] -> VTD -> [yellow]complemento direto: 'os celulares'[reset]
            [red]'muito contrariadas'[reset] -> [yellow]Predicativo do sujeito[reset]
             [red]VTD + predicativo do sujeito[reset] =[yellow] Predicado verbo nominal[reset]

    [bg_red]Verbos de ligação:[reset]

Eles ligam um sujeito a uma característica, estado, qualidade (predicativo do sujeito). 

Eis os verbos que costumeiramente funcionam como verbos de ligação:
[yellow]ser, estar, ficar, parecer, permanecer, continuar, viver, tornar-se, andar, etc   [reset]

        Ele será médico. (VL / Predicativo do Sujeito)

        [red]'ele' [reset]-> [yellow]Sujeito simples[reset]
        [red]'será' [reset]-> [yellow]Verbo SER o futuro do presente do indicativo[reset]
        [red]'médico' [reset]-> [yellow]característica atribuida ao sujeito, portanto, predicativo do sujeito.[reset]
        Tipo de predicado: Nominal, pois o núcleo do predicado é o predicativo do sujeito 'médico'
        estabelecida pela conexão com o verbo 'será'

        O animal estava quieto. (VL / Predicativo do Sujeito)

        [red]quem estava quieto?[reset] [yellow]'o animal'[reset]
        [red]'estava'[reset] -> [yellow]Verbo de ligação[reset]
        [red]'quieto'[reset] -> [yellow]característica atribuida ao sujeito, portanto, predicativo do sujeito[reset]

        Durante a conversa, ele ficou apático. (VL / Predicativo do Sujeito)

        [red]'ele'[reset] -> [yellow]Sujeito Simples[reset]
        [red]'ficou'[reset] -> [yellow]verbo 'ficar' de ligação[reset]
        [red]'apático'[reset] -> [yellow]característica do sujeito, portanto, predicativo do sujeito[reset]
        [red]'durante a conversa'[reset] ->[yellow] circunstância para o verbo 'ficar', portanto, adjunto adverbial de tempo[reset]
        O predicado é classificado como predicado nominal, pois o núcleo do predicado é o predicativo do sujeito ("apático"), 
        enquanto o verbo de ligação "ficou" apenas estabelece a relação.

        A garota parecia doente. (VL / Predicativo do Sujeito)

        [red]quem parecia doente?[reset] [yellow]' a garota'[reset]
        [red]'parecia'[reset] -> [yellow]verbo parecer, de ligação[reset]
        [red]'doente'[reset]  -> [yellow]característica do sujeito, portanto, predicativo do sujeito.[reset]

        Resumo:

Predicado Verbal: Seu núcleo é um verbo que expressa ação. São formados por verbos transitivos ou intransitivos e sem predicativo.

    Abrirei o portão

    O verbo 'abrirei' é intransitivo, não precisa de complemento. Por sua vez 'o portão' é o sujeito paciente.

        Portanto,  o termo é predicado verbal.

    A população da vila assistia ao embarque

    'assistia' -> verbo transitivo indireto 
    'ao embarque' -> objeto indireto

        Portanto, o termo è predicado verbal. Não apresenta predicativo.

    Comunicaremos o fato ao diretor logo pela manhã.

    'comunicaremos' é um verbo transitivo direto e indireto
    'o fato' é objeto direto // 'ao diretor' -> objeto indireto

Predicado Nominal: Formado por verbo de ligação mais predicativo. Seu núcleo é o predicativo do sujeito

    A tristeza era imortal

    'era'- Verbo de ligação
    'imortal' -> Predicativo do sujeito

        Predicado Nominal

    Os príncipes viraram sapos

    'sapos' -> predicativos do sujeito
    'virar' -> verbo de ligação -> 'viraram' -> 
        
        Predicado Nominal

    Nós éramos cinco

    'éramos' -> Verbo de ligação
    'cinco'  -> predicativo do sujeito

        Predicado Nominal

    A conversa paulatinamente se tornou uma briga de egos

    'se tornou' -> verbo de ligação
    'uma briga de egos' -> predicativo do sujeito

        Predicado nominal

    Predicado verbo-nominal : Formado por dois núcleos: Verbal e nominal

        Formado por verbo de ação - transitivo / intransitivo + predicativo do sujeito 

    a. Verbo intransitivo + predicativo do sujeito

        Os velhos morreram doentes 

        'morreram' -> verbo intransitivo
        'doentes' -> predicativo do sujeito qualificando o sujeito 'os velhos'

            Portanto o termo é predicado verbo nominal, por possuir um verbo intransitivo + predicativo do sujeito

        O diretor chegou nervoso

        'chegou' -> verbo intransitivo
        'nervoso' -> predicativo do sujeito qualificando o sujeito simples 'o diretor'

    b. Verbo transitivo + predicativo do sujeito

        Julieta, desesperada, ainda poderia beber algum resquício do veneno?

        'desesperada' -> qualidade do sujeito 'julieta' -> Portanto, predicativo do sujeito
        'beber' -> verbo transitivo direto, quem bebe, bebe algo: 'algum resquício do veneno.' <- objeto direto

            Portanto a oração é um predicado verbo nominal, por possuir um núcleto verbal de ação transitivo 'beber' + nominal : 'desesperada'

        A multidão assistia ao jogo emocionada                    

        'assistia' -> verbo transitivo indireto, seu complemento direto: 'ao jogo'
        'emocianada' -> predicativo do sujeito, qualificando o sujeito 'a multidão'

            Portanto a frase possui 2 núcleos, um verbal 'assistia' VTI e nominal 'emocionada' qualificando o sujeito.

            Atenção!

            Na caso da voz passiva , em sua estrutura, possuir um predicativo do sujeito ou do objeto, o predicado será verbo-nominal.

            O espetáculo foi considerado imoral.

            'foi considerado' -> voz passiva 
            'imoral' -> predicativo do sujeito atribuindo característica ao sujeito 'o espetáculo' que seria por sua vez o objeto direto na voz ativa

                Na voz ativa:

                Eles consideraram o espetáculo imoral.

                Na voz ativa: 'eles' -> sujeito
                'consideraram' -> VTD
                'o espetáculo' -> objeto direto
                'imoral' -> Predicativo do objeto

                Considerou-se o espetáculo imoral                

                'se' -> pronome apassivador
                'considerou' -> VTD // Não há objeto direto, porque a frase está na voz passiva, portanto 'o espetáculo' é o sujeito
                'imoral' -> qualidade do sujeito atribuida -> Predicativo do sujeito

                Na voz ativa seria:

                    Alguém considerou o espetáculo imoral

                    Sujeito: 'alguém' 
                    'considedou' -> VTD // Como está na voz ativa, agora temos o objeto direto: 'o espetáculo'
                    'imoral' -> Predicativo do objeto

                Vejamos outro exemplo:

                O réu foi considerado culpado

                'foi julgado' -> voz passiva com VTD
                'culpado' -> Predicativo do sujeito

                Para a voz ativa:
                
                O júri cosiderou o réu culpado

                Agora o sujeito não é mais 'o réu' na voz passiva, sendo agora objeto direto do verbo 'considerar' VTD
                'o júri' -> comete a ação, portanto, é o sujeito da ação.
                'culpado' -> predicativo do objeto <- atribuindo uma qualidade ao objeto direto 'o réu'

                Pedro foi chamado de herói.

                'Pedro' -> Sujeito paciente
                'foi chamado' -> voz passiva com VTD, sem objeto direto
                'de herói' -> Predicativo do sujeito atribuindo qualidade ao Pedro, sujeito

                Voz ativa:

                Chamaram Pedro de herói

                'chamaram' -> VTD // Objeto direto: Pedro // ' de herói' -> Predicativo do objeto 
                Sujeito eliptico, oculto, desinencial

                Os procedimentos foram declarados corretos pelos auditores

                'foram declarados' -> voz passiva com VTD, sem objeto direto, por estar na voz passiva
                'corretos' -> predicativo do sujeito atribuindo qualidade aos procedimentos que por sua vez é o sujeito simples da oração
                
                Voz ativa:
                
                Os auditores declararam os procedimentos corretos

                'os auditores' -> Sujeito simples
                'declararam' -> verbo transitivo direto
                'os procedimentos' -> objeto direto
                'corretos' -> Predicativo do objeto.

                Veja este exemplo:

                Sempre que houver um predicativo do objeto, o predicado será verbo-nominal.

                Encontrei destruídas as mesas de mogno.

                quem encontra, encontra algo: 'as mesas de mogno' <- Objeto Direto sendo assim, 'encontrei' é: VTD
                'destruídas' -> Predicadivo do objeto

                                Predicado verbo-nominal

                Consideraram sua opinião inteligente

                quem considera, considera algo: 'sua opninião' <- Objeto Direto / 'consideraram' -> VTD
                'inteligente' -> Predicativo do objeto
                Sujeito é elíptico

                    Predicado verbo-nominal

                Não gostamos de sua irmã triste

                'gostamos' -> VTI -> 'de sua irmã' -> Objeto Indireto
                'triste' -> Predicativo do sujeito qualificando o objeto indireto 'de sua irmã'
                O sujeito por sua vez é elíptico

                    Predicado verbo-nominal

        ATENÇÃO REDOBRADA!

            Funções Sintáticas de Orações

            Em estruturas mais complexas, é comum que funções sintáticas sejam exercidas por orações.                                                                                           

            Estruturas oracionais podem exercer funções sintáticas.

            O servidor afirmou [yellow]o desconhecimento do fato.[reset]
            O servidor afirmou [yellow]que desconhecia o fato.[reset]
            
            Veja que, nas frases apresentadas, o termo “o desconhecimento do fato” e 
            a oração “que desconhecia o fato” exercem a função de objeto direto.

            Vejamos mais exemplos.

            [yellow]Após a demissão do empregado[reset], a empresa não lhe devolveu a carteira de trabalho.
            [yellow]Depois que demitiu o empregado[reset], a empresa não lhe devolveu a carteira de trabalho.
            
            Nas frases apresentadas, o termo “Após a demissão do empregado” e a oração “Depois 
            que demitiu o empregado” exercem a função de adjunto adverbial.

            Nessas situações, nas quais uma função sintática é exercida por uma oração, tem uma relação de subordinação.
             Daí por que tais orações são denominadas orações subordinadas, e os períodos pertinentes são chamados de períodos 
                compostos por subordinação. 

                Vejamos exemplos:

            A Constituição determina [yellow]que ninguém é obrigado a fazer algo senão por força da lei. [reset] (Objeto direto)

            'a constituição' -> Sujeito simples
            'determina' -> verbo transitivo direto. quem determina, detemrina algo: 'que ninguém...'

            A conquista da excelência necessita [yellow]de que todos se comprometam com ela. [reset](Objeto indireto)

            'a conquista da excelência' -> sujeito simples
            'da excelência' -> Complemento nominal  ( sujeito paciente, a exelência é conquistada )
            'necessita' -> verbo transitivo indireto. quem necessita, necessita de: 'de que todos...' <- Objeto indireto

            O ponto fundamental é [yellow]que seja garantida a lisura do procedimento.[reset] (Predicativo)

            'é' -> verbo de ligação, portanto, 'que seja garantida...' é predicativo do sujeito
            'O ponto fundamental' -> sujeito simples

            É importante [yellow]que as unidades cumpram o prazo pertinente à entrega dos questioná-rios.[reset] (Sujeito)

            'é' -> verbo de ligação // 'importante' -> predicativo do sujeito, atribuindo qualidade ao sujeito que por sua vez
                é a oração subordinada substantivo adjetiva 'que as unidades cumpram...'

            A oração subordinada funciona como o sujeito da oração principal (É importante). 
                    Isso porque o que "é importante" é o fato expresso na subordinada.

            Veja outro exemplo:

            Existe clara necessidade [yellow]de que todos participem do processo decisório.[reset]                   

            'de que todos participem...' é uma oração subordinada e tem a função de complementar o nome 'necessidade'.
                    Portanto é complemento nominal.

                    ATENÇÃO!

            Objetos indiretos e complementos nominais na forma de oração podem deixar a preposição pertinente subentendida.
                 Tal fato não altera a função sintática dos termos envolvidos.

            Acreditamos [yellow]em que esses problemas serão solucionados com o tempo.[reset]

            'acreditamos' -> VTI
            'em que esses...' -> Objeto Indireto

            Acreditamos [yellow]que esses problemas serão solucionados com o tempo.[reset]

            Mesmo deixando a preposição, a função sintática continua a mesma. 'que esses problemas...' <- Objeto Indireto


            Veja este exemplo:

            Estou confiante em que ele virá. (VL / PS / CN)

                'estou' -> verbo de ligação
                'confiante' -> Predicativo do sujeito
                'em que ele virá' -> Complemento Nominal ( preposição 'em')

            Estou confiante que ele virá. (VL / PS / CN)

            'estou' -> verbo de ligação
            'confiante' -> Predicativo do sujeito
            'que ele virá' -> Complemento nominal ( mesmo sem preposição )

            [red]PRONOMES OBLÍQUOS ÁTONOS[reset]

            Os pronomes oblíquos átonos exercerão a função sintática de objeto direto ou objeto indireto.
              [red]a.  Com sentido reflexivo.[reset]

            Nem ele [yellow]se[reset] [blue]suporta[reset] nessas horas!

            [blue]'suporta'[reset] -> verbo transitivo direto 
            [yellow]'se'[reset] -> Pronome reflexivo com função sintática de objeto direto
                'se suporta' -> [yellow]a mim mesmo[reset]

            Atribui-[yellow]me[reset] a obrigação de ajudá-lo.

            quem atribui, atribui a ele mesmo: 'atribui' -> verbo transitivo direto -> [yellow]'me' -> pronome reflexivo com função sintática de objeto indireto[reset]
            quem atribui, atribui a algo: 'a obrigação de ajudá-lo' -> objeto direto
                Portanto o verbo 'atribui' é VTDI. 

            Depois de tudo, nós [yellow]nos abraçamos[reset], arrependidos

            [yellow]'nos'[reset] -> um ao outro // pronome reflexivo recíproco com fução sintática de objeto direto do verbo 'abraçamos' -> VTD
            'arrependidos' -> predicativo do sujeito

             [red]b) Com sentido possessivo, os pronomes oblíquos átonos atuam como adjuntos adnominais.[reset]

             Criticaram-[yellow]me[reset] a opinião.

             Criticaram a [yellow]minha[reset] opinião -> Adjunto Adnominal

                Ora [yellow]te[reset] aperto a mão como aliado.

                Ora aperto [yellow]tua[reset] mão como aliado -> [yellow]tua[reset] -> Adjunto Adnominal

                A cruz pesava-[yellow]lhe[reset] nos ombros.

                A cruz pesava nos [yellow]seus[reset] ombros -> [yellow]seus[reset] -> adjunto adnominal

            Esse menino já [yellow]nos[reset] testou demais a paciência

            Esse menina já testou demais [yellow]nossa[reset] paciência -> 'nossa' -> adjunto adnominal

            [red]c. Os pronomes pessoais do caso oblíquo átono, se encontram associados a nomes, sobretudo ADJETIVOS, sua função sintática[reset]
            [red]será de COMPLEMENTO NOMINAL.[reset]

                Confesso que perdoar seu erro não[yellow] me[reset] é [blue]fácil.[reset] ( fácil -> Adjetivo )

                Confesso que perdoar seu erro não é fácil [yellow]para mim[reset] -> Complemento Nominal

                Sempre [yellow]lhe[reset] fui [blue]próximo.[reset]

                Sempre fui próximo [yellow]dele[reset] -> Complemento Nominal

                    [blue]próximo[reset] -> adjetivo -> 'dele' -> complemento nominal

                Não nos trairá, pois sempre [yellow]nos[reset] permanece [yellow]leal.[reset]

                    (= Não nos trairá, pois sempre permanece [yellow]leal a nós.[reset] >> complemento nominal)                    


           d) Fique atento para estruturas nas quais figuram os chamados verbos causativos (mandar,deixar, fazer e seus sinônimos)
             ou sensitivos (ver, ouvir, sentir e seus sinônimos) seguidos de infinitivos.
              [red]Nelas, o pronome oblíquo átono atua como sujeito do infinitivo.                    [reset]

              Mandei-[yellow]o[reset] permanecer na sala.(o >> sujeito de “permanecer”) -> permanecer -> verbo no infinitivo

                    'mandei' -> verbo de causa

                Por favor, deixe-[yellow]me[reset] explicar o que aconteceu. [blue](me >> sujeito de “explicar”) [reset]                   

                    'explicar' -> seguido do verbo no infinitivo
                    'deixe' -> verbo causativo

                Ela [yellow]nos[reset] fez esperar por horas. (nos >> sujeito de “esperar”)

                    'fez' -> verbo causativo
                    'esperar' -> verbo no infinitivo

                Nunca [yellow]os[reset] vi conversar nos intervalos entre as atividades.

                'vi' -> verbo sensitivo
                (os >> sujeito de “conversar”) -> infinitivo

                Acho que [yellow]a[reset] ouvi gritar ao longe. Você não?
                    (a >> sujeito de “gritar”)
                'ouvi' -> verbo sensitivo
                'gritar' -> verbo no infinitivo
                'a' -> sujeito do verbo gritar

                Nós [yellow]te[reset] sentimos desestimular em relação à viagem. 
                
                'te' -> sujeito do verbo desestimular
                'sentimos' -> verbo sensitivo

                Com verbos causativos e sensitivos, há autores que também consideram os pronomes 
                    oblíquos átonos como sujeitos de gerúndios.

                    Ela [yellow]me[reset] [blue]deixou[reset] [yellow]falando[reset] sozinho.
                        (me >> sujeito de “falando”) <- verbo no gerúndio
                        'deixar' -> verbo deixou , causativo

                    São vizinhos barulhentos: já [yellow]os[reset] [blue]ouvi[reset] [yellow]gritando[reset] várias vezes.
                        (os >> sujeito de “gritando”) <- verbo no gerúndio
                        'ouvir' -> verbo sensitivo

                    Não foram poucas as vezes em que [yellow]as[reset] [blue]vimos[reset] [yellow]brigando[reset] entre si.
                        (as >> sujeito de “brigando”)
                        verbo 'ver' -> verbo sensitivo
                        'brigando' -> verbo no gerúndio // 'as' -> sujeito do verbo brigando.

                   Os pronomes oblíquos com valor reflexivo, também serão sujeitos de infinitivos/gerúndios 
                            com verbos causativos e sensitivos.

                    Deixou-se levar pela conversa do vendedor.
                            (se >> sujeito de “levar”)                            
                            'deixou' ->  verbo causativos
                            'levar' -> verbo no infinitivo
                    
                    Deixamo-nos ficar ali, olhando o entardecer.
                        (nos >> sujeito de “ficar”)                            
                        'deixamos' -> verbo deixar -> verbo causativos
                        'ficar' -> verbo no infinitivo

                    Tamanha era a paixão, que [yellow]se[reset] viu ouvindo a amada por horas.
                        (se >> sujeito de “ouvindo”)
                        'viu'-> verbo sensitivo
                        'ouvindo' -> verbo no gerúndio, portanto 'se' é o sujeito do verbo          



Questão 01:

O pobre Reginaldo - assim se chamava o marido - habituara-se de muito àquelas recriminações insensatas 
e era [yellow]um quase fenômeno de resignação e paciência.[reset]

O termo grifado tem função de:

a. Objeto direto
b. Objeto indireto
c. Predicativo do sujeito
d. Agente da passiva

[red]quem era um quase fenômeno?[reset] 'ele' -> sujeito oculto, elíptico, desinencial refere-se no texto ao pobre reginaldo ( sujeito simples )
'era' ->[yellow] verbo de estado, verbo de ligação ou verbo intransitivo[reset]
'um quase fenomeno de resignação e paciencia' -> [yellow]predicativo do sujeito[reset]

2. Assinale a alternativa que apresenta a correta função sintática do termo sublinhado no trecho a seguir:

	'Nos ambientes escolares há dificuldades de se conter a violência, persiste o desrespeito às diferenças e 
    [yellow]há pouca integração[reset] entre a escola e comunidade.'

a. sujeito
b. Objeto direto
c. Objeto indireto
d. Complemento Nominal
e. Adjunto adverbial

[red]'há pouca integração'[reset] -> 'há' é verbo impessoal, não admite sujeito, VTD e portanto 'pouca integração' é objeto direto.
Agora se trocar 'há' por 'existem pouca integração', 'existem' seria intransitivo e 'pouca integração' seria o sujeito simples.

            Há crianças perdidas

	[red]'há'[reset] -> verbo impessoal, não admite sujeito, só pode ficar no singular, então
 	[red]'crianças perdidas'[reset] -> não pode ser sujeito e sim objeto direto
	    [red]O VERBO HAVER  NO CASO É VERBO TRANSITIVO DIRETO[reset]

	        Existem crianças perdidas
	
	[red]'existem'[reset] é verbo pessoal, admite sujeito. Verbo intransitivo
	[red]'crianças perdidas'[reset] -> sujeito simples

3. Sobre o período 'O hábito de cultivar plantas em jardins dentro e fora de casa cresceu durante os meses de pandemia.'
Assinale a alternativa correta:

a. A expressão 'de cultivar plantas' é um objeto indireto.
b. A expressão 'o hábito' é um objeto direto
c. O verbo 'cultivar' é intransitivo.
d. O verbo 'cresceu' é intransitivo
e. A expressão 'em jardins' é objeto indireto.

[red]Na alternativa A[reset] - A expressão 'de cultivar plantas' é sujeito da oração. Está associado ao substantivo 'hábito'
[red]Na alternativa B[reset] - 'O hábito' é o sujeito da oração
[red]Na alternativa C[reset] - quem cultiva, cultiva algo, cultiva plantas. é um verbo VTD com complemento direto 'plantas'
[red]Na alternativa D[reset] - [bg_green]CORRETO[reset]
[red]Na alternativa E[reset] - 'em jardins' é adjunto adverbial de lugar

4. No trecho 'só o cachorro já velhíssimo (era jovem quando o jovem partiu) continuou a esperá-lo na sua esquina.'
As duas ocorrências do termo 'jovem' exercem, respectivamente, as funções sintáticas de:

a. predicativo e sujeito
b. sujeito e objeto direto
c. objeto direto e predicativo
d. sujeito e adjunto adnominal
e. adjunto adnominal e objeto direto

O primeiro jovem é uma característica do 'cachorrinho' -> predicativo do sujeito
'era' verbo de ligação, não transita, portanto não possui complemento do lado
O segundo jovem é o sujeito, quem que partiu? 'o jovem'

	Gabarito Letra 'a'

5. Assinale a frase em que o termo destacado não é objeto indireto.

a. Comparo o trabalho do professor [yellow]com o mais precioso dos tesouros.[reset]
b. [yellow] Aos astros[reset] prometeu ele uma recompensa pela graça almejada.
c. A veiculação [yellow] de informações[reset] implica responsabilidade, e muitos não atentam para isso.
d. Não compete [yellow]a vocês[reset] emitir opinião no que não lhes diz nenhum respeito. 

Alternativa A
[red]quem compara, compara algo, compara o que?[reset] 'o trabalho do professor' -> [yellow]Objeto direto[reset]
[red]quem compara algo, compara com alguma coisa:[reset] 'com o mais precioso dos tesouros' -> [yellow]Objeto Indireto[reset]

[red]Alternativa B[reset]

'ele' -> sujeito simples
[red]quem promete, promete algo:[reset] 'uma recompensa pela graça almejada' ->[yellow] Objeto Direto[reset]
[red]quem promete, promete a alguem:[reset] 'aos astros' ->[yellow] objeto indireto[reset]

[green]Alternativa C[reset]

[red]quem implica, implica o que?[reset] implica: responsabilidade -> [yellow]objeto direto[reset]
[blue]'a veiculação de informações'[reset] -> Sujeito / [blue]'de informações'[reset] -> complemento nominal -> complementa o substantivo

[red]Alternativa D[reset]

[red]quem não compete, não compete o que?[reset] 'emitir opinião no que não lhes diz nenhum respeito' -> [yellow]  objeto direto[reset]
[red]que não compete, não compete a quem?[reset] ' a vocês' -> [yellow] Objeto Indireto[reset]

10. Em: [yellow]Surpresa[reset], percebi um resto de capim seco saindo da fresta do poste, o termo destacado exerce função de:

a. predicativo do sujeito
b. predicativo do objeto
c. adjunto adverbial
d. complemento nominal
e. adjunto adnominal

 O sujeito no termo está elíptico (eu) percebi um resto... porém, surpresa é ela, uma qualidade do sujeito, portanto é predicativo do sujeito.
	
11. Ano: 2022 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - BNB - Analista - Área Desenvolvimento de Sistemas - 2022 

'Ela tem como base a disseminação de [yellow]soluções[reset] para problemas voltados a demandas de renda, trabalho, [yellow]educação[reset], conhecimento, cultura,
 alimentação, saúde, habitação, recursos hídricos, saneamento básico, energia...'


Os substantivos “soluções” (quarto parágrafo) e “educação” (quarto parágrafo) estabelecem 
com o termo “disseminação” (quarto parágrafo) o mesmo tipo de relação sintática.    

'de soluções' é complemento nominal do substantivo 'disseminação', completando o sentido do nome.
Cegalla nos ensina que "Complemento nominal é o termo complementar reclamado pela significação transitiva, incompleta, de certos substantivos, adjetivos e advérbios.
Já a palavra "educação" não estabelece uma relação sintática de complemento nominal em relação à palavra "disseminação", vemos que "educação" é adjunto adnominal da palavra "demandas".

"de soluções" modifica "disseminação", que é substantivo abstrato. "de soluções" é alvo da ação disseminar, portanto é Complemento Nominal.

"educação" modifica "demandas" (substantivo concreto), dessa forma é adjunto adnominal, e nem se relaciona com "disseminação".

12.Ano: 2022 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TCE RJ - Analista de Controle Externo - Área Organizacional - Tecnologia da Informação - 2022

No fim das contas, a democracia sempre teve como alicerces os pressupostos de que nosso conhecimento do mundo é imperfeito e incompleto; 
de que não há resposta definitiva para grande parte das questões políticas;
 e de que é sobretudo por meio da deliberação e do debate que expressamos nossa aprovação e nosso descontentamento.

No segundo período do primeiro parágrafo, o segmento “de que é sobretudo por meio da deliberação e do debate que expressamos nossa aprovação e nosso descontentamento” complementa o termo “pressupostos”.

Certo.
O substantivo "pressupostos" requer complemento iniciado pela preposição "de".
 Sozinho, esse substantivo não tem sentido completo, por isso precisa de complemento. 
 Dessa forma, o termo "de que é sobretudo por meio da deliberação e do debate que expressamos nossa
  aprovação e nosso descontentamento" funciona como complemento dele.

Observe que, no primeiro parágrafo, esse substantivo recebeu três complementos: 
"de que nosso conhecimento do mundo é imperfeito e incompleto", 
"de que não há resposta definitiva para grande parte das questões políticas" e 
"de que é sobretudo por meio da deliberação e do debate que expressamos nossa aprovação e nosso descontentamento".

13. Ano: 2022 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - Secretaria de Educação e Esportes de Pernambuco - Professor de Língua Portuguesa - 2022

No trecho “a interpretação sexista do masculino genérico” (segundo período do terceiro parágrafo), 
os vocábulos “a” e “sexista” classificam-se, sintaticamente, como adjuntos adnominais do termo “interpretação”,
 e a expressão “do masculino genérico” classifica-se como complemento nominal desse mesmo termo.

A afirmação está certa. O artigo definido "a" e o adjetivo "sexista" exercem a função sintática de adjunto adnominal do substantivo "interpretação",
pois ligam-se diretamente a este para caracterizá-lo, especificá-lo. 
Já o termo preposicionado "do masculino genérico" é uma locução adjetiva que exerce a função sintática de complemento nominal.
 Ela se liga a um substantivo abstrato, "interpretação", e funciona como alvo da ideia expressa por esse substantivo 
 (o masculino genérico não vai fazer a ação de interpretar, mas, sim, sofrer essa ação, ou seja, vai ser interpretado).
  Sem esse complemento, o substantivo "interpretação" fica com seu sentido incompleto.


14.Ano: 2021 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - SEDUC AL - Professor - Área: Português - 2021


Victor Hugo poderia ter sido tão importante quanto foi mesmo se falasse outra língua —
 desde que pertencesse a uma cultura equivalente, em grau de adiantamento, riqueza de tradição intelectual etc., 
 à cultura francesa de seu tempo.

No último período do segundo parágrafo, o trecho “em grau de adiantamento, riqueza de tradição intelectual etc.”
 está entre vírgulas porque se encontra intercalado entre o termo “equivalente” e seu complemento nominal.

Correto. Quando suprimida a passagem em negrito, pode-se notar que o termo preposicionado "à cultura francesa..." atua como complemento nominal do adjetivo "equivalente".

'à cultura francesa de seu tempo' refere-se a um adjetivo (equivalente), é preposicionado e é paciente do objeto, podendo ser transformado para a voz ativa:

"A cultura francesa É PERTENCIDA (ser + particípio) à uma cultura equivalente".

Portanto, é COMPLEMENTO NOMINAL.

Vale lembrar que diferentemente do adjunto adnominal, o complemento nominal ocorrerá apenas nos substantivos abstratos, adjetivo ou adjunto adverbial presente no trecho.

Os complementos nominais são sempre preposicionados, tendo natureza passiva sempre que se referirem a substantivos abstratos.



15. Mesmo assim impera a insônia. 

Na linha 36, o termo “a insônia” exerce função de complemento da forma verbal “impera”.

ERRADO -> quem impera? 'a insônia'

16. Ano: 2021 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ALE CE - Analista Legislativo - Área Direito - 2021

Consiste em uma forma de conhecimento aplicado que estimula a jornada rumo “ao tornar-se humano” ou “ao que nos torna humanos” ou,
em seu sentido coletivo, a uma humanidade que transcende a alteridade em todos os níveis interpessoais.

No segundo parágrafo do texto CG1A1-I, o trecho “a uma humanidade que transcende a alteridade em todos os níveis interpessoais” funciona sintaticamente como complemento do termo

A. “estimula”.
B. “conhecimento”.
C. "aplicado”.
D. “jornada”.
E. “rumo”.

A. Incorreta. De acordo com o posicionamento desta professora, na verdade, o trecho ''a jornada rumo ao tornar-se humano...” exerce a função de complemento direto em relação à forma verbal ''estimula''.

B. Incorreta. De acordo com o posicionamento desta professora, a palavra ''conhecimento'' não possui complemento.

C. Incorreta. De acordo com o posicionamento desta professora, a palavra ''aplicado'' é um adjunto adnominal da palavra ''conhecimento''.

D. Incorreta. De acordo com o posicionamento desta professora, a palavra faz parte do complemento verbal da forma verbal ''estimula''.

E. Correta. De acordo com o posicionamento desta professora, de fato, pode-se dizer que o trecho “a uma humanidade que transcende a alteridade em todos os níveis interpessoais” funciona como complemento nominal do substantivo ''rumo''.

17. Ano: 2021 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - DPF - Escrivão de Polícia Federal - 2021

Na oração “Cabia tudo em uma mala só”, o vocábulo “tudo” exerce a função de sujeito.

C.Certo ->: O sujeito está posposto ao verbo. Na ordem direta, teríamos: Tudo cabia em uma mala só.

18. Ano: 2018
Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - ALE RO - Analista Legislativo - Área Revisão - 2018 
“A música talvez seja o único exemplo do que poderia ter sido – se não tivessem existido a invenção [yellow]da linguagem[reset],
 a formação [yellow]das palavras[reset], a análise [yellow]das ideias[reset] – a comunicação [yellow]das almas[reset]”.

Sobre os termos sintáticos sublinhados, assinale a afirmativa correta.

A. Todos exercem a função de complemento nominal.
B. Todos exercem a função de adjunto adnominal.
C. O primeiro e o último termo exercem funções sintáticas distintas.
D. O segundo termo exerce função sintática distinta dos demais.
E. Os dois últimos termos exercem a mesma função sintática.

A linguagem é inventada. -> Complemento nominal, paciente, sofre a ação
As palavras são formadas -> Complemento nominal, paciente, sofre a ação.
As ideias são analisadas -> Complemento nominal, paciente, sofre a ação.
As almas se comunicam -> Adjunto Adnominal, ação das almas, 

Alternativa A - ERRADA - 'a comunicação das almas' é adjunto adnominal
Alternativa B - Somente o último termo em destaque
Alternativa C - CORRETO
Alternativa D - ERRADO
Alternativa E - ERRADO

19.Ano: 2018 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - Prefeitura de João Pessoa - Técnico Municipal de Controle Interno - Área Auditoria - 2018

aí temos o “jeitinho” virando corrupção. 
 
Em “temos o ‘jeitinho’ virando corrupção” (R.15), os termos ‘jeitinho’ e “corrupção” funcionam como complementos diretos da forma verbal “temos”.

Há duas orações:

[nós] temos o jeitinho;
o jeitinho virando corrupção.


Na primeira oração, a estrutura sintática é a seguinte:

Sujeito oculto: nós
Verbo transitivo direto: temos
Objeto direto: o jeitinho virando corrupção.


Na segunda oração, a estrutura é:

Sujeito: o jeitinho
Verbo de ligação: virando
Predicativo do sujeito: corrupção.

Portanto, apenas o termo "jeitinho" funciona como complemento direto da forma verbal "temos".

GABARITO: ITEM ERRADO.

20.Ano: 2004 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MCT - Analista em Ciência Pleno 1 - Área Jornalismo - 2004 
 
,dando, portanto, ao pensamento a dignidade do sensível,


Independentemente da ordem em que os complementos da forma verbal “dando” (l.3) aparecem na oração, 
o emprego da preposição em “ao pensamento” (l.4) indica que “o pensamento” é, sintaticamente, seu objeto indireto.

No trecho "dando, portanto, ao pensamento a dignidade do possível", a forma verbal "dando" rege dois complementos:


Quem dá, dá alguma coisa a alguém.

- alguma coisa seria o objeto direto: a dignidade do possível;

- a alguém seria o objeto indireto: ao pensamento.

Portanto, o objeto indireto é a expressão "ao pensamento" (incluindo a preposição a) e não apenas "o pensamento".

21. Ano: 2010 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - CAERN - Assistente Social - 2010

Essa abordagem é o [yellow]cerne do reducionismo[reset], [yellow]um método de estudo[reset] baseado na ideia de que a compreensão [yellow]do todo[reset] pode ser alcançada 
[yellow]através do estudo[reset] [yellow]das suas várias partes.[reset] (L.26-29)

Assinale o termo que, no período acima, desempenhe função sintática idêntica à do termo sublinhado no mesmo período.

A. do reducionismo
B. de estudo
C. do estudo
D. através do estudo
E. das suas várias partes

A compreensão do todo - 'do todo' -> complemento nominal, complementando a ideia.

Alternativa 'A'

Essa abordagem é o cerne do reducionismo

'é' -> verbo de ligação
'o cerne' -> Predicativo do sujeito / 'o' -> adjunto ' / 'o cerne' -> substantivo concreto
'do reducionismo' -> Adjunto Adnominal

o complemento nominal ocorrerá apenas nos substantivos abstratos, adjetivo ou adjunto adverbial presente no trecho.
Cegalla nos ensina que "Complemento nominal é o termo complementar reclamado pela significação transitiva, incompleta, de certos substantivos, adjetivos e advérbios.
	Adjunto adnominal   -> refere-se a substantivos concretos ou abstratos
	Complemento nominal -> refere-se a substantivos abstratos, adjetivos e advérbios
    Os complementos nominais são sempre preposicionados, tendo natureza passiva sempre que se referirem a substantivos abstratos.

Alternativa B

Um método de estudo -> 'de estudo' -> paciente -> Complemento Nominal

Alternativa C

'Através do estudo' -> Adjunto adverbial de meio

[yellow]pode ser alcançada[reset] através do estudo -> Locução verbal na voz passiva

Alternativa E

'das suas várias partes' -> Complemento nominal, que completa o sentido do substantivo 'estudo'

Gabarito alternativa E

22.Ano: 2013 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - CONDER - Analista - Área Advogado - 2013

Assinale a alternativa em que o termo abaixo que não exerce a função de complemento nominal, por não ser o paciente do termo anterior.

A. Criação de um fundo.
B. Deterioração das cidades.
C. Provisão de recursos.
D. Situação de urgência.
E. Planejamento das cidades.

-> Adjunto Adnominal: formado por locução adjetiva, representa o agente da ação ou a origem, pertença, 
qualidade de alguém ou de alguma coisa (Cegalla, 2008, p. 364).
 É o que se observa na alternativa D: Situação de urgência. A locução adjetiva "de urgência" significa "urgente" [situação urgente].

-> Complemento Nominal representa o alvo de uma ação expressa por um nome transitivo. Esse é o caso das alternativas A, B, C e D.
 DICA: substitua o termo nuclear criação pelo verbo corresponde, se houver a conversão, é complemento nominal:

- Criação de um fundo = Criar um fundo.

- Deterioração das cidades = Deteriorar as cidades.

- Provisão de recursos = prover recursos.

- Planejamento das cidades = planejar as cidades.

Portanto, a alternativa D é a única que não apresenta exemplo de Complemento Nominal.

GABARITO: ALTERNATIVA D.

23. Ano: 2013 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - ALE MT - Professor - Área: Português - 2013

Uma das maneiras de mostrar‐se a diferença entre o adjunto adnominal e o complemento nominal é a comparação entre a função de agente (adjunto adnominal) e a de paciente (complemento nominal). Essa estratégia pode ser empregada no seguinte caso:


A. “...alguns sebos do Centro da cidade”.
B. "...uma pequena fila de bibliófilos”.
C. “...relações de livros e revistas...”.
D. “...meus companheiros de expectativa...”.
E. “...eis‐me em frente à loja do sebo que me interessava”.

Alternativa 'A' - 'sebos' -> Substantivo concreto, portanto, Adjunto Adnominal.
Alternativa 'B' - 'fila' -> substantivo concreto, portanto, Adjunto Adnominal.
Alternativa 'C' - 'relaçoes' -> substantivo abstrato, portanto, Complemento Nominal
Alternativa 'D' - 'companheiros' -> substantivo concreto, portanto, Adjunto Adnominal
Alternativa 'E' - 'loja' -> substantivo concreto, portanto, adjunto adnominal

Gabarito letra 'C'

24. Ano: 2013 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ AM - Analista Judiciário - Área Pedagogia - 2013 

O termo sublinhado que desempenha uma função diferente da dos demais, é

A. patentes de medicamentos.
B. desenvolvimento dos medicamentos.
C. lançamento comercial do produto.
D. distribuição de medicamentos.
E. tratamento do câncer.


A. patentes de medicamentos. 'patentes' -> substantivo concreto - Adjunto Adnominal, 
B. desenvolvimento dos medicamentos. Os medicamentos são desenvolvidos, paciente, portanto, 'CN'
C. lançamento comercial do produto. O produto é lançado, paciente, CN
D. distribuição de medicamentos. Os medicamento são distribuidos, portanto, CN
E. tratamento do câncer. O câncer é tratado, portanto, paciente, CN

25. Ano: 2013 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - INEA - Contador - 2013 
Assinale a alternativa cujo termo sublinhado exerce função diferente da dos demais.

A. Conjunto de políticas.
B. Redução de riscos.
C. Situações de desastres.
D. Presenças de ameaças.
E. Condições de vulnerabilidade.

A. Conjunto de políticas. AA -> 'Conjunto' -> substantivo concreto 
B. Redução de riscos. CN -> 'de riscos', paciente, os riscos são reduzidos.
C. Situações de desastres. AA  
D. Presenças de ameaças. AA
E. Condições de vulnerabilidade. AA


26. Ano: 2013 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Fundação Pró-Sangue Hemocentro de São Paulo - Assistente Social - 2013

Nas alternativas a seguir, o termo sublinhado funciona como paciente do termo anterior, à exceção de uma. Assinale‐a.

A. ânsia por cigarro.
B. dependência do tabaco.
C. consumo de tabaco.
D. relaxamento de todo o corpo.
E. técnica de meditação.


A. ânsia por cigarro. -> CN -> indicando a causa da ânsia, além do termo 'por cigarro' ser o paciente.
B. dependência do tabaco. -> CN -> 'do tabaco' -> paciente
C. consumo de tabaco. -> CN -> 'de tabaco', paciente, o tabaco é consumido
D. relaxamento de todo o corpo. -> CN -> todo o corpo é relaxado, paciente
E. técnica de meditação. -> AA -> uma especificação da técnica, caracterizando o tipo de 'técnica'.

27.Ano: 2013 / Banca: Fundação Getúlio Vargas - FGV / prova: FGV - ALE MA - Técnico de Gestão Administrativa - Revisor - 2013
Assinale a frase em que o termo sublinhado exerce a função de complemento nominal e não de adjunto-adnominal.

A. “Um mosquito é uma pequena criação da natureza para nos fazer pensar”. (André Guillois)
B. “Não é a saída do porto que determina o sucesso de uma viagem”. (Anônimo)
C. “A vida é um hospital onde cada enfermo tem o desejo de troca de cama”. (Baudelaire)
D. “Uma vida é uma obre de arte”. (Clemenceau)
E. “Eu sou uma parte de tudo”. (Lord Tennyson)

a. a natureza cria, agente -> AA
b. qualifica o substantivo 'viagem', portanto AA
c. a cama é trocada, CN
D. obra -> substantivo concreto -> AA
e. 'parte' -> substantivo concreto -> AA

28. Ano: 2014 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - SEDUC AM - Professor - Área: Língua Portuguesa - 2014
Compare os termos sublinhados das seguintes frases:

1. Preciso de mais tempo.
2. Viajo de táxi.
3. Árvores de minha rua.
4. Recebi a cópia da foto.


Sobre esses termos, assinale a afirmativa correta.

A. Todo complemento é precedido de uma preposição obrigatória.
B. Os exemplos de 1 e 2 são complementos de tipos diferentes.
C. 2 e 3 são termos adjuntos de mesmo tipo.
D. 4 é um caso de adjunto adnominal.
E. 3 e 4 são adjuntos de tipos diferentes.

1. Preciso de mais tempo. -> Objeto indireto
2. Viajo de táxi. -> Adjunto Adverbial de meio
3. Árvores de minha rua. -> AA
4. Recebi a cópia da foto. -> AA

Gabarito letra 'B'

29.Ano: 2014 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - SEE AL - Professor Docente I - Educação Física - 2014

O Observatório originou-se da constatação de que foram cumpridas apenas 20% das metas previstas no PNE
anterior, que regeu o período de 2000 a 2010.

O segmento “de que foram cumpridas apenas (...) o período de 2000 a 2010” (l.12-14) exerce a função sintática de complemento do nome “constatação” (l.12).

C. Certo
De que foram cumpridas as metas previstas (...) = está exercendo a função sintática de complemento nominal. 
Observe que ela completa o nome ( Substantivo Abstrato ) constatação.
Essa oração está exercendo a função de completar o sentido de um termo da oração principal .
 O termo como vimos é constatação. Logo, trata-se de uma Oração Subordinada Completiva Nominal.

 30. Ano: 2014 / Banca: Fundação Getúlio Vargas - FGV / rova: FGV - Câmara de Recife - Programador - 2014 

A opção em que os dois termos sublinhados exercem a função de complementos nominais é:

A. ambiente de paz / guerra ao terrorismo;
B. guerra ao terrorismo / sensação de invulnerabilidade;
C. sensação de invulnerabilidade / máscaras de gás;
D. máscaras de gás / centro da cidade;
E. centro da cidade / ambiente de paz.

'centro', 'máscaras', 'ambiente' são substantivos concretos. Portanto, Adjunto adnominais.
    Sendo assim, elimina as alternativas A,C,D,E .

'guerra ao terrorismo' -> 'ao terrorismo' -> paciente, CN
'sensação de invulnerabilidade' -> a invulnerabilidade é sentida -> paciente, CN

    Portanto, alternativa B]

31. Ano: 2015 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ RO - Técnico Judiciário - 2015

Entre os termos sublinhados abaixo, aquele que representa um agente do termo anterior, e não seu paciente, é:

A. poluição do ar;
B. uso de veículos;
C. aumento da poluição;
D. reservas de petróleo;
E. mudança de século.    

Adjunto Adnominal: formado por locução adjetiva, representa o agente da ação, além da origem, pertença, qualidade de alguém ou de alguma coisa (Cegalla, 2008, p. 364). Vejamos um exemplo:

- o discurso do presidente (agente da ação: o presidente discursa).

Não se deve confundir o adjunto adnominal formado de locução adjetiva com o Complemento Nominal. Este representa o alvo da ação expressa por um nome transitivo. Portanto, não configura o agente do termo anterior.

Nos itens A, B, C e E, temos a presença de nomes transitivos, os quais são alvos da ação expressa por esse nome. A dica é mudar o nome para uma forma verbal correspondente:

- alguém polui o ar [o ar é paciente da ação expressa pela forma verbal poluir]

- alguém usa veículos [veículos é paciente da ação expressa pela forma verbal usar]

- alguém aumenta a poluição [poluição é paciente da ação expressa pela forma verbal aumentar]

- alguém muda o século [século é paciente da ação expressa pela forma verbal mudar]

Item D: correto.

Aqui temos a função de adjunto adnominal. Nesse caso, o termo de petróleo representa o agente do termo reservas e tem o sentido de posse (ou seja, quem está de posse das reservas? O petróleo).


32.Ano: 2015 / Banca: Fundação Carlos Chagas - FCC / Prova: FCC - TRT 4 - Técnico Judiciário - Área: Administrativa - 2015 

... ou seja, como fornecedora de alimentos para o mercado interno.

A relação estabelecida entre os termos constantes do segmento sublinhado acima está reproduzida no segmento, também sublinhado, em:

A. Nas cidades do Sul ...
B. ... e a exposição de um certo verniz social
C. ... implicavam em moldar as mulheres de uma determinada classe.
D. Nas imagens dos jornais das cidades do Sul
E. Os altos preços do café no mercado externo ...


Obs: Adjunto Adnominal acompanha substantivo concreto e substantivo abstrato, enquanto o Complemento Nominal completa, entre outros, substantivo abstrato.

Quando for Complemento Nominal, terá natureza passiva, ou seja, sofrerá a ação e será obrigatoriamente acompanhado de preposição.

Quando for Adjunto Adnominal, a preposição não será obrigatória e, o mais importante, terá natureza ativa, ou seja, pratica a ação.

... ou seja, como fornecedora de alimentos para o mercado interno.
fornecedora = substantivo abstrato (ato de fornecer)
de alimentos -> os alimentos estão fornecendo ou sendo fornecidos? Sendo fornecidos = natureza passiva (sofre a ação) = Complemento Nominal

Letra A errada:  Nas cidades do Sul ... cidades é substantivo concreto / do Sul é Adjunto Adnominal.
Letra B correta: ... e a exposição de um certo verniz social ... exposição é substantivo abstrato (ato de expor) / um certo verniz social natureza passiva = Complemento Nominal.
Letra C errada: ... implicavam em moldar as mulheres de uma determinada classe. mulheres é substantivo concreto / de uma determinada classe é Adjunto Adnominal.
Letra D errada:  Nas imagens dos jornais das cidades do Sul ... imagens é substantivo concreto / dos jornais é Adjunto Adnominal.
Letra E errada: Os altos preços do café no mercado externo ... preços é substantivo concreto / do café é Adjunto Adnominal.

33. Ano: 2015 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - TJ PI - Analista - Área Banco de Dados - 2015

Entre os termos sublinhados abaixo, aquele que exerce a função de complemento é:

A. áreas da cidade;
B. campanhas de conscientização;
C. cidades de médio porte;
D. cobrança de pedágio;
E. número de vítimas.

A. áreas da cidade -> 'áreas' -> substantivo concreto, portanto, AA
B. campanhas de conscientização; -> 'campanhas' -> substantivo concreto, portanto, AA
C. cidades de médio porte; -> 'cidades' -> substantivo concreto, portanto, AA
D. cobrança de pedágio; -> O substantivo 'cobrança' precisa de complemento para ter sentido, portanto, complemento nominal
E. número de vítimas. -> 'número' -> substantivo concreto, AA

Gabarito letra 'D'

34. Ano: 2015 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - DPE MT - Assistente Administrativo - 2015 

“Procure agregar aliados com interesses semelhantes [yellow]aos seus[reset], invista em parcerias corretas. 
Mercúrio segue retrógrado [yellow]em Aquário[yellow]: você ganha [yellow]mais[reset] se unir forças e trabalhar [yellow]em equipe.[reset]
 Continue com atenção redobrada ao se comunicar. 
 Bom período para ouvir opiniões [yellow]diferentes,[reset] repensar assuntos e se abrir para novos pontos de vista.
  Bom, também, para revisar equipamentos eletrônicos”.

Assinale a opção que indica o termo sublinhado que exerce a função de complemento e não de adjunto.

A. “aos seus”
B. “em Aquário”
C. “mais”
D. “em equipe”
E. “diferentes”


A. “aos seus”    -> Complemento nominal para o adjetivo 'semelhantes', completando o sentido do adjetivo, com preposição
B. “em Aquário”  -> Adjunto Adverbial de lugar 
C. “mais”        -> Adjunto Adverbial de intensidade
D. “em equipe”   -> Adjunto Adverbial de modo
E. “diferentes”  -> Adjunto Adnominal, 'diferentes' é um adjetivo que atribui característica ao substantivo 'opiniões', além de não estar preposicionado.

35. Ano: 2015 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - PGE RO - Técnico de Procuradoria - Área Sem Especialidade - 2015 

O termo que exerce a função de complemento, e não de adjunto, é:

A. salvadora da Pátria;
B. apoio de governos vizinhos;
C. dinheiro de várias nações;
D. 230 trilhões de dólares;
E. a maior floresta do mundo.

A. salvadora da Pátria; -> 'da Pátria' -> Locução adjetiva que está sendo salva pela salvadora, portanto, paciente. Complemento Nominal
B. apoio de governos vizinhos; -> os governos vizinhos é que apoiam, agentes, Adjunto Adnominal
C. dinheiro de várias nações; -> 'dinheiro' -> substantivo concreto -> Adjunto Adnominal
D. 230 trilhões de dólares; -> 230 trilhões é substantico concreto, portanto, Adjunto Adnominal
E. a maior floresta do mundo. -> 'floresta' é substantivo concreto, portanto, Adjunto Adnominal

Alternativa 'A' a correta.

36. Ano: 2015 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Secretaria de Fazenda de Niterói - Agente Fazendário - 2015

Considerando os seguintes segmentos do texto 1: “redução da maioridade penal” e “inclusão de jovens”, 
a afirmação correta sobre o papel dos termos sublinhados é:

A. os dois termos exercem a função de adjuntos adnominais;
B. apenas o primeiro termo exerce a função de adjunto;
C. apenas o segundo termo exerce a função de adjunto;
D. os dois termos exercem a função de complementos nominais;
E. apenas o primeiro termo exerce a função de complemento.

Adjunto Adnominal: formado por locução adjetiva, representa o agente da ação ou a origem, pertença, qualidade de alguém ou de alguma coisa (Cegalla, 2008, p. 364). Portanto, indica uma relação de posse, como no exemplo: atitude de vencedor [alguém possui a característica de ser vencedor por ter atitude].
-> Complemento Nominal representa o alvo de uma ação expressa por um nome transitivo (como as palavras "redução" e "inclusão". Esse é o caso dos dois termos sublinhados no enunciado da questão:

redução da maioridade penal;
inclusão de jovens.

Na dúvida, vamos seguir a seguinte DICA: substitua o termo nuclear redução e inclusão pelo verbo corresponde. Se houver a conversão, é complemento nominal. Teríamos algo como:

reduzir a menoridade penal;
incluir jovens.

Veja que ambos os termos sublinhados exercem a função sintática de complemento nominal.
GABARITO: ALTERNATIVA D.

37. Ano: 2004 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - HFA - Psicólogo - Área Desenvolvimento de Recursos Humanos - 2004 

"... devido à preocupação de parecer belo aos olhos alheios."

O emprego do sinal indicativo de crase em “à preocupação” (l.18-19) e o emprego da preposição a junto com o artigo o, em “aos olhos” (l.19), 
têm a mesma causa gramatical: o emprego de “devido” (l.18).

ERRADO - quem deve, deve à: preposição + artigo ( à preocupação = objeto indireto), portanto, 'deve' é VTI
quem parece, parece: belo -> objeto direto / à alguém: aos olhos ( preposição + artigo os) -> Objeto indireto, portanto, 'parece' é VTDI.

38.Ano: 2004 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - IEMA - Técnico de Meio Ambiente - Área Educação Ambiental - 2004 
 
Segunda a ministra, o estudo 'tem sido um instrumento importante nas discursões com os setores econômicos para minimizar os impactos
de projetos de infra-estrutura e de energia sobre biodiversidade.

A expressão “de energia” (l.18) funciona na oração como complemento da palavra “impactos” (l.17).

ERRADO- A expressão 'de energia' funciona na oração como complemento de 'de projetos'.

Repare a reescrita:

'...setores econômicos para minimizar os impactos de projetos de infraestrutura e de projetos de energia sobre a biodiversidade.''

Observação: a partir da vigência do Novo Acordo Ortográfico, a grafia da palavra ''infra-estrutura'' passou para ''infraestrutura''.

39.Ano: 2004 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - HFA - Citotécnico - 2004 
 
"Os cientistas passaram a entender que o ataque ao processo de envelhecimento tem que ser total..."

Nas linhas 12 e 13, o emprego da preposição em “ao processo” mostra que esse termo é um dos complementos da forma verbal “passaram”, junto com “a entender”.

E.Errado

'ao processo' é o termo paciente do substantivo 'o ataque', portanto, complemento nominal.
'que o ataque ao processo de envelhecimento tem que ser total' é uma oração subordinada

'a entender' é objeto indireto do verbo 'passaram' -> VTI

40.Ano: 2004 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TRT 10 - Analista Judiciário - Área Analista de Sistemas - 2004

A Constituição Federal erigiu o devido processo legal, situado substancialmente no acatamento ao primado do contraditório e do amplo
direito de defesa.
 
Na linha 5, a presença de preposição em "ao primado" justifica-se pela regência de "situado".

ERRADO - A presença do termo 'ao primado' justifica-se pela regência do substantivo 'acatamento' cujo é seu complemento nominal.
Cabe destacar que o termo "situado" rege complemento com a preposição em: situado no acatamento. 
Portanto, "no acatamento" justifica-se pela regência de "situado".

41.Ano: 2004 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - SMS SE - Técnico de Enfermagem - Área Urgência - 2004 
 
De acordo com pesquisas do governo, o incentivo ao turismo tem provocado a expansão urbana de forma desordenada, com loteamentos
clandestinos, desmonte de dunas, desmatamentos e aterros.

Na linha 21, o substantivo “desmonte” é complementado, sintática e semanticamente, por “de dunas, desmatamentos e aterros”.

ERRADO - Somente por 'de dunas'. 'desmatamentos e aterros' são regidos pela preposição iniciada 'COM':

- com loteamentos clandestinos;
- com desmonte de dunas;
- com desmatamentos; e
- com aterros.

42.Ano: 2004 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - SEAD PA - Auxiliar de Serviços Gerais - 2004 
 
Esse crescimento coincide com a inauguração de espaços restaurados e do aeroporto internacional de Belém.

Na oração em que é usada, a forma verbal “coincide” (l.30) é complementada por dois objetos indiretos: “de espaços restaurados” (l.31) 
e “do aeroporto internacional de Belém” (l.31-32).

ERRADO -a forma nominal 'a inauguração' rege os complementos nominais 'de espaços restaurados' e 'do aeroporto internacional de Belém.'

A forma verbal 'coincide' transita indiretamente com os sintagmas: 'com a inauguração de espaços restaurados e do aeroporto internacional de belém.'
Reescrita: ''...coincide com a inauguração de espaços restaurados e com a inauguração do aeroporto internacional de Belém''.

43.Ano: 2005 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TCE MA - Analista de Controle Externo - 2005
 
... os portos da Amazônia [yellow]têm[reset] um sistema de braços flutuantes... (último parágrafo)

O verbo que exige o mesmo tipo de complemento que o do grifado acima está na frase:

A. ... choveu menos na Amazônia.
B. ... assim como aconteceu no início do século XX.
C. ... duplicando o impacto sobre o ambiente.
D. ... que se trata de variações médias ao longo de três décadas.
E. ... a atual seca se torna mais relativa.

O verbo 'têm' é transitivo direto, 'um sistema de braços flutuantes' é objeto direto

A. ... choveu menos na Amazônia. -> 'choveu' é intransitivo, fenômeno da natureza.
B. ... assim como aconteceu no início do século XX. 'aconteceu' é verbo intransitivo, portanto, 'no início do século XX' é Adjunto adverbial de tempo
C. ... duplicando o impacto sobre o ambiente. quem duplica, duplica algo: 'o impacto sobre o ambiente' -> Objeto Direto. Alternativa C a correta
D. ... que se trata de variações médias ao longo de três décadas. quem se trata, se trata de : 'de variações médias' -> Objeto Indireto
E. ... a atual seca se torna mais relativa. 'se torna' -> verbo de ligação / 'mais relativa' -> predicativo do sujeito

44. Ano: 2007 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - MPU - Técnico - Área Apoio Especializado - Especialidade: Edificações - 2007 

... elas também [yellow]causam[reset] impactos significativos na agricultura e na saúde humana. (final do texto)

O verbo que exige o mesmo tipo de complemento que o do grifado acima está na frase:

A. ... grandes pinheiros brotam por toda parte.
B. ... mas que chegaram ao Brasil ...
C. ... e aqui encontraram espaço ...
D. ... o búfalo e o pinus são apenas espécies exóticas.
E. ... e competindo com elas por alimento.

    O verbo 'causam' é transitivo direto, exige complemento direto: 'impactos significativos...'

A. ... grandes pinheiros brotam por toda parte. //  quem brota, brota por: 'por toda parte' -> objeto indireto
B. ... mas que chegaram ao Brasil ... // quem chega, chega a: 'ao Brasil' -> Objeto Indireto
C. ... e aqui encontraram espaço ... // quem encontra, encontra: 'espaço' -> Objeto direto
D. ... o búfalo e o pinus são apenas espécies exóticas. // 'apenas espécies exóticas' -> predicativo do sujeito
E. ... e competindo com elas por alimento. // quem compete, compete com: 'com elas' -> objeto indireto, 'por alimento' -> adjunto adverbial de causa/finalidade


45.Ano: 2007 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRE MS - Técnico Judiciário - Área: Apoio Especializado - Especialidade: Operação de Computadores - 2007 

... [yellow]desempenham[reset] um papel fundamental na cultura brasileira. (1° parágrafo)

O verbo que exige o mesmo tipo de complemento que o do grifado acima está na frase:

A. Mas são menores diante do quê?
B. - onde quer que seja esse lugar –
C. ... nunca floresceu uma canção popular...
D. Machado de Assis, como de costume, intuiu admiravelmente tudo.
E. Morre consagrado...

Na alternativa A não possui nenhum verbo transitivo.
Na alternativa B não possui nenhum verbo transitivo
Na alternativa C o verbo floresceu é intransitivo e 'uma canção popular' é sujeito, a ordem direta é: uma canção popular nunca floresceu
Na alternativa D o verbo intuiu é transitivo direto que possui seu complemento direto 'tudo' <- objeto direto
Na alternativa E o verbo 'morre' é intransitivo 'consagrado é adjunto adverbial de modo

Portanto a alternativa correta é a:  'D'

46. Ano: 2008 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - IRBr - Diplomata - 2008

'Uma pessoa pode nascer e ser criada em condições domésticas adversas ao desenvolvimento do amor próprio e da auto-confiança...'

A presença da preposição de antes do termo “autoconfiança” (l.3) indica que esse termo é complemento de “desenvolvimento” (l.2), e não de “condições domésticas” (l.1-2).

ERRADO - 'em condições domésticas' é predicativo do sujeito
O substantivo 'desenvolvimento' rege os complementos nominais 'do amor próprio' e 'da auto-confiança'.

47.Ano: 2008 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - MPE RS - Agente Administrativo - 2008
 
... para aprovar, até o final de 2009, um texto ... (2o parágrafo do Texto II)

O verbo que exige o mesmo tipo de complemento que o do grifado acima está na frase:

A. De fato, o resultado é modesto.
B. ... como fugir aos temas ...
C. ... já respondem por 20% do total das emissões globais.
D. ... que já estão na atmosfera ...
E. ... só prejudica formas insustentáveis de desenvolvimento.


quem aprova, aprova algo: 'um texto' -> objeto direto

Na alternativa A não possui nenhum verbo transitivo
Na alternativa B não possui verbo transitivo
Na alternativa C quem responde , responde por: '20% do total das emissõws globais. <- Objeto INDIRETO
Na alternativa D não possui verbo transitivo
Na alternativa E quem prejudica, prejudica o que? 'formas insustentáveis de desenvolvimento' -> Objeto Direto

48. Ano: 2008 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - SF - Analista Legislativo - Área Tradução e Interpretação - 2008

“Que provocou o maior desastre fiscal da história brasileira, induzindo a disparada do déficit público, da dívida interna e da carga tributária.” (L.65-68)

No trecho acima, em relação às ocorrências de complemento nominal, é correto afirmar que há:

A. três.
B. quatro.
C. duas.
D. uma.
E. zero.

Desastre fiscal da história brasileira - agente - AA

O déficit público disparou - agente - AA

Dívida interna disparou - agente - AA

Carga tributária disparou - agente - AA

Alternativa 'E' - Zero

49. (QUADRIX/2022/CRP 9ª REGIÃO-GO E TO/ANALISTA ADMINISTRATIVO)

'... ao encontro de sua festa? Gostei muito do cometa. Devia sempre haver...'

A oração “Gostei muito do cometa” (linha 10) é classificada como oração sem sujeito.

Perceba que o sujeito não veio escrito na frase, mas é facilmente identificável. Trata-se, portanto, 
de um sujeito oculto, elíptico ou desinencial.

'gostei' -> verbo transitivo indireto (VTI) ( sintaticamente )
'muito' -> adjunto adverbial de intensidade ( sintaticamente )
'do cometa' -> objeto indireto ( sintaticamente )

Portanto, a oração possui sim sujeito. Questão ERRADA.

50. (QUADRIX/2022/CRN - 6ª REGIÃO-PE/NUTRICIONISTA FISCAL)

'Se eu soubesse hebraico, explicaria isto muito melhor.

A oração “explicaria isto muito melhor” (linha 12) é classificada como oração sem sujeito.

Desse modo, o sujeito da forma verbal “explicaria” é oculto, elíptico ou desinencial.
(Eu) = sujeito elíptico

'explicaria' -> VTD
'isto' -> objeto direto
'muito' -> adjunto adverbial de intensidade
'melhor' -> adjunto adverbial de modo

    Questão ERRADA. Existe o sujeito.

51. (CESPE/CEBRASPE/2022/MPC-SC/ANALISTA DE CONTAS PÚBLICAS/DIREITO) 
A palavra “corrupção” tem origem nas palavras latinas corruptio e corrumpere, que indicam 
algo que foi corrompido, deturpado. Por ela ser um termo polissêmico, entendemos que a 
sua história conceitual é incerta. É usual o tratamento da corrupção sob uma perspectiva moralista, 
como algo resultante da falta de caráter dos indivíduos. 
Contudo, tal abordagem não apresenta validade científica, já que moral é um atributo individual, dotado de subjetividade e 
culturalmente circunscrito.

No terceiro período do primeiro parágrafo, o termo “o tratamento da corrupção sob uma perspectiva moralista” desempenha a função de sujeito.    
    
'É' -> VERBO DE LIGAÇÃO
'USUAL' -> predicativo -> adjetivo ( vem logo depois do verbo de ligação, portanto é predicativo )  

O termo não pode ser complemento nominal porque não está completando o sentido de "usual" (que, neste caso, é um predicativo e não um substantivo abstrato).

A estrutura do verbo de ligação confirma que "usual" está atribuindo uma característica ao sujeito.

    Portanto, a afirmativa está correta. Desempenha a função de sujeito.

    Sujeito está POSPOSTO ao verbo.

Teste da concordância:

Em construções com sujeito, o verbo concorda com ele.
Se trocarmos "o tratamento" por um termo no plural, o verbo mudará de singular para plural:
"Os tratamentos da corrupção sob perspectivas moralistas são usuais."
Isso confirma que "o tratamento da corrupção sob uma perspectiva moralista" é o sujeito, já que o verbo concorda com ele.

52.(CESPE/CEBRASPE/2022/BANRISUL/ANALISTA DE SEGURANÇA DA TECNOLOGIA DA INFORMAÇÃO)

Uma das maiores festividades do Brasil! Essa é a Festa Nacional da Uva, 
o mais dinâmico símbolo de Caxias do Sul e da Serra Gaúcha. O evento comunitário é uma 
celebração da cultura dos imigrantes italianos, que fizeram da região sua morada.
 Em cada edição, milhares de pessoas ficam imersas na cultura, gastronomia, diversidade e alegria.

No trecho “Uma das maiores festividades do Brasil! Essa é a Festa Nacional da Uva” (primeiro parágrafo),
 o segmento “Uma das maiores festividades do Brasil” exerce a função de sujeito da forma verbal “é”.

 ERRADO. 'ESSA' é o sujeito da oração da forma verbal 'é'.

53.. (QUADRIX/2022/CREMEGO/MÉDICO FISCAL)

Em uma semana de encontros virtuais, foram apresentadas pesquisas nas fases II e III, ou seja, em estágios próximos da aprovação
de agências reguladoras.

A flexão da forma verbal “foram” na terceira pessoa do plural justifica-se por ser indeterminado o sujeito da oração,
 não havendo referente ao qual se possa atribuir a noção verbal.

 quem foram apresentadas? 'pesquisas nas fases II e III' -> Sujeito posposto ao verbo

        Portanto a questão está errada, o sujeito não é indeterminado.

54. (QUADRIX/2022/CREMERO/ASSISTENTE ADMINISTRATIVO)        

Infelizmente, da sua obra só restaram fragmentos esparsos e citações a ele atribuidas por outros autores.

A flexão da forma verbal “restaram” (linha 23) na terceira pessoa do plural justifica-se por ser 
indeterminado o sujeito da oração.

O sujeito está posposto ao verbo. Quem restaram? fragmentos esparsos e citações
'restaram' -> verbo transitivo indireto -> 'a ele atribuidas por outros autores' <- Objeto Indireto

Portanto a afirmativa está ERRADA, o sujeito existe e está posposto ao verbo.

55. (QUADRIX/2022/CRC-PR/ADVOGADO)

E nós, lá na roça, tínhamos quase a convicção de que o verdadeiro deputado era o coronel e o doutor Castro um simples preposto seu.

No período em que ocorre, o trecho “o coronel e o doutor Castro” (linha 14) consiste em um sujeito composto, uma vez que possui dois núcleos.

'o verdadeiro deputado' -> Sujeito
'era' -> verbo de ligação 
'o coronel e o doutor Castro' -> Predicativo do sujeito composto

56.. (QUADRIX/2022/CRA-PR/ADMINISTRADOR I)

Ainda que o administrador continue atuando na área de planejamento estratégico, finanças, marketing, produção, qualidade,
recursos humanos, tecnologia da informação, entre outras, esse profissional tem hoje um novo olhar para sua área de atuação...

O sujeito da forma verbal “tem” (linha 36) é “o administrador” (linha 33).

ERRADO -> O sujeito é 'esse profissional'

57. (QUADRIX/2022/CRA-PR/AUXILIAR ADMINISTRATIVO)

a ideia de que os homens que se importavam com a aparência formavam um grupo seleto morreu.

O sujeito do verbo “morreu” (linha 10) é “um grupo seleto” (linha 9).

ERRADO -> O sujeito do verbo 'morreu' é 'a ideia'

58. (QUADRIX/2022/CRMV-SP/ASSISTENTE ADMINISTRATIVO)

Quando se pensa em pecuária bovina, é consenso que o bem-estar dos animais afeta o produto final.

Na oração que inicia o texto, a partícula “se” indica que o sujeito é indeterminado.

A partícula se, quando acompanhada de VTI, VL ou VI é índice de indeterminação do sujeito.

59. (QUADRIX/2023/CRO – SC/ADMINISTRADOR)

Entenda que, tanto as facetas...

O sujeito da forma verbal 'entenda' é indeterminado.

ERRADO - A forma verbal ENTENDA está no modo imperativo afirmativo. Portanto, o sujeito é oculto, elíptico ou desinencial.

60. (CESPE/CEBRASPE/2023/SEPLAN-RR/ANALISTA DE PLANEJAMENTO E ORÇAMENTO/PLANEJAMENTO E ORÇAMENTO)
Há três dimensões inerentes ao conceito de governabilidade: capacidade do governo de identificar problemas críticos e
 de formular políticas adequadas ao enfrentamento desses problemas, capacidade de mobilizar meios e recursos 
necessários à execução e à implantação das políticas públicas e capacidade de liderança do 
Estado, sem a qual as decisões se tornam ineficientes.

O sujeito da forma verbal “Há” está posposto e determinado no período em que ocorre.

Não existe sujeito para a forma verbal 'há' por ser um verbo impessoal.
O verbo 'haver' no sentido de existir, ocorrer, tempo decorrido, sempre ficará no singular e não admitirá sujeito.

Questão ERRADA.

61. (QUADRIX/2022/CRECI - 11ª REGIÃO-SC/CONTADOR)

Numa tarde vêm o chaveiro, os bombeiros e a polícia. Arrombam a porta do apartamento.

O emprego do acento diferencial no verbo “vêm” (linha 15) é obrigatório, porque o seu sujeito é 
classificado como composto, logo o verbo deve apresentar flexão de plural.

Quem vêm? 'o chaveiro' <- núcleo //  'os bombeiros' <- 2 núcleo // 'a polícia' <- 3 núcleo <- Sujeito composto

    Questão CORRETA. Afirmativa CORRETA.

62. (CESPE/CEBRASPE/2022/TELEBRAS/TÉCNICO EM GESTÃO DE TELECOMUNICA-ÇÕES/ASSISTENTE ADMINISTRATIVO)    

. Fala-se já de bombas eletrônicas (E) que podem paralisar estabelecimentos neurais da sociedade moderna, 
como hospitais, centrais elétricas, oleodutos etc., destruindo os seus circuitos eletrônicos.

No último parágrafo do texto, a partícula “se”, em “Fala-se já de bombas eletrônicas”, indica que 
o sujeito da oração é indeterminado.

A partícula SE, acompanhada de VTI, VI ou VL + referente vago, exercerá papel sintático de índice 
de indeterminação do sujeito. ( IIS ) 
O verbo falar é VTI e seu objeto indireto é 'de bombas eletrônicas', portanto o 'se' é IIS

63. (INSTITUTO AOCP/2021/PREFEITURA DE JOÃO PESSOA – PB/ENFERMEIRO) 
Ainda em relação ao trecho “Esses últimos costumam ser até solicitados pelos pacientes, mas [yellow]devem ser evitados[reset] ao máximo,
porque [yellow]podem afrouxar[reset] o controle dos impulsos, assim como o álcool, além de [yellow]causarem dependência.[reset]”, 
os verbos destacados retomam a expressão “Esses últimos” e fazem referência a ela por meio de

a) sujeito elíptico, em que se oculta um termo já de conhecimento do leitor.
b) zeugma, em que se oculta um termo, independente de ter sido mencionado antes ou não.
c) coesão por anáfora, em que se usa um elemento para anunciar outro, ainda não mencionado no texto.
d) coesão por catáfora, em que se usa um elemento para recuperar outro, já mencionado no texto.
e) referenciação nominal, em que se emprega um nome para recuperar um termo anterior.

“Mas (esses últimos) devem ser evitados... porque (esses últimos) podem afrouxar... além de 
(esses últimos) causarem dependência.”
a) Certa. O sujeito das locuções verbais destacadas está oculto.
b) Errada. Só será ZEUGMA se o termo ter sido obrigatoriamente mencionado.
c) Errada. Na coesão anafórica, o referente deve ter sido mencionado.
d) Errada. Na coesão catafórico, não há retomada, mas sim anunciação de um novo elemento.
e) Errada. Não ocorre referenciação nominal.
Letra a.

64. (INSTITUTO AOCP/2021/MPE-RS/TÉCNICO DO MINISTÉRIO PÚBLICO) 
omos estimulados a sonhar, a buscar objetivos e a nos orientar em direção ao que desejamos. 
Às vezes, o problema é que não sabemos o que queremos. É o que tenho observado em muitas pessoas, até em mim mesma.
O sujeito sintático da forma verbal “Somos” é

a) indeterminado
b) inexistente
c) desinencial
d) composto
e) vago

(Nós) somos estimulados a sonhar.
O sujeito é desinencial.
Letra c.

65. (INSTITUTO AOCP/2016/IF-BA/PROFESSOR DE LÍNGUA PORTUGUESA) 
Assinale a alternativa em que a expressão em destaque indica o sujeito da oração.

a) “Há [yellow]alguns dias[reset] ela não estava tão bela”.
b) “Beleza está nos olhos [yellow]da dona Maria Francisca”.[reset]
c) “Deitada na maca, com suplemento de oxigênio em suas narinas, [yellow]sua fala[reset], ainda cansada e 
intercortada, buscava me deixar feliz...”.
d) “Respirava agora [yellow]por conta própria”.[reset]
e) “Não há [yellow]beleza maior que a gratidão mais sincera”.[reset]

a) Errada. Objeto direto.
b) Errada. Adjunto adnominal.
c) Certa. Quem buscava me deixar feliz? Sua fala = sujeito.
d) Errada. Adjunto adverbial de modo.
e) Errada. Objeto direto.
Letra c

66. (INSTITUTO AOCP/2019/IBGE/ANALISTA CENSITÁRIO/LETRAS)
No trecho “Por ora basta que saibam os meus leitores que o ponto de interrogação é um verdadeiro anzol.”, o 
sujeito do verbo “saibam” é classificado como:

a) simples.
b) composto.
c) indeterminado.
d) oculto desinencial.
e) oculto referencial.

Novamente o sujeito está posposto ao verbo. Quem que saibam? 'os meus leitores' <- Sujeito posposto simples explícito
'saibam' por sua vez é VTD -> saibam o que? 'que o ponto de interrogação é um verdadeiro anzol.' <- Objeto Direto

Análise sintática do sujeito:

    Os meus leitores <- sujeito
    'os' -> Artigo que acompanha o substantivo com função sintática de Adjunto Adnominal
    'meus' -> pronome possessivo acompanhando o substantivo com função sintática de Adjunto Adnominal
    'leitores' -> núcleo do sujeito

    Resposta letra 'A'.

    67. (IBFC/2022/MGS/CARGOS DE NÍVEL MÉDIO)

    O importante não era o valor material,

    No texto, encontramos estruturas sintáticas que são formadas por sujeito + verbo de ligação 
    + predicativo do sujeito. Assinale a alternativa que apresenta a oração que contenha essa estrutura descrita.

a) Todo mundo comemora o Dia das Mães.
b) O presente do Dia das Mães era todo um acontecimento.
c) Os romanos herdaram essa tradição.
d) A poeta e ativista Julia Ward Howe escreveu a Proclamação do Dia das Mães.

Vale frisar que procuramos por sujeito + verbo de ligação + predicativo do sujeito.

Letra 'A' 
Todo mundo -> Sujeito
'comemora' -> VTD // 'o dia das Mães' <- objeto direto

    Não há verbo de ligação nem predicativo do sujeito

letra 'B'
O presente do dia das Mães -> Sujeito
'era' -> verbo de ligação
'todo um acontecimento' -> predicativo do sujeito

    Essa é a alternativa correta.

Letra 'C'

Os romanos herdaram essa tradição

'Os romanos' -> Sujeito
'herdaram' -> VTD // 'essa tradição' <- Objeto direto

    Não é a alternatica correta, sem verbo ligação e predicativo do sujeito

Letra 'D' 

A poeta e ativista Julia Ward Howe escreveu a Proclamação do Dia das Mães.

'a poeta e ativista Julia Ward' -> Sujeito composto
'escreveu' -> VTD // 'a proclamação do dia das mães' -> Objeto direto

68. (IBFC/2022/DETRAN-AM/TÉCNICO ADMINISTRATIVO) 
Na seguinte sequência de orações “Vejo e me identifico com a luta, outras vezes, observo-os em silêncio e penso”, 
repete-se um tipo de sujeito que:

a) possui um caráter de indeterminação do agente.
b) deve ser identificado pela desinência verbal.
c) sofre as ações e classifica-se como passivo.
d) pode ser entendido como inexistente.


“(Eu) vejo e me identidico com a luta, outras vezes, (eu) observo-os em silêncio e (eu) penso.”
O sujeito é desinencial.

a) Possui um caráter de indeterminação do agente.
Errado. O sujeito não é indeterminado, pois sabemos que se trata de "eu", identificado pela conjugação verbal.

b) Deve ser identificado pela desinência verbal.
Correto. O sujeito oculto em todas as orações pode ser identificado pela desinência verbal na 1ª pessoa do singular ("-o").

c) Sofre as ações e classifica-se como passivo.
Errado. O sujeito é agente da ação em todas as orações, não sofre a ação.

d) Pode ser entendido como inexistente.
Errado. O sujeito existe e é oculto, identificado pelo verbo.

69. (IBFC/2022/IBGE/AGENTE CENSITÁRIO DE ADMINISTRAÇÃO E INFORMÁTICA/EDITAL N. 8)

[yellow]Uns[reset] saíam para o trabalho. [yellow]Outros[reset], em busca do primeiro gole de cachaça no balcão do armazém de sô Ladislau,

No texto, os vocábulos “Uns” e “Outros” relacionam-se entre si por meio de uma estrutura de paralelismo.
 Pode-se afirmar que, sintaticamente, exercem a função de:

a) objeto direto.
b) sujeito simples.
c) adjunto adnominal.
d) objeto indireto.
e) predicativo do sujeito.

Quem saíam para o trabalho?
Uns = sujeito simples.
Outros (saíam) em buscam do primeiro gole...

    Letra 'B' -> Ambos sujeito simples

70. (IBFC/2021/SEED – RR/PROFESSOR DE EDUCAÇÃO BÁSICA/ARTES) Na oração “Algo me vem em cheio nessas horas”,
 ao observar as relações sintáticas estabelecidas entre os termos que a constituem, é possível afirmar que seu sujeito classifica-se como:

a) desinencial.
b) indeterminado.
c) simples.
d) inexistente    

o que vem em cheio nessas horas? 'algo' <- Sujeito simples // Alternativa 'C' a correta.

025. (IBFC/2022/MGS/MONITOR EDUCACIONAL) Faça a análise sintática da seguinte estrutura:
 “O professor divulgou as notas aos alunos”. A este respeito, analise as afirmativas abaixo e dê valores Verdadeiro (V) ou Falso (F).

(  )	 “O professor” é o sujeito da oração.
(  )	 “divulgou as notas aos alunos” é o predicado.
(  )	 “as notas” é o objeto indireto.
(  )	 “aos alunos” é o objeto direto.
(  )	 “o”, “aos” são adjuntos adnominais.

Assinale a alternativa que apresenta a sequência correta de cima para baixo.
a) V - V - F - F - V.
b) V - V - V - F - F.
c) F - F - F - F - F.
d) V - F - V - F - F.

O professor = sujeito simples
divulgou = VTD/I (bitransitivo)
as notas = objeto direto e não indireto -> F
aos alunos = objeto indireto e não direto -> F

(V) “O professor” é o sujeito da oração. Certo! Sujeito simples.
(V) “divulgou as notas aos alunos” é o predicado. Certo! Predicado verbal.
(F) “as notas” é o objeto indireto. Errado! Objeto direto.
(F) “aos alunos” é o objeto direto. Errado! Objeto indireto.
(V) “o”, “aos” são adjuntos adnominais. Certo. A função sintática do artigo é a de adjunto adnominal.
Letra a.

71. (IBFC/2021/PREFEITURA DE SÃO GONÇALO DO AMARANTE – RN/AGENTE ADMINISTRATIVO) 
Analise os enunciados abaixo e assinale a alternativa que apresenta, correta e respectivamente, a classificação dos termos destacados.

I – [yellow]Paulo, o jovem mais dedicado da turma,[reset] recebeu o título de funcionário do mês.
II – [yellow]Paulo, o jovem mais dedicado da turma[reset] recebeu o título de funcionário do mês.

a) I – sujeito e aposto, II- vocativo e sujeito.
b) I – vocativo e sujeito, II- sujeito e aposto.
c) I – aposto e sujeito, II- sujeito e vocativo.
d) I – vocativo e aposto, II- aposto e sujeito.

No item I, o jovem mais dedicado da turma está isolado por vírgulas, explicando quem é Paulo. Portanto, aposto explicativo. Anteposto ao aposto
temos o sujeito, Paulo.

No item II,  temos Paulo 'VOCATIVO' e o jovem mais dedicado da turma como sujeito.

        Portanto, a alternativa 'A' a correta.

72. (IBFC/2021/IBGE/SUPERVISOR DE PESQUISAS/GESTÃO) No verso “[yellow]Há[reset] tempos [yellow]treino/[reset] 
o equilíbrio sobre” (v.4/v.5), destacam-se dois verbos. Ao analisá-los com atenção, é correto 
afirmar que:

a) O verbo “há” é impessoal e poderia ser substituído por “existir”.
b) “treino” está no singular, concordando com um substantivo “equilíbrio”.
c) “há” está flexionado na primeira pessoa do singular, assim como “treino”.
d) O verbo “treino” concorda com um sujeito que não está explícito no verso.
e) O verbo “há” poderia, facultativamente, concordar com o substantivo “tempos”.        

a) Errada. O verbo haver é impessoal, mas foi empregado no sentido de tempo decorrido e poderia ser substituído apenas pelo verbo FAZER.
b) Errada. O sujeito do verbo TREINAR é o EU, ou seja, está elíptico.
c) Errada. A forma verbal “treino” está flexionada no primeira pessoa do singular.
d) Certa. “Há tempos (eu) treino...” O sujeito é elíptico.
e) Errada. Verbo não concorda com complemento.
Letra d.

73. (FUNATEC/2022/CÂMARA DE PRESIDENTE DUTRA – MA/MOTORISTA) Assinale a alternativa que contém um exemplo de sujeito simples.

a) Não consigo relaxar em casa.
b) Criticaram-nos na reunião de ontem.
c) Alguém escondeu minha farda.
d) Nevou como nunca.

a) Errada. (Eu) não consigo relaxar em casa. (Sujeito desinencial)
b) Errada. Quem criticou? Não se sabe. Com o verbo na terceira pessoa do plural e referente vago, o sujeito será indeterminado.
c) Certa. Quem escondeu minha farda? Alguém = sujeito simples.
d) Errada. Nevou = fenômeno da natureza. (Sujeito inexistente)
Letra c.

74. (IBADE/2022/PREFEITURA DE COLÍDER - MT – ADVOGADO) “Trata-se de um exército de trabalhadores urbanos, majoritariamente jovens [...].”
O sujeito dessa oração é classificado como:

a) indeterminado.
b) desinencial.
c) oração sem sujeito.
d) determinado - simples.
e) determinado - composto.

quem trata, trata de: 'de um exército de trabalhadores urbanos <- Objeto indireto // Portanto 'se' é índice de indeterminação do sujeito
'majoritariamente' -> advérbio // 'jovens' -> adjetivo -> Adjunto Adnominais qualificando os trabalhadores ( substantivo concreto)
'de trabalhadores urbanos' -> Adjunto Adnominal ( agentes do exército -> substantivo concreto )

Quando a palavra SE acompanhar VTI, VI ou VL (sem referente preciso), o SE será um índice de indeterminação do sujeito.
 Assim, o sujeito será indeterminado. O verbo tratar é VTI. 

    Alternativa 'A' a correta.

75. (QUADRIX/2021/CRF – RR/AUXILIAR DE LIMPEZA)

'...que provavelmente a maioria das pessoas nunca se perguntou: o que é um medicamento?'

Na oração “provavelmente a maioria das pessoas nunca se perguntou” (linhas 6 e 7),
 a forma verbal “perguntou” pode ficar no singular ou no plural.

 'a maioria' -> singular -> Núcleto do sujeito, seu especificante é 'das pessoas' que está no plural. Portanto o verbo 'perguntou'
 pode concordar tanto com o núcleo que está no singular quanto ao seu espefificante que está no plural.


76. (QUADRIX/2022/CFFA/TÉCNICO ADMINISTRATIVO)

A maioria dos casos de vocabulário deficiário ou forma de falar inadequada para a idade tende a ser transitória.

A flexão da forma verbal “tende” (linha 14) na terceira pessoa do singular justifica-se pela concordância do verbo com o termo “maioria” 
(linha 13), que é o núcleo do sujeito da oração.

CORRETO. 

    Atenção!

    Por que o verbo 'tende' não pode ir para o plural?

        O verbo "tender" não é associado diretamente a uma ação de um grupo específico (como no caso de "perguntar"), 
        mas a uma característica ou tendência atribuída ao núcleo do sujeito ("maioria"). Portanto ele só deve concordar com o núcleo.

         O verbo "tender" não admite a concordância semântica. é um verbo de estado.

         Já o verbo 'perguntar' é de ação , associado às pessoas, portanto permite concordância semântica tanto com o núcleo quanto com
         o especificante.

         Na frase "a maioria dos casos tende a ser transitória", a norma padrão restringe a concordância ao núcleo do sujeito,
          já que o verbo expressa um estado/tendência atribuível exclusivamente à "maioria".


77. (QUADRIX/2022/CRM-SC/ASSISTENTE ADMINISTRATIVO/ADAPTADA)

porque há vários hormônios que participam do ciclo do apetite e da sociedade.

'há' por 'existe'

Em 'há vários hormônios', nesse caso temos o verbo haver empregado o sentido de existir. VTD e impessoal. Há - VTD
vários hormônios = objeto direto

Na substituição de haver por existir haverá modificação na sintaxe e na concordância. O correto então é: 'existem vários hormônios'
existem = VI
vários hormônios = sujeito
O verbo existir é intransitivo, ou seja, não pede complemento. Além disso, é considerado um verbo pessoal, isto é, possui sujeito.

78. (QUADRIX/2022/CRA-PR/AUXILIAR DE SERVIÇOS GERAIS)

76,1% dos entrevistados afirmaram que comem arroz com frequência, e 60% disseram que não dispensam o feijão.

'afirmaram' por 'afirmou'

Esta incorreto porque tanto o percentual quanto o substantivo posterior estão no plural.
Não podemos colocar 'afirmou' na oração.  Precisa concordar em número singular/plural

'76,1%' -> plural
'dos entrevistados' -> plural

79. (QUADRIX/2022/CRECI - 24ª REGIÃO-RO/FISCAL)

Além disso, existem boas projeções para o mercado imobiliário, no geral.

'existem' por 'há'

O verbo "há" (do verbo haver) pode ser usado com o sentido de "existir". Nesse caso, ele é impessoal, ou seja, não possui sujeito,
 e deve ser conjugado apenas na 3ª pessoa do singular.
Diferentemente de "existem", que concorda com o sujeito plural "boas projeções", o verbo "há" não sofre flexão, pois não admite sujeito.

"Além disso": Adjunto adverbial de acréscimo.
"Há boas projeções":
"Há": Verbo impessoal no singular.
"Boas projeções": Objeto direto do verbo "haver".
"Para o mercado imobiliário": Adjunto adverbial de finalidade.
"No geral": Adjunto adverbial de modo.

80. (QUADRIX/2021/CRMV-RO/FISCAL/MÉDICO VETERINÁRIO)

Algo que os setores da produção almejavam havia muito tempo.

'havia' por 'faziam'

ERRADO. O verbo fazer também é impessoal, não admite sujeito e somente fica no singular. O correto seria: 'Fazia muito tempo'

81. (QUADRIX/2021/CFT/SECRETÁRIO (A))

Lembremos que houve um universo sem a escrita que foi estruturado de uma maneira muito diferente.

O verbo 'houve' está no singular porque concorda com o termo 'um universo'.

O verbo 'houve' é impessoal, deve somente ficar no singular por não concordar com o sujeito, não possui sujeito.
De certa forma, 'houve' é um VTD - Verbo transitivo direto, houve o que? 'um universo' -> objeto direto
Além disso o verbo não concorda com seu complemento 'um universo' não pode ser sujeito, 'um universo' é objeto direto.

82. (QUADRIX/2021/CRP - MA - 22ª REGIÃO/ASSISTENTE TÉCNICO ADMINISTRATIVO E SERVIÇOS)

'Mesmo assim, sempre havia erros nas contas e raramente o que estava no papel correspondia...'

O verbo 'havia' poderia ser substituido por acontecia, sem prejuízo dos sentidos e da correção gramatical do texto.

ERRADO - O sentido não mudaria mas gramaticalmente sim, haveria prejuizo.

O verbo 'haver' é impessoal e não admite sujeito, sendo assim 'erros' é objeto direto.
Apesar do verbo 'haver' ser impessoal e não admitir sujeito ele é transitivo direto. 'erros' é seu complemento direto.
'acontecer' -> verbo pessoal e admite sujeito, que por sua vez é 'erros' <- Sujeito
Dessa forma, o verbo deve concordar com o sujeito, então seria 'aconteciam' e não 'acontecia'.
    Erro de concordância verbal.

83. (QUADRIX/2021/CREFONO - 4ª REGIÃO/FONOAUDIÓLOGO FISCAL/ADAPTADA)

'Existe uma vantagem evidente no uso da voz para comandar máquinas.'

O sujeito da forma verbal 'existe' é inexistente.

O verbo 'existir' é pessoal, admite sujeito. Portanto ERRADO.
'existe' -> Verbo Intransitivo.   ( O sujeito já completa o sentido, por isso não há objeto direto e o verbo é intransitivo. )
'uma vantagem evidente' -> sujeito simples
'no uso da voz para comandar máquinas' -> adjunto adverbial de meio
'para comandar máquinas' -> adjunto adverbial de finalidade

84. (QUADRIX/2021/CREMESE/MÉDICO)

'... a de frotas encabeçadas por dois almirantes chineses, Zhou Man e Hong Bao, haviam navegado da África até a foz do Rio Orenoco...'

Por ser considerado impessoal, o verbo 'haviam' poderia ser substituido por 'havia', sem prejuízo da correção gramatical do texto.

ERRADO - Repare que há uma locução verbal 'haviam navegado' e o verbo haver está como verbo auxiliar / 'navegado' -> verbo principal
        Sendo assim 'haviam' deve concordar com o sujeito 'dois almirantes chineses' que está no plural.
                            Assim, esse verbo não pode ir para o singular.

85. (FUNDATEC/2023/FOZPREV/ANALISTA PREVIDENCIÁRIO/ARQUIVOLOGIA)

...e que lhes garanta proteção social - e não apenas contas a pagar.'

Assinale a alternativa que apresenta a correta função sintática do pronome oblíquo sublinhado no trecho a seguir:
'que lhes garanta proteção social.'

a) Complemento nominal.
b) Objeto direto.
c) Objeto indireto.
d) Sujeito.
e) Agente da Passiva.

'que' -> conjunção integrante
'lhes' -> objeto indireto do verbo transitivo indireto -> garanta, quem garante, garante algo a alguém: 'lhes' -> objeto indireto
'proteção social' -> quem garante, garante alguma coisa: 'proteção social'
Portanto, o 'lhes' é objeto indireto -> alternativa 'C'

86. (IBADE/2022/PREFEITURA DE COLÍDER – MT/TÉCNICO EM SEGURANÇA DO TRABALHO) “[...] para [yellow]lhe[reset] dar uma notícia grave: A Primavera chegou.” 1º§
O termo destacado exerce a seguinte função sintática:

a) sujeito.
b) complemento nominal.
c) objeto indireto.
d) adjunto adverbial.
e) adjunto adnominal.

quem dar, dar uma notícia a alguém: 'lhe' <- objeto indireto
quem dar, dar algo: 'uma notícia grave' <- objeto direto

87. (FAU/2022/PREFEITURA DE ALTAMIRA DO PARANÁ – PR/ASSISTENTE SOCIAL) 
Assinale a alternativa que apresente a função sintática exercida pela oração subordinada no período:
 “A pesquisa mostrou ainda [yellow]aumento na falta de segurança[reset] no trajeto para a escola”.

a) Sujeito.
b) Objeto Indireto.
c) Predicativo do Sujeito.
d) Aposto.
e) Objeto Direto.

O verbo 'mostrar' é transitivo direto, quem mostra, mostra algo: 'aumeto na falta de segurança' <- objeto direto
sujeito: 'a pesquisa'
'no trajeto para a escola' <- adjunto adverbial de meio

Alternativa 'e'


88. (UNICENTRO/2022/PREFEITURA DE CORONEL VIVIDA – PR/MÉDICO DA FAMÍLIA) 
Assinale a alternativa que apresente a função sintática dos termos em destaque no seguinte 
trecho: “A Candelária é sem dúvidas o coração da cidade, o bairro reúne as principais atrações 
turísticas e preserva [yellow]a tradição colombiana”.[reset]

a) Sujeito.
b) Objeto Direto.
c) Complemento Nominal.
d) Predicativo.
e) Objeto Indireto.

quem preserva, preserva algo: 'a tradição colombiana' <- Objeto Direto
'o bairro' -> sujeito
'reúne' -> verbo que quem reúne, reúne algo: 'as principais atrações turísticas' <- Objeto direto
' A Candelária' -> sujeito // 'é' -> verbo de ligação, sendo assim, 'o coração da cidade' <- Predicativo do sujeito
'sem dúvidas' -> adjunto adverbial de modo

Portanto, alternativa 'B'. Objeto direto do verbo transitivo direto 'preserva'


89. (IBADE/2022/PREFEITURA DE COSTA MARQUES - RO - MICROSCOPISTA/ADAPTADA) 
“Cada obstáculo pode ser encarado como uma oportunidade para descobrirmos [yellow]a nossa coragem desconhecida [reset][...].”4º§

A expressão acima sublinhada exerce a função de:

a) predicativo.
b) objeto direto.
c) objeto indireto.
d) sujeito.
e) predicado.

quem descobri, descobri algo: ' a nossa coragem desconhecida' -> Objeto direto. Complemento direto do verbo 'descobrimos'
Sujeito elíptico -> 'nós'

90. (OBJETIVA/2022/PREFEITURA DE SÃO MIGUEL DO PASSA QUATRO – GO/MÉDICO) 
Assinalar a alternativa que apresenta uma oração cujo verbo tem como complemento um objeto indireto:

a) Ana e Carla tem mais uma chance.
b) Ela é tão linda.
c) Essas notícias falam só a verdade.
d) Esses móveis precisam de conserto

'ana e carla' -> Sujeito Composto
'tem' -> acento diferencial -> plural -> 'têm' // 'mais uma chance' -> objeto direto do verbo transitivo direto 'têm'

            Não é a alternativa 'A'.

'Ela' -> Sujeito Simples
'é' -> Verbo de ligação
'tão linda' -> Predicativo do sujeito

        Não transitividade verbal na alterantiva 'B'

item C -> Essas notícias -> Sujeito simples // falam, quem fala, fala algo: 'só a verdade' <- Objeto direto do verbo transitivo direto 'falar'

        Não há objeto indireto no item C

Item D - Esses móveis -> Sujeito // 'precisam' -> verbo transitivo direto // 'de conserto' <- Objeto indireto ( de - Preposição )        

91. (FUNDATEC/2022/PREFEITURA DE VIAMÃO – RS/TÉCNICO EM ENFERMAGEM) 
No trecho “todas as outras formas de ajudar a combater [yellow]o mosquito[reset] e, portanto, a transmissão da dengue”,
 a expressão sublinhada tem função de:

a) Agente da passiva.
b) Adjunto adverbial.
c) Complemento nominal.
d) Objeto indireto.
e) Objeto direto.

'todas as outras formas' -> sujeito
'ajudar' -> verbo principal da locução verbal -> 'ajudar a combater' -> complemento direto -> ' a combater o mosquito'
'e' -> conjunção aditiva - Não há função sintática // 'portanto' -> conjunção conclusiva
'a transmissaõ da dengue' -> objeto direto

Portanto, alternativa correta a: 'e'

92. (CESPE/CEBRASPE/2022/BANRISUL/ANALISTA DE SEGURANÇA DA TECNOLOGIA DA INFORMAÇÃO)

O termo “o novo cartão do Banrisul” exerce a função de complemento da forma verbal “Chegou”.

'chegou' -> verbo intransitivo 
'o novo cartão do Banrisul' -> Sujeito posposto

ERRADO.

93. (CESPE/CEBRASPE/2022/SECONT-ES/AUDITOR DO ESTADO/ADMINISTRAÇÃO)

'e ao toque brilhava o brilho da água deles,'

o termo “brilho” funciona sintaticamente como complemento da forma verbal “brilhava”.

quem brilhava? 'o brilho da água deles' <- Sujeito
quem brilhava, brilhava a algo: 'ao toque' -> Objeto indireto

94. (QUADRIX/2022/CRN 4ª REGIÃO - ES, RJ/NUTRICIONISTA FISCAL)

Na confusão , circulavam notícias diversas.

Na linha 31, o termo “notícias diversas” funciona como complemento do verbo “circularam”.

quem circulavam? 'notícias diversas' -> Sujeito
'circulavam' -> verbo intranstivo

95. (AMEOSC/2022/PREFEITURA DE ITAPIRANGA – SC/PROFESSOR DE ARTE) Você será o único no piquenique.

Assinale a opção CORRETA quanto à análise sintática.

a) O predicado é nominal cujo núcleo é o vocábulo ‘piquenique’.
b) O pronome do caso reto ‘você’ é o aposto da oração.
c) O vocábulo ‘único’ é o predicativo do sujeito.
d) O predicativo do sujeito é o pronome do caso reto ‘você’.

'você' -> sujeito
'será' -> verbo de ligação
'o único no piquenique' -> Predicado nominal / 'único' -> núcleo do predicado nominal
'o único' -> Predicativo do sujeito
'no piquenique' -> Adjunto adverbial de lugar

a.) O predicado é nominal cujo núcleo é o vocábulo ‘piquenique’. ( no piquenique está preposicionado. O núcleo é um substantivo ou adjetivo)
b. 'você' -> núcleo
c. CORRETO
d. 'você' é núcleo. 'o único' -> predicativo do sujeito

Letra C a correta.

96. (PREFEITURA DE BAURU - SP/2022/PREFEITURA DE BAURU – SP/NUTRICIONISTA/EDITAL N. 12)
No fragmento do texto “carnes processadas são mais [yellow]prejudiciais[reset] do que carnes não processadas”, 
o termo em destaque exerce a função sintática de:

a) Predicativo do sujeito.
b) Adjunto adverbial.
c) Complemento Nominal.
d) Objeto direto

carnes processadas -> sujeito
'são' -> Verbo de ligação
'mais processadas' -> Predicativo do sujeito

Alternativa correta -> Letra 'A'

Uma das funções sintáticas do adjetivo é a de predicativo do sujeito. No contexto, o vocábulo 
“prejudiciais” é uma característica do substantivo “carnes”.

97. (REIS & REIS/2022/PREFEITURA DE JUATUBA – MG/PEDAGOGO) Assinale a alternativa em que o termo em negrito é um predicativo do sujeito:

a) Antônio chegou [yellow]exausto[reset] do trabalho.
b) [yellow]Antônio[reset] chegou exausto do trabalho.
c) [yellow]Professor[reset], posso ir ao banheiro?
d) O político assinou [yellow]o documento.[reset]

a. Predicativo do sujeito ( atenção: característica do sujeito Antônio, adjetivo ao Antônio, portanto, função sintática de predicativo do sujeito)
b. Sujeito
c. vocativo
d. Objeto direto


98. (REIS & REIS/2022/PREFEITURA DE JUATUBA – MG/ASSISTENTE SOCIAL) “Mamãe achou o parque [yellow]sujo[reset]”. 

O termo em destaque na frase é um:

a) Predicativo do sujeito
b) Objeto direto
c) Predicativo do objeto
d) Objeto indireto

Predicativo do objeto a qual é um complemento do objeto direto 'o parque' <- Objeto direto

99. (REIS & REIS/2022/PREFEITURA DE JUATUBA – MG/ASSISTENTE SOCIAL)
Na frase “Marina chegou [yellow]cansada[reset] da festa”, o termo cansada é um:

a) Predicativo do objeto
b) Predicativo do sujeito
c) Complemento nominal
d) Aposto

'marina' -> sujeito
'chegou' -> Verbo Intransitivo / Portant, predicado nominal.
'cansada' -> caracteristica atribuida a Marina -> Predicativo do sujeito
'da festa' -> Adjunto Adverbial de lugar

Portanto, a alternativa correta é:  'B'

100. (IBFC/2022/MGS/CARGOS DE NÍVEL MÉDIO) No texto, encontramos estruturas sintáticas que são formadas por:
 sujeito + verbo de ligação + predicativo do sujeito.
 Assinale a alternativa que apresenta a oração que contenha essa estrutura descrita.

a) Todo mundo comemora o Dia das Mães.
b) O presente do Dia das Mães era todo um acontecimento.
c) Os romanos herdaram essa tradição.
d) A poeta e ativista Julia Ward Howe escreveu a Proclamação do Dia das Mães.


a. 'todo mundo' -> Sujeito / 'comemora' -> VTD / 'o dia das mães' -> objeto direto
b. 'o presente do dias das mães' -> Sujeito / 'era' -> verbo de ligação // 'todo um acontecimento' -> Predicativo do sujeito
c. 'os romanos' -> sujeito / 'herdaram' -> VTD // 'essa tradição' -> Objeto direto
d. 'a poeta e ativsita Julia ward howe' -> Sujeito // 'escreveu' -> VTD / ' a proclamação...' -> objeto direto


101. (AMEOSC/2022/PREFEITURA DE PRINCESA – SC/AGENTE COMUNITÁRIO DE SAÚDE) 
Na oração “A linguagem é a maior prova disso “, temos:

a) Uma frase nominal.
b) Um predicado Verbo-Nominal.
c) Um predicado Nominal.
d) Um predicado Verbal.

Temos um predicado nominal. Na frase tem somente um verbo de ligação 'é'
' a maior prova disso' é uma característica da linguagem. Predicativo do sujeito

Alternativa 'C'

No predicado verbo-nominal, deve haver verbo de ação + predicativo.
Não há verbo de ação da frase, somente de ligação.

102. (AMEOSC/2022/PREFEITURA DE PRINCESA – SC/ARQUITETO E URBANISTA)
No trecho: “Amizade é UMA PALAVRA PEQUENININHA, mas que nunca vem sozinha.”, o termo 
destacado está exercendo função sintática de:

a) Objeto indireto.
b) Complemento nominal.
c) Predicativo do sujeito.
d) Objeto direto.

Trata-se de um predicado nominal e o trecho “uma palavra pequenininha” exerce função sintática de predicativo do sujeito.

Alternativa 'C'

103. (IBADE/2022/PREFEITURA DE SOORETAMA – ES/PROFESSOR MAE-II/ENSINO FUNDAMENTAL/LÍNGUA PORTUGUESA)
 “A bomba atômica é [yellow]triste[reset] [...].” Marque a alternativa que apresenta a função sintática da palavra destacada.

a) Predicado.
b) Adjetivo.
c) Predicativo.
d) Complemento verbal.
e) Complemento nominal.

Alternativa 'C' - Predicativo do sujeito -> Característica da bomba - adjetivo da bomba

104. (METRÓPOLE/2022/PREFEITURA DE PEDRA BRANCA DO AMAPARI – AP/ASSISTENTE SOCIAL)

bons tempos aqueles em que só a pedra era lascada

Qual é a função sintática da palavra “lascada” nesse meme?

a) Predicativo do objeto.
b) Aposto especificador.
c) Adjunto adnominal.
d) Predicativo do sujeito.
e) Adjunto adverbial.

A pedra = sujeito
era = verbo de ligação
lascada = predicativo do sujeito.
Letra d.


105. (QUADRIX/2022/CRP 18ª REGIÃO MT/AUXILIAR ADMINISTRATIVO DE SECRETARIA)

No trecho “Por exemplo: o homem ficou feliz e calmo ou seguiu chateado?” 
os termos “feliz”, “calmo” e “chateado” exercem todos a mesma função sintática: predicativo do sujeito.

CORRETO -  'o homem' -> Sujeito // 'ficou' -> Verbo de ligação // 'feliz' -> Adjetivo com função sintática de predicativo do sujeito
'calmo' -> Adjetivo do homem que por sua vez possui função sintática de predicativo do sujeito
'seguiu' -> verbo de ligação // 'chateado' -> adjetivo do homem -> Predicativo do sujeito também.

106. (CESPE/2016/TCE-PA/CONHECIMENTOS BÁSICOS/CARGOS 1, 18, 19, 37 E 38)

De que adiantaria,então, tornar a lei mais rigorosa, se nem nas condições atuais esses responsáveis estão sendo capazes de cumpri-la?

Na linha 21, o termo “mais rigorosa” funciona como um predicativo do termo “a lei”.

CORRETO

o verbo "tornar" é usado como verbo transitivo direto, pois indica a ação de transformar algo:

Verbo: "tornar" (transitivo direto).
Objeto direto: "a lei".
Predicativo do objeto: "mais rigorosa".

    Atribuindo uma característica ao complemento 'a lei' que por sua vez é objeto direto.

107. (CESPE/2019/SLU-DF/CONHECIMENTOS BÁSICOS)

Logo atrás de mim, uma senhora furiosa levantou-se.

O deslocamento do termo “furiosa” (ℓ.8) para imediatamente após a forma verbal “levantou-se” 
(ℓ.9) manteria a coerência do texto.


No texto: “uma senhora furiosa levantou-se” (furiosa = adjunto adnominal/ característica permanente)
Na reescritura: “uma senhora levantou-se furiosa” (furiosa = predicativo do sujeito/ característica temporária).

Certo. Manteria a coerência mas a correação gramatical seria diferente.

'furiosa' antes do verbo 'levantou-se' seria um adjunto adnominal para o substantivo concreto 'uma senhora'
'furiosa' após o verbo seria um predicativo do sujeito a qual o verbo 'levantou-se' seria um verbo de ligação.

108. (FUNDATEC/2022/PREFEITURA DE TAQUARI – RS/ASSISTENTE SOCIAL)
 Assinale a alternativa que indica a correta função sintática exercida pela oração sublinhada no trecho a 
seguir: “enquanto aguardo meu personal para uma hora de treino de força, confiante [yellow]de que isso me garantirá alguma longevidade”.[reset]

a) Complemento nominal.
b) Sujeito.
c) Adjunto adverbial.
d) Adjunto adnominal.
e) Objeto direto.

A palavra “confiante” é um substantivo abstrato e exige complemento. Afinal, quem está confiante, 
está confiante de algo. Logo, toda oração subsequente exerce função sintática de complemento nominal.
 Em regra, chamamos de oração subordinada substantiva completiva nominal.
Letra a.

109. (INSTITUTO ACCESS/2022/CELEPAR – PR/ADVOGADO JÚNIOR)
 “‘Considerando essa perspectiva, uma ID digital segura será ainda mais imprescindível e os ganhos serão imensos, 
sobretudo na facilidade de interação do indivíduo (1) com os diversos ecossistemas, na oferta de serviços (2) por parte das várias organizações,
e, claro, no respeito à privacidade do cidadão (3) e alinhamento às leis gerais de proteção de dados (4)’, diz ela.”

No trecho acima, a função sintática dos termos sublinhados (1, 2, 3 e 4) pode ser de adjunto adnominal (AA) ou complemento nominal (CN).

Em relação a esses termos, é correto afirmar que desempenham, respectivamente, função de:

a) AA, CN, AA e CN.
b) AA, AA, CN e CN.
c) CN, CN, AA e AA.
d) CN, AA, CN e AA.
e) CN, AA, AA e CN.

interação do indivíduo -> interação DELE , relação de posse  -> AA
oferta de servicos -> serviços são ofertados -> paciente -> CN
a privacidade do cidadão -> 'cidadão -> AA ( privacidade DELE - posse)
proteção de dados -> os dados são protegidos -> 'dados' paciente -> CN

Portanto, alternativa 'A' a correta.

110. (FUNDEP/2022/UFJF/ASSISTENTE DE ALUNOS/EDITAL N. 70) 
Na passagem “Apresentar material digno à magnitude de uma figura pública, localizar e discutir seu legado, 
é papel básico da imprensa, o chamado registro histórico.”, 

o termo que complementa um nome de maneira adequada é:

a) “à magnitude de uma figura pública”.
b) “seu legado”.
c) “material digno”.
d) “papel básico da imprensa”.
e) “registro histórico”.

Alternativa 'A', a correta.
O termo "à magnitude" é um substantivo abstrato (magnitude) complementado por "de uma figura pública",
que expressa o destino ou referência da magnitude.

"De uma figura pública" é um complemento nominal porque completa o sentido de "magnitude".

Na letra 'b'. 
Aqui, "seu" é um pronome possessivo que determina o substantivo "legado".
 No entanto, não há complemento nominal porque não há uma preposição que complemente o sentido de "legado".

Na letra 'C'.

"Digno" é um adjetivo que qualifica "material". Não há complemento nominal aqui, apenas uma relação adjetiva.

Na letra 'D' - papel básico da imprensa

"Da imprensa" complementa o substantivo "papel", mas funciona como um adjunto adnominal (expressa posse ou origem), 
e não como complemento nominal.

Na alternativa 'E' -> registro histórico

"Histórico" é um adjetivo que qualifica "registro". Assim, não há complemento nominal, mas uma relação de adjetivação.


111. (IBADE/2022/PREFEITURA DE COSTA MARQUES – RO/ENGENHEIRO AGRÔNOMO)
“[...] a adoção é hoje vista pelos órgãos judiciais como um artifício usado para garantir os 
direitos da criança e do adolescente de terem acesso [yellow]a um meio familiar saudável [...].”[reset]

A expressão destacada é um:

a) objeto direto, por isso faz parte dos termos integrantes da oração.
b) objeto indireto, por isso faz parte dos termos integrantes da oração.
c) complemento nominal, por isso faz parte dos termos integrantes da oração.
d) complemento nominal, por isso faz parte dos termos essenciais da oração.
e) predicativo do sujeito, por isso faz parte dos termos essenciais da oração

O nome “acesso” exige complemento. Afinal, quem tem acesso, tem acesso a algo, a alguma 
coisa ou a alguém. Logo, “a um meio familiar saudável” exerce função sintática de complemento nominal.
Vale lembrar que o CN é um termo integrante da oração.
'acesso' <- substantivo abstrato / 
Letra c.


112. (VUNESP/2022/PC-SP/ESCRIVÃO DE POLÍCIA)

'Ao longo de quinze anos, a pesquisadora Vanessa Bohns realizou experimentos [yellow]sociais[reset] com cerca de 15 000 pessoas...'

a) objeto direto.
b) predicativo do sujeito.
c) aposto.
d) complemento nominal.
e) adjunto adnominal.

realizou = VTD // experimentos sociais = Objeto direto // 'sociais' -> adjunto adnominal

113. (CONTEMAX/2022/CÂMARA DE SANTA TEREZINHA – PE/TÉCNICO ADMINISTRATIVO)
 O papel sintático do termo destacado no excerto “Ele demonstra ter muito mais tolerância 
[yellow]com as revistas[reset] do que com a TV; (...)” está corretamente apontado na opção:

a) Objeto indireto.
b) Complemento nominal.
c) Adjunto adnominal.
d) Objeto direto.
e) Adjunto adverbial

'tolerância com as revistas' -> Complemento Nominal -> 'tolerância' <- substantivo abstrato // 'com as reivistas' <- paciente
Afinal, quem tem tolerância, tem tolerância com algo, com alguma coisa ou com alguém. Portanto, o trecho “com as revistas”,
o qual completa o nome tolerância, exerce função sintática de complemento nominal.

Alternativa correta a 'B'

114. (INSTITUTO ACCESS/2022/TJ-PB - JUIZ LEIGO) “A socióloga argumenta que a educação 
sexual nas escolas, que vive sob ataque de grupos políticos (1) no país, ajudaria na prevenção 
da gravidez precoce (2) e, consequentemente, no número de abortos.”

No período acima, as funções dos termos (1) e (2) são, respectivamente, de

a) adjunto adnominal e adjunto adnominal.
b) complemento nominal e complemento nominal.
c) adjunto adnominal e complemento nominal.
d) complemento nominal e adjunto adnominal.

'ataque de grupos políticos' <- 'grupos políticos atacam' Agente -> Adjunto Adnominal
'prevenção da gravidez precoce' -> ' a gravidez é previnida' -> Complemento nominal -> paciente

Alternativa 'C'

115. (FAFIPA/2018/FOZHABITA/AGENTE FISCAL JÚNIOR) Marque a alternativa que indica apenas termos acessórios da oração:

a) Vocativo.
b) Sujeito e predicado.
c) Adjunto adverbial, adjunto adnominal e aposto.
d) Objeto direto, objeto indireto, predicativo do sujeito e predicativo do objeto.

Alternativa 'C' -> adjunto adverbial, adjunt adnominal e aposto

116. (FAFIPA/2018/PREFEITURA DE PARAÍSO DO NORTE – PR/EDUCADOR SOCIAL) Marque a alternativa em que a função sintática da palavra sublinhada, 
dada entre parênteses e em itálico, está INCORRETA:

a) José, [yellow]advogado renomado[reset], nunca havia viajado para a Europa. (vocativo)
b) [yellow]Cláudia[reset] encomendou uma pizza. (sujeito)
c) Juliano escreveu uma carta [yellow]aos seus pais.[reset] (objeto indireto)
d) Lavei [yellow]a louça[reset]. (objeto direto)

“advogado renomado” = aposto explicativo.
Vale frisar que o aposto consiste na relação em que um substantivo está ligado a outro substantivo.
José = substantivo
Advogado = substantivo
Ou seja, relação apositiva.

A alternativa 'A' é a incorreta.

117. (CETREDE/2018/PREFEITURA DE CANINDÉ – CE/ASSISTENTE SOCIAL) Qual das frases a seguir apresenta complemento nominal?

a) O dourado alimenta-se de pequenos peixes.
b) Independentemente do empréstimo, construirei a casa.
c) A lâmpada elétrica foi inventada por Tomas Edson.
d) A felicidade de um povo depende da educação da juventude.
e) Há muita gente que não crê em nada.

Item 'A'  ->  'o dourado' -> sujeito // alimenta-se -> VTI // 'de pequenos peixes' -> Objeto Direto
item 'B'  ->  'independentemente' -> adjunto adverbial (advérbio) <- 'do empréstimo' -> Complemento Nominal
                    'construirei' -> VTD // 'a casa' -> Objeto Direto

Item 'C' -> A lâmpada elétrica foi inventada por Tomas Edson.                    

                'a lâmpada elétrica' -> Sujeito // 'foi inventada' -> locução verbal // 'por thoma edson' -> agente da passiva

Item 'D' -> ' a felicidade de um povo' -> Sujeito // depende -> VTI // 'da educação da juventude' <- Objeto indireto

Item 'E' -> 'Há' -> VTD // 'muita gente' -> objeto direto / 'que não crê em nada' -> oração subordinada adjetiva

118. (CESPE/CEBRASPE/2019/PREFEITURA DE SÃO CRISTÓVÃO – SE/PROFESSOR DE EDUCAÇÃO BÁSICA/PORTUGUÊS)

'pedra ou indigesto, um grão imastigável,..'

o termo “imastigável” funciona como complemento nominal de “grão”.

ERRADO - O complemento nominal é um termo SEMPRE preposicionado, o qual completa nome abstrato, 
adjetivo ou advérbio.
Perceba que a palavra “imastigável” não está preposicionada.
Por se tratar de um adjetivo, o vocábulo “imastigável” exerce função sintática de adjutno adnominal.
Errado.

119. (CESPE/CEBRASPE/2021/SEDUC-AL/PROFESSOR/PORTUGUÊS)

Daí a certeza com que o vulgo, cujo faro é extremamente delicado, distingue o medalhão completo do medalhão incompleto.
No último período do texto, o termo “do medalhão incompleto” exerce a função sintática de adjunto adnominal.

ERRADO - o verbo 'distingue' é transitivo direto e indireto. 'o medalhão completo' <- objeto direto / 'do medalhão incompleto' -> ob. indireto

120. (CESPE/CEBRASPE/2021/MPE-SC/PROMOTOR DE JUSTIÇA SUBSTITUTO - PROVA 2) 
'Comentando sobre a história de Juan Goytisolo a respeito de um velho, Milan Kundera salienta que a biografia —...'

O termo “Milan Kundera” funciona como aposto, uma vez que especifica o termo “um velho”.

ERRADO- Milan Kundera é Sujeito e não aposto.

121. (CESPE/2018/CGM DE JOÃO PESSOA – PB/TÉCNICO MUNICIPAL DE CONTROLE INTERNO/GERAL)

A corrupção é uma doença que deve ser combatida por meio de uma vacina: a educação.

Os dois-pontos empregados na linha 4 introduzem um aposto.

“a educação” tem função explicativa e justifica o susbtantivo “vacina”.
Ou seja, “a educação” = aposto explicativo.
Certo.
'''
    def regencia_verbal(self):

        return '''
        REGÊNCIA VERBAIS ESPECIAIS:

        '''

    def transitividade_verbal (self):

        return '''
        Transitividade Verbal:

        São verbos que normalmente expressam ação, cujo sentido, por ser incompleto, transita para um complemento (objeto), 
        que, por sua vez, constitui a indicação de uma pessoa ou de uma coisa.

        A depender do fato de o verbo transitivo exigir ou não uma preposição para seu sentido transitar para o objeto pertinente,
         é possível subclassificá-lo em transitivo direto, transitivo indireto ou ainda transitivo direto e indireto.

         Verbo Transitivo de ligação:

         Eles ligam um sujeito a uma característica, estado, qualidade (predicativo do sujeito). 

Eis os verbos que costumeiramente funcionam como verbos de ligação:
[yellow]ser, estar, ficar, parecer, permanecer, continuar, viver, tornar-se, andar, etc   [reset]

        Ele será médico. (VL / Predicativo do Sujeito)

        [red]'ele' [reset]-> [yellow]Sujeito simples[reset]
        [red]'será' [reset]-> [yellow]Verbo SER o futuro do presente do indicativo[reset]
        [red]'médico' [reset]-> [yellow]característica atribuida ao sujeito, portanto, predicativo do sujeito.[reset]
        Tipo de predicado: Nominal, pois o núcleo do predicado é o predicativo do sujeito 'médico'
        estabelecida pela conexão com o verbo 'será'

        O animal estava quieto. (VL / Predicativo do Sujeito)

        [red]quem estava quieto?[reset] [yellow]'o animal'[reset]
        [red]'estava'[reset] -> [yellow]Verbo de ligação[reset]
        [red]'quieto'[reset] -> [yellow]característica atribuida ao sujeito, portanto, predicativo do sujeito[reset]

        Durante a conversa, ele ficou apático. (VL / Predicativo do Sujeito)

        [red]'ele'[reset] -> [yellow]Sujeito Simples[reset]
        [red]'ficou'[reset] -> [yellow]verbo 'ficar' de ligação[reset]
        [red]'apático'[reset] -> [yellow]característica do sujeito, portanto, predicativo do sujeito[reset]
        [red]'durante a conversa'[reset] ->[yellow] circunstância para o verbo 'ficar', portanto, adjunto adverbial de tempo[reset]
        O predicado é classificado como predicado nominal, pois o núcleo do predicado é o predicativo do sujeito ("apático"), 
        enquanto o verbo de ligação "ficou" apenas estabelece a relação.

        A garota parecia doente. (VL / Predicativo do Sujeito)

        [red]quem parecia doente?[reset] [yellow]' a garota'[reset]
        [red]'parecia'[reset] -> [yellow]verbo parecer, de ligação[reset]
        [red]'doente'[reset]  -> [yellow]característica do sujeito, portanto, predicativo do sujeito.[reset]

        Atenção! Se houver sentido de ação, não será transitivo de ligação:

            Flávia anda depressa   -> indica ação
            Cláudia está no Paraná -> indica ação

            Flávia anda alegre    -> de ligação
            Cláudia está contente -> de ligação
          

[bg_blue]Verbos transitivos diretos – exigem complemento que se liga ao verbo sem preposição obrigatória (objeto direto).[reset]

        Não vimos nada ( VTD / OD )
            [red]quem vê, vê algo[reset]: nada <- objeto direto[reset]
        [red]verbo 'ver'[reset]: verbo transitivo direto[reset]

        Houve problemas graves
            [red]'houve'[reset] -> [yellow]verbo transitivo direto[reset]
            [red]'problemas graves'[reset] -> [yellow]objeto direto[reset]

        [blue]Espero[reset]-[yellow]a[reset] no lugar de sempre
            [red]'verbo transitivo direto'[reset] -> [yellow]esperar[reset]
            [red]'pronome olblíquo átono'[reset]  -> 'a' -> [yellow]Objeto Direto[reset]

[bg_blue]Verbos transitivos indiretos – exigem complemento que se liga ao verbo com preposição (objeto indireto)[reset]   

        Aspiro ao melhor cargo.

        [red]quem aspira, aspira a:[reset] ao melhor cargo <- [red]Objeto Indireto[reset]
        Verbo Transitivo Indireto -> Aspirar

        [bg_red]** Lembrando que o verbo ASPIRAR possui duplo sentido, dupla transitividade **[reset]
                No sentido de sover, aspirar, sugar.
                        Exemplo: A diarista aspirou o pó da sala < 'aspirar' -> Verbo Transitivo direto (VTD)
                No sentido de desejar, almejar, ele é Verbo Transitivo indireto, exige preposição 'a'
                quem aspira, aspira a?
                        Exemplo: Ele aspira a um cargo público         

        Nós confiamos em Deus.
            [red]quem confia, confia em? [reset]'em' preposição <- [red]Verbo Transitivo Indireto[reset]
                'em deus' -> Objeto Indireto

        Eles lutam contra a desigualdade social                 

            [red]quem luta, luta contra?[reset] <- Verbo Transitivo indireto com o uso do preposição 'contra'
            'contra a desiqualdade social' -> Complemento de transitivo Objeto direto

        O soldado obedeceu prontamente ao comando
            [red]quem obecede, obedece a?[reset] <- Verbo transitivo indireto com complemento indireto 'ao comando'
                    * Lembrando que o verbo obedecer é sempre intransitivo indireto *

[red]Verbos transitivos diretos e indiretos - exigem um objeto direto e um objeto indireto.[reset]

        Comuniquei o fato ao chefe

        [red]quem comunica, comunica algo :[reset] o fato <- [red]Objeto Direto[reset]
        [red]quem comunica, comunica a alguem:[reset] 'ao chefe' <- [red]Objeto Indireto[reset]
                        Portanto, o verbo comunicar é VTDI.

        Oponho-[yellow]me[reset] ao castigo físico das crianças
            [red]quem oponhe, oponhe a algo:[reset] 'ao castigo físico das crianças' <- [yellow]Objeto indireto[reset]
            [red]quem oponhe, opnhe a alguem:[reset] 'me' <- [yellow]Objeto Direto[reset]

            Conforme se percebe em alguns dos exemplos apresentados, os objetos podem ser pronomes oblíquos.
             Nesse contexto, os pronomes oblíquos átonos o, a, os e as funcionam sempre como objetos diretos.

             Vale recordar que os pronomes oblíquos 'o', 'a', 'os' e 'as' podem sofrer o fenômeno da assimilação 
                            quando precedidos de formas verbais terminadas por -z, -r e -s. 
             Tais consoantes são suprimidas e os oblíquos passam a ser grafados nas formas lo, la, los e las, que
                                    também funcionam sempre como objetos diretos.

                Fiz os relatórios.
                [red]'fiz' -> verbo transitivo direto
                [red]'os relatórios' -> Objeto direto
                    Verbo terminado em 'z', fiz + os, fi-los ( 'fi' - VTD / 'los' -> objeto direto )

                Vou vender a casa.
                    [red]'vender' -> VTD // [red]'a casa' -> Objeto Direto
                Verbo terminado em 'R' - Vou vendê-la. ( VTD -> 'vendê' // 'la' -> Objeto Direto )                                        

                Quis esse resultado.
                    [red]'quis'[reset] [yellow]verbo terminado em s[reset], transitivo direto // [red]'esse resultado'[reset] -> objeto direto
                    quis + o // 'qui' -> VTD / 'lo' -> Objeto Direto

                    Os mesmos pronomes o, a, os e as podem sofrer o fenômeno da nasalização quando
                            precedidos de formas verbais terminadas por -am, -em, -ão, -õe. 
                    
                    Nessa situação, nada ocorre com a forma verbal, mas os oblíquos passam a ser grafados nas formas no, na,
                    nos e nas, que também funcionam sempre como objetos diretos.

                    Levaram meu livro

                        verbo levar, terminado em 'am', portanto, caso usar o pronome para concordar com o substantivo seria 'o'
                        [red]quem levam, leva algo:[reset] 'meu livro' -> [yellow]complemento verbal objeto direto[reset]

                        Levaram-no (VTD / OD) -> 'no' -> [red]objeto direto[reset]

                    Contem a verdade

                        [red]quem conta, conta algo:[reset] 'a verdade' -> [red]Objeto direto[reset]
                        verbo terminado em 'em', portanto, caso usar o pronome para concordar com o substantivo seria 'a'

                        Contem-[red]na[reset] -> 'na' -> [yellow]pronome oblíquo átono[reset]

                    Dão más notícias sempre

                        [red]quem dá, dá algo:[reset] 'más notícias' -> [red]Objeto direto[reset]
                        verbo 'dar' terminado em 'ão', portanto, caso usar o pronome oblíquo átono, ênclise obrigatória. 
                            Seria 'as' -> ênclise -> 'nas' -> Dão-nas sempre

                    Compõe a música hoje.
                        [red]quem compõe, compõe algo:[reset] a música <- [red]Objeto Direto[reset]

                    [red]Verbo terminado em 'õe'[reset] -> [yellow]Caso uso do pronome 'a', seria 'na'[reset]
                        [yellow]Compõe-na[reset] hoje -> 'na' - [yellow]Objeto Direto[reset]

[bg_red]Os pronomes lhe e lhes, quando atuam como objetos, sempre funcionam como objetos indiretos.[reset]

        Entreguei-lhe a carta discretamente.

        [red]quem entrega, entrega algo:[reset] 'a carta discretamente' -> [blue]Objeto direto[reset]
        [red]quem entrega, entrega algo a alguem:[reset] 'lhe' <- [blue]Objeto indireto[reset]

        O atendente [blue]sugeriu[reset]-[yellow]lhe[reset] o melhor vinho do restaurante

        [red]quem sugere, sugere algo:[reset] 'o melhor vinho do restaurante' <- [red]Objeto Direto[reset]
        [red]quem sugere, sugere algo a alguem:[reset] 'lhe' <- [red]Objeto Indireto[reset]

        Os demais pronomes oblíquos átonos – vos, se, nos, te, me – pode exercer função de
        objeto direto ou objeto indireto, de acordo com o verbo a que se apresentem vinculados.

        Joana [blue]encontrou[reset]-[yellow]me[reset] na praça.

            [red]quem encontra algo:[reset] não possui
            [red]quem encontra, encontra alquém:[reset] 'me' -> [yellow]Objeto direto[reset]
            [red]'na praça'[reset] -> adjunto adverbial de lugar
            Sujeito simples: [yellow]Joana[reset]

        Ele me obedeceu prontamente.

            [red]quem obedece, obedece a alguém:[reset] 'me' -> [yellow]Objeto direto[reset]
            [yellow]'prontamente'[reset] -> Adjunto Adverbial de modo

Verbos intransitivos:

     São aqueles cuja ação verbal não transita, não passa para nenhum complemento.
     Desse modo, não possuindo objeto, podem formar predicados sozinhos ou com indicações de circunstância de tempo, lugar, modo (adjuntos adverbiais).                        

     A cidade dorme (Verbo Intransitivo)
     'a cidade' -> Sujeito
     'dorme'  -> verbo intransitivo sem complementos para a transitividade

     Infelizmente, a festa acabou. ( acabou -> verbo intransitivo )
            
    Eles cantam bem
        'eles' -> Sujeito simples
        'cantam' -> Verbo intransitivo
        'bem' -> Adjunto adverbial de modo

    Fomos ao shopping e ao cinema.

    'fomos' -> Verbo intransitivo
    'ao shopping e ao cinema' -> Adjunto adverbial de lugar

    Durante o carnaval, fico em casa.

    'durante o carnaval' -> Adjunto adverbial de tempo
    'fico' -> Verbo intransitivo
    'ontem à noite' -> adjunto adverbial de tempo

    Certos verbos que normalmente seriam de ligação podem figurar no predicado apenas
    com adjuntos adverbiais (sobretudo de lugar e tempo). Em tal situação, tais verbos são considerados intransitivos.

    O baile de encerramneto será na quadra da escola

    'será' além de ser verbo de ligação é um verbo de estado , portanto, instransitivo.
    'na quadra da escola' -> Adjunto adverbial de lugar

    A reunião será amanhã, às 14h30.

    'será' usado como tempo transcorrido, intransitivo.
    'amanha','as 14h30' -> adjunto adverbial de tempo

    Os passageiros permaneciam na sala de espera.

    'permanecer' -> verbo de estado, intransitivo.
    'na sala de espera' -> adjunto adverbial de lugar

    No natal, João estava em casa.

    verbo intransitivo: estava ( verbo de estado )
    'em casa' - Adjunto Adverbial de lugar

    A transitividade verbal deve sempre partir do contexto estrutural em que o verbo se apresenta.
     lembre-se de que cada frase é uma frase, o que implica afirmar que o mesmo verbo pode apresentar predicações diversas dependendo de como ele se apresenta na frase.       

    Ela chegará logo. 

    'ela' -> Sujeito Simples
    'chegará' -> verbo intransitivo
    'logo' -> adjunto adverbial

    Um dia, chegarei a médico

    'chegarei' -> verbo de ligação
    'a medico' -> predicativo do sujeito

    Veja outros exemplos:

    Há quem deva e nunca [yellow]pague![reset]

    [red]'pague'[reset] -> [yellow]verbo intranstivo[reset]

    Só [yellow]paguei[reset] ao mecânico 

    [red]'paguei'[reset] -> [red]verbo transitivo indireto[reset] // [red]'ao mecânico'[reset] -> [red]Objeto indireto[reset]

    Você [yellow]pagou[reset] as contas?

    [red]'pagou'[reset] -> objeto direto

    Ela sempre [yellow]falou[reset] bem.

    'falou' -> verbo intransitivo
    'bem' -> adjunto adverbial de modo

    Ela sempre falou a verdade.

    'falou' -> VTD // 'a verdade' -> Objeto direto

    Ela sempre falou a verdade aos repórteres.

    quem fala, fala algo: 'a verdade' a alguém; 'aos reporteres'
    Portanto o verbo 'falou' é: VTDI

    Tratando-se de locuções verbais, deve-se analisar tão somente o verbo principal 
    (que é o último que aparece e sempre se encontra em uma forma nominal: infinitivo, gerúndio ou particípio); 
    verbos auxiliares não são analisados

    As crianças [yellow]devem voltar[reset] da escola logo.

    'voltar' -> Intransitivo, sem complementos
    'da escola logo' -> adjunto adverbial

    Eles já [yellow]devem ter comprado[reset] [blue]isso[reset] antes.

    'comprado' -> VTD // 'isso' -> pronome demonstrativo como objeto direto

    Os dados já [yellow]foram lançados[reset] na planilha.

    'lançados' -> verbo transitivo direto
    'na planilha' -> agente passivo

    4. Adjuntos Adverbiais
Adjunto adverbial é o termo da oração que modifica o verbo (ou um adjetivo ou o próprio advérbio), 
expressando uma circunstância: lugar, tempo, modo, intensidade, negação, afirmação, dúvida, fim, meio, companhia, exclusão, inclusão, concessão, condição, etc.

Atropelei-o, [yellow]efetivamente.[reset](afirmação)
Sei, [yellow]de fato,[reset] a lição.(afirmação)
Morreu [yellow]de fome[reset] durante a seca.(causa)
Brigaram [yellow]por uma coisa ridícula.[reset](causa)
Falaram [yellow]sobre política[reset].(assunto)
Especializou-se [yellow]em Economia[reset] pela USP.(assunto)
Voltarei [yellow]contigo[reset] para nossa cidade.(companhia)
[yellow]Sem esforço[reset], não o conseguirás.(condição)
Não o consigo fazer,[yellow] apesar de minha boa vontade.[reset](concessão)
[yellow]Não obstante sua pobreza,[reset] ele venceu.(concessão)
Apontou [yellow]para o alto[reset].(direção)
[yellow]Talvez[reset] possa ir à cidade.(dúvida)

[yellow]Quiçá[reset] encontre.(dúvida)
Todos partiram,[yellow] menos ela.[reset](exclusão)
Vive [yellow]para o estudo.[reset](fim)
O noivo ali apareceu [yellow]duas vezes.[reset](frequência)
Demoliram-no [yellow]à picareta[reset].(instrumento)
Voltaremos [yellow]logo.[reset](tempo)
Amam-se [yellow]muito[reset] desde a infância.(intensidade)
Jorrava água [yellow]à farta[reset].(intensidade)
Cantas [yellow]bem mal.[reset](intensidade)
Voltaremos [yellow]pelo túnel.[reset](lugar)
Viajou [yellow]para Campinas.[reset](lugar)
[yellow]Daqui[reset] não sairão.(lugar)
Estarei [yellow]em casa.[reset](lugar)
Viemos [yellow]de ônibus.[reset](meio)
Soube [yellow]por intermédio dos alunos[reset] a data da prova.(meio)
Cantas [yellow]mal.[reset](modo)
Erraste [yellow]de propósito.[reset](modo)
Ele sofre [yellow]de teimoso.[reset] (causa)

    [red]Peculiaridades:[reset]

    Objeto Direto preposicionado:

    a.Quando há possibilidade de ambiguidade (duplo sentido). Veja as frases a seguir:

    O caçador o leão matou. (Sentido ambíguo: quem matou quem?)

    Ao caçador o leão matou. (OD preposicionado / sujeito / VTD >> Como o sujeito não pode ser preposicionado, conclui-se que o caçador foi morto pelo leão.)

    [yellow]'ao caçador'[reset] -> [red]Não pode ser o sujeito, pela preposição[reset]
    [yellow]' o leão'[reset]    -> [blue]Sujeito que praticou a ação de matar[reset]
    [yellow]'ao caçador'[reset] -> [green]objeto direto preposicionado[reset]

    b) Quando se precisa realçar a ideia de parte.

    Ele comeu [yellow]o bolo.[reset]  (VTD / OD >> Trata-se do bolo inteiro.)

    [red]quem come, come algo:[reset] 'o bolo' -> Trata-se do bolo inteiro

    Ele comeu [yellow]do bolo.[reset] (VTD / OD preposicionado >> Trata-se de parte do bolo.)

    [red]quem come, come de algo:[reset] 'do bolo' -> [blue]Objeto direto preposicionado[reset]

    c) Quando se emprega pronome oblíquo tônico ou o relativo 'quem' como OD:

    Ele viu [yellow]a mim[reset] apenas. (VTD / OD preposicionado)

    [red]quem vê, vê alguém:[reset] 'a mim' -> [blue]objeto direto preposiconado[reset]

    O palestrante [yellow]a quem[reset] convidei é Juiz do Trabalho. (OD preposicionado / VTD)

    [red]quem convida, convida alguem:[reset] 'a quem' -> [blue]Objeto direto preposicionado[reset]

    d) Quando se emprega pronome de tratamento, demonstrativo, indefinido ou interrogativo.

    Vejo [yellow]a Vossa Excelência[reset] como exemplo de vida. (VTD / OD preposicionado)

        [red]quem ve, ve alguém:[reset] 'a Vossa Excelência' -> [red]Objeto direto preposicionado ( pronome de tratamento )[reset]

    Ele atacou [yellow]a uns[reset] que nada tinham a ver com a briga. (VTD / OD preposicionado)        

        [red]quem ve, ve alguém:[reset] 'a uns' -> [blue]Objeto direto preposicionado ( pronome indefinido )[reset]

    Sempre amou mais [yellow]a estes[reset] do que [yellow]àqueles[reset] que são filhos. (VTD / OD preposicionado)        

        [red]quem ama, ama alguém:[reset] 'a estes' e 'àqueles' -> [blue]Objeto direto preposicionado[reset]

e) Quando o objeto direto é substantivo próprio ou os que indiquem pessoas (normalmente em contexto de indicação de respeito).        

    Louvemos [yellow]ao Senhor![reset] (VTD / OD preposicionado)

    'louvemos' -> [yellow]verbo transitivo direto[reset]
    'ao Senhor' -> [yellow]Substantivo próprio[reset]

    Ama a teus pais e a teus irmãos. (VTD / OD preposicionado)

        quem ama, ama alguém: 'a teus pais' / 'a teus irmãos' -> Objeto direto preposicionado

f) Com certas expressões idiomáticas:

    Expressões idiomáticas são frases ou expressões cujo significado não pode ser deduzido diretamente do significado literal das palavras 
    que as compõem. Elas são usadas de forma figurativa e são características de uma língua específica,
    refletindo a cultura e as tradições do povo que a fala.

    Diante do perigo, ela pediu [yellow]por socorro.[reset] (VTD / OD preposicionado)

    [red]quem pedi, pedi por algo:[reset] 'por socorro' -> [red]objeto direto preposicionado[reset]

    Já cumpri [yellow]com meu dever[reset]

    'com meu dever' -> Objeto direto preposicionado ( expressão idiomática )

        [red]Objeto direto interno ou cognato:[reset]
    Ocorre quando o objeto direto apresenta núcleo cujo radical é o mesmo do verbo que complementa ou carrega consigo sentido contido no mesmo campo semântico do verbo.    

    [yellow]Viveu[reset] [blue]vida de rei[reset]; logo, nada tem a reclamar. (VTD / OD interno)

        Verbo 'viver' transitivo direto // 'vida de rei' -> objeto direto interno ou cognato

        Foi herói; mas, ao fim, [yellow]morreu[reset] [blue]morte infame.[reset] (VTD / OD interno)

        'morreu' -> verbo transitivo direto // 'morte infame' -> Objeto direto interno

        Depois de tanta luta, [yellow]dormirei[reset] [blue]o sono dos justos![reset] (VTD / OD interno)

        Hei de [yellow]cantar[reset] [blue]a canção mais devota[reset] por causa do teu amor. (VTD / OD interno )

        “E [yellow]rir[reset] [blue]meu riso[reset] e derramar meu pranto.” (Vinícius de Moraes) (VTD / OD interno)

        Objeto direto pleonástico:

        Trata-se de recurso estilístico que consiste em empregar um pronome oblíquo átono para enfatizar um objeto direto 
            já apresentado anteriormente na frase.

        Exemplo:

        [yellow]Tuas palavras[reset], [blue]guardo[reset]-[yellow]as[reset] uma a uma. (OD / VTD / OD pleonástico)            

            [red]quem guarda, guarda algo:[reset] 'tuas palavras' -> [red]Objeto Direto[reset] / 'as' -> [red]objeto direto pleonástico[reset]

        [yellow]O rosto da amada[reset], [blue]carrego[reset]-[yellow]o[reset] em meus olhos e minha alma. (OD / VTD / OD pleonástico)

            [red]quem carrega, carrega algo:[reset] 'o rosto da amada' -> [red]Objeto direto[reset] / 'o' -> [red]pronome oblíquo átono[reset] ( objeto direto pleonástico )            

        [red]Objeto indireto pleonástico:[reset]

        [yellow]Aos inimigos[reset], [blue]devo[reset]-[yellow]lhes[reset] nada. (OI / VTDI / OI pleonástico)

        [red]quem deve, deve a alguém:[reset] 'aos inimigos' -> [red]Objeto indireto[reset] // 'lhes' -> [red]pronome obliquo átono, objeto indireto pleonástico[reset]

        [yellow]A mim[reset] não [yellow]me[reset] [blue]agrada[reset] sua atitude. (OI / OI pleonástico / VTI)

        [red]quem agrada, agrada a alguém:[reset] 'a mim' -> [red]objeto indireto[reset] / 'me' -> [red]pronome oblíquo átono, objeto indireto pleonástico[reset]

        '''

    def cn_aa(self):
        return '''
        Complemento Nominal X Adjunto Adnominal:

Complemento nominal é o termo que completa o sentido de substantivos abstratos, adjetivos e advérbios que, como os verbos transitivos,
 têm sentido incompleto. Portanto, enquanto o objeto completa o sentido de um verbo, o complemento nominal completa o sentido de um nome.
        
        AA -> pode ou não ter preposição // CN -> sempre tem preposição

        Um carro desgovernado

        O numeral 'um' está junto ao 'carro' substantivo ao passo que 'desgovernado' também está junto ao nome.
	    Portanto, o numeral 'um' e o adjetivo 'desgovernado' exercem função sintática de adjunto adnominal. 

        Agora se eu colocar um verbo:

    	Um carro está desgovernado -> 'um carro' passa a ser 'sujeito' e 'desgovernado' agora é predicativo do sujeito.

        Obs: Os pronomes adjetivos e os artigos sempre serão adjunto adnominais.

        Esse amor selvagem

        'amor' -> substantivo
            'esse' -> junto ao nome, pronome demonstrativo adjetivo -> não está preposicionado, adjunto adnominal
                'selvagem' -> adjetivo -> adjunto adnominal, não está preposicionado

                As mesas de vidro

            'as' -> artigo -> adjunto adnominal 
                'mesas' -> substantivo
                    'de vidro' -> expressão preposicionada se referindo ao nome 'mesas' -> locução adjetiva // 'mesa' é substantivo concreto 
	                    Portanto, 'de vidro' é adjunto adnominal

	Adjunto adnominal -> refere-se a substantivos concretos ou abstratos
	Complemento nominal -> refere-se a substantivos abstratos, adjetivos e advérbios

            Um dia de sol

                'dia' -> substantivo concreto // 'de sol' -> adjunto adnominal

                O atendimento à comunidade

                'atendimento' -> substantivo abstrato -> derivado do verbo atender, ainda pode ser AA ou CN. Possui preposição.
                A comunidade é o receptor, passiva. Portanto, é complemento nominal

                O atendimento do dentista

                        'do dentista' -> ativo
                                Por ser ativo, é adjunto adnominal.

	                O adjunto adnominal é sempre agente, ativo
	                    Complemento Nominal é sempre paciente, receptor, passivo


                O pedido de socorro

	                'pedido' -> derivado do verbo pedir, substantivo abstrato
	                'de socorro' -> receptor, paciente. Alguém está praticando a ação de pedir ajuda, portanto, Complemento Nominal

                O pedido do pai

                	o pedido do pai, o pai portanto é agente, ativo. -> Portanto 'do pai' é adjunto adnominal

               O amor de Deus aos homens

	                'de Deus' pratica a ação, ativo recaindo ao paciente do amor 'aos homens'
                	'de Deus' -> Adjunto Adnominal ( agente )
	                'aos Homens' -> Complemento Nominal ( paciente )	

                    O consumo de leite -> o leite é consumido, paciente -> 'de leite' -> Complemento Nominal

	                A confiança em novas atitudes -> 'em novas atitudes' -> paciente -> Complemento Nominal 

                    A mudança de Marina -> 'de Marina' -> ela mudou, agente -> Adjunto adnominal

	                A alteração da emenda -> a emenda é alterada -> paciente -> Complemento Nominal

                    O posicionamento dos radicais -> derivado do verbo posicionar, eles tomaram a atitudes, ativo -> Adjunto adnominal

                    O complemento Nominal se liga aos adjetivos, veja só:

                    Aquele funcionário foi considerado apto ao cargo.

	                'aquele funcionário' -> sujeito ( quem foi considerado? -> aquele funcionario )
	                    Portanto, 'apto ao cargo' -> predicativo do sujeito 
	                    'apto' é um atributo do 'aquele funcionario' -> adjetivo

	                    O complemento nominal se liga a substantivos abstratos, adjetivos e adverbios.
	                        'ao cargo' -> se liga ao adjetivo 'apto', somente pode ser complemento nominal.

                            Eles são justos com os pobres

	                            'justos' -> adjetivo para o sujeito 'eles' <- Predicativo do sujeito
	                            'com os pobres' -> portanto é complemento nominal do adjetivo 'justos'

                Complemento Nominal se liga diretamente a advérbios, veja só:

                A polícia agiu contrariamente a seus princípios 

	            'contrariamente' -> advérbio, expressão preposicionada que se liga a advérbio então ' a seus princípios' é complemento nominal                                

                Ela mora perto de um vulcão

                	'perto' -> advérbio -> expressão preposicionada se conecta ao advérbio, sendo assim: 'de um vulcão' complemento nominal.

Veja mais exemplos:

        Tenho necessidade [yellow]de dinheiro.[reset]

        'necessidade' -> substantivo abstrato derivado do verbo 'necessitar', portanto, 'de dinheiro' é complemento nominal.

        A luta foi prejudicial [yellow]aos jovens[reset]

        'prejudicial' -> substantivo abstrato derivado do verbo 'prejudicar', portanto, 'aos jovens' é complemento nominal.

        É um filme proibido para menores.

        'proibido' -> substantivo abstrato derivado do verbo 'proibir', portanto, 'para menores' é complemento nominal.

        O júri decidiu favoravelmente ao réu

        'favoravelmente' é advérbio, portanto, complementos nominal se conectam diretamente aos advérbios. 'ao réu' é CN.

        O respeito às leis deve prevalecer sempre.

        'respeito' -> substantivo abstrato, derivado do verbo 'respeitar', portanto, 'às leis' é complemento nominal.

        O monitor ficará responsável pela assistência às aulas

        'assistência' -> substantivo abstrato, derivado do verbo 'assistir', portanto, 'às aulas' é complemento nominal.

        A luta contra o mal nunca cessa.

        'a luta' -> substantivo abstrato, derivado do verbo 'lutar', portanto, 'contra o mal' é complemento nominal.
                * lembrando que 'contra' é preposição. *

        G. Bell foi o inventor do telefone.

        'o inventor' -> substantivo abstrato, derivado do verbo inventar, portanto, 'do telefone' é complemento nominal.

        Sempre foi atencioso para com todos

        'atencioso' -> adjetivo para sujeito elíptico, portanto, 'para com todos' é complemento nominal.
        
        Trata-se de filme impróprio para menores.

        'impróprio' -> adjetivo para o filme, portanto, 'para menores' é complemento nominal.

        Permaneceu insaciável de vingança por anos.

        'insaciável' -> adjetivo para sujeito elíptico, portanto, 'de vingança por anos' é complemento nominal.

        Trata-se de conhecimento útil ao bem comum.

        'útil' -> adjeito para o substantivo 'conhecimento, portanto 'ao bem comum' é complemento nominal.


Complemento nominal e objeto indireto não devem ser confundidos entre si. A distinção é feita de maneira relativamente simples:
o complemento nominal, como o nome indica, é termo preposicionado associado a um nome, enquanto o objeto indireto é termo preposicionado que
completa um verbo transitivo indireto.                

        Necessito de ajuda. (VTI / OI)

        quem necessita, necessita de algo: 'de ajuda' / 'necessito' portanto é verbo transitivo indireto e 'de ajuda' é objeto indireto
            
        Tenho necessidade de ajuda. (nome / CN)

        'necessidade' -> substantivo abstrato derivado do verbo 'necessitar', portanto, 'de ajuda' é complemento nominal

        Cremos na força da fé. (VTI / OI)

            quem cre, cre em algo: 'na força da fé', portanto, o verbo cremos é verbo transitivo indireto e 'na força da fé' é objeto indireto

        Nossa crença na força da fé nos torna inabaláveis. (nome / CN)

            'crença' é substantivo abstrato do verbo 'crer', portanto, 'na força da fé' é complemento nominal.

        Seu resultado atendeu às expectativas. (VTI / OI)

        quem atende, atende a algo: 'às expectativas'. Verbo transitivo indireto e 'às expetativas' é objeto indireto
        
        O atendimento às expectativas nos deixou satisfeitos. (nome / CN)

        'o atendimento' é substantivo abstrato do verbo 'atender', portanto, 'às expectativas' é complemento nominal.

        2. Adjunto Adnominal
Adjunto adnominal é o termo acessório que vem junto ao nome (= substantivo concreto), aumentando-lhe a compreensão.

a) Um artigo: As lágrimas corriam copiosamente.
b) Um adjetivo: Trago-lhe flores brancas.
c) Um numeral adjetivo: Dez aves rasgavam o céu.
d) Um pronome adjetivo: Meu palpite é vitória da equipe brasileira.
e) Uma locução ou expressão adjetiva:

Homem sem cabelos (= calvo)
Fé sem limites (= ilimitada)
Aliança de ouro (= áurea)
Brancura de neve (= nívea)
Amor de mãe (= materno)
Mulher de valor
Casa de Saúde
Jornal de ontem
Terra de ninguém
Cidade sem lei
Pista sem acostamento
Fruta da estação

        A única função sintática que expressa a ideia de posse é o adjunto adnominal.

        A resposta do professor agradou o aluno.

        'do professor' -> ele possui a resposta, portanto, adjunto adnominal

        Agora veja:

        A resposta ao professor agradou

        'ao professor' -> paciente da ação, portanto, complemento nominal do substantivo

        A invenção de Santos Dumont

        A invenção dele, ideia de posse, portanto, 'de Santos Dumont' é adjunto adnominal

        A invenção do avião

        O aviação foi inventado, portanto, 'do avião' é paciente da ação, sendo assim, complemento nominal.

        Crítica do artista

        a crítica é do artista, ele tem a posse da crítica, portanto, 'do artista' é adjunto adnominal

        Agora veja:

        Critica ao artista

        o artista recebe a critica, paciente da ação, portanto, 'ao artista' complemento nominal.

Vale lembrar que o adjetivo que exerce a função de adjunto adnominal efetivamente se apresenta junto ao nome que caracteriza.
Por outro lado, o adjetivo que exerce a função de predicativo tende a se apresentar estruturalmente separado do substantivo 
para o qual apresenta o atributo. Tal separação pode ocorrer mediante a presença de verbo ou pontuação.        


    O infeliz animal foi atropelado

        'infeliz' é um adjetivo que qualifica o substantivo 'animal', que por sua vez possui sua função sintática de adjunto adnominal.

    Agora repare a mesma sentença com um verbo:

        Aquele cachorro era infeliz 

        Agora o adjetivo 'infeliz' tem a função sintática de predicativo do sujeito, por ter o verbo de SER , 'era', verbo de ligação.        

    Agora separado por vírgula:

        O cão, infeliz, não tinha lar.

        Por ter a presença do verbo 'TER' e separação por vírgula, 'infeliz' é adjetivo do cão, portanto, predicativo do sujeito.

Veja outra frase que possui verbo:

    Os soldados voltaram feridos da última batalha.

        Verbo 'voltar', intransitivo.
        'feridos' -> adjetivo que qualifica 'os soldados', sujeito da oração que por sua vez possui um verbo, portanto, predicativo do sujeito.

    Agora a mesma sentença, com verbo e sem vírgula, o mesmo adjetivo 'feriados' ao lado do substantivo:

    Os soldados feridos não podem ficar no campo de batalha. (adjunto adnominal)        

    'feridos' -> adjetivo que qualifica o substantivo antes do verbo, sem vírgulas, portanto, Adjunto Adnominal.

        Repare que o Adjunto Adnominal estará colado ao substantivo, que por sua vez, o prediticativo do sujeito estará ao lado do verbo:

        Conheci muitos homens sem cabelos. (adjunto adnominal)

        'sem cabelos' -> adjetivo que qualifica 'homens' -> 'sem cabelos' -> locução adjetiva

        Repare agora, ao lado do verbo, a função sintática muda:

        Os homens estavam sem cabelos. (predicativo do sujeito)

        'sem cabelos' está qualificando o verbo 'ESTAR', intransitivo.  Portanto, é predicativo do sujeito.

        Tínhamos fé sem limites. (adjunto adnominal)

        'sem limites' -> adjetivo que está qualificando ao lado dosubstantivo 'fé', portanto, adjunto adnominal

        Nossa fé era sem limites. (predicativo do sujeito)

        'sem limites' -> adjetivo que está circunstanciando o verbo 'SER', era, portanto, predicativo do sujeito.

        Tomei um café de ontem. (adjunto adnominal)

        'um café'-> substantivo que sendo modificado pela locução adverbial 'de ontem', portanto, adjunto adnominal

        Repare a mesma sentença, com verbo:

        O café parecia de ontem. (predicativo do sujeito)

        'parecer' é verbo de ligação , de estado, serve de ligação. Sendo assim, 'de ontem' é um predicativo do sujeito
            modificando o verbo.

         Por fim: artigos, pronomes, adjetivos e numerais que se apresentem junto a um nome-núcleo funcionarão como
adjuntos adnominais.


Questões 1:

	A poluição [yellow]da água[reset] ocorre devido à alimentação [yellow]do esgoto[reset] não tratado, de produtos químicos e resíduos industriais
e domésticos, uso de fertilizantes na agricultura e uso de mercúrio no garimpo.

	Os termos sublinhados acima desempenham função sintática, de:

a. adjunto adnominal e adjunto adnominal
b. adjunto adnominal e complemento nominal
c. complemento nominal e complemento nominal
d. complemento nominal e adjunto adnominal

substantivo 'poluição' -> substantivo abstrato, a água está sendo poluida, 'da água' é paciente -> complemento nominal
substantivo 'eliminação' -> substantivo abstrato, o esgoto é alimentado, paciente, 'do esgoto' -> complemento nominal

Alternativa 'C'

2. que serve de pretexto para o atentado [yellow]contra biorritmos.[reset]

	O termo sublinhado no perido acima:

a. objeto indireto
b. complemento nominal
c. adjunto adnominal
d. predicativo do objeto

'Que': Pronome relativo que retoma um antecedente na oração anterior. -> Sujeito da oração subordinada adjetiva
Verbo 'serve' Transitivo indireto , quem serve de algo: com complemento indireto, 'de pretexto'
'para o atentado' -> complemento do verbo expressando circunstância de finalidade , adjunto adverbial de finalidade
'o atentado' -> é substantivo do verbo 'atentar', o artigo determinado como um substantivo
'contra biorritmos' -> Complemento nominal do substantivo 'o atentado'

3. No fragmento, 'o segundo grupo são pessoas frequentemente expostas 'a altos níveis de mercúrio', o termo destacado exerce função de:

a. adjunto adnominal
b. Complemento nominal
c. Predicativo do sujeito
d. Predicativo do objeto

'expostas' -> característica do sujeito 'pessoas'	
'a altos níveis de mercúrio' -> Expressão preposicionado ligada ao adjetivo 'expostas', so pode ser complemento nominal.

    Alternativa 'B'

4. No trecho 'a interpretação sexista do masculino genérico', os vocábulos  'a' e 'sexista' classificam-se , sintaticamente, como adjuntos 
adnominais, do termo da 'interpretação  e a expressão  'do masculino genérico' classifica-se como complemento nominal.

CORRETO.

'sexista' -> atributo da interpretação, sendo assim, um adjetivo Sintaticamente, está junto ao nome sem preposição, adjunto adnominal. CORRETO
'do masculino genérico' -> preposição que se liga ao substantivo 'interpretação' derivado do verbo interpretar, substantivo abstrato,
	'a interpretação' é o sujeito ativo, e 'o masculino genérico' é passivo, portanto é complemento nominal.
			'do masculino genérico' está ao lado do adjetivo, portanto complemento nominal.

5. Assinalde a alternativa que indica o número do termo que exerce a função sintática de adjunto adnominal no período a seguir. 
O número relativo ao termo está inserido imediatamente após o termo sublinhado.            

Para quem não está familiarizado, a CID é UM GRANDE MANUAL que elenca OS TIPOS DE DOENÇA e SEUS SINTOMAS para servir de base DE CONSULTA
e padronização de enfermidades - ela é usada em 115 países.

'um grande manual' -> Predicativo do sujeito, característica do sujeito 'a CID'
quem elenca, elenca algo: os tipos de doença, sem preposição, portanto, objeto direto
quem elenca, elenca algo: seus sintomas, sem preposição, portanto, objeto direto
'de base' -> substantivo concreto, portanto, 'de consulta' é adjunto adnominal

Para quem não está familiarizado, a CID é UM GRANDE MANUAL que elenca OS TIPOS DE DOENÇA e SEUS SINTOMAS para servir de base DE CONSULTA
e padronização de enfermidades - ela é usada em 115 países.

6. Agora estamos testemunhando o desaparecimento 'de estrelas'.

	O termo sublinhado no período acima exerce função sintática de:

a. complemento nominal
b. adjunto adnominal
c. objeto indireto 
d. adjunto adnominal
e. agente da passiva

As estrelas estão desaparecendo, elas são as agentes, portanto, Adjunto Adnominal.

7. O uso da palavra está, necessariamente, ligado à questão da eficácia.

	No primeiro período do texto, o termo 'da palavra' complementa o sentido do substantivo 'uso'.

    A palavra está sendo usada, portanto, paciente, complemento do nome 'o uso' -> substantivo abstrato, portanto, complemento nominal.

8. As cartas do missionário Bonifácio conferem testemunho adicional a esse fato.

	No terceiro período do segundo parágrafo, a expressão 'a esse fato' complementa o termo 'adicional.'

    quem confere, confere algo: 'conferem' -> VTD -> conferem: 'testemunho adicional' -> objeto direto
	quem confere, confere a alguém: 'conferem' -> VTI, a quem? 'a esse fato' -> Objeto Indireto
	Sujeito    -> ' As cartas do missionário Bonifácio '

    Portanto, 'a esse fato' complementa o verbo 'conferem' e não o termo 'adicional'

9. Em 'Drummond pôde acompanhar a trajetória 'de uma das maiores contistas da literatura brasileira'
a expressão em destaque funciona como complemento do nome 'trajetória', exercendo, assim, a função de objeto indireto, por iniciar por
preposição.

Questão para confundir o condidato,
quem acompanha, acompanha algo: a trejatória -> objeto direto
'de uma das maiores contistas da literatura brasileira' -> Complemento Nominal do substantivo 'a trajetória'

10. Em 'Os peconheiros do Pará resolveram aquela situação', há quantos adjuntos adnominais?

'os' -> artigo que determina o substantivo' -> Adjunto Adnominal
'do Pará' -> completa o sentido do substantico 'peconheiros' -> Adjunto Adnominal
'aquela' -> Pronome demonstrativo adjetivo que acompanha o substantivo 'situação'      

11. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - MinC - Atividades Técnicas de Suporte - Área Nível Superior - 2024
Assinale a sentença em que o elemento destacado atua como complemento do substantivo a que se refere.

A. A resolução do problema requereu esforços de todos os lados.
B. A invenção do cientista permitiu uma melhoria no sistema.
C. O esforço do candidato contribuiu para sua classificação.
D. O documento aguarda a sanção do governador.
E. Era admirável a superação do atleta na competição.

Alternativa 'A'
Este termo indica o objeto sobre o qual a resolução se aplica, caracterizando uma relação de complemento.

Na alternativa 'B'
O termo 'do cientista' é um adjunto adnominal, pois especifica a quem pertence a invenção, caracterizando uma relação de posse.

Na alternativa 'C'
O termo 'do candidato' é um adjunto adnominal, pois especifica a quem pertence o esforço, caracterizando uma relação de posse.

Na alternativa 'D'

O termo 'do governador' é um adjunto adnominal, pois especifica quem realizará a sanção, caracterizando uma relação de posse.

Na alternativa 'E'
O termo 'do atleta' é um adjunto adnominal, pois especifica a quem pertence a superação, caracterizando uma relação de posse.


12. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Câmara de São Paulo - Técnico Legislativo - Área: Contabilidade - 2024 
Assinale a opção em que o termo sublinhado funciona como adjunto adnominal (preposição nocional) e não complemento nominal (preposição gramatical).

A.O controle [yellow]da natalidade[reset] é algo que não se pode conceber.
B.Progresso é a realização [yellow]de utopias.[reset]
C.O caminho [yellow]do progresso[reset] não é rápido nem fácil.
D.A construção [yellow]do amor[reset] é lenta e prazerosa.
E.A física é a única ciência, o resto é coleção [yellow]de borboletas.[reset]


Todos são preposicionados (então podem ser tanto AA como CN), todos referem-se a substantivos abstratos (ainda podem ser tanto AA como CN),
então o que diferencia é se pratica ou sofre a ação. No caso, o único que pratica a ação é a opção C.

Alternativa 'A' - A natalidade é controlada, 'natalidade' paciente, indicando sobre o que se exerce o controle. -> Complemento Nominal
Alternativa 'B' - Utopias são realizadas, 'utopia' paciente -> Complemento Nominal
Alternativa 'C' - O progresso é o caminho, 'progresso' - ativo da ação,  indicando de que tipo de caminho se trata -> Adjunto Adnominal
Alternativa 'D' - O amor é construido , 'amor' - paciente -> Complemento Nominal
Alternativa 'E' - As borboletas são colecionadas, 'de borboletas' - Paciente -> Complemento Nominal

13. Ano: 2024 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPE TO - Analista Ministerial - Área Letras - 2024


O grande assunto da época era o crescimento populacional: naquela década, a taxa média de natalidade havia ultrapassado a marca de cinco 
filhos por mulher, a maior já registrada.

A expressão “da época” (segundo período do primeiro parágrafo) funciona como complemento nominal de “assunto”.

No caso acima: O grande assunto da época...

Primeiramente vamos analisar:

Tem preposição? Sim, então pode ser A.A ou C.N

Classificação morfológica de assunto: substantivo, então pode ser A.A ou C.N

É substantivo concreto ou abstrato? Para dirimir esta dúvida tentemos responder às seguintes questões:

Assunto é um sentimento? É uma sensação? É uma ação ( substantivo derivado de verbo)? É um estado? Não, então é um substantivo concreto. 
Neste caso estamos diante de um adjunto adnominal.

14. Ano: 2024 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - ALE TO - Procurador Jurídico - 2024

Nas frases a seguir ocorre a presença da preposição DE.

Assinale a frase em que o termo precedido por essa preposição que exerce a função de adjunto e não de complemento.

A. “...quando são tomados pelo desejo DE procriar?”
B. “...pela geração DE filhos”.
C. “...recorrem DE preferência às mulheres”.
D. “...e de uma recordação perene DE si”.
E. “...podem se assegurar da imortalidade e DE uma recordação”.

O conceito central envolve a compreensão de que o adjunto adnominal caracteriza ou qualifica um substantivo,
enquanto o complemento nominal completa o sentido de um nome (substantivo, adjetivo ou advérbio) que não se completa por si só,
necessitando de outro termo para conferir-lhe plenitude de sentido.

Alternativa 'A'
'desejo' -> substantivo abstrato, uma sensação que 'de procriar' completa o sentido ao substantivo indicando a finalidade ou motivo do desejo.
funciona como complemento nominal

Alternativa 'B'

o termo 'de filhos' atua como complemento nominal, especificando o tipo de geração. Ele completa o sentido do substantivo 'geração'

Alternativa 'C'

"de preferência" indica a maneira como algo é feito. Neste caso, "de preferência" é um adjunto adverbial de modo. [bg_green][CORRETA][reset]

Alternativa 'D'

'perene' é adjetivo para o substantivo 'recordação', portanto é complemento nominal.

Alternativa 'E'

 o termo 'de uma recordação' atua como complemento nominal, completando o sentido do verbo 'assegurar

 Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV / Prova: FGV - Prefeitura de São José dos Campos - Professor I - 2023
Assinale a frase em que o elemento sintático sublinhado corresponde a um complemento e não a um adjunto.

A. A ciência é a inteligência [yellow]do mundo.[reset]
B. O problema [yellow]dos especialistas[reset] é que eles pensam sempre nas mesmas coisas.
C. A solidão é o destino [yellow]de todos os homens.[reset]
D. A capacidade [yellow]de viver só[reset] é uma arte a ser conquistada.
E. O sono é a imagem [yellow]da morte.[reset]


Adjunto adnominal

Pode ou não ser preposicionado
Refere-se a substantivos concretos ou abstratos
Sempre é agente


Complemento nominal

É sempre preposicionado
Substantivos abstratos, adjetivos ou advérbios
Sempre é paciente


A) A ciência é a inteligência do mundo.

É preposicionado: preposição de + artigo "o"; ( Pode ser CN ou AA)

É agente: a inteligência é de algo ou alguém. O mundo detêm a inteligência.

Adjunto adnominal


B) O problema dos especialistas é que eles pensam sempre nas mesmas coisas.

É preposicionado; ( Pode ser CN ou AA )

É agente: Os especialistas têm o problema.

Adjunto adnominal


C) A solidão é o destino de todos os homens.

É agente: todos os homens têm um destino

adjunto adnominal


D) A capacidade de viver só é uma arte a ser conquistada.

É paciente: A capacidade recai no complemento viver só, ou seja, você tem a capacidade de viver só.

Complemento nominal ( Gabarito )


E) O sono é a imagem da morte.

Preposicionado;

substantivo abstrato;

é agente: A morte tem essa imagem.

Adjunto Adnominal

Portanto, Letra D, Complemento nominal.

Perceba que a forma mais fácil de identificar a diferença é saber o que é agente "pratica a ação" e o que é paciente " sofre a ação".

15.Ano: 2023 / Banca: Fundação Getúlio Vargas - FGV
Prova: FGV - Prefeitura de São José dos Campos - Guarda Civil Municipal - 2023
Assinale a frase em que o termo sublinhado exerce a função de complemento nominal e não de adjunto adnominal.

A. A necessidade [yellow]de dinheiro[reset] é universal.
B. É falta [yellow]de educação[reset] calar um idiota e crueldade deixá-lo prosseguir.
C. Espírito é o sal [yellow]da conversação[reset], não o alimento.
D. O segredo [yellow]do demagogo[reset] é fazer-se passar por distraído.
E. O objetivo [yellow]da oratória[reset] não é a verdade, mas a persuasão.

Alternativa 'A' -> 'a necessidade' é um substantivo abstrato, é um sentimento.

Dinheiro é necessário, portanto, recai para o substantivo. paciente, complemento nominal.

é um sentimento? É uma sensação? É uma ação ( substantivo derivado de verbo)? É um estado? Não, então é um substantivo concreto.

Complementos nominais referem-se a substantivo concretos.

Alternativa 'B' -> 'de educação' é uma característica do substantivo 'falta'





        
         '''        

    def menu (self):
        self.print_slow('Bem vindo aos estudos da sintaxe para concursos...')
        self.dots()
        while True:
            try:        
                indice = int(input('''
                Estudos da sintaxe:

                [1] - Introdução aos termos da oração: Sujeitos de uma oração
                [2] - Exercicícios de fixação: SUJEITOS de uma oração
                [3] - Predicação Verbal e Nominal + Exercícios
                [4] - Transitividade Verbal
                [5] - Regência Verbal
                [6] - Complemento Nominal X Adjunto Adnominal
                [0] - Sair

                Escolha: '''))

                if indice == 1:
                    self.print_slow_2(self.sujeito())
                if indice == 2:
                    self.print_slow_2(self.exercicios_fixacao_sujeito())     
                if indice == 3:
                    self.print_slow_2(self.predicacao_verbal_nominal()) 
                if indice == 4:
                    self.print_slow_2(self.transitividade_verbal())
                if indice == 5:
                    self.print_slow_2(self.regencia_verbal())    
                if indice == 6:
                    self.print_slow_2(self.cn_aa())                                                                                          
                if indice == 0:
                    self.print_slow_2('Saindo...')                    
                    break
                else:
                    self.print_slow('Escolha inválida. Tente novamente')
            except ValueError:
                self.print_slow('Somente valores inteiros')       

if __name__=='__main__':
     
    sintaxe = Sintaxe()
    sintaxe.menu()
