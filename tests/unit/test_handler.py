# import json

import pytest

from src.create_item import app as create_item
from src.return_items import app as return_items


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

    ret = create_item.lambda_handler(apigw_event, "")

    print(ret["body"])

    assert ret["statusCode"] == 201
    assert "id" in ret["body"]


@pytest.mark.parametrize(
    "apigw_event",
    [
        {
            "body": "",
            "resource": "/items",
            "httpMethod": "GET",
        }
    ],
    indirect=[
        "apigw_event",
    ],
)
def test_list_items(apigw_event):
    ret = return_items.lambda_handler(apigw_event, "")

    assert ret["statusCode"] == 200
    assert "id" in ret["body"]
