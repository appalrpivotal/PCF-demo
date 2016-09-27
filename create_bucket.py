import boto3
s3 = boto3.resource('s3')

for i in range(1,25):
  bucketName = "student"+`i`+"-pcfdemo-releases"
  bucketNameRC = "student"+`i`+"-pcfdemo-release-candidates"
  print bucketName
  s3.create_bucket(Bucket=bucketName)
  s3.create_bucket(Bucket=bucketNameRC)


