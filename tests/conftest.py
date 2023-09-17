import os

import pytest
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")


# @pytest.fixture(scope="session", autouse=True)
# def api_key():
#     return os.getenv("API_KEY")
#
#
# @pytest.fixture
# def base_url(scope="session", autouse=True):
#     return os.getenv("BASE_URL")
