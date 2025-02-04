# --- Exercício 2 de spark da Sprint 8 --- #
# Script desenvolvido no google collab
import pandas
import random
from google.colab import files
from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import lit, udf, col

# Definições globais
files_to_upload = files.upload()
nomes_aleatorio = list(files_to_upload.keys())[0]

spark = SparkSession \
        .builder \
        .master ("local[*]") \
        .appName("Exercicio Intro") \
        .getOrCreate()

schema = StructType([
    StructField('Nome', StringType(), True)
])

# Funções
def get_random_indice_from_list(list):
    return random.choice(list)


def generate_random_int_in_range(min, max):
    return random.randint(min, max)


# Etapa 1: carregar "nomes_aleatorios.txt" atraves do comando spark.read.csv
# Imprimir alguns itens do novo dataframe
print("--- Etapa 1 ---")
print("Criando novo dataframe usando o arquivo 'nomes_aleatorios.txt'")
df_nomes = spark.read.csv(nomes_aleatorio, header=False)
print("Imprimindo 5 itens do dataframe")
df_nomes.show(5)

# Etapa 2: renomear a coluna com o nome automático para "Nomes"
print("--- Etapa 2 ---")
print("Renomeando a coluna com o nome automático para 'Nomes'")
df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")
print("Imprimindo 10 itens do dataframe")
df_nomes.show(10)


# Etapa 3: adicionar coluna Escolariedade com os seguintes valores:
# Fundamental, médio e superior, aleatorio para cada linha
print("--- Etapa 3 ---")
print("Adicionar uma coluna chamada 'Escolariedade' com 3 valores sendo aleatorios para cada linha")
escolariedade = ['Fundamental', 'Médio', 'Superior']
udf_escolariedade = udf(lambda: get_random_indice_from_list(escolariedade), StringType())
df_nomes = df_nomes.withColumn("Escolariedade", udf_escolariedade())
print("Imprimindo 10 itens do dataframe")
df_nomes.show(10)


# Etapa 4: adicionar uma coluna chamada "Pais" com os nomes dos 13 países da America do sul de forma aleatória para cada linha
print("--- Etapa 4 ---")
print("Adicionar uma coluna chamada 'Pais' da qual vai conter nome dos países da America do sul de forma aleatoria")
paises = ['Argentina','Bolívia','Brasil','Chile','Colômbia','Equador',
          'Guiana Francesa','Guiana','Paraguai','Peru','Suriname', 
          'Uruguai','Venezuela']
udf_paises = udf(lambda: get_random_indice_from_list(paises), StringType())
df_nomes = df_nomes.withColumn("Pais", udf_paises())
print("Imprimindo 10 itens do dataframe")
df_nomes.show(10)


# Etapa 5: adicionar uma coluna chamada "AnoNascimento" em que tenha idades de 1945 a 2010 de forma aleatoria a cada linha
print("--- Etapa 5 ---")
print("Adicionar uma coluna chamda 'AnoNascimento' que tenha os valores entre 1945 a 2010 aleatorios")
udf_AnoNascimento = udf(lambda: generate_random_int_in_range(1945, 2010), IntegerType())
df_nomes = df_nomes.withColumn("AnoNascimento", udf_AnoNascimento())
print("Imprimindo 10 itens do dataframe")
df_nomes.show(10)


# Etapa 6: filtrar em um novo dataframe o nome das pessoas que nasceram no seculo atual
print("--- Etapa 6 ---")
print("Filtrar em um novo dataframe o nome das pessoas que nasceram no seculo atual")
# Antes de aplicar a etapa 6, executar a função cache para corrigir filtros de dados
df_nomes = df_nomes.cache()
df_select = df_nomes.filter(col("AnoNascimento").cast("int") >= 2001).select("Nome", "AnoNascimento")
print("Imprimindo 10 itens do dataframe")
df_select.show(10)


# Etapa 7: Repetir o mesmo da etapa anterior, mas agora no SparkSQL
print("--- Etapa 7 ---")
print("Repetir o mesmo da etapa 6, mas utilizando o SparkSQL")
df_nomes.createOrReplaceTempView("Nomes")
df_select_sql = spark.sql(""" 
SELECT Nome, AnoNascimento
FROM Nomes
WHERE AnoNascimento >= 2001
""")
print("Imprimindo 10 itens do dataframe")
df_select_sql.show(10)


# Etapa 8: Contar a quantidade de pessoas que são milenares (nascidos entre 1980 a 1994)
print("--- Etapa 8 ---")
print("Contar a quantidade de pessoas que são milenares (nascidos entre 1980 a 1994)")
df_millenials = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994))
quantidade_milenares = df_millenials.count()
print(f"Quantidade de pessoas da geração milenar: {quantidade_milenares} ")


# Etapa 9: Realizar a mesma operação da etapa 8 mas em SparkSQL
print("--- Etapa 9 ---")
print("Realizar a mesma operação da etapa 8 mas em SparkSQL")
df_nomes.createOrReplaceTempView("Pessoas")
quantidade_milenares_sql = spark.sql(""" 
    SELECT COUNT(*) as quantidade_milenares
    FROM Pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""")
print("Imprimindo a quantidade de pessoas da geração milenar")
quantidade_milenares_sql.show()


# Etapa 10: Consultar a quantidade de pessoas de cada país para cada geração
print("--- Etapa 10 ---")
print("Consultar a quantidade de pessoas de cada país para cada geração")
df_nomes.createOrReplaceTempView("pessoas")
df_consulta = spark.sql("""
    SELECT 
        Pais,
        CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Milennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao, Quantidade
""")
print("Imprimindo dataframe da consulta")
df_consulta.show()