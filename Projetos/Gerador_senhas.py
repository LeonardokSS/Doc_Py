import string
import random
from colorama import Fore,Style


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
        Tipo_senha = int(input("""
***********************************
        Gerador de Senhas
***********************************

Escolha o nível da senha:
1 - Apenas letras
2 - Letras e números
3 - Letras, números e símbolos

Digite o número correspondente ao nível desejado: 
"""))
        
        if Tipo_senha == 1:
                for i in range(NUM):
                    Senha = random.choices(letras_lista)
                    #Transforma para string
                    SenhaSTR = "".join(Senha)
                    #Adiciona lista
                    Lista_string.append(SenhaSTR)
                    
                    final = "".join(Lista_string)
                    
                print(f"A sua nova senha é: {Fore.YELLOW}{final}{Style.RESET_ALL}")
        elif Tipo_senha == 2:
                
                for n in range(NUM):
                    ListaEscolhida = random.choice([letras_lista,numeros_lista])
                    Escolhido = random.choice(ListaEscolhida)
                    #Adiciona lista
                    Lista_string.append(Escolhido)
                    
                    final = "".join(Lista_string)
                print(f"A sua nova senha é: {Fore.YELLOW}{final}{Style.RESET_ALL}")

        elif Tipo_senha == 3:
                for n in range(NUM):
                    ListaEscolhida = random.choice([letras_lista,numeros_lista,pontuacao_lista])
                    Escolhido = random.choice(ListaEscolhida)
                  
                    
                    #Adiciona lista
                    Lista_string.append(Escolhido)
                    final = "".join(Lista_string)
                print(f"A sua nova senha é: {Fore.YELLOW}{final}{Style.RESET_ALL}")

        else:
                print(f"{Fore.RED}{"Digite uma opção valida!"}{Style.RESET_ALL}")
                
            
GerarSenha()
