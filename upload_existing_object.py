import boto3
import os

s3 = boto3.client('s3')


with open("test_text.txt", 'rb') as f:
    s3.put_object(Bucket="jkarran-boto3-080623-1756", Key="test_text2.txt", Body=f, ContentType="text/plain")