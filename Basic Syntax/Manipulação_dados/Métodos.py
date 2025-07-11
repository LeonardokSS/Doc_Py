texto = "olá Esse TEXTO é aPeNaS um Teste"

# Tamanho da String
len(texto)  #Retorna o número de caracteres.

# Alterar caixa de Texto

texto.lower()         # Converte todos os caracteres para minúsculo  

texto.upper()         # Converte todos os caracteres para maiúsculo  

texto.capitalize()    # Converte a primeira letra para maiúsculo e o resto para minúsculo  

texto.title()         # Converte a primeira letra de cada palavra para maiúsculo  

texto.swapcase()      # Inverte maiúsculas e minúsculas na string  

# Substituição e Modificação

texto.replace('antigo', 'novo')  # Substitui todas as ocorrências de 'antigo' por 'novo'  

texto.strip()                    # Remove espaços em branco no início e no fim  

texto.lstrip()                   # Remove espaços à esquerda (início)  

texto.rstrip()                   # Remove espaços à direita (fim)  

# Divisão e Junção

texto.replace('antigo', 'novo')  # Substitui todas as ocorrências de 'antigo' por 'novo'  

texto.strip()                    # Remove espaços em branco no início e no fim  

texto.lstrip()                   # Remove espaços à esquerda (início)  

texto.rstrip()                   # Remove espaços à direita (fim)  

# Verificação

texto.startswith('abc') # Verifica se a string começa com 'abc' (retorna True ou False) 

texto.endswith('xyz')   # Verifica se a string termina com 'xyz' (retorna True ou False)  

texto.isalpha()         # Verifica se a string contém apenas letras (sem números ou espaços)
 
texto.isdigit()         # Verifica se a string contém apenas números  

texto.isalnum()         # Verifica se a string contém apenas letras e números (sem espaços ou símbolos)  

respostas = texto.lower()   

print (texto.isalnum())

