# **Linguagem de programação Python**
### _Fundamentials_



![logo python](https://github.com/userdanixdev/Programa-o-em-Python/assets/132594952/1f3da02b-f706-4563-b90f-37a124ceb77a)
***
## Origem da linguagem Python:

* A linguagem Python foi criada pelo matemático e programador Guido van Rossum em 1991. 

* O site oficial: www.python.org é possível instalar. 

* O IDLE é um ambiente de desenvolvimento integrado ao Python que vem junto ao programa para formar os códigos. De qualquer forma, pelo terminal é possível executar os programas.

* O Pycharm da JetBrains , https://www.jetbrains.com/pt-br/pycharm/ , é um ambiente mais completo, porém, mais pesado e seu desempenho dependerá da sua máquina.

* Para início é recomendado o IDLE.
***
### Características da Linguagem:

* A linguagem de programação Python possui códigos mais enxutos e menos verbal, ou seja, menos sintaxes complexas e mais estruturas de código simples;

* A linguagem Python é interpretada, multiplataforma e livre, o que a torna de fácil acesso;

* Uma linguagem de alto nível que possui um nível de abstração elevado;

* É totalmente orientada a objetos;
>  Qualidade: legibilidade, fácil de manter, suporte à reutilização de código;
> 
> Produtividade do desenvolvedor: tamanho reduzido do código em relação às 
>linguagens Java e C++, por exemplo;
> 
>  Linguagem interpretada, eliminando a etapa 
>de compilação e vinculação com outras ferramentas.

* Possui muitos módulos de extensão;
>
> Integração de componentes: pode ser usada como uma ferramenta e extensão de 
produto, podendo se chamar bibliotecas C e C++, assim como ser chamado por 
essas linguagens. Pode ser integrado com componentes Java e comunicar-se por 
meio de COM, COrba e .NET, além de interagir como SOAP e XML-RPC.

* Muitas instituições de ensino nacional e internacional usam a linguagem para aprendizado;

* É mas das linguagens mais populares e usadas atualmente.
***
### Tipos de objetos

Tipo de objeto | Formatos | Exemplo
| ---| --- | --- 
Números | int, long, float, complex | 1234, 999L, 3.1415, 3+4j
Strings | str e Unicode |‘spam’, “guido´s”
Booleanos | bool (true, false) | [1, [2, ‘three’], 4]
Dicionários | Dict |{‘food’ : ‘spam’, ‘taste’: ‘yum’}
Tuplas/Listas | list, tuple |{1, ‘spam’, 4, ‘U’}
Arquivos | File | Text=open (‘eggs’,’r’).read{}
None | None| Vazio  (null)


`Verificação do tipo de objeto : >>> x = 10, >>> type(x), <class 'int'>`

> A Constante `x` recebe tipo de classe inteira `10`.
> 
> A atribuição de um valor: `10` define a 
variável e seu tipo.
*** 

### Tipos primitivos

Tipo | Exemplos:
| ---| ---
Inteiros | 7 / -4 / 0 / 9875
Float | 4.5 / 0.075 /  -15.1545 / 7.0
Booleanos (bool)| True / False
Str (STRING) | Palavras entre aspas '' 
Complex | 999L, 3.1415, 3+4j
List | Conjunto de elementos por índice
dic | Conjunto de elementos por chave
>
>_Obs: Para o interpretador Python tudo que estiver entre aspas `''` são do tipo primitivo strings_
***
### Operadores Aritméticos

Descrição | Operador | Exemplo
| ---| --- | ---
Adição  | + | print(4+2) = 6 
Subtração | - | print(4-2) = 2
Multiplicação | * | print(4*2) = 8 _asterisco_
Divisão (_comum_)  | / | print(4/3) = 1.33333
Quociente Inteiro da div | // | print (4 // 3) = 1
Resto divisão inteira | % | print(4 % 2) = 0
Potenciação | ´**` | print(4**2) = 16


> `A potenciação ** `pode ser substituida pela função `pow(base, exp)`. _Exemplo: 4**2 ou pow(4, 2)_
> 


    Ordem de precedência matemática:
    1. ()- Parênteses
    2. ** - Potência (Exponênciação)
    3. * - Multiplicação
       / - Divisão
       //- Inteiro da divisão
       % - Resto da divisão
    4. + & - - Soma e subtração

***    

