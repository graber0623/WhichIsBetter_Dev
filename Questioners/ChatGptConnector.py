import sys
sys.path.append("/Users/sanglokkim/dev_env/WhichIsBetter_Dev")
import requests
from JDBCConnector.jdbcConnector import UserDatabase

class ChatGPTQuestioner:
    API_URL = "https://api.openai.com/v1/chat/completions"
    
    def __init__(self, username, password):
        self.api_key = self._fetch_api_key(username, password)
        
    def _fetch_api_key(self, username, password):
        try:
            userConnect = UserDatabase()
            api_key = userConnect.get_user(username, password)
            if api_key == "Invalid User or Password":
                raise ValueError("Invalid User or Password")
            return api_key
        except ValueError as ve:
            raise ValueError(f"Error in fetching API Key: {str(ve)}")
            
    def make_request(self, question):
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "gpt-4",
                "messages": [{"role": "user", "content": f"{question}"}],
                "temperature": 0.7
            }
        
            response = requests.post(self.API_URL, headers=headers, json=data)
            response.raise_for_status()
            
            response_json = response.json()
            return response_json['choices'][0]['message']['content']
        except requests.RequestException as e:
            raise ValueError(f"Error in making request to GPT-4 API: {str(e)}")
        except KeyError:
            raise ValueError("Unexpected response structure from GPT-4 API")
