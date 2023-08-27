import os

import pytest
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


@pytest.fixture(scope="session", autouse=True)
def api_key():
    return os.getenv("API_KEY")


@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")
