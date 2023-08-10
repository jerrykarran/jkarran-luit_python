import boto3

ec2 = boto3.client('ec2')

imageid = "ami-0a845b3963701c7aa"
instanceType = 't2.micro'
keyname = "Key from boto3"
securityGroupIds = ["sg-0cdf8b0b74f08a97d"]
maxCount=1
minCount=1

response = ec2.run_instances(
    ImageId=imageid,
    InstanceType=instanceType,
    KeyName=keyname,
    MaxCount=maxCount,
    MinCount=minCount,
    SecurityGroupIds=securityGroupIds,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'new boto3 test',
                },
            ],
        },
    ],
)

print(response["Instances"][0]["InstanceId"])