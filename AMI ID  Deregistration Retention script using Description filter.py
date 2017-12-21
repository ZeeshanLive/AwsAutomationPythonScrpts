""" ********************** IF YOU ARE USING THIS SCRIPT IN AWS LAMBDA FUNCTION USE THE BELOW SCRIPT ******** """
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
  #NOTE : You can use different filters to filter your Images , AVAILABLE Filters options are provided end of this script 
  
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
"""" ******************** END OF SCRIPT *********************************************** """            

""" ********************** IF YOU ARE USING THIS SCRIPT IN WINDOWS OR LINUX SYSTEMS  USE THE BELOW SCRIPT ******** """
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
#NOTE : You can use different filters to filter your Images , AVAILABLE Filters options are provided end of this script 
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
  if ( DiffDays == 0 ):    # Replace the number with your retention no of days  eg for 2 days [if ( DiffDays >= 2  )]
              sn.deregister()
 
"""" ******************** END OF SCRIPT *********************************************** """

"""  ************************** AVAILABLE FILTER OPTIONS ***************************************** """
"""
For Example to filter your images with  architecture basis  ,  please refer the below command 

ami = imageid.describe_images(Filters=[{'Name':'architecture','Values':['i386']},],Owners=['YOUR ACCOUNT ID'])

architecture - The image architecture (i386 | x86_64 ).
block-device-mapping.delete-on-termination - A Boolean value that indicates whether the Amazon EBS volume is deleted on instance termination.
block-device-mapping.device-name - The device name specified in the block device mapping (for example, /dev/sdh or xvdh ).
block-device-mapping.snapshot-id - The ID of the snapshot used for the EBS volume.
block-device-mapping.volume-size - The volume size of the EBS volume, in GiB.
block-device-mapping.volume-type - The volume type of the EBS volume (gp2 | io1 | st1 | sc1 | standard ).
description - The description of the image (provided during image creation).
ena-support - A Boolean that indicates whether enhanced networking with ENA is enabled.
hypervisor - The hypervisor type (ovm | xen ).
image-id - The ID of the image.
image-type - The image type (machine | kernel | ramdisk ).
is-public - A Boolean that indicates whether the image is public.
kernel-id - The kernel ID.
manifest-location - The location of the image manifest.
name - The name of the AMI (provided during image creation).
owner-alias - String value from an Amazon-maintained list (amazon | aws-marketplace | microsoft ) of snapshot owners. Not to be confused with the user-configured AWS account alias, which is set from the IAM console.
owner-id - The AWS account ID of the image owner.
platform - The platform. To only list Windows-based AMIs, use windows .
product-code - The product code.
product-code.type - The type of the product code (devpay | marketplace ).
ramdisk-id - The RAM disk ID.
root-device-name - The device name of the root device volume (for example, /dev/sda1 ).
root-device-type - The type of the root device volume (ebs | instance-store ).
state - The state of the image (available | pending | failed ).
state-reason-code - The reason code for the state change.
state-reason-message - The message for the state change.
sriov-net-support - A value of simple indicates that enhanced networking with the Intel 82599 VF interface is enabled.
tag :key =*value* - The key/value combination of a tag assigned to the resource. Specify the key of the tag in the filter name and the value of the tag in the filter value. For example, for the tag Purpose=X, specify tag:Purpose for the filter name and X for the filter value.
tag-key - The key of a tag assigned to the resource. This filter is independent of the tag-value filter. For example, if you use both the filter "tag-key=Purpose" and the filter "tag-value=X", you get any resources assigned both the tag key Purpose (regardless of what the tag's value is), and the tag value X (regardless of what the tag's key is). If you want to list only resources where Purpose is X, see the tag :key =*value* filter.
tag-value - The value of a tag assigned to the resource. This filter is independent of the tag-key filter.
virtualization-type - The virtualization type (paravirtual | hvm ).

"""


