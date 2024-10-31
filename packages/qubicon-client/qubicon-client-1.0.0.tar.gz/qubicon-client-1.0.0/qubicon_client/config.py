import os
import logging
import json
import time

CONFIG_DIR = os.path.expanduser('~/.qubicon')
TOKEN_FILE = os.path.join(CONFIG_DIR, 'credentials.json')

SERVER_OPTIONS = {
    "1": "https://master.qub-lab.io/",
    "2": "https://release-3.5.qub-lab.io",
}

BASE_URL = None
TOKEN_EXPIRATION_SECONDS = 3600  # 1 hour (60 minutes * 60 seconds)


def set_base_url(choice):
    """Set the BASE_URL based on user input or default to a predefined option."""
    global BASE_URL
    if choice in SERVER_OPTIONS:
        BASE_URL = SERVER_OPTIONS[choice]
        logging.info(f"BASE_URL set to {BASE_URL}")
    elif choice.startswith("http://") or choice.startswith("https://"):
        BASE_URL = choice
        logging.info(f"Custom BASE_URL set to {BASE_URL}")
    else:
        logging.error("Invalid URL provided. URL must start with 'http://' or 'https://'.")
        raise ValueError("Invalid URL. Please make sure the URL is valid.")


def get_base_url():
    """Return the current BASE_URL or raise an error if not set."""
    global BASE_URL
    if BASE_URL is None:
        _, loaded_base_url = load_token()
        if loaded_base_url:
            BASE_URL = loaded_base_url
        else:
            raise ValueError("BASE_URL is not set.")
    return BASE_URL


def load_token():
    """Load token and BASE_URL from file and check if the token has expired."""
    global BASE_URL
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, 'r') as f:
                token_data = json.load(f)

            token = token_data.get('token')
            BASE_URL = token_data.get('base_url')
            expiration_time = token_data.get('expires_at')

            # Check if token and BASE_URL are set and token is valid
            if time.time() >= expiration_time or not token or not BASE_URL:
                logging.warning("Token has expired or is invalid.")
                delete_token()  # Clear token and BASE_URL if invalid
                return None, None
            return token, BASE_URL
        except json.JSONDecodeError:
            logging.error("Error decoding the token file. Deleting corrupted token file.")
            delete_token()
            return None, None
        except Exception as e:
            logging.error(f"Failed to load token: {e}")
            return None, None
    return None, None


def save_token(token, expiration_time):
    """Save token, expiration time, and BASE_URL to a file."""
    global BASE_URL
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    
    token_data = {
        'token': token,
        'expires_at': expiration_time,
        'base_url': BASE_URL  # Store BASE_URL
    }

    with open(TOKEN_FILE, 'w') as f:
        json.dump(token_data, f)
    logging.info("Token, expiration time, and BASE_URL saved successfully.")


def delete_token():
    """Delete the saved token safely and reset BASE_URL."""
    global BASE_URL
    BASE_URL = None  # Reset BASE_URL when logging out
    if os.path.exists(TOKEN_FILE):
        try:
            os.remove(TOKEN_FILE)
            logging.info("Token deleted successfully.")
        except Exception as e:
            logging.error(f"Error deleting token: {e}")
    else:
        logging.warning("No token found to delete.")


def is_logged_in():
    """Check if the user is logged in by verifying the token and BASE_URL."""
    token, base_url = load_token()
    return token is not None and base_url is not None
