""" ******** FOR AWS LAMBDA *************** """
def lambda_handler(event, context):
    import boto3
    import datetime
    import time
    from datetime import date
    dbsnap = boto3.client('rds')
    DbSnapList = dbsnap.describe_db_snapshots()
    LengthOfSnaps = len(DbSnapList['DBSnapshots'])
    DbId =[]
    i = 0 
    while ( i < LengthOfSnaps):
        if (DbSnapList['DBSnapshots'][i]['SnapshotType'] == 'manual') and (DbSnapList['DBSnapshots'][i]['DBInstanceIdentifier'] == 'mydb2'):   # IF you are going for automated Snapshots replace "manual" to "automated and 'mydb2' to your dbidentifier i.e dbname"
            SID = DbSnapList['DBSnapshots'][i]['DBSnapshotIdentifier']
            DbId.append(SID)
            a = DbSnapList['DBSnapshots'][i]['InstanceCreateTime']
            DbSCT = date(a.year,a.month,a.day)
            HostDateIn = time.localtime(time.time())
            HostDate=date(HostDateIn.tm_year,HostDateIn.tm_mon,HostDateIn.tm_mday)
            diff = HostDate - DbSCT
            DiffDays = diff.days
            print(DiffDays)
            if (DiffDays == 0 ):                                                # REPLACE "0" WiTH NO OF DAYS YOU WANT YOUR SNAPSHOT TO BE DELETED
              re = dbsnap.delete_db_snapshot(DBSnapshotIdentifier=SID)        
        i = i + 1
 
""" ******* FOR WINDOWS / LINUX other work stations ************ """

import boto3
import datetime
import time
from datetime import date
dbsnap = boto3.client('rds',aws_access_key_id='YOURACCESSKEY', aws_secret_access_key='SECRETKEY',region_name='REGIONNAME')
DbSnapList = dbsnap.describe_db_snapshots()
LengthOfSnaps = len(DbSnapList['DBSnapshots'])
DbId =[]
i = 0 
while ( i < LengthOfSnaps):
	if (DbSnapList['DBSnapshots'][i]['SnapshotType'] == 'manual') and (DbSnapList['DBSnapshots'][i]['DBInstanceIdentifier'] == 'mydb2'):   # IF you are going for automated Snapshots replace "manual" to "automated and 'mydb2' to your dbidentifier i.e dbname"
		SID = DbSnapList['DBSnapshots'][i]['DBSnapshotIdentifier']
		DbId.append(SID)
		a = DbSnapList['DBSnapshots'][i]['InstanceCreateTime']
		DbSCT = date(a.year,a.month,a.day)
		HostDateIn = time.localtime(time.time())
		HostDate=date(HostDateIn.tm_year,HostDateIn.tm_mon,HostDateIn.tm_mday)
		diff = HostDate - DbSCT
		DiffDays = diff.days
		if (DiffDays == 0 ):                                    # REPLACE "0" WiTH NO OF DAYS YOU WANT YOUR SNAPSHOT TO BE DELETED
			re = dbsnap.delete_db_snapshot(DBSnapshotIdentifier=SID)
	i = i + 1
