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