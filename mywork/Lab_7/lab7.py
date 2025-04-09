import boto3
import requests
import sys

image_link = sys.argv[1]
bucket = sys.argv[2]
file_name = sys.argv[3]
expiration = int(sys.argv[4])

#Getting the image from the link the person added to command line
print(f"Getting the {image_link}")
upload = requests.get(image_link)
with open(file_name, 'wb') as f:
    f.write(upload.content)
print(f"Saved the {file_name}")

#Upload to a s3 bucket
s3 = boto3.client('s3', region_name = "us-east-1")
s3.upload_file(Filename = file_name, Bucket=bucket, Key=file_name)
print(f"Added to S3")

#Presign Url
presignurl = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': file_name},
    ExpiresIn=expiration
)

print(f"Presign Url valid for {expiration} seconds:\n{presignurl}")