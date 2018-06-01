currentregions=['ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-west-1', 'ap-northeast-2', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1','us-west-1', 'us-west-2']

for b in currentregions:
    client = boto3.client('ec2',region_name=b)
    w= client.describe_key_pairs()
    i = 0
    while i < len(w['KeyPairs']):
        l = w['KeyPairs'][i]['KeyName']
        print (l)
        ec2 = boto3.resource('ec2')
        key_pair = ec2.KeyPair(l)
        key_pair.delete()
        i =i+1
