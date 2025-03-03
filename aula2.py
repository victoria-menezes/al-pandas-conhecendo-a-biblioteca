# # O processo de Análise Exploratória de Dados (EDA) consiste em buscar entender como são estruturados os dados que queremos analisar.
# É um processo de caráter investigativo, onde tentamos compreender várias características, como: os valores presentes nas colunas, os tipos de estrutura de dados, verificar se são dados qualitativos ou quantitativos, se há valores faltantes ou incomuns.
# Por isso, nesse momento, perguntas sobre os dados são sempre bem-vindas. Elas irão guiar todo o processo de análise, e, através das ferramentas disponíveis, como o nosso querido Pandas, iremos buscar por respostas.
# Algumas perguntas que podemos fazer nesse momento:
#     Quais os valores médios de aluguel por tipo de imóvel?
#     Qual o percentual de cada tipo de imóvel na nossa base de dados?

## IMPORTANDO OS DADOS
import pandas as pd
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';') # tipo DataFrame

## QUAL O VALOR MÉDIO POR TIPO DE IMÓVEL?
# Tipo de imóvel: coluna 0
# Valor: coluna 6

# media_valores = dados['Valor'].mean() # MÉDIA DE TODOS OS VALORES
# df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor') # numeric_only = True para evitar que pegue as colunas não numéricas, mais útil caso não especifique a coluna. o [['Valor']] em vez de ['Valor'] retorna um dataframe
# esses dados incluem imoveis de tipo não residenciais, e portanto tem uma variacao de valor muito alta

# queremos entao SOMENTE os dados residenciais
imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']
  
df_residenciais = dados.query('@imoveis_comerciais not in Tipo') # sintaxe semelhante ao SQL, @ é uma variável
df_preco_tipo = df_residenciais.groupby('Tipo')[['Valor']].mean(numeric_only=True).sort_values('Valor')
df_preco_tipo.plot(kind='barh', figsize=(14,10), color='purple')
plt.savefig('figures/preco_tipo_aula2-1.png')
plt.clf()

## PERCENTUAL DE CADA TIPO DE IMÓVEL
df_preco_tipo_percentual = df_residenciais.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion') # normalize coloca no formato percentual (de 0 a 1)
df_preco_tipo_percentual.plot(kind='bar', figsize=(14,10), color='green', xlabel='Tipos', ylabel='Percentual')
plt.savefig('figures/preco_tipo_aula2-2.png')

## SELECIONANDO APENAS IMÓVEIS TIPO APARTAMENTO
df_apartamentos = dados.query('Tipo == "Apartamento"')