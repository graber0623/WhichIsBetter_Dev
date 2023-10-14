
from datetime import datetime
import os
import requests
import json

url = "http://127.0.0.1:8080/chatApp/ask"

headers = {
    "Content-Type": "application/json"
}

temp = {
    "user_name":"graber1991",
    "user_pass":"123456",
    "question":"in python print('Hello')"
}

data = json.dumps(temp)

response = requests.post(url, headers=headers, data=data)

print("response: ", response)
print("response.text: ", response.text)

