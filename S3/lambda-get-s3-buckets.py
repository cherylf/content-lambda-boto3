import boto3

# get resource
s3 = boto3.resource('s3')

# get and print all buckets in the account
for bucket in s3.buckets.all():
    print(bucket.name)