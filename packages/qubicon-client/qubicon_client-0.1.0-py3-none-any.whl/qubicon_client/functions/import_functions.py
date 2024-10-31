import requests
import json
import logging
from rapidfuzz import fuzz
import re
from qubicon_client.config import load_token, get_base_url

ENDPOINTS = {
    'computable_models': '/api/computable-models',
    'physical_quantities': '/api/physical-quantities',
    'specific_physical_quantity': '/api/physical-quantities/{id}'
}

# Normalize the physical quantity names
def normalize_name(name):
    # Convert to lowercase and remove spaces, dashes, and special characters
    return re.sub(r'[^a-zA-Z0-9]', '', name).lower()

# Fuzzy matching for physical quantities using rapidfuzz
def fuzzy_match(name1, name2, threshold=93):
    normalized_name1 = normalize_name(name1)
    normalized_name2 = normalize_name(name2)
    
    # Use token_sort_ratio for comparison, which handles reordering of words
    similarity = fuzz.token_sort_ratio(normalized_name1, normalized_name2)
    return similarity >= threshold  # Return True if similarity exceeds threshold

def check_existing_physical_quantity(pq_name, token):
    headers = {'Authorization': f'Bearer {token}'}
    base_url = get_base_url()
    url = base_url + ENDPOINTS['physical_quantities']
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        logging.info(f"Checking existing physical quantities for a match with '{pq_name}'.")
        quantities = response.json()
        for q in quantities:
            if fuzzy_match(q['name'], pq_name):
                logging.info(f"Fuzzy match found: '{q['name']}' matches '{pq_name}' (ID: {q['id']}).")
                return q
        logging.info(f"No match found for physical quantity '{pq_name}'. It will be created.")
    else:
        logging.error(f"Failed to retrieve physical quantities. Status code: {response.status_code}")
    return None

def check_existing_unit(physical_quantity, unit_name):
    # Match unit within the physical quantity
    for unit in physical_quantity['units']:
        if fuzzy_match(unit['unit'], unit_name):
            logging.info(f"Unit match found: '{unit_name}' within physical quantity '{physical_quantity['name']}' (ID: {unit['id']}).")
            return unit
    logging.info(f"No unit match found for '{unit_name}' in physical quantity '{physical_quantity['name']}'.")
    return None

# Create a new physical quantity and unit if none exist
def create_physical_quantity(pq_name, unit_name, token):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    base_url = get_base_url()
    url = get_base_url + ENDPOINTS['physical_quantities']
    
    quantity_data = {
        "name": pq_name,
        "units": [{"unit": unit_name}]
    }

    logging.info(f"Creating a new physical quantity '{pq_name}' with unit '{unit_name}'.")
    response = requests.post(url, json=quantity_data, headers=headers)
    
    if response.status_code == 201:
        logging.info(f"Physical quantity '{pq_name}' created successfully.")
        return response.json()
    elif response.status_code == 200:
        logging.info(f"Physical quantity '{pq_name}' already existed but was retrieved successfully.")
        return response.json()  # Consider this a success
    else:
        logging.error(f"Failed to create new physical quantity '{pq_name}'. Response: {response.content}")
        return None

# Update an existing physical quantity to add a new unit
def add_unit_to_existing_physical_quantity(pq_id, pq_name, unit_name, token):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    base_url = get_base_url()
    url = base_url + ENDPOINTS['specific_physical_quantity'].format(id=pq_id)

    logging.info(f"Adding unit '{unit_name}' to existing physical quantity '{pq_name}' (ID: {pq_id}).")
    
    # Get the existing units and append the new unit
    existing_pq = check_existing_physical_quantity(pq_name, token)
    if not existing_pq:
        logging.error(f"Physical quantity '{pq_name}' not found for updating.")
        return None

    # Add the new unit
    units = existing_pq['units'] + [{"unit": unit_name, "physicalQuantityId": pq_id}]
    updated_data = {
        "id": pq_id,
        "name": pq_name,
        "status": existing_pq.get("status", "IN_USE"),  # Maintain the same status
        "units": units
    }

    response = requests.put(url, json=updated_data, headers=headers)
    if response.status_code == 200:
        logging.info(f"Unit '{unit_name}' added successfully to physical quantity '{pq_name}'.")
        return response.json()
    else:
        logging.error(f"Failed to add unit '{unit_name}' to physical quantity '{pq_name}'. Response: {response.content}")
        return None

