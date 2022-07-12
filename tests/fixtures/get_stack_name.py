from pathlib import Path
import pytest
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = os.path.join(BASE_DIR, "env", "dev.env")
load_dotenv(env)


@pytest.fixture(scope="function")
def get_stack_name():
    stack_name = os.environ.get("AWS_SAM_STACK_NAME")
    if not stack_name:
        raise Exception(
            "Cannot find env var AWS_SAM_STACK_NAME. \n"
            "Please setup this environment variable with the stack name where we are running integration tests."
        )

    return stack_name
