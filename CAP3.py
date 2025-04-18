Comentários = #comentário

numeros = "float ou int"
nota = float(input("Nota:"))

string = "isso e uma string"

Texto = "/n" abre uma nova linha, "texto1/nTexto2" 
(''') EX:
-----------------
texto = '''Olá,
Isso é uma string
que ocupa múltiplas linhas.'''
print(texto)
SAIDA-----------
Olá,
Isso é uma string
que ocupa múltiplas linhas.
-----------------------------
+ = soma duas trings "sss"+"ooo" = "sssooo"

Strings perto uma da outra se fecham automaticamente 'ss'  'ss'= 'ssss

text = ('Quebra a linha para texto muito '
        'graaaaanddes.')

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6

 print com essas posições para poder selecionar a letra   -- a letra deve estar entre os numeros do exemplo
 ex: print[0:1]
 >>> P

notas = []

for x in range(5):
 CodigoAluno = input("Digite o rm:")
 nota = float (input("Digite a nota:") )
 resultado = [CodigoAluno, nota]
 notas.append(resultado) #append e para adicionar algo no final da lista 

print("Quantidade de notas", len(notas) )
 #vai passar em cada item da lista anterior para fazer com que a proxima lista execute com todos os alunos
for n in notas:
 Rm_aluno = n[0]
 nota_aluno = n[1]
 print("RM:",Rm_aluno,"Tirou:", nota_aluno)


