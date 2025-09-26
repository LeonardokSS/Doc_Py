import string
import random


NUM = int(input("Digite o numero de caracteres entre 8 a 32: "))


 
#Letras recebe todos as letras do alfabeto
letras = string.ascii_letters

pontuacao = string.punctuation 

digitos = string.digits

letras_lista = []

numeros_lista = []

pontuacao_lista = []

for pontu in pontuacao:
    pontuacao_lista.append(pontu)

for numero in digitos:
    numeros_lista.append(numero)

for letra in letras:
    letras_lista.append(letra)


Lista_string = []
Final = ""

    

def GerarSenha():
        Tipo_senha = input("***********************************      Gerador de Senhas         *********************************** \nEscolha o nível da senha:\n1 Apenas letras / 2 Letras e números / 3 Letras, números e símbolos \n Digite o número correspondente ao nível desejado:") 
        match(Tipo_senha):
            case (1):
                for n in range(NUM):
                    Senha = random.choices(letras_lista)
                    #Transforma para string
                    SenhaSTR = "".join(Senha)
                    #Adiciona lista
                    Lista_string.append(SenhaSTR)
            case (2):
                print("sim ta funcionando")
        final = "".join(Lista_string)
        print("A sua nova senha é:  {}".format(final))
       




GerarSenha()
