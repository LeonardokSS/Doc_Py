#Podemos criar heranças multiplas quando usamos uma class. Por exemplo, podemos atribuir valores para os objetos criados a partir da classe.



class Carro_antigo():
   
   
   def __init__(self):
    self.nome = "Fusca"
    self.cor = "Preto"
    self.placa = "GSE2S-22"
    self.potencia = "100"

#O self serve como uma variavel que tem mesmo valor de outra variavel, a diferença é que o self é uma variavel interna da classe.
   def get_carro(self):
     return self.nome
   
   def set_carro(self,nome):
     self.nome = nome 

   def get_cor(self):
     return self.cor
   
   def set_cor(self,cor):
     self.cor = cor

   def get_placa(self):
     return self.placa
   
   def set_placa (self,placa):
     self.placa = placa

   def get_potencia(self):
     return self.potencia
   
   def set_potencia(self,potencia):
     self.potencia = potencia



class Dono():
  def __init__(self):
    self.nome = "Pedro"
    self.idade = "31"
    self.numero = "110000000"
   
  def get_nome(self):
    return self.nome
  
  def set_nome (self,nome):
    self.nome = nome

  def get_idade(self):
    return self.idade
  
  def set_idade(self,idade):
    self.idade = idade
 
  def get_numero(self):
    return self.numero
  
  def set_numero(self,numero):
    self.numero = numero
  

class Oficina(Carro_antigo,Dono):
  def __init__(self):
        super().__init__()
        self.motor = "false"
        self.embreagem = "false"
        self.alinhamento = "false"
        self.pintura = "false"


  def set_problema_motor(self,motor):
    self.motor = input("Digite o problema do motor:")
    self.motor = motor

  def verificar_motor(self,motor):
    print("O problema no motor agora é {}".format(self.motor))
    

  def verificar_embreagem(self,embreagem): 
    print("O problema na embreagem agora é {}".format(self.embreagem))
  

Carro = Oficina()

Carro.motor = "True"
Carro.embreagem = "True"

Carro.verificar_embreagem
Carro.verificar_motor







    
  
   

