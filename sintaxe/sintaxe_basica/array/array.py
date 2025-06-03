import array

# #Esse módulo define um tipo de objeto que pode representar compactamente um array de valores básicos: caracteres, inteiros, números de ponto flutuante. Arrays são tipos de sequência e funcionam bem parecidamente com listas, porém o tipo dos objetos armazenados é restringido. O tipo é especificado na criação do objeto usando um type code, que é um único caractere. Os seguintes type codes são definidos:

# #'b' = valores de -128 a 127
# #'B' = valores de 0 a 255
# #'u' = string de caracteres unicode 
# #'h' = valores de -32.768 a 32.767
# #'H' = valores de 0 a 65.535
# #'i' = valores de -2.147.483.648 a 2.147.483.647
# #'I' = valores de 0 a 4.294.967.295
# #'l' = valores depende do sistema operacional
# #'L' = valores depende do sistema operacional
# #'q' = valores de -9,22 × 10¹⁸ a 9,22 × 10¹⁸
# #'Q' = valores	0 a 18,44 × 10¹⁸
# #'f' = valores de 4 bytes	IEEE 754, precisão simples
# #'d' = valores de 8 bytes	IEEE 754, precisão dupla

# #array.typecodes = mostra uma string que contém todos os typecodes disponíveis

# #print(array.typecodes) 

# #class array.array(typecode[, initializer]) = cria um novo array cujos itens são restritos pelo typecode, e inicializados a partir do valor opicional que deve ser um objeto byte ou bytearray, uma string unicode ou elementos iteráveis

# a =  array.array('u',[ 'a','b','c'])

# print(*a) 

# #array.typecode = mostra o typecode do array

# print(a.typecode)

# #array.itemsize = mostra o tamanho em bytes de cada item do array

# print(a.itemsize)

# #array.append(x) = coloca um novo valor no array ao fim dele

# a.append('d')
# print(*a)

# #array.buffer_info() = retorna uma tupla (endereço, tamanho) contendo o endereço na memória do array e o tamanho do arry

# print(a.buffer_info())

# #array.byteswap() = ele inverte a ordem dos bytes


# numero = array.array('h', [1,2,3,4,5,1])

# numero.byteswap()

# print(numero)

# #array.count(x) = retorna o número de ocorrências de um valor x

# numero = array.array('h', [1,2,3,4,5,1])

# print(numero.count(1))

# #array.extend() = coloca valores no último ponto da fila, se o tipo for diferente retorna um TypeError

# numero.extend([1,2,3,4,5])

# print(numero)

# #array.from_bytes() = coloca valores no último ponto da fila, porém como valores binários, espera os itens como bytes

# buffer = bytes([1,2,3,4,5,6])

# numero.frombytes(buffer)

# print(numero)

# #array.fromfile(f,n) = lê n itens de um objeto arquivo e adiciona no final de um array

# file = open('arquivo', 'rb')

# arquivo = array.array('h')

# arquivo.fromfile(file, 10 )

# print(arquivo)

# #array.fromlist(list) = pega itens de uma lista e adiciona em outra

# lista_1 = array.array('h', [1,2,3,4,5])
# list_2 = array.array('h', [6,7,8,9,10])

# #array.tolist() = transforma um array em uma lista 

# lista_1.fromlist(list_2.tolist())



# print(lista_1)

# #array.fromunicode(s) = ele extende o array com a string s unicode dada, o array tem que ser do tipo 'u' ou 'w'

# exemplo = array.array('u',['a','b','c','d','e'])

# exemplo.fromunicode('f')

# print(*exemplo)

# #array.index(x[, start[, stop]]) = retorna o índice da primeira ocorrência de x, os argumentos start e stop podem ser usados para especificar posição iniciais e finais

# print(numero.index(1))

# #array.insert(i, x) = insere um valor x em um índice i, se extrapolar 

# numero = array.array('h', [1,2,3,4,5,1])
# numero.insert(len(numero),7)
# numero.insert(len(numero),9)


# print(numero)

# #array.pop([i]) = remove um índice i de um array

# numero.pop(7)

# print(numero)


# #array.remove(x) = remove a primeira ocorrência de x

# numero.remove(1)

# print(numero)

# #array.clear() = remove todos os elementos do aray

# # numero = array.array('h', [1,2,3,4,5,1])

# # print(type(numero))

# # numero.clear()

# # print(numero)

# #array.reverse() = inverte a ordem dos itens

# numero.reverse()

# print(numero)

# #array.tobytes() = converte um array com valores em bytes

# print(numero.tobytes())

# #array.tofile(f) = escreve todos itens em um arquivo

# numero = array.array('h', [1,2,3,4,5,1])

# file = open('arquivo', 'wb')

# numero.tofile(file)

# #array.tounicode() = converte o array em uma string unicode

# palavras = array.array('u', ['a','m','o','r'])

# print(palavras.tounicode())