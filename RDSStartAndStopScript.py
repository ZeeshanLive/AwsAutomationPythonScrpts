
import boto3
rdsobj = boto3.client('rds')
DBId = ['mydbinstance'] #replace with the name of your DB instance Identifier, 
for a in DBId:
	DbObj = rdsobj.describe_db_instances(DBInstanceIdentifier=a)
	StatusOfDb = DbObj['DBInstances'][0]['DBInstanceStatus']
	if StatusOfDb == 'available':
		se = rdsobj.stop_db_instance(DBInstanceIdentifier=a)
	else:
		se = rdsobj.start_db_instance(DBInstanceIdentifier=a)
	i = i+1
