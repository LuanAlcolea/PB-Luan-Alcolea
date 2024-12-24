# ---------- Script do desafio parte 1 ----------
import boto3

import sys
import os
sys.path.append(os.path.abspath('C:/Users/Luan/Documents/Compass/Sprint-5/Desafio/'))
import S3_lib

# Configurar cliente AWS na maquina local
S3_lib.s3_client = S3_lib.CreateClient(S3_lib.key_id, S3_lib.secret_key_id, S3_lib.token)
# Criar o bucket
S3_lib.CreateBucket(S3_lib.s3_client, 'bucketsprint5luan')
# Carregar objeto para o bucket
S3_lib.UploadFileIntoBucket(S3_lib.s3_client, S3_lib.csv_original, S3_lib.bucket_name, 'Aeronaves-Drones-Cadastrados.csv')
