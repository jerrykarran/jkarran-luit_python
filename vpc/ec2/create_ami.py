import boto3

ec2 = boto3.client('ec2')
instanceId = "i-07f670ec7620f49d5"
instanceName = "New Ami From Boto3"

response = ec2.create_image(InstanceId=instanceId, Name=instanceName)

