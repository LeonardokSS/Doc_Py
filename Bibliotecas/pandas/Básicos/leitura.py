import pandas as pd
import numpy as np


Dicionário = {
 "Nomes": ["Ana", "Bruno", "Carlos"],
 "Idades": [23, 34, 45],
}

#Leitura de um dicionário e conversão para DataFrame
di = pd.DataFrame(Dicionário)
print (di)

#Lê o arquivo Excel e carrega a tabela em um DataFrame
print("EXEL")
ex = pd.read_excel('Dados/cardapio_restaurante.xlss', sheet_name='Cardápio')
print(ex)

 #Leitura de arquivos em um banco de dados
Bc = pd.read_csv('funcionarios.csv')
print(Bc)

#Leitura de JSON e conversão para DataFrame
Js = pd.read_json("Dados/pratos.json") 


# Leitura dos 5 primeiros e últimos registros de um DataFrame
#Isso tranforma o dicionário em um DataFrame

df = pd.DataFrame(Dicionário)
print("PRIMEIROS")
df.head()
print("Últimos")
df.tail()

#Leitura simples de itens de um DataFrame
print(df["Nomes"])
print(df["Idades"])

#Leitura pela posição 
#DataFrame.iloc[], Esse método seleciona colunas e linhas por numeros inteiros começando pe'lo 0
df2 = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [23, 35, 30],
    'cidade': ['SP', 'RJ', 'BH']
})

#print(variavel.iloc[linha,coluna])
#O primeiro numero é incluido, o segundo não conta, apenas a posição anterior. Vazio começo = desde o início Vazio fim = até o final
# Pega a linha 0 e coluna 1 (idade de Ana)
print(df2.iloc[0, 1])  # Saída: 23

# Pega todas as linhas, coluna 2 (cidade)
print(df2.iloc[:, 2])

# Pega linhas 0 a 1 e colunas 0 a 1
print(df2.iloc[0:2, 0:2])


#o pandas ve o dicionario assim:
#| índice | nome   | idade | cidade |
#| ------ | --0--- | --1-- | --2--- |
#| 0      | Ana    | 23    | SP     |
#| 1      | Bruno  | 35    | RJ     |
#| 2      | Carlos | 30    | BH     |


