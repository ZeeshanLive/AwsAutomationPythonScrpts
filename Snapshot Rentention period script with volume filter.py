""" ********************** IF YOU ARE USING THIS SCRIPT IN AWS LAMBDA FUNCTION USE THE BELOW SCRIPT ******** """
def lambda_handler(event, context):
    import datetime
    import time
    import boto3
    from datetime import date
    def CurrentDate():
      localtime = time.localtime(time.time())
      cyear = int( localtime.tm_year)
      cmonth = int(localtime.tm_mon)
      cday = int(localtime.tm_mday)
      cdate = date(cyear,cmonth,cday)
      return cdate
    re = boto3.resource('ec2',aws_access_key_id='YOUR ACCESS KEY', aws_secret_access_key='YOUR SECRETKEY',region_name='REGION NAME')
    c = boto3.client('ec2',aws_access_key_id='YOUR ACCESS KEY', aws_secret_access_key='YOUR SECRETKEY',region_name='REGION NAME')
    snapid = c.describe_snapshots(Filters = [{'Name':'volume-id','Values': ['YOUR VOLUME ID ']},],) #you can specify multiple volumes by giving " , " 
    #NOTE : You can use different filters to filter your Images , AVAILABLE Filters options are provided end of this script 
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
        diff = (CurrentDate()-ST)
        DiffDays = diff.days
        if (DiffDays == 2):  #mention the number of days old snapshot you want to delete 
            out = n.delete()
 """" ******************** END OF SCRIPT *********************************************** """             
          
          
 #NOTE : SnapShots must not be in used while running this script 
 
 """ ********************** IF YOU ARE USING THIS SCRIPT IN WINDOWS OR LINUX SYSTEMS  USE THE BELOW SCRIPT ******** """
import datetime
import time
import boto3
from datetime import date
def CurrentDate():
    localtime = time.localtime(time.time())
    cyear = int( localtime.tm_year)
    cmonth = int(localtime.tm_mon)
    day = int(localtime.tm_mday)
    cdate = date(cyear,cmonth,cday)
    return cdate
re = boto3.resource('ec2',aws_access_key_id='YOUR ACCESS KEY', aws_secret_access_key='YOUR SECRETKEY',region_name='REGION NAME')
c = boto3.client('ec2',aws_access_key_id='YOUR ACCESS KEY', aws_secret_access_key='YOUR SECRETKEY',region_name='REGION NAME')
snapid = c.describe_snapshots(Filters = [{'Name':'volume-id','Values': ['YOUR VOLUME ID ']},],) #you can specify multiple volumes by giving " , " 
#NOTE : You can use different filters to filter your Images , AVAILABLE Filters options are provided end of this script 
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
    diff = (CurrentDate()-ST)
    DiffDays = diff.days
    if (DiffDays == 2):				#mention the number of days old snapshot you want to delete 
        out = n.delete()
 
  """" ******************** END OF SCRIPT *********************************************** """  
	
""" AVAILABLE FILTER TO FIter your snapshots 

description - A description of the snapshot.
owner-alias - Value from an Amazon-maintained list (amazon | aws-marketplace | microsoft ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console.
owner-id - The ID of the AWS account that owns the snapshot.
progress - The progress of the snapshot, as a percentage (for example, 80%).
snapshot-id - The snapshot ID.
start-time - The time stamp when the snapshot was initiated.
status - The status of the snapshot (pending | completed | error ).
tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter "tag-key=Purpose" and the filter "tag-value=X", you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
volume-id - The ID of the volume the snapshot is for.
volume-size - The size of the volume, in GiB.


"""
