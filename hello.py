import boto3

client = boto3.client('rekognition')

response = client.detect_labels(
    Image={
        'S3Object': {
            'Bucket': 'mingfu',
            'Name': 'licensePlate1.jpg',
        },
    },
)

print(response)