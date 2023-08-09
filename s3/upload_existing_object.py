import boto3
import os

s3 = boto3.client('s3')

with open("test_text.txt", 'rb') as f:
    s3.put_object(Bucket="jkarran-wk14, Key="test_text.txt", Body=f, ContentType="text/plain")