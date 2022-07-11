import boto3
import os
import json
import uuid
from datetime import datetime


def lambda_handler(message, context):
    if "body" not in message or message["httpMethod"] != "POST":
        return {
            "statusCode": 400,
            "headers": {},
            "body": json.dumps({"msg": "Bad Request"}),
        }

    table_name = os.environ.get("TABLE", "Item")
    region = os.environ.get("REGION", "ap-southeast-1")

    resource = boto3.resource("dynamodb", region_name=region)

    table = resource.Table(table_name)
    request = json.loads(message["body"])
    id = str(uuid.uuid4())

    params = {
        "id": id,
        "name": request["name"],
        "description": request["description"],
        "price": request["price"],
        "is_active": request["is_active"],
        "created_at": datetime.now().isoformat(),
    }

    response = table.put_item(Item=params)
    # print(response, "put_item")

    response = table.get_item(Key={"id": id})

    return {
        "statusCode": 201,
        "headers": {},
        "body": json.dumps(response["Item"]),
    }
