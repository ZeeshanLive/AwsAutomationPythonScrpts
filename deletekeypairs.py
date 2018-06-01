i = 0
currentregions=[]
while i < len(response['Regions']):
    currentregions.append(response['Regions'][i]['RegionName'])
    i=i+1

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
