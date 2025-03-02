## IMPORTANDO OS DADOS
import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
print()
dados = pd.read_csv(url, sep=';') # tipo DataFrame
print(dados.head(10)) # retorna as 10 primeiras linhas, tail() para retornar as x ultimas

## EXPLORAR CARACTERÍSTICAS GERAIS DOS DADOS
print(dados.shape) # linhas x colunas
print(dados.columns) # nomes das colunas
print(dados.info()) # retorna os tipos de dado em cada coluna
print(dados['Tipo']) # series : indices x valores