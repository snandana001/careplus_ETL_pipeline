from ingestion.mysql_ingestor import export_and_upload_mysql_table
from ingestion.log_uploader import upload_logs
from utils.gcs_ingestor import upload_to_gcs

def main():
    # Example: Export user table
    query = "SELECT * FROM support_tickets ;"
    export_and_upload_mysql_table(query, "careplus_tickets.csv", "careplus_tickets/careplus_tickets_raw/careplus_tickets.csv")

    # Upload log files
    #upload_logs()

if __name__ == "__main__":
    main()
