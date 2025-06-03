#Para se criar uma função basta: def nome_da_função(paramêtros): comandos, para retornar um valor a cláusula return deve ser adicionada

# a = int(input('Digite um número: '))
# b = int(input('Digite o segundo número: '))

# def soma(a,b):
#     return a + b

# print(soma(a,b))

# def diminuir_valor_em_5(x):
#     for i in range(5):
#         x -= 1
        
#         if(i == 4):
#             return x

# x = int(input('Digite um número maior que 5: '))

# print(diminuir_valor_em_5(x))

#def potencia(y):
   # y **= 2
   #return y

#y = int(input('Digite um número a ser potenciado: '))

#print(potencia(y))


#Diminuição de matemática simples: +=, -=, *=, /=, //= **=

#+= -> x = x + variável
#-= -> x = x - variável
#*= -> x = x * variável
#/= -> y = y / variável
#// -> y = y// variável
#**/ = y = y ** variável

#Função com argumento padrão, as funções com argumento padrão são criadas porque simplesmente são mais fáceis de escrever quando se tem um argumento padrão ja citado

# def somar_quantas_vezes(x, quantidade, vezes = 4):

    
#     while True:
        
#         x += quantidade

#         vezes -= 1

#         if (vezes == 0):
#             return x
        
  
# print(somar_quantas_vezes(9, 14))


#Função com argumentos nomeados, são funções que usam argumentos nomeados (str)

# def ação(verbo = 'respirar', tempo_verbal = 'presente'):
    

#     return print('Você está praticando uma ação, usando o verbo: ', verbo, ' No modo verbal: ' , tempo_verbal)
    

# ação('comer', 'futuro')


#Argumentos especiais, os argumentos especiais são '/' e '*', eles definem se um argumento será posicional, ou seja, escrito pelo usuário ou nomeado, definido por padrão

#Exemplo de argumento posicional '/'

# def diminuir_valor_em_5(x , /):

#     x = int(input('Digite um número a ser diminuido : '))
    
#     for i in range(5):
#        x -= 1
        
#     if(i == 4):
#         return x


# print(diminuir_valor_em_5(1))

# impossível de fazer print(diminuir_valor_em_5(x=1))

#Exemplo de argumentos nomeados:

# def ação(*,verbo = 'respirar', tempo_verbal = 'presente',):
    

#     return print('Você está praticando uma ação, usando o verbo: ', verbo, ' No modo verbal: ' , tempo_verbal)

# ação(verbo = 'comer', tempo_verbal= 'presente') #possível de fazer
# ação('andar', 'futuro') # impossível de fazer

#Lista de argumentos arbitrárias = atribuir os argumentos a uma tupla específica, argumentos que ocorrem depois dos argumentos arbitrários são sempre nomeados

# def somar_vários_itens(*args , vezes):
#     soma = 0  
    
#     for num in args: 
#         soma += num * vezes  
    
#     return soma  

# # Exemplo de uso:
# print(somar_vários_itens(1, 2, 3, 4, 5, vezes=10))

