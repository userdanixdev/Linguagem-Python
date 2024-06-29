from time import sleep
import textwrap
import sys

class Morfologia():

    def texto_inicial(self):
        return '''Uma língua se estrutura em torno de verbos e substantivos.\nEssas são as palavras centrais.'''

    def verbo(self):
        return '''Verbo: São palavras que podem indicar ação,fenômenos,posse.'''

    def substantivo(self):
        return '''Substantivo: O nome em que damos as coisas,seres ou conjuntos de seres e objetos,ideias,estados,sentimentos
Em volte deles, existem as classes gramaticais que sempre o acompanham: artigo,pronome,adjetivo,numeral e locução adjetiva.\nAssim como o verbo é acompanhado pelo advérbio.
                NOTA: O ADJETIVO É A PALAVRA QUE CARACTERIZA O SUBSTANTIVO, ATRIBUINDO-LHES QUALIDADE E DEFEITOS
Exemplos:\n\nEle é triste <- Triste é um adjetivo dele\nEle tem tristeza <- Tristeza é um sentimento de estado, um substantivo
Ela é alegre <- Alegre é adjetivo dela\nEla tem alegria <-- Um sentimento de tristeza, um substantivo.
Outro Exemplo importante:\n\nO jovem brasileiro conta com o Estado da Criança e do Adolescente.\n\nPelo contexto da oração o brasileiro é uma qualidade do brasileiro que tem o benefício do Estado.
jovem é o substantivo na oração. Nem todos os jovem contam com o benefício.\n\nEntre os turistas havia um jovem brasileiro e um velho japonês, os dois jovens encantados com a paisagem\n
Substantivos:'turistas','jovem','velho','jovens' <- O numeral dois ao lado da palavra 'jovens' ajuda a identificar os substantivos
Adjetivos:'brasileiro':qualificação e 'japonês' está qualificando o velho.\n\nUm brasileiro jovem tem expectativa de vida de 72 anos, enquanto um japonês jovem tem 81 anos
Pelo contexto da frase, a palavra 'brasileiro' agora é o substantivo e 'jovem' é um atributo do brasileiro. Assim como o 'japonês' é o substantivo a qual o adjetivo é 'jovem'.\n
PC-Vunesp:\n\nNa frase: ''...pareça mais um olhar ....'', a palavra olhar é um substantivo,(Como o artigo 'um' está acompanhando a palavra 'olhar', portanto é um subs.)\nComo na frase:
a) Quero olhar bem em seus olhos e dizer tudo que sinto.[Nesse caso são dois verbos: 'quero' e 'olhar'-Locução Verbal][ERRADO]
b) O jovem nem se dignou olhar para trás.[dignou=verbo,olhar=verbo][ERRADO]
c) Ela se pôs a olhar carinhosamente para o amado.[a = preposição de ligação 'pôs' ao 'olhar' que é verbo mesmo][ERRADO]
d) Esse teu olhar quando encontra o meu fala te tantas coisas [TEU=PRONOME,acompanha o substantivo, portanto é subs][CORRETO]
e) QUando você olhar para mim serei a pessoa mais feliz do mundo..[ERRADO]
'''

    def subs_exemplos(self):

        return '''Exemplos:\n\nMuitos livros,muitas revistas.\nSubs:'livros'\nSubs:'revistas',\n'muitas/muitos':Pronome Indefinido(quantidade indefinida) e não Advérbio.
Livros muitos novos,revistas muito velhas\n'livros':substantivo,\n'muito':advérbio de intensidade para reforçar o adjetivo de livros que são 'novos'
Assim como 'revistas':substantivo,\n'muito':advérbio de intensidade para reforçar o adjetivo de 'revistas' que são 'velhas'.
Tenho livros demais\n\nVerbo:'tenho',\n'livros':Substantivo,\n'demais':Pronome Indefinido pq a palavra 'demais' se relaciona com 'livros' que é substantivo
Eram bastantes ideias interessantes\n\nVerbo:'Eram',\nSubstantivo:'ideias',\nAdjetivo:'interessantes' que qualifica o nome 'ideias',\n'bastantes':Pronome Indefinido
A quantidade é indefinida de idéias e além disso ela possui sua relação com idéias que é substantivo e não com 'eram', o verbo.
Eram idéias bastante interessantes\n\nVerbo:'eram'\nSubstantivo:'ideias',\nAdjetivo:'interessantes' está qualificando idéias que é substantivo porem a palavra 'bastante'
mudou de forma e relação, agora é com o adjetivo 'interessantes' e não mais com 'idéias', portanto,virou um advérbio de intensidade.'''

    def chamada(self):
        return ''' A GRAMÁTICA É A FORMA COMO É ESCRITA, SEU SENTIDO E RELAÇÃO '''

    def verbos_exemplos(self):
        return '''Exemplos:\n\nEstudei demais\n\nVerbo:'estudei',\n'demais':Advérbio de intensidade\n\nTenho livros demais\n\nVerbo:'tenho',\n'livros':substantivos,
'demais':Pronome Indefinido por que a palavra 'demais' se relaciona com o substantivo 'livros' e não com o verbo 'ter' de 'tenho'.'''

    def classes_gramaticais(self):
        return  '''Em torno dos verbos e substantivos outras classes gramaticais aparecem relacionadas a eles.'''

    def classes_gramaticais_substantivo(self):
        return '''As classes gramaticais que acompanham o Substantivo:\nArtigo: define e particulariza o substantivo\nAdjetivo: Qualidade de um substantivo, características de um ser
Pronome: Substitui ou acompanha o nome
Numeral: Quantidade ou posição do nome em sequência\n
        SEMPRE IRÃO ESTAR ACOMPANHADAS DO SUBSTANTIVO
Locuções Adjetivas para substantivos: São grupos de duas ou mais palavras com o valor de uma só. A locução adjetiva está associada ao substantivo enquanto a locução adverbial está associada ao verbo.
'''

    def exemplo_locucao_adjetiva_adverbial(self):
        return '''Exemplo de locução adverbial:\n\nOs meus dois muito jovens amigos de Goiás chegaram bem cedo de bicicleta.\nSubstantivo:'amigos',\nNumeral:'dois',\nArtigo:'os',
Adjetivo:'jovens',\nAdvérbio:'muito'\nLocução Adjetiva:'de Goiás', a palavra 'de Goiás' estás associada a 'amigos' substantivo e núcleo da oração.
A parti de ...chegaram bem cedo de bicicleta:\nVerbo:'chegaram',\nAdvérbio:'cedo',\nAdvérbio:'bem',\nLocução Adverbial:'de bicicleta
O passeio com amigos é agradável.\n\nSubstantivo:'O passeio' ao lado do artigo 'o'.\n'com 'amigos':Locução Adjetiva(preposição + substantivo)'''

    def ex_loc_adv(self):

        return ''' Exemplo:\n\nOs meus amigos chegaram cedo de Goiânia.\nNesse sentido,a relação 'de Goiânia' é com o verbo 'chegaram', portanto é uma locução Adverbial.
Passear com amigos é mais agradável.\n\nVerbo:'passear',\n'com amigos':Locução Adverbial pois está acompanhando o verbo passear.
'''
    def classes_gramaticais_verbo(self):
        return ''' Advérbio: Pode ser o satélite do verbo, ou seja, sempre o acompanha. Além disso pode ser satélite de outro satélite'''

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

        return '''Exemplo:\n\nOs meus dois jovens amigos goianos chegaram cedo.\n
Substantivo: 'amigos' central da oração\nPalavras relacionadas ao nome em torno do substantivo:\n'jovens': Adjetivo\n'dois':quantidade EXATA de amigos : Numeral
'os':artigo - ** Nem sempre o artigo estará ao lado do substantivo **\n'goianos':Adjetivo para o nome amigos\nVerbo:'chegaram'Advérbio:'cedo'- que tem sua relação com chegaram -
                    '''
    def tripe(self):
        return '''\n\nA GRAMÁTICA É A FORMA COMO É ESCRITA, SEU SENTIDO E RELAÇÃO.'''

    def exemplo_2(self):

        print('Exemplo 2:\n\n Os meus dois muito jovens amigos goianos chegaram bem cedo.')
        return '''
Substantivo: Amigos Seus satélites são:\nArtigo: 'os',\nPronome: 'meus',\nNumeral:'dois',\nAdjetivo:'Jovens',\nAdjetivo:'goianos'
A palavra 'muito' está associada com jovens. Note que 'jovens'(adjetivo) já é satélite associado com o nome amigos (substantivo).
Portanto 'muito' é um advérbio. Para reforçar o adjetivo 'jovens'. O advérbio é de intensidade.
O verbo 'chegaram' tem como satélite após a palavra, a outras palavra 'cedo', seu único satélite, que só pode ser advérbio de tempo 'cedo'.
A palavra 'bem' está associada com 'cedo' de 'bem cedo'. A palavra 'bem' é um satélite de 'cedo', o 'bem' reforça o advérbio 'cedo'
com outro advérbio 'bem', advérbio de intensidade.'''

    def dica_1(self):

        return ''' O único advérbio que pode ser satélite do verbo, do adjetivo ou de outro advérbio é o advérbio de INTENSIDADE.
Os demais advérbios vão se relacionar com o verbo. Serão os advérbios de:\nTEMPO\nLUGAR\nMODO\nCausa\nMeio\nInstrumento\nFinalidade\nConcessão.'''

    def exemplo_verbo(self):

        return '''Exemplo : \nEle trabalha bem.\nAnálise Morfológica:\nEle:Pronome\nTrabalha:Verbo\nAdvérbio:bem (advérbio de modo associado ao verbo 'trabalha'
\nExemplo:\nEle acordou bem tarde.\nAnálise Morfológica:\nEle:Pronome\nVerbo:acordou\nAdvérbio:bem - Advérbio de intensidade que por sua vez está associado ao advérbio 'tarde' para reforçar\nAdvérbio:'tarde'-Advérbio de tempo associado ao verbo nuclear 'acordou'
NOTA: A palavra 'bem' poderia ser advérbio de modo relacionada ao verbo 'acordou' mas a palavra 'tarde' está no contexto.
Devido a isso a palavra 'bem' é de advérbio de intensidade por reforçar outro advérbio.'''
    
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
                    self.print_slow(self.texto_inicial())
                    self.print_slow(self.tripe())
                elif indice == 2:     
                    self.print_slow(self.verbo())
                    self.print_slow(self.exemplo_verbo())
                    self.print_slow(self.dica_1())
                    self.print_slow(self.tripe())
                elif indice == 3:
                    self.print_slow(self.substantivo())
                    self.print_slow(self.exemplo_1())
                    self.print_slow(self.exemplo_2())
                    self.print_slow(self.subs_exemplos())
                    self.print_slow(self.dica_1())
                    self.print_slow(self.tripe())
                elif indice == 4:
                    self.print_slow(self.classes_gramaticais())
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
                    self.print_slow(self.classes_gramaticais_substantivo())
                    self.print_slow(self.exemplo_locucao_adjetiva_adverbial())
                    self.print_slow(self.dica_1())
                elif opcao == 2:
                    self.print_slow(self.classes_gramaticais_verbo())
                    self.print_slow(self.exemplo_verbo())
                    self.print_slow(self.ex_loc_adv())
                    self.print_slow(self.exemplo_locucao_adjetiva_adverbial())
                    self.print_slow(self.dica_1())
                elif opcao == 3:
                    self.print_slow(self.outras_classes())
                    self.print_slow(self.dica_1())
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
                








                
