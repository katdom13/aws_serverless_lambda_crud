# import os
# from unittest import TestCase
# from urllib import response

# import boto3
import requests

"""
Make sure env variable AWS_SAM_STACK_NAME exists with the name of the stack we are going to test.
"""


def test_create_item_api_gateway(get_api_endpoint):
    # pass
    root = get_api_endpoint

    data = {
        "name": "Owl",
        "description": "A bjord",
        "price": "10.00",
        "is_active": "1",
    }

    """
    Call the API Gateway endpoint and check the response
    """
    response = requests.post(root + "/items", json=data)
    assert response.status_code == 201


def test_list_items_api_gateway(get_api_endpoint):
    # pass
    root = get_api_endpoint

    """
    Call the API Gateway endpoint and check the response
    """
    response = requests.get(root + "/items")
    assert response.status_code == 200
