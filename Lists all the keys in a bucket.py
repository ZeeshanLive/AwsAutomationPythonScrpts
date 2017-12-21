import boto3
base = boto3.client('s3')
BUCKETNAME = "YOUR BUCKET NAME"  #Replace "YOUR BUCKET NAME " with the name of your bucket 
obj = base.list_objects_v2(Bucket = BUCKETNAME)
L_o_C = len(obj['Contents'])
keynames = []
i = 0 
for i in range(L_o_C):
	k = obj['Contents'][i]['Key']
	keynames.append( k )
	i = i + 1 
keynames[]
