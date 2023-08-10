import boto3

ec2 = boto3.client('ec2')

def stop_instance(client, instance_id):
    response = ec2.stop_instances(InstanceIds=[instance_id])   # stop the running instances
    print(instance_id, "stopped")

def start_instance(client, instance_id):
    response = ec2.start_instances(InstanceIds=[instance_id])   # stop the running instances
    print(instance_id, "started")

def terminate_instance(client, instance_id):
    response = ec2.terminate_instances(InstanceIds=[instance_id])   # stop the running instances
    print(instance_id, "terminated")
    
if __name__ == '__main__':
    instance_id = "i-057c441cbeb37c682"
    
    ec2 = boto3.client('ec2')
    terminate_instance(ec2, instance_id)

