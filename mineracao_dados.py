import pandas as pd
import numpy as np

dados = {
    'ID': range(1, 21),
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana', 'Kaique', 'Laura', 'Marcos', 'Nina', 'Otávio', 'Patricia', 'Quintino', 'Rafaela', 'Samuel', 'Tatiana'],
    'Idade': [23, 45, 35, 29, 41, 120, np.nan, 31, 27, 33, 26, 30, 28, 150, 32, 35, 27, 29, np.nan, 100], 
    'Gênero': ['Feminino', 'Masculino', 'Masculino', 'Feminino', 'Masculino', np.nan, 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino', 'Outro'], # Erro em 'Genêro' e categoria inesperada 'Outro'
    'Salário': [50000, 60000, 70000, 55000, 65000, 200000, 52000, 49000, 47000, 54000, 56000, 58000, np.nan, 300000, 59000, 53000, 51000, np.nan, 64000, 250000], 
    'Satisfação': ['Alta', 'Média', 'Baixa', 'Alta', 'Média', 'Alta', np.nan, 'Média', 'Baixa', 'Alta', 'Média', 'Baixa', 'Alta', 'Média', 'Baixa', 'Alta', 'Média', 'Baixa', 'Alta', 'Média'],
    'Departamento': ['TI', 'RH', 'Marketing', 'Financeiro', 'TI', 'RH', 'Marketing', np.nan, 'TI', 'RH', 'Marketing', 'Financeiro', 'TI', 'RH', 'Marketing', 'Financeiro', 'TI', 'RH', 'Marketing', 'Financeiro']
}

df = pd.DataFrame(dados)

df = df.dropna()
df = df.drop_duplicates()
print(df.describe())
print(df.info())
