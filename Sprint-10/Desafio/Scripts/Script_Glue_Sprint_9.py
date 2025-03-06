import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, year, month, dayofmonth, md5, concat_ws, monotonically_increasing_id
from pyspark.sql.types import StringType

# @params: [JOB_NAME, S3_INPUT_MOVIES_CSV_PATH, S3_INPUT_MOVIES_JSON_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_MOVIES_CSV_PATH', 'S3_INPUT_MOVIES_JSON_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho dos dados
parquet_csv = spark.read.parquet(args['S3_INPUT_MOVIES_CSV_PATH'])
parquet_json = spark.read.parquet(args['S3_INPUT_MOVIES_JSON_PATH'])
refined_path = args['S3_TARGET_PATH']

# Filtrar gêneros Drama e Romance
filtered_parquet_csv = parquet_csv.filter(
    (col("genero").contains("Drama") & col("genero").contains("Romance")) |
    (col("genero").contains("Drama") & ~col("genero").contains("Romance")) |
    (col("genero").contains("Romance") & ~col("genero").contains("Drama"))
)

# Tabela: fato_filme
fato_filme = parquet_json.withColumn("ator", explode("actors")).select(
    monotonically_increasing_id().alias("pk_fato"),  
    col("movie_id").alias("id_filme"),  
    md5(col("release_date").cast("string")).alias("id_data"),  
    md5(concat_ws("", col("directors"))).alias("id_diretor"),  
    md5(col("ator")).alias("id_ator"),
    col("budget").alias("orcamento"),  
    col("revenue").alias("bilheteria"),  
    col("popularity").alias("popularidade")  
)

# Tabela: dim_data
dim_data = parquet_json.select(
    md5(col("release_date").cast("string")).alias("id_data"),             # id_data
    year(col("release_date")).alias("ano"),                               # ano
    month(col("release_date")).alias("mes"),                              # mes
    dayofmonth(col("release_date")).alias("dia")                          # dia
)

# Tabela: dim_filme
dim_filme = filtered_parquet_csv.select(
    col("id").alias("id_filme"),                                          # id_filme
    col("tituloPrincipal").alias("titulo"),                               # titulo
    col("tempoMinutos").alias("duracao"),                                 # duracao
    col("genero").alias("genero")
)

# Processar diretores
dim_diretores_temp = parquet_json.withColumn("diretor", explode("directors"))
dim_diretores = dim_diretores_temp.withColumn("genero", explode("director_genders")).select(
    md5(col("diretor")).alias("id_diretor"),                              # id_diretor
    col("diretor").alias("nome"),                                         # nome
    col("genero")                                                         # genero
)

# Processar atores
dim_atores = parquet_json.withColumn("ator", explode("actors")).select(
    md5(col("ator")).alias("id_ator"),                                    # id_ator
    col("ator").alias("nome_ator"),                                       # nome_ator
)

# Salvar os dados refinados na camada refined
fato_filme.write.mode("overwrite").parquet(f"{refined_path}fato_filme")       # fato_filme
dim_data.write.mode("overwrite").parquet(f"{refined_path}dim_data")           # dim_data
dim_filme.write.mode("overwrite").parquet(f"{refined_path}dim_filme")         # dim_filme
dim_atores.write.mode("overwrite").parquet(f"{refined_path}dim_atores")       # dim_atores
dim_diretores.write.mode("overwrite").parquet(f"{refined_path}dim_diretores") # dim_diretores

job.commit()
