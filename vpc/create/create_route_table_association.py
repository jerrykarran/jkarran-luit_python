import boto3

route_table_id = "rtb-0bb00c51c3a327358"
subnet_id = "subnet-0c3e5fab3ced8522c"

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)

print(association["AssociationId"])