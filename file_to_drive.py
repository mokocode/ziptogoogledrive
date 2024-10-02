import os
import zipfile
from datetime import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# File paths
LOCAL_FILE_PATH = '/path/to/local/file'
ZIP_FILE_PATH = '/path/to/local/zipfile_{timestamp}.zip'

# Google Drive details
SCOPES = ['https://www.googleapis.com/auth/drive.file']
TOKEN_FILE = 'token.json'
FOLDER_ID = 'your_google_drive_folder_id'

def zip_file():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_path = ZIP_FILE_PATH.format(timestamp=timestamp)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(LOCAL_FILE_PATH, os.path.basename(LOCAL_FILE_PATH))
    return zip_path

def upload_to_drive(zip_path):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {
        'name': os.path.basename(zip_path),
        'parents': [FOLDER_ID]
    }
    media = MediaFileUpload(zip_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'File ID: {file.get("id")}')

def main():
    zip_path = zip_file()
    upload_to_drive(zip_path)
    
    # Clean up local zip file
    os.remove(zip_path)

if __name__ == "__main__":
    main()
