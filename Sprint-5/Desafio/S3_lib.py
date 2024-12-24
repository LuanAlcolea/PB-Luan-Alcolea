# ---------- Modulo para manipular transferencias no AWS S3 ----------
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
csv_original = 'C:/Users/Luan/Documents/Compass/Sprint-5/Desafio/Databases/Aeronaves-Drones-Cadastrados.csv'
csv_processado = 'C:/Users/Luan/Documents/Compass/Sprint-5/Desafio/Databases/Aeronaves-Drones-Cadastrados-Processado.csv'
key_id = 'ASIA5CBDQ7EDOND2C2LZ'
secret_key_id = 't4x0ij6wvuqeruehST9J3t9DM0R9YPSj2HjPsIhh'
token = 'IQoJb3JpZ2luX2VjEAAaCXVzLWVhc3QtMSJIMEYCIQCSQkd4qspXr/sX8Q+9iXgEWSfXVNY2jQVNJM0tUDc9UwIhAJQlR4I53sctGASH4hOuKUbeB5KZ+UznVfxgt3zQnZNFKqYDCMj//////////wEQABoMODk3NzIyNjc3NTEwIgwU/k2SZh8RTOgKI7Yq+gI4ra8z1B/GdxcS1iUe4XjfdTyaBUG0qJZpeturE9jshZ5gSt5r9RY5rOkykK+NM7SbqeGhugMk+EO3Nmb7wfJCxc8b6muEfQOGhmHjVnE+6d4IWh4H6IR2vOmmgjDHkFBGwFECJMwXMI8/UEWlCEnOjVmWAB7YPrA9YI2bT032ptwumaymYd2AydXF5w8FAZMrsrt0OwMSahLiLYjj5ix3NP+4IfRw+I/nQhZAUDWLBgHZHUmuHdnbEeEWKYejfQkASTbYyq97B28EEkvnixQpOcB5sbZKOz9BZWPf4LZgtpjiVQb6J6BWZaSjVUpMLKW7szGN4EiINAasgWQH9ar30bbsVGSrEpTUr92PVgiL+DherxcP7jh5thHReXIcdGnlCJiL7RSuGaVAShSele+4dQMDY+8Tq7xOQfjEJy3wAu3pRA3CDKEhJplXrQmnxOhlwFpx03d3PAde160vo4/o8MnU1HCKlkbghHTWIyzqGXhFhBV15wSQLXcw27uiuwY6pQHhJXD+M3j0dQjGdrYdRVJAZ3T7Oz/ebEB5/B54FFMo+83amENn2Uc6ctyAOWANtMepEHHwAEl9eX9xPqjr5ZHi8Z44zK9cH7pcerZnRxB3e4Jv71gArBrjIu0SBe956HuHjK4rWhaM1cAaQViyUCXZHFY6KVpTT2KkeeLVLOsYaI4YFD0waq21JXp5fCWaC/DKhaFoik6VPS7fYdSDMC1EOmTS70g='
s3_client = None