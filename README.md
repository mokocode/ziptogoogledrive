
Python zip file or folder then upload to google drive automatically on a timeschedule.


Install the requirements using pip install -f requirements.txt

One is for single file 'file_to_drive.py' the other is for a folder ' folder_to_drive.py'

Before using the script, replace the placeholder values:

LOCAL_FILE_PATH: The path to the file you want to zip and upload
ZIP_FILE_PATH: The path where the zipped file will be created temporarily (including the {timestamp} placeholder)
TOKEN_FILE: The path to your Google Drive API token file
FOLDER_ID: The ID of the Google Drive folder where you want to upload the file

This script will now create zip files with names like "zipfile_20240103_145930.zip", making it easy to track when each file was created and uploaded.

Open crontab -e and add the following line:
0 2 * * * /usr/bin/python3 /path/to/your/script.py
change the path and time scedules to your liking, using https://crontab.guru



