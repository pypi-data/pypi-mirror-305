import requests
import json
import logging
from qubicon_client.config import load_token, get_base_url
from qubicon_client.utils import make_request

ENDPOINTS = {
    'single_model': '/api/computable-models/{model_id}?deleted=false'
}

def fetch_model_details(token, model_id):
    """
    Fetch model details from the API.
    
    Args:
        token (str): The authentication token.
        model_id (int): The ID of the model to fetch.

    Returns:
        dict: The model details from the API.
    """
    base_url = get_base_url()
    url = base_url + ENDPOINTS['single_model'].format(model_id=model_id)
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching model details: {e}")
        return None

def convert_to_importable_format(api_response):
    """
    Converts the API response of a model into an importable JSON structure.
    
    Args:
        api_response (dict): The API response from the GET model details endpoint.
        
    Returns:
        dict: The importable JSON structure.
    """
    if not api_response:
        logging.error("No valid model data to convert.")
        return None

    # Prepare the new structure for import
    importable_model = {
        "engineType": api_response.get("engineType"),
        "kpiName": api_response.get("kpiName"),
        "abbr": api_response.get("abbr"),
        "calculationStyle": api_response.get("calculationStyle"),
        "status": "DRAFT",  # Default status, can be updated if needed
        "description": api_response.get("description", ""),
        "script": api_response.get("script", "")
    }

    # Process inputs
    importable_model["inputs"] = [
        {
            "name": input_item.get("name"),
            "order": idx,
            "physicalQuantityUnit": {
                "name": input_item["physicalQuantityUnit"].get("name"),
                "unit": input_item["physicalQuantityUnit"].get("unit"),
                "status": input_item["physicalQuantityUnit"].get("status")
            },
            "description": input_item.get("description", "")
        } for idx, input_item in enumerate(api_response.get("inputs", []))
    ]

    # Process outputs
    importable_model["outputs"] = [
        {
            "name": output_item.get("name"),
            "order": idx,
            "physicalQuantityUnit": {
                "name": output_item["physicalQuantityUnit"].get("name"),
                "unit": output_item["physicalQuantityUnit"].get("unit"),
                "status": output_item["physicalQuantityUnit"].get("status")
            },
            "description": output_item.get("description", "")
        } for idx, output_item in enumerate(api_response.get("outputs", []))
    ]

    return importable_model

def export_model_to_json(model_id, output_file):
    """
    Export a model into a JSON file based on the given model ID.

    Args:
        model_id (int): The ID of the model to export.
        output_file (str): The output file path for the exported JSON.
    """
    token = load_token()
    if not token:
        logging.error("Authentication token is missing. Please log in first.")
        return

    # Fetch model details
    model_details = fetch_model_details(token, model_id)
    if not model_details:
        logging.error("Failed to fetch model details.")
        return

    # Convert the model details into an importable format
    importable_json = convert_to_importable_format(model_details)
    if not importable_json:
        logging.error("Failed to convert model to importable format.")
        return

    # Export to JSON file
    try:
        with open(output_file, 'w') as json_file:
            json.dump(importable_json, json_file, indent=4)
        logging.info(f"Model exported successfully to {output_file}.")
    except IOError as e:
        logging.error(f"Failed to write model to JSON file: {e}")

# Example usage:
# export_model_to_json(386, 'exported_model.json')
