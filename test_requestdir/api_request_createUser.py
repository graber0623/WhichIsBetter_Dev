import requests
import json

url = "http://127.0.0.1:8080/chatApp/user/create"

headers = {
    "Content-Type": "application/json"
}

temp = {
    "user_name":"graber1991",
    "user_pass":"123456",
    "chatgpt_api_key":"s"
}

data = json.dumps(temp)

response = requests.put(url, headers=headers, data=data)

print("response: ", response)
print("response.text: ", response.text)

    # userName = params["user_name"]
    # userPass = params["user_pass"]
    # apiKey = params["chatgpt_api_key"] 