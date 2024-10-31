import requests
import logging
from tabulate import tabulate
from qubicon_client.config import load_token, get_base_url

ENDPOINTS = {
    'computable_models': '/api/computable-models?search=&size=50&sort=updateDate,desc&page=0&statuses=DRAFT,RELEASED',
    'single_model': '/api/computable-models/{model_id}?deleted=false',
    'physical_quantities': '/api/physical-quantities',
    'specific_physical_quantity': '/api/physical-quantities/{id}'
}

def list_physical_quantities(token):
    base_url = get_base_url()
    url = base_url + ENDPOINTS['physical_quantities']
    headers = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        quantities = response.json()

        # Check if the response contains physical quantities
        if isinstance(quantities, list) and len(quantities) > 0:
            table = []
            for pq in quantities:
                # Loop through each unit for the current physical quantity
                for unit in pq.get('units', []):
                    table.append([
                        pq['id'],                   # Physical Quantity ID
                        pq['name'],                 # Physical Quantity Name
                        pq['status'],               # Physical Quantity Status
                        unit['id'],                 # Unit ID
                        unit['unit'],               # Unit Name
                        unit.get('status', '-')      # Unit Status (with default '-')
                    ])

            # Print the table with headers including the Unit ID and Unit Name
            print(tabulate(table, headers=["PQ ID", "Physical Quantity", "PQ Status", "Unit ID", "Unit Name", "Unit Status"]))
        else:
            logging.error("Unexpected response format or no physical quantities available.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching physical quantities: {e}")

def list_models(token):
    base_url = get_base_url()
    url = base_url + ENDPOINTS['computable_models']
    headers = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        models = response.json()
        
        if 'content' in models:
            table = [[m['id'], m['kpiName'], m['status']] for m in models['content']]
            print(tabulate(table, headers=["ID", "KPI Name", "Status"]))
        else:
            logging.error("Unexpected response format.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching models: {e}")

def get_model_details(token, model_id):
    base_url = get_base_url()
    url = base_url + ENDPOINTS['single_model'].format(model_id=model_id)
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        model = response.json()
        
        print(f"Model Details for ID {model.get('id')}:")
        print(f"Name: {model.get('kpiName')}")
        print(f"Abbreviation: {model.get('abbr')}")
        print(f"Status: {model.get('status')}")
        print(f"Engine Type: {model.get('engineType')}")
        print(f"Calculation Style: {model.get('calculationStyle')}")
        
        # Display inputs
        print("\nInputs:")
        for input_item in model.get('inputs', []):
            print(f"  - {input_item['name']} ({input_item['physicalQuantityUnit']['unit']})")
        
        # Display outputs
        print("\nOutputs:")
        for output_item in model.get('outputs', []):
            print(f"  - {output_item['name']} ({output_item['physicalQuantityUnit']['unit']})")
        
        print("\nScript:\n", model.get('script', 'No script available'))
        print("-" * 50)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching model details: {e}")

# Placeholder functions for future CRUD operations
def create_model(token):
    """Placeholder for creating a model."""
    logging.info("Creating model... (functionality to be added)")

def update_model(token, model_id):
    """Placeholder for updating a model."""
    logging.info(f"Updating model with ID {model_id}... (functionality to be added)")

def delete_model(token, model_id):
    pass
