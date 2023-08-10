import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for sg in response["SecurityGroups"]:
    print(sg["GroupId"], sg["VpcId"], sg["GroupName"], sg["Description"] )
    
    for permissions in sg["IpPermissions"]:
        if "FromPort" in permissions:
            print(permissions["FromPort"])
            
        if "IpProtocol" in permissions:
            print(permissions["IpProtocol"])
            
        if "ToPort" in permissions:
            print(permissions["ToPort"])
            
        if "IpRanges" in permissions:
             for iprange in permissions["IpRanges"]:
                 print(iprange["CidrIp"])