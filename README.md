# Análise Preditiva

## Henrique de Castilhos

## N2

### 1. Problema de Análise Preditiva

#### a. Descrever o problema

Em um cenário de e-commerce, a empresa está enfrentando desafios relacionados à gestão de estoque de produtos. Os problemas incluem excesso de estoque em alguns itens, resultando em custos de armazenamento elevados, e falta de estoque em outros, levando a perda de vendas e insatisfação dos clientes. A empresa deseja uma análise detalhada para otimizar sua gestão de estoque.

#### b. Descrever a solução proposta

1. **Coleta de dados**
   - Reunir dados históricos de vendas e estoque para um período significativo.
   - Identificar produtos em estoque e seus atributos, como categoria, fornecedor, preço, etc.
   - Coletar dados de vendas, incluindo datas de vendas, quantidade vendida e receita gerada.
2. **Análise de Dados Descritiva**
   - Realizar análises estatísticas descritivas para entender a distribuição de vendas e estoque.
   - Calcular métricas-chave, como média, mediana, desvio padrão e coeficiente de variação para os produtos.
   - Gerar gráficos, como histogramas e box plots, para visualizar a distribuição dos dados.
3. **Segmentação de Produtos**
   - Classificar os produtos em categorias com base em seus atributos, como popularidade, margem de lucro, sazonalidade, etc.
   - Identificar produtos com alta demanda e produtos sazonais que exigem estratégias específicas.
4. **Previsão de Demanda**
   - Utilizar técnicas de previsão de séries temporais para estimar a demanda futura para os produtos.
5. **Políticas de Reposição de Estoque**
   - Definir políticas de reposição de estoque com base nas análises.
   - Estabelecer pontos de pedido e níveis de estoque de segurança para diferentes produtos.

---

### 2. Disponibilizar no repositório, dados minimamente suficientes para a solução proposta

#### a. Gerar dados ou colher dados relacionados ao problema proposto

Os dados foram gerados utilizando o script [`01-generate_data.py`](./01-generate-data.py) e salvos em um banco de dados local Mongo. Um dump com dados gerados pode ser encontrado na pasta [`dump`](./dump/).

#### b. Executar as operações ETL de modo que altere o estado desses dados de estado bruto para estado pré-processado

## N3

Esta avaliação poderá ser solucionada em dupla, mas na interação (avaliação _in-loco_) da entrega será observado a participação individual. O objetivo é finalizar o fluxo de trabalho iniciado com as atividades N1, as quais foram expandidas com as atividades N2.Para tanto, pede-se que nesta avaliação haja a continuidade com a solução do problema apresentada na avaliação anterior, bem como os dados transformados e contidos no repositório,objetivando a construção de um ou mais modelos preditivos (quando mais que um faça a comparação), seguido de uma análise de resultado.

Os passos para apresentação _in-loco_ (dupla ou individual):

1. Resgate do problema/solução anterior (1,0);
2. Exibir os dados transformados (resultado da ETL anterior) (1,0);
3. Pipeline(s) para a modelagem preditiva (3,0);
4. Apresentar o(s) resultado(s) do(s) modelo(s) com ao menos duas métricas de análise preditiva (5,0).
   a. Análise do resultado (explicações, suposições feitas pelo Analista de Dados).

---

### 1. Resgate do problema/solução anterior

Os dados foram resgatados utilizando o script [`02-etl-data.py`](./02-etl-data.py) agrupados e salvos em um `.csv` chamado [`merged_data.csv`](./merged_data.csv).

### 2. Exibir os dados transformados

Para visualizar os dados transformados, basta abrir o arquivo `.csv` [`merged_data.csv`](./merged_data.csv).

### 3. Pipeline(s) para a modelagem preditiva

A pipeline de modelagem preditiva foi criada utilizando o notebook [`03-predictive-model.ipynb`](./03-predictive-model.ipynb).
