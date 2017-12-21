def lambda_handler(event, context):
    # TODO implement
    import datetime
    import time
    import boto3
    from datetime import date
    re = boto3.resource('ec2',aws_access_key_id='YOUR ACESS KEY ', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    c = boto3.client('ec2',aws_access_key_id='YOUR ACESS KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    ami = c.describe_images(Owners=['YOUR AWS ACCOUNT NUMBER'])
    amii = len(ami['Images'])
    amiid =[]
    k = 0
    while ( k < amii):
        am = ami['Images'][k]['ImageId']
        amiid.append(am)
        k = k+1
        #print (amiid)
    for amy in amiid:
        sn = re.Image(amy)
        times = str(sn.creation_date)
        year = int(times[0:4])
        month = int(times[5:7])
        day = int(times[8:10])
        ST = date( year , month , day )
        localtime = time.localtime(time.time())
        cyear = int( localtime.tm_year)
        cmonth = int(localtime.tm_mon)
        cday = int(localtime.tm_mday)
        cdate = (cyear,cmonth,cday)
        cdate = date(cyear,cmonth,cday)
        diff = cdate - ST
        DiffDays = diff.days
        if ( DiffDays >= 1  ):    # Replace the number with your retention no of days  eg for 2 days [if ( DiffDays >= 2  )]
            out = sn.deregister()
            print (out)
    snapid = c.describe_snapshots(OwnerIds = ['448674636570'])
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
	    localtime = time.localtime(time.time())
	    cyear = int( localtime.tm_year)
	    cmonth = int(localtime.tm_mon)
	    cday = int(localtime.tm_mday)
	    cdate = (cyear,cmonth,cday)
	    cdate = date(cyear,cmonth,cday)
	    diff = cdate - ST
	    DiffDays = diff.days
	    if ( DiffDays >= 1 ): Replace the number with your retention no of days  eg for 2 days [if ( DiffDays >= 2  )]
		    out = n.delete()
		    print (out)
        
        
#NOTE : script will compare the image id date with the host server or lambda date .. please make sure that your device running with coorect date  

