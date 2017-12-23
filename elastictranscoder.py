def lambda_handler(event, context):
    import boto3
    import time
    import datetime
    from datetime import date
    base = boto3.client('s3',aws_access_key_id='YOU_ACCESS_KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    c = boto3.client('elastictranscoder',aws_access_key_id='YOU_ACCESS_KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    BUCKETNAME = "transcoder-1"  #Replace "YOUR BUCKET NAME " with the name of your bucket 
    obj = base.list_objects_v2(Bucket = BUCKETNAME)
    L_o_C = len(obj['Contents'])
    keynames = []
    i = 0 
    for i in range(L_o_C):
        k = obj['Contents'][i]['Key']
        keynames.append(k)
        i = i+1
    print (keynames)
    re = c.create_pipeline(
    Name='newtest1',                                           #NAME OF YOUR PIPELINE
    InputBucket='transcoder-1',                                #INPUT BUCKET NAME 
	  OutputBucket='transcoder-2',                                #OUTPUT BUCKET NAME
    Role='arn:aws:iam::448674636570:role/Elastic_Transcoder_Default_Role',)
    popeye = re['Pipeline']['Id']
    pid = ['1351620000001-000001','1351620000001-200010']       #IF YOU WANT TO CONVERT SINGLE FILE WITH MULTIPLE PRESETS MENTION THE PRESET ID here GIVING  ","
    foldername = "testfolder/"   #IT WILL CREATE FOLDER IN THE BUCKET IF YOU DONT WANT TO CREATE FOLDER SKIP THIS VARIABLE  
    updatedkeey = []
    for k in keynames:
        for j in pid:
            localtime = time.localtime(time.time())
            yr = str(localtime.tm_year)
            mo = str(localtime.tm_mon)
            d = str(localtime.tm_mday)
            h = str(localtime.tm_hour)
            mini = str(localtime.tm_min)
            secon = str(localtime.tm_sec)
            daty = yr+"-"+mo+"-"+d+"-"+secon
            job = c.create_job(
            PipelineId= popeye,
            Input={'Key': k,'FrameRate':  '30','Resolution': 'auto',},
            Output={'Key': foldername+daty+k,'PresetId': j,}) # IF NOT USING FOLDER VARiABLE REMOVE[ 'Key': foldername+daty+k ] foldername from the key   
            time.sleep(2)
            
            
    """ **************************************** """
    # FOR LINUX AND WINDOWS SCRIPT 
    import boto3
    import time
    import datetime
    from datetime import date
    base = boto3.client('s3',aws_access_key_id='YOU_ACCESS_KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    c = boto3.client('elastictranscoder',aws_access_key_id='YOU_ACCESS_KEY', aws_secret_access_key='YOUR SECRET KEY',region_name='REGION NAME')
    BUCKETNAME = "transcoder-1"  #Replace "YOUR BUCKET NAME " with the name of your bucket 
    obj = base.list_objects_v2(Bucket = BUCKETNAME)
    L_o_C = len(obj['Contents'])
    keynames = []
    i = 0 
    for i in range(L_o_C):
        k = obj['Contents'][i]['Key']
        keynames.append(k)
        i = i+1
    print (keynames)
    re = c.create_pipeline(
    Name='newtest1',                                           #NAME OF YOUR PIPELINE
    InputBucket='transcoder-1',                                #INPUT BUCKET NAME 
	  OutputBucket='transcoder-2',                                #OUTPUT BUCKET NAME
    Role='arn:aws:iam::448674636570:role/Elastic_Transcoder_Default_Role',)
    popeye = re['Pipeline']['Id']
    pid = ['1351620000001-000001','1351620000001-200010']       #IF YOU WANT TO CONVERT SINGLE FILE WITH MULTIPLE PRESETS MENTION THE PRESET ID here GIVING  ","
    foldername = "testfolder/"   #IT WILL CREATE FOLDER IN THE BUCKET IF YOU DONT WANT TO CREATE FOLDER SKIP THIS VARIABLE  
    updatedkeey = []
    for k in keynames:
        for j in pid:
            localtime = time.localtime(time.time())
            yr = str(localtime.tm_year)
            mo = str(localtime.tm_mon)
            d = str(localtime.tm_mday)
            h = str(localtime.tm_hour)
            mini = str(localtime.tm_min)
            secon = str(localtime.tm_sec)
            daty = yr+"-"+mo+"-"+d+"-"+secon
            job = c.create_job(
            PipelineId= popeye,
            Input={'Key': k,'FrameRate':  '30','Resolution': 'auto',},
            Output={'Key': foldername+daty+k,'PresetId': j,}) # IF NOT USING FOLDER VARiABLE REMOVE[ 'Key': foldername+daty+k ] foldername from the key   
            time.sleep(2)
            
            
        
    
