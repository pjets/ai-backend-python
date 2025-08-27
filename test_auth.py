"""
Test Authentication Endpoints

Example requests for testing the authentication functionality
"""

import requests
import json
from datetime import date

# Base URL
BASE_URL = "http://localhost:8000"

def test_register():
    """Test user registration"""
    user_data = {
        "email": "test@example.com",
        "password": "testpassword123",
        "fullname": "Test User",
        "phone_number": "0812345678",
        "birthday": "1990-01-01"
    }
    
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    print("Register Response:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)
    return response

def test_login():
    """Test user login"""
    login_data = {
        "email": "test@example.com",
        "password": "testpassword123"
    }
    
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    print("Login Response:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)
    
    if response.status_code == 200:
        return response.json()["access_token"]
    return None

def test_profile(token):
    """Test protected profile endpoint"""
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(f"{BASE_URL}/profile", headers=headers)
    print("Profile Response:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

if __name__ == "__main__":
    print("Testing Authentication Endpoints")
    print("=" * 50)
    
    # Test registration
    test_register()
    
    # Test login
    token = test_login()
    
    # Test protected endpoint
    if token:
        test_profile(token)
    
    print("Testing completed!")
