# O time de ML chegou com algumas demandas de última hora para resolvermos nesse momento da análise exploratória. Essas demandas são:
# 1) Calcular a média de quartos por apartamento;
# 2) Conferir quantos bairros únicos existem na nossa base de dados;
# 3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas;
# 4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.

## IMPORTANDO OS DADOS
import pandas as pd
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';') # tipo DataFrame

## SELECIONANDO APENAS IMÓVEIS TIPO APARTAMENTO
df_apartamentos = dados.query('Tipo == "Apartamento"')

print(df_apartamentos.head(10))
## MÉDIA DE QUARTOS POR APTO
media_quartos = df_apartamentos['Quartos'].mean()
print(f'A média de quartos é {media_quartos}.')

## BAIRROS ÚNICOS
bairros = df_apartamentos['Bairro'].unique()
qtd_bairros = len(bairros)
print(qtd_bairros)

## QUAIS BAIRROS TEM O MAIOR ALUGUEL
bairros_aluguel_media = df_apartamentos.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False)
print(bairros_aluguel_media)

## GRÁFICO
bairros_aluguel_top10 = bairros_aluguel_media.head(5)
bairros_aluguel_top10.plot(kind='bar', figsize=(14,10), color='#E50914', xlabel='Bairro', ylabel='Valor médio')
plt.savefig('figures/extra2.png')