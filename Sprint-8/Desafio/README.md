# Desafio Sprint 8
## Resumo do desafio
Este desafio representa a terceira etapa de cinco do desafio final, nesta etapa vamos criar uma camada "Trusted" no nosso data lake e vamos converter os arquivos de dados que estão presentes da camada "Raw" para um formato otimizado para consultas, bem como os dados deverão ser normalizados antes de serem convertidos. Vamos utilizar o serviço AWS Glue e a ferramenta da linguagem python chamada "PySpark". A execução será dividida em dois Jobs, uma para converter os arquivos oriundos da API TMDB e outro para converter os arquivos carregados da máquina local.

* [Ir para o script do Job 1](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-8/Desafio/Desafio-Sprint-8-JSON.py)
* [Ir para o script do Job 2](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-8/Desafio/Desafio-Sprint-8-CSV.py)


## Explicação sobre os passos de execução
O objetivo é converter os arquivos da camada "Raw" que estão em dois formatos diferentes que são: "CSV" e "JSON", bem como ambos são de origens diferentes, o primeiro é de origem local e o segundo é de origem da API TMDB.

* 1 - Criar um Job para converter o JSON para Parquet: o script vai usar a biblioteca PySpark para processar o dataframe extraído do S3, primeiro o código vai limpar os dados, removendo linhas inconsistentes e dados nulos, após isso será gravado na camada "Trusted" de forma particionada os arquivos "Parquet" gerado pelo PySpark.

* 2 - Criar um Job para converter os CSVs para Parquet: usando a biblioteca PySpark o script vai processar um dataframe para cada arquivo CSV extraído do S3, limpando os dados. Após o processamento os dois dataframes serão salvos em seus respectivos diretorios dentro da camada "Trusted".

* 3 - Os dados agora estão confiáveis e em um formato de arquivo conveniente para o uso, vamos criar um Crawler e um database para executar consultas SQL usando o serviço AWS Athena, neste ponto será possível observar que apenas os dados consistentes foram populados aos arquivos Parquet.
## Execução do desafio
Primeiramente eu desenvolvi os scripts no google colab para depois converte-los para o AWS Glue, o primeiro script que eu executei em um Job no AWS Glue foi o "Script_JSON_to_PARQUET.py"
#### Script JSON para Parquet

 Primeiras linhas do script: nas primeiras linhas do código eu importos as bibliotecas necessárias para as operações, em seguida configuro os caminhos de entrada e saída de dados do AWS S3. Com tudo configurado eu crio o esquema de registros do dataframe para carregar o arquivo json corretamente.

![](/Sprint-8/Evidências/de_s1_1.png)

 Abaixo está o esquema de dados do dataframe definido do código, e em seguida um fragmento do código JSON.

![](/Sprint-8/Evidências/de_s1_2.png)

![](/Sprint-7/Evidências/Evidencia_json.png)

 Em seguida adicionei as linhas de código para configurar as variáveis auxílares e executar as operações que são: carregar o arquivo JSON do input_path em um dataframe, normalizar o dataframe e salvar o dataframe em um arquivo no formato Parquet no output_path.

![](/Sprint-8/Evidências/de_s1_3.png)

#### Script CSVs para Parquet
 Iniciei o script com a estrutura básica de um código do AWS Glue, importei as bibliotecas necessárias e iniciei o PySpark.

![](/Sprint-8/Evidências/de_s2_1.png)

 Declarei três funções auxíliares para a execução do script.
 Função READ_CSV: Ler o CSV de um diretorio AWS S3 e carrega-lo em um dataframe.

 Função NormalizeCSV_Movies: Subistitue os valores "\N" para "None", remove todas as linhas que contenha os valores "None" e realiza uma série de verificações para manter apenas as linhas consistentes no dataframe.

 Função NormalizeCSV_Series: Realiza as mesmas operações da função acima, porem ajustada para atender as específicações do arquivo series.csv. 

![](/Sprint-8/Evidências/de_s2_2.png)

 Antes de carregar os dados do CSV para o dataframe movies eu defini o seu esquema do PySpark.

![](/Sprint-8/Evidências/de_s2_3.png)

 Realizo a mesma operação mas agora levando em consideração os dados do arquivo de series.

![](/Sprint-8/Evidências/de_s2_4.png)

 Agora é hora de programar a rotina de execução, criei quatro variáveis auxíliares para controlar o fluxo de arquivos dentro do S3. Depois declarei os meus dataframes df_movies e df_series, bem como chamei as duas funções para normalizar seus respectivos dataframes.

 Após a limpeza de dados dos dois dataframes eu salvo no formato parquet usando a função do dataframe pyspark "write.mode("overwrite").parquet(target_path)".

![](/Sprint-8/Evidências/de_s2_5.png)

## Resultados e logs da execução
Eu executei os dois Job no AWS Glue, o arquivos foram gerados em seus respectivos diretórios, abaixo está evidências da execução bem-sucedida.
* Log de execução do script json para parquet
![](/Sprint-8/Evidências/de_log_1.png)
* Log de execução do script csv para parquet
![](/Sprint-8/Evidências/de_log_2.png)
* Arquivo parquet gerado a partir do json
![](/Sprint-8/Evidências/de_bk_3.png)
* Arquivo parquet gerado a partir do movies.csv
![](/Sprint-8/Evidências/de_bk_1.png)
* Arquivo parquet gerado a partir do series.csv
![](/Sprint-8/Evidências/de_bk_2.png)
## Criando o Crawler para realizar consultas nos arquivos parquet
Criei os crawlers necessários para executar as consultas SQL no AWS Athena para verificar se os arquivos parquet.
* Resultado da consulta no parquet gerado a partir do json
![](/Sprint-8/Evidências/de_cw_1.png)
* Resultado da consulta no parquet gerado a partir do csv movies
![](/Sprint-8/Evidências/de_cw_2.png)
* Resultado da consulta no parquet gerado a partir do csv series
![](/Sprint-8/Evidências/de_cw_3.png)

Os arquivos e evidências desenvolvidas neste desafio estão todos carregados neste repositório.