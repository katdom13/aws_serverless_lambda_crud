# import json

import pytest

from src.create_item import app


@pytest.fixture()
def apigw_event():
    """Generates API GW Event"""

    return {
        "body": '{"name": "Owl3", "description": "A bird", "price": "3.00", "is_active": "True"}',
        "resource": "/items",
        "requestContext": {
            "resourcePath": "/items",
            "httpMethod": "POST",
        },
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "httpMethod": "POST",
    }


def test_lambda_handler(apigw_event):

    ret = app.lambda_handler(apigw_event, "")
    # data = json.loads(ret["body"])

    assert ret["statusCode"] == 201
    assert "id" in ret["body"]
    # assert data["message"] == "hello world"
    # assert "location" in data.dict_keys()
