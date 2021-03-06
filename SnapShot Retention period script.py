""" ********************** IF YOU ARE USING THIS SCRIPT IN AWS LAMBDA FUNCTION USE THE BELOW SCRIPT ******** """
def lambda_handler(event, context):
    import datetime
    import time
    import boto3
    from datetime import date
    re = boto3.resource('ec2',aws_access_key_id='YOUR ACESS KEY ', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    c = boto3.client('ec2',aws_access_key_id='YOUR ACESS KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    snapid = c.describe_snapshots(OwnerIds = ['YOUR ACCOUNT ID'])
    L = len(snapid['Snapshots'])
    i = 0
    los = []
    while ( i < L ):
	    a=snapid['Snapshots'][i]['SnapshotId']
	    los.append(a)
	    i = i+1
    for list in los:
	    n = re.Snapshot(list)
	    times = str(n.start_time)
	    year = int(times[0:4])
	    month = int(times[5:7])
	    day = int(times[8:10])
	    ST = date( year , month , day )
	    localtime = time.localtime(time.time())
	    cyear = int( localtime.tm_year)
	    cmonth = int(localtime.tm_mon)
	    cday = int(localtime.tm_mday)
	    cdate = (cyear,cmonth,cday)
	    cdate = date(cyear,cmonth,cday)
	    diff = cdate - ST
	    DiffDays = diff.days
	    if ( DiffDays >= 1 ): Replace the number with your retention no of days  eg for 2 days [if ( DiffDays >= 2  )]
		    out = n.delete()
		    print (out)
""" ******************** END OF SCRIPT *********************************************** """ 

""" ********************** IF YOU ARE USING THIS SCRIPT IN WINDOWS OR LINUX SYSTEMS  USE THE BELOW SCRIPT ******** """

import datetime
import time
import boto3
from datetime import date
re = boto3.resource('ec2',aws_access_key_id='YOUR ACESS KEY ', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
c = boto3.client('ec2',aws_access_key_id='YOUR ACESS KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
snapid = c.describe_snapshots(OwnerIds = ['YOUR ACCOUNT ID'])
L = len(snapid['Snapshots'])
i = 0
los = []
while ( i < L ):
	a=snapid['Snapshots'][i]['SnapshotId']
  	los.append(a)
  	i = i+1
for list in los:
	n = re.Snapshot(list)
	times = str(n.start_time)
	year = int(times[0:4])
	month = int(times[5:7])
	day = int(times[8:10])
	ST = date( year , month , day )
	localtime = time.localtime(time.time())
	cyear = int( localtime.tm_year)
	cmonth = int(localtime.tm_mon)
	cday = int(localtime.tm_mday)
	cdate = date(cyear,cmonth,cday)
	diff = cdate - ST
	DiffDays = diff.days
	if ( DiffDays >= 1 ):
					#Replace the number with your retention no of days  eg for 2 days [if ( DiffDays >= 2  )]
		out = n.delete()
		
""" ******************** END OF SCRIPT *********************************************** """ 
