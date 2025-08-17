import os
from config.config import Config
from utils.gcs_ingestor import upload_to_gcs

def upload_logs():
    log_dir = Config.log_folder_path
    print(f"Log folder path: {log_dir}")

    found_any = False
    for root, _, files in os.walk(log_dir):
        print(f"Scanning: {root}, files: {files}")
        for file in files:
            found_any = True
            print(f"Found file: {file}")
            local_path = os.path.join(root, file)
            rel_path = os.path.relpath(local_path, log_dir)
            gcs_path = f"careplus_logs/careplus_logs_raw/{rel_path}"
            print(f"Uploading {local_path} → {gcs_path}")
            upload_to_gcs(local_path, gcs_path)

    if not found_any:
        print("⚠️ No files found in the log folder.")


