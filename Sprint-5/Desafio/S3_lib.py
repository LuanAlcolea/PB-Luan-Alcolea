# ---------- Modulo para manipular transferencias no AWS S3 ----------
import os
import boto3

def UploadFileIntoBucket(s3client, path, bucket, filename):
    s3client.upload_file(path, bucket, filename)


def DownloadFileFromBucket(s3client, path, bucket, filename):
    s3client.download_file(bucket, filename, path)


def CreateBucket(s3client, name):
    try:
        response = s3client.create_bucket(
            Bucket=name
            #CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
        )
        print(f"Bucket criado com sucesso! {name}")
    except Exception as e:
        print(f"Erro ao criar o bucket! {e}")
    

def CreateClient(key_id, secret_key_id, token):
    return boto3.client('s3',
                        aws_access_key_id=key_id, 
                        aws_secret_access_key=secret_key_id, 
                        aws_session_token=token,
                        region_name='us-east-1')


bucket_name = 'bucketsprint5luan'
csv_original = 'CAMINHO_CSV_ORIGINAL'
csv_processado = 'CAMINHO_CSV_PROCESSADO'
key_id = os.environ['AWS_ACCESS_KEY_ID']
secret_key_id = os.environ['AWS_SECRET_ACCESS_KEY']
token = os.environ['AWS_SESSION_TOKEN']
s3_client = None