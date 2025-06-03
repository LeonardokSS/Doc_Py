#Essa pasta visa aumentar ainda mais o conhecimento sobre estrutura de dados que já vimos antes

#Lista tem vários metódos que serão apresentados

#lista.append(x) = adiciona um indice ao final da lista

lista = [1,2,3,4,5,6,7,8,9,10]
lista.append(11)
print('Metódo append: ',lista)

#list.extend(iterable) = adiciona no fim de todos os elementos um argumento iterável

lista_extended = [11,12,13,14,15]
lista.extend( lista_extended)

print('Método extend: ',lista)

#list.insert(i,x) = adiciona em uma posição dada um elemento

lista.insert(0, 0)
print('Método insert: ', lista)

#list.remove(x) = remove o primeiro valor na lista cujo valor seja igual a x
lista.remove(0)
print('Método remove: ', lista)

#list.pop([i]) = remove um index específico e se não tiver um index, removo o último item da lista
lista.pop(14)
print('Método pop: ', lista)

#list.clear() = remove todos itens de uma lista

lista_exemplo = [1,2,3,4,5,6,7,8,9,10]
print('Lista antes do metódo clear :', lista_exemplo)

lista_exemplo.clear()
print('Lista depois do método clear: ', lista_exemplo)

#list.index(x[, start [, end]]) = retorna um índice de um elemento cujo valor é igual a x, os argumentos start e end servem como fatiamento e podem ser usados para indicar mais de um iten

print('Índice de 3 da lista: ', lista.index(3))

#list.count(x) = devolve o número de vezes que x aparece na lista

lista_exemplo = [1,2,3,4,5,6,7,8,9,10]
lista_exemplo.append(1)

print('Número de vezes que o número 1 aparece na lista: ', lista_exemplo.count(1))

#list.sort(*, key=None, reverse=false) = ordena os itens da lista, os argumentos podem ser usados para facilitar a utilização

lista_exemplo.sort()
print('Lista de números organizada: ', lista_exemplo)

#list.reverse = inverte a ordem dos itens da lista

lista.reverse()
print('Lista em ordem reversa: ', lista)

#list.copy = devolve uma cópia rasa da lista

lista_copia = lista.copy()

print('Copiei uma lista: ', lista_copia)

#del = remove um valor da lista, porém usa o índice do valor

del lista[0]

print('Lista com valor removido por del: ', lista)


