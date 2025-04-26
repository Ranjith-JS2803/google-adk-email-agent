import os
import base64
import json
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_message(to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    return {'raw': raw.decode()}

def send_mail(to, subject, body):
    service = authenticate_gmail()
    user_id = "me"
    message = create_message(
        to=to, 
        subject=subject, 
        message_text=body
    )    
    sent_message = service.users().messages().send(userId=user_id, body=message).execute()
    print(f"Message Id: {sent_message['id']}")
    return f"Successfully sent your mail to {to}"

if __name__ == '__main__':
    to = "ranjithjs28@gmail.com"
    subject = "Testing Gmail API"
    body = "Hello, this is a test email sent using Gmail API!"
    send_mail(to, subject, body)