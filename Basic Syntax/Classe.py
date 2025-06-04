#Classe e um molde que cria objetos e define quais características e funções eles iram ter
class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor             #No self, estou basicamente dizendo que o input é igual as variáveis da class
    def Buzinar(self):
        print("BIBIBI!!!")
    
    #aqui defino características para um carro que criei
carro_pai = Carro("Ford","Vermelho")
meu_carro = Carro("Chevrolet","Preto")

print(carro_pai.cor) #aqui eu faço a requisão da cor do carro do pai
print(carro_pai.marca) #aqui da marcar do carro do pai


#No exemplo dos peixe temos agora um Method que retorna a resposta formatada pela função que pega o self 
class peixes():
    def __init__(self,nome):
        self.nome = nome
    def __str__(self):
        return "Um peixe chamado :" + self.nome

baiacu = peixes("Baiacu")
print(baiacu)