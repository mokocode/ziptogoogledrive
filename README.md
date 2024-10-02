Install the requirements using pip install -f requirements.txt

Before using the script, replace the placeholder values:

LOCAL_FILE_PATH: The path to the file you want to zip and upload
ZIP_FILE_PATH: The path where the zipped file will be created temporarily (including the {timestamp} placeholder)
TOKEN_FILE: The path to your Google Drive API token file
FOLDER_ID: The ID of the Google Drive folder where you want to upload the file

This script will now create zip files with names like "zipfile_20240103_145930.zip", making it easy to track when each file was created and uploaded.

Add to cronjob using crontab -e
To change schedule, use https://crontab.guru

