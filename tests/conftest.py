import pytest


@pytest.fixture
def api():
    return "https://jsonplaceholder.typicode.com/"


@pytest.fixture
def posts():
    return {
        'title': 'John',
        'body': 'Marshall',
        'userId': '91',
    }


@pytest.fixture
def header():
    return {'Content-type': 'application/json; charset=UTF-8'}
