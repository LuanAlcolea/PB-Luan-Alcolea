# Este é o script que filtra os dados que serão utilizados posteriomente. A origem dos dados no bucket é da camada trusted, o script traz eles filtrados para a camada refined
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, monotonically_increasing_id, year, month, dayofmonth, md5, concat_ws
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

# Tabela: fato_filme, dados: json
fato_filme = parquet_json.select(
    col("movie_id").alias("id_filme"),
    md5(col("release_date").cast("string")).alias("id_data"),
    col("revenue").alias("receita"),
    col("budget").alias("orcamento"),
    col("popularity").alias("nota_publica")
    )

# Tabela: dim_data, dados: json
dim_data = parquet_json.select(
    md5(col("release_date").cast("string")).alias("id_data"),
    year(col("release_date")).alias("ano"),
    month(col("release_date")).alias("mes"),
    dayofmonth(col("release_date")).alias("dia")
    )

# Tabela: dim_filme, dados: csv
dim_filme = parquet_csv.select(
    col("id").alias("id_filme"),
    col("tituloPrincipal").alias("titulo"),
    col("genero").alias("genero"),
    col("tempoMinutos").alias("duracao")
    )

# Tabela: dim_atores, dados: json
dim_atores_temp1 = parquet_json.withColumn("actor", explode("actors"))
dim_atores_temp2 = dim_atores_temp1.withColumn("genero_ator", explode("actor_genders"))
dim_atores_temp3 = dim_atores_temp2.withColumn("personagem", explode("personagens"))

dim_atores = dim_atores_temp3.select(
    md5(concat_ws("", col("actor"), col("genero_ator"), col("personagem"))).alias("id_ator"),
    col("actor").alias("nome"),
    col("genero_ator").alias("genero"),
    col("personagem")
)

# Tabela: dim_diretores, dados: json
dim_diretores_temp1 = parquet_json.withColumn("diretor", explode("directors"))
dim_diretores_temp2 = dim_diretores_temp1.withColumn("genero_diretor", explode("director_genders"))

dim_diretores = dim_diretores_temp2.select(
    md5(concat_ws("", col("diretor"), col("genero_diretor"))).alias("id_diretor"),
    col("diretor").alias("nome"),
    col("genero_diretor").alias("genero")
)

# Tabela: dim_bridge_filme
dim_bridge_filme_temp0 = parquet_json.withColumn("id_filme", col("movie_id"))
dim_bridge_filme_temp1 = dim_bridge_filme_temp0.withColumn("actor", explode("actors"))
dim_bridge_filme_temp2 = dim_bridge_filme_temp1.withColumn("genero_ator", explode("actor_genders"))
dim_bridge_filme_temp3 = dim_bridge_filme_temp2.withColumn("personagem", explode("personagens"))
dim_bridge_filme_temp4 = dim_bridge_filme_temp3.withColumn("diretor", explode("directors"))
dim_bridge_filme_temp5 = dim_bridge_filme_temp4.withColumn("genero_diretor", explode("director_genders"))

dim_bridge_filme = dim_bridge_filme_temp5.select(
    col("id_filme"),
    md5(concat_ws("", col("actor"), col("genero_ator"), col("personagem"))).alias("id_ator"),
    md5(concat_ws("", col("diretor"), col("genero_diretor"))).alias("id_diretor")
)

# Salvar parquets na camada refined
dim_data.write.mode("overwrite").parquet(f"{refined_path}dim_data")
dim_filme.write.mode("overwrite").parquet(f"{refined_path}dim_filme")
fato_filme.write.mode("overwrite").parquet(f"{refined_path}fato_filme")
dim_atores.write.mode("overwrite").parquet(f"{refined_path}dim_atores")
dim_diretores.write.mode("overwrite").parquet(f"{refined_path}dim_diretores")
dim_bridge_filme.write.mode("overwrite").parquet(f"{refined_path}dim_bridge_filme")

job.commit()