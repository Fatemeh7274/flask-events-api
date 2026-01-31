import json
import boto3
from datetime import datetime

REGION = "eu-north-1"
BUCKET_NAME = "flask-visit-logs-2026"

s3 = boto3.client("s3", region_name=REGION)

def log_event_to_s3(data):
    now = datetime.utcnow()

    key = (
        f"logs/{now.year}/"
        f"{now.month:02d}/"
        f"{now.day:02d}/"
        f"event_{now.strftime('%H%M%S%f')}.json"
    )



    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(data),
        ContentType="application/json"
    )
