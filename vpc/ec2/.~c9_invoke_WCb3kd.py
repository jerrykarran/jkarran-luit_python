import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_images()


#     Filters=[
#         {
#             'Name': 'free-tier-eligible',
#             'Values':[
#                 'true',
#             ]
            
            
#         },
        
        
#     ]
# )
print(reponse)

# for instanceType in response["InstanceTypes"]:
#     print(instanceType["InstanceType"], instanceType["FreeTierEligible"])