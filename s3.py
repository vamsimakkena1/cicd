import json
import boto3
from boto3.session import Session

with open('input.json') as json_file:
  data = json.load(json_file)
abc = data['s3bucket']
print(abc)

ACCESS_KEY=''
SECRET_KEY=''

session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
your_bucket = s3.Bucket(abc)
#your_bucket = s3.Bucket('lavamsi')
for s3_file in your_bucket.objects.all():
    print(s3_file.key)

#s3.create_bucket(Bucket='ladivya')


#conn = boto3.client('s3')  # again assumes boto.cfg setup, assume AWS S3
#for key in conn.list_objects(Bucket='lavamsi')['Contents']:
 #   print(key['Key'])
