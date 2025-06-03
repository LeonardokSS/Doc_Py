#A instrução raise permite forçar a ocorrência de um determinado tipo de exceção, para se usar basta: raise tipo_de_exceção

#Exemplo:

# raise NameError('Olá') #Gerará um NameError forçadamente

#Caso você precise determinar se uma exceção foi levantada ou não, mas não quer manipular o erro, uma forma simples de instrução raise permite que você levante-a novamente:

# try:
#     raise NameError('Olá')
# except NameError:
#     print('Uma exceção passou por aqui!')
#     raise

#Encadeamento de exceções: Se uma exceção não tratada ocorrer dentro de uma seção except, ela terá a exceção sendo tratada anexada a ela e incluída na mensagem de erro:

# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

#Para indicar que uma exceção é uma consequência direta de outra, a cláusula raise permite a cláusula from

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc