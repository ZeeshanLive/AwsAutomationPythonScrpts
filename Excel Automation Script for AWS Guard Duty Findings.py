import boto3
import os
import datetime
import time
from datetime import date
def lambda_handler(event, context):
    c = os.getcwd()
    os.chdir("/tmp/")
    b = os.getcwd()
    localtime = time.localtime(time.time())
    yr = str(localtime.tm_year)
    mo = str(localtime.tm_mon)
    d = str(localtime.tm_mday)
    h = str(localtime.tm_hour)
    mini = str(localtime.tm_min)
    LT = yr +"-"+mo+"-"+d+"-"+h+"-"+mini+"(minutes)"
    m = 'GuardDutyFinding'+""+LT+".csv"
    GD = boto3.client('guardduty',region_name='ap-south-1')
    detector = GD.list_detectors()
    IDLIST=[]
    i = 0
    while i < len(detector['DetectorIds']):
        ID = str(detector['DetectorIds'][i])
        IDLIST.append(str(ID))
        i=i+1
    print (IDLIST)
    u=[]
    paginator = GD.get_paginator('list_findings')
    b = paginator.paginate(DetectorId=IDLIST[0],PaginationConfig={'PageSize':10})
    for k in b:
        a = k['FindingIds']
        u.append(a)
    findingdata=[]
    for fin in u:
        l = GD.get_findings(DetectorId=IDLIST[0],FindingIds=fin)
        findingdata.append(l['Findings'])
    finaldata=[]
    for mm in findingdata:
        for uu in mm:
            finaldata.append(uu)
    file = open('test.csv','w')
    for item in finaldata:
        file.write("%s\n" % item)
    file.close()
    s3 = boto3.client('s3')
    with open('test.csv', 'rb') as jj:
        s3.upload_fileobj(jj, '#YOURBUCKETNAME', m ) 
    
