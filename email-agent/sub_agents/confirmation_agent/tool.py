import os
import base64
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

def send_mail_(recipient_email:str, subject:str, body:str):
    """
    Sends the mail to the recipient give the `to` email address, `subject` for the mail and `body` for the mail.

    Args:
        recipient_email (str): The recipient mail id (e.g., abcd@gmail.com).
        subject (str): The subject for the mail.
        body (str): The body for the mail.

    Returns:
        str: Success or Error message for the mail sent.
    """
    try:
        service = authenticate_gmail()
        user_id = "me"
        message = create_message(
            to=recipient_email, 
            subject=subject, 
            message_text=body
        )
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"Message Id: {sent_message['id']}")
        return f"Successfully sent your mail to {recipient_email}"
    except Exception as e:
        print(f"Error sending the mail to {recipient_email}: {e}")
        return f"Error sending the mail!!"

def send_mail(state: dict):
    """
    Sends the mail to the recipient give the `to` email address, `subject` for the mail and `body` for the mail.

    Args:
        state (dict): The state shared by the agent
    Returns:
        str: Success or Error message for the mail sent.
    """
    
    recipient_email = state.get("recipient_email_id")
    subject = state.get("draft_subject")
    body = state.get("draft_body")
    
    return send_mail_(recipient_email, subject, body)