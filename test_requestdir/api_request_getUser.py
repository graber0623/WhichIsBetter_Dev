import requests
import json

url = "http://127.0.0.1:8080/chatApp/user/get"

headers = {
    "Content-Type": "application/json"
}

temp = {
    "user_name":"jameskwak",
    "user_pass":"44455",
}

data = json.dumps(temp)

response = requests.get(url, headers=headers, data=data)

print("response: ", response)
print("response.text: ", response.text)

    # userName = params["user_name"]
    # userPass = params["user_pass"]
    # apiKey = params["chatgpt_api_key"] 