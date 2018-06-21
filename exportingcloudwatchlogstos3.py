import boto3
import datetime
from datetime import datetime as dt

logs = boto3.client('logs')

currentdateINmilisec = int(time.mktime(datetime.datetime.now().timetuple()) * 1000)
past30_date = datetime.datetime.now() + datetime.timedelta(-100)
PastdateINmilisec = int(time.mktime(past30_date .timetuple()) * 1000)

rr = logs.create_export_task(taskName = 'testexpo',logGroupName='wonderlatest-UAT',fromTime=PastdateINmilisec,to=currentdateINmilisec
,destination='cloudwatcglogautomationbucket')
