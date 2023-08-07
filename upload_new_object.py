import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="jkarran-boto3-080623-1756", Key="test_text_string.txt", Body="This is a string", ContentType="text/plain")