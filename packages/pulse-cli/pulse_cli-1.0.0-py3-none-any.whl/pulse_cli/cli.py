import subprocess
import platform
import requests
import sys
import os
import shutil

def run_command(command):
    """Executes a command with sudo on Linux."""
    try:
        if platform.system() == 'Linux':
            subprocess.run(['sudo'] + command, check=True)
        else:
            print("This tool is designed to run systemctl commands on Linux only.")
            sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{' '.join(command)}' failed with error: {e}")
        sys.exit(1)

def download_and_replace_file(url, destination_path):
    """Downloads a file from a URL and writes it to the specified path."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(destination_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("File downloaded and replaced successfully.")
    except requests.RequestException as e:
        print(f"Error: Failed to download the file. {e}")
        sys.exit(1)

def pulse_refresh():
    """Stops, reloads, and starts the pulse service."""
    print("Refreshing the pulse service...")
    run_command(['systemctl', 'stop', 'pulse.service'])
    run_command(['systemctl', 'daemon-reload'])
    run_command(['systemctl', 'start', 'pulse.service'])
    print("Pulse service refreshed successfully.")

def pulse_update(download_url, destination_path):
    """Updates the pulse service by downloading and replacing a file."""
    print("Updating the pulse service...")
    run_command(['systemctl', 'stop', 'pulse.service'])
    download_and_replace_file(download_url, destination_path)
    run_command(['systemctl', 'daemon-reload'])
    run_command(['systemctl', 'start', 'pulse.service'])
    print("Pulse service updated successfully.")

def pulse_logs():
    """Displays the logs for the pulse service using journalctl."""
    print("Fetching logs for the pulse service...")
    try:
        subprocess.run(['sudo', 'journalctl', '-u', 'pulse.service', '--no-pager'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to fetch logs. {e}")
        sys.exit(1)

def pulse_stop():
    """Stops the pulse service."""
    print("Stopping the pulse service...")
    run_command(['systemctl', 'stop', 'pulse.service'])
    print("Pulse service stopped successfully.")

def pulse_status():
    """Displays the status of the pulse service."""
    print("Fetching the status of the pulse service...")
    try:
        subprocess.run(['systemctl', 'status', 'pulse.service'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to fetch status. {e}")
        sys.exit(1)

def pulse_remove():
    """Stops and removes the pulse service and deletes the command-line tool."""
    print("Removing the pulse service and command-line tool...")
    try:
        # Stop and disable the service
        run_command(['systemctl', 'stop', 'pulse.service'])
        run_command(['systemctl', 'disable', 'pulse.service'])

        # Remove the service file
        service_path = '/etc/systemd/system/pulse.service'
        if os.path.exists(service_path):
            print(f"Deleting the service file: {service_path}")
            os.remove(service_path)

        # Reload systemd daemon
        run_command(['systemctl', 'daemon-reload'])
        run_command(['systemctl', 'reset-failed'])

        # Delete the CLI tool (assuming it's installed via pip or directly)
        cli_path = shutil.which('pulse')
        if cli_path:
            print(f"Deleting the CLI tool: {cli_path}")
            os.remove(cli_path)
            # Optionally, remove the Python package with pip
            print("Uninstalling the Python package...")
            subprocess.run(['pip3', 'uninstall', '-y', 'pulse-cli'], check=False)
        else:
            print("CLI tool not found or already removed.")

        print("Pulse service and command-line tool removed successfully.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: pulse <command> [args...]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'refresh':
        pulse_refresh()
    elif command == 'update':
        if len(sys.argv) != 4:
            print("Usage: pulse update <download_url> <destination_path>")
            sys.exit(1)
        download_url = sys.argv[2]
        destination_path = sys.argv[3]
        pulse_update(download_url, destination_path)
    elif command == 'logs':
        pulse_logs()
    elif command == 'stop':
        pulse_stop()
    elif command == 'status':
        pulse_status()
    elif command == 'remove':
        pulse_remove()
    else:
        print("Unknown command. Available commands: refresh, update, logs, stop, status, remove")
        sys.exit(1)

if __name__ == '__main__':
    main()