# Import model from a JSON file
def import_model_from_json(file_path):
    token = load_token()
    if not token:
        logging.error("You must be logged in to import a model.")
        return

    with open(file_path, 'r') as f:
        model_data = json.load(f)

    # Handle physical quantities and units for inputs and outputs
    model_data = handle_physical_quantities(model_data, token)

    # Finally, create the model
    create_model(token, model_data)

# Handle physical quantities and map them correctly for both inputs and outputs
def handle_physical_quantities(model_data, token):
    """Handle physical quantities and map them correctly for both inputs and outputs."""
    for var in model_data['inputs'] + model_data['outputs']:
        pq_name = var['physicalQuantityUnit']['name']
        unit_name = var['physicalQuantityUnit']['unit']
        
        # Check if the physical quantity already exists
        existing_pq = check_existing_physical_quantity(pq_name, token)
        
        if existing_pq:
            logging.info(f"Found existing physical quantity '{pq_name}' (ID: {existing_pq['id']}).")
            var['physicalQuantityUnit']['physicalQuantityId'] = existing_pq['id']  # Assign existing PQ ID
            
            # Check if the unit exists within the physical quantity
            existing_unit = check_existing_unit(existing_pq, unit_name)
            
            if existing_unit:
                var['physicalQuantityUnit']['unit'] = existing_unit['unit']  # Use the existing unit name
                var['physicalQuantityUnit']['id'] = existing_unit['id']    # Assign the existing unit ID
            else:
                # If unit doesn't exist, add it and update the PQ
                updated_pq = add_unit_to_existing_physical_quantity(
                    existing_pq['id'], pq_name, unit_name, token)
                
                # Retrieve the newly added unit ID and use it in the model
                new_unit = next((u for u in updated_pq['units'] if u['unit'] == unit_name), None)
                if new_unit:
                    var['physicalQuantityUnit']['unit'] = new_unit['unit']
                    var['physicalQuantityUnit']['id'] = new_unit['id']
                else:
                    logging.error(f"Failed to retrieve the new unit '{unit_name}' after adding it to PQ '{pq_name}'.")
        else:
            # If physical quantity doesn't exist, create a new one
            logging.info(f"Creating new physical quantity '{pq_name}'.")
            new_pq = create_physical_quantity(pq_name, unit_name, token)
            if new_pq:
                var['physicalQuantityUnit']['physicalQuantityId'] = new_pq['id']
                
                # Use the first unit returned in the newly created physical quantity
                if new_pq['units']:
                    new_unit = new_pq['units'][0]
                    var['physicalQuantityUnit']['unit'] = new_unit['unit']
                    var['physicalQuantityUnit']['id'] = new_unit['id']
                else:
                    logging.error(f"No units found in the newly created physical quantity '{pq_name}'.")
            else:
                logging.error(f"Failed to create physical quantity '{pq_name}'. Model import aborted.")
                return None  # Abort the process if the creation fails

    return model_data

# Create the model using the final updated model_data
def create_model(token, model_data):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    base_url = get_base_url()
    url = base_url + ENDPOINTS['computable_models']
    
    logging.info("Attempting to create/import the model.")
    response = requests.post(url, json=model_data, headers=headers)
    
    # Check for success (201 Created)
    if response.status_code == 201:
        logging.info("Model imported successfully!")
    # Handle other success responses (200 OK)
    elif response.status_code == 200:
        logging.info("Model updated or already existed.")
    elif response.status_code == 409:
        logging.error("A conflict occurred. The model might already exist.")
    elif response.status_code == 403:
        logging.error("Access denied. You do not have permission to import this model.")
    else:
        logging.error(f"Unexpected error. Status Code: {response.status_code}. Response: {response.content}")
