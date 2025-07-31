Importante: O terminal padrão não permite manipular a barra de rolagem diretamente. 
O que podemos fazer é controlar a saída exibida, atualizando o conteúdo para dar a sensação de “subida” da tela.


A função go_back() apaga a linha com códigos ANSI (\033[F, \033[K), mas o terminal padrão do Windows não "sobe" a tela visível quando o cursor atinge o topo.

O que você vê no terminal é um buffer fixo de visualização, e esse buffer só rola quando linhas são adicionadas, não quando são apagadas.

A rich simula rolagem e atualizações dentro do seu próprio sistema de renderização, mas isso exige usar o Live, Console.clear() ou atualizar o conteúdo dinamicamente.

def go_back():
                nonlocal current_index, rewind_requested
                if current_index > 0:
                    current_index -= 1
                    rewind_requested = True # Sinaliza para interromper a linha atual
                    sys.stdout.write("\033[F") # Move o cursor para a linha anterior
                    sys.stdout.write("\033[K")  # Limpa a linha
                    sys.stdout.flush()


Se você realmente quiser usar rich para melhorar a visualização, a única forma funcional é substituir a exibição por uma tela redesenhada,
como com Live. Mas isso requer alterar o código de exibição, não apenas go_back().


Para melhorar o efeito da sua função go_back() usando a biblioteca rich e tentar simular uma “subida da barra de rolagem” de forma mais
visual e limpa, você vai precisar trocar o controle manual dos códigos ANSI pelo controle do conteúdo via rich.live.Live.


31/07/2025 -> Decidir por não alterar nada ainda, usando o 'rich', por falta de tempo e paciência.



