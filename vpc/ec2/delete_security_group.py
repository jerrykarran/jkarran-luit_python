import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-0cdf8b0b74f08a97d',
)