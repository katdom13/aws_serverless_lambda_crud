import boto3
import os
import json


def lambda_handler(message, context):
    if "httpMethod" not in message or message["httpMethod"] != "GET":
        return {
            "statusCode": 400,
            "headers": {},
            "body": json.dumps({"msg": "Bad Request"}),
        }

    table_name = os.environ.get("TABLE", "Item")
    region = os.environ.get("REGION", "ap-southeast-1")

    resource = boto3.resource("dynamodb", region_name=region)

    table = resource.Table(table_name)
    response = table.scan()

    return {
        "statusCode": 200,
        "headers": {},
        "body": json.dumps(response["Items"]),
    }
