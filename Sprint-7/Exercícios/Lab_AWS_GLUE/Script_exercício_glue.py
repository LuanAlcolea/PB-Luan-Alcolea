from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, count, upper

spark = SparkSession.builder \
    .appName("Ler CSV") \
    .getOrCreate()

caminho_csv = "nomes.csv"

df = spark.read.csv(caminho_csv, header=True, inferSchema=True)

# Nomes minusculos para maisculos
df_upper = df.withColumn("nome", upper(df["nome"]))
print("1) Valores nomes convertidos para letras maiúsculas")

# Mostrar linhas presentes no dataframe
df_linhas = df_upper.count()
print(f"2) Quantidade de linhas contidas no dataframe: {df_linhas}")

# Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
df_grouped = df_upper.groupBy("ano", "sexo").agg(count("nome").alias("contagem_nomes"))
print("3) Contagem de nomes agrupados pelas colunas ano e sexo!")

# Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.
df_ordered = df_grouped.orderBy("ano", ascending=False)
print("4) Dados ordenados para que o ano mais recente apareça como o primeiro registro do dataframe")

# Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.
df_feminino_mais_registrado = df_upper.filter(col("sexo") == "F") \
    .groupBy("nome", "ano") \
    .agg(count("*").alias("total_registros")) \
    .orderBy(desc("total_registros")) \
    .first()
print(f"5) Nome: {df_feminino_mais_registrado['nome']}, Ano: {df_feminino_mais_registrado['ano']}, Total de Registros: {df_feminino_mais_registrado['total_registros']}")

# Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.
df_masculino_mais_registrado = df_upper.filter(col("sexo") == "M") \
    .groupBy("nome", "ano") \
    .agg(count("*").alias("total_registros")) \
    .orderBy(desc("total_registros")) \
    .first()
print(f"6) Nome: {df_masculino_mais_registrado['nome']}, Ano: {df_masculino_mais_registrado['ano']}, Total de Registros: {df_masculino_mais_registrado['total_registros']}")

# Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe. Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente.
df_total_registros_por_ano = df_upper.groupBy("ano") \
    .agg(count("*").alias("total_registros")) \
    .orderBy("ano") \
    .limit(10)
print("7) Total de registros por ano (primeiras 10 linhas):")
df_total_registros_por_ano.show()

print("Imprimindo dataframe final")
df_ordered.show()
df_ordered.printSchema()

spark.stop()
