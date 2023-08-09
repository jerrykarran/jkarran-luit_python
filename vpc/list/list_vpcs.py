import boto3

def get_vpc_information(client, filter=[]):
    response = client.describe_vpcs(Filters=filter)
    print("You have the following VPCs:\n")
    for vpc in response["Vpcs"]:
        print("vpc id: " + str(vpc["VpcId"]) + "\nvpc cidrblock; " + str(vpc["CidrBlock"]) + 
                "\nDefault? " + str(vpc["IsDefault"]) + "\n")

def get_default_vpc_name(client):
    response = client.describe_vpcs()
    for vpc in response["Vpcs"]:
        if "Tags" in vpc:
            for tag in vpc["Tags"]:
                if "Name" == tag["Key"]:
                    print (tag["Value"])
                    
if __name__ == '__main__':
    Filters=[{'Name': 'isDefault','Values': ['true']},]
    ec2 = boto3.client('ec2')

            
    # get_vpc_information(ec2, Filters)
    # get_vpc_information(ec2)
    # get_default_vpc_name(ec2)