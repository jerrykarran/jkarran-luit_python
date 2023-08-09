import boto3
ec2 = boto3.client('ec2')

response = ec2.describe_instance_status()                           # get all instances
instancesToStop = []                                                #create a list to hold instances to stop

for instance in response["InstanceStatuses"]:                       # check all instances
    if "InstanceState" in instance:                                 # if an instance exists
        if instance["InstanceState"]["Name"] == "running":          # check if its running
            if  instance["InstanceId"] != "i-0ed1cf0b0e3fdb30d":    # keep testgin instance running for testing
                instancesToStop.append(instance["InstanceId"])      # if it's running, add to the list to stop
                
response = ec2.stop_instances(InstanceIds=instancesToStop)          # stop the running instances