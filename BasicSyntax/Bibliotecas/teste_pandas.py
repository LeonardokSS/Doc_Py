import pandas as pd
# pd é o apelhido para pandas, para facilitar o uso do pandas

Funcionarios = {
    "Nomes":["Pedro","Bruno","João"],
    "Idade":[25,30,35],
}

#Le o arquivo e transforma em um DataFrame, ou um planilha de exel

Df = pd.DataFrame(Funcionarios)

print(Df)

#Le o arquivo e transforma em uma coluna

Coluna = pd.Series(Funcionarios)
print(Coluna)

#Leitura de arquivos em um banco de dados

Bc = pd.read_csv('funcionarios.csv')
print(Bc)


#Leitura de EXEL

df = pd.read_excel('Nome.exel',sheet_name="Nome_da_aba")
print(df)

#-----Argumentos de formatação no texto-----





#------MANIPULAÇÃO DE DADOS-------

#Mostra os primeiros 5 itens da tabela

df.head(Funcionarios)


#Mostra os últimos 5 itens da tabela

df.tail(Funcionarios)








