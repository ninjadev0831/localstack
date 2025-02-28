import json
import os

import boto3

should_configure_client = os.environ.get("CONFIGURE_CLIENT", "0") == "1"

if should_configure_client:
    sqs_client = boto3.client("sqs", endpoint_url=os.environ["AWS_ENDPOINT_URL"])
else:
    sqs_client = boto3.client("sqs")


def handler(event, context):
    print(json.dumps(event))
    sqs_client.list_queues()
    return "ok"
