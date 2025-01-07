import os
import boto3

bucketname = 'exercicio-lambda-pb-luan'
local_path = 'C:/Users/Luan/Documents/Compass/PB-Luan-Alcolea/Sprint-6/Exercícios/Exercício-AWS-Lambda/'
local_file = 'minha-camada-pandas.zip'
    
key_id = os.environ['AWS_ACCESS_KEY_ID']
secret_key_id = os.environ['AWS_SECRET_ACCESS_KEY']
token = os.environ['AWS_SESSION_TOKEN']

s3_client = boto3.client('s3',
                        aws_access_key_id=key_id, 
                        aws_secret_access_key=secret_key_id, 
                        aws_session_token=token,
                        region_name='us-east-1')


s3_client.upload_file(f'{local_path}{local_file}', bucketname, 'dados/minha-camada-pandas.zip')