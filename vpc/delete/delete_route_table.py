import boto3

route_table_id ="rtb-0bb00c51c3a327358"

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id
)