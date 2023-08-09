import boto3

s3 = boto3.client('s3')

import logging
import boto3
from botocore.exceptions import ClientError


# def create_presigned_url(bucket_name, object_name, expiration=3600):

bucket_name = "jkarran-boto3-080623-1756"
object_name = "test_text2.txt"

response = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=300)
                                                    
print(response)