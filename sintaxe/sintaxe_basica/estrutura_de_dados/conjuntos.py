# Python também inclui um tipo de dados para conjuntos, chamado set. Um conjunto é uma coleção desordenada de elementos, sem elementos repetidos. Usos comuns para conjuntos incluem a verificação eficiente da existência de objetos e a eliminação de itens duplicados. Conjuntos também suportam operações matemáticas como união, interseção, diferença e diferença simétrica.


a = set('abacaxi')
b = set('melância')

print(b)
print(a - b) 


#frozenset() = cria um conjunto não mutável

conjunto1 = frozenset([1,2,3,4,5,6])

#conjunto1[0] = 1 #gerará erro

print(conjunto1) 

#Operações com conjuntos

conjunto2 = frozenset([3,4,1,7,1,6,8])


#União de conjuntos: conjunto1 | conjunto2

união = conjunto1 | conjunto2
print(união)

#Interseção de conjuntos: conjunto1 & conjunto2

interserção = conjunto1 & conjunto2
print(interserção)

#Diferença de conjuntos: conjunto1 - conjunto2

diferença = conjunto1 - conjunto2
print(diferença)
