import pandas as pd


funcionarios = {
    "ID": [1001, 1002, 1003, 1004, 1005],
    "Nome": ["Ana Silva", "João Santos", "Maria Oliveira", "Pedro Costa", "Julia Lima"],
    "Idade": [28, 35, 42, 31, 29],
    "Cargo": ["Analista", "Gerente", "Desenvolvedor", "Designer", "Coordenador"],
    "Salário": [5000.00, 8500.00, 6200.00, 4800.00, 7000.00]
}
df = pd.DataFrame(funcionarios)
#Para Criar uma coluna basta: df['Coluna_Nova'] = ['Coluna_Existente'] * 12

df['Salário Anual'] = ['Salario'] * 12

#Para deletar uma coluna basta: df = df.drop('Coluna_Excluir', axis=1)

df = df.drop('Salário Anual', axis = 1)
