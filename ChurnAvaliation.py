# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

#     PASSO A PASSO DE SOLUCAO DO PROBLEMA:
# 
#     - Passo 1: Importar a base de dados
#     - Passo 2: Visualizar a base de dados
#         - Entender as informacoes que temos disponível
#         - Descobrir os possíveis erros na base de dados
#     - Passo 3:
#          - Valores que sao números e estao reconhecidos como texto
#          - Valores vazios
#     - Passo 4: Análise inicial (Análise Exploratória) -> ver como estao os cancelamentos
#     - Passo 5: Observar cada característica do seu cliente e ver como aquela característica impacta no cancelamento

#==============================================
# Passo 1: Importar a base de dados

import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

#==============================================
# Passo 2: 

display(tabela)

#==============================================
# Passo 3

# Dados que nao nos interessam
# Coluna Unnamed é inútil (deletar)
tabela = tabela.drop("Unnamed: 0", axis=1)

#display(tabela)

# Ver se tem colunas com tipagem de texto ao invés de número
# print(tabela.info())

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Valor vazio (NaN) None
# colunas completamente vazias
tabela = tabela.dropna(how="all", axis=1)

# linhas vazias
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

#==============================================
# Passo 4 - Como estao os nossos cancelamentos ?

display(tabela["Churn"].value_counts())
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#==============================================
# Passo 5

import plotly.express as px

# para edicoes nos gráficos: https: //plotly.com/python/histograms/ 

#grafico = px.histogram(tabela,x="MesesComoCliente", color="Churn")
#grafico.show()

#para percorrer as linhas: tabela.index
# o for percorre por padrao cada coluna da tabela, logo o nome 'coluna' é apenas uma referência natural 
for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    #display(grafico)
    grafico.show()

#==============================================