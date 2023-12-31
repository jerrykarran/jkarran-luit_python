import boto3

def stop_instances(client):
    response = client.describe_instance_status()                           # get all instances
    instancesToStop = []                                                #create a list to hold instances to stop
    
    for instance in response["InstanceStatuses"]:                       # check all instances
        if "InstanceState" in instance:                                 # if an instance exists
            if instance["InstanceState"]["Name"] == "running":          # check if its running
                if instance["InstanceId"] != "i-0ed1cf0b0e3fdb30d":    # keep testgin instance running for testing
                    instancesToStop.append(instance["InstanceId"])      # if it's running, add to the list to stop
                    
    if instancesToStop != []:                                           # prevents error if there are no running instances
        response = client.stop_instances(InstanceIds=instancesToStop)   # stop the running instances
        
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    stop_instances(ec2)