import os
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# set the ID of the Google Docs file
doc_id = "YOUR_GOOGLE_DOCS_FILE_ID"

# set the path of the local .txt file
txt_file_path = "PATH_TO_LOCAL_TXT_FILE"

# authenticate and create the Drive API client
creds, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/drive"]
)
service = build("drive", "v3", credentials=creds)

# read the content of the local .txt file
with open(txt_file_path, "r") as f:
    txt_content = f.read()

# insert the text into the Google Docs file
try:
    doc_service = build("docs", "v1", credentials=creds)
    requests = [
        {
            "insertText": {
                "location": {"index": 1},
                "text": txt_content,
            }
        }
    ]
    result = doc_service.documents().batchUpdate(
        documentId=doc_id, body={"requests": requests}
    ).execute()
    print("Text inserted successfully.")
except HttpError as error:
    print(f"An error occurred: {error}")

    
# Note that you will need to replace YOUR_GOOGLE_DOCS_FILE_ID with the ID of your Google Docs file, 
# and PATH_TO_LOCAL_TXT_FILE with the path of your local .txt file. 
# You will also need to have the google-auth and google-api-python-client libraries installed.
