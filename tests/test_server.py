import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Test that index page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'MarkItDown' in response.data


def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert 'service' in data


def test_static_files(client):
    """Test that static files are accessible"""
    response = client.get('/app.js')
    assert response.status_code == 200
