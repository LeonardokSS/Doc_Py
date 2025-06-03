#Também é possível fazer herança múltipla em python, basta: class nome_classe(Base1, Base2, Base3): atributos.. métodos.. self..

class Pessoa():

    

    def __init__(self):
        self.nome = 'Roberto'
        self.idade = '16'
        self.gênero = 'Masculino'
        self.telefone = '11978421029'

    def get_nome(self):
        return self.nome 
    
    def set_nome(self,nome):
        self.nome = nome

    def get_idade(self):
        return self.idade 
    
    def set_idade(self,idade):
        self.idade = idade
    
    def get_gênero(self):
        return self.gênero 
    
    def set_gênero(self,gênero):
        self.gênero = gênero

    
    def get_telefone(self):
        return self.telefone 
    
    def set_telefone(self,telefone):
        self.telefone = telefone


class Trabalho():

    def __init__(self):
        self.tipo = 'Engenharia Cívil'
        self.salário = 2500
        self.carga_horária = '12 horas por dia'
        self.cargo = 'Engenheiro'

    def get_tipo(self):
        return self.tipo
    
    def get_salário(self):
        return self.salário
    
    def get_carga_horária(self):
        return self.carga_horária
    
    def get_cargo(self):
        return self.cargo
    
    def set_tipo(self,tipo):
        self.tipo = tipo

    def set_salário(self,salário):
        self.salário= salário

    def set_carga_horária(self,carga_horária):
        self.carga_horária = carga_horária

    def set_cargo(self,cargo):
        self.cargo = cargo



class Funcionário(Pessoa, Trabalho):

    def __init__(self):
        super().__init__()
        
        self.trabalho = 'false'
        self.aumento = 0
        self.descanso = 'false'
       

    
    def trabalhar(self):
        print('O funcionário {} está trabalhando'.format(self.nome))
        self.trabalho = 'true'

    def receber_aumento(self, aumento):
        print('O funcionário {} recebeu um aumento de {}'.format(self.nome, aumento))
        self.aumento = aumento

    def descansar(self):
        print('O funcionário {} está descansando agorá! '.format(self.nome))
        self.descanso = 'true'

    def get_trabalhar(self):
        return self.trabalho
    
    def get_ganhar_aumento(self):
        print('O funcionário tem um salário atual de {}'.format(self.salário+self.aumento))

    def get_descansar(self):
        return self.descanso
        
Rogério = Funcionário()

#Definindo valores da classe Pessoa

Rogério.nome = 'Rogério'
Rogério.idade = '30'
Rogério.gênero = 'Masculino'
Rogério.telefone = '112233445566'

#Definindo valores da classe Trabalho

Rogério.tipo = 'Engenharia de Software'
Rogério.carga_horária = '8 horas'
Rogério.cargo = 'Desenvolvedor Back-End Sênior'
Rogério.salário = 5000

#Definindo valores da classe Funcionário

Rogério.receber_aumento(200)
Rogério.get_ganhar_aumento()