import boto3
s3 = boto3.resource('s3')

for i in range(1,25):
  bucketName = "student"+`i`+"-pcfdemo-releases"
  print bucketName
  bucket = s3.Bucket(bucketName)
  for key in bucket.objects.all():
    key.delete()
  bucket.delete()
  bucketNameRC = "student"+`i`+"-pcfdemo-release-candidates"
  print bucketNameRC
  bucketRC = s3.Bucket(bucketNameRC)
  for key in bucketRC.objects.all():
    key.delete()
  bucketRC.delete()




