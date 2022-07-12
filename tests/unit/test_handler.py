# import json

import pytest

from src.create_item import app


@pytest.mark.parametrize(
    "apigw_event",
    [
        {
            "body": {
                "name": "Owl",
                "description": "A bjord",
                "price": "10.00",
                "is_active": "1",
            },
            "resource": "/items",
            "httpMethod": "POST",
        }
    ],
    indirect=[
        "apigw_event",
    ],
)
def test_create_item(apigw_event):

    ret = app.lambda_handler(apigw_event, "")

    print(ret["body"])

    assert ret["statusCode"] == 201
    assert "id" in ret["body"]
