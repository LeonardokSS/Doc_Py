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
#Literalmente uma linha fisica composta por caracteres e encerrada por enter ou \.

soma = 1 + 2 + 3 \ 
       3 + 4 + 5
# 2 linhas fisicas que formam uma linha lógica.


# Junção de linha explícita
#Duas linhas fisicas podem ser unidas por uma contrabarra(\).


# Junção de linha implícita 
#linha físicas dentro de ( ), [ ],{ } podem ser quebradas em linhas lógicas sem a necessidae de utilizar \.


#Linhas em branco
#Linhas de lógica totalmente em braco são completamente anuladas, e todas as ações que estão nela são ignoradas.

#CAP 3--------------------------------------------------------------------------------


#Objetos são abstrações do Python para dados. Todos os tipos de dados no Python são objetos.


#Todo os objetos tem identidade, tipo e valor. A identidade de um objeto nunca muda depois de criado; você pode pensar nisso como endereço de objetos em memória. O 'is'  compara as identidades de dois objetos; a função id() retorna um inteiro representando sua identidade.

#Objetos que podem mudar seu valor são chamados mutáveis e os que tem valor definido na sua criação e não podem mudar são imutáveis.


#O tipo de um objeto determina as operações que o objeto implementa (por exemplo, “ele tem um comprimento?”) e também define os valores possíveis para objetos desse tipo. A função type() retorna o tipo de um objeto (que é também um objeto). Como sua identidade, o tipo do objeto também é imutável. [1]


#Contêiners são objetos que fazem referencia a outros objetos. São eles ('Tuplas,Listas e Dicionários'). As referências fazem parte do valor de um contêiner. As referencias fazem parte do contêiner.


#Os tipos afetam todos os aspectos e comportamentos do objeto.Para objetos imutáveis,
# se atribuirmos um mesmo valor a duas variáveis, o python vai dizer que eles apontam para o mesmo objeto, já para valores imutáveis, se c = [] e d = [] serão duas listas sempre diferentes, mesmo que elas possuam o mesmo valor. 

 
#hierarquia de tipos padrão

#None
#Utilizado para significar a ausência de um valor, esse tipo possui um valor único
#Exemplo: a = None, b = None


#NotImplemented
#Possui um valor único e existe um unico objeto dessa classe, ele é usado quando uma classe não implementa um método.


class MeuNumero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        if isinstance(outro, MeuNumero):
            return MeuNumero(self.valor + outro.valor)
        return NotImplemented  # Diz ao Python que ele não sabe lidar com isso

a = MeuNumero(10)
b = MeuNumero(5)
c = a + b
print(c.valor)  # Saída: 15

print(a + 3) # Isso vai causar um TypeError, porque MeuNumero + int não é implementado


#Sequências
#Função len(nome sequencia) mostra o numero de itens de uma sequencia
#Formados por sequêcias de numeros finitos e não negativos, O Índice começa do 0. Você pode quanto itens estão presentes com 'len()'e usar 'a[]' para acessar um item
a = [10, 20, 30, 40, 50]


# Acessando elementos
print(a[0])    # 10 (primeiro item)
print(a[-1])   # 50 (último item)


# Fatiamento simples
print(a[1:4])  # [20, 30, 40] (do índice 1 até 3)


# Fatiamento com passo
print(a[0:5:2])  # [10, 30, 50] (pula de 2 em 2)


# Mudando um valor (mutável)
a[2] = 99
print(a)  # [10, 20, 99, 40, 50]


#sequências imutaveis
#São elas string e tupla
s = 'python'
print(s[0]) # p
print(s[2]) # t


#Dicionários
#Conjunto de Objetos que são armazenados sem ordem, e podem ser acesados por chaves
#carro = {"marca": "Chevrolet", "modelo": "Tracker", "ano": 2020}
