import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Meus imports
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType
from pyspark.sql.functions import col

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
    StructField("rating", FloatType(), True),
    StructField("budget", IntegerType(), True),
    StructField("revenue", IntegerType(), True),
    StructField("actors", ArrayType(StringType()), True),
    StructField("genres", ArrayType(StringType()), True),
    StructField("crew", ArrayType(StructType([
        StructField("name", StringType(), True),
        StructField("job", StringType(), True)
    ])), True)
])

# Caminhos do S3
input_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
raw_file_path = f"{input_path}movies_details.json"
trusted_file_path = f"{target_path}/2025/01/20/movies_details_parquet"

# Ler JSON do S3
df = spark.read.option("multiline", "true").json(raw_file_path, schema=schema)

# Normalizar os dados
df = df.na.drop()
df = df.filter(col("rating") != 0)

# Salvar como parquet no S3
df.write.mode("overwrite").parquet(trusted_file_path)

print(f"Arquivos Parquet gerados e salvos em: {trusted_file_path}")

job.commit()
