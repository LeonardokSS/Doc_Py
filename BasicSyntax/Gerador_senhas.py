import string
import random


NUM = int(input("Digite o numero de caracteres entre 8 a 32: "))
 

letras = string.ascii_letters

letras_lista = []

for letra in letras:
    letras_lista.append(letra)


penis = []
Final = ""
def GerarSenha():
    
    for n in range(NUM):
        Senha = random.choices(letras_lista)
        #Transforma para string
        SenhaSTR = "".join(Senha)
        #Adiciona lista
        penis.append(SenhaSTR)
    final = "".join(penis)
    print("A sua nova senha é:{}".format(final))


GerarSenha()