#A instrução try possui outra cláusula opcional, cuja finalidade é permitir a implementação de ações de limpeza, que sempre devem ser executadas independentemente da ocorrência de exceções. Se uma cláusula finally estiver presente, a cláusula finally será executada como a última tarefa antes da conclusão da instrução try. A cláusula finally executa se a instrução try produz uma exceção. A cláusula finally tem maior prioridade do que a cláusula try
 
# try: 
#     raise KeyboardInterrupt
# finally: 
#     print('Acabou')


#Exemplo de prioridade da cláusula finally

# def retorna_booleano():

#     try: 
#         return True
#     finally:
#         return False
    
# print(retorna_booleano())