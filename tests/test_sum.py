import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

def test_get_sums_by_invalid_result(client):
    response = client.get('/sum/result/not_an_int')  
    assert response.status_code == 404 or response.status_code == 400
    assert 'error' in response.get_json()
