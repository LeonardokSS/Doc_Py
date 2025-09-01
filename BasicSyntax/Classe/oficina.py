class motor():
    def __init__(self):
        self.potencia = 100
        self.torque = 20
        self.turbo = False
        
    #Quando usamos as funções de set, adiante no codigo, mesmo que o valor deles seja igual, precisamos usar o self.
    #Porque se utilizarmos o self. o Python sabera que você esta se referenciando ao objeto do que voçê adicionou
        
    def set_potencia(self,potencia):
        self.potencia = potencia 

    def set_turbo(self,turbo):
        self.turbo = turbo
    
    def set_torque(self,torque):
        self.torque = torque

    def Instalar_Turbo(self):
        print ('Agora seu carro possue o turbo {}'.format(self.turbo))
        self.potencia + 20
        self.torque + 20

    def Check_Potencia(self):
        print('O turbo do seu carro é {} sua potêcia é {} e o torque é {}'.format(self.turbo,self.potencia,self.torque))


#O objeto BMW entrou na class, então sempre para modificar os atributos do objeto BWM temos que utilizar o self
BMW = motor()
BMW.potencia = 90
BMW.torque = 30
BMW.turbo = 'False'

BMW.Instalar_Turbo

BMW.Check_Potencia
    
    
