#Para se criar classes derivadas basta: class nome_classe(classe_base): atributos.. self.. métodos...
#Também é possível fazer a mesma coisa com nomes: class nome_classe(nomemódolo.class_base): atributos.. self.. métodos..

#Exemplo de Herança

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


Guilherme = Pessoa()

Guilherme.set_nome('Guilherme')
Guilherme.set_gênero('Masculinho')
Guilherme.set_idade('22')
Guilherme.set_telefone('1197732919')

class Aluno(Pessoa):

  

    def __init__(self):
        super().__init__()
        self.nome = 'Roberto'
        self.idade = '16'
        self.gênero = 'Masculino'
        self.telefone = '11978421029'

        self.Série = '1° EM'
        self.Nota = '6'
        self.Matrículo = False

    def get_série(self):
            return self.Série
        
    def set_série(self, série):
        self.Série = série

    def get_matricula(self):
            return self.Matrículo
    
    def set_matricula(self, Matrículo):
        self.Matrículo = Matrículo
        
    

Ricardo = Aluno()

#Usando métodos tanto da class Pessoa, tanto da class Aluno
Ricardo.set_série('9° FM')
Ricardo.set_nome('Ricardo')
Ricardo.set_matricula(True)

#Printando métodos tanto da class Pessoa, tanto da class Aluno

print(Ricardo.nome)
print(Ricardo.Série)
print(Ricardo.get_matricula())

        
        