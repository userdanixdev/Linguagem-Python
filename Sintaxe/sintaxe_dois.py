from colorama import Fore, Style, Back, init
from time import sleep
import sys
import keyboard

class sintaxe_dois_:     
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
                end_index = text.find(']',i + 1 )
                if end_index != -1 and text [i+1:end_index] in color_codes:
                    current_line += text [i:end_index +1]
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
                    rewind_requested = True # Sinaliza para interromper a linha atual
                    sys.stdout.write("\033[F") # Move o cursor para a linha anterior
                    sys.stdout.write("\033[K")  # Limpa a linha
                    sys.stdout.flush()

        def increase_speed():
            nonlocal speed
            speed = max(0.005, speed - 0.01) # 

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
                        sleep (0.1)
                        continue
                    if rewind_requested:
                        break # Interrompe a linha se voltar foi pedido

                    if line[i] == '[':
                            end_index = line.find(']', i + 1)
                            if end_index != -1:
                                color_code = line [i + 1:end_index]
                                if color_code in color_codes:
                                    current_color = color_codes[color_code]
                                    i = end_index + 1
                                    continue
                    sys.stdout.write(current_color + line[i])
                    sys.stdout.flush()
                    sleep(speed)
                    i += 1
            if not rewind_requested:
                current_index += 1 # Só avança se não foi pedido para voltar                    
            

        print(Style.RESET_ALL)
                
        

    def sintaxe_dois(self):
            return ''' 
            [blue]Sintaxe - Lingua Portuguesa:[reset]

[yellow]Período Composto:[reset]

	- [red]Por subordinação[reset] : Oração Principal + oração subordinada - Substantiva / Adjetiva / Adverbial

	- [red]Por coordenação:[reset] : Oração Coordenada Assindética + Oração Coordenada Sindédica

    [red]Síndedo[reset] = com conectivos 
    [red]Assíndedo[reset] = sem conectivos

                [red]REPARE QUE PARA SER PERIODO SIMPLES, A ORAÇÃO DEVE TER SOMENTE UM VERBO.[reset]
		                [red]PARA SER PERÍODO COMPOSTO DEVERÁ TER PELO MENOS 2 VERBOS.[reset]


Exemplo:

	Um jornal de Brasília informou, no início da tarde, o falecimento do papa.

[yellow]quem que informou o falecimento?[reset]  [blue]'um jornal de Brasília'[reset] -> [red]Sujeito[reset]
[yellow]quem informa, informa o que?[reset] [blue]'o falecimento do papa'[reset] -> [red]Objeto direto[reset]

'informou' -> [blue] Verbo transitivo direto[reset]
'no início da tarde' -> [blue] Adjunto Adverbial[reset]

Um jornal de Brasília' -> 'jornal' -> núcleo do sujeito, substantivo concreto
[yellow]'de Brasília' -> Adjunto Adnominal ( acompanha o substantivo concreto ) [reset]

        [red]Período Composto:[reset]

            Um jornal [yellow]que[reset] é de Brasília informou, no início da tarde, o falecimento do ator.


            'é' -> [yellow]verbo de ligação, logo após a conjunção 'que' é outra oração.[reset] [blue]( oração subordinada adjetiva )[reset]
            'de Brasília' => [yellow]Adjunto Adverbial Oracional [reset]-> [blue]Característica do jornal ( Predicativo do sujeito )[reset]
            'informou' -> [yellow]Verbo Transitvo Direto[reset] / 'o falecimento do ator' -> [blue] Objeto direto[reset]

            Na frase "Um jornal que é de Brasília informou, no início da tarde, o falecimento do ator", 
a oração subordinada adjetiva "que é de Brasília" está qualificando o substantivo concreto, sem preposição "um jornal",
funcionando como um adjunto adnominal. Ou seja, ela tem um papel descritivo, adicionando uma informação sobre "um jornal".
Agora, por que não é uma oração subordinada substantiva predicativa? As orações subordinadas substantivas predicativas exercem a função de predicativo do sujeito 
e normalmente aparecem ligadas por verbos de ligação. Elas ocorrem quando a oração inteira atribui uma qualidade ou característica ao sujeito, 
funcionando como parte essencial do predicado.
Se analisarmos apenas a parte "que é de Brasília", vemos que ela não está designando ou definindo o sujeito "um jornal". 
Em vez disso, está apenas complementando uma informação sobre ele. Por isso, é uma oração subordinada adjetiva restritiva, não substantiva predicativa.
Se quiséssemos uma estrutura com uma oração substantiva predicativa, precisaríamos reformular para algo como: "O jornal é o que foi fundado em Brasília."
Aqui, "o que foi fundado em Brasília" exerce a função de predicativo do sujeito "O jornal".


[red]Outro exemplo:[reset]

	Um jornal de Brasília informou, quando entardeceu, o falecimento do ator.

	[yellow]'quando entardeceu'[reset] -> [green]Adjunto Adverbial ou oração subordinada adverbial temporal ( verbo dentro )[reset]

        Apesar de que quem informa, informa algo: 'o falecimento do ator' <- Objeto direto

        Isso acontece porque "o falecimento do ator" não é uma oração, mas sim um simples sintagma nominal.
        Para ser classificada como uma oração subordinada substantiva objetiva direta, precisaria conter um verbo próprio, como em:

                "Um jornal de Brasília informou [yellow]que o ator faleceu."[reset]

            Aqui, "que o ator faleceu" é uma oração subordinada substantiva objetiva direta, pois tem um verbo ("faleceu") e exerce a função de objeto direto do verbo "informou".

[red]Veja esse outro exemplo para ficar mais claro:[reset]

            Um jornal de Brasília informou, no início da tarde, que o ator faleceu.

    [yellow]'que o ator faleceu'[reset] -> Complemento direto ao verbo transitivo direto 'informou' <- [red]Objeto direto oracional [reset]
		[blue]ou oração subordinada substantiva ( núcleo do objeto direto é substantivo 'ator' + verbo 'faleceu' )[reset]
	                                Oração subordinada substantiva objetiva direta


                                    [red]ORAÇÃO SUBORDINADA SUBSTANTIVA:[reset]

Classificam-se:

	[red]1.[reset] Subjetivas -> [blue] Função sintática de sujeito [reset] -> [yellow]Sujeito oracional [reset]
	[red]2.[reset] Predicativas -> [blue] Função sintática de predicativo do sujeito [reset] -> [yellow]Predicativo do sujeito oracional[reset]
	[red]3.[reset] Objetiva Direta -> [blue] Função sintática de objeto direto [reset]-> [yellow]Objeto direto oracional[reset]
	[red]4.[reset] Objetiva Indireta -> [blue] Função sintática de objeto indireto [reset] -> [yellow]Objeto indireto oracional[reset]
	[red]5.[reset] Completiva Nominal -> [blue] Função sintática de complemento nominal [reset]->[yellow] Complemento nominal oracional[reset]
	[red]6.[reset] Apositiva -> [blue] Função sintática de aposto [reset] -> [yellow] Aposto oracional[reset]


    [red]LEMBRE-SE : As funções sintáticas serão desempenhadas por verbos. [reset]

    Por período composto de subordinação, algumas orações são desenvolvidas e reduzidas.

As orações subordinadas substantivas desenvolvidas teremos verbos conjugados, sem formas nominais e com presença de conjunções integrantes 'QUE' e 'SE'

As conjunções não possuem função sintática.

As conjunções integrantes ligam a oração principal a oração subordinada sem valor semântico.

TESTE: substituir a oração subordinada provável e colocar ISSO.

Exemplo:

	                [yellow]É necessário que o governo adote medidas emergencias.[reset]


    A oração possui dois verbos, portanto, período composto. 'é' -> verbo de ligação // 'adote' -> verbo no presente

[bg_red]A oração subordinada substantiva é introduzida pela conjunção integrante 'que' ou 'se', sempre.![reset]

    [bg_yellow]LEMBRE-SE, A ORAÇÃO SUBORDINADA SUBSTANTIVA É SEMPRE INTRODUZIADA PELAS CONJUNÇÕES INTEGRANTES 'QUE' E 'SE'.[reset]
    
    '...[yellow]que[reset] o governo adote medidas emergenciais.' <- [red]Oração subordinada substantiva[reset]

    TESTE: É necessário [yellow]ISSO[reset] <- isso o que? '..que o governo adote...'

    	[blue]Depois do teste e a conjunção, podemos considerar que é uma oração subordinada substantiva.[reset]

			'que' -> conjunção integrante
			'é necessário ISSO' -> ISSO é necessário <- [yellow]'isso' <- Sujeito[reset] // 'é' -> verbo de ligação que liga o sujeito a sua 
				característica : 'necessário' -> Predicativo do sujeito

			[red]Portanto, é uma oração subordinada substantiva subjetiva.[reset] 
            
                [red]1.[reset] ( subjetiva por que possui função sintática de sujeito )
                [red]2.[reset] ( substantiva por que possui conjunção integrante )
                [red]3.[reset] ( subordinada por que possui mais de um verbo na oração + conjunção integrante )


[red]Outro exemplo:[reset]

                            	É sabido que o Brasil é o país do futuro.


    [red]locução verbal[reset]: 'é sabido' -> [yellow]verbo de ligação[reset] + [yellow]verbo nominal[reset] // [red]'que'[reset] -> conjunção integrante

    é sabido o que? é sabido [yellow]ISSO[reset] <- [green]Oração subordinada substantiva[reset]

    ( subjetiva por que possui uma característica do sujeito, é sabido o que? '...que o Brasil é o país do futuro.' )

[red] Outro exemplo:[reset]

                        Consta nos documentos que você não declarou o Imposto de Renda.

	'consta' -> [red]verbo[reset] // 'declarou' -> [red]verbo[reset] -> [blue]Período Composto[reset]

        [yellow]Consta nos documentos[reset] -> Oração Principal // 'que' -> conjunção integrante 
                            [blue]'que você não declarou o Imposto de Renda'[reset] <- Oração Subordinada

	    [yellow]'consta'[reset] -> verbo intransitivo, não há complementos // [red]'nos documentos'[reset] -> Adjunto Adverbial de lugar
                    [green]Predicado verbal para a primeira oração , núcleo do predicado é o verbo 'consta'.[reset]
        
        o que consta nos documentos? consta nos documentos ISSO. <- [red]SUJEITO[reset] // [yellow]ISSO[reset] consta nos documentos
		                        [green]Portanto, oração subordinada substantiva subjetiva. ( função sintática de sujeito oracional )[reset]

                 [yellow]Sujeito da oração subordinada[reset]: você //  'declarou' -> [red]verbo transitivo direto[reset]. Quem declara, declara algo:
            [yellow]'o Imposto de Renda'[reset] -> Objeto direto complementar do verbo 'declarar', portanto predicado verbal.

[red]Outro exemplo:[reset]

                                    É necessário que o governo adote medidas emergenciais.

    [yellow]'é necessário'[reset] -> Oração principal // [yellow]'isso'[reset] -> [red]Sujeito[reset] // 'é' -> [red]verbo de ligação[reset] 
                            [yellow]'necessário'[reset] -> [green]predicativo do sujeito[reset] [yellow]( ISSO É NECESSÁRIO )[reset]

        'que o governo...' -> Oração subordinada substantiva ( devido a conjunção integrante 'que' )  
                                    subjetiva ( por ser uma característica do sujeito ISSO )

                        Análise sintática da oração subordinada:

                    [red]Atenção![reset] 'o governo' -> [green]sujeito[reset] -> núcleo do sujeito: 'governo' // 'adote' ->  Verbo transitivo direto
                            Objeto Direto -> 'medidas emergenciais' // Predicado verbal ( possui verbo transitivo e complemento )


Preste atenção nesse exemplo:

                                O ideal é que o governo adote medidas emergenciais.

	[yellow]O ideal é ISSO[reset] <- Oração subordinada substantiva <- [green]'que o governo adote medidas emergencias'[reset]

    'O ideal' -> [red]Sujeito[reset] // 'ideal' -> Núcleo do sujeito SUBSTANTIVO / [red]	NÃO É CARACTERÍSTICA, E SIM O PRÓPRIO SUJEITO -> 'IDEAL'[reset]


    O QUE É ISSO? 'ideial' <- Sujeito ( atente-se que o artigo 'o' antes do substantivo determina o sujeito ) e 'ISSO' é um predicativo do sujeito e não o sujeito,
                         Portanto a oração é subordinada substantiva predicativa
		em que 'o ideal' é o sujeito //  'é' -> verbo de ligação // 'ISSO' -> Característica do sujeito


[red]Outro exemplo:[reset]

	                            É legal que nós estudemos mais.

        'É legal' -> [blue]Oração principal[reset] // 'que' -> [blue]conjunção integrante[reset] // 'que nós estudemos mais' -> [blue]oração subordinada[reset]                                    

    'É' -> [blue]Verbo de ligação[reset] //  'estudemos' -> 'que nós estudemos' -> [blue]Presente do subjuntivo ( 2 verbos = oração subordinada )[reset]

	É legal o que? [blue]ISSO[reset] <- 'que nós estudemos mais' <- [red]Oração subordinada substantiva[reset] [blue]( conjunção integrante 'que' )[reset]

    'legal' -> [blue]adjetivo que possui função sintática de predicativo do sujeito, caracterizando o sujeito[reset] -> [red]'que nós estudemos mais'[reset]

                            [green]Portanto temos uma oração subordinada substantiva subjetiva.[reset]

            Predicado da oração principal: [blue]nominal[reset] // Predicado da subordinada: [blue]verbal[reset]                            
	

[red]    Outro exemplo:[reset]
    
                                O legal é que você não dirija bêbado.

    O legal é o que? O legal é [yellow]ISSO[reset] <- [green]'que você não dirija bêbado'[reset] <- [red]Oração subordinada substantiva[reset]

        Repare nesse exemplo que o artigo define o substantivo em questão, portanto, [red]'O legal' já o sujeito.[reset]
            O legal é ISSO o que? [yellow]'que você não dirija bêbado'[reset] -> característica atribuida ao sujeito 
                                                    [yellow]'é'[reset] -> verbo de ligação

                        Portanto, esse exemplo é uma oração subordinada substantiva predicativa.

            Por que:
            
                 'o legal' é o sujeito // 'é' -> verbo de ligação // 'que vc não dirija bêbado' -> característica do sujeito

                                    Predicado nominal ( verbo de ligação + predicativo do sujeito )


            São 6 tipos de orações subordinadas substantivas.

Mais exemplos:

            Os docentes entendem que os pais devem ser convocados.

            'entendem' -> Verbo // 'devem ser convocados' -> locução verbal ( 4 verbos = Período composto )

            Os Docentes entendem ISSO? <- Oração subordinada substantiva // Portanto o 'que' é conjunção integrante.
		        Ela não pode ser subjetiva, pois já temos o sujeito => 'os docentes'

                'entendem' o que? 'os pais devem ser convocados' -> Objeto Direto

	            Portanto devemos classificar essa oração como oração subordinada substantiva objetiva direta

                Predicado verbal ( núcleo -> verbo 'entendem' ) -> Oração Principal

                2º oração -> 'que os pais devem ser convocados' -> Sujeito 'os pais' // verbo: 'devem ser convocados' -> voz passiva analítica

                        Predicado verbal -> núcleo do predicado -> 'devem ser convocados'


Outro exemplo:

                Não sabemos se o parto será hoje.

                [yellow]'Não sabemos'[reset] : [red]oração principal [reset]
                
                [yellow]'saber'[reset] -> verbo // [yellow]'será'[reset] -> verbo // [yellow]'se'[reset] <- conjunção integrante // [yellow]'não'[reset] -> [blue]adjunto adverbial de negação[reset]

                quem é que não sabe? [yellow]'nós'[reset] -> sujeito elíptico,oculto ou desinencial // não sabemos [yellow]ISSO[reset] <- oração subordinada substantiva

                quem sabe, sabe algo: [yellow]ISSO[reset] -> 'se o parto será hoje' <- Objeto direto //[yellow] Predicado verbal[reset]

                                Portanto, trata-se de uma oração subordinada substantiva objetiva direta.


Mais exemplos:
                
                                        Preciso de que você trabalhe com seriedade.

                [yellow]'Preciso de '[reset] -> verbo[blue] ( Oração principal )[reset] / [red]Verbo transitivo direto[reset] -> Sujeito oculto 'eu' <- [green]1° pessoa do discurso[reset]
                
                [yellow]'trabalhe'[reset] -> [red]verbo ( período composto por subordinação )[reset] -> Predicado da oração principal: [red]VERBAL[reset]

                quem precisa, precisa de algo: [yellow]'de que vc trabalhe...'[reset] <- [blue]objeto indireto[reset]

                Preciso DISSO, DISSO O QUE? [yellow]'de que você trabalhe com seriedade.'[reset] ( preposição 'de' + conjunção integrante 'que' )

                [blue]Sujeito da oração subordinada:[reset] [yellow]'você'[reset] // [yellow]'trabalhe'[reset] -> [red]verbo intransitivo[reset]

                [yellow]'com seriedade'[reset] -> Adjunto Adverbial de modo // Predicado VERBAL

                            Portanto, temos uma oração subordinada substantiva objetiva indireta.

                                        
Outro exemplo:

                                        Meus pais estavam certos de que eu venceria.

                [yellow]'meus pais estavam certos'[reset] -> [blue]Oração Principal[reset]

                [red]'estavam'[reset] -> verbo de ligação // [red]'venceria'[reset] -> verbo // [blue]período composto por subordinação[reset]

                [red]'meus pais'[reset] -> sujeito simples  // [red]'certos' -> adjetivo dos pais, função sintática de predicativo do sujeito.

                [red]Predicado nominal [reset] [blue]( verbo de ligação + predicativo sujeito )[reset]

                Meus pais estavam certos [red]DISSO[reset] <- Oração subordinada substantiva.

                [red]Oração subordinada: [reset]

                [red]'certos de que eu venceria'[reset] -> 'de que eu venceria' -> completa o adjetivo do sujeito. Portanto é complemento nominal.

                    Sujeito: [red]'eu'[reset] // [red]'venceria'[reset] -> verbo transitivo direto sem complemento

                        [red]Predicado verbal.[reset]


                        Lembrando que o complemento nominal não somente completa substantivos, mas também adjetivos e advérbios.

                        Sendo assim, é uma oração subordinada completiva nominal.

                        [red]ATENÇÃO![reset]

                        Lembre-se: se a oração subordinada tiver preposição pode ser completiva nominal ou objetiva indireta.

			Se na oração subordinada tiver preposição acompanhada do verbo: Objetiva indireta
			Se na oração subordinada tiver preposição acompanhada de um substantivo, adjetivo ou advérbio: Completiva Nominal


Agora sem preposição das frases acima:

	Preciso que você estude

	Temos confiança que esse caminho é o melhor.


	Alguns autores dizem que é uso obrigatório da preposição.
	Celso Cunha diz que é facultativa nas completivas nominais e obrigatório nas objetivas diretas.

	Para Ivanildo Bechara optativa em ambos os casos.

		Conjunção já é elemento de conectar e preposição serve para ligar orações também. Recomendado somente usar um conectivo.

	IADES intende que é obrigatória o uso da preposição.
	CESPE não tem definição.


                                    Temos confiança que esse caminho é o melhor.

    [blue]Oração principal:[reset] 'temos confiança' // [blue]oração subordinada:[reset] 'de que esse caminho é o melhor.

        [blue]Sujeito da oração principal[reset]: [red]Oculto 'nós'[reset] // [blue]quem tem, tem algo:[reset] 'confiança' <- [red]Objeto Direto[reset]
            [red]'temos'[reset] -> verbo transitivo direto //[blue] Predicado da 1º oração principal:[reset] [red]VERBAL[reset]

            Para completar o sentido do substantivo 'confiança' -> [red]Complemento Nominal[reset]

            [blue]Sujeito da oração subordinada:[reset] [red]'esse caminho'[reset] // [blue]núcleo [reset]:'caminho' //[blue] Verbo de ligação[reset]: 'é' 
            [blue]Predicativo do sujeito[reset]: [red]'o melhor'[reset] <- [green]Qualificando o substantivo 'caminho'[reset]
                    [red]Portanto o predicado é nominal[reset] [blue]( verbo de ligação + predicativo do sujeito )[reset]

	Temos confiança NISSO. quem confia, confia em algo: 'que esse caminho é o melhor' <- oração subordinada substantiva completiva nominal
		                                tal qual que 'confiança' é um substantivo abstrato. 


Exemplos:

                    Eu tenho um desejo: que o dia termine bem.

	Pontuação pode ser 'vírgula', travessão, dois pontos.

	Eu tenho um desejo: [yellow]ISSO.[reset]

		[green]A frase possui duas orações, unidas por dois-pontos, sem conjunção explícita.[reset]

        [blue]Oração Principal[reset]: 'Eu tenho um desejo'

        [blue]'eu'[reset] -> [red]Sujeito[reset] // [red]verbo[reset]: 'tenho' ( verbo transitivo direto ) -> quem tem, tem algo: [blue]'desejo'[reset] <- [red]Objeto Direto[reset]

        [red]    Predicado VERBAL[reset]

        [red]Oração subordinada[reset]: 'que o dia termine bem'

        [red]sujeito:[reset] 'o dia' // [red]verbo intransitivo[reset] : 'termine' // 'bem' -> [red]Adjunto Adverbial de modo[reset] //
        
            [red] Predicado verbal            [reset]

	A função sintática do aposto: equivalência semântica, igualdade de sentido presente.

	ele tem um desejo, que o dia termine bem. Deverá ter igualdade de sentido. 
	
		Portanto, a oração subordinada substantiva apositiva.

'''
    def exercicios (self):

        return ''' Exercícios de fixação:

	1. A fotografia mostra que estamos muito bem no atacado, acima da média mundial em alguns recortes.

    A oração subordinada apresenta função sintática de:

    a. Adjunto Adnominal do substantivo 'fotografia'
    b. Adjunto Adverbial do verbo 'estamos'
    c. Aposto que explica os adjuntos adverbiais 'muito' e 'bem'
    d. Complemento da forma verbal 'mostra'.

    A fotografia mostra ISSO, ISSO o que? <- [red]'que estamos muito bem...'[reset] <- [blue]oração subordinada substantiva[reset] //
         'que' -> conjunção integrante

Na alternativa 'a'.

            Para que a oração tenha a função de adjunto adnominal é a oração subordinada substantiva adjetiva depois da conjunção integrante.
			Além disso, [yellow]'A fotografia mostra...'[reset] é a oração principal e não a subordinada.
            A subordinada é depois da conjunção integrante.
			Além disso, o sujeito é identificável na oração. E não há nenhum complemento para o sujeito.
			Há uma transitividade do verbo 'mostrar' e seu complemento, que seria a oração subordinada substantiva objetiva direta

Na alternatica 'b'. As orações substantivas não desempenham função de adjunto adverbial, nem de advérbios.

Na alternativa 'c' aposto deve vim com pontuação, e não há pontuação nenhuma na frase. ERRADA

Na alternativa 'd' -> 'a fotografia' -> sujeito. Quem mostra, mostra algo: mostra ISSO.
				        Oração subordinada substantiva objetiva direta.

		[red]'mostra'[reset] -> [blue]Verbo transitivo direto[reset] // [blue]objeto direto[reset]: [red]'que estamos muito bem...'[reset]

					            Alternativa 'D' -> Gabarito

[red]Questão 02.[reset]

	No período 'É pouco provável [yellow]que[reset] o surto da Guiné Equatorial se torne uma pandemia tão disseminada quanto a da Covid-19.'
    
     A oração em destaque é:

a. Subordinada substantiva predicativa.
b. Subordinada adjetiva restritiva.
c. Subordinada substantiva subjetiva.
d. Subordinada adverbial comparativa.                    

        É utilizado uma conjunção integrante para separar a oração principal da subordinada ( que )
                Sendo assim, é uma oração subordinada substantiva. Eliminando os itens 'b' e 'd'.

                É pouco provável [yellow]ISSO[reset] -> [yellow]ISSO[reset] o que? [red]'que o surto da Guiné...'[reset] <- [green]Oração subordinada substantiva (possui conjunção integrante)[reset]

                Não há sujeito explícito, [yellow]ISSO[reset] portanto passa a ser o sujeito da oração.
                    Sendo assim: [yellow]ISSO[reset] é pouco provável. 
                    Assim: [yellow]'é'[reset] -> [blue]verbo de ligação[reset] // [yellow]'pouco provável'[reset] -> [green]característica atribuida ao sujeito[reset]
                        [red]'pouco provável'[reset] -> [yellow]Predicativo do sujeito[reset]
                                        Portanto, é uma oração subordinada substantiva subjetiva.


                    DETALHE:
            [red]Se o artigo que determina o substantivo estivesse na oração, seria uma oração subordinada substantiva predicativa.[reset]

[red]Questão 03.[reset]

No fragmento textual: 

'O voluntário viu uma sequência de letras exibidas em uma tela e tinha de dizer [yellow]se[reset] cada uma era vogal ou consoante,
 maiúscula ou minúscula e [yellow]se[reset] estava na cor verde ou vermelha'.

As duas orações subordinadas introduzidas pela conjunção SE classificam-se , respectivamente, como:

a. Substantiva Objetiva Direta - Adverbial Condicional
b. Substantiva Objetiva Direta - Substantiva Objetiva Direta
c. Adverbial Condicional - Adverbial Condicional
d. Substantiva Subjetiva - Adverbial Modal
e. Adverbial Modal - Adverbial Modal

[yellow]Lembre-se de substituir a conjunção integrante 'SE' ou 'QUE' por ISSO, DISSO para identificar se a oração é substantiva.[reset]

[green]'... e tinha de dizer se...'[reset] ->> [blue]'...e tinha de dizer[reset] ISSO <- Oração subordinada substantiva 

    [blue]quem diz, diz algo[reset]: diz [yellow]'se cada um era vogal ou consoante...'[reset] <- [red]Objeto Direto[reset]
        

No outro [red]'SE'[reset] -> [yellow]'...e se estava na cor...'[reset] -> ...e [red]ISSO[reset]' -> [red]ISSO[reset] o que?
                         [yellow]'...e se estava na cor...'[reset] <- oração subordinada substantiva

        [blue]quem diz, diz algo[reset]: diz [yellow]'e se estava na cor verde...'[reset] <- Objeto Direto

            Portanto, as duas partículas 'SE' são conjunções integrantes e fazem parte da oração subordinada objetiva direta.
                                Ambos são complementos do verbo transitivo direto 'DIZER'.

[red]Questão 04.[reset]

' O levantamento do Datafolha [yellow]revela[reset] que, entre os desempregados, 38% [yellow]disseram[reset] que não tiveram comida suficiente.'

No período composto transcrito do texto, os verbos destacados são:

a. complementados por orações que funcionam como objeto direto
b. complementados por orações que funcionam como objeto indireto
c. intransitivos e, portanto, não pedem complemento verbal.
d. seguidos de orações que funcionam como predicativos

[red]Análise:[reset]

[yellow]'O levantamento'[reset] -> Sujeito, substantivo // [yellow]'do Datafolha'[reset] -> Adjunto Adnominal // [blue]quem revela, revela algo[reset]: revela [yellow]ISSO ( subordinada substantiva )[reset]
        [blue]quem revela, revela que[reset]: [yellow]38% disseram que não tiveram comida suficiente[reset] <- [red]Objeto direto complementar do verbo transitivo direto revelar.[reset]
                Portanto o primeiro verbo destacado 'revela' funciona como objeto direto.

                [red]quem que disseram?[reset] [yellow]'38%'[reset] <- Sujeito // [red]quem diz, diz algo[reset]: [yellow]'que não tiveram comida suficiente'[reset] <- Objeto Direto

                        Portanto, o segundo verbo também é uma oração subordinada substantiva objetiva direta.

[red]Na alternativa 'b'[reset]: não apresentam preposições para serem como objetos indiretos.
[red]Na alternativa 'c'[reset]: os verbos não são intransitivos e sim transitivos diretos com seus complementos.
[red]Na alternativa 'd'[reset]: funcionam como objetos diretos, não há verbos de ligação.

[red]Questão 05.[reset]

Marque a alternativa, onde há uma oração subordinada substantiva completiva nominal:

a. Todos os jogadores discordaram de que o time havia jogado mal.
b. Ele não tem muita certeza de que sua namorada lhe seja fiel.
c. A exigência dos torcedores era a contratação de um novo técnico
d. Foi muito importante a sua participação na reunião.


[red]Análise do item A: [reset]

        Todos os jogadores discordaram de que o time havia jogado mal.

        [red]Verbos[reset]: 'discordaram' // 'havia' ->[red] Período composto [reset]

        Todos os jogadores discordaram [yellow]DISSO, DISSO[reset] o que? [green]'de que o time havia...' ( subordinada substantiva )[reset]
        Já o pronome "todos" tem uma função diferente: ele atua como adjunto adnominal, 
        adicionando uma ideia de totalidade ao núcleo do sujeito ("jogadores"). 
        Em outras palavras, ele reforça que não estamos falando de alguns jogadores, mas de todos eles.


        [red]quem discorda, discorda de algo[reset]: [yellow]'de que o time havia jogado mal'[reset] <-[blue] Objeto Indireto ( preposição 'de' do verbo transitivo direto )[reset]

                Portanto o item A é uma oração subordinada substantiva objetiva indireta.

[red]Análise do item B:[reset]

            Ele não tem muita certeza de que sua namorada lhe seja fiel.

            [red]'tem' / 'seja'[reset] -> Período composto ( 2 verbos )

            Ele não tem muita certeza [yellow]DISSO, DISSO[reset] o que? [yellow]'de que sua namorada lhe seja fiel'[reset] <- [blue]Oração subordinada substantiva[reset]

            [blue]'ele'[reset] -> sujeito simples // quem tem, tem o que: [red]'muita certeza'[reset] <- Objeto Direto
                    
                    [bg_green]Predicativo do sujeito é somente para verbos antecedidos de ligação. ( SER, ESTAR, PARECER )[reset] <- Atenção!

            [blue]'certeza'[reset] -> substantivo que na frase possui complemento nominal. certeza de que? [green]'certeza de que sua namorada lhe seja fiel'[reset]

                    Portanto, a oração é subordinada substantiva completiva nominal. GABARITO LETRA B        

[red]Análise do item C:[reset]

            A exigência dos torcedores era a contratação de um novo técnico.

            Na expressão [yellow]"A exigência dos torcedores"[reset], o termo [yellow]"dos torcedores"[reset] funciona como um adjunto adnominal do substantivo "exigência".
Isso acontece porque "dos torcedores" indica quem faz a exigência, ou seja, especifica a origem da exigência e qualifica o substantivo sem alterar seu significado essencial.

            [blue]'era'[reset] -> [red] verbo de ligação [reset] // Somente um verbo -> Período Simples, não há subordinação na oração.

                [blue]'a contratação de um novo técnico'[reset] -> [red]Predicativo do sujeito[reset]

                A estrutura após o verbo "era" forma um predicado nominal.
Isso acontece porque temos o verbo de ligação "era", que não indica uma ação, mas sim um estado ou identidade.

[red]Análise do item D:[reset]

                    Foi muito importante a sua participação na reunião.

                    Somente 1 verbo na frase, 'foi', não possui oração subordinada.

                    [red]'foi'[reset] -> verbo de ligação // [red]'muito importante'[reset] -> [blue]Predicativo do sujeito [reset]
                    [red]'a sua participação na reunião'[reset] -> [blue]Sujeito [reset]// - Determinado pelo pronome possessivo "sua"
                    [red]'na reunião'[reset] -> [blue]Complemento Nominal[reset]

                    [green]Como há um verbo de ligação e um predicativo do sujeito, o predicado é nominal.[reset]

[red]Questão 06.[reset]

Classifique, sintaticamente, a oração sublinhada: 
'Mas os garotinhos também colheram muitas e fugiram das mães voltando à taba e pedindo à avó [yellow]que lhes fizesse um bolo de milho.'[reset]

a. Oração subordinada substantiva apositiva
b. Oração subordinada substantiva objetiva indireta
c. Oração subordinada substantiva objeto direta
d. Oração subordinada substantiva completiva nominal

[yellow]'os garotinhos' -> sujeito simples // [yellow]'eles' fugiram -> sujeito elíptico / e pedindo ->[yellow] 'eles' -> [blue]sujeito elíptico[reset]
    [yellow]'... e pedindo à avó [reset][red]ISSO, ISSO[reset] o que? [red]'que lhes fizesse um bolo...'[reset] <-[yellow] oração subordinada substantiva[reset]
    quem pedi, pedi a alguém:[red] à avó[reset] <-[green] Objeto Indireto ( preposição )[reset]
    quem pedi, pedi algo: [red]'que lhes fizesse um bolo de milho'[reset] -> [green]Objeto direto [reset]

        Alternatica C , a correta.[blue] Oração subordinada substantiva objetiva direta.[reset]

Na oração principal temos:

    'Os garotinhos também colheram muitas e fugiram das mães..'

        'colheram' -> Verbo Transitivo Direto // 'fugiram' -> Verbo Intranstivo -> Complementos: colheram o que? 'muitas' <- Objeto Direto
                'das mães' ->  Complemento e adjunto adverbial do verbo intransitivo 'fugiram'.

                    Não há verbo de ligação e nem predicativo do sujeito, portanto o predicado é VERBAL.


                    Lembrando:

        Verbo transitivo: precisa de complemento verbal (objeto direto ou indireto) para completar seu sentido.

        Verbo intransitivo: já tem sentido completo sem objeto, mas pode ser ampliado com adjuntos adverbiais (lugar, tempo, modo, causa etc.).
        Um adjunto adverbial não é objeto. Ele não é exigido pelo verbo, e sim opcional e circunstancial, embora muitas vezes relevante.
                  
[red]Questão 07.[reset] Assinale a alternativa em que ocorre uma oração subordinada substantiva objetiva direta.

a. O meteorologista informou que hoje faria frio
b. É necessário que tenhas foco para alcançares a vitória
c. Necessito de que me ajudes a superar essa perda.
d. É bom que você venha buscar seu carro ainda hoje.


[red]Análise do item A:[reset]

            O meteorologista informou que hoje faria frio.

        [red]'informou' // 'faria'[reset] -> Verbos ->[blue] Período composto por subordinação[reset]

        [red]'o meteorologista'[reset] -> Sujeito Simples // O meteorologista informou [yellow]ISSO[reset], [red]ISSO[reset] o que? ( Oração subordinada substantiva, conjunção integrante )
        [red]quem informa, informa algo:[reset] 'que hoje faria frio' -> Objeto Direto

                Gabarito da questão alternativa 'A'.

O verbo "informou" é um verbo significativo, ou seja, indica uma ação realizada pelo sujeito ("O meteorologista"). 
Como o núcleo do predicado é esse verbo de ação e não há um predicativo atribuindo característica ao sujeito,
classificamos essa estrutura como predicado verbal.


[red]Análise do item B:                [reset]

            É necessário que tenhas foco para alcançares a vitória.

                [blue]'é'[reset] -> [red]verbo de ligação[reset] // [red]'tenhas'[reset] -> verbo no imperativo // Período composto por subordinação

                é necessário [yellow]ISSO[reset], [yellow]ISSO[reset] o que? [green]'que tenhas foco...'[reset] <- Oração subordinada substantiva.

                [yellow]ISSO[reset] é necessário -> [red]Sujeito [reset]-> ISSO // [blue]'é'[reset] ->[red] verbo de ligação[reset] 
                [blue] 'necessário'[reset] ->[green] Predicativo do sujeito[reset]

                    O predicado é nominal. Por que possui 1 verbo de ligação e um predicativo do sujeito.
                    Portanto não é alternativa que a questão pedi.                

O verbo "é" funciona como um verbo de ligação, conectando o sujeito "que tenhas foco para alcançares a vitória" ao seu predicativo "necessário".
                [red]Portanto, temos um predicado nominal.[reset]

[red]Análise do item C:[reset]

            Necessito de que me ajudes a superar essa perda.

            [red]Sujeito elíptico, oculto ou desinencial.[reset]

            necessito [yellow]DISSO[reset] -> Oração subordinada substantiva

            quem necessita, necessita de algo: [red]'de que me ajudes...'[reset] <- Objeto Indireto para o verbo transitivo direto.

                Portanto a oração é subordinada substantiva objetiva indireta.

O verbo "necessito" é um verbo significativo (de ação), e seu complemento é a oração "de que me ajudes a superar essa perda", funcionando como objeto indireto. 
Como o núcleo do predicado é um verbo de ação e não há um predicativo atribuindo característica ao sujeito,
classificamos essa estrutura como predicado verbal.

[red]Análise do item D:[reset]


            É bom que você venha buscar seu carro ainda hoje.

            é bom [yellow]ISSO[reset], [yellow]ISSO[reset] o que? [blue]'que você venha buscar...'[reset] -> oração subordinada substantiva  ( conjunção integrante )

            [yellow]ISSO[reset] é bom.  [yellow]ISSO[reset] o que? 
            
            [red]Sujeito[reset] -> [blue]'que você venha buscar seu carro ainda hoje'[reset] //  [blue]'é'[reset] -> [red]verbo de ligação[reset] 
            
                [red]'bom'[reset] -> [yellow]Predicativo do sujeito  [reset]

            [bg_green]Portanto, a oração é subordinada substantiva subjetiva.[reset]

[red]Atenção! Se o artigo que determina o substantivo estivesse na oração, seria uma oração subordinada substantiva predicativa.[reset]

        O predicado é nominal. Não possui um verbo transitivo e sim predicativo do sujeito + verbo de ligação.

        O verbo "é" funciona como um verbo de ligação, conectando o sujeito "que você venha buscar seu carro ainda hoje" ao seu predicativo do sujeito, que é "bom".
    Esse predicativo indica uma característica atribuída à oração subordinada, que funciona como sujeito da oração principal.
Além disso, a oração "que você venha buscar seu carro ainda hoje" é uma oração subordinada substantiva subjetiva, pois exerce a função de sujeito para o verbo "é".


[red]Questão 8.[reset]

	Parece [yellow]que esquecemos as faculdades do pensamento e da imaginação.[reset]

A oração subordinada substantiva sublinhada é classificada como:

a. subjetiva
b. predicativa
c. objetiva direta
d. completiva nominal

    Parece [yellow]ISSO[reset] <- oração subordinada substantiva // [red]'parece'[reset] -> [blue]verbo de estado, de ligação. Não é verbo de ação.[reset]
	[yellow]ISSO[reset] parece,[yellow] ISSO[reset] é o sujeito da oração. -> Que esquecemos as faculdades do pensamento e da imaginação" exerce a função de sujeito

Portanto é uma oração subordinada substantiva subjetiva.

    O verbo "parece" funciona como um verbo de ligação, pois indica um estado ou aparência. 
No entanto, o verbo "esquecemos" é um verbo significativo (de ação) e tem um objeto direto, que é "as faculdades do pensamento e da imaginação".
Como há um verbo significativo indicando ação ("esquecemos") e um termo que caracteriza o sujeito ("parece"), 
                            Essa estrutura é classificada como predicado verbo-nominal.

A oração principal não possui sujeito.
[green]Não atua como verbo de ligação, mas sim como verbo impessoal e intransitivo.[reset]
Ele não liga sujeito a uma qualidade, e sim introduz uma oração subordinada substantiva subjetiva que funciona como sujeito oracional.

[red]Ele pode atuar como verbo de ligação, mas somente quando ligar o sujeito ( se existir ) a uma característica.[reset]

Verbo de ligação (quando liga o sujeito a uma característica):
🔸 Exemplo:

"Ele parece cansado."

[yellow]"cansado"[reset] = [blue]predicativo do sujeito[reset]

[yellow]"parece"[reset] = [blue]verbo de ligação[reset]


[red]Questão 09.[reset] 

Leia: 'Minha esperança é [yellow]que um dia descubram...'[reset], a oração sublinhada é:

a. Oração Subordinada substantiva apositiva
b. oração subordinada substantiva objetiva indireta
c. oração subordinada substantiva objetiva direta
d. oração subordinada substantiva predicativa

[yellow]'minha esperança'[reset] -> Sujeito ( 'minha' -> Pronome possessivo determinante, 'esperança' -> Substantivo ) 
    [yellow]'é'[reset] -> [red]Verbo de ligação[reset]

    Minha esperança é [yellow]ISSO[reset], [yellow]ISSO[reset] o que? [green]'que um dia descubram...'[reset] -> Predicativo do sujeito

        Sendo assim, a oração é subordinada substantiva predicativa.
        Também possui um predicado nominal. ( verbo de ligação + predicativo do sujeito )

[red]Questão 10.[reset]

A diferença é que aqui o tráfico controla territórios com armamento de guerra.

No trecho ' A diferença é que o tráfico controla territórios com armamento de guerra', a oração introduzida por 'que' 
complementa o sentido do nome 'diferença'.        

[yellow]'A diferença'[reset] -> substantivo e sujeito // [yellow]'é'[reset] -> verbo de ligação // [yellow]ISSO[reset] -> Predicativo do sujeito

    [red]	Predicativo do sujeito não é complemento de nada.[reset]
		A banca insiste em chamar as orações predicativas e subjetivas de complemento e está ERRADO.
        Além disso a oração é predicativa nominal ( verbo de ligação + predicativo do sujeito )


        CESPE, exemplo:

	                É fundamental que os meninos cheguem.

                                A oração funciona como complemento do vocábulo de 'fundamental'

                            ERRADO -> o que é fundamental? 'que os meninos cheguem...'
		                            Oração subordinada substantiva subjetiva

	                            É fundamental ISSO, ISSO é o sujeito // ISSO é fundamental.
	                                    'é' -> verbo de ligação, 'fundamental' -> predicativo do sujeito
                    '''

    def osare (self):
        return '''
        Periodo Composto por Subordinação:

[red]Orações Subordinadas Adjetivas:[reset]

Estamos dizendo de Adjunto Adnominal oracional

As orações subordinadas adjetivas explicativa -> [green]Com pontuação ( vírgula, travessão, parênteses )[reset]
As orações subordinadas adjetivas restritivas -> [green]Sem pontuação[reset]

São introduzidas por pronomes relativos: ( quando desenvolvidas )

	- [yellow]QUE[reset]
	- [green]O QUAL, A QUAL, OS QUAIS, AS QUAIS[reset]
	- [yellow]ONDE[reset]
	- [green]CUJO[reset]
	- [yellow]COMO[reset]
	- [red]QUANDO[reset]
	- [yellow]QUEM[reset]

    TESTE:

	Os pronomes relativos 	: [red]Troque o QUE pelo - O QUAL, A QUAL, OS QUAIS, AS QUAIS[reset]

	Irá depender da concordância nominal da sentença, retomando o nome. Esse nome possui gênero e número.
				Irá ser colocado de acordo com seu referente.

Existe a oração subordinada adjetiva sem pronome relativo, porém ela será REDUZIDA. e não desenvolvida.

	EM poucas situações, essa troca de pronomes não irá funcionar tão bem.
		Portanto, é fundamental que busque o valor adjetivo da oração.
			Se a oração tem propriedades adjetivas: caracterizar um substantivo.

        
1º exemplo:

    	Jesus, que foi um grande profeta, anunciou a paz.

	        [red]verbos:[reset] 'foi' - 'anunciou' -> [red]Período Composto[reset]


	Como descobrir a oração subordinada adjetiva:

		- Identificar o valor adjetivo da frase.

	[green]'que foi um grande profeta' -> característica de Jesus ( valor adjetivo )[reset] <- 	Oração Subordinada Adjetiva

	[red]Oração Principal:[reset]

		Jesus (...) anunciou a paz.

	[red]Oração Subordinada:[reset]
		
		[yellow],que foi um grande profeta,[reset]

		Troca por '[yellow]O QUAL[reset] foi um grande profeta'. Portanto, a palavra 'que' na sentença é um pronome relativo.

		O primeiro exemplo a oração é uma oração subordinada adjetiva explicativa, por usar a sentença subordinada entre vírgulas.

2º exemplo:

        Os servidores que recebem bem trabalham satisfeitos

		'recebem' // 'trabalham' -> Período Composto

		Os servidores [yellow]os quais[reset] recebem... [green]( Portanto, a palavra 'que' na sentença é um pronome relativo. )[reset]


    [red]Oração Subordinada:[reset]

	    [yellow]'...que recebem bem...'[reset] -> [green]característica atribuida aos servidores[reset] [red]( valor adjetivo )[reset]

		[yellow]É Oração Subordinada Adjetiva[reset]

		A oração subordinada não está separada por pontuação, portanto, é uma oração subordinada adjetiva restritiva.

	[red]Caso retire as vírgulas no primeiro exemplo, a oração ficaria RESTRITIVA.[reset]

    Observação:

		Sem ferir a correção gramatical do texto, poderiamos colocar entre vírgulas.

		Os servidores [yellow], que recebem bem,[reset] trabalham satisfeitos.

		Mas altera o sentido ORIGINAL do texto. 

[red]2º exemplo:[reset]

	Jesus, [yellow]que foi um grande profeta[reset], anunciou a paz. [blue]( Oração Subordinada Adjetiva Explicativa )[reset]

	Um atributo que não foi dado para diferenciar dos outros, mas sim determinante DELE. 

		[red]A explicativa não diferencia mas sim uma característica própria.[reset] ( a alguém ou grupo que seja comum a todo o grupo )
		
        [blue]A restritiva diferencia dos demais. ( separar uma coisa de outra coisa )[reset]

Exemplo:

        O programa 'Minha Casa, Minha Vida' que foi criado pelo governo ajudou os Brasileiros.

	[red]Oração Principal:[reset]

		O programa 'Minha Casa,Minha vida' (...) ajudou os brasileiros.

	[red]Oração Subordinada:[reset]

	[blue]'...que foi criado pelo governo...'[reset]

		Para identificar se a oração subordinada é adjetiva temos que trocar o pronome 'que' por 'os quais', 'as quais' 

			O programa Minha casa, Minha vida [yellow]O QUAL[reset] foi criado pelo governo.

		O pronome relativo retoma 'O programa Minha Casa, minha vida' <- [blue]( Masculino e singular)[reset]

		[red]Portanto a oração é subordinada adjetiva.[reset]

		[blue]Também podemos fazer pelo valor ADJETIVO da oração.[reset]

		Formato: sem pontuação, portanto, oração subordinada adjetiva restritiva

			[bg_red]Sinal então que foi colocada para separar um dos outros. Mas não existe outro programa, dentro do contexto.[reset]

		Portanto, o adequado seria uma oração subordinada adjetiva EXPLICATIVA.

		Não é uma característica de diferencia de outros programas, mas uma característica específica do programa.

	[blue]Sendo assim, o correto:[reset]

		O programa 'Minha Casa, Minha Vida'[yellow], que foi criado pelo governo,[reset] ajudou os Brasileiros.

			[bg_blue]Ou seja, característica ÚNICA.[reset]


Outro Exemplo:

	                As mulheres, que não estudam, ganham menos.

	
	[red]'que'[reset] -> As mulheres, [red]as quais[reset] não estudam, ganham menos -> [red]Pronome relativo[reset]

        [blue]'...que não estudam...'[reset] -> [red]oração subordinada adjetiva ( característica das mulheres )[reset]

		[red]Oração principal[reset] -> [blue]'As mulheres,(...), ganham menos'[reset]

	[green]Com pontuação, portanto, oração subordinada adjetiva explicativa.[reset]

		O adequado seria a RESTRITIVA, sem pontuação.

		[bg_red]A explicativa não diferencia mas sim uma característica própria.[reset] ( a alguém ou grupo que seja comum a todo o grupo )
			No caso do texto, é uma generalização. Separar uma coisa da outra, 

		[bg_red]A restritiva diferencia dos demais.[reset] ( separar uma coisa de outra coisa )       

        Outro exemplo:

	            Os homens que são seres vivos devem cuidar do planeta.     

                'que' -> os homens OS QUAIS são seres vivos devem cuidar do planeta.
			Portanto, pronome relativo.
				Característica dos homens -> 'que são seres vivos' -> oração subordinada adjetiva
		
        Oração principal: Os homens (...) devem cuidar do planeta.

		Sem pontuação: Oração subordinada adjetiva restritiva

		Mas todos são seres vivos, inclusive as mulheres. O adequado seria explicativa, com pontuação.
		O formato adequado seria esse:

			Os homens[yellow], que são seres vivos,[reset] devem cuidar do planeta.

		Característica que é comum a todos no grupo.
		A restritiva separa uma coisa da outra, certo, porém, todos os homens são seres vivos. Não existe 'the walking dead'.

        
Vejamos mais exemplos:

	    A cidade onde moro é tranquila.

	            'moro' -> verbo // 'é' -> verbo -> Período composto por subordinação

		A cidade é tranquila -> Oração Principal // '...onde moro...' -> Oração subordinada

	            'onde' -> Pronome relativo


		Não é cidade qualquer , é uma cidade onde moro -> Oração subordinada adjetiva restritiva
			Existem outras cidades, portanto, está adequado o uso da restritiva.

Exemplo:

        A casa cuja parede foi pintada pertence à rainha.

	[red]'foi pintada'[reset] -> locução verbal // [red]'pertence'[reset] -> verbo -> Período Composto
		'A casa (...) pertence à rainha.' -> [red]Oração principal[reset]

	[red]'cuja'[reset] -> [blue]Pronome relativo[reset] // [blue]'...cuja a parede foi pintada...'[reset] -> Oração Subordinada Adjetiva Restritiva 
                                ( valor adjetivo - caracteristica da casa )

Exemplo:                                

            A maneira como você me trata é incrível.

            [red]'como'[reset] -> Pronome relativo // [red]'...como você me trata...'[reset] -> Oração subordinada ( 'trata' -> verbo // 'é' -> incrível )

        	[yellow]A maneira (...) é incrível[reset] -> [red]oração principal [reset]

		'A maneira' -> 'como você me trata' -> caracterizando 'a maneira' , sem pontuação, oração subordinada adjetiva restritiva.

Exemplo:        

            A mulher a quem me refiro é minha mãe

	'a mulher' -> não é qualquer mulher -> '...é a quem me refiro...', caracterizando a mulher. ( Oração Subordinada Adjetiva Restritiva )
    [red]'a quem'[reset] -> Pronome relativo que introduz a oração subordinada adjetiva.
		'a mulher (...) é minha mãe' -> Oração Principal ( sem pontuação, restritiva )

		'quem'   -> Pronome relativo como referente a pessoas [red]( 'a' de a quem é uma preposição em concordância com o[reset]
                                    [red] verbo transitivo indireto 'referir' )[reset]

                    Pronomes:

		'quando' -> Pronome relativo que serve para tempo	
		'como' ->   ideia de modo, maneira

Exemplos:        

        O ano que vem será maravilhoso !

	        O ano [yellow]O QUAL[reset] vem será maravilhoso! ( som estranho )

		        'que' -> pronome relativo  ( mesmo trocando por 'O QUAL', é uma oração subordinada adjetiva restritiva )

	    Oração Principal: 'O ano (...) será maravilhoso'

                Oração Subordinada: '...que vem...'

[bg_red]            PRONOME RELATIVO:[reset]

	Possui função sintática [red]( a conjunção integrante não possui sintaxe )[reset]

Exemplo:

	    Eu comprei uma roupa nova. Ela custou mais de R$ 300,00.

	[red]verbos:[reset] 'comprei' // 'custou' -> [blue]2 períodos simples.[reset]

	[red]'eu'[reset]  -> Sujeito simples // quem compra, compra: [red]'uma roupa nova'[reset] -> Objeto Direto

	[red]'ela'[reset] -> Sujeito simples // 'custou' -> [red]verbo intransitivo[reset] 
                    [red]'mais de R$ 300,00[reset] -> Adjunto Adverbial de preço ( circunstância )

	Posso transformar em um período composto? SIM

	[bg_blue]'ela' -> Pronome pessoal do caso reto para retomar 'uma roupa nova'.[reset]

	Eu comprei uma roupa nova [yellow]que[reset] custou mais de R$ 300,00.
	
		No lugar do 'ela' foi o 'que', tendo assim um período composto.

	EU comprei uma roupa nova [yellow]A QUAL[reset] custou mais... ( 'que' portanto é pronome relativo )

		Sendo assim, depois do '[yellow]...que custo mais de R$300,00.'[reset] -> [blue]oração subordinada adjetiva restritiva.[reset]

	O pronome 'que' não existe de marcar gênero e número. Já o pronome pessoal do caso reto não relaciona períodos e forma um somente.

		Já o pronome relativo , relaciona orações.
		O pronome pessoal do caso reto acompanha ou substitui um substantivo. Substituindo o substantivo 'uma roupa nova'.
		Já o pronome relativo é sempre pronome substantivo.    
        
        Macetes para descobrir a função sintática do pronome:


        1. Leia no pronome relativo o próprio referente. [red]'que' = 'uma roupa nova'[reset]

		Sendo assim, o pronome relativo 'que' na sentença é o sujeito da oração subordinada.
			            A função sintática desse pronome é o sujeito.
				            Nem todo pronome relativo é sujeito.

Exemplo:


            A criança que foi encontrada sozinha no parque já foi entregue aos pais.

                [red]'foi encontrada'[reset] // [yellow]'foi entregue'[reset] -> Locuções verbais -> Período composto.

                [green]'que foi encontrada sozinha no parque'[reset] -> atributo da criança -> [blue]oração subordinada adjetiva restritiva[reset]

                Para certificar a classificação do pronome relativo:

                Substituindo o pronome relativo 'que' por 'a qual' -> 'A criança [yellow]a qual[reset] foi encontrada...'

        Oração principal: A criança (...) já foi entregue aos pais.

        Qual é a função sintática do pronome relativo 'que' na oração subordinada?

        1. Identificar o pronome relativo e o seu referente:

		O pronome relativo é o [yellow]'que'[reset] e seu referente é [yellow]'A criança'[reset] <- Sujeito simples

        2. Substituir o pronome pelo referente na oração subordinada:

            [red]'A criança[reset] foi encontrada sozinha no parque...'

        3. Fazer a análise sintática do pronome substituido:

                    'a criança' <- Sujeito = 'que' -> Sujeito 


Portanto, o pronome relativo 'que' na sentença é sintaticamente o sujeito da locução verbal 'foi encontrada'.


+ Exemplos:

		    Eles conheceram os diretores que convocaram a reunião.

		        'conheceram' - 'convocaram' -> 2 verbos ( período composto )

		        vocábulo suspeito: 'que' é pronome relativo?

		            [yellow]'os quais[reset] convocaram a reunião' -> 'que' é pronome relativo.
		
		Sem pontuação, portanto, '...que convocaram a reunião' <- oração subordinada adjetiva restritiva

		qual a função sintatica do pronome relativo QUE?

			Esse pronome relativo precisa ter um referente.
				O [yellow]'QUE'[reset] retoma [red]'os diretores'[reset] <- detalhe: 'os diretores' é sujeito, veja só:

                '[blue]...os diretores[reset] convocaram a reunião.' [green]( substituir o pronome pelo referente )[reset]

			quem é que convocaram a reunião? [red]'os diretores'[reset] <- [blue]Sujeito simples[reset]

		[bg_red]OPA![reset] - > Se [red]'os diretores'[reset] é o sujeito e o pronome relativo [red]'QUE'[reset] está substituindo os diretores <-
				então o 'QUE' possui a função sintática de SUJEITO. // Sujeito do verbo 'convocaram.'
                                quem convoca, convoca algo: 'a reunião' <- objeto direto

            Repare que na oração principal temos um verbo transitivo direto: 'conheceram' -> quem conheci, conheci alguém: 'os diretores'                                

		Oração Principal:

				Eles conheceram os diretores...

		Oração subordinada:

				...que convocaram a nova reunião ( adjetiva restritiva )

Exemplos:

                As coisas que o mundo oferecia me impediam de te encontrar.

                'As coisas [yellow]as quais[reset] o mundo oferecia...' -> 'que' portanto é pronome relativo.

                Oração Principal:

                As coisas (...) me impediam de te encontrar.

                Oração Subordinada:

                [yellow]'...que o mundo oferecia...'[reset]  <- Adjetiva restritiva ( sem pontuação )

                Oração Principal:

                [red]'as coisas'[reset] -> Sujeito da oração principal do primeiro verbo 'impediam'
                            		referente do pronome relativo é o sujeito 'as coisas', certo?

                    2. Substituir pelo pronome relativo pelo sujeito da oração principal:

                            [yellow]As coisas[reset] o mundo [yellow]oferecia[reset] ...

                            'as coisas' não pode ser sujeito do verbo 'oferecia'				
				                    [red]Por que não há concordância verbal !![reset]

                    [bg_red]O verbo 'oferecia' está no singular e o referente 'as coisas' (sbus) está plural ![reset]

                            [yellow]'O mundo'[reset] é o sujeito. ( a frase não está na ordem direta )

                                quem que oferecia as coisas? [red]'o mundo'[reset] -> [blue] O sujeito [reset]
                                    quem oferece, oferece algo: [red]'as coisas'[reset] <- [blue]Objeto direto [reset]

Se 'as coisas' é objeto direto e o pronome relativo 'que' foi substituido pelo nome 'as coisas'.
		Portanto a função sintática do pronome relativo é objeto direto da oração subordinada adjetiva restritiva.                                    

                        Mostrando que o pronome relativo 'que' nem sempre será SUJEITO.

                        O pronome relativo é sempre pronome substantivo ( não é adjetivo )
			                      Sempre anafórico, sempre retomar o que vem antes.
		                    Outra: O termo retomado sempre estará na oração principal.


                            LEMBRANDO!


	O pronome relativo é uma classificação morfológica e do ponto de vista sintático o pronome relativo pode asssumir diversas funções.

		 Nem sempre será sujeito, e a função sintática nem sempre será sobre o referente. Até por que o referente compõe a oração principal
					                    ao passo que o pronome relativo compõe a oração subordinada.

			A função sintática do pronome relativo não tem relação direta com a função a sintática do referente.


Exemplo:

       	As medidas [yellow]que[reset] o governo adotou pregam a austeridade.

        'As medidas [yellow]AS QUAIS[reset] o governo adotou...' -> [blue]'que' portanto é pronome relativo.[reset]

        [red]Oração principal:[reset]

		    As medidas (..) pregam a austeridade.

        [red] Oração Subordinada:[reset]

            [yellow]'... que o governo adotou...'[reset] <- Oração Subordinada Adjetiva Restritiva            

            Qual a função sintática do pronome relativo dentro da oração subordinada?


            Lembrando que:

				O pronome relativo 'que' no contexto retoma 'as medidas'.

                Substituindo o pronome pelo nome seria:

                        'As medidas o governo adotou...' <- 'o governo' -> Sujeito

                            quem adotou as medidas??  'o governo' -> Sujeito

                            quem adota, adota algo: 'as medidas' -> Objeto Direto

            Existe uma relação entre sujeito e verbo que é: Concordância verbal!   

                        E nesse caso há concordância verbal.

            Agora 'as medidas', o termo retomado é na verdade o pronome relativo substituido: 'que'
        que por sua vez é objeto direto, portanto, o pronome relativo em questão possui função sintática de objeto direto.   


Outro exemplo com pronomes preposicionados:

                    As medidas [yellow]em que[reset] o governo confia podem não ser aprovadas.

        Oração Principal:

        'As medidas (...) podem não ser aprovadas.'           

        Oração Subordinada:

        '...em que o governo confia...'

        'o governo' <- Sujeito // quem confia, confia EM: 'nas medidas' -> [blue]( contração ou aglutinação: preposição 'em' + artigo 'as' )[reset]

        Precisamos conservar a preposição sem erro ou perda gramatical:

        'em que' -> 'nas quais'

        A aglutinação é um processo de formação de palavras compostas em que dois ou mais elementos se unem, 
        mas com alterações em pelo menos um deles — como a perda de fonemas ou sílabas, ou mudanças na pronúncia.

Por exemplo:

- água + ardente  → aguardente
- plano + alto    → planalto
- em + boa + hora → embora

Diferente da justaposição, onde os elementos se mantêm intactos (como em guarda-chuva), 
na aglutinação há uma fusão mais intensa, resultando em uma nova palavra com estrutura e som diferentes das originais.


Outro exemplo:

                As medidas [yellow]de que[reset] o governo precisa são questionadas.

                [red]Oração Principal:[reset]

                As medidas (...) são questionadas.

                [red]Oração Subordinada:[reset]

                [yellow]'... de que o governo precisa...'[reset] <- ( não são medidas quaisquer, são específicas, portanto, oração subordinada adjetiva restritiva )

                [yellow]'o governo'[reset] -> Sujeito // quem precisa, precisa [yellow]de[reset]: [blue]'de medidas'[reset] <- [green]Objeto indireto[reset]

                [red]Pronome relativo[reset]: [yellow]'de que'[reset] por [yellow]'das quais'[reset] o governo precisa <- [blue]Confirmando que é pronome relativo preposicionado[reset]

Sem prejuizo gramatical: preposição 'de' + artigo 'as' ( aglutinação ou contração )	

A aglutinação é um processo de formação de palavras compostas em que dois ou mais elementos se unem, mas com alterações em pelo menos um deles — 
como a perda de fonemas ou sílabas, ou mudanças na pronúncia.

Por exemplo:

- água + ardente  → aguardente
- plano + alto    → planalto
- em + boa + hora → embora

Diferente da justaposição, onde os elementos se mantêm intactos (como em guarda-chuva), 
na aglutinação há uma fusão mais intensa, resultando em uma nova palavra com estrutura e som diferentes das originais.	                


         
Exemplos:

            As medidas a que o governo se refere são constitucionais.


                [red]Oração Principal:[reset]

			As medidas (...) são constitucionais.

                    Oração Subordinada:

			[yellow]'...a que o governo se refere...'[reset] ( não são medidas quaisquer, portanto, oração subordinada adjetiva restritiva )

            Pronome relativo?  'As medidas [yellow]às quais[reset] o governo se refere...' -> [blue]( preposição 'a' + artigo 'a' <- JUNÇÃO = CRASE ) sim, PRONOME RELATIVO.[reset]


            Substituindo o pronome pelo nome:

                    '...às medidas o governo se refere...'

                    quem se refere, se refere à: 'às medidas' <- Objeto indireto

Outros exemplos:

		            O servidor que serei será exemplo na administração pública.

                    [red]Oração Principal:[reset]

                    O servidor (...) será exemplo na administração pública.

                    [red]Oração Subordinada:[reset]

                    [green]'que serei'[reset] -> não é qualquer servidor, uma atribuição, portanto, subordinada adjetiva restritiva

                    Substituindo o pronome 'que' por 'o qual':

                    'O servidor [yellow]o qual[reset] serei...' <- [blue]retomando 'o servidor'[reset] <- Sujeito da oração principal

                    Substituir o pronome relativo pelo referente: 'O servidor', assim:

                        '[yellow]O servidor[reset] (eu) serei...'

                        ( verbo SER = de estado, servindo como ligação para uma atribuição ao sujeito elíptico 'EU' )

                        Se o verbo de estado 'SER' é de ligação, o sujeito é elíptico, sendo assim, 'O servidor' é um predicativo do sujeito.

                        Sendo assim, o pronome relativo 'que' tem função sintática de predicativo do sujeito.

Outro exemplo:

        Não estão disponíveis os medicamentos [yellow]a que[reset] a população tem acesso.


        Não são medicamentos quaisquer, são [blue]'a que a população tem acesso.'[reset] <- [red]Oração subordinada adjetiva restritiva[reset]

        Substituindo o pronome preposicionado: 'a que' por 'aos quais' temos:

            'Não estão disponíveis os medicamentos aos quais a população tem acesso.'

            [yellow]'aos quais'[reset] -> Para concordar com número e gênero com 'medicamentos' ( preposição 'a' + artigo 'os' = Contração )


        2. Substituir o pronome relativo pelo referente:

                '...[yellow]aos medicamentos[reset] a população tem acesso.' ( Atenção!  Usar a contração para substituir o pronome pelo referente! )


                quem tem acesso? [green]'a população'[reset] <- Sujeito // quem tem, tem algo: [green]'acesso aos medicamentos'[reset] <- Objeto Direto
		( preposição 'a' + artigo 'os' <- Contração )

                        Colocar em ordem direta:

                            'A população tem acesso [yellow]aos medicamentos[reset]...'

[red]  'aos medicamentos' [reset]é complemento nominal, portanto, o pronome relativo substituido pelo referente possui função sintática de:
				                    complemento nominal ( os medicamentos são acessados )  


            [red] Oração Principal:[reset]                                                              

            'Não estão disponíveis os medicamentos...'

            [red] Oração Subordinada:[reset]

            '...a que a população tem acesso.'

+ exemplos:

            A criança de que Maria foi mãe é Jesus.


            [red]Oração Principal:[reset]

		                A criança  (...) é Jesus.

	            [red]Oração Subordinada:[reset]

                        '... de que Maria foi mãe...'


            Passo 1:

            Substituindo o pronome relativo preposicionado 'de que' por 'da qual' [blue]( preposição 'de'+ artigo 'a' = 'da' ( contração ) )[reset]
			Seu referente é feminino, concordando e retomando o referente.

            '... [yellow]da qual[reset] Maria foi mãe..' <- Portanto é um pronome relativo que seu referente é 'a criança'.                        

            Substituindo o pronome pelo referente:

            ...[yellow]da criança[reset] Maria foi mãe...'	[bg_red]( ATENÇÃO!! 'usar a preposição contraida' )[reset]

            Lembrando que precisamos saber a função sintática do pronome relativo a qual está sendo substituido:

            Ordem direta:

			            Maria foi mãe da criança.

            quem foi mãe da criança?  'Maria' <- Sujeito

            'foi' é um verbo de ligação a qual 'mãe da criança' é um atributo de 'Maria' que por sua vez é o sujeito.
				            Sendo assim, 'mãe da criança' é um predicativo do sujeito.                        

                            'mãe da criança' -> 'da criança' é adjunto adnominal
				        ( expressão preposicionada ligada a substantivo concreto )

                [blue]Portanto, o pronome relativo 'de que' na frase possui a função sintática de adjunto adnominal.[reset]


Exemplo:

		            O restaurante [yellow]em que almoçamos ontem[reset] será fechado.                


                    [red]Oração Principal:[reset]

			                O restaurante (...) será fechado.

                    [red]Oração subordinada:[reset]

			                '... em que almoçamos ontem...'          


    Substituindo o pronome relativo preposicionado: [red]'em que'[reset] por [red]'no qual'[reset] 
                            ( preposição 'em' + artigo 'o' = 'no qual' -> Contração )
			Concordando em gênero e número com o sujeito retomado e referente 'O restaurante'.            

            O restaurante [yellow]no qual[reset] almoçamos ontem será fechado. ( Portanto, pronome relativo )                                  

Substituindo o pronome pelo referente temos:

        [bg_red]ATENÇÃO! Conservar a preposição e contraí-lo:[reset]

        no restaurante almoçamos ontem

            		Ordem direta:

    		Almoçamos ontem no restaurante

                quem almoçaram? Sujeito elíptico, oculto ou desinencial (nós)


                Verbo 'almoçar' é intransitivo:
		
		            almoçou quando? [green]'ontem'[reset] <- Adjunto Adverbial de tempo

		            almoçou onde? [green]'no restaurante'[reset] <- Adjunto Adverbial de lugar


                    [blue]Portanto, 'no restaurante' é equivalente ao pronome substituido 'em que'[reset]
			            [blue]Logo, 'em que' possui a função sintática de ADJUNTO ADVERBIAL[reset]

Observação:

		Mais frequência em provas:

			1. Pronome relativo funcionando como sujeito
			2. Pronome relativo como objeto direto
			3. Pronome relativo em que é necessário colocar uma preposição


Atenção!

	Em geral:

			Ao substituir um pronome relativo preposicionado somente poderá substitui-lo pela mesma preposição.

	                    'em que' por 'na qual' ou 'no qual' dependendo do referente. ( gênero e número )			
			
		    	    Agora se o pronome relativo não está preposicionado, não devemos colocar preposição.

	    		            Claro que pode mudar a sintaxe se substituir ou inserir preposição.
    		                    Mas não há erro gramatical mas acarreta mudança de sentido.

ONDE -> Pronome Relativo

                        A democracia é um regime [red]onde[reset] todos têm voz.

                        O pronome relativo 'ONDE' retoma REGIME.

                        'regime' -> Não é lugar, portanto está ERRADO. Não pode ser utilizado dessa forma.
		        Somente para lugares, que por sua vez possui função sintática de Adjunto Adverbial de lugar


                Como seria CORRETO?

                Usar o : [blue]'em que'[reset]

		            Já que regime é [green]MASCULINO e SINGULAR[reset] : 'em que'  ou 'no qual' :

                        A democracia é um regime [green]em que/no qual[reset] todos têm voz.


            ONDE -> Há preposição imbutida nele [blue]( sempre e equivalente igual a 'em que' )[reset]

            Dependendo da circunstância ('no qual', 'na qual', 'nos quais', 'nas quais') -> referente estiver no plural/singular


            A quadra onde moro é calma.


                [red]Fique atento a concordância do referente[reset]: [blue]'A quadra'[reset] -> [green]Singular e Feminino[reset]

                A quadra [green]NA QUAL[reset] moro é calma. -> Correto
	            A quadra [green]EM QUE[reset]  moro é calma. -> Correto


                Obrigatoriamente a preposição irá aparecer devido ao fato de morar em algum lugar.
		                                quem mora, mora EM algum lugar.

                    Ninguém mora [red]á a algum lugar, com algum lugar, por algum lugar[reset]

                            ou seja o verbo MORAR quando se associa em lugares exige a preposição EM ou NA QUAL.

                LEMBRE-SE: [blue]O 'onde' já contém a preposição dentro dele.                            [reset]

                Quem vai à algum lugar, vai trabalhar à algum lugar.

                Daí ai você usa o pronome relativo AONDE [red]( NÃO SE USA PREPOSIÇÃO 'EM')[reset]

                O país [blue]A QUE[reset] vou está em guerra.
	            O país [blue]AO QUAL[reset] vou está em guerra.


Exemplo abaixo:

            Verbo IR -> quem vai, vai a algum lugar. Agora quem vem DE algum lugar:

                A praça [yellow]DE ONDE/DONDE[reset] venho está perto.
	            A praça [yellow]DE QUE/DA QUAL[reset] venho está perto.

            Verbo CORRER -> quem corre, corre [yellow]EM[reset] algum lugar. ( corro na esteira, na casa, na pista )                

            O parque [yellow]ONDE (em que)[reset] corro será reformado.
	        O parque [yellow]NO QUAL[reset] corro será reformado.

            CUJO -> Adjunto Adnominal ( quase sempre ) //  complemento nominal (raramente)

Não é usado muito, e caiu em desuso. Pouco usado.

		Existe uma série de regras pra usar.

	A sentença que é feita para usar o pronome relativo CUJO é somente para esse pronome.

Exemplo:

	        O carro cujas as portas estão amassadas é meu.      

            1.( O 'cujo' retoma o antecedente ) <- Pronome relativo sempre faz referente ao antecedente.
				Mas deve concordar com o consequente.

		    2. O pronome CUJO não pode ser seguido de artigo.

		    3. Relaciona ideias de posse.
		    4. Não possui substituto ( frase feita somente para o CUJO )     

Na frase temos:


            O carro velho cujas portas estão amassadas é meu.

            As portas são do carro, cujas as portas ( do carro ) as portas pertencem ao carro, ideia de posse.
		Lembre-se que o adjunto adnominal é o agente possuidor, sintaticamente.
		Agora quando for complemento nominal, a ideia de posse não vai rolar. (raramente)

            
Outro exemplo:

            Na linha pontilhada vou indo, na terra [yellow]cujo[reset] herói matou 1 milhão de índios.


            [yellow]cujo[reset] retoma o antecedende: [blue]'terra'[reset]
            [yellow]cujo[reset] concorda com o consequente: [blue]'herói'[reset]

                    Indica posse: herói da terra. ( ele é da terra) // 'da terra' -> Adjunto Adnominal

            [red]Oração Principal:[reset]                    

            'Na linha pontilhada vou indo, na terra...'

            'na linha pontilhada' -> Adjunto Adverbial de lugar
            'vou indo' -> Locução verbal intransitivo
            
                Sujeito oculto -> 'na linha pontilhada (eu) vou indo, na terra <- 'na terra' -> Adjunto Adverbial de lugar

            [red] Oração Subordinada:[reset]                

            '...cujo herói matou 1 milhão de índios.' <- Subordinada adjetiva restritiva 

            Introduzida pelo pronome relativo possessivo 'cujo'.
            Não exerce função sintática própria, apenas liga “terra” a “herói” com ideia de posse.

            quem matou? 'herói' -> Sujeito Simples ( substantivo concreto)

            quem mata, mata alguém: '1 milhão de índios' <- Objeto Direto.

Exemplo:

            A mulher cuja bolsa foi roubada é Helena.

            Oração Principal:

                A mulher (...) é Helena.

            Oração Subordinada:

                '...cuja bolsa foi roubada...'

                Ideia de posse: como se dentro do pronome estive a preposição 'de'

                                Bolsa da mulher ( de ( preposição ) + a (artigo) -> Contração)                


                'foi roubada' -> voz passiva  // Bolsa da mulher foi roubada ( sendo 'bolsa da mulher' -> Sujeito Paciente )

                'da mulher' -> Adjunto Adnominal, sendo assim, o 'cuja' admite função sintática de adjunto adnominal.



Exemplo:            

            A carne cuja venda caiu será comercializada a preços menores.

         'cuja' na sentença retoma o antecedente 'carne' e concorda com o consequente 'venda' -> feminino e singular
         Sem presença de artigo.
		 A venda (...) da carne <- A carne é vendida, 'a carne' é complemento nominal.

         - O pronome “cuja” estabelece uma relação de posse entre dois substantivos.


         Oração Principal:

            A carne (...) será comercializada a preços menores.

                'A carne' -> Sujeito da oração principal

                    'será comercializada' -> Voz passiva ( locução verbal )

                    'a preço menores' -> Adjunto Adverbial de modo

         Oração Subordinada:

            '...cuja venda caiu...'  <- subordinada adjetiva restritiva ( caracteiza carne, que caiu )

            'venda' -> Sujeito da oração subordinada // 'caiu' -> Verbo intransitivo

            'cuja' -> Pronome relativo possessivo

            Na análise mais tradicional da gramática normativa, “cujo” é considerado apenas um pronome relativo possessivo, 
que faz parte de um termo da oração (normalmente o sujeito ou objeto), mas ele mesmo não exerce função sintática isolada —
essa função cabe ao termo completo (ex: “cuja venda”).

"A carne cuja venda caiu..."
→ Aqui, o termo “cuja venda” seria o sujeito da oração “venda caiu”, e "cuja" serve apenas como elemento de ligação e posse.

2. Função sintática: Complemento nominal (visão alternativa)
Alguns estudiosos de base mais funcionalista ou estruturalista argumentam que, em certas estruturas, 
o pronome "cujo" exerce uma função similar à de complemento nominal, pois representa uma relação de posse com
o núcleo de um substantivo abstrato — por exemplo, "venda", "conhecimento", "proposta", etc.
Exemplo: “O projeto cuja aprovação foi adiada...”
→ “cuja” indicaria o possuidor (o projeto) do substantivo abstrato “aprovação”, típico caso em que se aceita complemento nominal.


✅ Conclusão:
- Na gramática tradicional, prevalece a visão de que “cujo” não exerce função sintática direta —
a função pertence ao termo do qual faz parte (como sujeito).
- Em abordagens mais modernas ou descritivas, há espaço para reconhecê-lo também como complemento nominal,
especialmente em contextos com substantivos abstratos que pedem esse tipo de complemento.

ATENÇÃO! 

	O pronome relativo CUJO pode vir PREPOSICIONADO.

            As mulheres em cujo entendimento confio devem ser recompensadas.

            antecede 'mulheres' e concorda com 'entendimento' -> CORRETO

		    sem artigo, entre substantivos e sem verbos -> CORRETO

            Queremos dizer:
	
			As mulheres em cujo entendimento (EU) confio devem ser recompensadas.

		    Eu confio no entendimento das mulheres <- Sujeito oculto ( EU ) 

            ( VTI ) quem confia, confia em algo: 'no entendimento das mulheres' <- Objeto indireto

			'cujo' continua sendo ADJUNTO ADNOMINAL ( 'das mulheres' possuem o entendimento )

            [red]Oração Principal:[reset]

            'As mulheres (...) devem ser recompensadas.'

            quem que devem ser recompensadas? 'As mulheres' <- Sujeito

                'devem ser recompensadas' -> Predicado da oração principal verbal passiva analítica

            [red]Oração Subordinada:[reset]

                '...em cujo entendimento confio.' -> Oração subordinada adjetiva restritiva

                As mulheres em cujo entendimento (EU) confio devem ser recompensadas.

        		Eu confio no entendimento das mulheres <- Sujeito oculto ( EU ) // ( Preposição 'em' + artigo 'o' = 'NO' -> Contração )

                entendimento DELAS -> Adjunto Adnominal

                Portanto, o 'em cujo' admite função sintática de ADJUNTO ADNOMINAL.                 
        
        '''
    def exercicios_OS (self):
        return '''
        
        Exercícios:


1. Assinale a alternativa na qual a palavra 'que' não tenha sido empregada como pronome relativo:

a. Podemos dizer [yellow]que[reset] é a busca de uma relação harmoniosa.
b. Sujeitos [yellow]que[reset] amam, sofrem, adoecem.
c. Complexidade dos problemas [yellow]que[reset] caracterizam a realidade sanitária.
d. Drogas lícitas ou ilícitas, [yellow]que[reset] são determinantes fundamentais.
e. Mobilização [yellow]que[reset] tenta romper o individualismo.
        

        Podemos dizer [yellow]que[reset] é a busca de uma relação harmoniosa.

        Podemos dizer ISSO <- oração subordinada substantiva

        Não podemos dizer assim:  Podemos dizer [yellow]o qual[reset] é a busca...??  [blue]Portanto, é uma conjunção integrante.[reset]

        [blue](nós)[reset] podemos dizer... <- [red]Sujeito Oculto[reset]

        quem diz, diz algo, diz [yellow]ISSO[reset]: que é a busca de uma relação harmoniosa. <- [red]Objeto Direto[reset]

        [red]Portanto, é uma oração subordinada substantiva objtiva direta.[reset]

        [green]OBSERVAÇÃO![reset]


		       [green] O 'que' está depois de um verbo, nunca será um pronome relativo![reset]
			          [green]  Pode ser conjunção integrante e entre outras coisas.[reset]

                      Gabarito correto LETRA A.

Letra B:
		
		Sujeitos [yellow]que[reset] amam, sofrem, adoecem

		Sujeitos [yellow]os quais[reset] amam, sofrem, adoecem.

		Pronome relativo, portanto.
		Atribuindo valores 'aos sujeitos', sendo assim, oração subordinada adjetiva restritiva.

Letra C:

        
	    Complexidade dos problemas [yellow]que[reset] caracterizam a realidade sanitária.

        Substituir por outro pronome relativo, se der certo, é pronome relativo.


        Complexidade dos problemas [yellow]os quais[reset] caracterizam a realidade sanitária.

			            Portanto, 'que' é pronome relativo.  

Letra 'D':

	    Drogas lícitas ou ilícitas, [yellow]que[reset] são determinantes fundamentais.

		        Substituir por outro pronome relativo:

		        ....drogas lícitas ou ilícitas, [yellow]as quais[reset] são determinantes fundamentais
		
			                Portanto, 'que' é pronome relativo.                        


Alternativa E. 

            Mobilização que tenta romper o individualismo.

	            Mobilização [yellow]A QUAL[reset] tenta romper o individualismo.                            

2. Marque a alternativa incorreta quanto ao uso do pronome relativo:

a. Países [yellow]cujo[reset] os índices de desenvolvimento humano sejam baixos não serão considerados nesta pesquisa.
b. A menina passava longo tempo observando os pássaros do rancho, [yellow]os quais[reset] se agrupavam na grama em busca de insetos.
c. A fazenda [yellow]onde[reset] nasci não existe mais: a área foi toda loteada há vinte anos.
d. Fui eu [yellow]quem[reset] escreveu o texto.

[red]Análise da alternativa A:[reset]


Países [yellow]cujo os[reset] índices de desenvolvimento humano sejam baixos não serão considerados nesta pesquisa.

        Pronome relativo [yellow]'cujo'[reset] retoma o antecedente e deve concordar com o consequente.
                [red]'índices'[reset] está no plural.
		    [bg_red]Além disso temos um artigo, que está errado.[reset]

		Então o adequado seria:

		Países [yellow]cujos[reset] índices de desenvolvimento humano...

        Portanto, gabarito letra 'A'.


A menina passava longo tempo observando os pássaros do rancho, [yellow]os quais[reset] se agrupavam na grama em busca de insetos.

        [yellow]'os quais'[reset] <- Pronome relativo que introduz uma subordinação adjetiva restritiva. Além disso retoma 'pássaros'.
		
        Substituindo o pronome relativo pelo referente temos:

		[yellow]pássaros[reset] se agrupavam na grama...  // quem é que se agrupavam na grama? [yellow]'pássaros'[reset] <- [red]Sujeito[reset]
		    [blue]Sendo assim, o pronome relativo 'os quais' na sentença possui a função sintática de SUJEITO.[reset]

[red]Letra C:[reset]

		A fazenda [yellow]onde[reset] nasci não existe mais: a área foi toda loteada há vinte anos.

			O pronome relativo [blue]'onde'[reset] retoma [yellow]'fazenda'[reset] que é um lugar. -> [green]CORRETO[reset]

		Para realocar outro pronome relativo: [yellow]DONDE, AONDE[reset] precisamos olhar o verbo [blue]'nascer'[reset]

			[blue]por que quem nasci, nasci em algum lugar:[reset] [bg_green]'EM'[reset] <- [bg_red]Preposição obrigatória[reset]

            O pronome relativo [yellow]'ONDE'[reset] usado no contexto já possui a preposição [yellow]'em',[reset]
             funciona com o verbo 'nascer' que tambem exige em seu complemento a preposição 'em'.

            [red]Agora o pronome AONDE exige a preposição 'a' [reset] -> ideia de movimento a ( destino, deslocamento ) - 
                                            [bg_red]Não funciona com o verbo NASCER[reset]

            [red]Agora o pronome DONDE exige a preposição 'de'[reset] -> origem, procedência <- Não funciona com o verbo NASCER

            [bg_red]Se vc quiser ou eu quiser mudar o pronome, devemos mudar o verbo.[reset]

            O verbo 'VIR' exige em seu complemento a [blue]preposição 'DE'[reset] -> A cidade [yellow]DONDE[reset] vim.  [green] ( quem vai, vai de...)[reset]                 
            O verbo 'IR' exige em seu complemento a [blue]preposição 'A'[reset]   -> O lugar [yellow]AONDE[reset] vou.  [green]( quem vai, vai a...)[reset]

Atenção para a alternativa 'D':

	Fui eu [yellow]quem[reset] escreveu o texto.

	Fui eu [yellow]que[reset] escrevi o texto.

    Sempre que usamos o vocábulo [yellow]'que'[reset], a concordância do verbo que vem na sequência é com o pronome pessoal do caso reto -> [green]'EU'[reset]

    Fomos [green]nós[reset] [yellow]que[reset] [blue]escrevemos[reset] o texto.

    Sempre que usamos o vocábulo 'que', a concordância do verbo que vem na sequência é com o pronome pessoal do caso reto -> [green]'NÓS'[reset]

    Foram [green]eles[reset] [yellow]que[reset] [blue]escreveram[reset] o texto.

    Sempre que usamos o vocábulo 'que', a concordância do verbo que vem na sequência é com o pron. pessoal do caso reto [bg_red]( 3º pessoa do plural -> Eles )[reset]

    O pronome relativo [yellow]'que'[reset] é um pronome neutro, ou seja, não exige gênero nem número para concordar com ningúem.
			Ele vai assumir o gênero e número do seu referente , os pronomes pessoais.


                        [blue]Eu que[reset] escrevi // [blue]nós que[reset] escrevemos // [blue]eles que[reset] escreveram


Agora o pronome relativo [yellow]QUEM[reset], de natureza, é somente só, na 3º pessoa do singular [red]( Não é neutro!)[reset]      

          		[blue]Pronome neutro ajustamos para qualquer pessoa do discurso! ( O caso do pronome relativo QUE )[reset]                

                Agora com o pronome [yellow]QUEM[reset] é diferente:

                Sendo assim, temos duas possibilidades de concordância.
                O verbo deve concordar com o pronome relativo [blue]'quem' ( somente na 3º pessoa do singular )[reset]

                Fui eu [yellow]quem escreveu[reset] o texto. 
            
                Fomos nós [yellow]QUEM ESCREVEU[reset] o texto.

                Foram eles [yellow]QUEM ESCREVEU[reset] o texto.


                [red]Atenção![reset]

                [bg_red]Quando usamos o pronome relativo 'que', o verbo deve concordar com o pronome pessoal do caso reto.[reset]
		
		        [bg_blue]Quando usamos o pronome relativo 'quem' antecedido do pronome pessoal do caso reto.[reset]

                [bg_green]O verbo pode concordar com o pronome pessoal do caso reto ou com o relativo. ( estando os dois na mesma sentença ) [reset]

                        Mas o mais adequado é usar o 'quem' para verbos no SINGULAR.

                Foram eles [yellow]quem[reset] fizeram isso. <- Verbo concordando com o sujeito 'eles' -> [blue]3º pessoa do plural[reset]

                    Mas, pela norma culta, essa construção é menos recomendável. 
                        A forma com “que” é mais gramaticalmente aceita quando o antecedente é plural.

3. Assinale a afirmativa na qual a palavra destacada NÃO exerce a mesma função que em 
'Mas a ele, no canto mais afastado do jardim, [yellow]que[reset] a seus cuidados cabia, ninguém via.'                        


a. 'Mas ele, [yellow]que[reset] há tanto esperava, não tinha pressa.'
b. '... podando os espigões teimosos [yellow]que[reset] escapavam à harmonia exigida.'
c. ' sua voz não se entrelaçava à música distante [yellow]que[reset] vinha dos salões.'
d. 'disse o jardineiro a si mesmo [yellow]que[reset] já era tempo de ter uma companheira.'
e. 'Já se fazia grande e frondosa a primeira árvore [yellow]que[reset] havia plantada naquele jardim...'

[blue]Vamos analisar a frase do enunciado:[reset]

                '... no canto mais afastado do jardim, [yellow]o qual[reset] a seus cuidados cabia...'

                [yellow]'o qual'[reset] -> retomando o vocábulo 'jardim' ->: [red]singular e masculino[reset]
					                    Portanto, é um pronome relativo.

a. Mas ele, que há tanto esperava, não tinha pressa.'

        [red]Oração principal:[reset]

            'Mas ele, (...), não tinha pressa.'

        [red]Oração Subordinada:[reset]

            '...que há tanto esperava...' <- [blue]ideia de atribuição adjetiva ao SUJEITO[reset]

                Portanto, há uma subordinação adjetiva explicativa ( com pontuação )

        [red]Análise sintática:[reset]

                 Mas ele, que há tanto esperava, não tinha pressa.'

                 [yellow]'mas'[reset] -> [blue]conjunção adversativa coordenativa[reset]
                 [yellow]'ele'[reset] -> [red]Sujeito[reset] [blue]( pronome pessoal do caso reto)[reset]
                 quem não tem, não tem: [yellow]'pressa'[reset] <- [red]Objeto direto[reset] // [red]'tinha'[reset] ->[blue] Verbo transitivo direto[reset]
                 [yellow]'que'[reset] -> [red]pronome relativo ( retoma o sujeito 'ELE')[reset],[blue] atua como sujeito da oração subordinada.[reset]
                 [yellow]'esperava'[reset] -> [blue]Verbo intransitivo[reset]
                 [yellow]'há tanto'[reset] -> [blue]locução adverbial de tempo[reset]
                 [yellow]'não tinha pressa'[reset] ->[blue] predicado verbal da oração principal[reset]
                 [yellow]'não'[reset] -> [blue]advérbio de negação[reset]

B. '... podando os espigões teimosos que escapavam à harmonia exigida.'

            '...podando os espigões teimosos [yellow]'os quais'[reset] escapavam à harmonia exigida.'

Pronome relativo retomando [yellow]'os espigões teimosos'[reset] e além disso seu consequente faz introduzir uma :
                                [blue]oração subordinada adjetiva restritiva[reset]

    [green]O pronome relativo 'que' é usado de forma correta.[reset]

    [red]Análise sintática:[reset]

    [blue]'...podando os espigões teimosos...'[reset] -> [red]oração reduzida no gerúndio[reset]
    [yellow]quem poda, poda algo:[reset] [blue]'os espigões teimosos'[reset] <- [red]Objeto Direto[reset]

    [blue]'...que escapavam à harmonia exigida.'[reset] -> 'que' é pronome relativo que introduz oração subordinada adjetiva restritiva
                            que caracteriza 'os espigões'.

    [yellow]Como saber o sujeito da oração subordinada?[reset]

            Substituir o pronome relativo pelo seu referente: [red]'os espigões':[reset]

                '... [red]os espigões escapavam à harmonia exigida.'[reset]

                [yellow]quem escapava à harmonia exigida?[reset] [red]'os espigões'[reset] -> [blue]SUJEITO[reset]

        Portanto, o pronome relativo 'que' usado na sentença possui a função sintátiva de SUJEITO.

        [yellow]Predicado da oração subordinada?[reset]

                [blue]'...escapavam à harmonia exigida.'[reset]
        [yellow]quem escapa, escapa de algo[reset]: [red]'à harmonia exigida.' <- Objeto indireto
            [yellow]'escapavam'[reset] -> [red]Verbo transitivo direto                        [reset]



c. '...sua voz não se entrelaçava à música distante [yellow]que[reset] vinha dos salões.'                                


	[red]O vocábulo 'que' introduz uma subordinação adjetiva restritiva para a oração principal caracterizando 'a musica distante'.[reset]

		[yellow]Podemos colocar:[reset] '...à música distante [blue]a qual[reset] vinha dos salões.'
		                	            Portanto, pronome relativo.

    [red] Análise sintática:[reset]                  


            [yellow]Oração Principal:[reset]

                [blue]'...sua voz não se entrelaçava à música distante...'[reset]
                
                   [red]quem que não se entrelaçava ?[reset] 'sua voz' <- [green]SUJEITO                      [reset]
                   'não' -> [red]Advérbio de negação[reset]
                   'se entrelaçava' <- [red]Predicado da oração principal ( verbo pronominal )[reset]
                   'se' -> [red]Pronome reflexivo[reset]
                   quem se entrelaça, se entrelaça a alguém: [red]( preposição 'a' + artigo 'a' -> Junção):[reset] 'à música distante' <- [blue]Objeto Indireto[reset]

            [yellow]Oração Subordinada:[reset]

                [blue]'...que vinha dos salões.'[reset] <- O pronome relativo 'que' retoma 'música', cuja característica dela 
                                            'que vinha dos salões'                   

d. '...disse o jardineiro a si mesmo [yellow]que[reset] já era tempo de ter uma companheira.'


        disse o jardineiro a si mesmo [yellow]ISSO[reset] -> [blue]ISSO[reset] [red]é subordinação [reset]
		quem é que disse? [blue]'o jardineiro'[reset] <- [red]Sujeito[reset]
		quem diz, diz algo: [yellow]'que já era tempo de ter uma companheira'[reset] <- [red]Objeto Direto[reset]

			Sendo assim, a oração subordinada é substantiva objetiva direta e o vocábulo 'que' é uma conjunção integrante.
		
        Além disso, o jardineiro disse algo, algo : [blue]a si mesmo ( com preposição ) [reset]-> [red]Objeto Indireto[reset]

        [red] Análise sintática:[reset]

            [blue]Oração Principal:[reset]

                [yellow]'...disse o jardineiro a si mesmo...'[reset]

                [red]quem diz, diz algo:[reset] a si mesmo <- [yellow]'a si mesmo' [reset]<- [red]Objeto direto[reset]
                [red]'disse'[reset] do verbo DIZER :[blue] transitivo indireto e direto[reset]
                [red]quem que disse algo a si mesmo?[reset] [yellow]'o jardineiro'[reset] <- Sujeito simples

            [blue]Oração Subordinada:[reset]

                [yellow]'...que já era tempo de ter uma companheira.'[reset] <- 'que' conjunção integrante que liga a subordinada à principal
                [green]o jardineiro além de dizer algo a si mesmo, disse também[reset][yellow] ISSO[reset] -> [blue]'que já era tempo de ter uma companheira.'[reset]
                                Portanto, a oração é subordinada substantiva objetiva direta.

                [yellow]A conjunção integrante é o SUJEITO ORACIONAL da oração SUBORDINADA.[reset]

                [yellow]'já era tempo de ter uma companheira'[reset] -> predicado da oração subordinada

                [yellow]'já'[reset] -> advérbio de tempo que possui a função sintática de Adjunto Adverbial de tempo, modificando o verbo 'SER' no
                                    pretérito imperfeito do indicativo na 3º pessoa do singular.                                    

                [yellow]'era' [reset]-> Verbo de ligação // [yellow]'tempo de ter uma companheira'[reset] -> Predicativo do sujeito     
                [yellow]'tempo'[reset] -> núcleo do predicativo.  
                [yellow]'de ter uma companheira'[reset] -> Complemento Nominal                             


        GABARITO LETRA 'D'

e. Já se fazia grande e frondosa a primeira árvore [yellow]que[reset] havia plantada naquele jardim...'        

Trocando o vocábulo [green]'que'[reset] por [yellow]'a qual'[reset], retomando o termo anterior que é feminino e singular temos:

					'... a primeira árvore [yellow]a qual[reset] havia plantado naquele jardim...'

			Portanto, é um pronome relativo. Não é o gabarito da questão.


         [red]Análise sintática:[reset]

            [blue]Oração Principal:[reset]

                'Já se fazia grande e frondosa a primeira árvore...'

            [yellow]'já'[reset] -> Advérbio que possui função sintática de Adjunto Adverbial de tempo, modificando o verbo 'fazia'

            [yellow]'se fazia'[reset] -> verbo pronominal reflexivo de ligação

            [yellow]'grande e frondosa'[reset] -> Adjetivos atribuidos ao sujeito exercendo a função sintática de predicativo de sujeito

            quem que havia plantada naquele jardim? [yellow]'a primeira árvore'[reset] <- [red]Sujeito simples[reset] ( núcleo -> 'árvore')

            
            [red]Oração Subordinada:[reset]

                '... que havia plantada naquele jardim.'

            [red]'que'[reset] -> pronome relativo que introduz a oração subordinada adjetiva restritiva

            [red]'havia plantada'[reset] -> Verbo na voz passiva analítica

            [red]'naquele jardim'[reset] -> Adjunto Adverbial de lugar 

Observação importante: problema verbal
A forma [yellow]“que havia plantada”[reset] está incorreta. Pela norma culta, o correto seria:

            [yellow]“que havia sido plantada”[reset]

Pois o verbo "plantar" está na voz passiva, e a forma “plantada” funciona como particípio passado que exige o verbo auxiliar “ser” + particípio.

✅ Portanto, a forma corrigida seria:

                "Já se fazia grande e frondosa a primeira árvore que havia sido plantada naquele jardim."

[red]Questão 04.[reset]

4. Foi na constituição de 1891 que, pela primeira vez, o MP mereceu uma referência no texto fundamental.

No primeiro período do terceiro parágrafom, o vocábulo 'que' introduz uma oração subordinada adjetiva restritiva.

CERTO ou ERRADO?

[red]Atenção![reset]

		Detalhe a ser observado:

				[bg_blue]Para ser adjetiva restritiva, a pontuação deve aparecer antes do pronome relativo![reset]

Portanto alternativa ERRADA.

Se o verbo 'foi' é retirado, e o vocábulo 'que' também, a leitura do texto continua coerente, vejamos:

			Na constituição de 1891, pela primeira vez, o MP mereceu uma referência no texto fundamental.

           [bg_red] O verbo 'foi' e o 'que' são elementos expletivos = partículas de realce.[reset]
				                [bg_red]Serve para enfatizar informações![reset]

Exemplo:

			[yellow]É[reset] o Elias [yellow]que[reset] é meu professor de português.

		Enfatizando o 'ELIAS', podendo retirar esses vocábulos:

			O Elias é meu professor de português.

		O verbo SER conjugado na 1º primeira pessoa do singular do presente do indicativo: 'É' é elemento expletivo.
				                Assim como o vocábulo 'que' não constituem na oração.


Portanto, não é uma oração subordinada adjetiva restritiva. ERRADO. Temos elementos expletivos de realce.

5. No segundo parágrafo, em - e CUJA largura, nesta era de rápidas transformações, se mede em anos-luz -, o termo destacado é um pronome relativo.
Considerando essa categoria de pronomes, assinale a alternativa que preenche, correta e respectivamente, a frase a seguir.

Infelizmente, vivemos em uma sociedade ____ ainda há crianças ______ dia a dia se limita ao esforço para enfrentar a miséria____elas sonham escapar.


a. onde...   a que o...com que
b. onde...   cujo...   com que
c. em que... cujo...   de que
d. de que... a que o...com que
e. de que... cujo...   de que


O pronome relativo [blue]'onde'[reset] retoma lugares, e [blue]'sociedade'[reset] não é lugar. Sendo assim, 'onde' não pode ser.
                                Elimina-se então as alternativas 'a', 'b'

Analisando o verbo 'viver'. quem vive, vive [yellow]EM[reset] algum lugar: 'em sociedade', portanto, podemos eliminar as alternativas 'd' e 'e'.
Sobrando a alternativa 'C'.

Continuando a próxima lacuna:

	...ainda há crianças [yellow]CUJO[reset] dia a dia <- [blue]Pronome relativo 'cujo' concordando com 'dia a dia'[reset] <- masculino e singular 
	                        ideia de posse = dia a dia das crianças ( são das crianças o dia a dia )

        [bg_blue]A regra gramatical determina que sua concordância é com o termo possuído (consequente), e não com o possuidor.[reset]

[red]Continuando a próxima lacuna:[reset]

... ao esforço para enfrentar a miséria ____ elas sonham escapar      

        [red]'elas'[reset] -> que retoma 'as crianças'

            [blue]quem escapa, escapa de algo[reset]: 'da miséria' ( preposição 'de' + artigo 'a' -> Junção ( contração ))
                                    [green]Sendo assim, 'de que' retoma 'da miséria'[reset]

[yellow]Infelizmente, vivemos em uma sociedade em que ainda há crianças cujo dia a dia se limita ao esforço para enfrentar [reset]
                                            [yellow]a miséria de que elas sonham escapar.[reset]                

[yellow]'infelizmente'[reset] -> Advérbio de modo ( função sintática de adjunto adverbial de modo ) modificando o verbo 'vivemos' com valor emocional.

quem que vive em uma sociedade? [blue]'nós'[reset] -> [yellow]sujeito oculto, elíptico ou desinencial[reset]
No contexto, o verbo viver tem o sentido de 'existir','estar'. Um verbo de estado. portanto é verbo intransitivo.
        Sendo assim não exige complemento verbal : [blue]'em uma sociedade'[reset] <- Adjunto Adverbial de Lugar
                        [red]( só que 'sociedade' não é lugar, nem substantivo concreto, é substantivo abstrato )[reset]
                                                Portanto, 'vivemos' é instransitivo.

Exemplo de transitividade do verbo VIVER:

    Vivemos grandes aventuras 

    O verbo tem o sentido de experimentar novas e grandes aventuras.
    quem vive, vive: 'grandes aventuras' <- Obejto Direto

                                                                       

[yellow]'em que'[reset] -> [blue]pronome relativo preposicionado ( retoma 'sociedade' em que liga ao seu consequente 'há crianças...') [reset]
                            [blue]introduzindo uma oração subordinada adjetiva restritiva[reset]

1º oração subordinada adjetiva restritiva:

[red]'em que ainda há crianças'[reset] -> 'em que' -> admite função sintática de adjunto adverbial de lugar
[red]'ainda'[reset] -> [yellow]Advérbio de tempo[reset] ( adjunto adverbial de tempo - alterando o verbo 'há' -> não admite sujeito )   
[red]'há'[reset] -> verbo haver no sentido de existir (impessoal) é transitivo direto -> ainda há, o que? 'crianças' <- [red]objeto direto [reset]
[red]'cujo'[reset] -> pronome relativo que retoma seu antecedente ( 'criança' ) e liga ao seu consequente ( 'dia a dia' ) -> [red]masculino e singular[reset]

            O pronome relativo 'cujo' introduz uma 2º oração subordinada adjetiva restritiva, caracterizando 'crianças'.

    quem se limita? 'o dia a dia' <- Sujeito da oração subordinada. ' se limita' -> verbo transitivo indireto pronominal reflexivo ( limitar-se a: )
    quem se limita, se limita a algo: [blue]'ao esforço para enfrentar a miséria...'[reset] <- [red]Objeto direto[reset] ( complemento verbal indireto do verbo pronominal reflexivo 'limitar-se') 

'para enfrentar a miséria' -> [blue]oração subordinda final ( finalidade )       [reset]

[yellow]'de que elas sonham escapar'[reset] -> Pronome relativo 'de que' introduzindo outra oração subordinada adjetiva restritiva caracterizando 'miséria'
                                            de que elas sonham escapar? 'da miséria'

[red]'de que'[reset] -> pronome relativo preposicionado que retoma 'da miséria' em que liga ao seu consequente 'elas'
[red]'elas'[reset] -> pronome pessoal do caso reto ('crianças')
[red]'sonham escapar'[reset] ->  Predicado verbal em que 'escapar' funciona como objeto direto do verbo 'sonham'

    quem sonha, sonha em : [blue]'escapar da miséria'[reset] <- [red]'da míséria'[reset] <- complemento verbal indireto
            portanto podemos inferir que a função sintática do pronome relativo 'em que' é de objeto indireto.

Questão 06.

Para a surpresa de muitas pessoas, acostumadas a ver em nosso país tantas leis [yellow]que[reset] não saem do papel, a LRF, 
logo nos primeiros anos, atinge boa parte de seus objetivos, notadamente em relação à observância dos limites da despesa com pessoal, 
o que permitiu uma descompressão da receita líquida e propiciou maior capacidade de investimento público. 
O regulamento marca avanços também no controle de gastos em fins de gestão e em relação ao novo papel [yellow]que[reset] as leis de diretrizes 
orçamentárias passaram a desempenhar.
	
	Os pronomes relativos 'que' e 'que' embora retomem elementos distintos do texto, desempenham a mesma função sintática nos 
                                                        períodos em que ocorrem.

	[red]fazendo a substituição por outro pronome relativo temos concordância retomada ao substantivo[reset][blue] 'leis'[reset] -> 
                                            [yellow]portanto é pronome relativo[reset]

    '...acostumadas a ver em nosso país tantas leis [yellow]as quais[reset] não saem do papel...'

    [red]Substituindo o pronome relativo pelo substantivo temos:[reset]

            [yellow]leis não saem do papel[reset]

            quem que não saem do papel?  [blue]'leis'[reset] <- [red]Sujeito[reset]

            [green]Portanto, o pronome relativo 'que' é sintaticamente 'sujeito'.      [reset]

[red]A outra frase:[reset]

    O regulamento marca avanços também no controle de gastos em fins de gestão e em relação ao novo papel [yellow]que[reset] as leis de diretrizes 
orçamentárias passaram a desempenhar.

         [red]Substituir por outro pronome:[reset]  '...ao novo papel [yellow]o qual[reset] as leis de diretrizes...' 
                            [yellow]O pronome relativo retoma 'papel'[reset] [green](o papel -> singular )[reset]


        quem é que [green]passaram a desempenhar [reset] um novo papel? [yellow]'as leis de diretrizes orçamentárias'[reset] <- [red]Sujeito[reset]
		O pronome relativo que retoma [blue]'um novo papel'[reset], quem passa a desempenhar, desempenha o que? [blue]'um novo papel'[reset] -> [red]Objeto Direto[reset]
			            Portanto, o pronome relativo 'que' possui a função sintática de [bg_blue]OBJETO DIRETO.[reset]

                [bg_red]'Cujo' indica ( retoma ) o possuidor (antecedente), mas concorda com o possuído (consequente).[reset]

                Sendo assim, os pronomes 'que' desempenham função sintáticas diferentes.

                [bg_blue]O primeiro 'que' é sujeito e o segundo 'que' é objeto direto.[reset]

[red]Questão 08. [reset]

Estamos geralmente tão hipnotizados pela 'necessidade de um compromisso para se alcançar o bem comum' e pela opinião de que 'as instituições sociais 
já estão fazendo todo o possível para isso', que não conseguimos perceber nossa contribuição na legitimação dessa política policial que administra 
alguns corpos e torna invisíveis outros.


O sentido original do texto seria alterado caso se inserisse uma vírgula imediatamente após a palavra 'policial'.


	Substituindo o vocábulo 'que' por um pronome relativo 'a qual' ficaria correto também:

    			'...nossa contribuição na legitimação dessa política policial [yellow]a qual[reset] administra...'
		Portanto o vocábulo 'que' é também um pronome relativo.
        

	Se é pronome relativo é sinal de que a oração é subordinada adjetiva, sem vírgulas, portanto é restritiva.
    
    Por isso, o sentido muda colocando a vírgula [bg_red]após[reset] da palavra 'policial' tornando-a uma subordinada adjetiva explicativa.

            [bg_red]Generalizando que toda a política policial administra corpos e torna visíveis outros.[reset]
		            
                    Já na restritiva, no texto original o sentido é que algumas políticas policiais administram.... 
			            ( classificada sintaticamente como oração subordinada adjetiva restritiva )

                    Portanto a questão está CORRETA em afirmar que o sentido original é alterado.

Questão 09.

Considere os dois períodos abaixo e assinale a alternativa correta.

I. Os meninos, que gostam de futebol, adoram as aulas de Educação Física.
II.Os meninos que gostam de futebol adoram as aulas de Educação Física.

a. O sentido é o mesmo nos dois períodos, pois o uso das vírgulas marca apenas a pausa na leitura.
b. Em I, há uma generalização, afirmando que todos os meninos gostam de futebol.
c. Em I, a vírgula separa, incorretamente, o sujeito e o verbo.
d. Em II, há erro de pontuação.                    


A diferença entre o item I e II é que no item I temos separação por vírgulas, portanto 'que gostam de futebol' é uma oração subordinada
			adjetiva explicativa. O sentido é outro: define os que [yellow]TODOS[reset] gostam de forma generalização.
            
No item II, 'que gostam de futebol' [blue]não está separado por vírgulas[reset] e portanto muda seu sentido ( semântica ) para uma oração
        			subordinada adjetiva restritiva [bg_red]( separando quem 'que gostam de futebol' dos outros )[reset]

Na alternativa 'A' o sentido não é o mesmo para os dois períodos, além de marcar a pausa, o seu sentido muda.

No item I, ocorre semanticamente uma generalização que todos os meninos gostam de futebol, separado por vírgula
			que por sua vez é uma oração subordinada adjetiva ( por ter um atributo dos meninos ) explicativa 
							             ( por ser separado por pontuação )

Sendo assim, a alternativa 'b' é a correta.

Na alternativa 'C':

Em I, não separa incorretamente o sujeito do verbo. Entre as vírgulas está a oração subordinada adjetiva explicativa.

Na alternativa 'D':

No item II não há erro de pontuação. Ocorre na gramática o que chamamos de oração subordinada adjetiva restritiva intercalada
			que por sua vez a oração principal é 'Os meninos (...) adoram aulas de Educação Física.

Questão 10.

Se, no lugar dos verbos destacados no verso 'Escolho os filmes que eu não vejo no elevador', fossem empregados, respectivamente, Esquecer e gostar,
a nova redação, de acordo com as regras sobre regência verbal e concordância nominal prescritas pela norma-padrão, deveria ser:

a. Esqueço dos filmes que eu não gosto no elevador.
b. Esqueço os filmes os quais não gosto no elevador.
c. Esqueço dos filmes do quais não gosto no elevador.
d. Esqueço dos filmes dos quais não gosto no elevador.
e. Esqueço os filmes dos quais não gosto no elevador.

Vamos analisar a frase do enunciado primeiro:

                    Escolho os filmes que eu não vejo no elevador


		quem escolhi, escolhi algo: [red]'os filmes'[reset] <- [yellow]Objeto direto[reset] ( complemento verbal do verbo 'escolher' -> Transitivo Direto )

        			[red]quem escolhe, escolhe algo![reset] [bg_red]E NÃO escolho DE ALGO[reset] <- CUIDADO! ( sem preposição )                    [reset]

        [red]Atenção![reset]

            Agora, quem esquece, esqueci algo: [yellow]'os filmes'[reset] -> [blue]Objeto direto[reset] -> [bg_blue]( sem preposição )[reset]

			Agora... quem [yellow]SE[reset] esqueci, [yellow]SE[reset] esqueci de algo. [bg_red]( com preposição 'DE'! )[reset]

                quem se esqueci, se esquece de algo: [yellow]'dos filmes'[reset] <- Mas somente com o pronome pessoal de caso oblíquo átono ( SE )
				                            ( Eliminando as alternativas A, C & D )

                            Escolho os filmes [yellow]que[reset] eu não vejo no elevador.

O vocábulo 'que' poderia ser substituido por 'os quais' retomando o seu referente que por sua vez é objeto direto 'os filmes' ( singular e plural)
		Sendo assim, o pronome relativo 'que' é também objeto direto e introduz uma oração subordinada adjetiva restritiva.


[red] Na oração principal:[reset]

            'Esqueço os filmes...'

[red]Na oração subordinada temos:        [reset]

            '...que eu não vejo no elevador.'

            quem que não vê? [blue]'eu'[reset] -> [red]Sujeito Simples da oração subordinada[reset]
            quem não vê, não vê algo: [yellow]'os filmes'[reset] <- [red]Objeto Direto[reset]
            [blue]'no elevador'[reset] -> [yellow]Adjunto Adverbial de lugar[reset]

            Agora substituindo o verbo por outro da oração subordinada:

            '...que eu não [yellow]gosto[reset] no elevador.'

            O verbo 'gostar' é transitivo indireto, quem gosta ou quem não gosta, não gosta [yellow]DE[reset] algo: '[bg_red]de[reset] filmes' <- Objeto Indireto
            Portanto, necessita de preposição para a transitiva indireta do verbo 'gostar', um complemento indireto.

                Sendo assim, seria correto afirmar: 

				Esqueço dos filmes [yellow]DE QUE[reset] eu não gosto no elevador.

                    [bg_blue]Por que o verbo precisa de complemento indireto obrigatório, ou seja, com preposição.[reset]

                    Sobraram as alternativas: 'B' e 'E'.

                    B. Esqueço os filmes [yellow]os quais[reset] não gosto no elevador.
                    E. Esqueço os filmes [yellow]dos quais[reset] não gosto no elevador.

Na alternativa 'B' está 'os quais' sem preposição. [bg_red]O verbo 'ver' precisa de preposição obrigatória, ele é transitivo indireto![reset]

Sobrando assim a alternativa 'E':

		Esqueço os filmes [yellow]DOS QUAIS[reset] não gosto no elevador. [green](  preposição 'DE' + artigo 'OS' -> Contração )[reset]

Questão.11

'Pois há uma única coisa [yellow]de que[reset] o próprio Deus está privado: fazer o que foi não tenha sido.'

A correção gramatical do texto seria preservada caso se eliminasse a preposição 'de'.

     	Podemos substituir por um pronome relativo preposicionado [yellow]'da qual'[reset]:

            'Pois há uma única coisa [yellow]DA QUAL[reset] o próprio Deus...'

       		[bg_red]Ou seja, o elemento é um pronome relativo introduzindo um oração subordinada adjetiva restritiva.[reset]

            		[blue]Portanto 'de que' é um pronome relativo preposicionado! [reset]

                    A preposição com o pronome relativo possui uma função sintática:

                    '... há uma única coisa [yellow]DA QUAL[reset] o próprio Deus está privado...'

                    [bg_red]O pronome relativo irá ligar uma oração a outra. O termo consequente sempre será regido pelo verbo[reset]
                            [bg_red]e o pronome relativo irá concordar em gênero e número com o termo antecedente.[reset]
                            
                    [yellow]"o próprio Deus”[reset] é o sujeito da oração subordinada, mas não tem relação de concordância com o pronome relativo.

                    O pronome relativo retoma “coisa”, que é o termo possuído ou retomado, e concorda com ele (fem. sing.).                            
                    
                    [red]'está'[reset] -> verbo de estado em que liga ao seu predicativo do sujeito 'privado'

                    'privado' é um substantivo derivado do verbo 'privar' portanto, necessita-se de um complemento NOMINAL.

                    [red]Ordem direta:[reset]

                    Já que sabemos que 'o próprio Deus' é o sujeito da oração...

                        O próprio Deus está privado de uma única coisa

                        quem está privado, priva de alguma coisa: [yellow]'de uma única coisa'[reset] -> [green]Complemento Nominal[reset]

           			quem é que está privado?? [red]'o próprio Deus'[reset] <- [blue]função sintática de Sujeito[reset]

           			[red]'está'[reset] -> verbo de estado que por sua vez então 'privado' é uma característica do sujeito.

		            Sendo assim, [blue]Predicativo do sujeito[reset] ( Privado é um adjetivo )

Portanto, a correção gramatical do texto não seria preservada caso se eliminasse a preposição 'de'.                    


        [bg_red]Gramaticalmente incorreto, pois violaria a regência verbal.[reset]

                [red]'estar privado'[reset] exige a preposição [red]'de'[reset]: quem priva, priva de alguma coisa: [yellow]Verbo transitivo indireto[reset]

                [red]ATENÇÃO! [reset]

                o SUBSTANTIVO 'PRIVADO' NECESSITA DE COMPLEMENTO PARA COMPLETAR O SENTIDO. A FRASE NÃO ESTÁ NA ORDEM DIRETA.
		Sendo assim o próprio Deus está privado de alguma coisa:

				[yellow]'DE UMA ÚNICA COISA'[reset] <- Complemento Nominal.

		[blue]Portanto, 'de que' ou 'da qual' possui função sintática de complemento nominal.[reset]

[red]Questão 11.[reset]

	Escolha mais adequada é empreender uma apropriação crítica desse passado político recente, tanto para consolidar nossa frágil cidadania
quanto para entender a realidade [yellow]em que vivemos[reset]. Para tanto, é fundamental estudar a ditadura, a fim de compreender a atualidade do seu legado e,
assim, criar condições de superá-lo.

	No trecho 'entender a realidade em que vivemos', a supressão da preposição não prejudica a correção gramatical do texto, ainda que interfira
na relação sintático-semântica entre seus elementos.

                [red]TESTES:[reset]


			    '... entender a realidade [yellow]NA QUAL[reset] vivemos.'

				Portanto, [yellow]'em que'[reset] é pronome relativo e retoma [yellow]'a realidade'.[reset]

                    Substituir o pronome pelo nome que o retoma com a preposição, seria:

                                    '...[yellow]na[reset] realidade vivemos...'

                quem é que vivemos? [blue]'nós'[reset] <- [yellow]Sujeito está OCULTO[reset]
                [yellow]'vivemos'[reset] -> [blue]Verbo intransitivo.[reset] [green]( significado de existir, estar, residir, morar )[reset]
                        [bg_blue]quem vive, vive em algum lugar... ( )[reset]
                vive [yellow]'na realidade'[reset] -> [blue]Adjunto Adverbial[reset] ( classificação: Sintagma Nominal )

                    Portanto, o pronome relativo preposicionado 'em que' possui função sintática de Adjunto Adverbial.

                    'na realidade ( em que nós ) vivemos'

                [red]Com a supressão 'em' ( preposição )[reset]
                
                    '...entender a realidade que vivemos.'

                    quem é que vive? [blue]'nós'[reset] -> [red]Sujeito Oculto[reset]
                            quem vive, vive algo: [blue]'a realidade'[reset] <- [red]Objeto Direto[reset]

                [green]Portanto o verbo agora passa a ser transitivo direto exigindo complemento direto![reset]

                	[bg_red]As duas sentenças são gramaticalmente válidas.[reset]

                    quem entende, entende algo: [blue]'a realidade'[reset]
                    [yellow]'que vivemos'[reset] ->  Oração subordinada adjetiva restritiva ( não é qualquer realidade, uma realidade que vivemos )

	As duas sentenças são gramaticalmente válidas.

		[blue]A diferença é a relação semântico-sintática.[reset]

	[red]Na sentença original[reset]: 'na realidade [blue]EM QUE[reset] vivemos, intendemos no contexto 'na realidade' -> [green]um sentido de lugar, um adjunto adverbial[reset]
					Veja que o verbo é até intransitivo. Mas exige preposição, indicando um lugar.
		
	Agora: 'intender a realidade [yellow]QUE[reset] vivemos'.[blue] O pronome relativo 'QUE' passa a ser um complemento direto do verbo VIVER[reset]
			Tendo assim outra relação sintática, dentro de outro contexto. Uma realidade vivida pelo SUJEITO, 'eu vi a realidade'
							                Uma visão específica do sujeito.


            Portanto, o item está CORRETO.

		[red]Atenção![reset]

		Um pronome relativo preposicionado, a preposição não pode ser eliminada e também não pode ser substituida por outra preposição.
                							Acarretando na mudança sintático-semântica.


[red]Questão 12.[reset]

	Cláudio, marido e imperador, esteve implicado nessas execuções. Não existem dúvidas de que lhe [yellow]diziam que[reset] determinado amante tramava contra ele
ou que outro desviava o dinheiro público, mas ele sempre [yellow]fazia o que[reset] a mulher lhe pedia e logo se livrava daqueles homens.

	O vocábulo 'que', em 'diziam que' e em 'fazia o que', pertence a classes gramaticais distintas.

    [red]Resolução da questão:[reset]

    Não existem dúvidas de que lhe [yellow]diziam que[reset] determinado amante...'

    Não existem dúvidas de que lhe diziam [yellow]DISSO[reset]. [yellow]DISSO[reset] o que? [blue]'de que lhe diziam que determinado amante...'[reset]
            [yellow]DISSO[reset] -> [blue]Oração subordinada substantiva objetiva indireta.[reset]

                Portanto, 'que' é uma conjunção integrante.

        '...mas ele sempre fazia o [yellow]que[reset] a mulher lhe pedia...' ->             

        '...mas ele sempre fazia [yellow]o ISSO??[reset]  [red]NÃO né...[reset] => [blue]( o vocábulo 'o' não pode ser desconsiderado )[reset]

                quem faz, faz algo: [blue]'...o que a mulher lhe pedia...'[reset] <- [red]Oração subordinada[reset]

         O 'o' não é artigo. A palavra que está depois é um pronome.  Para ser artigo, deveria ser seguido de um substantivo.

         			'o' que não é artigo, pode ser [blue]PRONOME.[reset]

		No lugar do 'o', colocar o pronome demonstrativo [blue]AQUILO.[reset]

        			'...mas ele sempre fazia [yellow]aquilo o qual[reset] a mulher lhe pedia...'

   			[bg_blue]Portanto, o 'o' funciona como pronome demonstrativo e o 'que' como pronome relativo.[reset]                    

		Assim, CERTO, pertencem a classes gramaticais distintas. [green]'diziam que' <- o 'que' é conjunção integrante.[reset]
					            e [green]'fazia o que'. o 'que' é pronome relativo.[reset]

[red]Questão 13.[reset]

	Pode-se dizer que a engenharia científica só teve início quando se chegou a um consenso de que tudo aquilo que se fazia em bases empíricas
e intuitivas era, na realidade, regido por leis físicas e matemáticas, que importava descobrir e estudar

	A flexão de singular na forma verbal 'importava' justifica-se por ser o sujeito da oração indeterminado, de interpretação genérica.

		[blue]O enunciado esta querendo dizer que o verbo 'importava' possui sujeito indeterminado.[reset]

        Para ser [yellow]SUJEITO INDETERMINADO:[reset]

	[red]1[reset]. [blue]Verbo na 3º pessoa do plural sem referente textual[reset]
	[red]2[reset]. [blue]Verbo na 3º pessoa do singular + SE ( indice de indeterminação do sujeito )[reset]
	[red]3[reset]. [blue]Infinitivo Impessoal[reset]

    		O verbo 'importava' não está na 3º pessoa do plural.
	    	O verbo 'importava' está na 3º pessoa do singular, porém não exite partícula SE.
    		O verbo 'importava' não está no infinitivo impessoal.

       		Obs: O verbo 'importava' está no pretérito imperfeito do indicativo ( -AVA )

            	[red] Portanto, o sujeito não é indeterminado. [reset]

		'...,regido por leis físicas e matemáticas , [yellow]que[reset] importava descobrir e estudar.'

		'...,regido por leis físicas e matemáticas , [yellow]as quais[reset] importava descobrir e estudar.'

        			[yellow]'as quais'[reset] <- pronome relativo que retoma -> [red]'leis físicas e matemáticas' (plural)[reset]

        			[bg_red]o verbo 'importava' está no singular, logo, o pronome relativo não pode ser SUJEITO.[reset]

	Substituindo o pronome relativo 'que' pelo seu referente temos:

    		'... [yellow]leis físicas e matemáticas[reset] importava descobrir e estudar.'

		[red]Ordem direta:[reset]

				descobrir e estudar leis físicas e matemática importava

			quem que importava? [blue]'descobrir e estudar leis físicas e matemáticas'[reset] <-[red] Sujeito oracional // Sujeito verbal[reset]

				[bg_red]Os verbos que possuem sujeito oracional só podem ficar SINGULAR.[reset]
                						Mesmo sendo composto.

  		quem descobre, descobre algo // quem estuda, estuda algo: [blue]'leis físicas e matemáticas'[reset] <- [red]Objeto Direto          [reset]
        
GranQuestões
Questão 14.

Ano: 2025 / Prova: Instituto Consulplan - TJ RO - Técnico Judiciário Pós-Edital - 2025 - 4º Simulado

No trecho do texto “Célia diz que veio para o Reino Unido com uma ‘ilusão’”, a oração destacada desempenha a função de:

A. Oração subordinada substantiva completiva nominal.
B. Oração subordinada substantiva objetiva direta.
C. Oração subordinada substantiva predicativa.
D. Oração subordinada substantiva subjetiva.
E. Oração subordinada substantiva apositiva.


'Célia' -> Sujeito Simples // quem diz, diz algo: ...[yellow]'que veio para o Reino Unido com uma ilusão.'[reset]

Célia diz [yellow]ISSO[reset] <- [yellow]ISSO[reset] o que? -> '...[yellow]que[reset] veio para o Reino Unido...' <- A conjunção integrante 'que' introduz uma oração subordinada substantiva objetiva direta.

"Ir" é um verbo intransitivo. //  Mesmo quando vem seguido de expressões como “para o mercado”, “ao trabalho”, “à escola”,
o verbo não exige um objeto – exige apenas um adjunto adverbial de lugar, que completa o sentido circunstancial da ação, 
mas não é exigido como complemento essencial do verbo.

"para" é preposição. Mas não é a presença da preposição que define se o verbo é transitivo indireto ou não.

O verbo ir, assim como vir, chegar, partir, é intransitivo.

🧩 Termos como “para o Reino Unido” são adjuntos adverbiais de lugar, mesmo que introduzidos por preposição.

❌ Não são objetos indiretos, portanto o verbo não é transitivo indireto.

 [yellow]'...para o Reino Unido...'[reset] <- [red]Adjunto Adverbial de lugar[reset]
[red]'com uma ilusão'[reset] <- [blue]Adjunto Adverbial de modo[reset] <- Adicionando uma circunstância ao verbo de ir para um lugar...


A Oração Subordinada Substantiva Objetiva Direta (OSSOD) funciona como objeto direto de um verbo transitivo direto na oração principal. 
É introduzida por conjunção integrante (que) ou pronome interrogativo (quem, o que, qual).

Para identificar uma OSSOD, encontre o verbo transitivo direto na oração principal e pergunte "o quê?" ou "quem?".

Questão.15.

Ano: 2025  / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRO AL - Analista de Comunicação - 2025 

A Justiça fez buscas nas contas bancárias do dentista, e encontrou R$ 887,74, que foram bloqueados.

Na linha 10, em “que foram bloqueados”, aparece a subordinada adjetiva restritiva. conjunção coordenativa explicativa “que”.

C.Certo 
E.Errado

A questão está correta em dizer que é uma oração subordinada adjetiva restritiva. Já que a [yellow]explicativa[reset] é separada por vírgulas.
	Mas é separada pela pontuação após o pronome relativo 'que' que introduz esse tipo de oração subordinada. E não antes 
O 'que' não é conjunção coordenativa [yellow]explicativa[reset], elas introduzem orações subordinadas [yellow]explicativas[reset] e não coordenadas.


	A vírgula antes da conjunção aditiva 'e' é facultativa.
	A segunda vírgula introduz uma explicação.

[red]Análise do período:[reset]

    	Repare que temos mais de 2 verbos, sendo assim período composto mas por coordenação e não por subordinação.

	Repare que temos mais de 2 verbos, sendo assim período composto mas por coordenação e não por subordinação.
		As orações subordinadas uma oração depende da outra sintaticamente por meio de complementos verbais, sujeitos ou adjuntos...
	No determinado contexto , cada oração tem seu sentido completo, sem depender uma da outra e são ligadas pela conjunção aditiva 'e' 
							que por sua vez é coordenativa sindética aditiva.

	Quando uma oração tem autonomia sintática e ligadas pela conjunção coordenativa 'e' é um período composto por coordenação.

	[yellow]A Justiça fez buscas nas contas bancárias do dentista, e encontrou R$ 887,74, que foram bloqueados.[reset]

   	[blue]'A justiça'[reset] -> Sujeito simples
	[blue]'fez'[reset] verbo [blue]FAZER[reset] -> [green]Ele fez[reset] -> 3º pessoa do singular do presente de indicativo
	 quem fez, fez algo: [blue]'buscas'[reset] <- Objeto Direto
	[blue]'buscas'[reset] -> substantivo abstrato derivado do verbo 'buscar'
	[blue]'nas contas bancárias'[reset] <- Complemento nominal
	 quem é que pratica a ação de buscar? -> [blue]'A justiça'[reset] [red](não as contas)[reset] -> 'as contas bancárias' são o alvo paciente da busca.

        Resumo prático para esse tipo de questão:

        		✔️ [blue]Complemento nominal[reset]: paciente ou alvo de substantivo abstrato. ( adjetivos, advérbios e substantivos abstratos )
			✔️ [blue]Adjunto adnominal[reset]: possuidor, agente, qualidade. ( substantivos concretos e abstratos )

        2º Oração:

            	'..., [yellow]e[reset] encontrou R$ 887,74,...' <- Oração coordenada sindética aditiva

           	quem encontra, encontra algo: [blue]'R$ 887,74'[reset] <- Objeto Direto // [blue]'encontrou'[reset] -> [red]'ele encontrou'[reset] -> 3º pes. singular -> pretérito perfeito do indicativo
		[yellow]( O pretérito perfeito é uma ação concluida no passado )[reset] O modo indicativo expressa certeza do fato, afirmação objetiva.

            Sujeito dessa oração está OCULTO.

   		3º oração: subordinada adjetiva explicativa:

       			[yellow]'..., que foram bloquados.'[reset] <- [blue]Repare que está separados por pontuação.[reset] ( vírgula e ponto final -> Portanto, explicativa )

                [red]Observação:[reset]

                [yellow]'que'[reset] é pronome relativo que introduz a oração subordinada e retoma [yellow]'R$ 887,74'[reset].
                                    [bg_blue] Seu consequente está na voz passiva analítica.[reset]

                [red]Voz passiva analítica:[reset]

        			Verbo auxiliar + verbo no particípio:

		        	Verbo auxiliar: [blue]'foram' ( verbo SER )[reset]
			            Particípio: [blue]'bloqueados'[reset]

                [red]Comparando com a voz passiva sintética:[reset]

                    	A voz passiva sintética usa pronome apassivador “se” com verbo transitivo direto:
            				- Exemplo: [yellow]Bloquearam-se os valores.[reset] → Aqui temos uma forma sintética.

              		Substituindo o pronome pelo seu antecedente temos:

                			[yellow]'...R$ 887,74 foram bloqueados.'[reset]

				quem que foram bloqueados? [yellow]'R$ 887,74'[reset] <- Portanto, sujeito

			[bg_blue]Sendo assim, o pronome relativo 'que' admite-se função sintática de SUJEITO da voz passiva analítica 'foram bloqueados'.[reset]

Questão.16
Língua Portuguesa  Orações subordinadas adverbiais comparativas / Ano: 2025
Banca: Instituto de Administração e Tecnologia - ADM TEC / Prova: ADM&TEC - Prefeitura de João Alfredo - Tratorista - 2025 

Na frase: "Hassan, o menino de lábio leporino [yellow]que corria atrás das pipas como ninguém"[reset], qual é a classificação da oração sublinhada?

A. Oração subordinada substantiva subjetiva.
B. Oração subordinada substantiva objetiva direta.
C. Oração subordinada adverbial comparativa.
D. Oração subordinada adjetiva restritiva.


	'... [yellow]que[reset] corria atrás das pipas como ninguém.' 

		Substituindo por um pronome relativo:

		Hassan, o menino de lábio leporino [yellow]o qual[reset] corria atrás das pipas como niguém.'

- O pronome relativo “o qual” deve concordar com o antecedente em gênero (masculino/feminino) e número (singular/plural).
- Neste caso, o antecedente é "o menino", que é masculino e singular.

		Portanto, o 'que' é pronome relativo e introduz uma oração subordinada adjetiva restritiva.
			Qualificando e restringindo o substantivo 'menino', especificando qual o menino Hassan.

Alternativa correta "D".

Análise da alternativa 'A':

Oração subordinada substantiva subjetiva?

		Não é substantiva subjetiva por que o sujeito da oração principal já está definido como 'HASSAN'.

Análise da alternativa 'B':

Oração subordinada substantiva objetiva direta?

		Não é substantiva objetiva direta por que não há objeto direto de um verbo na oração.

Análise da alternativa 'C':

Oração subordinada adverbial comparativa?

Não é uma oração subordinada adverbial comparativa, pois não estabelece uma comparação entre duas ações ou qualidades. 
					A oração está qualificando o substantivo 'menino'.


Questão.17
Ano: 2025 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Nonoai - Professor - Área: Língua Portuguesa - 2025

Qual é a classificação da oração sublinhada no trecho abaixo?

Após uma sequência de frentes frias, [yellow]que amenizaram as temperaturas principalmente no Centro-Sul[reset], o tempo deve voltar a esquentar em boa parte do Brasil. 
A partir desta quinta-feira, uma nova massa de ar quente deve se instalar na região central, fazendo com que as temperaturas voltem a subir.
Fonte: G1 (julho de 2024).


A. Oração subordinada adverbial condicional.
B. Oração subordinada adjetiva restritiva.
C. Oração subordinada adjetiva explicativa.
D. Oração subordinada adverbial consecutiva.


	O pronome relativo [yellow]'que'[reset] retoma [blue]'as frentes frias'[reset] ( plural e feminino ) e introduz uma oração subordinada.

        Substituindo por outro pronome:

	'Após uma sequência de frentes frias, [yellow]as quais[reset] amenizaram...' <- Portanto, é pronome relativo.
		Separado por pontuação, caracteristica  das frentes frias, portanto, subordinada adjetiva explicativa.

[red]Análise da alternativa 'A':[reset]

	Não pode ser uma oração subordinada adverbial condicional.
Orações subordinadas adverbiais condicionais expressam uma condição, geralmente introduzidas por conjunções como 'se', 'caso', 'contanto que'. 
Neste caso, a oração introduzida por 'que' está explicando uma característica das frentes frias, não uma condição. 

        Não é a alternativa 'A' o gabarito da questão.

[red]Análise da alternativa 'B':[reset]

	Não é uma oração subordinada adjetiva restritiva. Orações subordinadas adjetivas restritivas especificam ou restringem o significado do antecedente 
sem a presença de vírgulas. No trecho, a oração está entre vírgulas, indicando que se trata de uma explicação adicional sobre as frentes frias, não uma restrição.

[red]Análise da alternativa 'C':[reset]

	[bg_green]CORRETA[reset]

	 é uma oração subordinada adjetiva explicativa. Este tipo de oração fornece uma informação adicional sobre o antecedente, que neste caso são as 'frentes frias', 
e está entre vírgulas, o que é característico das orações explicativas.

[red]Análise da alternativa 'D':[reset]

	Não é uma oração subordinada adverbial consecutiva. Orações subordinadas adverbiais consecutivas expressam uma consequência e são introduzidas 
por conjunções como 'tanto que', 'de forma que'. A oração em questão está explicando uma característica das frentes frias, não uma consequência. 

Questão.18
Ano: 2025 / Banca: Objetiva Concursos / Prova: Objetiva Concursos - Prefeitura de Rio Negro - Auditor Tributário - 2025 

Assinalar a alternativa em que os termos sublinhados representam uma oração subordinada substantiva completiva nominal:


A. Tenho saudade [yellow]do que vivemos.[reset]
B. Não gosto [yellow]dessas brincadeiras que vocês fazem.[reset]
C. Ela me convenceu [yellow]de que estou errado.[reset]
D. Todos querem [yellow]que você seja feliz.[reset]


A questão aborda o tema das orações subordinadas substantivas completivas nominais, que são aquelas que completam o sentido de um nome, 
geralmente um substantivo abstrato, que exige complemento. Essas orações são introduzidas por conjunções integrantes, como 'que' ou 'se'.


[red]Análise das afirmativas:[reset]


	Tenho saudade [yellow]do que vivemos.[reset]

	A oração subordinada substantiva completiva nominal é introduzida pela preposição 'de', que é exigida pelo substantivo 'saudade'.

	[yellow]'tenho'[reset] -> [blue]Verbo transitivo direto[reset] -> [yellow]'saudade'[reset] <- Objeto direto ( complemento verbal )
				Sujeito oculto -> [yellow]Eu[reset]

	[yellow]'...do que vivemos.'[reset] <- Complemento nominal do substantivo abstrato 'saudade' <-
			Sujeito oculto da oração subordinada -> [yellow]'nós'[reset] -> '...do que [blue](nós)[reset] vivemos.'

Dica prática:

✔️ Se houver antecedente (expresso ou subentendido) → pronome relativo
✔️ Se não houver antecedente → conjunção integrante

[yellow]'do que'[reset] -> preposição 'de' + artigo 'o' + pronome relativo 'que' <-[blue] quem sente saudade, sente saudade DE algo. [reset]
	[yellow]'o que'[reset] - > pronome demonstrativo + pronome relativo => [blue]'o'[reset] -> [yellow]aquilo[reset]
		[yellow]'do que vivemos'[reset] retoma algo subentendido -> [green]'...aquilo que vivemos.'[reset]

	Sendo assim, vivemos o quê? [blue]'vivemos aquilo que...'[reset] <- [yellow]'aquilo que'[reset] <- Objeto Direto do VTD 'vivemos'

[red]Análise da alternativa 'B':[reset]

			Não gosto [yellow]dessas brincadeiras que vocês fazem.[reset]

	[red]Oração Principal:[reset]

		'Não gosto dessas brincadeiras...'

		quem não gosta, não gosta de algo: [blue]'dessas brincadeiras[reset] ( preposição 'de' + pronome demonstrativo 'essas' -> Contração ) <- [red]Objeto Indireto[reset]
		[red]'não'[reset] -> Advérbio de negação // [green]função sintática de adjunto adverbial[reset]

	[red]Oração Subordinada:[reset]

		'...que vocês fazem.'

		[red]'que'[reset] <- Pronome relativo que retoma 'brincadeiras' e introduz uma oração subordinada adjetiva restritiva ( adicionando um atributo as brincadeiras )

		[red]'vocês'[reset] <- sujeito da oração subordinada

		[red]'fazem'[reset] -> [blue]Verbo transitivo direto[reset] // fazem o que? [blue]'brincadeiras'[reset] -> Substantivo retomado pelo pronome relativo 'que'
					[bg_blue]Sendo assim, o pronome relativo 'que' é objeto direto do verbo fazem...[reset]

        [red]Atenção![reset]

            [bg_red]O texto sublinhado é parte oração principal e parte subordinada para confundir o candidato.![reset]
                                   [bg_red] Não é o gabarito da questão.[reset]                    
            A oração subordinada que a questão pedi é: [yellow]'...que vocês fazem.'[reset] e não [yellow]'...dessas brincadeiras que vocês fazem.'[reset]                                 

			[bg_red]Atenção! [reset]
			Se fosse substantiva completiva nominal, seria 'Não gosto [yellow']DISSO...'[reset] 
			Cuidado que para substituir por um substantivo genérico [yellow]'DISSO'[reset] é somente no vocábulo 'QUE', e não no termo sublinhado na questão.

[red]Análise da alternativa 'C':[reset]

                    Ela me convenceu [yellow]de que estou errado.[reset]

         [red]Oração principal:[reset]

		        'Ela me convenceu...' 

	        [red]Sujeito explícito:[reset] [blue]'Ela'[reset] <- [green]3° pessoa do singular[reset] <- Pronome pessoal do caso reto.

            Pronomes pessoais do caso reto:

- Representam as pessoas do discurso e exercem a função de sujeito na oração.
| Pessoa do discurso | Singular | Plural | 
| 1ª pessoa |           eu |       nós | 
| 2ª pessoa |           tu |       vós | 
| 3ª pessoa |           ele / ela | eles / elas | 

            	quem se convence, convence de algo: [yellow]'de que estou errado.'[reset] <- [red]Objeto indireto[reset]
            		Ela se convenceu [yellow]DISSO[reset] -> [blue]Oração substantiva objetiva indireta[reset]
		            [green]'convenceu'[reset] ->[red] Verbo transitivo indireto e direto[reset]
		            quem convence, convence alguém: [yellow]'me'[reset]-> [blue]Objeto direto do verbo 'convencer' ( pronome oblíquo átono )[reset]

       	 [red]Oração subordinada:[reset]

		        '...de que estou errado.'

                	[yellow]'de que'[reset] -> [blue]Conjunção integrante preposicionada [reset]( somente liga uma oração a outra )
                                    Introduz orações subordinadas substantivas

                	[yellow]'estou'[reset]  -> verbo de estado // [yellow]'errado'[reset] -> Predicativo do sujeito ( atributo ao sujeito 'ela' )

	[red]O termo em destaque é uma oração subordinada substantiva objetiva indireta. Exercendo função sintática de objeto indireto do verbo 'convencer'.[reset]
	[red]Não é o gabarito da questão.[reset]  [blue] O termo 'de que' é uma conjunção integrante preposicionada, introduzindo a oração subordinada substantiva Ob.In.[reset]

[red]Análise da alternativa 'D':[reset]                    


		Todos querem [yellow]que você seja feliz.[reset]

	[red]Oração principal:[reset]

		[yellow]'Todos querem...'[reset] // Todos querem o que? [blue]'que você seja feliz'[reset] <- [red]Objeto Direto[reset]
			[yellow]'querem'[reset] -> [red]Verbo transitivo direto[reset]

		todos quem? [yellow]'eles'[reset] <- [blue]pronome pessoal do caso reto ( 3º pessoa do discurso )[reset] <- [red]Sujeito oculto, elíptico ou desinencial[reset]

	[red]Oração Subordinada:[reset]

            '... que você seja feliz.'

		Portanto, o 'que' é conjunção integrante. Ligando a oração principal a oração subordinada.

		[red]'você'[reset]  -> Sujeito explícito da oração subordinada
		[red]'seja'[reset]  -> verbo na 1º pessoa do presente do subjuntivo que sintaticamente funciona como verbo de ligação.
		[red]'feliz'[reset] -> adjetivo que funciona sintaticamente como predicativo do sujeito. ( atributo do sujeito )

	[red]O termo em destaque é uma oração subordinada substantiva objetiva direta. Exercendo função sintática de objeto direto do verbo 'querer'.[reset]
									[red]Não é o gabarito da questão.[reset]

[red]Questão.19[reset]        

Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - EMBRAPA - Pós Edital - Conhecimentos Básicos. - 2025 - 1º Simulado

No trecho “Recebi uma carta da escola em que ele estudava que chamou a atenção para um comportamento muito parecido com alguns sintomas 
típicos do autismo” (segundo parágrafo),
A oração “que chamou a atenção para um comportamento muito parecido com alguns sintomas típicos do autismo” 
é subordinada adjetiva explicativa, pois fornece uma informação adicional sobre o antecedente “uma carta”.

C.Certo
E.Errado

Recebi uma carta da escola em que ele estudava [yellow]que chamou a atenção para um comportamento muito parecido com alguns sintomas típicos do autismo.[reset]

[red]Oração Principal:[reset]

	    'Recebi uma carta da escola...'

Verbo 'receber'. quem recebi , recebi algo: [blue]'uma carta da escola em que ele estudava que chamou a atenção para um comportamento muito parecido...'[reset] <- [red]Ob. Direto[reset]        

      	[red]substantivo concreto[reset] -> [blue]uma carta[reset] <- Objeto direto
		[red] Eu [reset] -> Sujeito Oculto ( elíptico ou desinencial )
        
         [red]'da escola'[reset] -> [blue]Adjunto Adnominal[reset] [green]( indica origem da carta)[reset] Referindo-se ao substantivo 'carta'.

		 	[red] recebi [reset] -> verbo transitivo direto ( VTD ) // quem recebe, recebe algo: [blue]'uma carta'[reset] <- Objeto Direto
		[red]Atenção![reset]	

			[yellow]'da escola'[reset] -> Indica a origem da carta, portanto, adjunto adverbial de lugar/origem em que refere ao verbo.

	[red]2º oração subordinada:[reset]         

    	[yellow]'...em que ele estudava...'[reset] ->[blue] Subordinada Adjetiva restritiva[reset] ( restringindo o substantivo )

	Substituindo por um pronome relativo:

		'...[yellow]a qual[reset] ele estudava...' <- Portanto, [yellow]'em que'[reset] é pronome relativo preposicionado que retoma 'escola'.

		[red]Queremos dizer:[reset]

			[blue]'na escola ele estudava'[reset] 
            
            [red]Ordem direta:[reset] [yellow]'Ele estudava na escola'[reset] <- 'na escola' <- [red]Adjunto Adverbial de lugar[reset]

		Sendo assim:
	
			O pronome relativo preposicionado na 2º oração admite função sintática de Adjunto Adverbial de lugar

			'ele' -> Sujeito
			'estudava' -> Verbo intransitivo ( não há complementos ) 

				[red]Atenção a transitividade do verbo 'estudar'.[reset]

		quem estuda, estuda algo -> [yellow]Objeto Direto[reset]  
		quem estuda, estuda em algum lugar -> [yellowExigindo a preposição 'em' para expressar	circunstância de lugar.[reset]
	
		Sendo assim ele continua sendo intransitivo nesse contexto.
		[yellow]Porque o termo "em algum lugar" funciona como adjunto adverbial de lugar, não como objeto indireto.[reset]

📌 Exemplo:
Ele estuda na escola.

[red]Verbo[reset]: estuda → [red]intransitivo[reset]

[yellow]"na escola"[reset] = [blue]adjunto adverbial de lugar[reset]

[yellow]"na"[reset] = em + a → [blue]preposição + artigo[reset] -> Contração

[red]Tipo de termo:[reset]			
Objeto indireto	[yellow]"O quê?" ou "a quem?"[reset] com preposição	
Adjunto adverbial	[yellow]Onde? Quando? Como?[reset] (Ele estuda na escola -> "na escola" ->	Adjunto adverbial)


	    [red]3º oração subordinada adjetiva restritiva:[reset]

		[yellow]'... que chamou a atenção para um...'[reset] <- O que chamou a atenção? [yellow]'A carta'[reset] -> feminino e singular

                [bg_red] Portanto, não é qualquer carta, e sim uma carta que chamou a atenção [reset] [bg_blue]( restringindo a carta )[reset]

   		Substituindo por um pronome relativo: '[yellow]a qual[reset] chamou a atenção..' <- Portanto, é pronome relativo ( sem preposição )

        	[red]Substituir o pronome pelo nome retomado:[reset]

			'[yellow]A carta[reset] chamou a atenção...'  
    		[blue]quem que chamou a atenção?[reset] [yellow]'A carta'[reset]

			[yellow]'A carta'[reset] -> Objeto direto, portanto o pronome relativo admite a função sintática de [yellow]OBJETO DIRETO.[reset]
			Que por sua vez introduz a oração sub.

		    O verbo chamar pode ser transitivo direto e indireto. No caso do indireto, exige preposição: 'de'
			Geralmente antecedido do objeto direto -> Aquilo que recebe o nome. Ao nome dado 'de' alguma coisa.

			Exemplo:

			Chamaram o menino de gênio.
				→ "o menino" = objeto direto
				→ "de gênio" = objeto indireto

				Agora quando chama para algo, em algum lugar, está introduzindo um complemento expressionário. ( adjunto adverbial )


	        quem chama, chama [algo/alguém] [para] algo/alguma coisa [blue]'a atenção'[reset] <- [red]Objeto Direto[reset]

            			[bg_blue]Portanto, o verbo 'chamar' é transitivo direto e indireto, no contexto.[reset]

	[red]Análise sintática dos objetos do verbo:[reset]     

			'...para um comportamento muito parecido com alguns sintomas típicos do autismo.' <- [blue]Objeto Indireto[reset]                   

            '...para um comportamento...' -> Objeto Indireto. // '...muito parecido' -> [blue]Adjunto Adnominal[reset] 

			'...com alguns sintomas típicos do autismo.' -> [blue]Complemento Nominal[reset] ( 'com' é preposição )			
		
 
O adjunto adnominal modifica o substantivo concreto ou abstrato.
O complemento nominal modifica o substantivo abstrato, adjetivo ou advérbio.

O adjunto adnominal pode vim preposição ou não. Já o Complemento Nominal sempre terá preposição.
A função do adjunto adnominal caracteriza, especifica e determina o substantivo.
O complemento nominal completa o sentido.
A relação com o substantivo do Adjunto Adnominal é ativa ( POSSE -> AGENTE )
O complemento nominal tem uma relação com o substantivo de PASSIVA ( possuido -> PACIENTE )

		Núcleo do predicado: alguns sintomas..
	        [yellow]'sintomas típicos do autismo'[reset] <- [blue]'do autismo'[reset] <- [green]Adjunto Adnominal[reset]
    		[yellow]'sintomas'[reset] <- Substantivo abstrato + 'típicos' -> Adjetivo para o substantivo. [red]Portanto[reset]: [blue]Adjunto Adnominal[reset]

	[red]Sendo assim:[reset]

		[yellow]'do autismo'[reset] -> [blue]Indica a origem ( os sintomas pertencem ao quadro de autismo, 'do autismo' possui os sintomas )[reset] <- [blue]Adj.Adnominal[reset]

[red]Questão.20[reset]
Ano: 2025 / Banca: COSEAC / Prova: COSEAC - SEAP RJ - Inspetor de Polícia Penal Pós-Edital - 2025 - 4º Simulado

Na oração “O jornalismo, que submetido a um Código de Ética que entende o ‘acesso à informação pública como um direito inerente à condição de vida em 
sociedade’“, a oração subordinada introduzida por 
[yellow]“que entende o ‘acesso à informação pública como um direito inerente à condição de vida em sociedade’“[reset]
classifica-se como:

A. oração subordinada adjetiva explicativa.
B. oração subordinada substantiva objetiva direta.
C. oração subordinada adjetiva restritiva.
D. oração subordinada substantiva completiva nominal.
E. oração subordinada adverbial causal.        

	[red]Oração Principal:[reset]

	O jornalismo, 'que (é) submetido a um código de ética' <- predicado ( verbo elíptico )
	[yellow]'O Jornalismo'[reset] -> [red]Sujeito[reset]

	[red]Oração Subordinada:[reset]

	'...que é submetido a um Código de Ética.'

				Podemos substituir o vocábulo 'que' por um pronome relativo:

		O jornalismo, [yellow]o qual[reset] é submetido a um código de ética.

		Portanto, o [yellow]'que' [reset]é um pronome relativo que retoma [yellow]'jornalismo' [reset]-> [blue]Sujeito da oração principal e que introduz uma oração subordinada.[reset]

	[red]2º Oração Subordinada:[reset]

	'... que entende o ‘acesso à informação pública como um direito inerente à condição de vida em sociedade.'

	Podemos substituir o vocábulo [yellow]'que'[reset] por um pronome relativo: [yellow]'o qual'[reset]

		'... a um código de ética [yellow]o qual [reset]entende o acesso à informação...

	Pronome relativo [yellow]'que'[reset] retoma [yellow]'código de ética'[reset], sendo assim podemos substituir o termo retomado no lugar do pronome:

		[red]'...código de ética[reset] entende o acesso à informação...'

			quem é que entende o acesso à informação??? -> [yellow]Código de ética [reset]-> [red]SUJEITO [reset]
	Sendo assim, o pronome relativo admite-se função sintática de SUJEITO da oração subordinada que por sua vez introduz uma oração subordinada.

	[red]verbo: [reset][yellow]'entende' [reset]-> quem entende, entende algo: [red]'o acesso à informação pública' [reset]<- Complemento verbal direto do verbo transitivo direto 'entender'.

	que por sua vez temos um complemento do objeto direto:

		[yellow]'...como um direito inerente à condição de vida em sociedade.'[reset] <- [red]Predicativo do objeto direto[reset]

	[yellow]'o acesso à informação pública..'[reset] -> [red]'à informação pública' [reset]é complemento nominal da palavra [yellow]'acesso'.[reset]
            						Por que a informação é acessada [red]( PACIENTE )[reset]


Não há objeto indireto aqui.
➡️ Verbo entender = VTD + predicativo do objeto, com objeto direto composto por “acesso” + seu complemento nominal.

Por que não é COMPLETIVA NOMINAL?

Classificação correta:

✔️ Não é completiva nominal porque:

Não completa o sentido de um nome abstrato (Código de Ética).

Está qualificando, explicando, especificando o antecedente “Código de Ética”.

➡️ Ou seja:

✔️ É uma oração subordinada adjetiva restritiva que:

Tem função adjetiva (equivale a “Código de Ética que possui tal característica”).

Não exerce função nominal, mas sim atribui uma característica ao substantivo antecedente.


[red]Questão 21.[reset]
Ano: 2025 / Banca: Instituto Quadrix - Quadrix / Prova: Quadrix - CRO AL - Analista Financeiro - 2025 

As chapas, para dar forma ao automóvel, foram cortadas no laboratório que ele montou nos fundos da [blue]casa[reset] [yellow]onde mora[reset], em Cachoeira Paulista.

A oração “onde mora” (linha 24) é uma oração subordinada adjetiva restritiva.

C. Certo
E. Errado

[red]Termos essenciais da oração:[reset]

	[blue]Sujeito e Predicado[reset]

	[blue]Sujeito[reset] -> [yellow]'As chapas...' [reset]
	[blue]Predicado[reset] -> [yellow]'...foram cortadas no laboratório que ele montou nos fundos da casa onde mora, em Cachoeira Paulista.'[reset]
				[red]Predicado verbal:[reset] [yellow]'foram cortadas'[reset] <- [blue]verbo na voz passiva analítica [reset]
[green]( verbo auxiliar + particípio (voz passiva analítica))[reset]

	[red]Oração Principal:[reset]

		As chapas (...) foram cortadas no laboratório.

		[red]'no laboratório'[reset] -> [blue]Adjunto Adverbial de lugar[reset]

[red]Termos integrantes e acessórios:[reset]

	[blue]1º oração subordinada adverbial final: Reduzida no infinitivo[reset]

		-> '...para dar forma ao automóvel..' <-
		[blue]Oração Subordinada adverbial final[reset] -> [green]Indicando a finalidade da ação 'de cortar as chapas'.[reset]

	[blue]'para'[reset] -> conjunção adverbial de finalidade // [bg_red]A oração completa está reduzida no infinitivo[reset]

[bg_blue]O verbo está no infinitivo, sem flexão de tempo e pessoa, não exige sujeito.[reset]

	Para que a oração seja desenvolvida teríamos que flexionar o verbo : [bg_red]( além disso, a locução prepositiva adverbial 'para que' é mais comum )[reset]

	'... [yellow]para que dessem [reset]forma ao automóvel...' -> [green]'dessem'[reset] -> [blue]Pretérito imperfeito do subjuntivo na 3º pessoa do plural[reset]

        '... [yellow]para que se desse[reset] forma ao automóvel." -> [green]'desse'[reset]  -> [blue]Pretérito imperfeito do subjuntivo na 3º pessoal do singular[reset]

	[red]'...se desse'[reset] <- voz passiva sintética com pronome apassivador 'se' [bg_blue]( 'forma' é objeto direto que vira sujeito paciente na passiva )[reset]
				A voz passiva sintética -> [bg_blue] -> (V.Transitivo + “se” apassivador + sujeito paciente).[reset]
		
			'... [yellow]para que se desse[reset] forma ao automóvel."

	[blue]Reescrevendo na voz passiva analítica:[reset]
		✔ [red]Ativa:[reset]para dar forma ao automóvel... ( reduzida no infinitivo ) <- 'forma' é objeto direto do VTD 'dar'
		
			✔ [red]Voz Passiva analítica:[reset] para que [yellow]a forma fosse dada[reset] ao automóvel. ( desenvolvida )
					[bg_red]verbo auxiliar + verbo no particípio + Sujeito paciente[reset]
				[green]'fosse'[reset] -> Verbo auxiliar (SER) -> Pretérito imperfeito do subjuntivo -> 3º pessoa do singular
					[green]'dada'[reset]  -> particípio do verbo DAR, concordando com o sujeito 'a forma'.
						[green]'a forma'[reset] -> Sujeito Paciente -> [red]Recebe a ação[reset]	

	

	[blue]2° oração subordinada:[reset]

	'... no laboratório [yellow]que[reset] ele montou nos fundos da casa onde mora, em Cachoeira Paulista.'

	'... no laboratório [yellow]no qual[reset] ele montou...' -> Portanto, [yellow]'que'[reset] é pronome relativo que retoma [yellow]'laboratório' [reset]
	
		[blue]'...que ele montou...'[reset] -> [yellow]'que'[reset] retoma apenas o núcleo 'laboratório', não a preposição.
			[bg_red]O pronome relativo “que” substitui apenas o substantivo núcleo do termo anterior.[reset]

[bg_blue]Logo na oração subordinada o verbo “montar”[reset] = [yellow]VTD (quem monta, monta algo)[reset] // [yellow]Objeto direto[reset] = [red]que (laboratório)[reset]
				
		Sendo assim, não é qualquer laboratório, é onde ele montou nos fundos da casa onde mora.
	Portanto, oração subordinada adjetiva restritiva [blue]( adicionando informações e restringindo o local 'laboratório' )[reset]

	'... nos fundos da casa onde mora...' <- [blue]Adjunto Adverbial de lugar[reset]

	[blue]3º oração subordinada:[reset]

	'...nos fundos da [yellow]casa[reset] onde mora...
	[yellow]'onde mora'[reset] -> [blue]'onde'[reset] -> Pronome relativo ( relaciona a lugares ) e deve retomar o termo (nome) anterior -> [bg_red]RETOMA 'CASA'[reset]
        Queremos dizer: 'Casa onde [red](ele)[reset] mora' -> Podemos inferir que o pronome relativo 'onde' possui a função sintática de Adjunto Adverbial de lugar		
		[red]'mora'[reset] -> Verbo intransitivo // [red]'ele'[reset] -> [blue]Sujeito Elíptico[reset]
	
		Sendo assim, não é qualquer casa, é onde ele mora. Portanto, oração subordinada adjetiva restritiva.
	
	[yellow]'... em Cachoeira Paulista'[reset] -> [blue]Adjunto Adverbial de lugar[reset]

Sendo assim, a alternativa está correta:
A oração subordinada adjetiva "onde mora" restringe o significado do termo antecedente "laboratório", 
especificando que se trata do laboratório que ele montou nos fundos da casa onde mora, e não de qualquer outro laboratório.

Questão 22.

Ano: 2025 / Banca: Instituto de Desenvolvimento Social e Tecnologia - IDESG
Prova: IDESG - Prefeitura de Itapemirim - Agente Comunitário de Saúde - 2025

No trecho "A quantidade de crianças e adolescentes [yellow]que exerciam trabalho infantil no país[reset] caiu para 1,6 milhão em 2023", a oração sublinhada é classificada como:

A. Subordinada adjetiva restritiva.
B. Subordinada adjetiva explicativa.
C. Subordinada substantiva predicativa.
D. Subordinada substantiva completiva nominal.

Para certificar que o pronome 'que' exerce, basta substituir por outro equivalente. 

	'A quantidade de crianças e adolescentes [yellow]as quais[reset] exerciam trabalho...'

	Portanto, [yellow]'que'[reset] é pronome relativo e introduz oração subordinada adjetiva restritiva. [red]( restringindo a quantidade de crianças e adolescentes )[reset]

	[yellow]'A quantidade de crianças e adolescentes...'[reset] -> [red]Sujeito Composto[reset] 
		[yellow]'A quantidade'[reset] <- [blue]núcleo[reset] // [blue]'A'[reset] -> Artigo determinante que exerce função sintática de Adjunto Adnominal 
	// [yellow]'de crianças e adolescentes'[reset] <- [red]Complemento Nominal[reset]

	[blue]	Predicado é verbal:[reset]

	[red]'exerciam'[reset] -> [yellow]verbo transitivo direto[reset] -> quem exerce, exerce algo: [yellow]'trabalho infantil'[reset] <- Objeto Direto // [yellow]'no país'[reset] -> [blue]Adjunto Adverbial de lugar[reset]

	[red]Predicado:[reset]
		
			[red]'caiu'[reset] -> (verbo intransitivo) [blue]( sua natureza é intransitiva, não exige complemento )[reset]
			// [red]'para 1,6 milhão'[reset] -> Adjunto Adverbial de finalidade / limite / resultado
							 // [red]'em 2023'[reset] -> Adjunto Adverbial de tempo


[bg_red] Portanto a alternativa correta é a 'A'.[reset]

[red]Questão 23.[reset]

Ano: 2025 / Banca: FACET Concursos - FACET / Prova: FACET - Prefeitura de Pedro Velho - Professor - Área: Língua Portuguesa - 2025
Identifique qual dos períodos abaixo possui uma oração subordinada substantiva completiva nominal:


A. Eu estava desejando doce mais cedo.
B. O mais importante é vencer o jogo.
C. Não te liguei porque estava ocupada.
D. Nosso desejo é te ver feliz!
E. Temos fé de que a humanidade pare de destruir o planeta.


						                	[yellow]Eu estava desejando doce mais cedo.[reset]

	[red]Período simples:[reset]	

	[red]'Eu'[reset] -> [yellow]Sujeito Simples[reset] // [red]Predicado:[reset] [yellow]'estava desejando doce mais cedo.'[reset] <- [blue]Termos essencias[reset]
	[red]'estava desejando'[reset] -> locução verbal ( verbo auxiliar 'estava' + verbo principal nominal 'gerúndio') -> 1 núcleo verbal ( predicado verbal )
	[red]'estava'[reset] -> [blue]pretérito imperfeito do indicativo ( 1º pessoa do singular )[reset] + [blue]verbo de ação contínua no passado/habitual ( predicado verbal )[reset]

Você pode identificar um predicado verbo-nominal quando:

- Há um verbo indicando ação ou estado e algo que caracteriza o sujeito (adjetivo ou expressão equivalente)

Mesmo que o verbo auxiliar seja um verbo de estado (estar), ele está auxiliando a formação de uma locução verbal com sentido principal de ação 
				[bg_red](o núcleo do predicado é sempre o verbo principal).[reset]
		quem deseja, deseja algo: [blue]'doce'[reset] -> [red]Objeto direto[reset] // [blue]Termo integrante:[reset] Objeto direto 
			   	[red]'mais cedo'[reset] -> [blue] adjunto adverbial de tempo [reset] -> [blue]( termo acessório )[reset]
	[red]Classificação do predicado:[reset] Predicado verbo-nominal ( Há predicativo do sujeito ou objeto )

[red]Predicado verbal:[reset]

[yellow]Tem como núcleo um verbo significativo (de ação ou processo), não há predicativo do sujeito ou objeto.	[reset]

[red]Predicado nominal:[reset]

Tem como núcleo um nome (predicativo), e o verbo é de ligação.(antes)

[red]Predicado verbo-nominal:[reset]

[red]Possui dois núcleos:[reset] [yellow]um verbo significativo (ação)[reset] + [yellow]um predicativo (do sujeito ou objeto).[reset]

				[red]Sendo assim, não há subordinação. Não é a afirmativa correta.[reset]


[red]Alternativa 'B'[reset]					

										[yellow]O mais importante é vencer o jogo.[reset]


	[red]Período simples:[reset] há somente 1 verbo na oração principal. E esse é de ligação ainda, nem de ação é.
	
	[red]Sujeito:[reset] [blue]'O mais importante...' [reset]-> [red]Sujeito Simples [reset] -> ( núcleo do sujeito -> [yellow]'importante'[reset] ) [blue]( termo essencial )[reset]
	- Determinado por artigo (o) e intensificado por advérbio (mais) -> [green]Adjunto Adnominal e Adjunto Adverbial de intensidade [reset] [red]( TERMOS ACESSÓRIOS )[reset]

	[red]Predicado:[reset] -> [blue]'...é vencer o jogo.'[reset] [blue]( Termo essencial )[reset]
	[blue]Verbo 'SER'[reset] -> Conjugado na 1º pessoa do singular 'Ele é' do presente do indicativo.

	Na gramática, após um verbo de ligação deverá haver (na sintaxe) um predicativo do sujeito atribuindo uma qualidade/ essência ao sujeito.

	[red]Classificação do predicado:[reset]
	
	[yellow]'é'[reset] -> [green]Verbo de ligação [reset]
	[red]'vencer o jogo'[reset] -> predicativo do sujeito [yellow]( oração subordinada predicativa reduzida no infinitivo )[reset]
	O verbo [yellow]"vencer"[reset] está no [green]infinitivo impessoal[reset] [yellow]( sem conjugação, sujeito indefinido ou genérico )[reset]
				 e tem como complemento [yellow]"o jogo"[reset] -> [blue](objeto direto).[reset]


	[red]O predicado nominal [reset]-> temos um verbo de ligação e uma atribuição ao sujeito.

Dentro do predicativo do sujeito (quando é uma oração reduzida), o núcleo permanece sendo a expressão principal que atribui significado ao sujeito.
Não podemos inferir que o predicado é verbo-nominal, pois não há verbo significativo na oração principal + predicativo do sujeito ou do objeto.


Orações subordinadas substantivas desenvolvidas geralmente são introduzidas por conjunções integrantes, como "que", "se", etc. 
[yellow]No entanto, quando temos verbos no infinitivo, ocorre o fenômeno das orações subordinadas substantivas reduzidas.[reset]

Desempenha papel de predicativo do sujeito, explicando ou caracterizando [yellow]"O mais importante".[reset]

É uma oração subordinada substantiva predicativa porque desempenha função nominal de [blue](predicativo do sujeito). [reset]
Por isso o predicado é nominal [yellow]( verbo de ligação + predicativo ).[reset]
É reduzida porque o verbo está no infinitivo impessoal, e não conjugado pessoalmente.
É subordinada por que depende sintaticamente da outra oração, a principal. Ela não tem sentido completo sozinha.


[red]Equivalência com oração desenvolvida:[reset]

[yellow]"O mais importante é que se vença o jogo."[reset] <- [red]Oração subordinada substantiva predicativa desenvolvida[reset]

Aqui, temos uma oração subordinada substantiva predicativa desenvolvida, introduzida pela conjunção integrante "que".

	[yellow]Que exerce a função de predicativo do sujeito "O mais importante".[reset]
	
		[red]Análise sintática da oração desenvolvida:[reset]

	[red]Núcleo do sujeito da oração subordinada desenvolvida:[reset] 
	[blue]'se'[reset] <- [green]Pronome apassivador[reset] -> [red]Índice de indeterminação do sujeito[reset]
		[blue]'o jogo'[reset] -> [red]Objeto direto[reset] -> Sofre a ação expressa pelo verbo [blue]( SUJEITO PACIENTE )[reset]
		[blue]'vença'[reset] -> [red]presente do subjuntivo[reset] -> Voz passiva sintética

Na oração subordinada "que se vença o jogo", não há um sujeito ativo explícito. 
Isso ocorre porque a oração está na voz passiva sintética, onde a partícula apassivadora "se" é usada junto com o verbo para indicar
que o sujeito ("o jogo") é o receptor da ação, não o executor.		

[red] Voz passiva analítica [reset]

		'....o jogo foi vencido por alguém.' -=> [yellow]Verbo auxiliar (ser/estar) + particípio do verbo principal + agente da passiva[reset]

[red]Possível transformação para voz ativa sintética:[reset]

"O mais importante é que [blue]alguém[reset] vença o jogo."

Aqui, o [yellow]"alguém"[reset] funciona como sujeito agente na oração subordinada, que passou a voz ativa sintética.

[red]Transformar para a voz passiva analítica:[reset]

O sujeito da voz ativa passa a ser o agente da passiva, introduzido pela preposição 'por.'
O objeto direto da voz ativa passa a se tornar o sujeito paciente da passiva.
O verbo principal torna-se uma locução verbal formada pelo verbo auxiliar ser + particípio passado do verbo principal.

Entretanto, a oração subordinada predicativa com verbo no subjuntivo e sujeito indeterminado não permite uma transformação literal 
tradicional para a voz passiva analítica dupla com agente explícito sem mudar o sentido da frase.

Transformação aproximada para voz passiva analítica:
"O mais importante é que o jogo seja vencido por alguém."

"O jogo" é o sujeito paciente da oração subordinada. ( Era objeto direto na passiva sintética)

"seja vencido" é o verbo no presente do subjuntivo na voz passiva analítica (verbo "ser" no subjuntivo + particípio "vencido").

"por alguém" indica o agente da passiva (indeterminado).

Resumo:
"vencer o jogo" é uma oração subordinada substantiva predicativa reduzida de infinitivo, que funciona como predicativo do sujeito.

A ausência da conjunção ocorre porque esta é uma forma reduzida.
Quando usada desenvolvida, a oração viria com a conjunção "que" ou similar.

	[red]				Sendo assim, não é a alternativa correta.[reset]



						               [yellow] Não te liguei porque estava ocupada.[reset]


	[red]Oração Principal:[reset]

		'Não te liguei...'

	[red]Sujeito da oração principal:[reset] [blue]'EU'[reset] <- [green]Elíptico, oculto, desinencial [reset]
	[red]'não'[reset] -> [blue]Advérbio de negação[reset]
	[red]Quem liga, liga para algúem: [reset] para 'te' // [red]Sendo assim, o verbo [reset]'ligar' [red]é transitivo indireto.[reset]
	[red]Quem liga, liga para alguém, liga a alguém:[reset] [yellow]'te'[reset] -> [green]complemento verbal indireto [reset]( pronome pessoal oblíquo átono )
	[yellow]'liguei'[reset] -> [yellow]Pretérito perfeito do indicativo [reset] - [blue]( ação concluida no passado )[reset]
	[red]Predicado da oração principal:[reset] [blue]VERBAL.[reset] Tem como núcleo um verbo significativo de ação, transitivo. ( verbo: 'liguei' )
		

	[red]Oração Subordinada:[reset]

		[yellow]'...porque estava ocupada.'[reset] <- [red]'porque' introduz uma oração subordinada adverbial causal[reset]

	[red]Sujeito da oração subordinada:[reset] [blue]Elíptico[reset] // [red]Predicado da oração subordinada:[reset] [blue]Nominal[reset]
	[yellow]'porque'[reset]  -> conjunção subordinativa causal ( introduz a oração )
	[yellow]'estava'[reset]  -> Verbo ESTAR na 1º pessoa do singular no pretérito imperfeito do indicativo 
				[blue]( sintaxe: verbo de estado, funciona como verbo de ligação )[reset]
	[yellow]'ocupada'[reset] -> atribuição ao sujeito. Portanto, predicativo do sujeito.
		
		[red]Sujeito da oração subordinada:[reset]  - [blue]Elíptico, oculto ou desinencial [reset] [red]( EU )[reset]

		[red]Predicado da oração subordinada:[reset] [yellow] - [blue]NOMINAL[reset] [green]( verbo de ligação + predicativo do sujeito )[reset]

			
					[bg_red]Há período composto por subordinação. Mas não é a substantiva nominal.[reset]
								[bg_red]Portanto, não é questão correta.[reset]


		
							            	Nosso desejo é te ver feliz!

	[red]Período simples:[reset]
	
	[red]Oração principal:[reset]

		[yellow]'Nosso desejo'[reset] -> Sujeito <- [blue]Termo essencial da oração [reset]
			
		[red]núcleo do sujeito[reset] -> [yellow]'DESEJO'[reset]

	[yellow]Adjunto Adnominal[reset] -> [red]'nosso'[reset] [blue]( Determina o sujeito pelo pronome possessivo adjetivo )[reset]
	
	[yellow]'...é te ver feliz!'[reset] <- Predicado da oração principal

	[yellow]'é'[reset] -> verbo SER na 3º pessoa do singular do presente do indicativo a qual liga a oração principal à oração subordinada reduzida.

	[yellow]'te ver feliz'[reset] -> Predicativo do sujeito que por sua vez é classificada como uma oração subordinada substantiva predicativa reduzida no infinitivo.
			[blue]Núcleo da oração reduzida:[reset] 'ver' -> [red]Verbal[reset] // 
			Não está introduzida por conjunção, está sendo introduzida por em verbo de no infinitivo pessoal.

	quem vê, vê alguém: [red]'te'[reset] <- [blue]Pronome pessoal oblíquo átono[reset] , equivale a [yellow]'ver você'[reset] [red]( funciona como objeto direto )[reset]
	[red]'ver'[reset]   -> [blue]verbo transitivo direto[reset]
	[red]'feliz'[reset] -> [blue]adjetivo , atribuindo uma qualidade ao pronome 'te', que por sua vez é complemento do objeto direto chamado de predicativo do objeto.[reset]
	[red]'feliz'[reset] -> [blue]Predicativo do objeto[reset]

					O Predicado é nominal [blue](verbo de ligação + predicativo do sujeito )[reset]

	Nosso desejo é [yellow]ver-te[reset] feliz! -> Também está correto. [blue]ênclise facultativa.[reset] [green]( Pronome posposto ao verbo )[reset]
	Nosso desejo é [yellow]te ver[reset] feliz! -> Também está correto. [blue]próclise facultativa[reset] [green]( Pronome anteposto ao verbo)[reset]		
	
	A próclise seria obrigatória se houvesse uma palavra atrativa antes do verbo, como advérbio ou preposição, pronome e conjunções.

					            
								Temos fé de que a humanidade pare de destruir o planeta.

	
	[red]Oração Principal:[reset]

	[red]'(Nós) Temos fé...'[reset] -> quem que tem fé? [blue]'Nós'[reset] -> Sujeito oculto, elíptico ou desinencial.
	[red]'Temos fé...'[reset] -> [blue]Predicado[reset]
		[red]'temos'[reset] -> verbo transitivo direto -> [yellow]tem o que?[reset] [blue]'fé'[reset] -> [green]Objeto Direto[reset]

	Podemos substituir o vocábulo preposicionado [yellow]'de que'[reset] por [yellow]'da qual'[reset] para certificar se é pronome relativo ou conjunção integrante.
		
	'Temos fé [red]da qual[reset] a humanidade pare...' -> [bg_red]Não ficou legal.[reset]
				 Portanto, trata-se de uma conjunção integrante preposicionada.
			[bg_red]Conjunção integrante preposicionada introduz orações subordinadas substantivas[reset]

	[red]Termos essenciais da oração principal:[reset]

	[red]Sujeito da oração principal:[reset]
		
		[blue]'Nós'[reset] -> [red]Sujeito Oculto[reset]
		[blue]'...temos fé'[reset] -> [red]Predicado verbal[reset]
		[blue]quem tem, tem algo:[reset] [yellow]'fé'[reset] -> [yellow]Objeto Direto[reset] [red]( termo integrante )[reset]

	[red]Termos essenciais da oração subordinada:[reset]

	Temos fé [yellow]DISSO, DISSO[reset] o quê?

		'...de que a humanidade pare de destruir o planeta.' -> Oração Subordinada Substantiva Completiva Nominal
	A oração possui função sintática de [yellow]COMPLEMENTO NOMINAL[reset] da oração principal 

	Substantiva por que refere-se à um nome 'fé' e é substituido por um substantivo genérico 'disso'.
	Completiva Nominal por que está completando o termo 'fé'.	


	[blue]'a humanidade'[reset] -> [red]Sujeito[reset] <- Termo essencial da oração subordinada	subs. completiva nominal
	
	[blue]'...pare de destruir o planeta.'[reset] -> [red]Predicado verbal[reset] <- Verbos de ação
		
		O verbo [red]'pare'[reset] é transitivo indireto -> '[blue]...de destruir o planeta'[reset] -> [red]Objeto indireto[reset]
		
	[red]'destruir'[reset] -> verbo no infinitivo -> [red]'o planeta'[reset] -> [blue]Objeto Direto[reset]		


A oração "de que a humanidade pare de destruir o planeta" exerce a função de complemento nominal, pois:

- Completa o sentido do substantivo fé, que é abstrato.
- Está ligada por preposição ("de").
- Pode ser substituída por "disso": substantivo genérico
		
			Temos fé [yellow]DISSO.[reset]

				Portanto, trata-se de uma oração subordinada substantiva completiva nominal.
							Sendo a alternativa CORRETA.

[red]Questão 24.[reset]
Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - TRT 10 - Técnico Judiciário - Área: Administrativa Pós-Edital - 2025 - 1º Simulado

No trecho “Disse-me que, dobrando à esquerda, além do cemitério, havia casa cercada de árvore” (terceiro parágrafo), 
a oração “que, dobrando à esquerda, além do cemitério, havia casa cercada de árvore” é uma oração subordinada substantiva completiva nominal, 
pois complementa o termo “Disse-me”.

C.Certo
E.Errado	

	Disse-me [yellow]ISSO[reset] -> quem diz, diz algo, diz [yellow]ISSO[reset] -> [yellow]'...que, dobrando à esquerda, além do cemitério, havia casa cercada de árvore.'[reset]
	[red]Portanto, é uma oração subordinada substantiva objetiva direta.[reset]
	quem diz, diz algo a alguém: [yellow]'me disse'[reset] -> [red]'me' pronome pessoal do caso oblíquo átono funciona sintaticamente como objeto indireto.[reset]
		Também pode ser : [yellow]Disse a mim.'[reset] <- [blue]Objeto Indireto[reset]
		
		Queremos dizer: [blue]'(Ele)[reset] me disse [yellow]ISSO...'[reset]

		[red]Termo essencial:[reset] [blue]Sujeito oculto[reset]
		[red]Termo essencial:[reset] [blue]Predicado [reset] -> 'Disse-me que havia casa cercada de árvore.' [green]( Predicado verbal )[reset]

	  Portanto, a questão está ERRADA em afirmar que é completiva nominal, não completa nome nenhum e sim complementa um verbo.
		[yellow]Só que o objeto direto é substituido por um substantivo genérico. Substituido por ISSO. Sendo subordinada substantiva.[reset]
					Portanto, é uma subordinada substantiva objetiva direta.

[red]De qualquer forma, iremos fazer uma análise sintática completa:[reset]


	O pronome relativo 'que' introduz a oração subordinada objetiva direta.
	A oração principal é: [yellow]'Disse-me...' ou 'Ele me disse...'[reset]
	[red]Sujeito oculto:[reset] [blue]'(ELE) me disse[reset] ou [blue]'disse a mim'[reset] // quem diz, diz alguma coisa: [yellow]'à mim'[reset] -> [yellow]Objeto indireto[reset]

	[red]Oração Subordinada Substantiva Objetiva Direta:[reset] -> [blue]'...que, dobrando à esquerda, além do cemitério, havia casa cercada de árvore.'[reset]

	[red]3º oração:[reset] -> [blue]'...dobrando à esquerda...'[reset] <- [green]Oração reduzida de gerúndio com valor adverbial, sendo assim, Adjunto Adverbial de lugar.[reset]

		[red]Verbo no gerúndio de ação:[reset] [yellow]'dobrando'[reset] -> [blue]Introduzindo uma oração reduzida no gerúndio subordinada adverbial[reset]
		[yellow]'à esquerda'[reset] -> [green]locução adverbial de lugar[reset]
		[red]Sujeito da oração subordinada:[reset] '(Ele)' -> [red]Oculto[reset]
		[red]Predicado: 'dobrando à esquerda...'[reset] <- [red]O termo todo é adjunto adverbial de lugar[reset]

	[yellow]'...além do cemitério...'[reset] <- [blue]Adjunto Adverbial de lugar[reset]

	[red]4º oração:[reset]

		'... havia casa cercada de árvore.'

	[red]'havia'[reset] -> [yellow]verbo impessoal transitivo direto[reset] [blue](não possui sujeito)[reset]
	Predicado da oração subordinada: [yellow]Verbo-nominal [reset] -> [blue]( verbo de significado + predicativo )[reset]
	[red]'casa cercada de árvore'[reset] <- [yellow]objeto direto [reset]( complemento do verbo HAVER ) e [red]'cercada de árvore'[reset] -> [yellow]Predicativo do objeto[reset]

	[red]Oração subordinada substantiva objetiva direta:[reset]

	Disse-me [yellow]ISSO[reset] -> [yellow]ISSO[reset] o quê...
	
		'... havia casa cercada de árvore.'

			

[red]Questão 25.[reset]

Ano: 2025  / Banca: Ministério da Defesa - Marinha - ComDN / Prova: ComDN - Marinha - Oficial Pós-Edital - 2025 - 2º Simulado

Em "O amor se mantém o mesmo apenas para aqueles que se mantêm os mesmos", a estrutura sintática revela a presença de uma oração subordinada. 
Sobre essa oração, analise as afirmativas abaixo e marque a alternativa correta:


A. Trata-se de uma oração subordinada adverbial concessiva, pois estabelece uma ideia de contraste em relação à oração principal.
B. A oração subordinada presente no período é substantiva predicativa, pois atua como predicativo do sujeito da oração principal.
C. Identifica-se uma oração subordinada adverbial causal, que explica a razão de o amor se manter o mesmo.
D. A oração subordinada é adjetiva restritiva, qualificando o termo “aqueles” e especificando a quem a ideia se aplica.
E. Trata-se de uma oração subordinada substantiva completiva nominal, pois complementa o sentido de um nome presente na oração principal.


	
				O amor se mantém o mesmo apenas para aqueles que se mantêm os mesmos.

	[red]Devemos fazer uma análise sintática:[reset]

[red]Termos essenciais da oração:[reset]

	[red]Oração principal: [reset]
	
	'O amor se mantém o mesmo apenas para aqueles...'

	[red]Sujeito[reset] -> [blue]'O amor'[reset]  -> núcleo 'amor' // Artigo 'o' -> Adjunto Adnominal
	[red]Verbo[reset] -> [blue]'se mantêm'[reset] -> verbo pronominal reflexivo 
	Aqui “manter-se” é um verbo pronominal, ou seja, o pronome “se” faz parte do verbo, não é objeto.
Verbo pronominal: aquele que exige o pronome reflexivo ou que o inclui em seu significado, sem exercer função sintática autônoma de objeto direto ou indireto.

	[red]'o mesmo'[reset] -> Característica atribuida ao sujeito, o substantivo 'amor' -> [yellow]Predicativo do sujeito[reset]

Compare:

Manter algo (VTDI)

Ex: Eu mantenho meu filho alimentado.

'mantenho': verbo transitivo direto // 'meu filho': objeto direto // 'alimentado': predicativo do objeto

	Predicado nominal -> verbo de ligação + predicativo ( se mantêm o mesmo apenas para aqueles )

	[red]Termos integrantes e acessórios:[reset]

		[yellow]'... apenas para aqueles...'[reset] -> [blue]Adjunto Adverbial de restrição ou finalidade[reset]

	[blue]Oração subordinada:[reset]

	[yellow]'aqueles que se mantêm os mesmos.'[reset] -> [red]substituindo por um outro pronome[reset] -> '... aqueles [yellow]os quais[reset] se mantêm os mesmos.'
	
	Portanto, o [yellow]'que'[reset] é um pronome relativo que retoma [yellow]'aqueles'[reset] que exerce função de [yellow]SUJEITO[reset] da oração subordinada.
		
		Para verificar, devemos substituir o pronome pelo nome retomado: [yellow]AQUELES[reset]

				[yellow]'...aqueles[reset] se mantêm os mesmos.' // quem se mantêm os mesmos?  [yellow]'aqueles'[reset] -> [red]Sujeito[reset]

	O pronome relativo 'que' exerce função de sujeito da oração subordinada.

			Além também de introduzir uma oração subordinada adjetiva restritiva.

	[yellow]'...se mantêm os mesmos.'[reset] ->  verbo pronominal reflexivo intransitivo ( manter-se ) // 'os mesmos' -> predicativo do sujeito
o pronome “se” faz parte do verbo, não é objeto.
Verbo pronominal: aquele que exige o pronome reflexivo ou que o inclui em seu significado, sem exercer função sintática autônoma de objeto direto ou indireto.

	[yellow]Predicado da oração subordinada:[reset] [blue]NOMINAL[reset] -> [red]Verbo de ligação[reset] + [red]predicativo[reset] (se mantêm os mesmos )


	Portanto, a afirmativa correta é a:

D. A oração subordinada é adjetiva restritiva, qualificando o termo “aqueles” e especificando a quem a ideia se aplica.
	
[red](A) Errada.[reset] - Não se trata de uma oração adverbial concessiva, pois não há ideia de contraste.

[red](B) Errada.[reset] - A oração subordinada não desempenha a função de predicativo do sujeito, mas sim de restrição ao termo “aqueles”.

[red](C) Errada.[reset] - Não há indicação de relação causal no período analisado.

[red](D) Certa. [reset] - A oração subordinada “que se mantêm os mesmos” é adjetiva restritiva, pois especifica a quem a oração principal se refere, limitando o alcance do termo “aqueles”.

[red](E) Errada.[reset] - A oração não complementa o sentido de um nome, mas restringe o significado de um substantivo (aqueles).

Questão 26.
Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - IBAMA - Analista Administrativo Pós-Edital - 2025 - 1º Simulado 

No excerto “Não há nenhuma lei que mande você avisar o garçom”, a oração subordinada adjetiva expressa uma ideia explicativa, 
pois esclarece o antecedente “nenhuma lei”.

C.Certo
E.Errado

[red]ERRADO[reset] ->  traz uma ideia restritiva, restringindo o antecedente 'nenhuma lei', ou seja, especificando que não existe lei que determine a ação mencionada.
				 Além disso não há uma vírgula separando a oração subordinada do antecedente.

[red]Termo essencial:[reset]
	
	[red]Oração Principal:[reset]
			

			'Não há nenhuma lei...' -> [red]Verbo impessoal 'há' + objeto direto <- ( nenhuma lei )[reset]

	[red]Oração Subordinada:[reset]

			[yellow]'...que mande você avisar o garçom.'[yellow] -> 'que' -> [blue]pronome relativo que retoma 'lei'[reset] -> [blue]Sujeito da oração subordinada[reset]
		
	[red]Predicado da oração subordinada desenvolvida:[reset] [yellow]'...mande você avisar o garçom.'[reset]

	[red]verbo 'mandar'[reset] -> [blue]V.T.D[reset]  -> quem manda, manda alguém fazer algo: [yellow]'você avisar o garçom'[reset] <- [blue]( função sintática de objeto direto )[reset]

	[red]'...você avisar o garçom'[reset] -> [blue]Oração subordinada reduzida no infinitivo[reset] ( classificação )

	Não há nenhuma lei que mande [yellow]ISSO[reset], [yellow]ISSO[reset] o quê? [blue]'...você avisar o garçom.'[reset]

	[blue]'você'[reset] -> [red]Sujeito da oração subordinada reduzida[reset] // [red]'avisar o garçom'[reset] -> Predicado da oração subordinada substantiva objetiva reduzida no infinitivo

	 - [yellow]Subordinada substantiva, porque exerce função típica de substantivo (objeto direto).[reset]
		✔ [red]Objetiva direta, [reset] [yellow]pois é o objeto direto do verbo “mande”.[reset]
			✔ [red]Reduzida de infinitivo, pois:[reset]	[yellow]Não possui conjunção subordinativa.[reset] // [red]Verbo está no infinitivo (avisar).[reset]


Questão 27.
Ano: 2025 / Banca: Instituto Quadrix - Quadrix 
Prova: Quadrix - CFBio - Analista de Sistemas - 2025 

Esses patógenos são extremamente exigentes quanto às células [yellow]que infectam[reset], e apenas uma ínfima fração dos vírus [yellow]que nos cercam[reset] representa realmente uma ameaça.

Nas orações “que infectam” (linha 9) e “que nos cercam” (linha 10), ambas adjetivas restritivas, o vocábulo “que” funciona como sujeito.

C.Certo
E.Errado

	[red]Oração principal:[reset]

	 Oração coordenada assindética ( sem conectivos ) + [blue]oração subordinada adjetiva restritiva[reset] (“que infectam”)

	[blue]'Esses patógenos'[reset] <- [red]Sujeito simples[reset]
	[blue]'são'[reset] -> verbo de ligação -> [red]3º pessoa do plural[reset]
	[blue]'extremamente exigentes'[reset] -> [red]Predicativo do sujeito [reset] ( atribuição aos patógenos )
	[blue]'extremamente'[reset] -> [red] Advérbio de intensidade [reset]// [blue]'exigentes'[reset] -> [red]Substantivo abstrato[reset] 
	[blue]'...quanto às células que infectam...'[reset] <- [red]Complemento nominal[reset]

				[blue]Predicado nominal para a 1º oração [reset] -> [green]( verbo de ligação + predicativo do sujeito )[reset]

	 Cada oração possui seu próprio núcleo verbal e sujeito, logo são coordenadas, mas dentro delas temo subordinadas.
	
	[red]Oração Subordinada:[reset]

	[red]'que infectam'[reset] <- 'que' pronome relativo que retoma 'às células' e introduz uma oração subordinada.
	[red]'infectam'[reset] -> verbo intransitivo e o pronome relativo 'que' retoma 'células'.
		Portanto, 'que infectam' o pronome relativo 'que' admite função sintática de SUJEITO.
	[red]O Sujeito da oração subordinada é [reset] -> [bg_red]OCULTO.[reset] ->  '...que (eles) infectam' -> [green]o Sujeito oculto retoma 'os patógenos'[reset]
		[bg_red]O sujeito oculto da oração subordinada refere-se ao sujeito da oração principal 'os patógenos'.[reset]
				[bg_red]Portanto a 1º oração subordinada é adjetiva restritiva.[reset]

		[bg_blue]Não são quaisquer células, são aquelas que infectam, restringindo e especificando quais células são.[reset]

	[blue]Oração Coordenativa sindética[reset] + [yellow]oração subordinada adjetiva restritiva[reset] (“que nos cercam”)

		Oração coordenada sindética aditiva introduzida pela conjunção 'e' -> [yellow]onjunção coordenativa aditiva[reset]

		[yellow]'...apenas uma ínfima fração dos vírus...'[reset] <- [blue]oração coordenada sindética aditiva [reset]

		Há duas orações coordenadas (ligadas por “e”), cada qual com sua subordinada adjetiva restritiva interna.

	[red]4º oração subordinada adjetiva restritiva:[reset]

		'...[yellow]que nos cercam[reset] representa realmente uma ameaça.'

		'...fração dos vírus [yellow]que nos cercam...'[reset]  <- pronome relativo 'que' retoma o nome 'vírus'
		[red]Queremos dizer:[reset] [yellow]'...vírus nos cercam...'[reset] <- quem que nos cercam? [blue]'vírus'[reset] -> Portanto o pronome funciona como SUJEITO

		[blue]'nos cercam'[reset] -> verbo transitivo em que seu objeto direto é 'uma ameaça'.

Em “nos cercam”, o “nos” é objeto direto do verbo “cercar”. Ou seja, não é parte integrante do verbo, mas sim um complemento verbal (aquilo que é cercado = nos).

Verbo pronominal			Exemplo	Pronome faz parte do verbo?
arrepender-se	“Ele se arrependeu.”	Sim, não existe “arrepender” sem o “se”.
suicidar-se	“Ela se suicidou.”	Sim, o “se” é obrigatório.

Verbo pronominal é aquele que exige um pronome reflexivo como parte de sua conjugação, não podendo aparecer sem ele, 
e esse pronome não exerce função sintática típica de objeto direto ou indireto.

		[blue]'representa'[reset] -> quem representa, representa algo: [red]'uma ameaça'[reset] -> [blue]objeto direto[reset] // 
						[red]'representa'[reset] -> [blue]verbo transitivo direto[reset]
		[blue]'realmente'[reset]  -> [blue]Advérbio de intensidade que por sua vez tem sintaxe de Adjunto Adverbial de intensidade[reset]

		Portanto, o gabarito da questão é [green]CORRETO.[reset] -> Ambos os termos exercem função de sintática de SUJEITO.


[red]Questão 28.[reset]
Ano: 2025 / Banca: Instituto de Administração e Tecnologia - ADM TEC
Prova: ADM&TEC - Prefeitura de João Alfredo - Técnico em Enfermagem - 2025 

A única alternativa que traz uma oração subordinada substantiva subjetiva é:

A. A minha vontade é que seja feliz.
B. É essencial que você vença a partida.
C. Todo ser humano precisa de paz.
D. Tenho esperança de que as crianças sejam melhor educadas.

[red]Análise da alternativa 'A':[reset]

	[red]Termo essencial:[reset]

	[blue]'A minha vontade'[reset] <- [red]Sujeito[reset] // [blue]'minha'[reset] -> [red]Pronome possessivo[reset] // [red]'a'[reset] -> [blue]Artigo[reset]
	
	[red]Predicado[reset]: [red]nominal[reset] [green]( verbo de ligação + predicativo )[reset]
	 [blue]'é'[reset] -> [blue]verbo de ligação[reset] // [blue]'...que seja feliz.'[reset] <- [red]Predicativo do sujeito[reset]

	[red]Oração subordinada:[reset]

		[yellow]'...que seja feliz...'[reset] -> [blue]oração subordinada substantiva subjetiva[reset] [red]( predicativo do sujeito ao sujeito )[reset]

		[yellow]'que'[reset] é conjunção integrante em que liga duas orações e introduz uma oração subordinada substantiva predicativa.

A oração subordinada substantiva predicativa exerce a função de predicativo do sujeito da oração principal. 
		Ou seja, ela atribui uma característica, estado ou identidade ao sujeito.


				A minha vontade é [yellow]ISSO[reset]. [yellow]ISSO[reset] o que? [blue]'que seja feliz'[reset]

[red]Análise da alternativa 'B':[reset]

				É essencial que você vença a partida.


	[red]Oração Principal:[reset]

	[blue]'É essencial...'[reset] <- Oração iniciada com verbo de ligação // [blue]'essencial'[reset] -> [yellow]predicativo do sujeito[reset]

	[red]Sujeito[reset]   -> [blue]Oração Subordinada[reset]
	[red]Predicado[reset] -> [blue]Nominal[reset]

	[red]Oração Subordinada:[reset]

	[yellow]'...que você vença a partida.'[reset] <- [yellow]'que'[reset] -> conjunção integrante e introduz uma oração subordinada.
	[yellow]'você'[reset] <- [red]Sujeito[reset] da oração subordinada.
	[red]'vença'[reset] -> verbo transitivo direto -> [red]'a partida'[reset] -> [blue]Objeto Direto[reset]
	
	[red]Predicado da oração[reset] : [yellow]Predicado verbal[reset]	

	É essencial [yellow]ISSO[reset] <- [yellow]ISSO[reset] equivale à um substantivo. 
		Porém a oração não tem [yellow]SUJEITO[reset] ainda, o [yellow]SUJEITO[reset] está na oração subordinada.	

	Se a oração subordinada substantiva funciona como [yellow]SUJEITO[reset] da oração principal então temos uma oração substantiva subjetiva.	

		
	[blue]Análise da alternativa 'C':[reset]

					Todo ser humano precisa de paz.

	[red]'todo'[reset] -> [blue]Pronome indefinido[reset] -> Adjunto Adnominal, determinando o substantivo 'ser humano'. [green]( termo acessório )[reset]
	[red]'Todo ser humano'[reset] -> Sujeito // <- [green]Termo essencial[reset]

	Sem termos integrantes

	[blue]Predicado verbal:[reset]

	[red]'precisa'[reset] -> verbo transitivo direto // [red]'de paz'[reset] -> Objeto Indireto [blue]( termo integrante )[reset]


	[red]Análise da alternativa 'D':[reset]

				Tenho esperança de que as crianças sejam melhor educadas.

	[red]'de que'[reset] -> vocábulo preposicionado. 

		[red]TESTE:[reset] Colocar outro vocábulo para certificar se é pronome relativo.
	
			Tenho esperança [yellow]da qual[reset] as crianças...  <- [red]Ficou estranho...[reset]
		
		Tenho esperança [yellow]DISSO, DISSO[reset] o quê? '...de que as crianças...' -> [green]Completando um nome.[reset]
		
		Podemos dizer que é uma oração subordinada substantiva completiva nominal, completando o sentido do nome 'esperança'.	

[red]	Não é subordinada substantiva subjetiva. Em que exerce função de SUJEITO.[reset]

Tenho esperança de que as crianças sejam melhor educadas.

	[red]Oração principal: [reset] -> ( Termo essencial da oração -> Sujeito e Predicado )

	[red]Predicado verbal:[reset] -> [blue]'Tenho'[reset] -> Verbo transitivo direto // [blue]'esperança'[reset] -> Objeto Direto
	[red]Sujeito Oculto:[reset] [blue]'Eu'[reset]

	[red]Oração Subordinada: [reset] ( Termo integrante por que a oração está funcionando como complemento nominal)

	[red]'de que'[reset] -> Termo preposicionado com conjunção integrante.
	[red]'sejam'[reset]  -> que elas sejam -> [blue]3º pessoa do plural do presente do subjuntivo[reset]
	[red]'melhor educadas'[reset]-> Predicativo do sujeito [green]( atribuindo qualidade 'às crianças' )[reset]
	[red]'melhor'[reset] -> Verbo transitivo direto // [red]'educadas'[reset] -> Objeto Direto ( Termos integrantes )


	De qualquer forma não é o que a questão está pedindo. A questão pedi uma oração subordinada substantiva subjetiva.

Questão 29.
Ano: 2025 / Banca: SELECON Instituto Nacional de Seleções e Concursos - SELECON
Prova: SELECON - Hemominas - Médico Hematologista - 2025 

“A previsão é [yellow]concluir 2024 com pelo menos 92 mil doações”[reset] (4º parágrafo). A oração em destaque é classificada sintaticamente como:

A. principal
B. coordenada assindética
C. subordinada adjetiva restritiva
D. subordinada substantiva predicativa	


[red]'A previsão'[reset] <- Sujeito Simples // [red]'a'[reset] -> Artigo determinante // Adjunto Adnominal // [red]'previsão'[reset] -> núcleo do sujeito <- Termo essencial
[red]Predicado??[reset] [blue]'concluir 2024 com pelo menos 92 mil doações'[reset] -> [yellow]Predicativo do sujeito (oração reduzida de infinitivo)[reset]
[red]'é'[reset] -> [blue]verbo de ligação [reset] -> [yellow]( Ele 'é' -> 3º pessoa do singular do presente do indicativo )[reset]

	A previsão é [yellow]ISSO.[reset]

A oração subordinada está reduzida — ou seja, não começa com “que” ou “se”, mas sim com o verbo no infinitivo (“concluir”), 
			o que é comum em orações subordinadas predicativas reduzidas no infinitivo.

	[yellow]Oração subordinada substantiva predicativa reduzida no infinitivo:[reset]

		[red]'concluir...'[reset] -> verbo no infinitivo // objeto direto: [red]'2024'[reset] // [blue]'com pelo menos 92 mil doações'[reset] -> Adjunto adverbial de modo


Questão.30.
Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - PF - Papiloscopista Pré-Edital - 2025 - 2º Simulado

Na frase "Tomas encontrou sempre uma desculpa para se livrar da companheira, levando-a de volta à casa dela", 
a oração "levando-a de volta à casa dela" exerce a função de oração subordinada adjetiva explicativa, fornecendo uma informação adicional sobre a ação de Tomas.

C.Certo
E.Errado

[red]'Tomas'[reset] <- [blue]Sujeito Simples[reset] -> [green]( Termo essencial )[reset]

[green]( termo essencial )[reset] -> [blue]Predicado verbal:[reset]

[red]'encontrou'[reset] -> verbo no pretérito perfeito do indicativo na 3º pessoa do singular. [red]Transitivo Direto [reset]
[red]'uma desculpa'[reset] -> [blue]objeto direto[reset] // [red]'sempre'[reset] -> [green]Advérbio como adjunto adverbial de tempo[reset]

	[blue]'...para se livrar da companheira...'[reset] -> indica uma finalidade da ação principal de encontrar uma desculpa. Mostrando uma circunstância final.
[blue]Funciona como Adjunto Adverbial Final.[reset]

Introduz a conjunção subordinativa “para que”, típica das orações subordinadas adverbiais finais desenvolvidas.

Exemplo:

“Estudo [yellow]para que[reset] eu passe no concurso.”
([yellow]para que[reset] = locução conjuntiva subordinativa final, introduzindo oração de finalidade)

	Mas de qualquer forma '...levando-a de volta à casa dela.' <- Não exerce função de subordinada adjetiva explicativa, pode parecer,
mas sim uma adverbial final que expressa a razão pela qual Thomas encontra sempre uma desculpa para se livrar da companheira.
Portanto, ela está ligada à oração principal por uma relação de subordinação causal, e não adjetiva, que explicaria uma característica do substantivo 
(no caso, da "desculpa"). Assim, o erro foi classificar a oração subordinada como adjetiva, quando na verdade ela é adverbial causal.

	[yellow]'...levando-a de volta à casa dela.'[reset] <- oração subordinada adverbial causal reduzida de gerúndio, com valor de modo ou circunstância explicativa.

	[yellow]'levando'[reset] -> [blue]Verbo no gerúndio[reset] // [yellow]'a'[reset] -> [blue]Pronome pessoal oblíquo átono que refere-se à ela:[reset] [red]'levando ela'[reset]
			Portanto o pronome 'a' funciona como objeto direto do verbo transitivo direto 'levando'.
		[yellow]'de volta à casa dela'[reset] -> Não é complemento nominal, pois não completa nome, mas sim modifica o verbo (advérbio).
					[bg_blue]O conjunto todo funciona como adjunto adverbial de lugar.[reset]
		[yellow]'de volta'[reset] -> locução adverbial de movimento // [yellow]'à casa dela'[reset] -> Adjunto Adverbial de lugar

Questão.31
Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ICMBio - Analista Ambiental Pós-Edital - 2025 - 3º Simulado

No trecho “Espécies de plantas invasoras podem excluir competitivamente plantas nativas, impedir os processos de sucessão ecológica e 
alterar o funcionamento dos ecossistemas, que são essenciais para a manutenção da biodiversidade”, 
a oração subordinada adjetiva “que são essenciais para a manutenção da biodiversidade” tem a função de explicar o efeito das plantas invasoras sobre os ecossistemas.

C. Certo
E. Errado

[red]ERRADO[reset] - Tem a função de caracterizar o efeito das plantas... Qualificando o substantivo 'ecossistemas'.
		O pronome relativo 'que' retoma o nome antecessor e liga as duas orações: a principal a subordinada.
As orações subordinadas adjetivas restritivas têm a função de qualificar ou especificar um substantivo da oração principal.

[red]Análise sintática do período completo:[reset]

Espécies de plantas invasoras podem excluir competitivamente plantas nativas, impedir os processos de sucessão ecológica e 
alterar o funcionamento dos ecossistemas, que são essenciais para a manutenção da biodiversidade”.

	[red]Oração Principal:[reset]

	[yellow]'Espécies de plantas invasoras podem excluir competitivamente plantas nativas, impedir os processos de sucessão ecológica e alterar[reset]
[yellow]o funcionamento dos ecossistemas,...'[reset]

[red]Quem pratica a ação?[reset]

	[red]Sujeito[reset] -> [yellow]'Espécies de plantas invasoras'[reset] -> Núcleo do sujeito -> [yellow]'espécies'[reset] 
	// [yellow]'de plantas invasoras'[reset] -> [blue]Complemento Nominal[reset]

	[red]Predicado verbal composto da oração principal:[reset]

		[red]'podem excluir'[reset] -> Verbo transitivo -> [yellow]'plantas nativas'[reset] -> [red]Objeto Direto[reset]
		[red]'competitivamente'[reset] -> Advérbio de modo -> Adjunto Adverbial de modo, modificando o verbo 'excluir'. ( termo acessório )
		[red]'impedir'[reset] -> Verbo transitivo -> [yellow]'os processos de sucessão ecológica'[reset] -> [red]Objeto Direto[reset]
		[red]'alterar'[reset] -> Verbo transitivo -> [yellow]'o funcionamento dos ecossistemas'[reset]   -> [red]Objeto Direto[reset]

Não inicia nova oração com novo sujeito.
✅ Permanece na oração principal, sendo um predicado com verbos coordenados (excluir, impedir, alterar).

Trata-se de um predicado com estrutura composta, onde há:

Verbo auxiliar + verbo principal + objetos diretos coordenados por elipse do auxiliar.

O verbo “podem” (verbo auxiliar/modal) está explicitamente presente apenas no primeiro verbo principal (excluir).

Nos verbos seguintes (impedir e alterar), o auxiliar “podem” está elíptico (oculto), mas é entendido pelo contexto.

[yellow]podem[reset] excluir competitivamente plantas nativas, [yellow](podem)[reset] impedir os processos de sucessão ecológica e [yellow](podem)[reset] alterar[reset]
[yellow]o[reset] funcionamento dos ecossistemas,...

	
	[yellow]Oração Subordinada:[reset]
	
	'...,que são essenciais para a manutenção da biodiversidade.'

Se o texto indica que só alguns ecossistemas são essenciais, a oração passa a ser restritiva mesmo com vírgula.
[yellow](pois a vírgula pode ser opcional em restritivas curtas no final de frase, embora seja rara essa interpretação segundo a gramática tradicional).[reset]

[red]Regra geral de pontuação e classificação:[reset]

[red]Restritiva:[reset]				[red]Explicativa:[reset]
Sem vírgulas.					Entre vírgulas (ou vírgula antes e ponto final).
Restringe o sentido do antecedente.		Acrescenta informação acessória.
Ex: Os alunos que estudam passarão.		Ex: Os alunos, que estudam, passarão.


É uma oração subordinada adjetiva explicativa, pois está sendo separada por pontuação (vírgula e ponto final ) e além disso, acrescenta informação e não restringindo.

Mas se o texto indica que só alguns ecossistemas são essenciais, a oração passa a ser restritiva mesmo com vírgula e ponto final.

[blue](pois a vírgula pode ser opcional em restritivas curtas no final de frase, embora seja rara essa interpretação segundo a gramática tradicional).[reset]

	[green]De qualquer forma, nenhuma das orações subordinadas adjetivas seja restritiva ou explicativa, não possuem a função de explicar.[reset]
[green]A restritiva tem o propósito de restringir o termo anterior e a explicativa tem o propósito de generalizar o termo anterior utilizando pontuação.[reset]


Questão.32.
Ano: 2025 / Banca: Associação dos Municípios do Extremo Oeste de Santa Catarina - AMEOSC
Prova: AMEOSC - Câmara de Princesa - Contador Legislativo - 2025

A pesquisadora Marina Hirota, professora associada da Universidade Federal de Santa Catarina (UFSC), 
explica [yellow]"que há uma massa de ar quente instalada na região"[reset] que compreende o Sul do Brasil, o norte da Argentina e partes do Paraguai.

A expressão destacada trata-se de uma oração:

A. Coordenada sindética explicativa.
B. Subordinada substantiva completiva nominal.
C. Coordenada sindética conclusiva.
D. Subordinada adjetiva explicativa.

O gabarito da questão não está em nenhuma das alternativas.

	[red]Análise sintática:[reset]

	[red]Oração Principal:[reset]

	[yellow]'A pesquisadora Marina Hirota, professora associada da UFSC,'[reset]<- [red]Sujeito simples[reset]
		[red]núcleo do sujeito[reset] -> [yellow]'pesquisadora'[reset] // [yellow]'A'[reset] -> [blue]Artigo que determina e acompanha o substantivo, funciona como Adjunto Adnominal [reset]
[blue]'Marina Hirota'[reset] -> [red]Aposto explicativo[reset] // [blue]'...professora associada da UFSC...'[reset] ->[red] Aposto explicativo ( qualificando Marina )[reset]
		[red]'explica'[reset] -> verbo na 3º pessoa do singular do presente do indicativo , [red]sintaxe:[reset] transitivo direto
	quem explica, explica algo, explica o que? ISSO, ISSO o quê? - [yellow]'...que há uma massa de ar quente instalada na região...'[reset]
		Portanto, o objeto direto do verbo 'explica' introduz uma oração subordinada substantiva objetiva direta.
						Introduzida pela conjunção integrante 'que'.
	Além disso, é substantiva por que é substituida por um substantivo genérico e é objetiva direta por que completa o sentido do verbo.

	[yellow]2º oração:[reset] [red]Subordinada Substantiva Objetiva Direta[reset]

	[yellow]'que'[reset] -> Conjunção integrante ( não retoma nome nenhum ) Apenas introduz a oração.
		[yellow]'há'[reset] -> verbo impessoal no sentido de existir, não admite sujeito e é transitivo direto: [yellow]'uma massa de ar quente instalada na região'[reset] <- [red]Objeto direto[reset]
	[yellow]'uma massa de ar'[reset] <- [blue]'uma massa'[reset] -> [red]substantivo concreto [reset] ( 'massa' núcleo do sujeito da or. subordinada ) -> [yellow]'de ar quente'[reset] -> [blue]Adjunto Adnominal [reset]( sendo um substantivo concreto qualificando outro substantivo concreto.)
				Além disso, é adjunto adnominal por expressar tipo, origem ou matéria.
	[yellow]'instalada na região'[reset] -> [blue]Predicativo do objeto[reset] ( completa o sentido do objeto direto: 'uma massa de ar quente...')
			[red]Predicado verbal:[reset] -> [yellow]VTD impessoal + Obj. Direto[reset]
	

	[red]3º oração:[reset] subordinada adjetiva restritiva

	Podemos verficar substituindo o vocábulo [yellow]'que'[reset] por um pronome relativo [yellow]'a qual':[reset]

		'...na região [yellow]a qual[reset] compreende o Sul do Brasil...' -> Portanto, [yellow]'que'[reset] é pronome relativo e deve retomar [yellow]'região'[reset] e introduzir a oração subordinada.

	Para sabermos qual a função sintática do pronome relativo, temos que substituir o pronome pelo nome retomado:

			[yellow]região[reset] compreende o Sul do Brasil...-> [blue]quem que compreende o sul do Brasil?[reset] [yellow]'a região'[reset] <- Sujeito do verbo 'compreende'.
		
		Portanto, a função sintática do pronome relativo 'que' na oração subordinada adjetiva restritiva é de [yellow]SUJEITO.[reset]
Além disso, restringe o sentido de “região” especificando qual região está sendo mencionada (aquela que compreende esses locais).

	[yellow]'compreende'[reset] -> 3º pessoa do singular do presente do indicativo <- [red]verbo transtivo direto [reset]
	[yellow]'sul do Brasil, o Norte da Argentina e partes do Paraguai'[reset] <- [red]Objeto direto[reset]

			Esses termos são objetos diretos coordenados do verbo “compreende”.

Por que não são adjuntos adverbiais?  -> Adjunto adverbial de lugar indica local onde ocorre a ação:

Ex.: Moro em Porto Alegre. (em Porto Alegre = adj. adverbial de lugar)

Na frase: '...o Sul do Brasil, o norte da Argentina e partes do Paraguai.' não indicam lugar de ação, mas o que está sendo compreendido (incluído) pela região.


Questão.33.
Ano: 2025 / Banca: Universidade do Extremo Sul Catarinense - UNESC
Prova: UNESC - InoversaSul - Professor de Anos Iniciais/Finais - Área: Língua Portuguesa - 2025

É claro [yellow]que nem todas as crianças têm a mesma probabilidade de desenvolver estes tipos de interesses repetitivos.[reset]

O termo destacado é classificado como:

A. Oração subordinada substantiva predicativa.
B. Oração subordinada substantiva subjetiva.
C. Oração subordinada substantiva completiva nominal.
D. Oração subordinada substantiva objetiva direta.


	É claro o quê? [yellow]ISSO, ISSO[reset] o quê? [yellow]'..que nem todas as crianças...'[reset] <- Sujeito oracional ( oração principal que está em ordem inversa ) 
		[yellow]ISSO é um termo genérico substancial.[reset] // 'que' -> [blue]conjunção integrante[reset] 
				[red]'É'[reset] -> [blue]Verbo de ligação[reset] // [red]'claro'[reset] -> [blue]Predicativo do Sujeito[reset]

	Portanto, a oração em destaque é substantiva subjetiva em que exerce função de sujeito da oração principal.

	'É claro..' -> Predicado verbo-nominal ( predicado verbo-nominal )

	[red]Análise sintática da oração subordinada:[reset]

	'...que nem todas as crianças têm a mesma probabilidade de desenvolver estes tipos de interesses repetitivos.'

	[yellow]'que'[reset] <- Conjunção integrante que introduz a oração subordinada

		[red]Sujeito da oração subordinada:[reset] [yellow]'...nem todas as crianças...'[reset] // [red]Núcleo:[reset] -> [yellow]'crianças'[reset]
		[yellow]'têm'[reset] -> verbo na 3º pessoa do singular do presente do indicativo.  ( V.T.D ) <- Sintaxe ( termo acessório )
		[yellow]'a mesma probabilidade'[reset] -> [red]Objeto Direto[reset]
		[yellow]'de desenvolver estes tipos de interesses repetitivos.'[reset] <- [blue]Complemento Nominal de 'probabilidade'[reset]
		[yellow]'de desenvolver' [reset]-> [blue]preposição + verbo no infinitivo transitivo direto[reset]
		[yellow]'estes tipos de interesses repetitivos'[reset] -> [blue]Objeto Direto do verbo 'desenvolver'[reset]
		[yellow]'estes'[reset] -> Adjunto Adnominal / [red]'tipos'[reset] -> [blue]núcleo do objeto direto que por sua vez possui complemento por ser substantivo abstrato[reset]
		[yellow]'de interesses repetitivos'[reset] -> [blue]Complemento Nominal[reset]


Observações:

	O verbo 'desenvolver' dentro da oração subordinada substantiva subjetiva introduz uma oração subordinada substantiva completiva nominal.

	'....de desenvolver estes tipos de interesses repetitivos.'
	
		[red]Sujeito:[reset] 'probabilidade' // [red]Predicado:[reset] '...de desenvolver estes tipos de interesses repetitivos.'
	
	Por que [yellow]SUBSTANTIVA?[reset]

		...desenvolver [yellow]ISTO, ISTO[reset] o quê? [blue]'... estes tipos de interesses repetitivos.'[reset] 

	Por que Completiva Nominal?

		Está completando o sentido do substantivo 'probabilidade'.

	Temos uma oração subordinada substantiva completiva nominal reduzida no infinitivo.
	
	Por que reduzida?

		 1. Verbo no infinitivo impessoal. ( sem conjugação )
		 2. Sem conjunção integrante.

	

Questão.34.
Ano: 2025 / Banca: Instituto Federal de Educação, Ciência e Tecnologia - IFSUL
Prova: IFSUL - IFSUL - Professor do Ensino Básico, Técnico e Tecnológico - Área: Português/Inglês - 2025


Mas, pelo menos na decisão judicial americana, a invasão de um olhar não autorizado, [yellow]que capta uma cena privada e a torna pública[reset], é legal.

Considere as afirmações a seguir quanto à oração destacada na linha 46:

[red]I.[reset]   É uma oração subordinada adjetiva restritiva e, portanto, precisa estar entre vírgulas.
[red]II.[reset]  É uma oração subordinada adjetiva explicativa e, portanto, precisa estar entre vírgulas.
[red]III.[reset] Caso as vírgulas que a delimitam fossem removidas, essa oração seria transformada em subordinada adjetiva restritiva, alterando assim o sentido da frase.
[red]IV.[reset]  Essa oração delimita e restringe o sentido da estrutura “na decisão judicial americana” (linha 45).

Estão corretas apenas as afirmativas:

A.II e IV.
B.II e III.
C.I e IV.
D.III e IV.

I - ERRADA / II - CERTA / III - CERTA / IV - ERRADA

[red]Análise das sentenças:[reset]

	I   - [red]ERRADA[reset] - A restritiva não precisa estar entre vírgulas.
	II  - Afirmação correta.
	III - Sim, a restritiva estaria restringindo o termo anterior 'a invasão' caracterizando que somente essa invasão capta uma cena e a torna pública.
	IV  - [red]ERRADA[reset] - Essa oração delimita e restringe o sentido da estrutura '...a invasão de um olhar não autorizado...'

[red]Análise do período:[reset]

	Mas, pelo menos na decisão judicial americana, a invasão de um olhar não autorizado, que capta uma cena privada e a torna pública, é legal.

	[red]'Mas'[reset] -> Conjunção coordenativa adversativa // [red]'pelo menos'[reset] -> locução adverbial de intensidade/moderação ( adjunto adverbial ) <- Termo acessório
	[red]'na decisão judicial americana'[reset] -> Adjunto Adverbial de lugar
	[red]'a invasão de um olhar não autorizado'[reset] -> Sujeito -> núcleo 'invasão' // [red]'de um olhar não autorizado'[reset] -> Complemento nominal 
	[red]'que'[reset] -> pronome relativo que retoma o termo 'invasão' e introduz uma oração subordinada adjetiva explicativa 
	[red]'capta'[reset] -> verbo na 3º pessoa do singular do presente do indicativo com função sintática de verbo transitivo direto -> 'uma cena privada' -> Objeto Direto
	[red]'torna'[reset] -> verbo na 3º ps. do sing. do pres.ind. com função sintática de verb.trans.dir
	[red]'a'[reset] -> pronome pessoal oblíquo átono em que retoma 'cena privada' que por sua vez é objeto direto do verbo 'tornar'.
	[red]'pública'[reset] -> Predicativo do objeto direto

	[red]'é'[reset] -> verbo de ligação // [red]'legal'[reset] -> Predicativo do sujeito

[red]Atenção![reset]

 Quando “tornar” é verbo de estado:
Ele funciona como verbo de ligação, ligando o sujeito a uma característica ou estado.
- Exemplo: Ela se tornou professora.
Aqui, “tornou” está conectando “ela” à condição de “professora” — ou seja, indica uma mudança de estado ou identidade.
Outros exemplos com “tornar-se” como verbo de estado:
- O céu se tornou escuro.
- Ele se tornou mais confiante com o tempo.
Nesse caso, ele é sinônimo de verbos como ficar, passar a ser, virar, que indicam transformação ou mudança de estado.

⚙️ Mas atenção!
O verbo “tornar” também pode ser usado como verbo transitivo direto, com sentido causativo — ou seja, quando alguém faz algo virar outra coisa.
- Exemplo: O medo tornou a decisão mais difícil.
Aqui, “tornou” não é de estado, mas está transformando algo (a decisão) em outra coisa (mais difícil).

Quando exprime mudança de estado, mas não traz sentido pleno de transformação como ação voluntária, 
funcionando apenas para ligar o sujeito a uma característica nova.

➡️ Exemplo de verbo de ligação:

“Ele tornou-se médico.”
Aqui, “tornou-se” = verbo de ligação (indica mudança de estado).
✔️ “Médico” = predicativo do sujeito.


Questão.35
Ano: 2025 / Banca: COSEAC
Prova: COSEAC - SEAP RJ - Inspetor de Polícia Penal Pós-Edital - 2025 - 4º Simulado

No trecho “Apesar disso, não há qualquer regulação [yellow]que obrigue plataformas e usuários a terem um mínimo de obrigações para com a sociedade”[reset], 
a oração subordinada “que obrigue plataformas e usuários a terem um mínimo de obrigações para com a sociedade” exerce a função de:

A. oração subordinada adverbial concessiva.
B. oração subordinada substantiva subjetiva.
C. oração subordinada substantiva completiva nominal.
D. oração subordinada adjetiva explicativa.
E. oração subordinada adjetiva restritiva.


	O vocábulo 'que' deverá ser substituido por um pronome relativo para certificar se é uma oração subordinada adjetiva.
	
	'Apesar disso, não há qualquer regulação [yellow]a qual[reset] obrigue plataformas...' <- [yellow]Portanto o 'que' é pronome relativo.[reset]
	Além disso, o pronome [yellow]'que'[reset] retoma [yellow]'regulação'[reset] e introduz por sua vez uma oração subordinada adjetiva restritiva.
Ou seja, não é qualquer regulação, é uma regulação que obrigue plataformas e usuários a terem um mínimo de obrigações para com a sociedade...

						Sendo assim, a alternativa correta é a 'E'.


	[red]Análise sintática da sentença:[reset]

Apesar disso, não há qualquer regulação que obrigue plataformas e usuários a terem um mínimo de obrigações para com a sociedade.


	[red]Oração principal:[reset]

	[red]'Apesar disso'[reset] -> Locução prepositiva [blue]( preposição + pronome demonstrativo )[reset] -> [blue]Adjunto Adverbial de concessão[reset]
	[red]'não há'[reset] -> Verbo impessoal 'haver' + advérbio de negação 'não'
	[red]'qualquer regulação'[reset] -> [blue]Objeto Direto do verbo 'haver'[reset]
	
	[red]Oração Subordinada:[reset]

	[yellow]'...que obrigue plataformas e usuários a terem um mínimo de obrigações para com a sociedade.'[reset]

	Não é qualquer regulação, é uma regulação que obrigue plataformas e usuários a terem um mínimo de obrigações para com a sociedade.
					Portanto, a oração trata-se de ser adjetiva restritiva.

	[red]'que'[reset] -> Pronome relativo [yellow]SUJEITO[reset] de 'obrigue' na oração subordinada.
		[red]verbo:[reset] obrigue ( verbo transitivo direto ) quem obriga, obriga: [yellow]'plataformas e usuários'[reset] -> [red]Objeto Direto[reset]
	[red]'a terem um mínimo de obrigações para com a sociedade'[reset] -> [yellow]Predicativo do objeto[reset]
	[red]'terem' [reset]-> [blue]'eles terem'[reset] -> [yellow]3º pessoa do plural no INFINITIVO[reset]
	[red]'um mínimo de obrigações'[reset] -> [yellow]Objeto direto[reset] de 'terem'
	[red]'de obrigações'[reset] -> [yellow]Complemento Nominal[reset]
	[red]'para com a sociedade'[reset] -> [yellow]Adjunto Adverbial de finalidade/referência[reset]

		'...a terem um mínimo de obrigações para com a sociedade.' -> 

	'a' -> O vocábulo não pode ser pronome pessoal por que não substitui ou representa nenhuma termo como faria o pronome pessoal oblíquo átono.
		
		O vocábulo 'a' é preposição exigida pelo verbo obrigar: '...obrigar alguém a algo...'/ '...a fazer algo...'

	
	'...a terem [yellow]ISSO[reset], [yellow]ISSO[reset] é: [blue]'substantivo genérico'[reset]

	Portanto, oração subordinada substantiva predicativa
	


Questão.36
Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - EMBRAPA - Pós Edital - Conhecimentos Básicos. - 2025 - 1º Simulado

No trecho “A neuropediatra que acompanha Breno ainda não descartou e nem confirmou um diagnóstico de autismo” (penúltimo parágrafo), 
a oração “que acompanha Breno” é subordinada adjetiva restritiva, pois delimita o antecedente “A neuropediatra”.

C.Certo
E.Errado

	Não é qualquer 'neuropediatra', é aquela que acompanha Breno.. ou seja, restringe a neuropediatra. Portanto, delimita o antecedente 'A neuropediatra'.
O pronome relativo 'que' retoma o sujeito e introduz uma oração subordinada adjetiva restritiva.

	Portanto, item [yellow]CORRETO.[reset]
	
	A neuropediatra que acompanha Breno ainda não descartou e nem confirmou um diagnóstico de autismo.

	[yellow]Termo essencial:[reset]

	[red]Oração principal:[reset]
		
		A neuropediatra (...) ainda não descartou e nem confirmou um diagnóstico de autismo.

	[yellow]'A neuropediatra'[reset] -> [red]Sujeito Simples[reset] // [yellow]'...ainda não descartou e nem confirmou um diagnóstico de autismo.'[reset] <- [red]Predicado[reset]

		
	[red]Oração Subordinada: [reset]

		[yellow]'...que acompanha Breno...'[reset]

		[yellow]'que'[reset] -> Pronome relativo que retoma 'a neuropediatra' que por sua vez é sujeito da oração subordinada.
	quem acompanha, acompanha alguém: [yellow]'Breno'[reset] // [yellow]'ainda'[reset] -> Advérbio que por sua vez é Adjunto Adverbial de tempo, alterando o verbo 'acompanhar'.
		[yellow]'não'[reset] -> Advérbio de negação que por sua vez é adjunto adverbial de negação alterando o verbo 'acompanhar'.
	[yellow]'descartou'[reset] -> Ele descartou -> Presente do indicativo 3º pessoa do singular // [red]Verbo intransitivo[reset]
		[yellow]'e'[reset] -> Conjunção coordenativa aditiva // [yellow]'nem'[reset] -> Conjunção coordenativa aditiva negativa:
	Verbo 'confirmar' ( ele confirmou -> Presente do indicativo 3º pessoa do singular ) quem confirma, confirma algo: [yellow]'um diagnóstico de autismo'[reset] <- [red]Objeto Direto[reset]
		[yellow]'de autismo'[reset] -> Complemento Nominal ( por que o autismo é diagnosticado )


Questão.36
Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ICMBio - Analista Administrativo Pós-Edital - 2025 - 4º Simulado

Na frase “A Amazônia ocupa quase 50% do território nacional, porque a maior parte da formação florestal do bioma é de terras baixas”, 
a oração “porque a maior parte da formação florestal do bioma é de terras baixas” é uma oração subordinada adjetiva explicativa, 
pois está adicionando uma informação extra sobre a Amazônia.

C. Certo
E. Errado

[red]ERRADO[reset] - 'porque' introduz outra oração e não a adjetiva explicativa.
	
	[yellow]Na verdade introduz uma oração subordinada adverbial causal. O “porque” é uma conjunção integrante e estabelece uma relação de causa, explicando o motivo...[reset]

[red]Análise sintática completa da frase:[reset]

	A Amazônia ocupa quase 50% do território nacional, [yellow]porque[reset] a maior parte da formação florestal do bioma é de terras baixas.

	[red]Oração Principal:[reset]

	'A Amazônia ocupa quase 50% do território nacional...' 

	[yellow]'A Amazônia'[reset] -> [red]Sujeito[reset] // [yellow]'ocupa'[reset] -> verbo na 3º pessoa do singular do presente do indicativo // 
	Complemento direto do verbo 'ocupa' -> [yellow]'quase 50% do território nacional'[reset] -> [red]Objeto Direto[reset] // 
	[yellow]'quase'[reset] -> Advérbio de intensidade modificando o verbo 'quase'
	[yellow]'do território nacional'[reset] -> Complemento nominal 

	[red]Oração Subordinada[reset] : adverbial causal

		[yellow]'...porque[reset] a maior parte da formação florestal do bioma é de terras baixas.'

	[yellow]'porque'[reset] -> Conjunção integrante em que liga a oração principal a subordinada

	[yellow]'...a maior parte da formação florestal do bioma...'[reset] -> [red]Sujeito [reset]

	[yellow]'a'[reset] -> [red]Artigo definido[reset] (adjunto adnominal) -> [yellow]'maior'[reset] -> é um adjetivo de grau comparativo de superioridade do adjetivo “grande”.

	[yellow]'parte'[reset] -> núcleo // [yellow]'da formação florestal do bioma'[reset] -> [red]Complemento Nominal[reset]

	[yellow]'formação florestal do bioma'[reset] -> [yellow]'formação'[reset] -> núcleo do termo 
	
	[yellow]'florestal'[reset] -> Adjunto Adnominal ( qualificando 'formação' ) // [yellow]'do bioma'[reset] -> [red]complemento nominal[reset]

	[yellow]'é'[reset] -> [red]Verbo de ligação[reset] // [yellow]'de terras baixas'[reset] -> [red]Predicativo do sujeito[reset]

Questão.37
Ano: 2025 /Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - ICMBio - Analista Ambiental Pós-Edital - 2025 - 2º Simulado

No trecho “A voz fria e convincente disse: ‘Não adianta votar... A decepção é maior [yellow]do que a esperança.[reset]’”, 
a oração em destaque é classificada como oração subordinada adjetiva explicativa que adiciona uma informação extra sobre a “decepção”.

C.Certo
E.Errado


						A decepção é maior do que a esperança.


	Precisa de mais 1 verbo para que haja uma oração subordinada.

	[yellow]'do que a esperança'[reset] funciona como grau comparativo do adjetivo 'maior' e não como oração subordinada.

	[yellow]'A decepção'[reset] -> [red]Sujeito Simples[reset] // [yellow]'é'[reset] -> [yellow]Verbo de ligação[reset] 
	[yellow]'maior do que a esperança'[reset] -> [red]Predicativo do Sujeito[reset]

	[yellow]'do que'[reset] -> Conjunção subordinativa comparativa preposicionada(locução).
			oração reduzida comparativa com elipse do verbo: “maior do que (é) a esperança”).

			[yellow]'maior'[reset] -> Adjetivo no grau comparativo de superioridade de “grande”.

A decepção é maior do que a esperança.

✔ Não há verbo implícito que retome o verbo principal, pois não diria:

❌ “A decepção é maior do que a esperança [yellow]é.[reset]”

	Mas o verbo implícito sempre vai estar implícito até alguém dizer que não está mais.
		Portanto, eu digo que ele está lá. Tanto depois da conjunção subordinativa ou depois do substantivo 'esperança'

	Sendo assim:

	A decepção é maior do que a esperança” está, de fato, [yellow]funcionando como uma oração subordinada adverbial comparativa, [reset]
pois expressa uma comparação entre a decepção e a esperança. A forma verbal “é” está implícita, pois, ao estabelecer a comparação, 
	A oração sugere implicitamente a ideia de que a decepção “é maior” em relação à esperança, o que é uma comparação.

	A questão está errada em dizer que é uma oração subordinada adjetiva explicativa que adiciona uma informação extra sobre a “decepção”.
	Apesar de exercer sintaxe de predicativo do sujeito após o verbo de ligação, ocorre um grau comparativo entre o nome e outro.
Tome cuidado com a locução adverbial comparativa 'do que' que introduz uma oração subordinada adverbial comparativa reduzida no infinitivo.

	
Questão.38
Ano: 2025 / Banca: Instituto Brasileiro de Apoio e Desenvolvimento Executivo - IBADE
Prova: IBADE - UNIVESP - Designer Gráfico e de Interface - 2025

De acordo com o período a seguir, marque a alternativa correta quanto às classificações das orações destacadas:

É bem provável que o esforçado Marcos, cujas notas sempre foram boas, seja aprovado, mesmo não tendo concluído o Ensino Médio, 
nos exames vestibulares que prestou no final do ano.


A.“É bem provável”
classificação: oração substantiva subjetiva.

B.“...que o esforçado Marcos seja aprovado nos exames vestibulares que prestou no final do ano.” – 
classificação: oração subordinada substantiva objetiva direta.

C....”, cujas notas sempre foram boas,”
classificação: oração subordinada apositiva.

D.“..., mesmo não tendo concluído o Ensino Médio....”
classificação: oração subordinada adverbial concessiva, reduzida de gerúndio.

E.“... que prestou no final do ano.”
classificação: oração coordenada adjetiva explicativa.


É bem provável que o esforçado Marcos, cujas notas sempre foram boas, seja aprovado, mesmo não tendo concluído o Ensino Médio, 
					nos exames vestibulares que prestou no final do ano.

	[red]Oração principal:[reset]

	[yellow]'É'[reset] -> [red]Verbo principal de ligação[reset] // [yellow]'bem provável'[reset] -> [red]predicativo do sujeito[reset]
		[red]Sujeito oracional: [yellow]'...que o esforçado Marcos, cujas notas sempre foram boas, seja aprovado...'[reset]

	Portanto a alternativa 'A' está errada. 'É bem provável' é a oração principal. A substantiva subjetiva exerce função de sujeito da oração,
em que é toda a frase, menos a principal. Pela ordem em que está. Portanto, questão ERRADA.

	[red]1º Oração subordinada substantiva subjetiva:[reset]

	'...[yellow]que[reset] o esforçado Marcos, cujas notas sempre foram boas, seja aprovado..'

		[red]'que'[reset] -> conjunção integrante que introduz a oração subordinada SUBJETIVA que exerce função de SUJEITO da oração principal

Portanto, a alternativa 'B' nos diz que é substantiva objetiva direta sendo que o termo em destaque exerce a função sintatica de SUJEITO. 
				Ou seja, SUJEITO oracional ou oração subordinada substantiva subjetiva.

 							Sendo assim, questão ERRADA.

	[red]2º oração subordinada: Adjetiva explicativa[reset]

'...o esforçado [yellow]Marcos, cujas notas [reset]sempre foram boas...' <- Pronome relativo 'cujas' retoma 'Marcos' com sentido de posse ao consequente 'notas'.
				as notas de Marcos, sendo assim, a função sintática do pronome relativo 'cujas' é de Adjunto Adnominal.
			por que as notas são de MARCOS -> Adjunto Adnominal, e além disso, introduz uma oração subordinada adjetiva explicativa.
					pois não são quaisquer notas, são aquelas que sempre foram boas...

			O restante da oração não tem muito que explicar. Temos: 'sempre' -> Advérbio de tempo ( Adjunto Adverbial de tempo )
			'foram' -> Verbo IR com sentido de ligação, de estado. // 'boas' -> Adjetivo com função sintática de Predicativo do Sujeito

			Na alternativa C nos diz que a classificação é oração subordinada apositiva, está ERRADO. 
						É uma oração subordinada Adjetiva explicativa.

	[red]3º oração subordinada: Adverbial concessiva[reset]


						'...mesmo não tendo concluído o Ensino Médio...'

		Indica concessão, ou seja, um fato contrário ao da oração principal, mas que não impede sua realização.
		[red]Conectivos principais:[reset]	[yellow]embora, ainda que, mesmo que, se bem que, conquanto, posto que.[reset]
		[red]Forma verbal predominante:[reset]	[yellow]Conjugação no subjuntivo (quando desenvolvida)[reset]

		Mas o verbo está nominal no gerúndio e não há locução completa subordinativa explícita + verbo conjugado no subjuntivo
						sendo assim sua forma está reduzida: 'mesmo' + gerúndio

O vocábulo 'mesmo' é uma partícula concessiva (equivale a 'embora') ou a sua forma completa 'mesmo que' torna-se uma conjunção subordinativa concessiva adverbial.

		A locução verbal no gerúndio composta: “ter”-> 'TENDO' (verbo auxiliar) + “concluído” (verbo principal no particípio) a faz ser reduzida no gerúndio.

Por que é gerúndio composto? Porque indica ação anterior à do verbo principal da oração principal, e a forma é:

ter (auxiliar no gerúndio) + particípio do verbo principal.

		Agora em sua forma desenvolvida a partícula concessiva torna-se uma locução adverbial de concessão 'mesmo que', uma conjunção.
		que por sua vez, introduz orações subordinadas adverbiais concessivas.
		E a forma verbal torna-se conjugada, geralmente no subjuntivo, independente do tempo:

			Exemplo:

		mesmo que não [yellow]concluísse[reset] o Ensino Médio.  ( [yellow]'concluísse'[reset] -> [blue]Pretérito imperfeito do subjuntivo[reset] -> Uma hipótese ou possibilidade no passado )

					ou

		mesmo que não tenha concluído o Ensino Médio. ( [yellow]'que eu tenha'[reset] -> Verbo auxiliar no presente do subjuntivo + verbo principal no partícipio )

					ou

		embora não concluísse o Ensino Médio.
		

			A alternativa 'D' está correta. Trata-se de uma oração subordinada adverbial concessiva reduzida no gerúndio.

	[red]4º oração subordinada: [reset]

					
					nos [red]exames vestibulares[reset] [yellow]que[reset] prestou no final do ano.



	Não foi qualquer exame vestibular, foi o que ele prestou no final do ano, portanto, trata-se de uma oração subordinada adjetiva restritiva
							restringindo 'os exames vestibulares' 

		Aqui o vocábulo 'que' é um pronome relativo que retoma 'exames vestibulares' -> atribuindo uma restrição ao exames, aqueles prestados
								no final do ano.

		Além disso, o pronome 'que' não pode exercer função sintática de SUJEITO, por que o verbo 'prestou' não concorda com 'exames vestibulares'.
				quem que prestou os exames vestibulares? 'ele' -> Sujeito Oculto
			quem presta, presta algo: 'os exames vestibulares' -> Objeto direto
			Sendo assim, o pronome relativo 'que' retoma 'os exames vestibulares' que por sua vez é objeto direto.

		A alternativa 'E' está errada em dizer que é explicativa. Não há pontuações que a caracterizem como explicativa.


Questão.39
Ano: 2025 / Banca: Centro de Seleção e de Promoção de Eventos UnB - CESPE CEBRASPE
Prova: CESPE/CEBRASPE - MPCE - Técnico Ministerial Pós-Edital - 2025 - 1º Simulado

O vocábulo “que”, em “você pode concluir que eu só estou querendo agradá-lo” (terceiro parágrafo), introduz uma oração completiva direta.

C. Certo
E. Errado

[green]CORRETO[reset] -> O vocábulo 'que' introduz uma oração subordinada substantiva objetiva direta. Além disso, é conjunção integrante em que liga a
oração principal a oração subordinada.

	[red]ATENÇÃO![reset] [bg_red]O CESPE também considera certo chamar de completiva direta.[reset]

[red]Vamos a análise sintática:[reset]

					Você pode concluir que eu só estou querendo agradá-lo

	[red]Oração principal:[reset]

	[yellow]'você'[reset] -> [red]Sujeito[reset] // [red]Locução verbal[reset] -> [yellow]'pode concluir'[reset] -> ( predicado verbal, termo essencial, (verbo auxiliar + verbo principal no infinitivo )

	Você pode concluir [yellow]ISSO. ISSO[reset] o que? quem conclui, conclui algo:  [yellow]'...que eu só estou querendo agradá-lo'[reset] <- [red]Objeto Direto[reset]

		O vocábulo 'que' é conjunção integrante e introduz a oração subordinada substantiva objetiva direta ou completiva direta.

[red]Análise sintática mais detalhada:[reset]

	[red]Oração subordinada:[reset]


		'... que eu só estou querendo agradá-lo.'

		[red]'eu'[reset] -> Sujeito da oração subordinada substantiva objetiva direta/completiva direta.
		[red]'estou querendo agradá-lo'[reset] -> locução verbal ( verbo auxiliar + verbo gerúndio ) -> Predicado da oração subordinada
		[red]'só'[reset] -> Advérbio de exclusividade, modificando o verbo.
		[red]Verbo principal[reset] : [yellow]'agradar'[reset] -> [red]VTD[reset] // [yellow]'lo'[reset] -> [red]Objeto Direto[reset] ( pronome oblíquo átono que se refere ao pronome pessoal do caso reto 'ele' )
			Seria a mesma coisa que [yellow]'agradar ele'[reset] <- [yellow]'ele'[reset] <- [red]Objeto Direto[reset]



Questão.40
Ano: 2025 / Banca: Universidade do Extremo Sul Catarinense - UNESC
Prova: UNESC - InoversaSul - Professor de Ensino Médio - Área: Língua Portuguesa - 2025

"Duas das páginas trazem desenhos de Miguel, neto de Ruth, [yellow]que é designer."[reset]

A oração destacada é uma oração:

A. Subordinada adjetiva.
B. Subordinada substantiva subjetiva.
C. Subordinada Substantiva objetiva direta.
D. Subordinada adverbial.	


		[green]Alternativa 'A' a correta. O termo sublinhado está qualificando o SUJEITO.[reset]

[red]Análise sintática da frase:[reset]


	[red]Oração Principal:[reset]

		'Duas das páginas trazem desenhos de Miguel, neto de Ruth,...' <- [red]Sujeito[reset]

[yellow]'Duas das páginas...'[reset] -> [red]Sujeito[reset] núcleo: 'Duas', 'das páginas' -> [yellow]Complemento Nominal[reset] -> Não expressa posse direta, mas relação de parte-todo.
	[yellow]'...trazem desenhos de Miguel, neto de Ruth,...'[reset] -> [red]Predicado Verbal[reset]
			Verbo 'trazem' -> (Eles) trazem -> 3º pessoa do plural do presente do indicativo ( VTD )
				quem traz, traz algo: [yellow]'desenhos de Miguel'[reset] <- [red]Objeto Direto[reset]
						[yellow]'de Miguel'[reset] -> [red]Adjunto Adnominal[reset] ( desenhos são do Miguel )

		[yellow]'... neto de Ruth...'[reset] -> [red]Aposto explicativo[reset]
'neto' não é um adjetivo e sim um aposto explicativo, qualificando com informação adicional de 'Miguel', além disso, 'neto' é substantivo concreto (pessoa)
			[yellow]'de Ruth' -> indica posse ou relação de parentesco. (posse parental)

	[red]Oração subordinada: Adjetiva explicativa[reset]

		[yellow]'...que é designer.'[reset] <- Está qualificando o neto de Ruth -> [red]Predicativo do sujeito[reset]

	[yellow]'que'[reset] -> Pronome relativo que liga a oração principal a subordinada, retoma o nome 'Miguel', não retoma 'Ruth' por que 'Ruth' está separado por vírgulas
e é aposto explicativo, portanto, retoma 'Miguel', sendo assim, o pronome relativo 'que' tem função sintática de SUJEITO da oração subordinada.
		verbo [yellow]'é'[reset] de ligação // [yellow]'designer'[reset] -> Adjetivo ( atribuição ao Miguel ) e predicativo do sujeito.

	A oração é subordinada adjetiva explicativa por que tem vírgula antes do pronome relativo, acrescenta informação extra sobre Miguel e o ponto final substitui a vírgula final.

Questão 41.
Ano: 2024 / Banca: COPEVE/UFAL - FUNDEPES
Prova: COPEVE/UFAL - FUNDEPES - Prefeitura de Viçosa - Auxiliar de Consultório Dentário - 2024
O outro sujeito inútil ( I ) que nos apareceu era muito diferente. 
Gordo, bem vestido, perfumado e falador, tão falador ( II ) que ficávamos enjoados com as lorotas dele. 

No fragmento textual, há duas orações em destaque que apresentam sentido de:

A. ( I ) tempo e ( II ) causa.
B. ( I ) explicação e ( II ) causa.
C. ( I ) restrição  e ( II ) finalidade.
D. ( I ) restrição  e ( II ) consequência.
E. ( I ) explicação e ( II ) consequência.

Vamos fazer uma análise sintática do período:


O outro sujeito inútil ( I ) que nos apareceu era muito diferente. 

	[red]Oração principal:[reset]

	'O outro sujeito inútil (...) era muito diferente.' -> [red]Sujeito[reset] ( núcleo[reset]: 'sujeito'[reset],'inútil'[reset] -> Adjetivo[reset])
		 'o' -> Artigo definido ( adj.Adn )[reset], 'outro' -> Pronome Adjetivo indefinido (adj. Adn)[reset]

	'...era muito diferente.' -> [red]Predicado nominal[reset]

		'era'[reset] -> Verbo SER na 3º pessoa do singular do pretérito imperfeito do indicativo ( usado para indicar hábitos no passado )
	'...muito diferente.' -> [red]Predicativo do Sujeito[reset]

	[red]Oração Subordinada:[reset]

		'...que nos apareceu...'[reset] -> subordinada adjetiva restritiva ( restringindo o sujeito em questão )

		[red]'que'[reset] -> pronome relativo que introduz a oração e liga o SUJEITO a oração subordinada.
	Além disso, retoma o nome 'sujeito', sendo assim, o pronome é o SUJEITO da oração subordinada.
		[red]'apareceu'[reset] -> ele apareceu -> verbo na 3º pessoa do singular do presente do indicativo. (Verbo transitivo indireto)
		quem aparece, aparece para alguém, a alguém... -> [red]'nos'[reset] -> Objeto indireto ( pronome pessoal oblíquo átono )


Portanto o primeiro período apresenta um sentido RESTRITIVO, sendo assim podemos eliminar as alternativas 'a','b','e'. Sobrando somente a 'c' e 'd'.

Análise do segundo período:[reset]

Gordo, bem vestido, perfumado e falador, tão falador que ficávamos enjoados com as lorotas dele. 

[yellow]'Gordo, bem vestido, perfumado e falador,[reset] -> série de adjetivos que caracterizam o sujeito [red]( Predicativos do sujeito )[reset]  -> [blue]Sujeito Oculto[reset]

	[blue]'...tão falador que ficávamos enjoados com as lorotas dele.[reset]' <- [yellow]Oração subordinada adverbial consecutiva[reset]
		
	[yellow]'tão... (falador) que...'[reset] é conjunção que liga uma oração a outra que expressam um fato mencionado na oração principal. 
					[green]Uma oração subordinada consecutiva a oração principal.[reset]
			 Outros exemplos incluem [yellow]"tanto...que"[reset], [yellow]"de tal forma...que"[reset] e [yellow]"de modo que".[reset]

	[blue]Conjunções Consecutivas[reset]: Estabelecem uma relação de causa e consequência entre duas orações, 
			sendo que a oração introduzida pela conjunção consecutiva é subordinada à principal. 
					Exemplo: "Falou tão alto que todos ouviram."

	[blue]Conjunções Coordenativas:[reset] Ligam orações ou termos independentes entre si, sem que uma oração subordine a outra. 
					Exemplo: "Falou alto [blue]e[reset] todos ouviram."


		[blue]'tão falador que[reset] ficávamos enjoados com as lorotas dele.' -> [blue]Oração subordinada adverbial consecutiva[reset]
						[blue]'tão...que'[reset] -> [red]conjunção consecutiva[reset]
			[red]Conjunções Consecutivas:[reset] Estabelecem uma relação de causa e consequência entre duas orações, 
			sendo que a oração introduzida pela conjunção consecutiva é subordinada à principal
			[red]'ficávamos'[reset] -> [yellow]3º pessoa do plural do pretérito imperfeito do indicativo[reset] -> [blue]verbo de ligação [reset]
					quem que ficava enjoado? Sujeito oculto da oração subordinada (nós)
			[yellow]'enjoados'[reset] -> [red]Predicativo do sujeito [reset] // [red]'com as lorotas dele' [reset]-> [blue]Adjunto Adverbial de causa/motivo [reset]

As orações subordinadas adverbiais exercem função de adjunto adverbial na oração principal, indicando circunstâncias como tempo, causa, 
condição, comparação, consequência, entre outras, intensidade.

As consecutivas, especificamente, indicam a circunstância de consequência, isto é, o efeito de algo mencionado antes.

Toda oração consecutiva é subordinada adverbial, pois adiciona uma circunstância de consequência ao verbo da oração principal.

				Portanto, a alternativa 'D' é a correta. Sentido de consequência.


Questão.42
Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 7 - Analista Judiciário - Área Judiciária Pós-Edital - 2024 - 1º Simulado

No trecho “Os resultados destacam que a ansiedade crônica está associada a um risco maior de demência”, 
a oração “que a ansiedade crônica está associada a um risco maior de demência” exerce a função de:

A. oração subordinada substantiva completiva nominal.
B. oração subordinada substantiva objetiva direta.
C. oração subordinada substantiva subjetiva.
D. oração subordinada substantiva predicativa.
E. oração subordinada substantiva apositiva.


	Os resultados destacam que a ansiedade crônica está associada a um risco maior de demência.

	[red]Oração principal:[reset]
		
		Os resultados destacam... <- [red]Sujeito[reset]
		quem destaca, destaca [yellow]ISSO[reset] -> [blue]'...que a ansiedade crônica está associada a um risco maior de demência.'[reset] -> [red]Objeto Direto[reset]
		
		[yellow]ISSO[reset] o quê? [yellow]ISSO[reset] é substantivo genérico -> se refere :[yellow]'os resultados'[reset] -> substantivo -> [yellow]'... que a ansiedade...'[reset] <- [red]Objeto Direto[reset]

	[red]Oração Subordinada:[reset]  substantiva objetiva direta a qual exerce função sintática de Objeto Direto do verbo 'destacam'


		'...que a ansiedade crônica está associada a um risco maior de demência.'

		[yellow]'que'[reset] -> Conjunção integrante que introduz a oração subordinada substantiva objetiva direta
		[yellow]'está associada a um risco maior de demência.'[reset] -> [red]Predicado Nominal[reset]

		[yellow]'a ansiedade crônica'[reset] <- Sujeito da oração subordinada 
	[yellow]'está associada'[reset] -> locução verbal (verbo auxiliar de ligação + verbo particípio usado como predicativo, valor de adjetivo)
		 Embora seja particípio do verbo “associar”, aqui tem valor adjetivo, pois:
			Não indica ação (não é verbo principal) e sim indica estado ou característica do sujeito. 
		[yellow]'associada a um risco maior de demência'[reset] -> Predicativo do sujeito
		[yellow]'de demência'[reset] -> Complemento nominal de 'risco'

[red]Exemplo comparativo:[reset]

[red]Verbo:[reset]

O médico associou a ansiedade ao risco de demência.
(aqui, “associou” é verbo no pretérito perfeito do indicativo)

[red]Adjetivo:[reset]

A ansiedade [yellow]está associada[reset] a um risco maior.
(aqui, “associada” = adjetivo, predicativo do sujeito)


Questão.43
Ano: 2024 / Banca: Instituto de Desenvolvimento e Capacitação - IDCAP
Prova: IDCAP - Prefeitura de Barra do Rocha - Professor - Área: Geografia - 2024

"As queimadas que aconteceram em São Paulo nos últimos dias foram extraordinárias."

Em relação à estrutura de formação do período acima, analise as afirmativas:

I. Há uma oração subordinada adjetiva.
II.Há uma oração subordinada completiva nominal.
III.O termo "extraordinárias" tem valor de predicativo do sujeito.
IV. O período é formado por predicado nominal e predicado verbal.

Estão corretas:

A. Apenas I e IV.
B. Apenas II, III e IV.
C. Apenas I, III e IV.
D. Apenas I, II e III.


	'As queimadas (...) foram extraordinárias.' <- [red]Oração Principal[reset]

	'As queimadas' -> [red]Sujeito[reset] // '...foram extraordinárias.' -> [red]Predicado nominal[reset]

	[red]Oração subordinada:[reset]

	[yellow]'...que aconteceram em São Paulo nos últimos dias...'[reset] <- restringindo as queimadas, especificando as que aconteceram em SP -> [yellow]sentido Adjetivo[reset]	
		Portanto, o 'que' é pronome relativo que retoma o sujeito 'as queimadas' e liga a oração subordinada adjetiva restritiva.

[red]Cuidado para não confundir com as completivas nominais as quais costumam a depender de nomes abstratos e quase sempre precedidos de uma preposição.[reset]

	O verbo 'acontecer' é intransitivo e não possui nenhum nome que caracterize o sujeito, não há predicativo. ( sem complementos )
		Sendo assim, o núcleo do predicado é um verbo 'aconteceram' -> Predicado Verbal
	  [yellow]'em São Paulo'[reset] -> [red]Adjunto Adverbial de lugar[reset] // [yellow]'nos últimos dias'[reset] <- [red]Adjunto Adverbial de tempo[reset]

						[green]Portanto, a alternativa correta é a 'C'.[reset]

Questão 44.
Ano: 2024 / Banca: Instituto Social da Cidadania - Juscelino Kubitschek - Instituto JK
Prova: Instituto JK - Prefeitura de Nina Rodrigues - Técnico em Enfermagem - 2024

“Só quando terminamos o namoro, percebi que gostava tanto dele.” 

No período, temos:

A. Três orações, sendo 1 principal, 1 coordenada assindética, 1 subordinada substantiva subjetiva.
B. Três orações, sendo todas coordenadas assindéticas.
C. Três orações, sendo 1 subordinada adverbial temporal, 1 principal e 1 subordinada substantiva subjetiva.
D. Três orações, sendo 1 subordinada adverbial temporal, 1 principal e 1 subordinada substantiva objetiva direta.

[blue]'Só quando terminamos o namoro'[reset] -> [red]subordinada adverbial temporal[reset]
[blue]'(Eu) percebi...'[reset] <- [red]oração principal[reset]
[blue]'...que gostava tanto dele.'[reset] <- [red]substantiva objetiva direta[reset]

						Alternativa correta é a 'D'.


[red]Análise sintática do período:[reset]

	Oração subordinada adverbial temporal:

	Por si só, o vocábulo 'só' não inicia orações subordinadas mas sim modifica o sentido de outro termo (verbo, adjetivo, advérbio)
Agora o vocábulo 'quando' introduz sim, oração subordinada adverbial temporal ->  pois indica tempo relacionado à ação da oração principal.
						É uma conjunção subornativa temporal 
	
[red]'terminamos'[reset] -> [blue](nós)[reset] terminamos -> 1º pessoa do plural do pretérito perfeito do indicativo 
 	[red]Verbo Transitivo Direto:[reset] [green]'o namoro'[reset] <- [red]Objeto Direto[reset] // [red]Sujeito elíptico 'nós'[reset]

	A primeira oração antes da vírgula é uma subordinada adverbial temporal.

	[red]Oração principal:[reset]

[blue](eu) percebi[reset] -> [red]Sujeito oculto, elíptico ou desinencial[reset] // quem percebi, percebi algo, percebi [yellow]ISSO.[reset] 
[yellow]ISSO[reset] o que? [blue]'...que gostava tanto dele.'[reset] -> [green]substantiva objetiva direta[reset]
	[yellow]'que'[reset] faz uso de uma conjunção integrante para ligar duas orações. quem gostava, gostava de alguém: [yellow]'dele'[reset] -> [red]Objeto Direto[reset] 
				[yellow]'tanto'[reset] -> [blue]Advérbio de intensidade[reset]

	[red]2º oração subordinada substantiva objetiva direta:[reset]

	percebi [yellow]ISSO, ISSO[reset] <- substantivo genérico

	[yellow]'...que gostava tanto dele.'[reset] -> Objeto Direto do verbo 'percebi' -> [blue]substantiva objetiva direta[reset]
		[yellow]'que'[reset] faz uso de uma conjunção integrante para ligar duas orações.
	 quem gostava, gostava de alguém: [yellow]'dele'[reset] -> [red]Objeto Direto [reset] [green]( contração da preposição 'de' com o pronome pessoal oblíquo 'ele' )[reset]
		[yellow]'tanto'[reset] -> [blue]Advérbio de intensidade[reset]

Questão 45.
Ano: 2024 / Banca: Escola de Sargentos das Armas - ESA
Prova: ESA - ESA - Sargento - Área: Geral Pós-Edital - 2024 - 3º Simulado

No trecho "As crianças e jovens podem trazer para dentro de casa esse assunto muito importante e podem inclusive colaborar para que haja conscientização dos pais,
"a oração "para que haja conscientização dos pais" desempenha a função de:

A. Complemento verbal, especificando a ação principal mencionada.
B. Oração subordinada adverbial final, indicando o propósito da ação descrita na oração principal.
C. Oração subordinada adjetiva restritiva, qualificando o substantivo "assunto."
D. Oração subordinada substantiva completiva nominal, completando o sentido da expressão "colaborar."
E. Oração coordenada explicativa, justificando a ação descrita anteriormente.

[red]Alternativa 'B'[reset] -> [green]CORRETA[reset]

As crianças e jovens podem trazer para dentro de casa esse assunto muito importante e podem inclusive colaborar [yellow]para que haja conscientização dos pais.[reset]

	[red]Por que não é oração principal?[reset]

	[yellow]No período composto por subordinação,[reset] a oração principal é aquela que não depende sintaticamente de outra, mas que possui uma subordinada dependente dela.
	[yellow]No período composto por coordenação, [reset]não há oração principal no sentido sintático. Há orações coordenadas, que podem ser:

	[red]Assindéticas:[reset] sem conjunção.

	[red]Sindéticas:[reset] com conjunção (aditivas, adversativas, alternativas, conclusivas ou explicativas).

O período completo não há oração principal. E sim um período composto por coordenação. Não há oração principal no ponto de vista sintático. 
Se fosse um período composto por subordinação, a oração principal possuiria uma subordinada dependente dela. 

[blue]Um período composto por coordenação é aquele formado por duas ou mais orações independentes entre si.[reset] 
		[green]Cada oração tem sentido próprio e pode existir separadamente.[reset]

No entanto, em termos de sentido discursivo ou didática básica, professores às vezes chamam a primeira oração de “principal” no contexto do período, 
para diferenciá-la das demais orações coordenadas que vêm depois. Mas tecnicamente, no período composto por coordenação:

➡️ Não há oração principal
➡️ Há orações coordenadas (assindética e sindética)



	[red]Oração coordenada assindética:[reset] -> É uma oração coordenada sem conjunção.

	[yellow]'As crianças e jovens...'[reset] -> [red]Sujeito Composto[reset] // [yellow]'podem trazer'[reset] -> [red]locução verbal[reset]  
		[yellow]'podem'[reset] -> VTD -> [red]Objeto Direto[reset] -> [yellow]'trazer'[reset]
		quem traz, traz : [yellow]'esse assunto muito importante'[reset] -> [red]Objeto Direto [reset]
	[yellow]'muito importante'[reset] -> Adjunto Adnominal // [yellow]'...para dentro de casa'[reset] -> [red]Adjunto Adverbial de lugar[reset]

	[red]Predicado verbal:[reset] [yellow]'...podem trazer [reset]para dentro de casa esse assunto muito importante...'

		[yellow]'e' [reset] -> [blue]conjunção coordenativa aditiva [reset]

	[red]Oração coordenada sindética aditiva:[reset]

	[yellow]'...podem inclusive colaborar para que haja conscientização dos pais.'[reset]

				[green]É uma oração coordenada introduzida por conjunção coordenativa.[reset]

	 [blue]Essa oração é coordenada sindética aditiva, [reset]porque: Tem mesmo sujeito da primeira (as crianças e jovens). Está ligada pela conjunção “e”, que indica adição.
					Possui sentido independente, mas soma ação à primeira oração.

	[yellow]'podem (...) colaborar'[reset] -> [green]locução verbal[reset] // [yellow]'inclusive'[reset] -> [blue]Adjunto Adverbial de inclusão[reset]

	[red]'podem'[reset] -> VTD -> [red]'colaborar'[reset] -> Objeto direto // [red]'colaborar'[reset] -> V.T.Indireto -> quem colabora, colabora para: [yellow]'para que haja conscientização dos pais'[reset] <- [blue]Obj.Indireto[reset]

	[red]Predicado verbal:[reset] -> [yellow]'...podem inclusive colaborar [reset] para que haja conscientização dos pais.'

	Por quê são duas orações assindéticas?

		Por que cada parte tem verbo próprio:
	
			“podem trazer…” //  “podem colaborar…”

		✔ Ambas têm sujeito comum: as crianças e jovens.

		✔ Não há relação de dependência sintática, ou seja, uma não completa o sentido sintático da outra. Elas se somam em sentido (adição).

	[red]Oração subordinada Adverbial final desenvolvida[reset]

		'...para que haja conscientização dos pais.' 

	[yellow]'para que'[reset] -> conjunção subordinativa adverbial final e introduz orações subordinadas adverbiais finais, indicando finalidade.

		[red]'haja'[reset] -> [green](que)[reset] ele haja -> [red]3º pessoa do singular do presente do subjuntivo [reset]-> VTD -> [blue]'concientização dos pais.'[reset] <- [red]Objeto Direto[reset]
	[red]'conscientização dos pais.'[reset] -> [green]'dos pais'[reset] -> [blue]'os pais são conscientizados'[reset] -> quem será conscientizado? [blue]'os pais'[reset] <- paciente -> [red]Complemento nominal[reset]


Gostei dessa questão. Há detalhes a serem observados que causam confusão...

O período completo não há oração principal. E sim um período composto por coordenação. Não há oração principal no ponto de vista sintático. 
Se fosse um período composto por subordinação, a oração principal possuiria uma subordinada dependente dela.
Um período composto por coordenação é aquele formado por duas ou mais orações independentes entre si. Cada oração tem sentido próprio e poderia existir separadamente.

Agora, pelo ponto de vista didático, alguns professores chamam a primeira oração de 'principal' para diferenciá-las das demais.
[yellow]Mas tecnicamente, período composto por coordenação não há oração principal.[reset]

No período em questão temos duas orações coordenadas:

[red]1º oração:[reset] [blue]assindética[reset] [yellow]( sem conectivos , sem conjunção )[reset]

'As crianças e jovens podem trazer para dentro de casa esse assunto muito importante... e <- [blue]Conjunção coordenativa aditiva[reset]


[red]2º oração: [reset] [blue]sindética aditiva[reset] [green]( iniciada por conjunção )[reset] -> Possui sentido independente, mas soma ação à primeira oração.

[blue](e)[reset] ....podem inclusive colaborar para que haja conscientização dos pais.

Agora dentro da oração coordenada sindética aditiva temos uma subordinada adverbial iniciada pela conjunção subordinativa adverbial indicando finalidade, [blue]'para que' ou 'para'[reset]:

[yellow]'...para que haja conscientização dos pais.' [reset]

[red]Mas atenção![reset]

A conjunção [yellow]'para'[reset] seguida do verbo no infinitivo tem finalidade reduzida no infinitivo. 
Agora [yellow]'para que'[reset] + verbo conjugado (geralmente no subjuntivo) é uma adverbial final desenvolvida.

	[yellow]'...para que haja conscientização dos pais.' [reset]

[red]Exemplo de uma reduzida:[reset]

Estudo muito [red] para [reset]aprender rápido. <- [yellow]'para'[reset] -> Introduzindo uma oração subordinada adverbial final reduzida no infinitivo


Questão 46.
Ano: 2024 / Banca: Instituto Brasileiro de Educação, Seleção e Tecnologia - Instituto IBEST
Prova: Instituto IBEST - Prefeitura de Muriaé - Agente Comunitário de Saúde - 2024 

O fazendeiro foi ao mercadinho de sua cidade e, como o pessoal estava demorando a empacotar suas compras, começou a puxar assunto com o dono do estabelecimento:

A oração “como o pessoal estava demorando a empacotar suas compras” (linhas 2-3) classifica-se como:

A. subordinada substantiva apositiva.
B. subordinada adjetiva explicativa.
C. subordinada adverbial causal.
D. subordinada adverbial temporal.


	[red]Temos uma oração coordenada assindética aqui:[reset]

	[yellow]'O fazendeiro foi ao mercado de sua cidade...'[reset] -> [red]Sujeito[reset] -> [yellow]'O fazendeiro'[reset] -> Núcleo do Sujeito 
	[yellow]'foi'[reset] -> Pretérito perfeito do indicativo -> 3º pessoa do singular -> verbo 'IR' -> O verbo 'ir' exige complemento, quem vai, vai a algum lugar.
		[yellow]'...ao mercadinho de sua cidade'[reset] <- [red]Objeto indireto[reset] // [red]Predicado verbal[reset] : [yellow]Verbo de significado (ação)[reset]

Alguns gramáticos analisam verbos de movimento (ir, chegar, sair, voltar) como:

[red]Visão tradicional[reset]				Visão moderna
[blue]Intransitivos[reset] + adjunto adverbial de lugar	Transitivos indiretos + objeto indireto


Em provas de bancas tradicionais (CESPE, FGV, FCC, Consulplan), considerar:

[red]➡️ “foi” como verbo transitivo indireto, pois exige complemento introduzido por preposição (a).[reset]

[yellow]'... mercadinho de sua cidade.'[reset] <- [blue]'de sua cidade'[reset] <- [green]Adjunto Adnominal ( o termo indica posse e 'mercadinho' é substantivo concreto )[reset]

	[yellow]'e'[reset] -> conjunção coordenativa aditiva

	[red]2º oração coordenativa sindética aditiva:[reset]

[yellow]'(e) ...começou a puxar assunto com o dono do estabelecimento...'[reset] -> oração coordenativa sindética aditiva

	verbo [yellow]'começou'[reset] é transitivo indireto por que quem começa , começa a: [yellow]'a puxar assunto com o dono do estabelecimento.[reset] <- [red]Complemento verbal é indireto[reset]
		[yellow]'assunto'[reset] -> substantivo abstrato que existe complemento -> [yellow]'...com o dono do estabelecimento...'[reset] <- [red]Complemento Nominal[reset]
			[yellow]'dono do estabelecimento'[reset] <- [green]'do estabelecimento'[reset] <- [red]Complemento nominal[reset]

	[red]Atenção![reset]

	No meio do período temos uma oração subordinada à primeira oração, onde temos o sujeito explícito.
Tecnicamente a oração causal depende sintaticamente da principal. Mas a oração TODA.

			'...como o pessoal estava demorando a empacotar suas compras...'

- A oração causal depende sintaticamente da principal, pois exerce a função sintaxe de adjunto adverbial de causa.
	
	- A conjunção subordinativa adverbial causal 'como' introduz uma oração subordinada adverbial causal que indica a causa da ação principal.
	
	[red]Análise sintática da oração subordinada:[reset]

	[yellow]'...o pessoal estava demorando a empacotar suas compras...'[reset]

	quem que estava demorando a empacotar?? -> [yellow]'o pessoal'[reset] <- [red]Sujeito da oração [reset]
	[red]'estava demorando'[reset] -> verbo auxiliar + verbo no gerúndio -> A locução verbal é uma ação habitual no passado.
	[red]'estava'[reset] -> Pretérito imperfeito do modo indicativo

Portanto, [yellow]'a empacotar suas compras'[reset] é um oração reduzida de infinitivo com função sintática de adjunto adverbial de finalidade.
	[red]'suas compras'[reset] -> [blue]Objeto direto do verbo 'empacotar'[reset]

	Mas eu considero como complemento verbal indireto. Uma ação habitual no passado em que no contexto precisa de complemento indireto.
		'...estava demorando a que? [yellow]'a empacotar suas compras'[reset] <- [red]Objeto indireto[reset]
		
[red]Exemplos de conjunções subordinadas adverbiais causais:[reset]

 Conjunções causais mais comuns:
- [yellow]porque[reset]
→ Não fui à aula [yellow]porque[reset] estava doente.

- [yellow]como [reset](quando vem no início da frase)
→ [yellow]Como[reset] estava chovendo, ficamos em casa.

- [yellow]já que[reset]
→ [yellow]Já que[reset] você terminou o trabalho, pode sair.

- [yellow]visto que[reset]
→ [yellow]Visto que [reset]não havia vagas, fomos embora.

- [yellow]pois que[reset]
→ [yellow]Pois que [reset]não estudou, não passou.

- [yellow]porquanto[reset]
→ [yellow]Porquanto[reset] não houve acordo, a reunião foi cancelada.

- [yellow]uma vez que[reset]
→ [yellow]Uma vez que não há provas, o caso será arquivado.

-[yellow] que [reset](em construções mais formais ou literárias)
→ Não saí, [yellow]que[reset] estava indisposto.

Observações sobre a questão:

A questão dessa banca é bem complicada em outro caso.

[red]É de fato uma oração subordinada no meio de outras orações se for analisar o período completo:[reset]

'O fazendeiro foi ao mercadinho de sua cidade e, como o pessoal estava demorando a empacotar suas compras, começou a puxar assunto com o dono do estabelecimento:'

A oração coordenada é:

'O fazendeiro foi ao mercadinho de sua cidade e começou a puxar assunto com o dono do estabelecimento:'

'O fazendeiro foi ao mercadinho de sua cidade...' <- [yellow]Temos a 1º oração assindética aqui[reset]

'... e começou a puxar assunto com o dono do estabelecimento:' -> [yellow]Temos a 2º oração sindética aditiva[reset]


O grande lance é justamente a oração subordinada da 1º oração. Tecnicamente a oração subordinada adverbial causal depende sintaticamente da principal.
Lembrando que tecnicamente não há oração principal, mas para fins didáticos temos a 1º oração coordenada que podemos dizer que é a oração principal.

'...como o pessoal estava demorando a empacotar suas compras...'

A conjunção subordinativa advervial causal 'como' introduz uma oração subordinada adverbial causal que indica a causa da ação principal.

					[green] Sendo a alternativa 'C' a correta.[reset]

O termo que realmente nos intriga é a locução verbal 'estava demorando'. Muitos gramáticos a consideram como intransitivo. 
E o termo seguinte: '...a empacotar suas compras.' 
É adjunto adverbial finalidade e que a meu ver técnico, não. Mas sim um complemento verbal.

A locução verbal 'estava demorando' é uma ação habitual no passado. O verbo ESTAR está no pretérito imperfeito do indicativo. 
Sendo por isso, uma ação não terminada no passado em que precisa de um complemento verbal e não uma modificação ou circunstância para com a locução. 
No contexto existe o complemento verbal indireto: '...a empacotar suas compras.'

[red]Questão.47[reset]
Ano: 2024 / Banca: SELECON Instituto Nacional de Seleções e Concursos - SELECON
Prova: SELECON - Prefeitura de São Gonçalo - Inspetor de Alunos - 2024 

Em “é preciso embrenhar-se na luta mais árdua de nossas vidas” (5º parágrafo), a oração destacada é classificada como:

A. principal
B. assindética
C. substantiva subjetiva
D. substantiva predicativa


	Dado somente ao contexto apresentado no enunciado é uma oração principal. Alternativa 'A' a correta.

	É preciso [yellow]ISSO, ISSO[reset] (substantivo genérico ), ISSO o quê? '...embrenhar-se na luta mais árdua de nossas vidas.' <- [red]Sujeito oracional[reset]

“embrenhar-se na luta mais árdua de nossas vidas” é uma: Oração subordinada substantiva subjetiva, subordinada à oração principal “É preciso”.

	[yellow]'é' [reset] -> Verbo de ligação e [yellow]'preciso'[reset] é predicativo do sujeito ( qualificando o sujeito )
	[yellow]'se'[reset] -> Pronome reflexivo ( pronome pessoal oblíquo átono ) [yellow]'embrenhar'[reset] -> [red]verbo transitivo indireto[reset]
	[yellow]'embrenhar-se'[reset] -> [red]verbo pronominal[reset]
	quem se embrenha, se embrenha na: [yellow]'...na luta mais árduas de nossas vidas...'[reset] <- [red]Objeto Indireto[reset] [blue](preposição "em" + artigo "a" = 'na' -> Contração )[reset]
	[yellow]'na luta mais árduas de nossas vidas' [reset] <- Pode ser considerado um Adjunto Adverbial Circunstancial / [red]Objeto Indireto[reset]
	[yellow]'mais árduas'[reset] -> [red]Adjunto Adnominal [reset]( [yellow]'árdua'[reset] -> adjetivo e [yellow]'mais'[reset] é advérbio em que qualificam 'luta' )
	[yellow]'de nossas vidas'[reset] -> [red]Adjunto Adnominal[reset]

- [red]“mais árdua”[reset]      → adjunto adnominal (adjetivo que qualifica “luta”)
- [red]“de nossas vidas”[reset] → adjunto adnominal também, pois “nossas vidas” são agentes da luta — somos nós que lutamos. 'nossas' -> pronome possessivo
Se fosse “a luta pela educação”, o termo “pela educação” seria complemento nominal, pois a educação é o alvo da luta, ou seja, recebe a ação.

[red]Questão.48[reset]
Ano: 2024 / Banca: Fundação Carlos Chagas - FCC
Prova: FCC - TRT 20 - Técnico Administrativo - Área Administrativa - 2024

Por isso, [yellow]antes sumirem de por completo[reset], tomei coragem para reviver as histórias que povoaram minha infância e adolescência. 
No contexto em que se insere, a oração sublinhada expressa ideia de:

A. finalidade.
B. tempo.
C. condição.
D. concessão.
E. proporcionalidade.

[yellow]'Por isso'[reset] <- Locução adverbial de causa/consequência - [red]Sintaxe[reset] -> Adjunto Adverbial de causa

[yellow]'...antes sumirem de por completo...'[reset] -> [red]Sintaxe[reset] : [yellow]Adjunto Adverbial de tempo[reset] -> Expressão que indica uma circunstância temporal em que a ação ocorreu.

	[yellow]'antes' [reset]-> [blue]advérbio de tempo que funciona como uma conjunção temporal para a oração subordinada adverbial reduzida no infinitivo.[reset]
	O verbo SUMIR no contexto está no infinitivo pessoal na 3º pessoa do plural 'sumirem' -> núcleo da oração subordinada, Predicado VERBAL
		[yellow]'...de por completo.'[reset] -> locução adverbial de modo que funciona como Adjunto Adverbial de modo
			O sujeito [yellow]'elas'[reset] -> Sujeito Oculto referente 'as histórias' -> [red]Sujeito da oração principal[reset]
	A oração subordinada inteira funciona como Adjunto Adverbial de tempo e é subordinada adverbial temporal reduzida de infinitivo.

[red]Observação:[reset]

Se fosse oração desenvolvida [yellow](“antes que sumissem”),[reset] [blue]“antes que”[reset] é [yellow]locução conjuntiva subordinativa temporal.[reset]


[red]Oração Principal:[reset]

'...tomei coragem para reviver as histórias que povoaram minha infância e adolescência.' 
	
	[yellow]'tomei'[reset] -> VTD // [yellow]'coragem'[reset] -> [red]Objeto Direto[reset] //
	 '...para reviver as histórias que povoaram minha infância e adolescência' -> [yellow]Adjunto Adverbial de finalidade[reset]
	[red]Sujeito:[reset] [yellow]'as histórias'[reset] -> [green]As histórias tomei coragem para reviver..'[reset] // [red]Predicado verbal:[reset] núcleo do predicado 'tomei'.
	Aqui, [yellow]“para reviver…”[reset] não completa “tomar”, mas indica para que foi tomada a coragem. Portanto, adjunto adverbial de finalidade.

[red]Oração Subordinada:[reset] [yellow]Adjetiva restritiva[reset]

	'...que povoaram minha infância e adolescência. '

	[red]Porque?[reset]

	[yellow]'que'[reset] -> pronome relativo que retoma [blue]'histórias'[reset] -> [blue]Sujeito da oração principal[reset]
		Não são quaisquer histórias, são aquelas [yellow]que povoaram minha infância e adolescência. [reset] -> [blue]Restringindo e especificando 'as histórias'.[reset]
	 Portanto, o que inicia uma oração subordinada adjetiva restritiva, tem função sintática de [yellow]SUJEITO[reset], pois retoma o sujeito da oração principal.
		Seu predicado é [yellow]VERBAL.[reset]
	[yellow]'povoaram'[reset] -> 3º pessoa do plural do modo indicativo pretérito perfeito - [red]Verbo transitivo direto[reset] // [yellow]'minha infância e adolescência'[reset] -> [red]Objeto Direto[reset]



[red]Observações:[reset]

Essa questão me fez ter uma atenção nas locuções adverbiais : [yellow]'antes'[reset] e [yellow]'antes que'[reset] e nos verbos:

"...antes sumirem de por completo..."

O [yellow]'antes'[reset], isolado, é advérbio de tempo que funciona como conjunção para a oração subordinada adverbial reduzida no infinitivo.
O verbo [yellow]SUMIR[reset] está no infinito pessoal, não precisa de locução. Precisa ter [yellow]SUJEITO.[reset]

[blue]Se tiver sujeito definido[reset] → [yellow]infinitivo pessoal.[reset] [red]( O verbo está conjugado )[reset] -> [blue]Eles sumirem...[reset] ( [yellow]futuro do subjuntivo[reset] : [blue]...(se) eles sumirem...[reset] -> 3º pessoa do plural )
[blue]Se não tiver sujeito[reset] → [yellow]infinitivo impessoal.[reset] [red]( Forma pura, sem flexão )[reset]

Agora se o verbo estivesse em seu [yellow]modo subjuntivo 'sumissem'[reset] seria necessário colocar o vocábulo 'que' para formar uma locução conjuntiva adverbial temporal desenvolvida.
e a oração se tornaria subordinada adverbial temporal desenvolvida:

[yellow]'...antes que[reset] sumissem de por completo...' <- [blue]Oração subordinada adverbial temporal desenvolvida[reset] ( não é o caso em questão )

A oração subordinada reduzida indica uma circunstância temporal em que a ação ocorreu da oração principal. Portanto, alternativa 'B'.


[red]Questão.49[reset]
Ano: 2024 / Banca: Instituto Quadrix - Quadrix
Prova: Quadrix - CRMV AL - Agente Fiscal - 2024 

A falsa médica disse que o animal teve uma parada cardíaca durante a cirurgia e morreu, mas não entregou o corpo da gata à tutora Christiane Duarte, 
que pagou R$ 50 adiantado e pagaria o restante após a castração.

A oração “mas não entregou o corpo da gata à tutora Christiane Duarte” (linhas 11 e 12) classifica-se como coordenada.

C.Certo
E.Errado

		[red]Antes de responder a questão vamos fazer a análise sintática:[reset]

[yellow]A falsa médica [reset] -> [red]Oração principal[reset] -> [yellow]'A falsa médica...'[reset] <- [red]Sujeito [reset]

[yellow]'...disse que o animal teve uma parada cardíaca durante a cirurgia e morreu..'[reset] <- [red]Predicado verbal[reset]

'...disse que o animal teve uma parada cardíaca durante a cirurgia e morreu..' <- [red]Oração subordinada substantiva objetiva direta[reset]

	[green]Por que?[reset]

	A falsa médica disse [yellow]ISSO, ISSO[reset] é o substantivo genérico. Por isso é subordinada substantiva.
		A oração exerce função sintática de objeto direto. Completa o sentido do verbo 'DIZER'.

	O vocábulo [yellow]'que'[reset] é uma conjunção integrante e introduz a oração subordinada substantiva objetiva direta.
[yellow]'o animal'[reset] -> [red]Sujeito da oração subordinada.[reset] [yellow]'teve'[reset] -> 3º pessoa do singular do pretérito perfeito do indicativo.
	[yellow]'teve'[reset] -> [red]V.T.D[reset] // [yellow]'... uma parada cardíaca...'[reset] <- [red]Complemento verbal direto[reset] // 
		[yellow]'...durante a cirurgia...'[reset] <- [red]Adjunto Adverbial de tempo [reset]

	[yellow]'...e morreu...'[reset] <- [blue]'e'[reset] -> [red]conjunção coordenada aditiva[reset]
	[yellow]'morreu'[reset] -> [red]verbo intransitivo[reset] // [yellow]'ELE'[reset] -> [red]Sujeito Oculto e refere-se ao [reset] -> [blue]'o animal'.[reset] <- [red]Oração coordenada sindética aditiva[reset]

O objeto direto é a oração subordinada substantiva objetiva direta. Dentro dessa oração subordinada, há orações coordenadas: 
					uma assindética e uma sindética aditiva.
	   		    	Estão ligadas pela conjunção aditiva coordenativa 'e'.

[yellow]'...mas não entregou o corpo da gata à tutora Christiane Duarte.'[reset] <- [blue]Oração coordenada sindética adversativa [reset]

[yellow]'mas'[reset] -> [blue]Conjunção coordenativa adversativa[reset] // [yellow](ela)[reset] <- [blue]Sujeito oculto referente a 'a falsa médica'[reset] 
					[red]'não'[reset] -> [yellow]Advérbio de negação[reset]

[red]Orações coordenadas:[reset]

Não exerce função sintática em relação à oração anterior (não é objeto, sujeito ou adjunto).
Tem sentido relativamente completo, mas conecta-se à anterior por relação lógica (neste caso, oposição).
 O fato de o sujeito estar explícito na anterior e oculto nesta não torna a oração subordinada.
[blue]✔ Continua coordenada, pois a ligação é feita por conjunção coordenativa (“mas”), e ela não exerce função sintática na oração anterior.[reset]

[red]Atenção![reset]
Sobre a vírgula antes de [blue]“mas”[reset] -> [yellow]Regra geral de pontuação:[reset]

[red]Antes de conjunções coordenativas adversativas [reset] -> [yellow](mas, porém, contudo, todavia, entretanto, no entanto),[reset] usa-se vírgula antes, obrigatoriamente.

	quem entrega, entrega algo: [yellow]'...o corpo da gata' [reset]-> [red]Objeto Direto[reset] // [yellow]'à tutora Christiane Duarte.'[reset] <- [red]Objeto Indireto[reset]
	[red]'o corpo da gata'[reset] -> [yellow]'da gata'[reset] -> [blue] Adjunto Adnominal [reset] -> [green]( ...o corpo é dela, sentido de posse,[reset] [blue]'da gata' )[reset]

	[red]Temos aqui uma oração subordinada:[reset] Adjetiva Restritiva

[yellow]'...que pagou R$ 50 adiantado e pagaria o restante após a castração.[reset]

O vocábulo [yellow]'que'[reset] refere-se à [yellow]'tutora Christiane Duarte',[reset] portanto é um pronome relativo que retoma o termo anterior e introduz uma oração subordinada.
	A tutora que pagou adiantado o restante após a castração, ou seja, uma restrição ao substantivo. Restringindo somente aquela tutora que fez isso.
						Portanto, uma oração subordinada adjetiva restritiva.

[yellow]'...que pagou R$ 50 adiantado e pagaria o restante após a castração.'[reset] <- [blue] Oração subordinada adjetiva restritiva[reset]
	
[yellow]'pagou'[reset]: [red]VTD [reset]-> [blue]'R$ 50'[reset] <-[red]Complemento Verbal Direto [reset] // [blue]'adiantado'[reset] -> [blue]Predicativo do sujeito [reset]( Adjunto Adverbial de modo )	
	[red]Objeto direto:[reset] [yellow]'...que pagou R$ 50 adiantado e pagaria o restante após a castração.'[reset]
	[yellow]'e' [reset]-> [yellow]conjunção aditiva coordenada [reset]( [red]Função:[reset] [yellow]liga as duas orações coordenadas internas, acrescentando ação.)[reset]
[red]'pagaria' [reset]-> [blue] 1º pessoa do singular [reset]-> [yellow]futuro do pretérito do indicativo (-RIA)[reset] -> [yellow]'o restante' [reset] <- [red]Objeto Direto [reset]
	[yellow]'...após a castração.' [reset] <- [blue]Adjunto Adverbial de tempo[reset]

		Dentro da oração subordinada adjetiva restritiva temos duas orações coordenadas:
					uma sindética e outra assindética

		[yellow]'... pagou R$ 50 adiantado...' [reset]-> [blue]oração coordenada assindética [reset]
		[yellow]'... e '(ela)' pagaria o restante após castração...'[reset] -> [blue]oração coordenada sindética aditiva[reset]

	[yellow]'pagaria'[reset] -> futuro do pretérito (V.T.D) // [yellow]'o restante'[reset] -> [red]Objeto Direto[reset] 
		[red]'após castração'[reset] -> 'após' -> [yellow]Advérbio temporal[reset] (adjunto adverbial de tempo )

		O vocábulo [yellow]'após'[reset] não pode ser preposição para a transitividade [yellow]'pagar'[reset], vejamos:

			[yellow]transitivo direto e indireto[reset] → [green]quando envolve a alguém (quem recebe) e algo (o que se paga):[reset]

					[red]Ex:[reset] Pagou o valor (objeto direto) ao médico (objeto indireto).

		Predicados verbais nas orações coordenadas que por sua vez também é na oração subordinada adjetiva restritiva.

Sim. Ambas possuem predicados verbais, pois:

O núcleo de cada predicado é um verbo que indica ação (pagou, pagaria).

Não há verbo de ligação + predicativo para formar predicado nominal.

A oração subordinada inteira contém essas duas ações, formando dois predicados verbais internos.


	Portanto a questão está correta.

                                

        '''        
    def menu (self):
                self.print_slow('Bem vindo aos estudos da sintaxe para concursos...')
                self.dots()
                while True:
                    try:        
                        indice = int(input('''
                        Estudos da sintaxe:

                        [1] - Introdução aos termos da oração do período composto
                        [2] - Exercícios de fixação: Período Composto
                        [3] - Oração Subordinada Adjetiva ( Restritiva e Explicativa )
                        [4] - Exercícios sobre OSA
                        [5] - Introdução as orações subordinadas adjetivas
                        [6] - 
                        [0] - Sair

                        Escolha: '''))

                        if indice == 1:
                            self.print_slow_2(self.sintaxe_dois())
                        if indice == 2:
                            self.print_slow_2(self.exercicios())     
                        if indice == 3:
                            self.print_slow_2(self.osare()) 
                        if indice == 4:
                            self.print_slow_2(self.exercicios_OS())
                        if indice == 5:
                            self.print_slow_2(self.exercicios_OS())    
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
     
    sintaxe = sintaxe_dois_()
    sintaxe.menu()
