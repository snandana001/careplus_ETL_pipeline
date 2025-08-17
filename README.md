This project ingests data from:
- ✅ A MySQL database containing support ticket data
- ✅ A local folder of log files

It uploads the cleaned data to Google Cloud Storage (GCS), organized in a structured data lake format.

## Features

- Modular Python code
- `.env` config support
- MySQL to GCS CSV upload
- Local logs to GCS folder upload
- Clean and production-ready structure