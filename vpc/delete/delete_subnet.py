import boto3

subnet_id = "subnet-0c3e5fab3ced8522c"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id
)