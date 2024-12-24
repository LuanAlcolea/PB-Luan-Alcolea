# Desafio Sprint 5
Neste desafio utilizamos os serviços da AWS para o seu desenvolvimento. O primeiro passo é baixar uma base de dados no site dados.gov.br, depois criar dois script python. O primeiro script devera configurar o acesso ao bucket pela maquina local e carregar o csv sem modificações para o mesmo. O segundo script deve baixar do bucket o csv e aplicar localmente uma serie de passos para o processamento de dados, após isso, o script deve carregar para o mesmo bucket o csv resultante. 
## Desenvolvimento
### Preparação de dados
No site dados.gov.br escolhi o arquivo de dados chamado "Aeronaves-Drones-Cadastrados.csv" para realizar o desafio, eu optei por utilizar este pois nele há informações consistentes e colunas interessantes para o processamento de dados.

* [Abrir site do database: Aeronaves-Drones-Cadastrados](https://dados.gov.br/dados/conjuntos-dados/aeronaves-drones-cadastrados)

### Scripts
Eu escrevi primeiramente dois scripts, um para ser importado como um modulo auxilar e o outro para configurar as credenciais, criar o bucket e carregar o dataframe no bucket.

### S3_lib
O script S3_lib contém variáveis e funções auxilares para que outros scripts possam utilizar com facilidade a biblioteca boto3.

* [Abrir script S3_lib.py](https://dados.gov.br/dados/conjuntos-dados/aeronaves-drones-cadastrados)

### Etapa-1
No script da primeira parte, eu importo a biblioteca auxilar criada para o código e utilizo suas funções para criar o bucket e carregar o arquivo baixado.

* [Abrir script Etapa-1.py](https://dados.gov.br/dados/conjuntos-dados/aeronaves-drones-cadastrados)

### Etapa-2
No script da segunda parte, começo importando a biblioteca auxilar e realizando um pré-processamento ao arquivo baixado do bucket. O pré-processamento consiste em retirar aspas, tratar dados nulos, ajustar caracteres conflitantes e erros de encodificação.
#### Processamento-1: filtrar dados usando ao menos dois operadores lógicos
Eu filtrei os dados da coluna "PESO_MAXIMO_DECOLAGEM_KG" para que apenas os valores dos intervalos 0.4 e 7.0 e os valores iguais a 8.0 estejam presentes no dataframe, os dois operadores foram o de maior/menor e de igual.
```python
dataframe = current_dataframe
    dataframe = dataframe.filter(
        (
            (pl.col("PESO_MAXIMO_DECOLAGEM_KG") > 0.4) & 
            (pl.col("PESO_MAXIMO_DECOLAGEM_KG") < 7.0) | 
            (pl.col("PESO_MAXIMO_DECOLAGEM_KG") == 8.0)
        )
    )
```
#### Processamento-2: realizar dois calculos de agregações
Criei duas novas colunas chamadas "TOTAL_PESO" e "MEDIA_PESO" por agregar duas vezes os valores da coluna "PESO_MAXIMO_DECOLAGEM_KG". A primeira agregação realiza a soma dos valores e a segunda gera a media dos valores da coluna.
```python
aggregated = dataframe.group_by("TIPO_USO").agg([
    pl.col("PESO_MAXIMO_DECOLAGEM_KG").sum().round(2).alias("TOTAL_PESO"),
    pl.col("PESO_MAXIMO_DECOLAGEM_KG").mean().round(2).alias("MEDIA_PESO")
    ])
    dataframe = dataframe.join(aggregated, on="TIPO_USO", how="left")
```
#### Processamento-3: Função condicional
Criei uma nova coluna chamada "PERFIL_CLIENTE" por realizar uma operação condicional nos valores da coluna "CPF_CNPJ". O valor das linhas "PERFIL_CLIENTE" é igual a "Pessoa_fisica" se o valor da coluna consultada tiver os caracteres "CPF" e caso contrario o valor sera "Empresa".
```python
dataframe = dataframe.with_columns([
        pl.when(pl.col("CPF_CNPJ").cast(pl.Utf8).str.contains("CPF"))
        .then(pl.lit("Pessoa_fisica"))
        .otherwise(pl.lit("Empresa")).alias("PERFIL_CLIENTE")
    ])
```
#### Processamento-4: Função de conversão
Eu converti o formato STR da coluna "DATA_VALIDADE" para o formato DATE.
```python
dataframe = dataframe.with_columns([
        pl.col("DATA_VALIDADE").str.to_date().alias("DATA_VALIDADE")
    ])
```
#### Processamento-5: Função de data
Nesta etapa o script cria uma nova coluna com o nome de "ESTA_VALIDO" e os seus valores são "Vencido" para os valores da coluna "DATA_VALIDADE" que estiverem menores ou igual a 2024 e "Dentro_do_prazo" para os valores que estiverem maiores que 2024.
```python
dataframe = dataframe.with_columns([
        pl.when(pl.col("DATA_VALIDADE").dt.year() <= 2024)
        .then(pl.lit("Vencido"))
        .otherwise(pl.lit("Dentro_do_prazo")).alias("ESTA_VALIDO")
    ])
```
#### Processamento-6: Função de string
Nesta parte, eu adicionei o underline/underscore para os textos da coluna "MODELO".
```python
dataframe = dataframe.with_columns([
        pl.col("MODELO")
        .str.replace_all(" ", "_")
        .alias("MODELO")
    ])
```

* [Abrir script Etapa-2.py](https://dados.gov.br/dados/conjuntos-dados/aeronaves-drones-cadastrados)

### Execução final do script
Após os processamentos, o dataframe é salvo localmente e carregado para o bucket com o nome "Aeronaves-Drones-Cadastrados-Processado.csv".


