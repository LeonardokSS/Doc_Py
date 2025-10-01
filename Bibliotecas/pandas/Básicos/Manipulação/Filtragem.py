import pandas as pd

df = pd.read_excel('cardapio_restaurante.xlsx', sheet_name='Cardápio')
print (df)


#Mostrar colunas 
#Mostra apenas as colunas de preço e de tempo
print('Separando por colunas')

print (df[['Preço', 'Categoria']])



# A filtragem dos dados pode ser feita usando condições como: nome_variavel['nome_coluna'] > valor

filtro_preco_b = df['Preço'] > 10  

#A filtragem pode ser feita de forma que apenas os itens que condizem com tal condição sejam exibidos:
# var = var[var{mome_coluna]condição]

Filtro_preco_a = df[df['Preço'] > 10]

#Podemos tabém filtrar varias colunas ao mesmo tempo, basta unir os filtros por meio de (&) 

Filtro_tempo = df[df['Tempo de Preparo (min)'] >= 10]
Filtro_disponivel = df[df['Disponível (Sim/Não)'] =="Sim"]



Filtro_tempo_disponivel = df[Filtro_disponivel & Filtro_tempo]

print(df.columns)