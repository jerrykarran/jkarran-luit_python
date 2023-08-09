import boto3
import os
from list_objects import list_object_keys

def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)

if __name__ == '__main__':

    bucket = 'jkarran-wk14'
    key = 'test_text_string.txt'
    filename = 'test_text_string.txt'
    
    s3 = boto3.client('s3')
    
    keys = list_object_keys(s3, bucket, prefix="folder/")
    
    for key in keys:
        if '/' == key[-1]:  # if its a folder
            try:
                os.mkdir(key)   # make a directory with the name
            except:
                pass
        else:
            download_single_object(s3, bucket, key, key)