import requests
import logging
from tabulate import tabulate
from qubicon_client.config import get_base_url, load_token
from rich.console import Console
from rich.prompt import Prompt
from datetime import datetime
import json
import pandas as pd

ENDPOINTS = {
    'processes': '/api/processes?size=90&sort=lastUsageDate,desc&search=&gmp=false&archivedOrWillBeArchived=false&partOfExperiment=false',
    'process_channels': '/api/processes/{process_id}/channels?sort=virtualEquipmentName',
    'multiplex_data': '/api/charts/multiplex-data-channels'
}

console = Console()

def list_processes(token):
    """List all available processes in a tabular format."""
    base_url = get_base_url()
    url = base_url + ENDPOINTS['processes']
    headers = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        processes = response.json().get('content', [])

        if processes:
            table = []
            for process in processes:
                table.append([
                    process['id'],
                    process['name'],
                    process['status'],
                    process['sensorCount'],
                    process['onlineSensorCount'],
                    process['offlineSensorCount'],
                    process['startDate'],
                    process['endDate']
                ])
            
            # Display processes in tabular format
            print(tabulate(table, headers=[
                "ID", "Process Name", "Status", "Total Sensors", 
                "Online Sensors", "Offline Sensors", "Type", 
                "GMP Enabled", "Simulated"
            ]))
        else:
            logging.error("No processes available or invalid response format.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching processes: {e}")

def list_process_channels(token, process_id):
    """List all available channels for a specific process in a tabular format."""
    base_url = get_base_url()
    url = base_url + ENDPOINTS['process_channels'].format(process_id=process_id)
    headers = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        channels = response.json()

        if channels:
            table = []
            for channel in channels:
                table.append([
                    channel['id'],
                    channel['name'],
                    channel['type'],
                    channel['nodeType'],
                    channel['physicalQuantityUnit']['name'],
                    channel['physicalQuantityUnit']['unit'],
                    channel['dataPresentationType'],
                    channel['equipmentLabel']
                ])

            # Display channels in a tabular format
            print(tabulate(table, headers=[
                "ID", "Channel Name", "Type", "Node Type", "Physical Quantity", 
                "Unit", "Data Presentation", "Equipment Label"
            ]))
        else:
            logging.error("No channels available or invalid response format.")
        return channels
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching channels: {e}")
        return None

# function to extract and save a process' data


def extract_process_data(token, process_id, selected_channels, start_date, end_date, granularity, output_file, output_format="json"):
    """Extracts process data for the selected channels and saves it to JSON or CSV format."""
    base_url = get_base_url()
    url = base_url + ENDPOINTS['multiplex_data']
    collected_data = []
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    for channel in selected_channels:
        # Prepare payload for individual channel
        payload = {
            "channels": [
                {
                    "id": channel["id"],
                    "type": "ONLINE",
                    "startDate": start_date,
                    "endDate": end_date,
                    "granularity": granularity
                }
            ]
        }

        try:
            # Perform POST request to fetch the data
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad HTTP responses

            # Store successful channel data
            channel_data = response.json()
            for entry in channel_data['channels']:
                for value in entry['value']:
                    collected_data.append({
                        "time": value['time'],  # Time is the first column now
                        "channel_id": entry['key']['id'],
                        "channel_type": "ONLINE",
                        "value": value['value']
                    })
            logging.info(f"Successfully fetched data for channel {channel['id']}")

        except requests.exceptions.HTTPError as e:
            logging.error(f"Error fetching data for channel {channel['id']}: {e}")
            continue  # Skip this channel and proceed to the next

        except Exception as e:
            logging.error(f"Unexpected error for channel {channel['id']}: {e}")
            continue

    # Save the collected data based on the desired output format
    if collected_data:
        df = pd.DataFrame(collected_data)

        if output_format == "0":
            # Save as JSON
            with open(output_file, 'w') as f:
                json.dump(collected_data, f, indent=4)
            logging.info(f"Process data successfully written to {output_file} as JSON")
        
        elif output_format == "1":
            # Pivot to have channel_id as columns, time as rows, and values as cells
            df_pivot = df.pivot(index="time", columns="channel_id", values="value")
            
            # Save to CSV
            df_pivot.to_csv(output_file)
            logging.info(f"Process data successfully written to {output_file} as CSV")

    else:
        logging.error("No valid data to write. All channel requests failed.")

def get_date_from_user(prompt_message, default_timestamp):
    """Prompt the user for a date and return the timestamp."""
    user_input = Prompt.ask(prompt_message, default=default_timestamp)
    try:
        date_object = datetime.strptime(user_input, '%Y-%m-%d %H:%M:%S')
        return int(date_object.timestamp() * 1000)  # Convert to milliseconds
    except ValueError:
        console.print("[red]Invalid date format. Please use YYYY-MM-DD HH:MM:SS format.[/red]")
        return get_date_from_user(prompt_message, default_timestamp)
    
def get_process_details(token, process_id):
    """Fetch the process startDate and endDate automatically."""
    base_url = get_base_url()
    url = f"{base_url}/api/processes/{process_id}"
    headers = {'Authorization': f'Bearer {token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        process_data = response.json()

        start_date = process_data.get('startDate')
        end_date = process_data.get('endDate')

        if end_date is None:
            # If the process is still running, set the end date to 30 minutes after the start date
            end_date = start_date + (30 * 60 * 1000)  # 30 minutes in milliseconds

        return start_date, end_date
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching process details: {e}")
        return None, None