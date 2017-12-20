
def lambda_handler(event, context):
  import datetime
  import time
  import boto3
  from datetime import date
  imageid = boto3.client('ec2',aws_access_key_id='YOUR ACCESS KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
  re = boto3.resource('ec2',aws_access_key_id='YOUR ACCESS KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
  localtime = time.localtime(time.time())
  yr = str(localtime.tm_year)
  mo = str(localtime.tm_mon)
  d = str(localtime.tm_mday)
  h = str(localtime.tm_hour)
  mini = str(localtime.tm_min)
  secon = str(localtime.tm_sec)
  ami = imageid.describe_images(Filters=[{'Name':'description','Values':['YOUR AMI DESCRIPTION ']},],Owners=['YOUR ACCOUNT ID'])
  amii = len(ami['Images'])
  amiid =[]
  k = 0
  while ( k < amii):
        am = ami['Images'][k]['ImageId']
        amiid.append(am)
        k = k+1
  
  for amy in amiid:
        sn = re.Image(amy)
        times = str(sn.creation_date)
        idee = (sn.id)
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
        print (DiffDays)
        if ( DiffDays == 0 ):    # Replace the number with your retention no of days  eg for 2 days [if ( DiffDays >= 2  )]
              sn.deregister()
        
