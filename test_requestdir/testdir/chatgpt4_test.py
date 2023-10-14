import requests
import json

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = 'sk-' # Replace with your API key

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
     "model": "gpt-4",
     "messages": [{"role": "user", "content": "say 'hello sanglok"}],
     "temperature": 0.7
}

response = requests.post(API_URL, headers=headers, data=json.dumps(data))

response_json = response.json()


print(response_json['choices'][0]['message']['content'])




