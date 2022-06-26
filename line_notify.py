import requests
import os;

TARGET_URL = 'https://notify-api.line.me/api/notify'
TOKEN = os.environ['LINE_ACCESS_TOKEN']

def line_notify(message):
    requests.post(
    TARGET_URL,
    headers={
        'Authorization': 'Bearer ' + TOKEN
    },
    data={
        "type": "text",
        "message": message
    }   
    )
