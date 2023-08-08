import boto3

def filter_objects_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if(extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])
            
    return keys
    
def list_object_keys(client, bucket, prefix=""):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response['Contents']:
        keys.append(content["Key"])
            
    return keys

s3 = boto3.client('s3')

extension = ".jpg"
bucket = "jkbucketdevops"

response = list_object_keys(s3, bucket, "department/")
print(response)