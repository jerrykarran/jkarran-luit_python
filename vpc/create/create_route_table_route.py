import boto3

internet_gateway_id = "igw-0ef5b48a5f465e7c3"
route_table_id = "rtb-0bb00c51c3a327358"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id
)