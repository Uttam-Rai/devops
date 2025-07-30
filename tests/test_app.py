# tests/test_app.py
import os
# Make sure to set the python path to import app from src
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app

def test_hello():
    """Test the default greeting."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, from your deployed Flask app!" in response.data