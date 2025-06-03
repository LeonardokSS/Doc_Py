#Métodos de arquivos 

#open(filename, mode, enconding=None) = serve para abrir um arquivo

# f = open('arquivo_exemplo', 'r', encoding='utf-8') 

# #read() = serve para ler o conteúdo de um arquivo
# leitura = f.read()

# print(leitura)

# #também é possível usar a cláusa with para ler arquivos:

# with open('arquivo_exemplo', encoding='utf-8') as f:
#     read_data = f.read()
#     print(read_data)

# #f.closed = verifica se o arquivo foi fechado automaticamente

# print(f.closed)

# #f.close() = fecha um arquivo manualmente

# a = open('arquivo_exemplo', 'r', encoding='utf-8') 
# print(a.read())
# print(a.closed)
# a.close()
# print(a.closed)

# #readline() = le apenas a primeira linha

# a = open('arquivo_exemplo', 'r', encoding='utf-8') 
# print(a.readline())
# a.close()

#para ler todas as linhas de um arquivo, pode usar list(f) ou f.readlines()

# f = open('arquivo_exemplo', 'r', encoding='utf-8') 
# print(list(f))
# f.close()

# f = open('arquivo_exemplo', 'r', encoding='utf-8') 
# print(f.readlines())
# f.close()

#f.write() = escreve no arquivo retornando o número de caracteres escritos

f = open('arquivo_exemplo', 'r+', encoding='utf-8') 
f.write('Meu nome é cláudio\n')


#f.tell() = diz a posição atual do cursos

print(f.tell())


#f.seek() = muda a posição atual do cursos

f.seek(0)
print(f.readline())
f.close()