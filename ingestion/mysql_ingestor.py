import pandas as pd
import mysql.connector
from config.config import Config
from utils.gcs_ingestor import upload_to_gcs
import os

def fetch_data_from_mysql(query: str) -> pd.DataFrame:
    conn = mysql.connector.connect(
        host=Config.mysql_host,
        port=Config.mysql_port,
        user=Config.mysql_user,
        password=Config.mysql_password,
        database=Config.mysql_db,
    )
    df = pd.read_sql(query, con=conn)
    conn.close()
    return df

def export_and_upload_mysql_table(query: str, local_file: str, gcs_path: str):
    df = fetch_data_from_mysql(query)
    df.to_csv(local_file, index=False)
    upload_to_gcs(local_file, gcs_path)
    os.remove(local_file)
