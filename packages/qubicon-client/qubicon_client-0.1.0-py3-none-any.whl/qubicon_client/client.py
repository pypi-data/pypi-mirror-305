import argparse
import logging
from qubicon_client.auth import login, logout, is_token_expired
from qubicon_client.functions.basic_functions import list_physical_quantities, list_models, get_model_details, create_model, update_model, delete_model
from qubicon_client.config import load_token, save_token, delete_token
from qubicon_client.config import set_base_url, get_base_url, SERVER_OPTIONS, TOKEN_EXPIRATION_SECONDS
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from qubicon_client.functions.import_functions import import_model_from_json
from qubicon_client.functions.interactive_functions import import_model_interactive
from qubicon_client.functions.export_functions import export_model_to_json
from qubicon_client.functions.process_functions import list_processes, list_process_channels, extract_process_data, get_date_from_user, get_process_details
import time

# Setup a Rich console for better formatting
console = Console()

logging.basicConfig(
    level=logging.INFO,  # Set the log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Set the log format
    handlers=[
        logging.FileHandler("import_model.log"),  # Log to a file
        logging.StreamHandler()  # Also log to the console (stdout)
    ]
)

def display_menu():
    """Display the interactive menu."""
    menu_table = Table(title="Qubicon API Client - Main Menu")
    menu_table.add_column("Option", justify="center")
    menu_table.add_column("Action", justify="left")
    menu_table.add_row("0", "Login")
    menu_table.add_row("1", "Log out")
    menu_table.add_row("2", "Exit")
    menu_table.add_row("3", "List all models")
    menu_table.add_row("4", "View model details")
    menu_table.add_row("5", "Import a new model")
    menu_table.add_row("6", "View physical quantities")
    menu_table.add_row("7", "Export a model to JSON")
    menu_table.add_row("8", "list all processes")
    menu_table.add_row("9", "list all channels for a process")
    menu_table.add_row("10", "Extract process data")
    
    console.print(Panel(menu_table, title="Choose an Action", expand=False))

def handle_login():
    """Handle the login process."""
    # Prompt for server choice and set the BASE_URL
    choose_server()  # Sets BASE_URL based on user choice
    username = Prompt.ask("Username")
    password = Prompt.ask("Password", password=True)

    console.print("[cyan]Attempting to log in...[/cyan]")
    token = login(username, password)

    if token:
        # Set expiration time 1 hour from now and save token and BASE_URL
        expiration_time = time.time() + TOKEN_EXPIRATION_SECONDS
        save_token(token, expiration_time)  # save_token includes both token and BASE_URL
        console.print("[green]Login successful![/green]")
        return token
    else:
        console.print("[red]Login failed. Please check your credentials and try again.[/red]")
        return None

def ensure_logged_in():
    """Ensure the user is logged in and the token and BASE_URL are valid. If not, prompt for login."""
    token, base_url = load_token()  # Load token and BASE_URL, checking expiration
    if not token or base_url is None:
        console.print("[yellow]Your session has expired or you are not logged in. Please log in.[/yellow]")
        return handle_login()  # Prompt login if token or BASE_URL is missing
    else:
        global BASE_URL
        BASE_URL = base_url  # Ensure BASE_URL is set globally
        return token  # Return the valid token


