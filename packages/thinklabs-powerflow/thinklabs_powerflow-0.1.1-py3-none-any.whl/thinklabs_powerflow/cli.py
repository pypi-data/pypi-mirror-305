import click
import requests
from pathlib import Path
import pandas as pd
import os
from utils import *
import certifi

ROOT = Path(__file__).parent

class ClickFileReader:
    """
    A file-like object wrapper that adds a colored progress bar using Click.
    """
    def __init__(self, file_path, desc, color='green'):
        self.file = open(file_path, 'rb')
        self.total_size = os.path.getsize(file_path)
        self.read_size = 0
        self.desc = desc
        self.color = color

    def read(self, size=-1):
        data = self.file.read(size)
        self.read_size += len(data)
        return data

    def close(self):
        self.file.close()

def send_files_to_api(api_url, file_p, file_q, system):
    """
    Sends P and Q files to the specified API with system information.
    """
    payload = {'system': system}

    try:
        # Create file readers with Click progress bars
        p_file_reader = ClickFileReader(file_p, desc='Uploading Active Power', color='cyan')
        q_file_reader = ClickFileReader(file_q, desc='Uploading Reactive Power', color='yellow')

        # Define Click progress bar for P file
        with click.progressbar(
            length=p_file_reader.total_size,
            label=click.style(p_file_reader.desc, fg=p_file_reader.color),
            fill_char=click.style('█', fg=p_file_reader.color),
        ) as bar_p:
            while True:
                chunk = p_file_reader.read(1024)
                if not chunk:
                    break
                bar_p.update(len(chunk))

        # Define Click progress bar for Q file
        with click.progressbar(
            length=q_file_reader.total_size,
            label=click.style(q_file_reader.desc, fg=q_file_reader.color),
            fill_char=click.style('█', fg=q_file_reader.color),
        ) as bar_q:
            while True:
                chunk = q_file_reader.read(1024)
                if not chunk:
                    break
                bar_q.update(len(chunk))

        files = {
            'p': ('p.csv', open(file_p, 'rb'), 'text/csv'),
            'q': ('q.csv', open(file_q, 'rb'), 'text/csv')
        }

        # Make the API request with file upload
        response = requests.post(api_url, data=payload, files=files, verify=certifi.where())

        # Close file readers
        p_file_reader.close()
        q_file_reader.close()

        if response.status_code == 200:
            click.echo(click.style(f"Success: {response.json()}", fg='green'))
            return response.json()
        else:
            click.echo(click.style(f"Failed with status code {response.status_code}.", fg='red'))
            click.echo(click.style(f"Error: {response.text}", fg='red'))
            return None

    except Exception as e:
        click.echo(click.style(f"Error sending files to API: {e}", fg='red'))
        return None

def process_files(p_file, q_file):
    """
    Process P and Q files by filtering data based on the 'Timestamp' column.
    """
    output_folder = ROOT / "data"
    output_folder.mkdir(parents=True, exist_ok=True)

    # Read and filter P file
    p_df = pd.read_csv(p_file)
    p_df["Timestamp"] = pd.to_datetime(p_df["Timestamp"])
    p_df = p_df[p_df["Timestamp"].dt.minute == 0]
    p_file_processed = output_folder / "PNET.csv"
    p_df.to_csv(p_file_processed, index=False)

    # Read and filter Q file
    q_df = pd.read_csv(q_file)
    q_df["Timestamp"] = pd.to_datetime(q_df["Timestamp"])
    q_df = q_df[q_df["Timestamp"].dt.minute == 0]
    q_file_processed = output_folder / "QNET.csv"
    q_df.to_csv(q_file_processed, index=False)

    return p_file_processed, q_file_processed
display_logo()
@click.command()
@click.option('--system', prompt='Enter system type (e.g., small or large)', help='System type for prediction')
@click.option('--p-file', prompt='Enter P file path(Active Power)', type=click.Path(exists=True, readable=True), help='Path to the P file')
@click.option('--q-file', prompt='Enter Q file path(Reactive Power)', type=click.Path(exists=True, readable=True), help='Path to the Q file')
def main(system, p_file, q_file):
    """
    CLI to process P and Q files and send them to the API.
    """    

    click.echo(click.style(f"System: {system}", fg='cyan'))
    click.echo(click.style(f"Active Power(csv): {p_file}", fg='cyan'))
    click.echo(click.style(f"Reactive Power(csv): {q_file}", fg='cyan'))

    click.echo(click.style("Processing files...", fg='yellow'))
    p_file_processed, q_file_processed = process_files(p_file, q_file)
    click.echo(click.style("Files processed successfully.", fg='green'))

    api_url = "https://dev.ext.thinklabs.ai/v1/api/bulk_predict"
    click.echo(click.style(f"Sending files to API at {api_url}...", fg='cyan'))

    response_data = send_files_to_api(api_url, p_file_processed, q_file_processed, system)

    if response_data:
        uuid_value = response_data.get('uuid')
        created_at_value = response_data.get('created_at')
        click.echo(click.style(f"Inference request submitted at {created_at_value}, Request ID: {uuid_value}", fg='green'))
    else:
        click.echo(click.style("Failed to get a valid response from the API.", fg='red'))

if __name__ == "__main__":       
    main()
