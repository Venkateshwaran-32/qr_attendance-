import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Google Sheets details
SPREADSHEET_ID = "1BfJZ7mtHJTYp6PxLFeXICBAstcZwDEHzY8IkxWHiads"
RANGE_NAME = "Sheet1!A:D"

# Function to log data to Google Sheets
def log_to_sheet(user_name, user_id, location, timestamp):
    # Dynamically resolve the path to credentials.json
    credentials_path = os.path.join(os.path.dirname(__file__), "credentials.json")
    
    # Authenticate using the credentials.json file
    creds = Credentials.from_service_account_file(
        credentials_path, scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build('sheets', 'v4', credentials=creds)

    # Data to append (row format)
    values = [[
        user_name, 
        user_id, 
        f"{location['latitude']}, {location['longitude']}",  # Combine latitude and longitude into a single string
        timestamp
    ]]
    body = {"values": values}

    # Append data to the specified range in Google Sheets
    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()

    print(f"{result.get('updates').get('updatedCells')} cells updated.")




# 1BfJZ7mtHJTYp6PxLFeXICBAstcZwDEHzY8IkxWHiads


