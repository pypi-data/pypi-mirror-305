import requests
import logging
from qubicon_client.config import save_token, delete_token, load_token, get_base_url
from qubicon_client.utils import make_request
import time

ENDPOINTS = {
    'login': '/api/login',
}


def login(username, password):
    """Log in the user and save the token."""
    base_url = get_base_url()
    url = base_url + '/api/login'
    data = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/json'}

    logging.info("Logging in...")
    response = make_request('POST', url, headers=headers, data=data)

    if response and 'normal' in response and 'token' in response['normal']:
        token = response['normal']['token']
        expiration_time = time.time() + 3600  # Set expiration time to 1 hour from now
        save_token(token, expiration_time)
        logging.info("Login successful!")
        return token
    else:
        logging.error("Login failed!")
        return None


def logout():
    """Log out the user by deleting the token."""
    logging.info("Logging out...")
    delete_token()
    logging.info("Logged out successfully!")

def is_token_expired():
    """Check if the token has expired manually (token valid for 1 hour)."""
    token = load_token()
    if not token:
        return True
    return False  # Token is valid if it was loaded successfully
