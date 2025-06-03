#Para se fazer strings em python basta colocar entre aspas('') ou aspas duplas("")

#nome = 'Gustavo'
#idade = '16 anos'
#dia_de_hoje = '28/02/25'

#input(nome + ' escreveu isso com: ' + idade + ' no dia: ' + dia_de_hoje)


#Para printar caracteres especiais como '' ou /, \ e até acentos, basta colocar um \ antes do caractere especial

#Exemplos:

#print("Flor d\água")
#print("O nome \'Pedro\' é muito bonito")

#Se você não quiser que os caracteres sejam precedidos com \, apenas adicione o r antes da "" ou '' para começar o modo cru

#print(r"O nome 'Pedro' é muito bonito")

#Para gerar uma lova linha em python apenas coloque o caractere \n no lugar onde deve pular linha

#print('Eu gosto de brincar de: \n') # o método print ja pula uma linha por definição
#print('Bola')

#Se você quiser que strings abrangem várias linhas, pode usar as aspas triplas para indicar isso

#print("""O meu nome é: 
         #Pedro, e eu gosto de
         #Bolinhas de gude """)

#Strings também podem ser concatenadas

#Exemplo:

#pala = 'pala'
#vra = 'vra'
#palavra = pala + vra 
#print(palavra)

#palavra2 = pala * 2 + vra
#print(palavra2)

#As strings também podem ser indexadas, com o primeiro caractere igual a 0. Não existe um tipo específico para caracteres; um caractere é simplesmente uma string cujo tamanho é 1


#palavra = 'supermercado'
#print(palavra[0]) #Busca o index 0 da palavra supermercado

#print(palavra[0:5]) #Busca o index 0 a 5 da palavra supermercado

#print(palavra[0:12]) #Busca o index 0 a 13 da palavra supermercado

#print(palavra[-1]) #Busca o index -1 (um index negativo significa inverso), então logo pegará o index 13

#print(palavra[:5]) #Busca todos os index até o index 5

#print(palavra[0:(10//2)]) #Em si faz a mesma coisa que o de cima porém com uma conta no meio

#print(palavra[:]) #São equivalentes
#print(palavra) #São equivalentes

#Se você tentar colocar index a mais doque a palavra tem, vai dar erro

#print(palavra[42])
#print(palavra[42:])

#Porém a estrapolação de index no final, resulta na palavra inteira

#print(palavra[:42])

#As strings não podem mudar os seus valores, são imutáveis

#print(palavra[0] = 'j')

#A função len retorna o tamanho de uma string

#print(len(palavra))

