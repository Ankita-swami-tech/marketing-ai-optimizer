import os
import requests

SLACK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_message(message):
    if not SLACK_URL:
        print("⚠ Slack webhook not configured. Message:")
        print(message)
        return

    payload = {"text": message}

    try:
        requests.post(SLACK_URL, json=payload, timeout=5)
    except Exception as e:
        print("⚠ Slack notification failed (network issue)")
        print(message)
