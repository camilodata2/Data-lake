import os
import boto3
import redshift_connector

client = boto3.client('s3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
)
conn = redshift_connector.connect( 
    iam=True,
    host= os.environ.get('REDSHIFT_HOST'),
    database=os.environ.get('REDSHIFT_DATABASE'),
    port=5439,
    user=os.environ.get('REDSHIFT_USER'),
    password=os.environ.get('REDSHIFT_PASSWORD')
)
cursor = conn.cursor()

