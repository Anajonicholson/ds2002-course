#!/c/Users/16073/AppData/Local/Programs/Python/Python310/python


import boto3

s3 = boto3.client('s3')

bucket = 'ds2002-fhy9gs'
local_file_path = "C:/Users/16073/Projects/ds2002-course/mywork/labs/lab4/babygoat.jpg"
object_name = 'babygoat.jpg'

with open(local_file_path, 'rb') as file:
    file_contents = file.read()

resp = s3.put_object(
    Body=file_contents,
    Bucket=bucket,
    Key=object_name
)

expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': object_name},
    ExpiresIn=expires_in
)

print("Presigned URL:", response)
