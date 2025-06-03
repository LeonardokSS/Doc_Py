#Para se criar uma lista em python a sintaxe é a seguinte = nome_lista = [] aonde [] são os valores que ficarão acoplado dentro da variável

#Exemplo

#a = ['a', 'b', 'c']

#print(a)

#Diferente das strings, lista são mutáveis, ou seja podem ter seus valores alterados

#a[0] = 'd'
#a[1] = 'e'
#a[2] = 'f'

#print(a)

#Também é possível adicionar valores a lista com o método append, só é possível fazer isso com um valor de cada vez

#a.append('g') 
#a.append('g', 'f') #Gerará um erro

#print(a)

#Para comparar o conteúdo de 2 listas, basta usar o método id

#lista1 = ['1','2','3','4','5','6','7','8','9','10']
#lista2 = lista1

#print(id(lista1) == id(lista2))

#A função len também se aplica a listas

#print(len(lista1))

#Fatiamento também é possível

#print(lista1[0:2])
#print(lista1[:10])
#print(lista1[0:(20//2)])
#print(lista1[-1])

#Para remover index de lista basta:

#lista1[5:10] =[]
#print(lista1)

#É possível colocar listas dentro de listas:

#a = ['a','b','c']
#d = ['d','e','f']
#g = [a,d,'g']

#print(g)

#Para pegar atributos de uma lista dentro de uma lista basta:

#print(g[1][0])
#print(g[0][2])