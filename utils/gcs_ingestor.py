from google.cloud import storage
from config.config import Config
import os

def upload_to_gcs(local_path: str ,gcs_path: str) -> None:
    storage_client = storage.Client.from_service_account_json(Config.google_application_creds)
    bucket = storage_client.bucket(Config.gcs_bucket_name)
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} to gs://{Config.gcs_bucket_name}/{gcs_path}")