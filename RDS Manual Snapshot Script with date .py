""" ************* FOR AWS LAMBDA FUNCTION USE BELOW SCRIPT *************** """ 

def lambda_handler(event, context):
    import boto3
    import datetime
    import time
    dbsnap = boto3.client('rds',aws_access_key_id='YOUR ACESS KEY ', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    from datetime import date
    def snapname():
        localtime = time.localtime(time.time())
        yr = str(localtime.tm_year)
        mo = str(localtime.tm_mon)
        d = str(localtime.tm_mday)
        h = str(localtime.tm_hour)
        mini = str(localtime.tm_min)
        secon = str(localtime.tm_sec)
        dbsnapnametime = "mydb"+"-"+d+"-"+mo+"-"+yr+"-"+secon
        return dbsnapnametime
        YourDbName= "YOUR DB NAME" #Replace YOUR DB NAME with your db name eg: your db name is mydb ,this line should look like YourDbName = 'mydb'
    dbsnapname=snapname()
    dbsnapre = dbsnap.create_db_snapshot(DBSnapshotIdentifier=dbsnapname,DBInstanceIdentifier=YourDbName,Tags=[{'Key':'Name','Value':'dbsnapshots'},])
    
    
    """IF you have proper execution role attached lambda function and your resource is in same region
    in which your running the script then you don't need to pass accesskey,secretkey or else pass then in the script like i did"""
    
    """********************FOR LINUX/ WINDOWS STATIONS USE BELOW SCRIPT *****************"""
    
import boto3
import datetime
import time
dbsnap = boto3.client('rds',aws_access_key_id='YOUR ACESS KEY ', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
from datetime import date
def snapname():
    localtime = time.localtime(time.time())
    yr = str(localtime.tm_year)
    mo = str(localtime.tm_mon)
    d = str(localtime.tm_mday)
    h = str(localtime.tm_hour)
    mini = str(localtime.tm_min)
    secon = str(localtime.tm_sec)
    dbsnapnametime = "mydb"+"-"+d+"-"+mo+"-"+yr+"-"+secon
    return dbsnapnametime
YourDbName= "YOUR DB NAME"    #Replace YOUR DB NAME with your db name eg: your db name is mydb ,this line should look like YourDbName = 'mydb'
dbsnapname=snapname()
dbsnapre = dbsnap.create_db_snapshot(DBSnapshotIdentifier=dbsnapname,DBInstanceIdentifier=YourDbName,Tags=[{'Key':'Name','Value':'dbsnapshots'},])
    
    
    
    """ NOTE : IF YOUR USING THIS SCRIPT IN WINDOWS/LINUX or ANY WORKSTATION ITS MANDATORY TO PASS SECRET KEY ACCESS KEY AND REGION """
