import boto3

ec2 = boto3.client('ec2')
vpcid = "vpc-039cd55b92a89defc"

ec2.delete_vpc(
    VpcId=vpcid
)