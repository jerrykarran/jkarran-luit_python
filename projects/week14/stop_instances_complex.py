import boto3
from datetime import datetime

def stop_instances(client):
    
    
    now = datetime.now()        # Get current date and time
    
    while (now.hour-4 < 19):
        now = datetime.now()
        
    response = client.describe_instance_status()                                        # run fuction at scheduled time

    instancesToStop = []
    running_dev_instances = []
    for instance in response["InstanceStatuses"]:                                       # check all instances
        if "InstanceState" in instance:                                                 # if an instance exists
            if instance["InstanceState"]["Name"] == "running":                          # check if its running
                if instance["InstanceId"] != "i-0ed1cf0b0e3fdb30d":                     # do not include the cloud9 instance to stop
                    instancesToStop.append(instance["InstanceId"])                      # if it's running, add to the list to stop

    if instancesToStop != []:  
        dev_instances = client.describe_tags(Filters=[                                  # check for running dev instances
                {'Name': 'key', 'Values': ['Environment',]},
                {'Name': 'value', 'Values': ['Dev',]}
            ,],)
       
        for instance in dev_instances["Tags"]:                                          # if there are running dev instances
            running_dev_instances.append(instance["ResourceId"])                        # add to list of running dev instances
        stop_dev_instances = client.stop_instances(InstanceIds=running_dev_instances)   # stop the running dev instances
                    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    stop_instances(ec2)