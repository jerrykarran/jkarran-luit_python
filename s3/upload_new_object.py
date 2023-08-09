import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="jkarran-wk14", 
                Key="folder/foldera/test_text_string.txt", 
                Body="Hey, this is a string 080823", 
                ContentType="text/plain")