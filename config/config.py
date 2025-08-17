import os 
from dotenv import load_dotenv

load_dotenv()

class Config():
    mysql_host=os.getenv("mysql_host")
    mysql_port=int(os.getenv("mysql_port",3306))
    mysql_user=os.getenv("mysql_user")
    mysql_password=os.getenv("mysql_psswd")
    mysql_db=os.getenv("mysql_db")

    google_application_creds=os.getenv("google_app_credentials")
    gcs_bucket_name=os.getenv("gcs_bucket_name")

    log_folder_path=os.getenv("log_folder_path")