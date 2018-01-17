
import boto3
ImageAmi = 'Your AMI ID' # AMI ID OF Your Image
ImageRegion = ' Region in which your image resides' # IN WHICH REGION YOUR AMI RESIDES
bck_region = 'your region name in which you want to create backup' #REGION IN WHICH YOU WANT TO COPY YOUR IMAGE
bck = boto3.client('ec2',region_name = bck_region )
CopyImage = bck.copy_image(Description="'Image copy from my'+'-'+ImageRegion",Name='crossregionbackupimage',SourceImageId = ImageAmi , SourceRegion = ImageRegion)
