import requests
import os;

TARGET_URL = 'https://notify-api.line.me/api/notify'
TOKEN = os.environ['LINE_ACCESS_TOKEN']

def line_notify(message):
    response = requests.post(
    TARGET_URL,
    headers={
        'Authorization': 'Bearer ' + TOKEN
    },
    data={
        'message': message
    }
    )

    print(response.text)

line_notify("test from python")