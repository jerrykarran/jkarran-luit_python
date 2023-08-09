import boto3

ec2 = boto3.client('ec2')

vpc = ec2.create_vpc(
    CidrBlock='11.0.0.0/16',
)

print(vpc["Vpc"]["VpcId"])