import datetime
import time
import boto3
from datetime import date
imageid = boto3.client('ec2',aws_access_key_id='YOURACCESSKEY', aws_secret_access_key='SECRETKEY',region_name='REGIONNAME')
localtime = time.localtime(time.time())
yr = str(localtime.tm_year)
mo = str(localtime.tm_mon)
d = str(localtime.tm_mday)
h = str(localtime.tm_hour)
mini = str(localtime.tm_min)
secon = str(localtime.tm_sec)
imagename = "Testimage"+" "+ yr + '-'+ mo + '-' + d + '-' + h + '-' + mini + '-' + secon 
r = c.create_image(InstanceId='YOURINSTANCEID',Name=imagename,NoReboot=True)
