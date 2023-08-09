import boto3

internet_gateway_id = "igw-0ef5b48a5f465e7c3"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id
)