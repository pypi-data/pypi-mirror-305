import boto3
import io
import configparser
import pandas as pd
import logging
import psycopg2
from io import StringIO
import boto3
from botocore.client import Config
from io import BytesIO
from datetime import datetime
import os
import click
from boto3 import client
from typing import Any, BinaryIO
from pathlib import Path


# Define log directory and file
log_dir = Path.home() / 'log'
log_filename = f"powerflow-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Ensure the log directory exists
log_dir.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_dir / f"{log_filename}.log"),
        logging.StreamHandler()
    ],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger('botocore').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def display_logo():
    """Display ThinkLabs AI logo as ASCII art."""
    logo = """
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░       ░▒▓████████▓▒░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓██▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ™ 
                                                                Welcome!!!
    """
    click.secho(logo, fg='green', bold=True)

# Initialize S3 client
s3_client = boto3.client('s3')

# Function to download a file from S3 as bytes
def download_s3_file(bucket_name, file_key):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read()
        return io.BytesIO(file_content)  # Return as file-like object
    except Exception as e:
        logger.error(f"Error downloading file from S3: {e}")
        return None
    
def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def reshape_data(df, value_prefix):
        before, after = value_prefix.split('_')
        reshaped_data = []
        for _, row in df.iterrows():
            timestamp = row['Timestamp']   
            for col in df.columns[1:]:
                base_node, suffix = col.rsplit('.', 1)  
                if suffix == '1':
                    val_a = row[col]
                    val_b = None
                    val_c = None
                elif suffix == '2':
                    val_a = None
                    val_b = row[col]
                    val_c = None
                elif suffix == '3':
                    val_a = None
                    val_b = None
                    val_c = row[col]
                reshaped_data.append({
                    'Timestamp': timestamp,
                    'bus_name': base_node,
                    f'{before}_a_{after}': val_a,
                    f'{before}_b_{after}': val_b,
                    f'{before}_c_{after}': val_c
                })
        reshaped_df = pd.DataFrame(reshaped_data)
         
        reshaped_df = reshaped_df.groupby(['Timestamp', 'bus_name'], as_index=False).first()
        
        return reshaped_df

def reshape_and_merge_csv_data(p_csv, q_csv,uuid,feederid,created_at):   
   
    p_df = pd.read_csv(p_csv)
    q_df = pd.read_csv(q_csv)
    
    reshaped_p_df = reshape_data(p_df, 'p_kw')
    reshaped_q_df = reshape_data(q_df, 'q_kvar')
     
    merged_df = pd.merge(reshaped_p_df, reshaped_q_df, on=['Timestamp', 'bus_name'], how='outer')

    merged_df['uuid'] = uuid
    merged_df['feederid'] = feederid
    merged_df['created_at'] = created_at
    
    return merged_df

def get_secret(secret_name, region_name='us-west-2'):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        response = client.get_secret_value(SecretId=secret_name)
        return eval(response['SecretString'])  
    except client.exceptions.ResourceNotFoundException:
        logger.error("The requested secret was not found.")
    except client.exceptions.InvalidRequestException:
        logger.error("The request was invalid due to incorrect parameters.")
    except client.exceptions.InvalidParameterException:
        logger.error("The request had invalid params.")
    except Exception:
        logger.error("An error occurred while retrieving the secret. Check AWS settings or permissions.")

def load_dataframe_to_postgres(df, host_name ,db_name,schema_name, table_name, secret_name):
    secrets = get_secret(secret_name)
    if secrets is None:
        return
    dbname = db_name
    user = secrets['username']
    password = secrets['password']
    host = host_name
    port = 5432

    # Step 3: Establish the PostgreSQL connection
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = conn.cursor()
        output = StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        copy_sql = f"COPY {schema_name}.{table_name} FROM STDIN WITH CSV DELIMITER '\t' NULL ''"
        cursor.copy_expert(copy_sql, output)
        conn.commit()
        logger.info(f"Data loaded successfully into {schema_name}.{table_name}")
    except Exception as e:
        logger.error(f"Error: {e}")
        conn.rollback() 
    finally:
        cursor.close()
        conn.close()

def get_s3_object(bucket: str, key: str) -> BytesIO:
    s3_client = boto3.client('s3')
    rsp = s3_client.get_object(Bucket=bucket, Key=key)
    file_content = rsp['Body'].read()
    return BytesIO(file_content)    

def load_data_to_dataframe(file: BytesIO) -> pd.DataFrame:
    file.seek(0) 
    df = pd.read_csv(file)
    return df

def load_csv_to_postgres(csv_file, table_name, schema_name, database_name, host, secret_name):
    
    secrets = get_secret(secret_name)
    if secrets is None:
        return
    
    # Establish a connection to the PostgreSQL database
    try:
        conn = psycopg2.connect(
            host=host,
            database=database_name,
            user = secrets['username'],
            password = secrets['password'],
            port=5432
        )
        cur = conn.cursor()
        
        # Construct the full table name with schema
        full_table_name = f"{schema_name}.{table_name}"
        
        # Load data using the COPY command
        with open(csv_file, 'r') as f:
            cur.copy_expert(f"COPY {full_table_name} FROM STDIN WITH CSV HEADER", f)
        
        # Commit the transaction
        conn.commit()
        logger.info(f"Data successfully loaded into {full_table_name}")
    
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        conn.rollback()
    
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

def get_s3_client() -> Any:
    return client("s3")

def get_object(
    bucket: str,
    key: str,
    s3_client: Any = None,
) -> StringIO:
    if s3_client is None:
        s3_client = get_s3_client()

    rsp = s3_client.get_object(Bucket=bucket, Key=key)
    content = rsp["Body"].read().decode("utf-8")

    file = StringIO(content)
    return file