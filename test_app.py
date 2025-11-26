import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the index route returns the calculator page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask Calculator' in response.data

def test_calculate_addition(client):
    """Test addition calculation."""
    response = client.post('/calculate', 
                         json={'expression': '2+3'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 5

def test_calculate_subtraction(client):
    """Test subtraction calculation."""
    response = client.post('/calculate', 
                         json={'expression': '10-4'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 6

def test_calculate_multiplication(client):
    """Test multiplication calculation."""
    response = client.post('/calculate', 
                         json={'expression': '3*4'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 12

def test_calculate_division(client):
    """Test division calculation."""
    response = client.post('/calculate', 
                         json={'expression': '15/3'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 5

def test_calculate_complex_expression(client):
    """Test complex mathematical expression."""
    response = client.post('/calculate', 
                         json={'expression': '(2+3)*4'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 20

def test_calculate_division_by_zero(client):
    """Test division by zero error handling."""
    response = client.post('/calculate', 
                         json={'expression': '5/0'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_calculate_invalid_expression(client):
    """Test invalid expression error handling."""
    response = client.post('/calculate', 
                         json={'expression': '2+'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_calculate_invalid_characters(client):
    """Test security check for invalid characters."""
    response = client.post('/calculate', 
                         json={'expression': 'import os'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_empty_expression(client):
    """Test empty expression handling."""
    response = client.post('/calculate', 
                         json={'expression': ''})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data