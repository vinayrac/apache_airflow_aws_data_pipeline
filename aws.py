import boto3
import json

S3_client = boto3.client('s3')

def lambda_handler(event , contaxt):

    source_bucket = event['Redaer'][0]['s3']['bucket']['name']
    object_key = event['Reader'][0]['s3']['object']['key']

    target_bucket = 'copy_of_raw_json_bucekt'
    copy_object = {'Bucekt' : source_bucket , 'Key' : object_key}

    waiter = S3_client.get_waiter('object_exits')
    waiter.wait(Bucket = source_bucket, Key = object_key)
    S3_client.copy_object(Bucket = target_bucket , Key = object_key , Copy_object = copy_object)

    return{
        'statusCode' : 200,
        'body' : json.dumps('Copy Completed successful')
    }