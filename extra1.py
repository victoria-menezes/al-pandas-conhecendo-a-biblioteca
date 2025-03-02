# Para praticar os métodos aprendidos no decorrer dessa aula e também aprender novos, vamos realizar algumas análises utilizando um arquivo csv diferente: alunos.csv.
# 1) Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.

import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

dados = pd.read_csv(url)

# 2) Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.
print('PRIMEIRAS 7 LINHAS:')
print(dados.head(7))
print('\nULTIMAS 5 LINHAS:')
print(dados.tail(5))

# 3) Confira a quantidade de linhas e colunas desse DataFrame.
print(f'\n{dados.shape[0]} linhas x {dados.shape[1]} colunas\n')

# 4) Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.
print(dados['Nome'])
print(dados['Notas'])

# Extra: Calcule algumas estatísticas descritivas básicas dos dados do DataFrame (média, desvio padrão, etc). Dica: pesquise pelo método describe.
print(dados.describe())