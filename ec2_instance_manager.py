import boto3

ec2 = boto3.client('ec2')


class EC2InstanceManager:

    def __init__(self, stack):
        self.stack = stack

    def get_instances(self):
        response = ec2.describe_instances(Filters=[
            {
                'Name': 'tag:opsworks:stack',
                'Values': [self.stack]
            }
        ])
        for r in response['Reservations']:
            instance_names = []
            instance_ids = []
            for i in r['Instances']:
                for t in i['Tags']:
                    if t['Key'] == 'Name':
                        instance_names.append(t['Value'])
                        instance_ids.append(i['InstanceId'])

        return instance_ids, instance_names

a = EC2InstanceManager("Demo 3")
c, d = a.get_instances()

print(c)
print(d)