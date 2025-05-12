https://docs.python.org/pt-br/3.13/reference/datamodel.html
#A sintaxe Python define um conjunto de regras que são utilizadas para criar um programa Python. A sintaxe da linguagem de programação Python tem muitas semelhanças com as linguagens de programação Perl, C e Java. No entanto, existem algumas diferenças definitivas entre as linguagens.

# Variaveis são como uma caixa que armazena informações de todos os tipos e pode manipular os mesmos
fruta = 'Banana'
n = 25
pi = 3.141592653589931

#Tipos de dados 
#Inteiros para numeros como: 1,20,399
#Pontos 


#Linhas lógicas
#A instrução completa que pode ocupar várias linhas físicas, mas que o Python entende como uma só.

#Linhas físicas
#Literalmente uma linha fisica composta por caracteres e encerrada por enter ou \

soma = 1 + 2 + 3 \ 
       3 + 4 + 5
# 2 linhas fisicas que formam uma linha lógica

# Junção de linha explícita
#Duas ou mais linhas físicas podem ser juntadas em linhas lógicas usando o caractere contrabarra (\) da seguinte forma: quando uma linha física termina com uma contrabarra que não é parte da uma literal string ou comentário, ela é juntada com a linha seguinte formando uma única linha lógica, removendo a contrabarra e o caractere de fim de linha seguinte.

# Junção de linha implícita 
#Expressões edntre ( ), [ ],{ } podem ser quebradas em linhas físicas sem a necessidae de utilizar \

#Linhas em branco
#Uma linha lógica que contém apenas espaços, tabulações, quebras de página e possivelmente um comentário é ignorada (ou seja, nenhum token NEWLINE é gerado). Durante a entrada interativa de instruções, o tratamento de uma linha em branco pode diferir dependendo da implementação do interpretador. No interpretador interativo padrão, uma linha lógica totalmente em branco (ou seja, uma que não contenha nem mesmo espaço em branco ou um comentário) encerra uma instrução de várias linhas.

#CAP 3
#Objetos são abstrações do Python para dados. Todos os dados em um programa Python são representados por objetos ou por relações entre objetos. (De certo modo, e em conformidade com o modelo de Von Neumann de um “computador com programa armazenado”, código também é representado por objetos.)

#Todo objeto tem uma identidade, um tipo e um valor. A identidade de um objeto nunca muda depois de criado; você pode pensar nisso como endereço de objetos em memória. O operador is compara as identidades de dois objetos; a função id() retorna um inteiro representando sua identidade.

#O tipo de um objeto determina as operações que o objeto implementa (por exemplo, “ele tem um comprimento?”) e também define os valores possíveis para objetos desse tipo. A função type() retorna o tipo de um objeto (que é também um objeto). Como sua identidade, o tipo do objeto também é imutável. [1]

#Alguns objetos contêm referências a recursos “externos”, como arquivos abertos ou janelas. Entende-se que esses recursos são liberados quando o objeto é coletado como lixo, mas como a coleta de lixo não é garantida, tais objetos também fornecem uma maneira explícita de liberar o recurso externo, geralmente um método close(). Os programas são fortemente recomendados para fechar explicitamente esses objetos. A instrução try…finally e a instrução with fornecem maneiras convenientes de fazer isso.

#Alguns objetos contêm referências a outros objetos; eles são chamados de contêineres. Exemplos de contêineres são tuplas, listas e dicionários. As referências fazem parte do valor de um contêiner. Na maioria dos casos, quando falamos sobre o valor de um contêiner, nos referimos aos valores, não às identidades dos objetos contidos; entretanto, quando falamos sobre a mutabilidade de um contêiner, apenas as identidades dos objetos contidos imediatamente estão implícitas. Portanto, se um contêiner imutável (como uma tupla) contém uma referência a um objeto mutável, seu valor muda se esse objeto mutável for alterado.

#Os tipos afetam quase todos os aspectos do comportamento do objeto. Até mesmo a importância da identidade do objeto é afetada em algum sentido: para tipos imutáveis, as operações que calculam novos valores podem realmente retornar uma referência a qualquer objeto existente com o mesmo tipo e valor, enquanto para objetos mutáveis isso não é permitido. Por exemplo, após a = 1; b = 1, a e b podem ou não se referir ao mesmo objeto com o valor um, dependendo da implementação. Isto ocorre porque int é um tipo imutável, então a referência a 1 pode ser reutilizada. Este comportamento depende da implementação usada, então não deve ser considerada confiável, mas é algo para se estar ciente ao fazer uso de testes de identidade de objeto. No entanto, após c = []; d = [], c e d têm a garantia de referir-se a duas listas vazias diferentes e únicas. (Observe que e = f = [] atribui o mesmo objeto para e e f.)
 
#hierarquia de tipos padrão
#Abaixo está uma lista dos tipos que são embutidos no Python. Módulos de extensão (escritos em C, Java ou outras linguagens, dependendo da implementação) podem definir tipos adicionais. Versões futuras do Python podem adicionar tipos à hierarquia de tipo (por exemplo, números racionais, matrizes de inteiros armazenadas de forma eficiente, etc.), embora tais adições sejam frequentemente fornecidas por meio da biblioteca padrão.

#Algumas das descrições de tipo abaixo contêm um parágrafo listando “atributos especiais”. Esses são atributos que fornecem acesso à implementação e não se destinam ao uso geral. Sua definição pode mudar no futuro.
