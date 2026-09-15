# Add project root to Python path
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Import Flask application
from app import app


# Create a test client
client = app.test_client()


# Test 1: Check homepage
def test_home_page():
    response = client.get("/")
    assert response.status_code == 200


# Test 2: Check movie details page
def test_movie_details():
    response = client.get("/movie/1")
    assert response.status_code == 200


# Test 3: Check invalid movie ID
def test_invalid_movie():
    response = client.get("/movie/999")
    assert response.status_code == 404
