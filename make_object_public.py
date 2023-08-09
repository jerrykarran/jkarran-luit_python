import boto3

s3 = boto3.client('s3')

bucket = "jkarran-wk14"
key = "test.txt"

response = s3.put_public_access_block(
    Bucket = bucket,
    
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)


response = s3.put_bucket_ownership_controls(
    Bucket = bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
)

response = s3.put_object_acl(
            ACL='private', 
            Bucket=bucket,
            Key=key
            )


print(response)













