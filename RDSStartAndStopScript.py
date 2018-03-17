
import boto3
rdsobj = boto3.client('rds')
DBId = ['mydbinstance'] #replace with the name of your DB instance Identifier, 
i=0
while i < len(DBId):
	DbObj = rdsobj.describe_db_instances(DBInstanceIdentifier=DBId[i])
	StatusOfDb = DbObj['DBInstances'][i]['DBInstanceStatus']
	if StatusOfDb == 'available':
		se = rdsobj.stop_db_instance(DBInstanceIdentifier=DBId[i])
	else:
		se = rdsobj.start_db_instance(DBInstanceIdentifier=DBId[i])
	i = i+1
