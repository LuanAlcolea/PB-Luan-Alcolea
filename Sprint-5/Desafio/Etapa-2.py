# ---------- Script do desafio parte 2 ----------
import polars as pl

import sys
import os
sys.path.append(os.path.abspath('C:/Users/Luan/Documents/Compass/Sprint-5/Desafio/'))
import S3_lib

csv_original = "C:/Users/Luan/Documents/Compass/Sprint-5/Desafio/Databases/Aeronaves-Drones-Cadastrados.csv"
csv_baixado = "C:/Users/Luan/Documents/Compass/Sprint-5/Desafio/Databases/Aeronaves-Drones-Cadastrados-Baixado.csv"
csv_processado = "C:/Users/Luan/Documents/Compass/Sprint-5/Desafio/Databases/Aeronaves-Drones-Cadastrados-Processado.csv"

def PrepararArquivo():
    S3_lib.DownloadFileFromBucket(S3_lib.s3_client, csv_original, S3_lib.bucket_name, 'Aeronaves-Drones-Cadastrados.csv')

    # Abrir database
    with open(csv_original, "r", encoding="utf-8") as file:
        arquivo = file.readlines()

    # Pre-processar o database
    with open(csv_processado, "w", encoding="utf-8") as file:
        for linha in arquivo:
            linha = linha.replace('; ', ' ')
            linha = linha.replace('"', '').replace('null', "Sem_dados").replace("Pulveriza��o", "Pulverização").replace("aplica��o", "aplicação").replace("Aeroagr�cola", "Aeroagricola")
            file.write(linha)
    
def ProcessarEtapas(current_dataframe):
    # ======== Etapa 1: filtrar dados usando ao menos dois operadores lógicos ========
    # Filtrar o peso máximo entre os intervalos 0.4 e 7.0, ou se o valor for 8.0
    dataframe = current_dataframe
    dataframe = dataframe.filter(
        (
            (pl.col("PESO_MAXIMO_DECOLAGEM_KG") > 0.4) & 
            (pl.col("PESO_MAXIMO_DECOLAGEM_KG") < 7.0) | 
            (pl.col("PESO_MAXIMO_DECOLAGEM_KG") == 8.0)
        )
    )

    # ======== Etapa 2: realizar dois calculos de agregações ========
    # Primeiro calculo: somar todos os pesos
    # Segundo calculo: extrair a media dos pesos
    aggregated = dataframe.group_by("TIPO_USO").agg([
    pl.col("PESO_MAXIMO_DECOLAGEM_KG").sum().round(2).alias("TOTAL_PESO"),
    pl.col("PESO_MAXIMO_DECOLAGEM_KG").mean().round(2).alias("MEDIA_PESO")
    ])
    dataframe = dataframe.join(aggregated, on="TIPO_USO", how="left")

    # ======== Etapa 3: Uma função Condicional ========
    print("========== Etapa 3 ==========")
    dataframe = dataframe.with_columns([
        pl.when(pl.col("CPF_CNPJ").cast(pl.Utf8).str.contains("CPF"))
        .then(pl.lit("Pessoa_fisica"))
        .otherwise(pl.lit("Empresa")).alias("PERFIL_CLIENTE")
    ])

    # ======== Etapa 4: Uma função de Conversão ========
    print("========== Etapa 4 ==========")
    dataframe = dataframe.with_columns([
        pl.col("DATA_VALIDADE").str.to_date().alias("DATA_VALIDADE")
    ])

    # ======== Etapa 5 Uma função de Data ========
    print("========== Etapa 5 ==========")
    dataframe = dataframe.with_columns([
        pl.when(pl.col("DATA_VALIDADE").dt.year() <= 2024)
        .then(pl.lit("Vencido"))
        .otherwise(pl.lit("Dentro_do_prazo")).alias("ESTA_VALIDO")
    ])

    # ======== Etapa 6: Uma função de String ========
    print("========== Etapa 6 ==========")
    dataframe = dataframe.with_columns([
        pl.col("MODELO")
        .str.replace_all(" ", "_")
        .alias("MODELO")
    ])

    return dataframe


# Configurar cliente AWS na maquina local
S3_lib.s3_client = S3_lib.CreateClient(S3_lib.key_id, S3_lib.secret_key_id, S3_lib.token)

# Preparar dataframe
PrepararArquivo()
pl.Config.set_tbl_cols(-1)
dataframe = pl.read_csv(csv_processado, separator=";", encoding="utf-8", skip_rows=1, null_values=["null"])

# Processar, salvar localmente e no S3 o dataframe
dataframe = ProcessarEtapas(dataframe)
dataframe.write_csv(csv_processado)
S3_lib.UploadFileIntoBucket(S3_lib.s3_client, S3_lib.csv_processado, S3_lib.bucket_name, 'Aeronaves-Drones-Cadastrados-Processado.csv')