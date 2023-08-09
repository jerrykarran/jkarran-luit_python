import boto3

# cidr_block = "11.0.1.0/24"
vpc_id = "vpc-00035e1a0307bcbb6"

ec2 = boto3.client('ec2')

route_table = ec2.create_route_table(VpcId=vpc_id)

print(route_table["RouteTable"]["RouteTableId"])