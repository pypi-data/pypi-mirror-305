import requests
import os
import json
from telesm.env import Env


class NoApiKeyException(Exception):
    def __init__(self):
        super().__init__("No Api Key could be found to connect to OpenAI")


class OpenAiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.openai.com/v1/chat/completions'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_word_definition(self, word):
        prompt = f"Provide the definition and couple of examples of the word '{
            word}'. Response in json."

        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 250
        }

        response = requests.post(self.api_url, headers=self.headers, json=data)
        response_json = response.json()

        if response.status_code == 200:
            content = json.loads(
                response_json['choices'][0]['message']['content'])
            return content["definition"], content["examples"], 200
        else:
            return response.json(), None, response.status_code


class Ai:
    def __init__(self):
        self.init_api_key()
        self.client = OpenAiClient(self.api_key)

    def init_api_key(self):
        Env().load_env()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise NoApiKeyException()
        self.api_key = api_key

    def get_definition(self, word):
        return self.client.get_word_definition(word)
