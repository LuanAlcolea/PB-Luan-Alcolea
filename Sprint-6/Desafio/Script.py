# Script para carregar os arquivos CSV para dentro do S3 na zona RAW
import os
import boto3
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Funções

def ConfigureClient(key_id, secret_key_id, token):
    return boto3.client('s3',
                        aws_access_key_id=key_id, 
                        aws_secret_access_key=secret_key_id, 
                        aws_session_token=token,
                        region_name='us-east-1')


def CreateBucket(s3_client, bucketname):
    try:
        s3_client.create_bucket(
            Bucket=bucketname
        )
        print(f"Bucket criado com sucesso! {bucketname}")
    except Exception as e:
        print(f"Erro ao criar o bucket! {e}")


def UploadFileToS3(s3_client, bucketname, local_path, local_file, s3_path, s3_file):
    try:
        s3_client.upload_file(f'{local_path}{local_file}', bucketname, f'{s3_path}{s3_file}')
        print(f'Sucesso ao carregar arquivo no bucket. {bucketname}')
    except Exception as e:
        print(f'Erro ao carregar arquivo no bucket. {e}')


# Variáveis

year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d')

bucket_name = 'data-lake-luan'
local_file_path = '/app/data/'
file_name_movie = 'movies.csv'
file_name_series = 'series.csv'
s3_path_movie = f'Raw/Local/CSV/Movies/{year}/{month}/{day}/'
s3_path_series = f'Raw/Local/CSV/Series/{year}/{month}/{day}/'

# Execução

# Configure s3 client
s3_client = ConfigureClient(os.environ['AWS_ACCESS_KEY_ID'], os.environ['AWS_SECRET_ACCESS_KEY'], os.environ['AWS_SESSION_TOKEN'])
# Create bucket
CreateBucket(s3_client, bucket_name)
# Upload movies
UploadFileToS3(s3_client, bucket_name, local_file_path, file_name_movie, s3_path_movie, file_name_movie)
# Upload series
UploadFileToS3(s3_client, bucket_name, local_file_path, file_name_series, s3_path_series, file_name_series)

