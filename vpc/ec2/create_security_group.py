import boto3
import os

ec2 = boto3.client('ec2')

vpcId = "vpc-06279afac18507d28"
description = "created security group from boto3"
sgGroupName = "boto3 SG Group Name"

response = ec2.create_security_group(
    Description='My security group',
    GroupName=description,
    VpcId=vpcId,
)

print(response)
