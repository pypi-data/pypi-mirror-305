
import os
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
from rich.console import Console
import logging
from qubicon_client.functions.import_functions import import_model_from_json

console = Console()

def import_model_interactive():
    """Handle the process of importing a model interactively and professionally."""
    try:
        # Prompt user for the file path dynamically
        file_path = Prompt.ask("Enter the path to the JSON file")

        # Check if file exists and has the correct .json extension
        if not os.path.exists(file_path):
            console.print(f"[red]Error: File '{file_path}' does not exist. Please check the path and try again.[/red]")
            return
        if not file_path.endswith(".json"):
            console.print("[red]Invalid file format. Only JSON files are supported.[/red]")
            return

        # Confirm with the user before proceeding
        confirmation = Prompt.ask(f"[yellow]You are about to import '{file_path}'. Proceed?[/yellow] (yes/no)", choices=["yes", "no"])
        if confirmation == "no":
            console.print("[blue]Import canceled by user.[/blue]")
            return

        # Start the import process with a spinner for feedback
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
            task = progress.add_task("Importing model...", start=False)
            progress.start_task(task)

            # Call the import function
            import_model_from_json(file_path)

            progress.update(task, description="[green]Import completed successfully!")
            progress.stop_task(task)

    except FileNotFoundError as e:
        console.print(f"[red]File not found: {e}. Please enter a valid path to the JSON file.[/red]")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        console.print(f"[red]Error: {e}[/red]")

import logging
from qubicon_client.auth import login, load_token

def perform_login():
    """
    Prompts the user for login credentials and performs the login.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")
    token = login(username, password)
    
    if not token:
        logging.error("Login failed. Please check your credentials.")
        return None
    
    logging.info("Login successful!")
    return token

def check_login(response_status_code, token):
    """
    Checks if the login token is expired or invalid and prompts the user to log in again.
    If the token is invalid, the function will automatically trigger the login process.
    """
    if response_status_code == 401:  # Unauthorized status code
        logging.warning("Token expired or invalid. Please log in again.")
        return perform_login()
    return token
