#Classe e um molde que cria objetos e define quais características e funções eles iram ter

#No self, estou basicamente criando um objeto
#No init, ele diz que a partir dele, ele vai começar a receber os valores para o objeto e depois os valores do objeto são iguais as valores das variáveis
class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor             
    def Buzinar(self):
        print("BIBIBI!!!")
    
#Aqui defino características para um carro que criei
carro_pai = Carro("Ford","Vermelho")
meu_carro = Carro("Chevrolet","Preto")

print(carro_pai.cor) #aqui eu faço a requisão do objeto que eu criei e tem o valor da cor
print(carro_pai.marca) #mesma coisa porém para marcas do carro


#No exemplo dos peixe temos agora um Method que retorna a resposta formatada pela função que pega o self 
class peixes():
    def __init__(self,nome):
        self.nome = nome
    def __str__(self):
        return "Um peixe chamado :" + self.nome

baiacu = peixes("Baiacu")
print(baiacu)
