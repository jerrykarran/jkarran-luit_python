# from datetime import datetime
from datetime import datetime
from datetime import timedelta


def schedule_stop_intances()
est_time = (datetime.now() - timedelta(hours=4)).time()

if est_time !=  "00:53:00":
    est_time = (datetime.now() - timedelta(hours=4)).time()
# import pytz
# from pytz import timezone

# timestamp = '05:22:00'
# current_time = datetime.strptime(timestamp,'%H:%M:%S').astimezone(pytz.timezone('US/Eastern')).strftime("%H:%M:%S")
# print(current_time)
# datetime object containing current date and time to create a schedule


# now = int(datetime.now()) - int("4:00:00")
# print(now)

# if now !=  "04:21:00":
#     print(now.strftime("%H:%M:%S"))
#     now = datetime.now()
# dd/mm/YY H:M:S

import boto3

def stop_instances(client):
    response = client.describe_instance_status()  

    instancesToStop = []
    running_dev_instances = []
    for instance in response["InstanceStatuses"]:                       # check all instances
        if "InstanceState" in instance:                                 # if an instance exists
            if instance["InstanceState"]["Name"] == "running":          # check if its running
                if instance["InstanceId"] != "i-0ed1cf0b0e3fdb30d":     # do not include the cloud9 instance to stop
                    instancesToStop.append(instance["InstanceId"])      # if it's running, add to the list to stop

    if instancesToStop != []:  
        dev_instances = client.describe_tags() # delete this
        print( dev_instances)
        # dev_instances = client.describe_tags(Filters=[                  # check for running dev instances
        #         {'Name': 'key', 'Values': ['Environment',]},
        #         {'Name': 'value', 'Values': ['Dev',]}
        #     ,],)
       
        for instance in dev_instances["Tags"]:                                          # if there are running dev instances
            running_dev_instances.append(instance["ResourceId"])                        # add to list of running dev instances
        # stop_dev_instances = client.stop_instances(InstanceIds=running_dev_instances)   # stop the running dev instances
                    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    stop_instances(ec2)