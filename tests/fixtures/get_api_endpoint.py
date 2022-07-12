import pytest
import boto3


@pytest.fixture(scope="function")
def get_api_endpoint(get_stack_name):
    """
    Based on the provided env variable AWS_SAM_STACK_NAME,
    here we use cloudformation API to find out what the ItemApi URL is
    """
    stack_name = get_stack_name
    client = boto3.client("cloudformation")

    try:
        response = client.describe_stacks(StackName=stack_name)
    except Exception as e:
        raise Exception(
            f"Cannot find stack {stack_name}. \n"
            f'Please make sure stack with the name "{stack_name}" exists.'
        ) from e

    stacks = response["Stacks"]

    stack_outputs = stacks[0]["Outputs"]
    api_outputs = [
        output for output in stack_outputs if output["OutputKey"] == "ItemApi"
    ]
    assert api_outputs

    return api_outputs[0]["OutputValue"]
