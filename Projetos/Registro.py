class Carro_antigo():
   
   # Definição de variaveis de input
   def __init__(self):
    self.nome = "Fusca"
    self.cor = "Preto"
    self.placa = "GSE2S-22"
    self.potencia = "100"
    self.turbo = False

#O self serve como uma variavel que tem mesmo valor de outra variavel, a diferença é que o self é uma variavel interna da classe.
   def get_carro(self):
    print (self.nome)
   
   def set_carro(self,nome):
     self.nome = nome 

   def get_cor(self):
    print (self.cor)
   
   def set_cor(self,cor):
     self.cor = cor

   def get_placa(self):
     print (self.placa)
   
   def set_placa (self,placa):
     self.placa = placa

   def get_potencia(self):
    print (self.potencia)
   
   def set_potencia(self,potencia):
     self.potencia = potencia

   def set_turbo(self,turbo):
     self.turbo = turbo
     

   def get_turbo(self):
     print(self.turbo)
      

Bmw = Carro_antigo()
Bmw.set_carro('Bmw')
Bmw.set_cor('Azsa')
Bmw.set_placa('Salsa')
Bmw.set_potencia('10000000000C')
Bmw.set_turbo(True)

Bmw.get_carro()
Bmw.get_placa()
Bmw.get_cor()
Bmw.get_potencia()
Bmw.get_turbo()








