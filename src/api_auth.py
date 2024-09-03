from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import json


# Authenticate and create the Drive service
def authenticate(cofig, SCOPES):
    creds = None
    # Check if we have token.json for stored credentials
    if os.path.exists(cofig.token):
        creds = Credentials.from_authorized_user_file(cofig.token, SCOPES)
    # If there are no valid credentials available, request login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cofig.credentials, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use
        with open(cofig.token, 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

