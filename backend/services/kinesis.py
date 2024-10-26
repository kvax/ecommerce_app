import boto3
import json
from config import Config

kinesis_client = boto3.client('kinesis', region_name=Config.KINESIS_REGION)

def put_user_activity(data):
    response = kinesis_client.put_record(
        StreamName=Config.KINESIS_STREAM_NAME,
        Data=json.dumps(data),
        PartitionKey="user_activity"
    )
    return response
