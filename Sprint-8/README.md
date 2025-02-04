# Sprint 8
## Resumo
O objetivo desta sprint é realizar a etapa de transformação dos arquivos de dados presentes na camada Raw para a camada Trusted, em que os arquivos se encontrarão limpos e confiáveis. Vamos converter os arquivos de diversos formatos para um único formato de arquivo chamado Parquet. A ferramenta que utilizaremos é o Apache Spark para a extração, processamento e conversão de dados. O serviço que utilizaremos é o AWS Glue para a execução do desafio.

Vamos criar dois Jobs no AWS Glue, um para transformar os arquivos de origem da API TMDB e outro para transformar os arquivos de origem local. Após a conversão dos arquivos e guarda-los em seus respectivos diretórios dentro do AWS S3, devemos criar Crawlers e executar uma breve consulta no AWS Athena usando o código automatico do serviço com o intuito de verificar os dados presentes nos arquivos Parquet.

* Abaixo segue um exemplo de como eu armazenei os arquivos processados oriundos da API TMDB:

```
data-lake-luan/Trusted/TMDB/Parquet/Movies/Year/Month/Day movies_details_parquet/
```

* Para o armazenamento dos arquivos de origem local os diretórios foi dispostos da seguinte forma:

```
movies: data-lake-luan/Trusted/Local/Parquet/Movies/
series: data-lake-luan/Trusted/Local/Parquet/Series/
```

* [Ir para o README dos exercícios](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-8/Exercícios/README.md)
* [Ir para o README do desafio](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-8/Desafio/README.md)
* [Ir para o README das evidências](https://github.com/LuanAlcolea/PB-Luan-Alcolea/tree/main/Sprint-8/Evidências/README.md)

## Exercícios propostos
Nesta sprint houve dois exercícios propostos para a fixação de conteúdo que trate de grandes quantidades de dados. O primeiro exercício vamos gerar um arquivo grande de nomes usando a biblioteca "names". O segundo exercício vamos utilizar o Apache Spark para criar um dataframe usando comandos próprios do PySpark e realizar algumas operações iguais usando o Spark SQL.

### Exercício: Gerador de nomes aleatorios
* Este exercício vamos gerar através de um script um arquivo chamado "nomes_aleatorios.txt" que sera utilizado no exercício. Primeiramente devemos realizar algumas etapas de aquecimentos (warm up), após isso vamos instalar ao nosso ambiente a biblitoeca "names" bem como incluí-la ao nosso código, e através dessa biblioteca vamos gerar o arquivo de nomes.


### Exercício: Apache Spark
* Neste exercício vamos utilizar como arquivo base o "nomes_aleatorios.txt" gerado no exercício anterior, foi disponibilizado dez etapas de execução para criar um dataframe final com as seguintes colunas: Nome, Escolariedade, Pais, AnoNascimento. Através de comando do PySpark e do Spark SQL realizaremos consultas ao nosso dataframe.

## Desafio proposto
O objetivo do desafio é processar os dados da camada raw para a camada trusted, vamos passar por todas as etapas de processamento e conversão para gerar arquivos no formato parquet otimizados para utilizar pouco armazenamento, processamento e próprio para consultas. Utilizando o serviço AWS Glue vamos criar dois Jobs das quais um de cada vai processar arquivos de formatos e origens diferentes, convertendo os arquivos para um formato em comun e armazenando os arquivos na camada Trusted do data-lake.


## Evidências de execução
Após todos os códigos serem executados foram extraídos através de capturas de tela os resultados e logs gerados pelos mesmos, abaixo está capturas de telas contendo logs de execução, bem como fragmentos de arquivos gerados e de código desenvolvido.
### Exercício: Gerador de nomes aleatorios
### Logs de execução do primeiro exercício.
* Capturas de tela do script.
![](/Sprint-8/Evidências/ex_1_log_1.png)
![](/Sprint-8/Evidências/ex_1_log_2.png)
### Captura de tela de um pequeno pedaço do arquivo "nomes_aleatorios.txt"
* Visão de um pedaço do arquivo movies_details.json.
![](/Sprint-8/Evidências/ex_1_ps_6.png)

### Exercício: Apache Spark
### Fragmento do script de "Apache Spark".
* Script "Apache Spark"
![](/Sprint-8/Evidências/ex_2_cd_1.png)
![](/Sprint-8/Evidências/ex_2_cd_2.png)
### Log de execução do script
* Log de execução do script "Apache Spark"
![](/Sprint-8/Evidências/ex_2_log_4.png)
### Evidência do desafio
### Logs de execução dos scripts no AWS GLUE
* Logs de execução do script no AWS Glue
![](/Sprint-8/Evidências/de_log_1.png)
![](/Sprint-8/Evidências/de_log_2.png)
### Arquivos gerados pelos scripts
* Arquivos parquet gerados e armazenados no AWS S3
![](/Sprint-8/Evidências/de_bk_1.png)
### Resultado da consulta no AWS Athena de um dos Crawlers
* Um dos crawlers executado no AWS Athena
![](/Sprint-8/Evidências/de_cw_1.png)
## Cursos externos
Nesta sprint houve um curso opcional exerterno nomeado de "Tutoriais Técnicos - Analytics".