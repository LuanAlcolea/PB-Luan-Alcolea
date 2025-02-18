# Este código representa a segunda implementação do script que converte os dados da camada raw para a camada trusted
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Meus imports
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from pyspark.sql.functions import col, to_date

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Esquema do JSON
schema = StructType([
    StructField("movie_id", StringType(), True),
    StructField("movie_name", StringType(), True),
    StructField("release_date", StringType(), True),
    StructField("rating", DoubleType(), True),
    StructField("budget", IntegerType(), True),
    StructField("revenue", IntegerType(), True),
    StructField("popularity", DoubleType(), True),
    StructField("actors", ArrayType(StringType()), True),
    StructField("actor_genders", ArrayType(IntegerType()), True),
    StructField("directors", ArrayType(StringType()), True),
    StructField("director_genders", ArrayType(IntegerType()), True),
    StructField("personagens", ArrayType(StringType()), True)
])

# Caminhos do S3
input_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
raw_file_path = f"{input_path}movies_json/*.json"
trusted_file_path = f"{target_path}2025/02/14/movies_parquet"

# Ler JSONs do S3
df = spark.read.option("multiline", "true").json(raw_file_path, schema=schema)

# Normalizar os dados
df = df.na.drop()
df = df.dropDuplicates() 
df = df.filter(col("rating") != 0)
df = df.withColumn("release_date", to_date(col("release_date"), "yyyy-MM-dd"))

# Salvar como Parquet no S3
df.write.mode("overwrite").parquet(trusted_file_path)

print(f"Arquivos Parquet gerados e salvos em: {trusted_file_path}")

job.commit()
