import requests
import os
from flask import request, jsonify

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def verify_supabase_token(token):
    """Verifies a JWT token with Supabase Auth API"""
    headers = {
        "Authorization": f"Bearer {token}",
        "apikey": SUPABASE_KEY
    }
    
    response = requests.get(f"{SUPABASE_URL}/auth/v1/user", headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns user data if token is valid
    return None  # Token is invalid or expired
