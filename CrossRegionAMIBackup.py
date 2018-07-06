import boto3
import datetime
from datetime import datetime as dt
geTAmi = boto3.client('ec2')
inSTre = boto3.resource('ec2')
InstanceName = geTAmi.describe_instances(Filters = [{'Name':'tag:AMITransfer','Values':['True']}])

i = 0
while i < len(InstanceName['Reservations']):
	idNt = InstanceName['Reservations'][i]['Instances'][0]['InstanceId']
	#print (idNt)
	instance = inSTre.Instance(idNt)
	#print (instance.tags)
	j = 0
	while j < len(instance.tags):
		q = instance.tags[j]
		if q['Key']=='Name':
			AmiName= q['Value']
			q = dt.now()
        	if (len(str(q.month)) == 1) and (len(str(q.day)) == 1):
        		aminamefilter = AmiName+"_"+str(q.year)+"-"+"0"+str(q.month)+"-"+"0"+str(q.day)+"_*"
            	print (aminamefilter)
        	elif (len(str(q.month)) == 2) and (len(str(q.day)) == 1):
        		aminamefilter = AmiName+"_"+str(q.year)+"-"+str(q.month)+"-"+"0"+str(q.day)+"_*"
        	elif (len(str(q.month)) == 1) and (len(str(q.day)) == 2):
            	aminamefilter = AmiName+"_"+str(q.year)+"-"+"0"+str(q.month)+"-"+str(q.day)+"_*"
        	elif (len(str(q.month)) == 2) and (len(str(q.day)) == 2):
            	aminamefilter = AmiName+"_"+str(q.year)+"-"+str(q.month)+"-"+str(q.day)+"_*"
            
        	else:
            	print ("jingalala")
            AmIList = geTAmi.describe_images(Filters=[{'Name':'name','Values':[aminamefilter]}])
            amifiltername = aminamefilter[0:len(aminamefilter)-2]
            print (AmIList['Images'][0]['ImageId'])
            #bck = boto3.client('ec2',region_name = "ap-southeast-1")
            #CopyImage = bck.copy_image(Description="CrossRegionImageBackup",Name=amifiltername,SourceImageId = AmIList['Images'][0]['ImageId'] , SourceRegion = "ap-south-1")

		j = j+1
	i = i +1
