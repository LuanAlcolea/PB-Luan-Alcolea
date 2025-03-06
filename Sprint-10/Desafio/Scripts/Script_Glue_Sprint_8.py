import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Meus imports
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType, DateType
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
    StructField("release_date", DateType(), True),
    StructField("budget", IntegerType(), True),
    StructField("revenue", IntegerType(), True),
    StructField("popularity", DoubleType(), True),
    StructField("genres", ArrayType(StringType()), True),
    StructField("actors", ArrayType(StringType()), True),
    StructField("directors", ArrayType(StringType()), True),
    StructField("director_genders", ArrayType(IntegerType()), True)
])

# Caminhos do S3
input_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
raw_file_path = input_path
trusted_file_path = f"{target_path}2025/03/05/movies_parquet"

# Ler JSONs do S3
df = spark.read.option("multiline", "true").json(raw_file_path, schema=schema)

# Normalizar os dados
df = df.na.drop()
df = df.dropDuplicates()
df = df.dropDuplicates(["movie_id"])
df = df.filter(col("budget") != 0)
df = df.filter(col("revenue") != 0)
df = df.withColumn("release_date", to_date(col("release_date"), "yyyy-MM-dd"))

# Salvar como Parquet no S3
df.write.mode("overwrite").parquet(trusted_file_path)

print(f"Arquivos Parquet gerados e salvos em: {trusted_file_path}")

job.commit()
