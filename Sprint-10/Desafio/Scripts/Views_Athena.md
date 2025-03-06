## Este arquivo contém as consultas realizadas no AWS Athena para criar as views.

#### 1.Quais diretores mais produziram filmes?
```sql
CREATE OR REPLACE VIEW "top_10_diretores" AS 
SELECT
  d.nome
, COUNT(DISTINCT f.pk_fato) qtd_filmes
FROM
  ("AwsDataCatalog"."data_lake_db"."fato_filme" f
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_diretores" d ON (f.id_diretor = d.id_diretor))
GROUP BY d.nome
ORDER BY qtd_filmes DESC
LIMIT 10
```

#### 2.Quais atores mais atuaram em filmes?
```sql
CREATE OR REPLACE VIEW "top_atores" AS 
SELECT
  a.nome_ator nome_ator
, COUNT(f.id_filme) quantidade_filmes
FROM
  ("AwsDataCatalog"."data_lake_db"."fato_filme" f
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_atores" a ON (f.id_ator = a.id_ator))
GROUP BY a.nome_ator
ORDER BY quantidade_filmes DESC
LIMIT 50
```

#### 3.Qual é a quantidade de filmes produzidos por diretores mulheres em comparação com filmes produzidos por diretores homens?
```sql
CREATE OR REPLACE VIEW "quantidade_diretores_mulheres_comparado_homens" AS 
SELECT
  (CASE dd.genero WHEN 1 THEN 'Feminino' WHEN 2 THEN 'Masculino' END) genero_diretor
, COUNT(DISTINCT ff.id_filme) quantidade_filmes
FROM
  ("AwsDataCatalog"."data_lake_db"."dim_diretores" dd
INNER JOIN "AwsDataCatalog"."data_lake_db"."fato_filme" ff ON (dd.id_diretor = ff.id_diretor))
WHERE (dd.genero IN (1, 2))
GROUP BY (CASE dd.genero WHEN 1 THEN 'Feminino' WHEN 2 THEN 'Masculino' END)
ORDER BY (CASE dd.genero WHEN 1 THEN 'Feminino' WHEN 2 THEN 'Masculino' END) ASC
```

#### 4.Qual a quantidade de filmes lançados dos generos drama e romance ao longo dos anos?
```sql
CREATE OR REPLACE VIEW "quantidade_filmes_drama_romance_ambos_por_ano" AS 
SELECT
  d.ano
, COUNT(f.id_filme) quantidade_filmes
FROM
  (("AwsDataCatalog"."data_lake_db"."fato_filme" f
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_data" d ON (f.id_data = d.id_data))
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_filme" df ON (f.id_filme = df.id_filme))
WHERE ((df.genero = 'Drama') OR (df.genero = 'Romance') OR ((df.genero = 'Drama e Romance') AND (d.ano BETWEEN 1960 AND 2022)))
GROUP BY d.ano
ORDER BY d.ano ASC
```

#### 5.Relação entre orçamento e popularidade dos filmes;
```sql
CREATE OR REPLACE VIEW "relacao_orcamento_popularidade" AS 
SELECT DISTINCT
  f.id_filme
, df.titulo
, f.orcamento
, f.popularidade
FROM
  ("AwsDataCatalog"."data_lake_db"."fato_filme" f
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_filme" df ON (f.id_filme = df.id_filme))
ORDER BY f.popularidade DESC
```

#### 6.Quantidade total de filmes de drama e romance;
```sql
CREATE OR REPLACE VIEW "quantidade_filmes_por_ano" AS 
SELECT
  d.ano
, COUNT(f.id_filme) quantidade_filmes
FROM
  ("AwsDataCatalog"."data_lake_db"."fato_filme" f
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_data" d ON (f.id_data = d.id_data))
WHERE (d.ano BETWEEN 1960 AND 2022)
GROUP BY d.ano
ORDER BY d.ano ASC
```


#### 7.Quais diretores também atuaram?
```sql
CREATE OR REPLACE VIEW "diretores_que_atuaram" AS 
SELECT
  d.nome nome_diretor
, COUNT(DISTINCT f.id_filme) quantidade_filmes
FROM
  (("AwsDataCatalog"."data_lake_db"."fato_filme" f
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_diretores" d ON (f.id_diretor = d.id_diretor))
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_atores" a ON (f.id_ator = a.id_ator))
WHERE (d.nome = a.nome_ator)
GROUP BY d.nome
ORDER BY quantidade_filmes DESC
LIMIT 10
```
#### 8.Quais filmes com baixo orçamento tiveram grande sucesso de bilheteria?
```sql
CREATE OR REPLACE VIEW "filmes_baixo_orcamento_alta_bilheteria" AS 
SELECT DISTINCT
  f.id_filme
, df.titulo
, df.duracao
, df.genero
, f.orcamento
, f.bilheteria
, f.popularidade
FROM
  ("AwsDataCatalog"."data_lake_db"."fato_filme" f
INNER JOIN "AwsDataCatalog"."data_lake_db"."dim_filme" df ON (f.id_filme = df.id_filme))
WHERE ((f.orcamento < 10000000) AND (f.bilheteria > 10000000))
ORDER BY f.bilheteria DESC
```