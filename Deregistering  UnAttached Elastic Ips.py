import boto3
import datetime
import time
import pandas as pd
import numpy as np
from datetime import date
import pandas as pd
import os
client = boto3.client('ec2')


currentregions=['ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-west-1', 'ap-northeast-2', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1','us-west-1', 'us-west-2']
csvdata=[]
todaydate=str(datetime.date.today())
for a in currentregions:
	client = boto3.client('ec2',region_name =a)
    response = client.describe_addresses()
	i = 0
	while i < len(response['Addresses']):
		if "NetworkInterfaceId" not in response['Addresses'][i]:
			print (response['Addresses'][i])
			publicIp = response['Addresses'][i]['PublicIp']
			AllocationId = response['Addresses'][i]['AllocationId']
			Region = a
			FinalData = [publicIp,AllocationId,Region]
			csvdata.append(FinalData)
			p = client.release_address( AllocationId = AllocationId)
		i += 1

df = pd.DataFrame(csvdata, columns=[ "PublicIp | (ElasticIp)","AllocationId" ,"Region"])
csvname = "List of Released  Elastic Ips  " + "-" + todaydate +".csv"
df.to_csv(csvname)
print ("your file is save in ", os.getcwd()+csvname)
	
	
	
