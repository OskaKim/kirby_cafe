import requests
import os;

TARGET_URL = 'https://notify-api.line.me/api/notify'
TOKEN = 'NEeiey4ymAoPfEO199Dm1p4RKtPVtenHNxi7FQb39Bz'

def line_notify(message):
    response = requests.post(
    TARGET_URL,
    headers={
        'Authorization': 'Bearer ' + TOKEN
    },
    data={
        "type": "text",
        "message": message,
        "imageThumbnail": "https://github.com/OskaKim/kirby_cafe/blob/main/kirby.jpg",
    }   
    )

    print(response.text)

line_notify("テスト")