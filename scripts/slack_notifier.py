import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_message(message):
    payload = {"text": message}
    requests.post(SLACK_URL, json=payload)
