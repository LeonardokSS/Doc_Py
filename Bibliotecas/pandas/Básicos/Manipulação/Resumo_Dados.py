import pandas as pd

funcionarios = {
    "ID": [1001, 1002, 1003, 1004, 1005],
    "Nome": ["Ana Silva", "João Santos", "Maria Oliveira", "Pedro Costa", "Julia Lima"],
    "Idade": [28, 35, 42, 31, 29],
    "Cargo": ["Analista", "Gerente", "Desenvolvedor", "Designer", "Coordenador"],
    "Salário": [5000.00, 8500.00, 6200.00, 4800.00, 7000.00]
}

df = pd.DataFrame(funcionarios)

#Mostrar o tipo de variável armazenada em cada coluna
df.info(funcionarios)

#Serve para fazer todas as médias com os valores, com mediana, valor máx, valor min, % e etc
df.describe(funcionarios)

#Soma de todos os valores de uma coluna
df['Salario'].sum(funcionarios)

#Média de todos os valores de uma coluna
df['Salario'].mean(funcionarios)

#Retorna o valor do meio
df["Salario"].median(funcionarios)

#Valor máximo
Maior_Salário = df["Salario"].max(funcionarios)
print('O maior salário é {}'.format(Maior_Salário))



