import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Meus imports
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import col

## @params: [JOB_NAME, S3_INPUT_PATH_MOVIES, S3_INPUT_PATH_MOVIES, S3_TARGET_PATH_MOVIES, S3_TARGET_PATH_MOVIES]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_MOVIES', 'S3_INPUT_PATH_SERIES','S3_TARGET_PATH_MOVIES', 'S3_TARGET_PATH_SERIES'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Função para ler CSV do S3
def ReadCSV(schema, csv_path):
    return spark.read.option("delimiter", "|").option("header", "false").schema(schema).csv(csv_path)


# Função para normalizar CSV movies
def NormalizeCSV_movies(df):
    df = df.replace("\\N", None)
    df = df.na.drop()
    df = df.filter(
                   (col("notaMedia") > 0) & (col("numeroVotos") > 0) &
                   (col("tempoMinutos") > 0) & (col("anoNascimento") > 0) & (col("anoFalecimento") > 0) &
                   (col("anoLancamento") > 0) & (col("personagem") != "\\N"))
    return df


# Função para normalizar CSV series
def NormalizeCSV_series(df):
    df = df.replace("\\N", None)
    df = df.na.drop()
    df = df.filter(
                   (col("notaMedia") > 0) & (col("numeroVotos") > 0) &
                   (col("tempoMinutos") > 0) & (col("anoNascimento") > 0) & (col("anoFalecimento") > 0) &
                   (col("anoLancamento") > 0) & (col("anoTermino") > 0) & (col("personagem") != "\\N"))
    return df


# Schema do movies
movies_schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Schema do series
series_schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("anoTermino", IntegerType(), True),     
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Caminhos do S3
input_path_movies = args['S3_INPUT_PATH_MOVIES']
input_path_series = args['S3_INPUT_PATH_SERIES']
target_path_movies = args['S3_TARGET_PATH_MOVIES']
target_path_series = args['S3_TARGET_PATH_SERIES']

# Ler e normalizar os CSVs
df_movies = ReadCSV(movies_schema, input_path_movies)
df_movies = NormalizeCSV_movies(df_movies)

df_series = ReadCSV(series_schema, input_path_series)
df_series = NormalizeCSV_series(df_series)

# Renomear colunas inconsistentes
df_movies = df_movies.withColumnRenamed("tituloPincipal", "tituloPrincipal")
df_series = df_series.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Salvar como Parquet no S3
df_movies.write.mode("overwrite").parquet(target_path_movies)
df_series.write.mode("overwrite").parquet(target_path_series)

print(f"Arquivos convertidos para parquet com sucesso e salvo em: {target_path_movies} e {target_path_series}")

job.commit()
