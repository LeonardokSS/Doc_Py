#Apenas vimos os erros por cima, agora vamos dar uma olhada mais de perto:

#Existem 2 tipos de erros erros de sintaxe e erros de exceções.

#Erro de sintaxe: quando alguma coisa foi escrita errado

# while True print('Olá mundo') #Vai gerar um erro porque o loop while espera os dois-pointos antes da ação acontecer.

# while True: print ('Olá mundo') #Versão correta

#Erros de exceções: quando acontece na hora da execução

# lista = [1,2,3,4,5]
# lista.append(6,7) #Gerará um erro de exceção porque o método apende só necessita de 1 argumento

# lista.append(6) #Versão correta

#Tratamento de exceções = Permitida com métodos try-except para tratamento de erros específicos, erros podem ser: 
#SyntaxError = Quando um erro de sintaxe ocorre
#IndexError = Ocorre quando é chamado um index inválido
#KeyError = Ocorre quando a chave não existe em um dicionáro
#TypeError = Quando ocorre uma operação com um tipo diferente do esperado
#ValueError = Ocorre quando o tipo é correto, mas o valor é errado
#NameError = Ocorre quando uma variável/método não foi definido
#AttributeError = Ocorre quando você tenta acessar um atributo que não existe
#FileNotFoundError = Ocorre quando não é encontrado o arquivo mencionado
#ZeroDivisionError = Ocorre quando um número é divido por 0
#OverflowError = Ocorre quando um cálculo resulta em um número muito grande para ser representado
#ImportError = Ocorre quando o módulo não existe
#RuntimeError = Erro genérico em tempo de execução
#StopIteration = Ocorre quando um iterador não tem mais itens a devolver
#IdentationError = Ocorre quando há um erro de identação
#UnicodeDecodeError = Ocorre quando há um erro na decodificação de caracteres Unicode.
#OSError = Ocorre quando há algum erro no sistema operacional
#AssertionError = Ocorre quando uma afirmação assert falha
#NotImplementationError = Ocorre quando um método ou função não foi implementada
#MemoryError = Ocorre quando não se consegue alocar memória suficiente
#ConnectionError = Ocorre quando há um erro em relação a conexão de redes
#TimeoutError = Ocorre quando a operação atingiu tempo limite
#BlockingIOError =  Ocorre quando uma operação de I/O bloqueia a execução.
#BrokenPipeError = Ocorre quando um processo tenta escrever em um pipe, mas o outro processo já fechou.
#KeyboardInterrupt = Quando a resposta foi cancelada

#Como tratar erros, usando try-except: try: comandos, except nome_do_erro: comandos

# while True:
#     try:
#         x = int(input('Digite um número'))
#         break
#     except ValueError:
#         print('Você digitou um caractere não número')

#a cláusula try funciona da seguinte forma: o que está dentro de try é executado, se nenhuma exceção ocorrer a clásula except é ignorada, se ocorrer uma exceção no meio da execução do try o resto dos comandos são ignorados, se o tipo da exceção for o que está em except, a cláusula except é executada, se a exceção não tiver na cláusula except, uma mensagem de erro será enviada no terminal, e o programa termina

#Uma cláusula try pode ter vários except:

# while True:
#     try:
#         x = int(input('Digite um número\n'))
#         break
#     except (ValueError, TypeError, RuntimeError, KeyboardInterrupt):
#         print('Você digitou um caractere não número ou não digitou nada')
#         break

#Criando exceções: para se criar uma exceção basta: class nome_da_exceção(Exception): comandos

#Exemplo:

# class exceção(Exception):
#     pass

#Argumentos da exceção. A presença e os tipos dos argumentos dependem do tipo da exceção. A cláusula except pode especificar uma variável após o nome da exceção. A variável está vinculada à instância de exceção que normalmente possui um atributo args que armazena os argumentos. Por conveniência, os tipos de exceção embutidos definem __str__() para exibir todos os argumentos sem acessar explicitamente .args.

# try:
#     raise Exception('spam', 'ovos')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)

#     x, y = inst.args

#     print(x)
#     print(y)

#A cláusula else também pode ser usada em try-except

# while True:
#     try: 
#         x = int(input('Digite um número\n'))
        
#     except (ValueError, TypeError, RuntimeError, KeyboardInterrupt):
#           print('Você digitou um caractere não número ou não digitou nada')
          
#     else: 
#          print('Aqui está o seu número :', x)
#          break

