import boto3
import os

ec2 = boto3.client('ec2')

key_name = "boto3keypair522"
filename = "keypairFromBoto522"

response = ec2.create_key_pair(KeyName=key_name)

with open(filename, 'w') as f:  # w means write, f means file
    f.write(response["KeyMaterial"])
    
os.chmod(filename, 0o400)