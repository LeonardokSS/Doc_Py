import pandas as pd



# A importação de arquivos serve para importar todas a informações de um arquivo para o programa. Todas a informações importadas serão armazanadas dentro de uma variável.


#Leitura de arquivos em um banco de dados

Bc = pd.read_csv('funcionarios.csv')
print(Bc)


#Leitura de EXEL

df = pd.read_excel('Nome.exel',sheet_name="Nome_da_aba")
print(df)