import pytest
from app import create_app
from flask.testing import FlaskClient
from http import HTTPStatus
from typing import Generator

@pytest.fixture(scope='module')
def test_dummy_client() -> Generator[FlaskClient, None, None]:
    config = {
        'TESTING': True
    }
    app = create_app(config)
    yield app.test_client()


def test_dummy_simple_first(test_dummy_client: FlaskClient):
    response = test_dummy_client.get('/api/dummy/v1_1')    
    assert response.status_code != HTTPStatus.NOT_FOUND