def interactive_mode(token):
    """Handle interactive mode with looping menu options."""
    while True:
        token = ensure_logged_in()  # Ensure token is valid before every operation

        display_menu()
        
        try:
            choice = Prompt.ask("\nEnter your choice (0-10)", choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        except ValueError:
            console.print("[red]Invalid input. Please enter a valid number between 0 and 6.[/red]")
            continue

        if choice == "0":
            if token:
                console.print("[yellow]You are already logged in. Please log out first to switch accounts.[/yellow]")
            else:
                token = handle_login()
        elif choice == "1":
            handle_logout()
            break  # Exit the loop after logout
        elif choice == "2":
            console.print("[green]Exiting the client. [/green]")
            break
        elif choice == "3":
            list_models(token)
        elif choice == "4":
            try:
                model_id = Prompt.ask("Enter the Model ID to view details", default="1")
                get_model_details(token, int(model_id))
            except ValueError:
                console.print("[red]Invalid Model ID. Please enter a valid number.[/red]")
        elif choice == "5":
            import_model_interactive()
        elif choice == "6":
            list_physical_quantities(token)
        elif choice == "7":
            try:
                model_id = Prompt.ask("Enter the Model ID to export to JSON", default="1")
                output_file = Prompt.ask("Enter the output file path", default="exported_model.json")
                export_model_to_json(int(model_id), output_file)
            except ValueError:
                console.print("[red]Invalid Model ID. Please enter a valid number.[/red]")  
        elif choice == "8":
            list_processes(token)
        elif choice == "9":
            try:
                process_id = Prompt.ask("Enter the Process ID to list channels", default="1")
                list_process_channels(token, int(process_id))
            except ValueError:
                console.print("[red]Invalid Process ID. Please enter a valid number.[/red]")
        elif choice == "10":
            interactive_extract_process_data(token)  
        else:
            console.print("[red]Invalid choice. Please enter a valid option.[/red]")
            continue

def interactive_extract_process_data(token):
    """Interactive process data extraction."""
    try:
        process_id = Prompt.ask("Enter the Process ID to extract data from", default="1")
        channels = list_process_channels(token, int(process_id))

        if channels:
            selected_channels = []
            channel_dict = {channel["id"]: channel for channel in channels}  # Create a dictionary of channels keyed by their ID
            while True:
                channel_id = Prompt.ask("Enter the Channel ID to extract (or 'ENTER' to finish)")
                if channel_id.lower() == '':
                    break
                channel_id = int(channel_id)
                if channel_id in channel_dict:
                    selected_channels.append({
                        "id": channel_id,
                        "type": channel_dict[channel_id]["type"]  # Fetching type directly from the channel data
                    })
                else:
                    console.print(f"[red]Channel ID {channel_id} not found. Please try again.[/red]")

            # Fetch startDate and endDate from the process details automatically
            start_date, end_date = get_process_details(token, int(process_id))
            if end_date is None:
                # If the process is still running, set endDate to 30 mins after startDate
                end_date = start_date + (30 * 60 * 1000)  # Add 30 minutes in milliseconds
            
            granularity = Prompt.ask("Enter the granularity (in ms)", default="148")
            
            try:
                while True:
                    output_format = Prompt.ask("\nEnter your format of choice (0: json, 1: CSV)", choices=["0", "1"])
                    if output_format in ["0", "1"]:
                        break
                    else:
                        console.print("[red]Invalid input. Please enter a valid number between 0 and 1.[/red]")

                output_file = Prompt.ask("Enter the output file path", default="process_data.csv")
                extract_process_data(token, int(process_id), selected_channels, start_date, end_date, int(granularity), output_file, output_format)
            except ValueError as e:
                console.print("ERROR: ", e)

    except ValueError:
        console.print("[red]Invalid input. Please enter valid data.[/red]")

def choose_server():
    """Prompt the user to choose a server or provide a custom server URL."""
    console.print("[cyan]Choose a server to connect to:[/cyan]")
    console.print("1.", SERVER_OPTIONS["1"])
    console.print("2.", SERVER_OPTIONS["2"])

    choice = Prompt.ask("Enter 1, 2, or enter a custom URL", default="1")

    # Set BASE_URL based on predefined or custom choice
    if choice in ["1", "2"]:
        set_base_url(choice)  # Use predefined server option
    else:
        set_base_url(choice)  # Treat as a custom URL input

def handle_logout():
    """Handle the logout process."""
    console.print("[cyan]Logging out...[/cyan]")
    logout()  # Perform logout on the API side
    delete_token()  # Delete saved token locally
    console.print("[green]Successfully logged out.[/green]")

def handle_login(username=None, password=None, server=None):
    """Handle the login process, either interactively or in batch mode if credentials and server are provided."""
    if server:
        set_base_url(server)
    else:
        # Only prompt for server if not provided
        choose_server()

    if not username or not password:
        username = Prompt.ask("Username")
        password = Prompt.ask("Password", password=True)

    console.print("[cyan]Attempting to log in...[/cyan]")
    token = login(username, password)

    if token:
        expiration_time = time.time() + TOKEN_EXPIRATION_SECONDS
        save_token(token, expiration_time)
        console.print("[green]Login successful![/green]")
        return token
    else:
        console.print("[red]Login failed. Please check your credentials and try again.[/red]")
        return None

def batch_mode(args):
    """Handle batch mode operations without any prompts for full automation."""
    token = None

    if args.login:
        if not (args.username and args.password and args.server):
            console.print("[red]Username, password, and server URL are required for login in batch mode.[/red]")
            return
        token = handle_login(username=args.username, password=args.password, server=args.server)
        if not token:
            return

    else:
        token, base_url = load_token()
        if not token or base_url is None:
            console.print("[yellow]You are not logged in. Use --login with credentials and server to log in.[/yellow]")
            return
        set_base_url(base_url)  # Ensure server URL is loaded from saved configuration

    # Remaining batch mode commands
    if args.logout:
        handle_logout()
    elif args.list_models:
        console.print("[cyan]Listing all models...[/cyan]")
        list_models(token)
    elif args.model_id:
        console.print(f"[cyan]Fetching details for Model ID: {args.model_id}...[/cyan]")
        get_model_details(token, args.model_id)
    elif args.import_model:
        if not args.import_model_path:
            console.print("[red]File path required for importing a model in batch mode.[/red]")
            return
        console.print(f"[cyan]Importing model from '{args.import_model_path}'...[/cyan]")
        import_model_from_json(args.import_model_path)
    elif args.view_physical_quantities:
        console.print("[cyan]Viewing physical quantities...[/cyan]")
        list_physical_quantities(token)
    elif args.list_processes:
        console.print("[cyan]Listing all processes...[/cyan]")
        list_processes(token)
    elif args.process_id and args.list_channels:
        console.print(f"[cyan]Listing channels for Process ID {args.process_id}...[/cyan]")
        list_process_channels(token, args.process_id)
    elif args.process_id and args.extract_process_data:
        if not args.channel_ids:
            console.print("[red]Channel IDs are required to extract process data in batch mode.[/red]")
            return
        start_date, end_date = get_process_details(token, args.process_id)
        if end_date is None:
            end_date = start_date + (30 * 60 * 1000)
        granularity = args.granularity if args.granularity else 148
        output_format = args.output_format if args.output_format else "json"
        output_file = args.output_file if args.output_file else "process_data.json"
        selected_channels = [{'id': ch_id, 'type': 'ONLINE'} for ch_id in args.channel_ids]
        console.print(f"[cyan]Extracting data for channels in Process ID {args.process_id}...[/cyan]")
        extract_process_data(token, args.process_id, selected_channels, start_date, end_date, granularity, output_file, output_format)

def main():
    parser = argparse.ArgumentParser(description="Qubicon API Client")

    # Authentication arguments
    parser.add_argument('--login', action='store_true', help="Log in with username, password, and server")
    parser.add_argument('--logout', action='store_true', help="Log out and remove the saved token")
    parser.add_argument('--username', help="Username for login")
    parser.add_argument('--password', help="Password for login")
    parser.add_argument('--server', help="Server URL for login (required for batch mode login)")

    # Model CRUD arguments
    parser.add_argument('--list-models', action='store_true', help="List all models")
    parser.add_argument('--model-id', type=int, help="Model ID to view details")
    parser.add_argument('--import-model', action='store_true', help="Import a new model from JSON")
    parser.add_argument('--import-model-path', help="File path for importing a model")
    parser.add_argument('--view-physical-quantities', action='store_true', help="View all physical quantities")

    # Process-related arguments
    parser.add_argument('--list-processes', action='store_true', help="List all processes")
    parser.add_argument('--process-id', type=int, help="Specify a Process ID for other operations")
    parser.add_argument('--list-channels', action='store_true', help="List channels for a specified Process ID")
    parser.add_argument('--extract-process-data', action='store_true', help="Extract data for a specified process")

    # Data extraction arguments
    parser.add_argument('--channel-ids', nargs='+', type=int, help="List of Channel IDs to extract data from")
    parser.add_argument('--granularity', type=int, help="Granularity in milliseconds for data extraction")
    parser.add_argument('--output-format', choices=["json", "csv"], help="Output format: 'json' or 'csv'")
    parser.add_argument('--output-file', help="Output file path for extracted data")

    # Parse arguments
    args = parser.parse_args()

    # Check if any batch mode arguments are provided
    if any([
        args.login, args.logout, args.list_models, args.model_id, args.import_model, args.view_physical_quantities,
        args.list_processes, args.process_id, args.list_channels, args.extract_process_data
    ]):
        batch_mode(args)  # Corrected call with only args
    else:
        # If no batch mode commands are provided, switch to interactive mode
        token = load_token()
        interactive_mode(token)

if __name__ == '__main__':
    main()
