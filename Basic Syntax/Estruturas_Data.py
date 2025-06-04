#Lista armazena todos os tipos de informação e pode posteriormete ser alterada
Lista = ["Jonh", 30, 30.00, False]

#Podemos vizualizar itens específicos da lista, começando do 0 que e o primeiro item
print (Lista[0])

#Podemos inserir elementos dentro da lista colocando nome da lista depois a posição dele e depois o elemento que queremos adicionar

Lista.insert(1,"teste")

print (Lista[1])

#Podemos usar também o .appen(x)

Lista.append(3)

#Para remover coisas da lista podemos usar o .remove

Lista.remove ("teste")

print (Lista)
#_____________________________________________________________________________________________________

#Tuplas são como listas normais porém não podem ser alteradas, ou seja não podemos usar o append(x) para inserir elementos dentro dela
#A syntaxe da tupla e com () e a das listas com []

x = tuple

x = ("Teste", 11, 33)

print (x)

#Podemos converter as tuplas em listas e listas em tuplas

B = (22,11,33)

list(B)

#E listas em tuplas 

C = [29,73,89]

tuple(C)

#_____________________________________________________________________________________________________

#Set é uma lista que não pode ter repetição de elementos e não pode ter elementos duplicados

Exemplo = set()

Exemplo = {1,1,2,2,3,3,1,3,2}

print(Exemplo)

#Set é útil para converter listas com repetição de elementos em listas mais organizadas
Lista2 = list()

Lista2 = [11,11,11,"sigasn"]

print (Lista2)

ListaOrganizada = set(Lista2)

print (ListaOrganizada)

#Dicionários servem para adicionar elementos que possuem "chaves"

Dicionário = dict()

Dicionário = {"Nome": "Pedro","Idade": 33}

print (Dicionário["Idade"])

#Podemos tambem mudar os valores pelo seu id

Dicionário["Idade"] = 900

print(Dicionário["Idade"])