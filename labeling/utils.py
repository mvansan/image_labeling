import boto3
from django.conf import settings
from .models import Image

s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_S3_REGION_NAME
)

def update_image_links_from_s3():
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    count = 0

    if 'Contents' in response:
        for item in response['Contents']:
            file_name = item['Key']
            s3_url = f'https://{bucket_name}.s3.amazonaws.com/{file_name}'

            if not Image.objects.filter(image_url=s3_url).exists():
                Image.objects.create(image_url=s3_url)
                count += 1 

        print(f"Đã thêm {count} ảnh mới vào database.") 
    else:
        print("Không có file nào trong bucket S3.")
