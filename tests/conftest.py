import pytest
import requests
from data import Urls
from helper import generate_courier

@pytest.fixture()
def new_courier():
    random_courier = generate_courier()
    requests.post(Urls.POST_COURIER, data=random_courier)
    yield random_courier