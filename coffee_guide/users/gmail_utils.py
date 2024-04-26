import base64
import os

from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from googleapiclient.discovery import build
from coffee_guide.settings import BASE_DIR
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.send", "https://www.googleapis.com/auth/gmail.compose"]

SERVICE_ACCOUNT_FILE = f"{BASE_DIR}/users/credentials_copy.json"
TOKEN = f"{BASE_DIR}/../token.json"


def send_email(sender, to, subject, message):
    email_message = create_message(sender, to, subject, message)
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                SERVICE_ACCOUNT_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    print(creds, "creds")
    service = build("gmail", "v1", credentials=creds)
    print(service, "service")
    send_message(service, "me", email_message)


def create_message(sender, to, subject, message_text):
    print(message_text, "message_text", *to, "to", sender, "sender")
    message = EmailMessage()
    message.set_content(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": encoded_message}


def send_message(service, user_id, message):
    try:
        sent_message = service.users().messages().send(
            userId=user_id,
            body=message
        ).execute()
        print("Message Id: %s" % sent_message["id"])
        return sent_message
    except Exception as e:
        print("An error occurred: %s" % e)
