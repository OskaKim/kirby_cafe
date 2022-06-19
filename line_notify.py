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
        "type": "text",
        "message": message,
        #"imageThumbnail": "https://raw.githubusercontent.com/OskaKim/kirby_cafe/main/kirby.jpg",
        #"imageFullsize": "https://raw.githubusercontent.com/OskaKim/kirby_cafe/main/kirby.jpg",
    }   
    )

    print(response.text)