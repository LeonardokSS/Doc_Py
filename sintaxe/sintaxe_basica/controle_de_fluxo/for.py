#Para criar um loop for em python, basta: for variável_de_controle in variável_analisar: comandos, esse loop pode não tem um número definido de ações

lista1 = [1,2,3,4,5,6,7,8,9,10]

for p in lista1:
    print(p)

#Para criar um loop com números definidos de ações basta: for variável_de_controle in range(quantia_de_ações): comandos

for p in range(len(lista1)): #definindo que a quantidade de ações é igual ao tamanho da lista
    print(lista1[p])

for p in range(5, len(lista1)): #definindo que a quantidade de ações começa em 5 e vai até o tamanho da lista
    print(lista1[p])

for p in range(10//2, len(lista1)): #a mesma coisa que o exemplo 2, porém com a adição de conta para definição de quantia inicial de ações
    print(lista1[p])


#Exemplo 

lista_nomes = ['Ana', 'Beatriz', 'Carlos', 'Davi', 'Eduardo', 'Felipe', 'Gustavo', 'Igor', 'Júlia']

for p in lista_nomes:
    print(p)

for p in range(9):
    print(p, lista_nomes[p])

for p in range(50):
    print('O nome: ' + lista_nomes[p] + ' está no índice: ', p)
    if(p + 1 == len(lista_nomes)):
        print('O algorítmo acabou')
        break
    else:
        continue

#Instruções break, continue

#break -> serve para parar o loop quando determinado evento acontecer, o exemplo acima, o loop acabou quando o p+1 foi igual a quantidade de indices na lista_nomes

#continue -> serve para continuar o algorítimo normalmente para a próxima repetição


#A cláusula else também pode ser usada em loops for:

for i in range(10):
    
    if(i == len(lista_nomes)):
        print('O algorítimo acabou')
        break
    else: 
        print('O número é: ', i)
        continue


