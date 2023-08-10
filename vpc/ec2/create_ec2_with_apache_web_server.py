import boto3
ec2 = boto3.client('ec2')

ami = "ami-0a845b3963701c7aa"
securityGroupIds = ["sg-0cdf8b0b74f08a97d"]
keypair_name = "Key from boto3"
user_data = ''''#!/bin/bash
        apt update -y
        apt-get install -y apache2
        systemctl start apache2
        systemctl enable apache2'''

def create_instance(client, ami, security_group_id, keypair_name, user_data=None):
    instanceType = 't2.micro'
    maxCount=1
    minCount=1
    
    response = client.run_instances(
        ImageId=ami,
        SecurityGroupIds=security_group_id,
        KeyName=keypair_name,
        
        InstanceType=instanceType,
        MaxCount=maxCount,
        MinCount=minCount,
        UserData = user_data,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': '2nd boto3 with apache',
                    },
                ],
            },
        ],
    )

create_instance(ec2, ami, securityGroupIds, keypair_name, user_data)


# print(response["Instances"][0]["InstanceId"])