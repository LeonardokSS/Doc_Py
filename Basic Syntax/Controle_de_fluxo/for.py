#Para criar loops basta: for variável de controle in variavel_analisar: comandos 

lista = [1,2,3,4,5,6,7,8,9,10]

for p in lista:
    print(p)

#Para criar com numero definido de ações basta usar: for variavel_controle in range(quantia de ações) : comandos

#Nesse exemplo eu defino a quandidade de ações é igual ao tamanho da lista 
for p in range (len(lista)):
    print(lista[p])

#Começa no 5 e termina com o tamanho da lista
for p in range (5,len(lista)):
    print(lista[p])

#Mesma coisa que o anterior
for p in range (10//2, len(lista)):
    print(lista[p])

lista_exemplo = ['Ana','Pedro','Cadu','Guilherme','Kenny','Matheus']

#Vai até a quinta posição, sendo que a Ana e a posição 0
for p in lista_exemplo:
    print(p)

#Esse mostra o indice + o elemento dentro da lista
for p in range(5):
 print(p,lista_exemplo[p])



