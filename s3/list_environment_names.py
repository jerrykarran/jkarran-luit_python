import boto3

cloud9 = boto3.client('cloud9')

response = cloud9.list_environments()

print(response)

# response = client.list_environments( # original
#     nextToken='string',
#     maxResults=123
# )