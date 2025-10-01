import pandas as pd
#Arrays são usadas no pandas, por definição arrays são como listas que armazenam valores do mesmo tipo, e são identificadas por uma chave

#Estrutura basicas
#Dicionarios que possuem chaves e valores
Dicionário = {
 "Nomes": ["Ana", "Bruno", "Carlos"],
 "Idades": [23, 34, 45],
}

#Series são criadas a partir de listas com elementos. O pandas gera um RangeIndex padrão

s = pd.Series([1, 3, 5, 6, 8])

