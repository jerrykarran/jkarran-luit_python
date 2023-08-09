import boto3

s3 = boto3.client('s3')

s3.upload_file('test_text.txt', 'jkarran-boto3-080623-1756', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})
