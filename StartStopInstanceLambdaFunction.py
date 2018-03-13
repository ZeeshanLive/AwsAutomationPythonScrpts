import boto3

def lambda_handler(event, context):
    ec2=boto3.resource('ec2',region_name='us-east-1')
    InstanceId=['i-01986ccfac8edXXX'] # Mention instance Ids 
    for a in InstanceId:
        instance= ec2.Instance(a)
        print (instance.state)
        if instance.state['Name'] == 'stopped':
            instance.start()
        if instance.state['Name'] == 'running':
            instance.stop()
